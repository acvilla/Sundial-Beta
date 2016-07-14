"""CALC_Firmware Package

Calculator functions are pulled by using their names.
Calculator functions must start with "calc_", if they are to be consumed by the framework.
    Or they should be returned by overriding the function:
        def getCalculationList(self):
"""

from collections import OrderedDict
import math
from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pyradioconfig.pycalcmodel import ModelVariableFormat

class CALC_Firmware(ICalculator):

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

        # Output fields
        self._addModelRegister(model, 'MODEM.RAMPLEV.RAMPLEV0'          , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.RAMPLEV.RAMPLEV1'          , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.RAMPLEV.RAMPLEV2'          , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'RAC.LPFCTRL.LPFBW'               , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'CRC.CMD.INITIALIZE'              , int, ModelVariableFormat.HEX )

        #Reserve FRC_RXCTRL register
        self._addModelRegister(model, 'FRC.RXCTRL.STORECRC', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.RXCTRL.ACCEPTCRCERRORS', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.RXCTRL.ACCEPTBLOCKERRORS', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.RXCTRL.TRACKABFRAME', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.RXCTRL.BUFCLEAR', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.RXCTRL.BUFRESTOREFRAMEERROR', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.RXCTRL.BUFRESTORERXABORTED', int, ModelVariableFormat.HEX )


    def calc_reserve_fields(self, model):
        """calc_reserve_fields

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        model.vars.MODEM_RAMPLEV_RAMPLEV0.value = None
        model.vars.MODEM_RAMPLEV_RAMPLEV1.value = None
        model.vars.MODEM_RAMPLEV_RAMPLEV2.value = None
        model.vars.RAC_LPFCTRL_LPFBW.value = None
        model.vars.CRC_CMD_INITIALIZE.value = None

        model.vars.FRC_RXCTRL_STORECRC.value = None
        model.vars.FRC_RXCTRL_ACCEPTCRCERRORS.value = None
        model.vars.FRC_RXCTRL_ACCEPTBLOCKERRORS.value = None
        model.vars.FRC_RXCTRL_TRACKABFRAME.value = None
        model.vars.FRC_RXCTRL_BUFCLEAR.value = None
        model.vars.FRC_RXCTRL_BUFRESTOREFRAMEERROR.value = None
        model.vars.FRC_RXCTRL_BUFRESTORERXABORTED.value = None

