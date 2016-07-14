"""
This defines the Whitening variables and calculation

NOTE: calc_whiten has an impact on FRC_FECCTRL_BLOCKWHITEMODE
      This calculation can be found in calc_frame.py since there are multiple blocks
      that impact this field

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

class CALC_Whitening(ICalculator):

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
        #WHITE_POLY
        var = self._addModelVariable(model, 'white_poly', Enum, ModelVariableFormat.DECIMAL, 'List of supported Whitening Polynomials')
        member_data = [
            ['NONE' , 0, 'No Whitening'],
            ['PN9',  1, 'X9+X5+1'],
            ['PN9_BYTE',  2, 'X9+X5+X1'],
            ['PN16', 3, 'X16+X14+X13+X11+1'],
            ['BLE', 4, 'X7+X4+1'],
        ]
        var.var_enum = CreateModelVariableEnum(
            'WhitePolyEnum',
            'List of supported Whitening Polynomials',
            member_data)

        #white_seed
        self._addModelVariable(model, 'white_seed', int, ModelVariableFormat.HEX, 'Whitening Initialization Value')

        #WHITE_OUTPUT_BIT
        var = self._addModelVariable(model, 'white_output_bit', int, ModelVariableFormat.HEX, 'Whitening Output Bit')

        """
        #Outputs
        """
        self._addModelRegister(model, 'FRC.WHITECTRL.SHROUTPUTSEL', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.WHITECTRL.XORFEEDBACK', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.WHITECTRL.FEEDBACKSEL', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.WHITEPOLY.POLY', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.WHITEINIT.WHITEINIT', int, ModelVariableFormat.HEX )

    def _calc_init(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

    def calc_white_settings(self, model):
        """
        This is a dictionary lookup of each of the supported CRC Polynomials\n
        Each dictionary entry is a tuple which maps to the following entries:\n
          (POLY, XORFEEDBACK, FEEDBACKSEL)\n

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        WHITE_POLY_LOOKUP = {
            model.vars.white_poly.var_enum.PN9.value:       ( 0x00000108, 0, 0 ),
            model.vars.white_poly.var_enum.PN9_BYTE.value:  ( 0x00000100, 1, 5 ),
            model.vars.white_poly.var_enum.PN16.value:      ( 0x00008016, 0, 0 ),
            model.vars.white_poly.var_enum.BLE.value:       ( 0x00000044, 0, 0 ),
        }

        if model.vars.ber_force_whitening.value is True:
            self._reg_write(model.vars.FRC_WHITEPOLY_POLY, 0x0100)
            self._reg_write(model.vars.FRC_WHITECTRL_XORFEEDBACK, 1)
            self._reg_write(model.vars.FRC_WHITECTRL_FEEDBACKSEL, 4)
            self._reg_write(model.vars.FRC_WHITEINIT_WHITEINIT, 0x0138)
            self._reg_write(model.vars.FRC_WHITECTRL_SHROUTPUTSEL, 0)

        elif model.vars.white_poly.value.value != model.vars.white_poly.var_enum.NONE.value:
            white_params = WHITE_POLY_LOOKUP[model.vars.white_poly.value.value]
            #Handle POLY configuration
            self._reg_write(model.vars.FRC_WHITEPOLY_POLY, white_params[0])
            # Subtract 1 from the CRC size to get the proper value
            self._reg_write(model.vars.FRC_WHITECTRL_XORFEEDBACK, white_params[1])
            self._reg_write(model.vars.FRC_WHITECTRL_FEEDBACKSEL, white_params[2])

            self._reg_write(model.vars.FRC_WHITEINIT_WHITEINIT, model.vars.white_seed.value)
            self._reg_write(model.vars.FRC_WHITECTRL_SHROUTPUTSEL, model.vars.white_output_bit.value)
            
        else:
            # Defaults if whitening is disabled
            self._reg_write(model.vars.FRC_WHITECTRL_XORFEEDBACK, 0)
            self._reg_write(model.vars.FRC_WHITECTRL_FEEDBACKSEL, 0)
            self._reg_write(model.vars.FRC_WHITEINIT_WHITEINIT, 0)
            
            # There's some code in calc_frame that might set the following.
            # So only set them here if we aren't going to set them there.
            if ((model.vars.frame_coding.value == model.vars.frame_coding.var_enum.NONE.value or
                 model.vars.frame_coding.value == model.vars.frame_coding.var_enum.UART_NO_VAL.value)
            ):
                self._reg_write(model.vars.FRC_WHITEPOLY_POLY, 0)
                self._reg_write(model.vars.FRC_WHITECTRL_SHROUTPUTSEL, 0)
        
        
        return

        
