"""
This provides values specific to image rejection calibration (ir cal).

"""
"""
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

class CALC_IrCal(ICalculator):

    """
    Init internal variables
    """
    def __init__(self):
        self._major = 1
        self._minor = 0
        self._patch = 0

        self.bandFreqs = [2400000000    , 915000000     , 868000000     , 490000000     , 434000000     , 315000000     , 169000000     ]
        self.auxNDiv   = {2400000000 : 0, 915000000 : 71, 868000000 : 69, 490000000 : 76, 434000000 : 68, 315000000 : 49, 169000000 : 53}
        self.auxLoDiv  = {2400000000 : 0, 915000000 :  3, 868000000 :  3, 490000000 :  6, 434000000 :  6, 315000000 :  6, 169000000 : 12}
        self.rampVal   = 6
        self.rxAmpPll  = 4
        self.rxAmpPa   = 16

        self.manufConfigIsValid = {2400000000 :  True, 915000000 : True, 868000000 : True, 490000000 : False, 434000000 : False, 315000000 : False, 169000000 : False}
        self.pllConfigIsValid   = {2400000000 : False, 915000000 : True, 868000000 : True, 490000000 :  True, 434000000 :  True, 315000000 :  True, 169000000 :  True}
        self.paConfigIsVaid     = {2400000000 : False, 915000000 : True, 868000000 : True, 490000000 :  True, 434000000 :  True, 315000000 :  True, 169000000 :  True}
        # self.bestConfig        = ...see method _calc_ircal_determine_best_config

        # for Software Averaging
        self.sw_useSwRssiAveraging   = True
        self.sw_numRssiToAvg         = 6 # = 2^*6* = 64
        self.sw_throwAwayBeforeRssi  = 0
        self.sw_delayUsBeforeRssi    = 10000
        self.sw_delayUsBetweenSwRssi = 0
        # for Hardware Averaging 
        self.hw_useSwRssiAveraging   = False
        self.hw_numRssiToAvg         = 2 # = 2^*2* = 4
        self.hw_throwAwayBeforeRssi  = 2
        self.hw_delayUsBeforeRssi    = 0
        self.hw_delayUsBetweenSwRssi = 0

    def _calc_ircal_determine_best_config(self, model, bandFreq):
        bestConfig = {2400000000 : model.vars.ircal_bestconfig.var_enum.MANUFACTURING,
                       915000000 : model.vars.ircal_bestconfig.var_enum.PA,
                       868000000 : model.vars.ircal_bestconfig.var_enum.PA,
                       490000000 : model.vars.ircal_bestconfig.var_enum.PA,
                       434000000 : model.vars.ircal_bestconfig.var_enum.PLL, 
                       315000000 : model.vars.ircal_bestconfig.var_enum.PLL, 
                       169000000 : model.vars.ircal_bestconfig.var_enum.PLL}
        return bestConfig[bandFreq]

    def buildVariables(self, model):
        """Populates a list of needed variables for this calculator

        Args:
            model (ModelRoot) : Builds the variables specific to this calculator
        """

        """
        #Inputs
        """

        """
        #Outputs
        """
        #-------- Register Settings Used During Calibration --------
        #auxNDiv (to be put into synth.auxfreq.mmddenom during ir cal only)
        self._addModelVariable(model, 'ircal_auxndiv', int, ModelVariableFormat.DECIMAL, units='bytes', desc='This value is predetermined.')
        #auxLoDiv (to be put into  synth.divctrl.auxlodivfreqctrl during ir cal only)
        self._addModelVariable(model, 'ircal_auxlodiv', int, ModelVariableFormat.DECIMAL, units='bytes', desc='This value is predetermined.')
        #rampVal (to be put into modem.rampctrl.rampval during ir cal only)
        self._addModelVariable(model, 'ircal_rampval', int, ModelVariableFormat.DECIMAL, units='bytes', desc='This value is predetermined.')
        #rxAmp_PLL (to be put into rac.auxctrl.rxamp during PLL loopback, ir cal only)
        self._addModelVariable(model, 'ircal_rxamppll', int, ModelVariableFormat.DECIMAL, units='bytes', desc='This value is predetermined.')
        #rxAmp_PA (to be put into rac.auxctrl.rxamp during PA loopback, ir cal only)
        self._addModelVariable(model, 'ircal_rxamppa', int, ModelVariableFormat.DECIMAL, units='bytes', desc='This value is predetermined.')
        
        #-------- Decide Between Calibration Procedures --------
        #diConfigIsValid (true = DI value / PTE value is an option)
        self._addModelVariable(model, 'ircal_manufconfigvalid', bool, ModelVariableFormat.ASCII, 'True = the manufacturing calibration value is saved on the chip')
        #pllLoopbackConfigIsValid (true = PLL loopback is an option)
        self._addModelVariable(model, 'ircal_pllconfigvalid', bool, ModelVariableFormat.ASCII, 'True = PLL loopback is permitted to generate a calibration value')
        #paLoopbackConfigIsValid (true = PA loopback is an option)
        self._addModelVariable(model, 'ircal_paconfigvalid', bool, ModelVariableFormat.ASCII, 'True = PA loopback is permitted to generate a calibration value')
        #recommendedConfig (DI/PTE vs PLL loopback vs PA loopback)
        var = self._addModelVariable(model, 'ircal_bestconfig', Enum, ModelVariableFormat.DECIMAL, 'Specify the best calibration method for this radio configuration.')
        member_data = [
            ['MANUFACTURING',  1, 'Use the calibration value saved during manufacturing, if applicable.'],
            ['PLL',  2, 'Put the part into a PLL loopback to generate a calibration value.'],
            ['PA',  3, 'Put the part into a PA loopback to generate a calibration value.'],
            ['UNSUPPORTED',  4, 'Image rejection calibration not supported.'],
        ]
        var.var_enum = CreateModelVariableEnum(
            'configType',
            'Specify how image rejection calibration is to run.',
            member_data)

        #-------- Decide Between Software/Hardware RSSI Averaging --------
        #useSwRssiAveraging (as opposed to HW averaging; HW is preferred but it wasn't validated first)
        self._addModelVariable(model, 'ircal_useswrssiaveraging', bool, ModelVariableFormat.ASCII, 'True = use software RSSI averaging; False = use hardware RSSI averaging')
        #numRssiToAvg
        self._addModelVariable(model, 'ircal_numrssitoavg', int, ModelVariableFormat.DECIMAL, units='bytes', desc='Number of RSSI values (2^value) to average in software. If value = 3, 8 values will be averaged.')
        #throwAwayBeforeRssi
        self._addModelVariable(model, 'ircal_throwawaybeforerssi', int, ModelVariableFormat.DECIMAL, units='bytes', desc='Number of RSSI values to discard before starting to average RSSI values.')
        #delayUsBeforeRssi
        self._addModelVariable(model, 'ircal_delayusbeforerssi', int, ModelVariableFormat.DECIMAL, units='bytes', desc='Microsecond delay between applying a calibration value and then reading RSSI values.')
        #delayUsBetweenSwRssi
        self._addModelVariable(model, 'ircal_delayusbetweenswrssi', int, ModelVariableFormat.DECIMAL, units='bytes', desc='Microsecond delay between gathering RSSI values. Software RSSI averaging mode only.')

    def calc_ircal_datarate_considerations(self, model):
        bitrate = model.vars.bitrate.value

        # Dumbo: for datarate below 10Kbps, use HW averaging (per Euisoo Yoo, 2016-5-11)
        if bitrate >= 10000:
            model.vars.ircal_useswrssiaveraging.value = self.sw_useSwRssiAveraging
            model.vars.ircal_numrssitoavg.value = self.sw_numRssiToAvg
            model.vars.ircal_throwawaybeforerssi.value = self.sw_throwAwayBeforeRssi
            model.vars.ircal_delayusbeforerssi.value = self.sw_delayUsBeforeRssi
            model.vars.ircal_delayusbetweenswrssi.value = self.sw_delayUsBetweenSwRssi
        else:
            model.vars.ircal_useswrssiaveraging.value = self.hw_useSwRssiAveraging
            model.vars.ircal_numrssitoavg.value = self.hw_numRssiToAvg
            model.vars.ircal_throwawaybeforerssi.value = self.hw_throwAwayBeforeRssi
            model.vars.ircal_delayusbeforerssi.value = self.hw_delayUsBeforeRssi
            model.vars.ircal_delayusbetweenswrssi.value = self.hw_delayUsBetweenSwRssi

    def calc_ircal_common_values(self, model):
        """
        The variable length location must be the last 1 or 2 bytes of the header

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        loDiv = model.vars.lodiv.value
        loSide = model.vars.SYNTH_IFFREQ_LOSIDE.value
        ifFreq = model.vars.SYNTH_IFFREQ_IFFREQ.value
        #rfFreq = model.vars.base_frequency_hz.value
        closestBandFreq = self._calc_ircal_closest_supported_band(model)

        model.vars.ircal_auxndiv.value = self.auxNDiv[closestBandFreq]
        model.vars.ircal_auxlodiv.value = self.auxLoDiv[closestBandFreq]
        model.vars.ircal_rampval.value = self.rampVal
        model.vars.ircal_rxamppll.value = self.rxAmpPll
        model.vars.ircal_rxamppa.value = self.rxAmpPa

        model.vars.ircal_manufconfigvalid.value = self.manufConfigIsValid[closestBandFreq]
        model.vars.ircal_pllconfigvalid.value = self.pllConfigIsValid[closestBandFreq]
        model.vars.ircal_paconfigvalid.value = self.paConfigIsVaid[closestBandFreq]
        model.vars.ircal_bestconfig.value = self._calc_ircal_determine_best_config(model, closestBandFreq)

    def _calc_ircal_closest_supported_band(self, model):
        bandFreqArray = self.bandFreqs
        rfFreq = model.vars.base_frequency_hz.value
        smallestDifference = 0xFFFFFFFF # large number
        closestBandFreq = 0

        for bandFreq in bandFreqArray:
            difference = abs(rfFreq - bandFreq)
            if difference < smallestDifference:
                smallestDifference = difference
                closestBandFreq = bandFreq

        return closestBandFreq
