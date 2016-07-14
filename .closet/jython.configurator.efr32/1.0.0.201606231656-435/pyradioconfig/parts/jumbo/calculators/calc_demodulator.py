""" CALC_Demodulator_jumbo Package

Calculator functions are pulled by using their names.
Calculator functions must start with "calc_", if they are to be consumed by the framework.
    Or they should be rturned by overriding the function:
        def getCalculationList(self):
"""

from collections import OrderedDict
import math
import itertools
from pyradioconfig.parts.common.calculators.calc_demodulator import CALC_Demodulator
from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pyradioconfig.parts.common.calculators.calc_utilities import CALC_Utilities
from pyradioconfig.parts.common.calculators.calc_freq_offset_comp import CALC_Freq_Offset_Comp
from pyradioconfig.pycalcmodel import ModelVariableFormat

class CALC_Demodulator_jumbo(CALC_Demodulator):

    """
    Init internal variables
    """
    def __init__(self):
        self._major = 1
        self._minor = 0
        self._patch = 0

    def calc_init_advanced(self, model):
        # init advanced inputs to defaults
        model.vars.src_disable.value = 0
        model.vars.viterbi_enable.value = 0
        model.vars.dsa_enable.value = 0
        model.vars.target_osr.value = 7

    def calc_src_reg(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        osr = model.vars.oversampling_rate_actual.value

        src1 = model.vars.src1.value
        src2 = model.vars.src2.value
        src1_enable = 1
        src2_enable = 1

        if src1 == 128:
            src1_enable = 0

        if src2 == 1024:
            src2_enable = 0

        if int(osr) == osr:
            intosr = 1
        else:
            intosr = 0

        self._reg_write(model.vars.MODEM_SRCCHF_SRCRATIO1, src1)
        self._reg_write(model.vars.MODEM_SRCCHF_SRCRATIO2, src2)
        self._reg_write(model.vars.MODEM_SRCCHF_SRCENABLE1, src1_enable)
        self._reg_write(model.vars.MODEM_SRCCHF_SRCENABLE2, src2_enable)
        self._reg_write(model.vars.MODEM_SRCCHF_INTOSR, intosr)


    def calc_bwsel_reg(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        bwsel = model.vars.bwsel.value

        if bwsel == 0.263:
            reg = 0
        elif bwsel == 0.219:
            reg = 1
        else:
            reg = 2

        self._reg_write(model.vars. MODEM_SRCCHF_BWSEL,  reg)


#FIXME: in FDM0 mode make sure osr * bitrate < 10M
    def calc_d0_d1_d2_cfosr_rxbr_value(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        # read required config parameters
        baudrate = model.vars.baudrate.value
        fxo = model.vars.xtal_frequency.value * 1.0
        bw_desired = model.vars.bandwidth_hz.value * 1.0
        brcalen = model.vars.brcalen.value
        tol = model.vars.baudrate_tol_ppm.value
        baudrate_offset = model.vars.rx_baudrate_offset_hz.value
        timingwindow = model.vars.timing_window_actual.value
        src_disable = model.vars.src_disable.value
        target_osr = model.vars.target_osr.value

        debug = 0

        if debug:
            f = open('debug.csv','w')
            f.write(    'cost, bw_error, range_error, rate_error, dec0, dec1, dec2, bwsel, src1, src2, bw, baudrate_real, osr, eliminate1, eliminate2, eliminate3, eliminate4\n')


        # baudrate calibration works only in one direction so we set the
        # baudrate to the smallest value we want to support and let the calibration
        # hardware track it

        # 3 options in how we choose rxbr and src values:
        # 1) if baudrate calibration is enable (in which case SRC should be disabled as well)
        #    we fix rxbrden to 31 and src1 to 128 and let rxbrnum range from 0 to 31
        # 2) if SRC is disabled we fix src1 to 128 and let both rxbrnum and rxbrden range from 0 to 31
        # 3) in all other cases we limit rxbr numbers that are multiples of 1/2 so that osr is integer
        #    and give src1 the full range supported.

        if brcalen == 1:
            baudrate -= baudrate * tol / 1000000.0
            rxbrint_list = [2, 3, 4]
            rxbrnum_list = xrange(0, 32, 1)
            rxbrden_list = [31]
            src1_range = [128]
        elif src_disable:
            rxbrint_list = [1, 2, 3, 4]
            rxbrnum_list = xrange(0, 32, 1)
            rxbrden_list = xrange(1, 32, 1)
            src1_range = [128]
        else:
            rxbrint_list = [1, 2, 3, 4]
            rxbrnum_list = [1, 0]
            rxbrden_list = [2]
            src1_range = xrange(108, 156, 1)

        # limit and apply baudrate offset to 1%
        offset_limit = 0.01 * baudrate

        if baudrate_offset > offset_limit:
            baudrate_offset = offset_limit
        elif baudrate_offset < -offset_limit:
            baudrate_offset = - offset_limit

        baudrate += baudrate_offset

        # want to minimize this so start with big number
        best_cost = 99e99
        best_fc = 0

        # loop over all possible DEC0, DEC1 values
        for dec0 in [8, 4, 3]:

            # 0.219 setting is going away in Nerio so we should not expose that to the customer
            for bwsel in [0.263, 0.196]: #[0.263, 0.219, 0.196]:

                # TODO: make the range variable - factor into min_dec1,max_dec1
                # limit SRC1 rate change to +/-18%
                # lower limit is 0.82 * 128 = 104.96 = 105
                # upper limit is 1.18 * 128 = 151.04 = 151
                for src1 in src1_range:

                    src1ratio = 128.0 / src1

                    dec1 = round((fxo * bwsel * src1ratio) / (dec0 * bw_desired ))

                    if dec1 < 1:
                        dec1 = 1

                    if dec1 > 16384:
                        dec1 = 16384

                    # given dec0 and dec1 calculate bandwidth we actually get
                    bw = (fxo * bwsel * src1ratio) / (dec0 * dec1 )

                    # unless we are at the largest BW possible skip the rest if bw is less
                    # than 95% of carson bw or 82% of carson bw for 2.4GHz band
                    # TODO: tune these constants - dont'forget to factor into min_dec1, max_dec1
                    if baudrate >= 1e6:
                        carson_scale = 0.82
                    else:
                        carson_scale = 0.95

                    #bw_desired *= carson_scale

                    # we technically could do the following checks in the cost function below but
                    # that would mean calculating the cost function for thousands of
                    # combinations that we know will not work so to save computation
                    # we check this here.

                    # if bw less than a scaled version of the carson bw throw away this combination
                    # unless we are using the widest possible bw setting we have on the chip
                    # dec0 = 4 actually results in wider bw than dec0 = 3 due to the wider bw
                    # decimation filter it has.
                    eliminate1 = 0
                    if bw < bw_desired*carson_scale and not (dec1 == 1 and (dec0 == 3 or dec0 == 4)):
                        if debug:
                            eliminate1 = 1
                        else:
                            continue

                    # calculate corresponding DEC2 values
                    # we have two possible values for DEC2 given DEC0 and DEC1 so we loop
                    # over those values below
                    dec2_start = int(math.floor(fxo / (5.0 * dec0 * dec1 * baudrate)))
                    dec2_end = dec2_start + 1

                    # 0 is not a valid value for DEC2 so only try 1 if we end up with 0
                    if dec2_start == 0:
                        dec2_start = 1
                        dec2_end = 1

                    for dec2 in xrange(dec2_start, dec2_end + 1):

                        #for rxbrint, rxbrnum in zip(rxbrint_list, rxbrnum_list):
                        for rxbrint, rxbrnum, rxbrden in list(itertools.product(rxbrint_list, rxbrnum_list, rxbrden_list)):

                            rxbrden = float(rxbrden)
                            rxbr = (rxbrint + rxbrnum / rxbrden)

                            eliminate2 = 0
                            if (rxbr < 1.5 or rxbr > 4):
                                if debug:
                                    eliminate2 = 1
                                else:
                                    continue

                            if brcalen or src_disable:
                                src2 = 1024
                            else:
                                src2 = round((fxo * 1024.0 * src1ratio) / (dec0 * dec1 * dec2 * baudrate * 2 * rxbr))

                            #print dec0, dec1, dec2, src1ratio, baudrate, rxbr, src2
                            #print dec0, dec1, bwsel, src1, fc, dec2, rxbr, src2

                            eliminate3 = 0
                            if (src2 < 838 or src2 > 1249):
                                if debug:
                                    eliminate3 = 1
                                else:
                                    continue

                            src2ratio = 1024.0 / src2

                            # calculate real baudrate we get with these setting
                            baudrate_real = fxo * src1ratio * src2ratio / (dec0 * dec1 * dec2 * 2 * rxbr)

                            # calculate oversampling rate for given combination
                            osr = 2 * rxbr

                            eliminate4 = 0
                            if timingwindow * osr > 512:
                                print "WARNING: Eliminating case due to memory restrictions"
                                if debug:
                                    eliminate4 = 1
                                else:
                                    continue

                            # calculate cost function based on over-sampling-rate, bw, and rx bit rate
                            cost, bw_error, range_error, rate_error = self.return_cost(model, osr, bw, bw_desired, baudrate_real, baudrate, brcalen, target_osr)

                            if debug:
                                printlist = [cost, bw_error, range_error, rate_error, dec0, dec1, dec2, bwsel, src1, src2, bw, baudrate_real, osr,  eliminate1, eliminate2, eliminate3, eliminate4]

                                for item in printlist:
                                    f.write('%s,' % item)
                                f.write('\n')

                            # record necessary info if we found a better combination than we had
                            # prefer larger decimation in dec0 if the cost is the same
                            if cost < best_cost or (cost == best_cost and dec0 > dec1):
                                best_cost = cost
                                best_dec0 = dec0
                                best_dec1 = dec1
                                best_dec2 = dec2
                                best_rxbrnum = rxbrnum
                                best_rxbrden = rxbrden
                                best_rxbrint = rxbrint
                                best_bwsel = bwsel
                                best_src1 = src1
                                best_src2 = src2
                                model.vars.cost_bandwidth.value = bw_error
                                model.vars.cost_range.value = range_error
                                model.vars.cost_rate.value = rate_error
                                model.vars.cost_total.value = cost

        # store best combination in variables to be written to registers in other functions
        model.vars.dec0.value = int(best_dec0)
        model.vars.dec1.value = int(best_dec1)
        model.vars.dec2.value = int(best_dec2)
        model.vars.rxbrint.value = int(best_rxbrint)
        model.vars.rxbrnum.value = int(best_rxbrnum)
        model.vars.rxbrden.value = int(best_rxbrden)
        model.vars.bwsel.value = best_bwsel
        model.vars.src1.value = int(best_src1)
        model.vars.src2.value = int(best_src2)

        if debug:
            f.close()

    # TODO: add deviation error to this cost function
    # TODO: if timing_window * osr  > 256 we might fail: find where we break down in terms of high OSR
    # TODO: make constant programmable
    def return_cost(self, model, osr, bw, bw_desired, baudrate_real, baudrate_hz, brcalen, target_osr):
        """
        Cost function used to find optimal settigs for DEC0, DEC1, DEC2, RXBRNUM, RXBRDEN

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        if bw > bw_desired:
            bw_error = 100.0 * (bw - bw_desired) / bw_desired
        else:
            #TODO: might want to give this a bigger cost
            bw_error = 100.0 * (bw_desired - bw) / bw_desired

        # calculate range_error as the distance to 5 or 8 if we are outside this range

        range_error = abs(osr - target_osr)

        if osr < 5 or osr > 7:
            range_error*100

        # if the baudrate is not exact penalize this setting by 1e9
        rate_error = 100.0 * abs(baudrate_real - baudrate_hz) / baudrate_real

        # if baudrate calibration is enabled allow up to 1% error if not allow
        # 0.1% error before penalizing due to excessive baudrate offset
        if brcalen == 1:
            rate_error_limit = 10.0
        else:
            rate_error_limit = 0.4

        if rate_error > rate_error_limit:
            rate_error += 1.0e9
        elif rate_error > 0:
            rate_error *= 100.0

        # if bandwidth was forced choose setting with smallest bw_error and
        #  look at other metrics only if there are several with the same bw_error
        if model.vars.bandwidth_hz.value_forced == None:
            cost = bw_error + range_error + rate_error
        else:
            cost = 10*bw_error + range_error + rate_error#

        return cost, bw_error, range_error, rate_error


    def calc_rxbr_reg(self, model):
        """
        write RXBR register values

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        self._reg_write(model.vars.MODEM_RXBR_RXBRINT, int(model.vars.rxbrint.value))
        self._reg_write(model.vars.MODEM_RXBR_RXBRNUM, int(model.vars.rxbrnum.value))
        self._reg_write(model.vars.MODEM_RXBR_RXBRDEN, int(model.vars.rxbrden.value))


    def calc_rx_baud_rate_actual(self, model):
        """
        calculate actual RX baud rate from register settings
        Equation (5.17) of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        fxo = model.vars.xtal_frequency.value
        dec0 = model.vars.dec0_actual.value
        dec1 = model.vars.dec1_actual.value
        dec2 = model.vars.dec2_actual.value
        rxbrint = model.vars.rxbrint_actual.value
        rxbrden = model.vars.rxbrden_actual.value*1.0
        rxbrnum = model.vars.rxbrnum_actual.value
        src1ratio = model.vars.src1_ratio_actual.value
        src2ratio = model.vars.src2_ratio_actual.value

        rx_baud_rate = (fxo * src1ratio * src2ratio) / (dec0 * dec1 * dec2 * 2 * (rxbrint + rxbrnum / rxbrden))

        model.vars.rx_baud_rate_actual.value = rx_baud_rate


    def calc_src_actual(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        src1 = model.vars.MODEM_SRCCHF_SRCRATIO1.value
        src2 = model.vars.MODEM_SRCCHF_SRCRATIO2.value
        src1_enable = model.vars.MODEM_SRCCHF_SRCENABLE1.value
        src2_enable = model.vars.MODEM_SRCCHF_SRCENABLE2.value

        if src1_enable:
            model.vars.src1_ratio_actual.value = 128.0 / src1
        else:
            model.vars.src1_ratio_actual.value = 1.0

        if src2_enable:
            model.vars.src2_ratio_actual.value = 1024.0 / src2
        else:
            model.vars.src2_ratio_actual.value = 1.0


    def calc_bwsel_actual(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        bwsel = model.vars.MODEM_SRCCHF_BWSEL.value

        if bwsel == 0:
            value = 0.263
        elif bwsel == 1:
            value = 0.219
        else:
            value = 0.196

        model.vars.bwsel_actual.value = value

    def calc_bandwidth_actual(self, model):
        """
        calculate actual BW from register settings
        Equation (5.15) of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        fxo = model.vars.xtal_frequency.value
        dec0 = model.vars.dec0_actual.value
        dec1 = model.vars.dec1_actual.value
        bwsel = model.vars.bwsel_actual.value
        src1ratio = model.vars.src1_ratio_actual.value

        bandwidth = round((fxo * bwsel * src1ratio ) / (dec0 * dec1))

        model.vars.bandwidth_actual.value = int(bandwidth)


    def dcalc_print_results(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        bw_actual = model.vars.bandwidth_actual.value
        br_actual = model.vars.rx_baud_rate_actual.value
        baudrate = model.vars.baudrate.value
        bw_desired = model.vars.bandwidth_hz.value
        baudrate_offset = model.vars.rx_baudrate_offset_hz.value

        print baudrate, baudrate_offset, br_actual, bw_desired, bw_actual

    def calc_rx_freq_dev_actual(self, model):
        """
        given register settings calculate actual frequency deviation
        the PHY nominally expects in the receive path.

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        fxo = model.vars.xtal_frequency.value * 1.0
        dec0 = model.vars.dec0_actual.value
        dec1 = model.vars.dec1_actual.value
        dec2 = model.vars.dec2_actual.value
        gain = model.vars.freq_gain_actual.value
        mod_format = model.vars.modulation_type.value
        src1ratio = model.vars.src1_ratio_actual.value
        src2ratio = model.vars.src2_ratio_actual.value

        # frequency deviation only used for 2-FSK and 4-FSK modulation
        deviation = 0.0

        if gain > 0:
            if mod_format == model.vars.modulation_type.var_enum.FSK2:
                deviation = fxo * src1ratio * src2ratio / (4.0 * gain * dec0 * dec1 * dec2)
            elif mod_format == model.vars.modulation_type.var_enum.FSK4:
                deviation = fxo * src1ratio * src2ratio / (8.0 * gain * dec0 * dec1 * dec2)

        model.vars.rx_deviation_actual.value = deviation

    def calc_freq_gain_value(self, model):
        """
        calculate desired frequency gain
        Using Equation (5.22) and (5.23) of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        fxo = model.vars.xtal_frequency.value * 1.0
        freq_offset = model.vars.freq_offset_hz.value * 1.0
        freq_dev_hz = model.vars.deviation.value
        dec0 = model.vars.dec0_actual.value
        dec1 = model.vars.dec1_actual.value
        dec2 = model.vars.dec2_actual.value
        mod_format = model.vars.modulation_type.value
        src1ratio = model.vars.src1_ratio_actual.value
        src2ratio = model.vars.src2_ratio_actual.value

        # if supported frequency offset is larger than the deviation we should use
        # that to calculate frequency gain to avoid saturation
        if freq_dev_hz != 0 and freq_offset >= freq_dev_hz:
            scale = freq_offset / freq_dev_hz
            freq_dev_hz = freq_offset
        else:
            scale = 1.0

        if freq_dev_hz > 0:
            if mod_format == model.vars.modulation_type.var_enum.FSK2:
                target_freq_gain = fxo * src1ratio * src2ratio / (4.0 * freq_dev_hz * dec0 * dec1 * dec2)
            elif mod_format == model.vars.modulation_type.var_enum.FSK4:
                target_freq_gain = fxo * src1ratio * src2ratio / (8.0 * freq_dev_hz * dec0 * dec1 * dec2)
            else:
                target_freq_gain = 0.0
        else:
            target_freq_gain = 0.0

        model.vars.freq_gain.value = target_freq_gain
        model.vars.freq_gain_scale.value = scale


    def calc_datafilter_reg(self, model):
        """set register for datafilter size
        see DATAFILTER register entry in EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        modformat = model.vars.modulation_type.value
        osr = model.vars.oversampling_rate_actual.value

        # disable datafilter by default
        datafilter = 0

        if modformat == model.vars.modulation_type.var_enum.FSK2 or \
           modformat == model.vars.modulation_type.var_enum.FSK4 or \
           modformat == model.vars.modulation_type.var_enum.OOK or \
           modformat == model.vars.modulation_type.var_enum.ASK or \
           modformat == model.vars.modulation_type.var_enum.BPSK:

            if osr >= 8.5:
                datafilter = 7
            elif osr >= 7.5:
                datafilter = 6
            elif osr >= 6.5:
                datafilter = 5
            elif osr >= 5.5:
                datafilter = 4
            elif osr >= 4.5:
                datafilter = 3
            elif osr >= 3.5:
                datafilter = 2
            elif osr >= 2.5:
                datafilter = 1

        self._reg_write(model.vars.MODEM_CTRL2_DATAFILTER,  datafilter)

    def calc_digmixfreq_reg(self, model):

        #if_analog_hz  = model.vars.if_analog_center_hz.value
        if_analog_hz = model.vars.if_frequency_hz_actual.value
        fxo = model.vars.xtal_frequency.value * 1.0
        dec0 = model.vars.dec0_actual.value

        digmixfreq = int(if_analog_hz * dec0 * pow(2, 20) / fxo)

        if digmixfreq > pow(2, 20) - 1:
            digmixfreq = pow(2, 20) - 1

        self._reg_write(model.vars.MODEM_DIGMIXCTRL_DIGMIXFREQ,  digmixfreq)

    def calc_digmixmode_reg(self, model):

        # always use DIGMIXFREQ mode over legacy CFOSR mode
        self._reg_write(model.vars.MODEM_DIGMIXCTRL_DIGMIXMODE,  1)
        # set to CFOSR register to 0 (divider value 7) by default
        model.vars.cfosr.value = 7

    def calc_if_frequency_actual(self, model):
        return

    def calc_if_center_digital_hz_actual(self, model):
        """calculate the actual IF frequency (IF frequency)
        Equation (5.14) of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        fxo = model.vars.xtal_frequency.value
        dec0 = model.vars.dec0_actual.value
        cfosr = model.vars.cfosr_actual.value
        digmixfreq = model.vars.MODEM_DIGMIXCTRL_DIGMIXFREQ.value
        digmixmode = model.vars.MODEM_DIGMIXCTRL_DIGMIXMODE.value

        if digmixmode:
            if_frequency = fxo * digmixfreq / (dec0 * pow(2, 20))
        else:
            if_frequency = fxo / (dec0 * cfosr)

        model.vars.if_center_digital_hz_actual.value = int(if_frequency)


    def calc_brcalmode_reg(self, model):

        brcalen = model.vars.brcalen.value

        if brcalen:
            self._reg_write(model.vars.MODEM_CTRL5_BRCALMODE, 2)
        else:
            self._reg_write(model.vars.MODEM_CTRL5_BRCALMODE, 0)


    def calc_detdel_reg(self, model):

        brcalen = model.vars.brcalen.value

        if brcalen:
            self._reg_write(model.vars.MODEM_CTRL5_DETDEL, 2)
        else:
            self._reg_write(model.vars.MODEM_CTRL5_DETDEL, 0)
