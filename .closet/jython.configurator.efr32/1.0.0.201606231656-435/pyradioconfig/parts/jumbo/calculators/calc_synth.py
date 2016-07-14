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
from pyradioconfig.parts.common.calculators.calc_synth import CALC_Synth

class CALC_Synth_jumbo(CALC_Synth):

    """
    Init internal variables
    """
    def __init__(self):
        self._major = 1
        self._minor = 0
        self._patch = 0


    def calc_iffreq_reg(self, model):
        """
        calculate IFFREQ register based on\n
        Equation (5.37) of EFR32 Reference Manual (internal.pdf)\n
        IFFREQ = f_IF / res
        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        res = model.vars.synth_res_actual.value

        # if IF frequency was forced we want to set the digital IF frequencies
        # to the forced value. If not we want to set it to the value of the analog
        # IF center frequency
        if model.vars.if_frequency_hz.value_forced == None:
            f_if = model.vars.if_center_analog_hz_actual.value
        else:
            f_if = model.vars.if_frequency_hz.value

        # calculate if frequency
        iffreq = math.floor(f_if / res)

        self._reg_write(model.vars.SYNTH_IFFREQ_IFFREQ,  int(iffreq))


    def calc_if_frequency_actual(self, model):
        """calculate the actual IF frequency (IF frequency)
        Equation (5.14) of EFR32 Reference Manual (internal.pdf)

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        iffreq = model.vars.SYNTH_IFFREQ_IFFREQ.value
        res = model.vars.synth_res_actual.value

        model.vars.if_frequency_hz_actual.value = int(iffreq * res)

