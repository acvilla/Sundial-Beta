"""Core CALC_Misc Package

Calculator functions are pulled by using their names.
Calculator functions must start with "calc_", if they are to be consumed by the framework.
    Or they should be returned by overriding the function:
        def getCalculationList(self):
"""

import inspect
from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pyradioconfig.pycalcmodel import ModelVariableFormat

class CALC_Misc(ICalculator):

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
        self._addModelRegister(model, 'MODEM.CTRL0.FDM0DIFFDIS'        , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL0.FRAMEDETDEL'        , int, ModelVariableFormat.HEX )


        self._addModelRegister(model, 'MODEM.CTRL1.SYNC1INV'           , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL1.SYNCERRORS'         , int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'MODEM.CTRL2.BRDIVA'             , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL2.BRDIVB'             , int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'MODEM.CTRL4.ADCSATDENS'         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL4.ADCSATLEVEL'        , int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'MODEM.CTRL5.BRCALMODE'          , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL5.DETDEL'	         , int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'MODEM.PRE.DSSSPRE'              , int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'MODEM.TIMING.FASTRESYNC'        , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.TIMING.TIMSEQSYNC'        , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.TIMING.TSAGCDEL'          , int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'MODEM.AFC.AFCTXMODE'            , int, ModelVariableFormat.HEX )


    def calc_misc(self, model):
        """
        These aren't really calculating right now.  Just using defaults or forced values.

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        self._reg_write(model.vars.MODEM_CTRL0_FRAMEDETDEL, 0)
        self._reg_write(model.vars.MODEM_CTRL0_FDM0DIFFDIS, 0)

        self._reg_write(model.vars.MODEM_CTRL1_SYNCERRORS, 0)
        self._reg_write(model.vars.MODEM_CTRL1_SYNC1INV, 0)

    
        self._reg_write(model.vars.MODEM_CTRL2_BRDIVB, 0)
        self._reg_write(model.vars.MODEM_CTRL2_BRDIVA, 0)
                                                                    
        self._reg_write(model.vars.MODEM_CTRL4_ADCSATDENS, 0)
        self._reg_write(model.vars.MODEM_CTRL4_ADCSATLEVEL, 6)
        
        self._reg_write(model.vars.MODEM_CTRL5_DETDEL, 0)
        self._reg_write(model.vars.MODEM_CTRL5_BRCALMODE, 0)
    
        self._reg_write(model.vars.MODEM_PRE_DSSSPRE, 0)
                                                                    
        self._reg_write(model.vars.MODEM_TIMING_TSAGCDEL, 0)
        self._reg_write(model.vars.MODEM_TIMING_TIMSEQSYNC, 0)
        self._reg_write(model.vars.MODEM_TIMING_FASTRESYNC, 0)
    
        self._reg_write(model.vars.MODEM_AFC_AFCTXMODE,       0)

        self._reg_write(model.vars.SEQ_MISC_SQBMODETX, 0)









