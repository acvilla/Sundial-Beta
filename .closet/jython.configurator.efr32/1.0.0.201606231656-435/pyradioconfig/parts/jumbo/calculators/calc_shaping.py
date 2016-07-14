"""Core AGC Calculator Package

Calculator functions are pulled by using their names.
Calculator functions must start with "calc_", if they are to be consumed by the framework.
    Or they should be returned by overriding the function:
        def getCalculationList(self):
"""

from collections import OrderedDict
import math

from enum import Enum
from pyradioconfig.pycalcmodel import ModelVariableFormat, CreateModelVariableEnum
from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pyradioconfig.pycalcmodel import ModelVariableFormat
from pyradioconfig.parts.common.utils.tinynumpy import tinynumpy
from pyradioconfig.parts.common.calculators.calc_shaping import CALC_Shaping

class CALC_Shaping_jumbo(CALC_Shaping):

    def gaussian_shaping_filter(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        # for gaussian pulse shapes pulse_shape_parameter holds BT value
        bt = model.vars.shaping_filter_param.value
        # map BT value to standard deviation
        std = 1.05 / bt

        # generate gaussian pulse shape
        w = self.gaussian(17, std)
        # scale for unit DC gain
        w = tinynumpy.divide(w, w.sum())
        # convolve with square wave of oversampling rate width which is 8 for the shaping filter
        f_hack = tinynumpy.convolve(w, tinynumpy.ones((1, 8)).flatten())
        # scale and quantize coefficients
        c_hack = tinynumpy.round_((84.5 * f_hack))
        # keep only first half of 17 coeffs - also skip convolution artifacts
        #coeff = c_hack[4:13]
        coeff = []
        for i in range(4, 14):
            coeff.append(c_hack[i])

        # c8 is not used in gaussian pulse shapes
        coeff[8] = 0.0
        # return coeffs
        return coeff

