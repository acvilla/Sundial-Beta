"""Core CALC_Synth Calculator Package

Calculator functions are pulled by using their names.
Calculator functions must start with "calc_", if they are to be consumed by the framework.
    Or they should be returned by overriding the function:
        def getCalculationList(self):
"""

from collections import OrderedDict
import math
from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pyradioconfig.pycalcmodel import ModelVariableFormat

class CALC_Synth(ICalculator):

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

        # Inputs
        self._addModelVariable(model,  'channel_spacing_hz',   int,     ModelVariableFormat.DECIMAL, units='Hz', desc='Channel raster used for relative frequency configuration')
        self._addModelActual  (model,  'channel_spacing',      int,     ModelVariableFormat.DECIMAL)
        
        self._addModelRegister(model, 'SYNTH.CALOFFSET.CALOFFSET'      , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'SYNTH.CHCTRL.CHNO'              , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'SYNTH.CHSP.CHSP'                , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'SYNTH.DIVCTRL.LODIVFREQCTRL'    , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'SYNTH.FREQ.FREQ'                ,long, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'SYNTH.IFFREQ.IFFREQ'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'SYNTH.IFFREQ.LOSIDE'	         , int, ModelVariableFormat.HEX )
                                              
        # These aren't really synth registers, but they must follow the synth register values,
        # so we set them here.
        self._addModelRegister(model, 'MODEM.MIXCTRL.MODE'             , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.MIXCTRL.DIGIQSWAPEN'      , int, ModelVariableFormat.HEX )
        

    #TODO: add AFC adjustment term to rx_synth_freq once AFC is implemented
    def calc_rx_synth_freq_actual(self, model):
        """
        calculate synthesizer frequency for RX
        Equation (5.31) of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        chan0_freq = model.vars.SYNTH_FREQ_FREQ.value
        chno = model.vars.SYNTH_CHCTRL_CHNO.value
        chan_spacing = model.vars.SYNTH_CHSP_CHSP.value
        cal_offset = model.vars.SYNTH_CALOFFSET_CALOFFSET.value
        if_freq = model.vars.SYNTH_IFFREQ_IFFREQ.value
        loside = model.vars.SYNTH_IFFREQ_LOSIDE.value
        res = model.vars.synth_res_actual.value

        if loside:
            rx_synth_freq = chan0_freq + chno * chan_spacing + cal_offset - if_freq * res
        else:
            rx_synth_freq = chan0_freq + chno * chan_spacing + cal_offset + if_freq * res

        model.vars.rx_synth_freq_actual.value = int(round(rx_synth_freq))


    #TODO: add AFC adjustment term to tx_synth_freq once AFC is implemented
    #TODO: add calbiration offset to tx_synth_freq
    def calc_tx_synth_freq_actual(self, model):
        """
        calculate synthesizer frequency for TX
        Equation (5.32) of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        chan0_freq = model.vars.SYNTH_FREQ_FREQ.value
        chno = model.vars.SYNTH_CHCTRL_CHNO.value
        chan_spacing = model.vars.SYNTH_CHSP_CHSP.value
        cal_offset = model.vars.SYNTH_CALOFFSET_CALOFFSET.value

        tx_synth_freq = 1.0 * chan0_freq + chno * chan_spacing + cal_offset

        model.vars.tx_synth_freq_actual.value = long(tx_synth_freq)


    def calc_synth_res_actual(self, model):
        """
        calculate synthesizer frequency resolution
        Equation (5.33) of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        fxo = model.vars.xtal_frequency.value * 1.0
        lodiv = model.vars.lodiv_actual.value

        # calculate frequency resolution
        res = fxo / lodiv / pow(2, 19)

        model.vars.synth_res_actual.value = res


    def calc_base_frequency_actual(self, model):
        """
        calculate the actual base (RF) frequency
        Equation (5.34) of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        chan0_freq_reg = model.vars.SYNTH_FREQ_FREQ.value
        res = model.vars.synth_res_actual.value

        ch0_freq_hz = round(chan0_freq_reg * res)

        model.vars.base_frequency_actual.value = long(ch0_freq_hz)


    def calc_chsp_freq_reg(self, model):
        """
        calculate channel spacing and frequency register settings
        Equation (5.34) of EFR32 Reference Manual (internal.pdf)
        Equation (5.35) of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        ch_spacing = model.vars.channel_spacing.value * 1.0
        f0 = model.vars.base_frequency.value * 1.0
        res = model.vars.synth_res_actual.value
        
        # channel spacing in terms of res
        chsp = round(ch_spacing / res)

        self._reg_write(model.vars.SYNTH_CHSP_CHSP,  int(chsp))

        # frequency in terms of res
        freq = math.floor(f0 / res)

        self._reg_write(model.vars.SYNTH_FREQ_FREQ,  long(freq))

        

    def calc_chan_spacing_actual(self, model):
        """
        calculate the actual channel spacing
        Equation (5.35) of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        chsp = model.vars.SYNTH_CHSP_CHSP.value
        res = model.vars.synth_res_actual.value

        ch_spacing = round(chsp * res)

        model.vars.channel_spacing_actual.value = int(ch_spacing)


    def calc_lodiv_value(self, model):
        """
        calculate desired LODIV value

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        f0 = model.vars.base_frequency.value

        # cannot calculate lodiv if RF frequency is not given
        if f0 == 0:
            return

        # calculate ideal lodiv by finding divider ratio to get
        # target RF frequency from nominal 2.6 GHz VCO
        lodiv_ideal = 2.6e9 / f0
        lodiv = round(lodiv_ideal)

        # LODIV can only have the following values:
        # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16
        # if we end up with missing 7 or 11 values
        # just go to the next best value.
        # for 13 use 12 for 14 use 15 and any number greater
        # than 16 stick with 16
        if lodiv == 7 or lodiv == 11:
            if lodiv_ideal > lodiv:
                lodiv += 1
            else:
                lodiv -= 1
        elif lodiv == 13:
            lodiv = 12
        elif lodiv == 14:
            lodiv = 15

        if lodiv > 16:
            lodiv = 16

        model.vars.lodiv.value = int(lodiv)


    # map LODIVFREQCTRL field to lodiv values
    lodiv_table = OrderedDict()
    lodiv_table[1] = 1
    lodiv_table[2] = 2
    lodiv_table[3] = 3
    lodiv_table[4] = 4
    lodiv_table[5] = 5
    lodiv_table[19] = 6
    lodiv_table[20] = 8
    lodiv_table[21] = 10
    lodiv_table[27] = 9
    lodiv_table[28] = 12
    lodiv_table[29] = 15
    lodiv_table[36] = 16


    def calc_lodiv_reg(self, model):
        """
        write LODIV register given desired divider ratio
        use LUT since mapping is not linear

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        lodiv = model.vars.lodiv.value

        for index, lo in self.lodiv_table.iteritems():
            if lodiv == lo:
                break

        self._reg_write(model.vars.SYNTH_DIVCTRL_LODIVFREQCTRL,  index)


    def calc_lodiv_actual(self, model):
        """
        read LODIV register value and return actual LO divider value

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        model.vars.lodiv_actual.value = self.lodiv_table[model.vars.SYNTH_DIVCTRL_LODIVFREQCTRL.value]


    def calc_iffreq_reg(self, model):
        """
        calculate IFFREQ register\n
        Equation (5.14), (5.33) and (5.37) of EFR32 Reference Manual (internal.pdf)\n
        IFFREQ = f_IF / res
        f_IF = fxo / (DEC0 * CFOSR)
        res = fxo / lodiv / pow(2,19)
        IFFREQ = fxo / (DEC0 * CFOSR) * lodiv * pow(2,19) / fxo
               = lodiv * pow(2,19) / (DEC0 * CFOSR)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        dec0 = model.vars.dec0_actual.value
        cfosr = model.vars.cfosr_actual.value
        lodiv = model.vars.lodiv_actual.value

        # calculate if frequency
        iffreq = math.floor(lodiv * pow(2, 19) / dec0 / cfosr)

        self._reg_write(model.vars.SYNTH_IFFREQ_IFFREQ,  int(abs(iffreq)))

    def calc_lo_side_regs(self, model):
        """
        calculate LOSIDE register in synth and matching one in modem

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        #TODO: have to find a way to set injection side for now use 1 (high side)
        self._reg_write(model.vars.SYNTH_IFFREQ_LOSIDE,  1)

        self._reg_write(model.vars.MODEM_MIXCTRL_MODE,           0)
        self._reg_write(model.vars.MODEM_MIXCTRL_DIGIQSWAPEN,    1)
        

    def calc_synth_misc(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        self._reg_write(model.vars.SYNTH_CHCTRL_CHNO, 0)
        self._reg_write(model.vars.SYNTH_CALOFFSET_CALOFFSET, 0)


