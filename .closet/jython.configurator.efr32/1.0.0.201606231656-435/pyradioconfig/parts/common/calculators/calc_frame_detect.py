"""CALC_Frame_Detect Calculator Package

Calculator functions are pulled by using their names.
Calculator functions must start with "calc_", if they are to be consumed by the framework.
    Or they should be returned by overriding the function:
        def getCalculationList(self):
"""

from collections import OrderedDict
import math
from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pyradioconfig.pycalcmodel import ModelVariableFormat

class CALC_Frame_Detect(ICalculator):

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

        self._addModelVariable(model,  'preamble_string',  str,          ModelVariableFormat.ASCII, desc='Output string representing the preamble pattern in binary')
        self._addModelVariable(model,  'syncword_string',  str,          ModelVariableFormat.ASCII, desc='Output string representing the sync word in binary')

        # Actual values
        self._addModelActual(model,    'syncword_0'     ,  long,         ModelVariableFormat.HEX, ) #  desc='Syncword 0 extracted from the register )
        self._addModelActual(model,    'syncword_1'     ,  long,         ModelVariableFormat.HEX, ) #  desc='Syncword 1 extracted from the register )

        self._addModelRegister(model, 'MODEM.CTRL1.DUALSYNC'           , int, ModelVariableFormat.HEX )
        
        
        
    def flip_bits(self, input, numbits):
        """
        flips the order of bits in an input numbits wide
        assuming the bits are aligned left in multiples of 4 bits

        Args:
            input (unknown) : input
            numbits (unknown) : numbits

        Returns:
            output (unknown) : unknown
        """

        output = 0L
        # find index of LSB
        first_bit = (4 - (numbits % 4)) % 4

        for bitnum in range(numbits):
            if (input & (1 << (bitnum + first_bit) )):
                output = output | (1 << (numbits - 1 - bitnum))

        return output


    def calc_deprecate_syncwords(self, model):
        """
        converts original syncword inputs to new left aligned syncword variables

        Args:
            input (unknown) : input

        Returns:
            output (unknown) : unknown
        """
        # syncword length
        len = model.vars.syncword_length.value

        # shift so that left most bit is aligned to a 4-bit boundary
        shift = 4 - (len % 4)

        if shift == 4:
            shift = 0

        model.vars.syncword_0_left.value_forced = model.vars.syncword_0.value << shift
        model.vars.syncword_1_left.value_forced = model.vars.syncword_1.value << shift

        # undef original variables
        model.vars.syncword_0.value_forced = None
        model.vars.syncword_1.value_forced = None


    def calc_deprecate_preamble_pattern(self, model):
        """
        converts original preamble_pattern inputs to new left aligned preamble_pattern_left variables

        Args:
            input (unknown) : input

        Returns:
            output (unknown) : unknown
        """
        # get length of preamble base variable
        len = model.vars.preamble_pattern_len.value

        # shift so that first bit is aligned left
        model.vars.preamble_pattern_left.value_forced = model.vars.preamble_pattern.value << (4 - len)

        model.vars.preamble_pattern.value_forced = None


    def calc_sync_words_reg(self, model):
        """
        write sync words from input to registers

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        syncword_length = model.vars.syncword_length.value
        self._reg_write(model.vars.MODEM_SYNC0_SYNC0,  long(self.flip_bits(model.vars.syncword_0_left.value, syncword_length)))
        self._reg_write(model.vars.MODEM_SYNC1_SYNC1,  long(self.flip_bits(model.vars.syncword_1_left.value, syncword_length)))

        if model.vars.ber_force_sync.value is True:
            self._reg_write(model.vars.MODEM_SYNC0_SYNC0, 0x1dd3d4a0L)      # gdc:  Fix this after we get rid of the "_left" stuff above.  
                                                                            # gdc:  Fix it so we just write syncword_0 before it gets flipped
                                                                            

        
    
    def calc_syncbits_reg(self, model):
        """
        write sync word length from input to register

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        assert(model.vars.syncword_length.value > 0)
        
        if model.vars.ber_force_sync.value is True:
            syncword_length = 32
        else:
            syncword_length = model.vars.syncword_length.value
            
        self._reg_write(model.vars.MODEM_CTRL1_SYNCBITS,  syncword_length - 1)

            
    
    def calc_syncword_length_actual(self, model):
        """given register read back actual sync word length

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        model.vars.syncword_length_actual.value = model.vars.MODEM_CTRL1_SYNCBITS.value + 1
    
    # Calculate the actual syncword from the register
    def calc_syncword_actual(self, model):
        syncword_length = model.vars.syncword_length_actual.value
        model.vars.syncword_0_actual.value = long(bin(model.vars.MODEM_SYNC0_SYNC0.value)[2:].zfill(syncword_length)[::-1], 2)
        model.vars.syncword_1_actual.value = long(bin(model.vars.MODEM_SYNC1_SYNC1.value)[2:].zfill(syncword_length)[::-1], 2)


    # Calculate a binary string that's
    def calc_syncword_string(self, model):
        syncword_length = model.vars.syncword_length_actual.value
        syncword = model.vars.syncword_0_actual.value
        model.vars.syncword_string.value = bin(syncword)[2:].zfill(syncword_length)


    def calc_preamble_string(self, model):
        preamble_pattern     = model.vars.preamble_pattern_left.value

        preamble_pattern_len = model.vars.preamble_pattern_len.value
        preamble_len      = model.vars.preamble_length.value

        repeats = preamble_len/preamble_pattern_len
        preamble_pattern_string = ('{:0' + str(preamble_pattern_len) + 'b}').format(preamble_pattern >> (4-preamble_pattern_len))
        
        preamble_string = preamble_pattern_string*repeats
        
        model.vars.preamble_string.value = preamble_string
    

        
    def calc_timbases_val(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        preamblebits = model.vars.preamble_length.value
        modformat = model.vars.modulation_type.value
        basebits = model.vars.preamble_pattern_len_actual.value
        encoding = model.vars.symbol_encoding.value

        if encoding == model.vars.symbol_encoding.var_enum.DSSS:
            timingbases = 1
        else:

            if model.vars.ber_force_fdm0.value is True:
                timingbases = 0
            elif modformat == model.vars.modulation_type.var_enum.FSK4:
                timingbases = round(preamblebits / 8.0)
            else:
                if preamblebits < 8:
                    timingbases = 0
                elif preamblebits < 10:
                    timingbases = 1
                elif preamblebits <= 32:
                    timingbases = 4
                else:
                    timingbases = 8
    
            if timingbases > 15:
                timingbases = 15

        model.vars.symbols_in_timing_window.value = int(timingbases * basebits)


    def calc_timbases_reg(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        timingwindow = model.vars.symbols_in_timing_window.value * 1.0
        basebits = model.vars.preamble_pattern_len_actual.value

        timingbases = int(round(timingwindow / basebits))

        self._reg_write(model.vars.MODEM_TIMING_TIMINGBASES,  timingbases)
    
    
    # TODO: tweak equation based on new PHYs
    def calc_addtimseq_val(self, model):
        """
        calculate additional timing sequences to detect given preamble length
        the equation used to calcualte ADDTIMSEQ is derived emprically and might need
        tweaking as we have more PHY providing additional data

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        preamblebits = model.vars.preamble_length.value * 1.0
        timingbases = model.vars.timingbases_actual.value
        timingwindow = model.vars.timing_window_actual.value
    
        if timingbases > 1:
            # looks like it is easier to get a working setting when this is set to 0
            # for now going to generate 0 until we find a better alternative
            addtimseq = math.floor(preamblebits / timingwindow) - 2
        else:
            addtimseq = 0
    
        # saturate addtimseq to fit into 4 bits
        if addtimseq > 15:
            addtimseq = 15
    
        if addtimseq < 0:
            addtimseq = 0

        model.vars.number_of_timing_windows.value = int(addtimseq) + 1

    def calc_addtimseq_reg(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        addtimseq = model.vars.number_of_timing_windows.value

        # one search is done by default
        if addtimseq > 0:
            addtimseq -= 1

        self._reg_write(model.vars.MODEM_TIMING_ADDTIMSEQ, addtimseq)
    
    
    def calc_timbases_actual(self, model):
        """
        return actual TIMINGBASES value

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        model.vars.timingbases_actual.value = model.vars.MODEM_TIMING_TIMINGBASES.value

    
    def calc_timingwindow_actual(self, model):
        """
        calculate the size of the timing window. If timingbases == 0 we are in FDM0 mode where
        the timing window is set by number of sync bits. In FDM1 (ADDTIMSEQ = 0) and FDM2 (ADDTIMSEQ > 0)
        modes the timing window size is a product of timingbases and basebits.

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        timingbases = model.vars.timingbases_actual.value
        basebits = model.vars.preamble_pattern_len_actual.value
        syncword_length = model.vars.syncword_length_actual.value
        spreading_factor = model.vars.dsss_spreading_factor.value

        if timingbases == 0:
            timing_window = syncword_length
        elif spreading_factor > 0:
            timing_window = timingbases * spreading_factor
        else:
            timing_window = timingbases * basebits

        model.vars.timing_window_actual.value = timing_window
    
    
    def calc_basebits_actual(self, model):
        """
        return actual base bits

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        model.vars.preamble_pattern_len_actual.value = model.vars.MODEM_PRE_BASEBITS.value + 1
    
    
    def calc_basebits_reg(self, model):
        """
        set BASEBITS register using input

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        basebits = model.vars.preamble_pattern_len.value
    
        if basebits > 0:
            reg = basebits - 1
        else:
            reg = 0
    
        self._reg_write(model.vars.MODEM_PRE_BASEBITS,  reg)
    
    
    def calc_base_reg(self, model):
        """
        set BASE register using input
        The bits have to be flipped around before writing the register

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        preamble_pattern_len = model.vars.preamble_pattern_len.value
        preamble_pattern     = model.vars.preamble_pattern_left.value

        modem_pre_base = self.flip_bits(preamble_pattern, preamble_pattern_len)
        modem_pre_base = int(modem_pre_base)
    
        self._reg_write(model.vars.MODEM_PRE_BASE,  modem_pre_base)
    
    
    #TODO: do we need to add dependency to bandwidth when calculating the timing treshold?
    #      we might want to reduce the threshold with increasing bandwidth
    def calc_timthresh_value(self, model):
        """
        calculate TIMTHRESH which is used in determining valid correlation values in timing detection

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        modformat = model.vars.modulation_type.value
        timingwindow = model.vars.timing_window_actual.value
    
        # given modulation method determine nominal soft decision values
        if modformat == model.vars.modulation_type.var_enum.MSK or \
           modformat == model.vars.modulation_type.var_enum.OQPSK or \
           modformat == model.vars.modulation_type.var_enum.BPSK or \
           modformat == model.vars.modulation_type.var_enum.DBPSK:
            nominal_soft_decision = 64
        elif modformat == model.vars.modulation_type.var_enum.FSK2:
            nominal_soft_decision = 64
        elif modformat == model.vars.modulation_type.var_enum.FSK4:
            nominal_soft_decision = 64
        else:
            nominal_soft_decision = 0
    
        # given nominal soft decision value and timing window size determine optimal threshold
        # TODO: equation for thresh is empirically derived and does need tuning
        if nominal_soft_decision > 0:
            thresh = timingwindow * nominal_soft_decision / 32.0 - 1.0
        else:
            thresh = 0.0
    
        model.vars.timing_detection_threshold.value = int(round(thresh))
    
    
    def calc_timthresh_reg(self, model):
        """
        given desired threshold set register value

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """


        self._reg_write(model.vars.MODEM_TIMING_TIMTHRESH, int(model.vars.timing_detection_threshold.value))
    
    
    def calc_timthresh_actual(self, model):
        """
        given register value return actual threshold value

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        model.vars.timthresh_actual.value = model.vars.MODEM_TIMING_TIMTHRESH.value
    
    
    def calc_preerrors_val(self, model):
        """
        calculate PREERRORS field

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        # FIXME: consider adding +1 to errors when AFC is enbabled - seems to work better

        dssslen = model.vars.dsss_len_actual.value

        # for now just set it to 0 except for DSSS cases where we want it to be
        # half the DSSS length
        if dssslen == 0:
            preerrors = 0
        else:
            preerrors = dssslen / 2.0

        # make sure we fit into 4 bits
        if preerrors > 15:
            preerrors = 15

        model.vars.errors_in_timing_window.value = int(round(preerrors))

    def calc_preerrors_reg(self, model):
        """
        write value to register

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        preerrors = model.vars.errors_in_timing_window.value

        if preerrors > 15:
            preerrors = 15

        self._reg_write(model.vars.MODEM_PRE_PREERRORS, preerrors)

    def calc_dsss0_reg(self, model):
        """
        write DSSS symbol 0 register

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        self._reg_write(model.vars.MODEM_DSSS0_DSSS0, model.vars.dsss_chipping_code.value)

    def calc_dsssshifts_val(self, model):
        """
        calculate DSSS shift value

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        length = model.vars.dsss_len.value
        bps = model.vars.dsss_bits_per_symbol.value

        if bps <= 1:
            val = 0
        else:
            val = length / (pow(2,bps) / 2)

        model.vars.dsss_shifts.value = val
    
    def calc_dsssshifts_reg(self, model):
        """
        write DSSS cyclic shifts number to generate new symbols when using DSSS

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        val = model.vars.dsss_shifts.value

        if val == 0:
            reg = 0
        elif val == 1:
            reg = 1
        elif val == 2:
            reg = 2
        elif val == 4:
            reg = 3
        elif val == 8:
            reg = 4
        elif val == 16:
            reg = 5
        else:
            print "Invalid dsss_shift value!"
            return
    
        self._reg_write(model.vars.MODEM_CTRL0_DSSSSHIFTS, reg)
    
    
    def calc_dsssshifts_actual(self, model):
        """
        given register setting return actual DSSS shifts value

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        reg = model.vars.MODEM_CTRL0_DSSSSHIFTS.value
    
        if reg == 0:
            val = 0
        elif reg == 1:
            val = 1
        elif reg == 2:
            val = 2
        elif reg == 3:
            val = 4
        elif reg == 4:
            val = 8
        elif reg == 5:
            val = 16
    
        model.vars.dsss_shifts_actual.value = val
    
    
    def calc_dssslen_reg(self, model):
        """
        set DSSS length register

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        length = model.vars.dsss_len.value
        shifts = model.vars.dsss_shifts_actual.value
    
        if length == 0:
            reg = 0
        else:
            if shifts == 0:
                if len < 4 or length > 32:
                    print "dsss_shift value must be between 4 and 32"
                    return
            else:
                if not length % shifts == 0:
                    print "dsss_len must be an integer multiple of dsss_shifts"
                    return
            reg = length - 1
    
        self._reg_write(model.vars.MODEM_CTRL0_DSSSLEN, reg)
    
    
    def calc_dssslen_actual(self, model):
        """
        given register setting return actual DSSS length

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        dsss0 = model.vars.MODEM_DSSS0_DSSS0.value
    
        if dsss0 == 0:
            len = 0
        else:
            len = model.vars.MODEM_CTRL0_DSSSLEN.value + 1
    
        model.vars.dsss_len_actual.value = len
    
    
    def calc_dsssdouble_reg(self, model):
        """
        based on modulation used select if DSSS symbol's inverted version
        should also be a DSSS symbol

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        length = model.vars.dsss_len.value
        modulation = model.vars.modulation_type.value
    
        if length > 0:
            if modulation == model.vars.modulation_type.var_enum.OQPSK:
                dsssdouble = 2
            elif modulation == model.vars.modulation_type.var_enum.BPSK:
                dsssdouble = 1
            else:
                print "ERROR: current modulation not supported with DSSS yet"
        else:
            dsssdouble = 0
    
        self._reg_write(model.vars.MODEM_CTRL0_DSSSDOUBLE, dsssdouble)
    
    def calc_dsss_bits_per_symbol(self, model):
        """
        calculate bits per symbol in DSSS mode

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        length = model.vars.dsss_len.value
        spreading_factor = model.vars.dsss_spreading_factor.value * 1.0

        if spreading_factor == 0:
            bps = 0
        else:
            bps = length / spreading_factor

        model.vars.dsss_bits_per_symbol.value = int(bps)

    def calc_tr_td_edge(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        modformat = model.vars.modulation_type.value

        if modformat == model.vars.modulation_type.var_enum.BPSK or \
           modformat == model.vars.modulation_type.var_enum.DBPSK:
            self._reg_write(model.vars.MODEM_CTRL5_TDEDGE, 1)
            self._reg_write(model.vars.MODEM_CTRL5_TREDGE, 1)
        else:
            self._reg_write(model.vars.MODEM_CTRL5_TDEDGE, 0)
            self._reg_write(model.vars.MODEM_CTRL5_TREDGE, 0)

    def calc_diffencmode_reg(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        DIFFENCMODE_LOOKUP = {
            model.vars.diff_encoding_mode.var_enum.DISABLED.value:  0,
            model.vars.diff_encoding_mode.var_enum.RR0.value:  1,
            model.vars.diff_encoding_mode.var_enum.RE0.value:  2,
            model.vars.diff_encoding_mode.var_enum.RR1.value:  3,
            model.vars.diff_encoding_mode.var_enum.RE1.value:  4,
        }

        self._reg_write(model.vars.MODEM_CTRL0_DIFFENCMODE,
                       DIFFENCMODE_LOOKUP[(model.vars.diff_encoding_mode.value).value])

    def calc_tsamplim_val(self, model):
        """
        set TSAMPLIM to a default value of 10. Have an intermediate variable so that we can
        overwrite it

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        modformat = model.vars.modulation_type.value

        # for amplitude modulated signal we need to turn off TSAMPMODE as enabling it
        # switches the slicer level from FREQOFFESTLIM to TSAMPLIM which we don't want.
        if modformat == model.vars.modulation_type.var_enum.OOK or \
           modformat == model.vars.modulation_type.var_enum.ASK:
            th = 0
        else:
            th = 10

        model.vars.timing_sample_threshold.value = th

    def calc_tsamplim_reg(self, model):
        """
        calculate TSAMPLIM register based on variable. Saturating to 100 based on the fact
        that we have not seen a register setting greater than 20 up to this point despite
        the the register being 16 bits

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        threshold = model.vars.timing_sample_threshold.value

        if threshold < 0:
            threshold = 0
        elif threshold > 100:
            threshold = 100

        self._reg_write(model.vars.MODEM_CTRL3_TSAMPLIM, threshold)

    def calc_tsampmode_reg(self, model):
        """
        set TSAMPMODE if we need a non-zero TSAMPLIM value

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        threshold = model.vars.timing_sample_threshold.value
        modformat = model.vars.modulation_type.value

        if threshold == 0 or \
           modformat == model.vars.modulation_type.var_enum.OOK or \
           modformat == model.vars.modulation_type.var_enum.ASK:
            mode = 0
        else:
            mode = 1

        self._reg_write(model.vars.MODEM_CTRL3_TSAMPMODE, mode)


    def calc_tsampdel_val(self, model):
        """
        We do not see a strong relation between performance and this delay parameter but
        using hand optimized results for about 50 PHYs we came up with a simple equation
        to calculate the delay parameter when TSAMPMODE is enabled.

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        baudrate = model.vars.baudrate.value
        osr = model.vars.oversampling_rate_actual.value

        if model.vars.MODEM_CTRL3_TSAMPMODE.value == 1:
            tsampdel = round(2.5e6/baudrate/osr)
        else:
            tsampdel = 0

        if tsampdel > 3:
            tsampdel = 3

        self._reg_write(model.vars.MODEM_CTRL3_TSAMPDEL, int(tsampdel))

    def calc_dualsync_reg(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        sync1 = model.vars.syncword_1_actual.value

        if sync1 > 0:
            dualsync = 1
        else:
            dualsync = 0

        self._reg_write(model.vars.MODEM_CTRL1_DUALSYNC, dualsync)