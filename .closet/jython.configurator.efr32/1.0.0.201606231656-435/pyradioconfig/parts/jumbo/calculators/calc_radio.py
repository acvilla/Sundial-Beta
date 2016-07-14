"""Core CALC_Radio Calculator Package

Calculator functions are pulled by using their names.
Calculator functions must start with "calc_", if they are to be consumed by the framework.
    Or they should be returned by overriding the function:
        def getCalculationList(self):
"""

from collections import OrderedDict
#import math
from enum import Enum
from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pyradioconfig.pycalcmodel import ModelVariableFormat, CreateModelVariableEnum
from pyradioconfig.parts.common.calculators.calc_radio import CALC_Radio

class CALC_Radio_jumbo(CALC_Radio):

    """
    Init internal variables
    """
    def __init__(self):
        self._major = 1
        self._minor = 0
        self._patch = 0

    def calc_if_frequency_hz_value(self, model):
        """
        calculate smallest IF frequency that analog filter can be centered\n
        at and that works with calculated bandwidth.
        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        bw_analog = model.vars.iffilt_bandwidth_actual.value
        bw_digital = model.vars.bandwidth_actual.value

        # loop over all possible center frequencies the analog filter
        # can be centered around given analog filter bandwidths
        for ratio_reg, ratio in self.iffilt_ratio.iteritems():

            f_if = bw_analog * ratio

            # pick first setting that ensures the lower edge of the band
            # is beyond 107 KHz lower threshold
            if f_if - bw_digital / 2.0 > 107e3:
                break

        model.vars.if_frequency_hz.value = int(f_if)

    def calc_iffilt_ratio_reg(self, model):
        """
        calculate CENTFREQ register setting given desired IF frequency and\n
        analog filter bandwidths already decided. \n
        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        bw_analog = model.vars.iffilt_bandwidth_actual.value
        f_if = float(model.vars.if_frequency_hz.value)

        ratio_target = f_if / bw_analog

        best_error = 99

        # loop over all ratios and find best closest to target ratio
        for ratio_reg, ratio in self.iffilt_ratio.iteritems():

            error = abs(ratio - ratio_target)
            if error < best_error:
                best_error = error
                best_ratio_reg = ratio_reg

        self._reg_write(model.vars.RAC_IFFILTCTRL_CENTFREQ, best_ratio_reg)


    def calc_if_center_analog_hz_actual(self, model):
        """
        given analog filter bandwidths and ration calculated actual IF \n
        center frequency for analog filters.
        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        bw_analog = model.vars.iffilt_bandwidth_actual.value
        ratio = model.vars.iffilt_ratio_actual.value

        model.vars.if_center_analog_hz_actual.value = int(bw_analog * ratio)


    def calc_reg_lpfbwtx_lpfbwrx(self, model):
        """
        Write the rx and tx sequencer registers for the SYNTH_LPFCTRL register

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        pll_bandwidth_tx = model.vars.pll_bandwidth_tx.value.value
        pll_bandwidth_rx = model.vars.pll_bandwidth_rx.value.value

        self._reg_write(model.vars.RAC_LPFCTRL_LPFBWRX,  pll_bandwidth_rx)
        self._reg_write(model.vars.RAC_LPFCTRL_LPFBWTX,  pll_bandwidth_tx)
