""" CALC_Global_jumbo Package

JUMBO specific global calculator functions live here.

Calculator functions are pulled by using their names.
Calculator functions must start with "calc_", if they are to be consumed by the framework.
    Or they should be rturned by overriding the function:
        def getCalculationList(self):
"""

from pyradioconfig.parts.common.calculators.calc_global import CALC_Global
from pyradioconfig.pycalcmodel import ModelVariableFormat, CreateModelVariableEnum
from enum import Enum


class CALC_Global_jumbo(CALC_Global):


    def buildAdditionalVariables(self, model):
        """Populates a list of needed variables for this calculator

        Args:
            model (ModelRoot) : Builds the variables specific to this calculator
        """

        # Inputs

        # Output fields
        self._addModelRegister(model, 'MODEM.SRCCHF.SRCRATIO1',           int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.SRCCHF.SRCENABLE1',          int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.SRCCHF.SRCRATIO2',           int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.SRCCHF.SRCENABLE2',          int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.SRCCHF.BWSEL',               int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.SRCCHF.INTOSR',              int, ModelVariableFormat.HEX)

        self._addModelRegister(model, 'AGC.GAINSTEPLIM.EN2XFASTSTEPDOWN', int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'AGC.GAINSTEPLIM.SLOWDECAYCNT',     int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'AGC.GAINSTEPLIM.ADCATTENCODE',     int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'AGC.GAINSTEPLIM.ADCATTENMODE',     int, ModelVariableFormat.HEX)

        self._addModelRegister(model, 'MODEM.VITERBIDEMOD.VTDEMODEN',     int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VITERBIDEMOD.HARDDECISION',  int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VITERBIDEMOD.VITERBIKSI1',   int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VITERBIDEMOD.VITERBIKSI2',   int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VITERBIDEMOD.VITERBIKSI3',   int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VITERBIDEMOD.SYNTHAFC',      int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VITERBIDEMOD.CORRCYCLE',     int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VITERBIDEMOD.CORRSTPSIZE',   int, ModelVariableFormat.HEX)

        self._addModelRegister(model, 'MODEM.VTCORRCFG0.EXPECTPATT',      int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VTCORRCFG0.EXPSYNCLEN',      int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VTCORRCFG0.BUFFHEAD',        int, ModelVariableFormat.HEX)

        self._addModelRegister(model, 'MODEM.VTCORRCFG1.CORRSHFTLEN',     int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VTCORRCFG1.VTFRQLIM',        int, ModelVariableFormat.HEX)

        self._addModelRegister(model, 'MODEM.VTTRACK.FREQTRACKMODE',      int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VTTRACK.TIMTRACKTHD',        int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VTTRACK.TIMEACQUTHD',        int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VTTRACK.TIMCHK',             int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VTTRACK.TIMEOUTMODE',        int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VTTRACK.TIMGEAR',            int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.VTTRACK.FREQBIAS',           int, ModelVariableFormat.HEX)

        self._addModelRegister(model, 'MODEM.CTRL0.DUALCORROPTDIS',       int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'MODEM.CTRL4.SOFTDSSSMODE',       int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'MODEM.CTRL5.DSSSCTD'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL5.BBSS'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL5.POEPER'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL5.FOEPREAVG'	     , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL5.LINCORR'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL5.PRSDEBUG'	     , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL5.RESYNCBAUDTRANS'	 , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL5.RESYNCLIMIT'	     , int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'MODEM.CTRL6.TDREW'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL6.PREBASES'	     , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL6.PSTIMABORT0'	     , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL6.PSTIMABORT1'	     , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL6.PSTIMABORT2'	     , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL6.PSTIMABORT3'	     , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL6.ARW'	             , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL6.TIMTHRESHGAIN'	 , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL6.CPLXCORREN'	     , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL6.RXBRCALCDIS'	     , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.CTRL6.DEMODRESTARTALL'	 , int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'MODEM.DSATHD0.SPIKETHD',           int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSATHD0.UNMODTHD',           int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSATHD0.FDEVMINTHD',         int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSATHD0.FDEVMAXTHD',         int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSATHD1.POWABSTHD',          int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSATHD1.POWRELTHD',          int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSATHD1.DSARSTCNT',          int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSATHD1.RSSIJMPTHD',         int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSATHD1.FREQLATDLY',         int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSATHD1.PWRFLTBYP',          int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSATHD1.AMPFLTBYP',          int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSATHD1.PWRDETDIS',          int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSATHD1.FREQSCALE',          int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSACTRL.DSAMODE',            int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSACTRL.ARRTHD',             int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSACTRL.ARRTOLERTHD0',       int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSACTRL.ARRTOLERTHD1',       int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSACTRL.SCHPRD',             int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSACTRL.FREQAVGSYM',         int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSACTRL.DSARSTON',           int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSACTRL.TIMEST',             int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSACTRL.AGCDEBOUNDLY',       int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSACTRL.LOWDUTY',            int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSACTRL.AGCBAUDEN',          int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DSACTRL.RESTORE',            int, ModelVariableFormat.HEX)

        self._addModelRegister(model, 'MODEM.DIGMIXCTRL.DIGMIXFREQ',      int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.DIGMIXCTRL.DIGMIXMODE',      int, ModelVariableFormat.HEX)

        self._addModelRegister(model, 'MODEM.AFC.AFCONESHOT',              int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.AFC.AFCDELDET',               int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.AFC.AFCDSAFREQOFFEST',        int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.AFC.AFCENINTCOMP',            int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.AFC.AFCLIMRESET',             int, ModelVariableFormat.HEX)

        self._addModelRegister(model, 'RAC.LPFCTRL.LPFBWRX',               int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'RAC.LPFCTRL.LPFBWTX',               int, ModelVariableFormat.HEX)

        self._addModelRegister(model, 'MODEM.INTAFC.FOEPREAVG0',           int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.INTAFC.FOEPREAVG1',           int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.INTAFC.FOEPREAVG2',           int, ModelVariableFormat.HEX)
        self._addModelRegister(model, 'MODEM.INTAFC.FOEPREAVG3',           int, ModelVariableFormat.HEX)

        self._addModelRegister(model, 'MODEM.CGCLKSTOP.FORCEOFF', int, ModelVariableFormat.HEX)

        self._addModelRegister(model, 'MODEM.SHAPING2.COEFF9'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING2.COEFF10'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING2.COEFF11'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING3.COEFF12'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING3.COEFF13'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING3.COEFF14'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING3.COEFF15'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING4.COEFF16'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING4.COEFF17'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING4.COEFF18'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING4.COEFF19'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING4.COEFF20'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING4.COEFF21'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING5.COEFF22'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING5.COEFF23'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING5.COEFF24'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING5.COEFF25'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING5.COEFF26'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING5.COEFF27'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING5.COEFF28'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING5.COEFF29'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING6.COEFF30'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING6.COEFF31'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING6.COEFF32'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING6.COEFF33'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING6.COEFF34'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING6.COEFF35'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING6.COEFF36'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING6.COEFF37'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING6.COEFF38'	         , int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'MODEM.SHAPING6.COEFF39'	         , int, ModelVariableFormat.HEX )


        # Internal variable
        self._addModelVariable(model, 'src1',                             int,   ModelVariableFormat.DECIMAL)
        self._addModelVariable(model, 'src2',                             int,   ModelVariableFormat.DECIMAL)
        self._addModelVariable(model, 'bwsel',                            float, ModelVariableFormat.DECIMAL)
        self._addModelVariable(model, 'if_center_analog_hz',              int,   ModelVariableFormat.DECIMAL)
        self._addModelVariable(model, 'src_disable',                      int,   ModelVariableFormat.DECIMAL)
        self._addModelVariable(model, 'viterbi_enable',                   int,   ModelVariableFormat.DECIMAL)
        self._addModelVariable(model, 'dsa_enable', int, ModelVariableFormat.DECIMAL)
        self._addModelVariable(model, 'target_osr', int, ModelVariableFormat.DECIMAL)

        var = self._addModelVariable(model, 'afc_run_mode', Enum, ModelVariableFormat.DECIMAL, 'AFC run mode')
        member_data = [
            ['CONTINUOUS', 0, 'Run AFC Continuously'],
            ['ONE_SHOT',   1, 'One-shot AFC update based on "Frequency Compensation Mode" selected.'],
        ]
        var.var_enum = CreateModelVariableEnum(
            'AfcRunMode',
            'List of supported AFC Run Modes',
            member_data)

        # Variables for the reverse path
        self._addModelActual(model,   'src1_ratio',                       float, ModelVariableFormat.DECIMAL)
        self._addModelActual(model,   'src2_ratio',                       float, ModelVariableFormat.DECIMAL)
        self._addModelActual(model,   'bwsel',                            float, ModelVariableFormat.DECIMAL)
        self._addModelActual(model,   'if_center_analog_hz',              int,   ModelVariableFormat.DECIMAL)
        self._addModelActual(model,   'if_center_digital_hz',             int,   ModelVariableFormat.DECIMAL)
        self._addModelActual(model,   'afc_lim_reset',                    int,   ModelVariableFormat.DECIMAL)



    # Example override
    #def calc.global.hello.world(self, model):
    #    print("HELLO from Jumbo Calculator!")