"""Core AGC Calculator Package

Calculator functions are pulled by using their names.
Calculator functions must start with "calc_", if they are to be consumed by the framework.
    Or they should be returned by overriding the function:
        def getCalculationList(self):
"""

from collections import OrderedDict
import math
from enum import Enum
from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pyradioconfig.pycalcmodel import ModelVariableFormat, CreateModelVariableEnum
from pyradioconfig.parts.common.calculators.calc_agc import CALC_AGC

class CALC_AGC_jumbo(CALC_AGC):

    """
    Init internal variables
    """
    def __init__(self):
        self._major = 1
        self._minor = 0
        self._patch = 0


    def calc_agc_clock_cycle(self, model):
       return


    def calc_fastloopdel_reg(self, model):
        """calculate FASTLOOPDEL based on corresponding delay

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        fxo = model.vars.xtal_frequency.value
        fast_loop_delay = model.vars.fast_loop_delay.value

        # TODO: add missing -1 to equation once verified
        delay = int(math.ceil(fast_loop_delay * fxo))

        if delay < 0:
            delay = 0
        elif delay > 31:
            delay = 31

        self._reg_write(model.vars.AGC_CTRL2_FASTLOOPDEL, delay)

    def calc_lnaslicesdel_reg(self, model):
        """calculate LNASLICESDEL based on corresponding delay

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        fxo = model.vars.xtal_frequency.value
        lna_slices_delay = model.vars.lna_slices_delay.value

        # TODO: add missing -1 to equation once verified
        delay = int(math.ceil(lna_slices_delay * fxo))

        if delay < 0:
            delay = 0
        elif delay > 31:
            delay = 31

        self._reg_write(model.vars.AGC_LOOPDEL_LNASLICESDEL, delay)

    def calc_ifpgadel_reg(self, model):
        """calculate IFPGADEL based on corresponding delay

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        fxo = model.vars.xtal_frequency.value
        if_pga_delay = model.vars.if_pga_delay.value

        # TODO: add missing -1 to equation once verified
        delay = int(math.ceil(if_pga_delay * fxo))

        if delay < 0:
            delay = 0
        elif delay > 31:
            delay = 31

        self._reg_write(model.vars.AGC_LOOPDEL_IFPGADEL, delay)

    def calc_pkdwait_reg(self, model):
        """calculate PKDWAIT based on agc_speed

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        fxo = model.vars.xtal_frequency.value
        f_if = float(model.vars.if_frequency_hz.value)
        freq_dev_hz = model.vars.deviation.value

        # per guideline in internal document
        wait = fxo / (4 * (f_if - freq_dev_hz))

        if wait < 0:
            wait = 0
        elif wait > 1023:
            wait = 1023

        self._reg_write(model.vars.AGC_LOOPDEL_PKDWAIT, int(wait))


    def calc_slowdecaycnt_reg(self, model):

        mod_format = model.vars.modulation_type.value
        baudrate_hz = model.vars.baudrate.value
        encoding = model.vars.symbol_encoding.value

        if encoding == model.vars.symbol_encoding.var_enum.DSSS or \
           encoding == model.vars.symbol_encoding.var_enum.Manchester:

            reg = 2

        elif mod_format == model.vars.modulation_type.var_enum.FSK2 or \
             mod_format == model.vars.modulation_type.var_enum.FSK4:

            if baudrate_hz > 500e3:
                reg = 2
            else:
                reg = 1

        else:
            reg = 8

        self._reg_write(model.vars.AGC_GAINSTEPLIM_SLOWDECAYCNT, reg)

