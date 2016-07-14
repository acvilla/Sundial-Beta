"""
This defines fec configurations and calculations
This file also houses calculations for fields that are affected by multiiple blocks:
  calc_blockwhitemode(): calc_whiten, calc_fec

Calculator functions are pulled by using their names.
Calculator functions must start with "calc_", if they are to be consumed by the framework.
    Or they should be returned by overriding the function:
        def getCalculationList(self):
"""

import inspect
from enum import Enum
from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pyradioconfig.pycalcmodel import ModelVariableFormat, CreateModelVariableEnum
from pyradioconfig.pycalcmodel import ModelVariableEmptyValue, ModelVariableInvalidValueType

class CALC_FEC(ICalculator):

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

        """
        #Inputs
        """
        #TODO Need to expand on this properly
        #CRC POLY
        var = self._addModelVariable(model, 'fec_en', Enum, ModelVariableFormat.DECIMAL, 'List of supported FEC Configurations')
        member_data = [
            ['NONE' , 0, 'No CRC'],
            ['FEC_154G',  1, 'Configure the chip for 15.4G FEC settings'],
            ['FEC_154G_K7',  2, 'Configure the chip for 15.4G FEC settings with K=7'],
        ]
        var.var_enum = CreateModelVariableEnum(
            'FECEnum',
            'List of supported FEC Configurations',
            member_data)

        """
        #Outputs
        """
        self._addModelRegister(model, 'FRC.FECCTRL.CONVMODE', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FECCTRL.CONVDECODEMODE', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FECCTRL.CONVTRACEBACKDISABLE', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FECCTRL.CONVINV', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FECCTRL.INTERLEAVEMODE', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FECCTRL.INTERLEAVEFIRSTINDEX', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FECCTRL.INTERLEAVEWIDTH', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FECCTRL.CONVBUSLOCK', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FECCTRL.CONVSUBFRAMETERMINATE', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FECCTRL.SINGLEBLOCK', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FECCTRL.FORCE2FSK', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FECCTRL.CONVHARDERROR', int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'FRC.CONVRAMADDR.CONVRAMADDR', int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'FRC.TRAILTXDATACTRL.TRAILTXDATA', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.TRAILTXDATACTRL.TRAILTXDATACNT', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.TRAILTXDATACTRL.TRAILTXDATAFORCE', int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'FRC.CONVGENERATOR.GENERATOR0', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.CONVGENERATOR.GENERATOR1', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.CONVGENERATOR.RECURSIVE', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.CONVGENERATOR.NONSYSTEMATIC', int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'FRC.PUNCTCTRL.PUNCT0', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.PUNCTCTRL.PUNCT1', int, ModelVariableFormat.HEX )

    def _calc_init(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        self._reg_write(model.vars.FRC_FECCTRL_CONVMODE, 0)
        self._reg_write(model.vars.FRC_FECCTRL_CONVDECODEMODE, 0)
        self._reg_write(model.vars.FRC_FECCTRL_CONVTRACEBACKDISABLE, 0)
        self._reg_write(model.vars.FRC_FECCTRL_CONVINV, 0)
        self._reg_write(model.vars.FRC_FECCTRL_INTERLEAVEMODE, 0)
        self._reg_write(model.vars.FRC_FECCTRL_INTERLEAVEFIRSTINDEX, 0)
        self._reg_write(model.vars.FRC_FECCTRL_INTERLEAVEWIDTH, 0)
        self._reg_write(model.vars.FRC_FECCTRL_CONVBUSLOCK, 0)
        self._reg_write(model.vars.FRC_FECCTRL_CONVSUBFRAMETERMINATE, 0)
        self._reg_write(model.vars.FRC_FECCTRL_SINGLEBLOCK, 0)
        self._reg_write(model.vars.FRC_FECCTRL_FORCE2FSK, 0)
        self._reg_write(model.vars.FRC_FECCTRL_CONVHARDERROR, 0)

        self._reg_write(model.vars.FRC_CONVRAMADDR_CONVRAMADDR, 0)

        self._reg_write(model.vars.FRC_TRAILTXDATACTRL_TRAILTXDATA, 0)
        self._reg_write(model.vars.FRC_TRAILTXDATACTRL_TRAILTXDATACNT, 0)
        self._reg_write(model.vars.FRC_TRAILTXDATACTRL_TRAILTXDATAFORCE, 0)

        self._reg_write(model.vars.FRC_CONVGENERATOR_GENERATOR0, 0)
        self._reg_write(model.vars.FRC_CONVGENERATOR_GENERATOR1, 0)
        self._reg_write(model.vars.FRC_CONVGENERATOR_RECURSIVE, 0)
        self._reg_write(model.vars.FRC_CONVGENERATOR_NONSYSTEMATIC, 0)

        self._reg_write(model.vars.FRC_PUNCTCTRL_PUNCT0, 0)
        self._reg_write(model.vars.FRC_PUNCTCTRL_PUNCT1, 0)

    def _FEC_154G_Base(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        self._reg_write(model.vars.FRC_FECCTRL_CONVMODE, 1)
        self._reg_write(model.vars.FRC_FECCTRL_CONVDECODEMODE, 0)
        self._reg_write(model.vars.FRC_FECCTRL_CONVTRACEBACKDISABLE, 0)
        self._reg_write(model.vars.FRC_FECCTRL_CONVINV, 0)
        self._reg_write(model.vars.FRC_FECCTRL_INTERLEAVEMODE, 1)
        self._reg_write(model.vars.FRC_FECCTRL_INTERLEAVEFIRSTINDEX, 0)
        self._reg_write(model.vars.FRC_FECCTRL_INTERLEAVEWIDTH, 0)
        self._reg_write(model.vars.FRC_FECCTRL_CONVBUSLOCK, 0)
        self._reg_write(model.vars.FRC_FECCTRL_CONVSUBFRAMETERMINATE, 0)
        self._reg_write(model.vars.FRC_FECCTRL_SINGLEBLOCK, 0)
        self._reg_write(model.vars.FRC_FECCTRL_FORCE2FSK, 0)
        self._reg_write(model.vars.FRC_FECCTRL_CONVHARDERROR, 0)

        self._reg_write(model.vars.FRC_CONVRAMADDR_CONVRAMADDR, (0x7C00 >> 2))

        self._reg_write(model.vars.FRC_TRAILTXDATACTRL_TRAILTXDATA, 0)
        self._reg_write(model.vars.FRC_TRAILTXDATACTRL_TRAILTXDATACNT, 0)
        self._reg_write(model.vars.FRC_TRAILTXDATACTRL_TRAILTXDATAFORCE, 0)

        self._reg_write(model.vars.FRC_CONVGENERATOR_GENERATOR0, 0x0D)
        self._reg_write(model.vars.FRC_CONVGENERATOR_GENERATOR1, 0x0E)
        self._reg_write(model.vars.FRC_CONVGENERATOR_RECURSIVE, 0)
        self._reg_write(model.vars.FRC_CONVGENERATOR_NONSYSTEMATIC, 0)

        self._reg_write(model.vars.FRC_PUNCTCTRL_PUNCT0, 1)
        self._reg_write(model.vars.FRC_PUNCTCTRL_PUNCT1, 1)

    def calc_fec(self, model):
        """calc_fec

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        self._calc_init(model)
        if model.vars.fec_en.value == model.vars.fec_en.var_enum.FEC_154G:
            self._FEC_154G_Base(model)

        elif (model.vars.fec_en.value == model.vars.fec_en.var_enum.FEC_154G_K7):
            self._FEC_154G_Base(model)
            self._reg_write(model.vars.FRC_CONVGENERATOR_GENERATOR0, 0x6D)
            self._reg_write(model.vars.FRC_CONVGENERATOR_GENERATOR1, 0x4F)



