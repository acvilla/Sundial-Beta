"""Core CALC_Modulator Calculator Package

Calculator functions are pulled by using their names.
Calculator functions must start with "calc_", if they are to be consumed by the framework.
    Or they should be returned by overriding the function:
        def getCalculationList(self):
"""

#import math
from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pyradioconfig.parts.common.calculators.calc_utilities import CALC_Utilities
from enum import Enum
from pyradioconfig.pycalcmodel import ModelVariableFormat, CreateModelVariableEnum

class CALC_Modulator(ICalculator):

    """
    Init internal variables
    """
    def __init__(self):
        self._major = 1
        self._minor = 0
        self._patch = 0

    def buildVariables(self, model):
        """Populates a list of needed variables for this calculator

        Args:
            model (ModelRoot) : Builds the variables specific to this calculator
        """

        # symbol_encoding
        var = self._addModelVariable(model, 'symbol_encoding', Enum, ModelVariableFormat.DECIMAL, 'Symbol Encoding Options')
        member_data = [
            ['NRZ',        0, 'Non Return Zero Coding'],
            ['Manchester', 1, 'Manchester Coding'],
            ['DSSS',       2, 'Direct Sequence Spread Spectrum Coding'],
        ]
        var.var_enum = CreateModelVariableEnum(
            'SymbolEncodingEnum',
            'List of supported symbol encoding options',
            member_data)


        # symbol_encoding
        var = self._addModelVariable(model, 'manchester_mapping', Enum, ModelVariableFormat.DECIMAL, 'Manchester Code Mapping Options')
        member_data = [
            ['Default',  0, '0-bit corresponds to a 0 to 1 transition and 1-bit corresponds to 1 to 0 transition'],
            ['Inverted', 1, '0-bit corresponds to a 1 to 0 transition and 1-bit corresponds to 0 to 1 transition'],
        ]
        var.var_enum = CreateModelVariableEnum(
            'ManchesterMappingEnum',
            'List of supported Manchester Code options',
            member_data)


    def calc_tx_baud_rate_actual(self, model):
        """
        calculate actual TX baud rate from register settings

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        fxo = model.vars.xtal_frequency.value
        txbr_ratio = model.vars.txbr_ratio_actual.value
    
        tx_baud_rate = fxo / (8.0 * txbr_ratio)
    
        model.vars.tx_baud_rate_actual.value = tx_baud_rate

    #TODO: add support for ASK modulation
    def calc_modindex_value(self, model):
        """
        calculate MODINDEX value
        Equations from Table 5.25 in EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        fxo = model.vars.xtal_frequency.value * 1.0
        modformat = model.vars.modulation_type.value
        freq_dev_hz = model.vars.deviation.value * 1.0
        synth_res = model.vars.synth_res_actual.value
        shaping_filter_gain = model.vars.shaping_filter_gain_actual.value
        interpolation_gain = model.vars.interpolation_gain_actual.value

        if modformat == model.vars.modulation_type.var_enum.FSK2 or \
           modformat == model.vars.modulation_type.var_enum.FSK4:
            modindex = freq_dev_hz * 16.0 / (synth_res * shaping_filter_gain * interpolation_gain)

        elif modformat == model.vars.modulation_type.var_enum.OQPSK or \
             modformat == model.vars.modulation_type.var_enum.MSK:
            modindex = fxo / (synth_res * 2 * shaping_filter_gain * interpolation_gain)

        elif modformat == model.vars.modulation_type.var_enum.BPSK or \
             modformat == model.vars.modulation_type.var_enum.OOK or \
             modformat == model.vars.modulation_type.var_enum.DBPSK:
            modindex = 150.0 * 16 / (shaping_filter_gain * interpolation_gain)
        else:
            print "ERROR: %s modulation not yet supported!" % modformat
            return

        model.vars.modindex.value = modindex

    
    def calc_modindex_field(self, model):
        """
        convert desired modindex fractional value to MODINDEXM * 2^MODINDEXE
        Equations (5.13) of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        modindex = model.vars.modindex.value
    
        # convert fractional modindex into m * 2^e format
        m, e = CALC_Utilities().frac2exp(31, modindex)
    
        # MODEINDEXE is a signed value
        if e < 0:
            e += 32
    
        # verify number fits into register
        if m > 31:
            m = 31
    
        if e > 31:
            e = 31
    
        if m < 0:
            m = 0
    
        self._reg_write(model.vars.MODEM_MODINDEX_MODINDEXM,  int(m))
        self._reg_write(model.vars.MODEM_MODINDEX_MODINDEXE,  int(e))
    
    
    def calc_modindex_actual(self, model):
        """
        given register settings return actual MODINDEX as fraction
        Equations (5.13) of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        m = model.vars.MODEM_MODINDEX_MODINDEXM.value
        e = model.vars.MODEM_MODINDEX_MODINDEXE.value
    
        # MODEINDEXE is a signed value
        if e > 15:
            e -= 32
    
        model.vars.modindex_actual.value = 1.0 * m * 2**e
    
    
    def calc_modulation_index_actual(self, model):
        """
        calculate the actual modulation index for given PHY
        This is the traditional modulation index as 2 * deviation / baudrate
        the one above we call modindex and is specific value used by EFR32

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        baudrate_hz = model.vars.rx_baud_rate_actual.value
        tx_deviation = model.vars.tx_deviation_actual.value
    
        model.vars.modulation_index_actual.value = tx_deviation * 2.0 / baudrate_hz
    
    
    def calc_tx_freq_dev_actual(self, model):
        """
        given register setting return actual frequency deviation used in the modulator
        Using Equations in Table 5.25 of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        modformat = model.vars.modulation_type.value
        modindex = model.vars.modindex_actual.value
        synth_res = model.vars.synth_res_actual.value
        shaping_filter_gain = model.vars.shaping_filter_gain_actual.value
        interpolation_gain = model.vars.interpolation_gain_actual.value

        if modformat == model.vars.modulation_type.var_enum.FSK2 or \
           modformat == model.vars.modulation_type.var_enum.FSK4:
            freq_dev_hz = modindex * (synth_res * shaping_filter_gain * interpolation_gain) / 16.0
        else:
            freq_dev_hz = 0.0
    
        model.vars.tx_deviation_actual.value = freq_dev_hz
    
    
    # calculate TX baudrate ratio
    # Using Equation (5.7) of EFR32 Reference Manual (internal.pdf)
    def calc_txbr_value(self, model):
        """
        calculate TX baudrate ratio
        Using Equation (5.7) of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        fxo = model.vars.xtal_frequency.value
        baudrate = model.vars.baudrate.value
    
        # calculate baudrate to fxo ratio
        ratio = fxo / (baudrate * 8.0)
    
        model.vars.txbr_ratio.value = ratio
    
    
    def calc_txbr_reg(self, model):
        """
        given desired TX baudrate ratio calculate TXBRNUM nd TXBRDEN
        that gets as close as possible to the ratio.
        Note that we start from the highest possible value for TXBRDEN
        and go down since having largest possible values in these register
        to have better phase resolution in OQPSK and MSK (see end of section
        5.6.5 in the manual)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        ratio = model.vars.txbr_ratio.value
    
        # find best integer ratio to match desired ratio
        for den in xrange(255, 0, -1):
             num = ratio * den
             if abs(round(num) - num) < 0.003 and num < 32768:
                break
    
        self._reg_write(model.vars.MODEM_TXBR_TXBRNUM,  int(round(num)))
        self._reg_write(model.vars.MODEM_TXBR_TXBRDEN,  int(den))
    
    
    def calc_txbr_actual(self, model):
        """
        given register values calculate actual TXBR ratio implemented

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        num = model.vars.MODEM_TXBR_TXBRNUM.value * 1.0
        den = model.vars.MODEM_TXBR_TXBRDEN.value
    
        ratio = num / den
    
        model.vars.txbr_ratio_actual.value = ratio
    
    
    def calc_txbases_reg(self, model):
        """
        set TXBASES based on preamble length and base bits value

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        txbases = model.vars.preamble_length.value / model.vars.preamble_pattern_len_actual.value
    
        self._reg_write(model.vars.MODEM_PRE_TXBASES, txbases)
    
    
    def calc_symbol_encoding(self, model):
        """
        set CODING register

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        encoding = model.vars.symbol_encoding.value

        if encoding == model.vars.symbol_encoding.var_enum.DSSS:
            coding = 2
        elif encoding == model.vars.symbol_encoding.var_enum.Manchester:
            coding = 1
        else:
            coding = 0

        self._reg_write(model.vars.MODEM_CTRL0_CODING,  coding)





    def calc_mapfsk_reg(self, model):
        """
        program MAPFSK register based on input

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        manchester_map = model.vars.manchester_mapping.value
        fsk_map = model.vars.fsk_symbol_map.value
        encoding = model.vars.symbol_encoding.value

        if encoding == model.vars.symbol_encoding.var_enum.Manchester:
            if manchester_map == model.vars.manchester_mapping.var_enum.Default:
                mapfsk = 0
            else:
                mapfsk = 1
        else:

            FSKMAP_LOOKUP = {
                model.vars.fsk_symbol_map.var_enum.MAP0.value:  0,
                model.vars.fsk_symbol_map.var_enum.MAP1.value:  1,
                model.vars.fsk_symbol_map.var_enum.MAP2.value:  2,
                model.vars.fsk_symbol_map.var_enum.MAP3.value:  3,
                model.vars.fsk_symbol_map.var_enum.MAP4.value:  4,
                model.vars.fsk_symbol_map.var_enum.MAP5.value:  5,
                model.vars.fsk_symbol_map.var_enum.MAP6.value:  6,
                model.vars.fsk_symbol_map.var_enum.MAP7.value:  7,
            }

            mapfsk = FSKMAP_LOOKUP[fsk_map.value]

        self._reg_write(model.vars.MODEM_CTRL0_MAPFSK, mapfsk)


