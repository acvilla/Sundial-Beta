
from static import Base_RM_Register
from CMU_field import *


class RM_Register_CMU_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_CTRL, self).__init__(rmio, label,
            0x400e4000, 0x000,
            'CTRL', 'CMU.CTRL', 'read-write',
            "",
            0x00300000, 0x003101EF)

        self.CLKOUTSEL0 = RM_Field_CMU_CTRL_CLKOUTSEL0(self)
        self.zz_fdict['CLKOUTSEL0'] = self.CLKOUTSEL0
        self.CLKOUTSEL1 = RM_Field_CMU_CTRL_CLKOUTSEL1(self)
        self.zz_fdict['CLKOUTSEL1'] = self.CLKOUTSEL1
        self.WSHFLE = RM_Field_CMU_CTRL_WSHFLE(self)
        self.zz_fdict['WSHFLE'] = self.WSHFLE
        self.HFPERCLKEN = RM_Field_CMU_CTRL_HFPERCLKEN(self)
        self.zz_fdict['HFPERCLKEN'] = self.HFPERCLKEN
        self.HFRADIOCLKEN = RM_Field_CMU_CTRL_HFRADIOCLKEN(self)
        self.zz_fdict['HFRADIOCLKEN'] = self.HFRADIOCLKEN
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFRCOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFRCOCTRL, self).__init__(rmio, label,
            0x400e4000, 0x010,
            'HFRCOCTRL', 'CMU.HFRCOCTRL', 'read-write',
            "",
            0xB1481F3C, 0xFFFF3F7F)

        self.TUNING = RM_Field_CMU_HFRCOCTRL_TUNING(self)
        self.zz_fdict['TUNING'] = self.TUNING
        self.FINETUNING = RM_Field_CMU_HFRCOCTRL_FINETUNING(self)
        self.zz_fdict['FINETUNING'] = self.FINETUNING
        self.FREQRANGE = RM_Field_CMU_HFRCOCTRL_FREQRANGE(self)
        self.zz_fdict['FREQRANGE'] = self.FREQRANGE
        self.CMPBIAS = RM_Field_CMU_HFRCOCTRL_CMPBIAS(self)
        self.zz_fdict['CMPBIAS'] = self.CMPBIAS
        self.LDOHP = RM_Field_CMU_HFRCOCTRL_LDOHP(self)
        self.zz_fdict['LDOHP'] = self.LDOHP
        self.CLKDIV = RM_Field_CMU_HFRCOCTRL_CLKDIV(self)
        self.zz_fdict['CLKDIV'] = self.CLKDIV
        self.FINETUNINGEN = RM_Field_CMU_HFRCOCTRL_FINETUNINGEN(self)
        self.zz_fdict['FINETUNINGEN'] = self.FINETUNINGEN
        self.VREFTC = RM_Field_CMU_HFRCOCTRL_VREFTC(self)
        self.zz_fdict['VREFTC'] = self.VREFTC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFRCOLDOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFRCOLDOCTRL, self).__init__(rmio, label,
            0x400e4000, 0x014,
            'HFRCOLDOCTRL', 'CMU.HFRCOLDOCTRL', 'read-write',
            "",
            0x00000030, 0x00000077)

        self.STANDBY = RM_Field_CMU_HFRCOLDOCTRL_STANDBY(self)
        self.zz_fdict['STANDBY'] = self.STANDBY
        self.PSRENHANCE = RM_Field_CMU_HFRCOLDOCTRL_PSRENHANCE(self)
        self.zz_fdict['PSRENHANCE'] = self.PSRENHANCE
        self.PDDIS = RM_Field_CMU_HFRCOLDOCTRL_PDDIS(self)
        self.zz_fdict['PDDIS'] = self.PDDIS
        self.TRIM = RM_Field_CMU_HFRCOLDOCTRL_TRIM(self)
        self.zz_fdict['TRIM'] = self.TRIM
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_AUXHFRCOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_AUXHFRCOCTRL, self).__init__(rmio, label,
            0x400e4000, 0x018,
            'AUXHFRCOCTRL', 'CMU.AUXHFRCOCTRL', 'read-write',
            "",
            0xB1481F3C, 0xFFFF3F7F)

        self.TUNING = RM_Field_CMU_AUXHFRCOCTRL_TUNING(self)
        self.zz_fdict['TUNING'] = self.TUNING
        self.FINETUNING = RM_Field_CMU_AUXHFRCOCTRL_FINETUNING(self)
        self.zz_fdict['FINETUNING'] = self.FINETUNING
        self.FREQRANGE = RM_Field_CMU_AUXHFRCOCTRL_FREQRANGE(self)
        self.zz_fdict['FREQRANGE'] = self.FREQRANGE
        self.CMPBIAS = RM_Field_CMU_AUXHFRCOCTRL_CMPBIAS(self)
        self.zz_fdict['CMPBIAS'] = self.CMPBIAS
        self.LDOHP = RM_Field_CMU_AUXHFRCOCTRL_LDOHP(self)
        self.zz_fdict['LDOHP'] = self.LDOHP
        self.CLKDIV = RM_Field_CMU_AUXHFRCOCTRL_CLKDIV(self)
        self.zz_fdict['CLKDIV'] = self.CLKDIV
        self.FINETUNINGEN = RM_Field_CMU_AUXHFRCOCTRL_FINETUNINGEN(self)
        self.zz_fdict['FINETUNINGEN'] = self.FINETUNINGEN
        self.VREFTC = RM_Field_CMU_AUXHFRCOCTRL_VREFTC(self)
        self.zz_fdict['VREFTC'] = self.VREFTC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_AUXHFRCOLDOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_AUXHFRCOLDOCTRL, self).__init__(rmio, label,
            0x400e4000, 0x01C,
            'AUXHFRCOLDOCTRL', 'CMU.AUXHFRCOLDOCTRL', 'read-write',
            "",
            0x00000030, 0x00000077)

        self.STANDBY = RM_Field_CMU_AUXHFRCOLDOCTRL_STANDBY(self)
        self.zz_fdict['STANDBY'] = self.STANDBY
        self.PSRENHANCE = RM_Field_CMU_AUXHFRCOLDOCTRL_PSRENHANCE(self)
        self.zz_fdict['PSRENHANCE'] = self.PSRENHANCE
        self.PDDIS = RM_Field_CMU_AUXHFRCOLDOCTRL_PDDIS(self)
        self.zz_fdict['PDDIS'] = self.PDDIS
        self.TRIM = RM_Field_CMU_AUXHFRCOLDOCTRL_TRIM(self)
        self.zz_fdict['TRIM'] = self.TRIM
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LFRCOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LFRCOCTRL, self).__init__(rmio, label,
            0x400e4000, 0x020,
            'LFRCOCTRL', 'CMU.LFRCOCTRL', 'read-write',
            "",
            0x81060100, 0xF30701FF)

        self.TUNING = RM_Field_CMU_LFRCOCTRL_TUNING(self)
        self.zz_fdict['TUNING'] = self.TUNING
        self.ENVREF = RM_Field_CMU_LFRCOCTRL_ENVREF(self)
        self.zz_fdict['ENVREF'] = self.ENVREF
        self.ENCHOP = RM_Field_CMU_LFRCOCTRL_ENCHOP(self)
        self.zz_fdict['ENCHOP'] = self.ENCHOP
        self.ENDEM = RM_Field_CMU_LFRCOCTRL_ENDEM(self)
        self.zz_fdict['ENDEM'] = self.ENDEM
        self.TIMEOUT = RM_Field_CMU_LFRCOCTRL_TIMEOUT(self)
        self.zz_fdict['TIMEOUT'] = self.TIMEOUT
        self.GMCCURTUNE = RM_Field_CMU_LFRCOCTRL_GMCCURTUNE(self)
        self.zz_fdict['GMCCURTUNE'] = self.GMCCURTUNE
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFXOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFXOCTRL, self).__init__(rmio, label,
            0x400e4000, 0x024,
            'HFXOCTRL', 'CMU.HFXOCTRL', 'read-write',
            "",
            0x00000000, 0x77000F31)

        self.MODE = RM_Field_CMU_HFXOCTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.PEAKDETSHUNTOPTMODE = RM_Field_CMU_HFXOCTRL_PEAKDETSHUNTOPTMODE(self)
        self.zz_fdict['PEAKDETSHUNTOPTMODE'] = self.PEAKDETSHUNTOPTMODE
        self.LOWPOWER = RM_Field_CMU_HFXOCTRL_LOWPOWER(self)
        self.zz_fdict['LOWPOWER'] = self.LOWPOWER
        self.XTI2GND = RM_Field_CMU_HFXOCTRL_XTI2GND(self)
        self.zz_fdict['XTI2GND'] = self.XTI2GND
        self.XTO2GND = RM_Field_CMU_HFXOCTRL_XTO2GND(self)
        self.zz_fdict['XTO2GND'] = self.XTO2GND
        self.KEEPWARM = RM_Field_CMU_HFXOCTRL_KEEPWARM(self)
        self.zz_fdict['KEEPWARM'] = self.KEEPWARM
        self.LFTIMEOUT = RM_Field_CMU_HFXOCTRL_LFTIMEOUT(self)
        self.zz_fdict['LFTIMEOUT'] = self.LFTIMEOUT
        self.AUTOSTARTEM0EM1 = RM_Field_CMU_HFXOCTRL_AUTOSTARTEM0EM1(self)
        self.zz_fdict['AUTOSTARTEM0EM1'] = self.AUTOSTARTEM0EM1
        self.AUTOSTARTSELEM0EM1 = RM_Field_CMU_HFXOCTRL_AUTOSTARTSELEM0EM1(self)
        self.zz_fdict['AUTOSTARTSELEM0EM1'] = self.AUTOSTARTSELEM0EM1
        self.AUTOSTARTRDYSELRAC = RM_Field_CMU_HFXOCTRL_AUTOSTARTRDYSELRAC(self)
        self.zz_fdict['AUTOSTARTRDYSELRAC'] = self.AUTOSTARTRDYSELRAC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFXOCTRL1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFXOCTRL1, self).__init__(rmio, label,
            0x400e4000, 0x028,
            'HFXOCTRL1', 'CMU.HFXOCTRL1', 'read-write',
            "",
            0x00000240, 0x00000F77)

        self.PEAKDETTHR = RM_Field_CMU_HFXOCTRL1_PEAKDETTHR(self)
        self.zz_fdict['PEAKDETTHR'] = self.PEAKDETTHR
        self.REGLVL = RM_Field_CMU_HFXOCTRL1_REGLVL(self)
        self.zz_fdict['REGLVL'] = self.REGLVL
        self.SQBLWPDCEN = RM_Field_CMU_HFXOCTRL1_SQBLWPDCEN(self)
        self.zz_fdict['SQBLWPDCEN'] = self.SQBLWPDCEN
        self.XTIBIASEN = RM_Field_CMU_HFXOCTRL1_XTIBIASEN(self)
        self.zz_fdict['XTIBIASEN'] = self.XTIBIASEN
        self.SQBMODE = RM_Field_CMU_HFXOCTRL1_SQBMODE(self)
        self.zz_fdict['SQBMODE'] = self.SQBMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFXOSTARTUPCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFXOSTARTUPCTRL, self).__init__(rmio, label,
            0x400e4000, 0x02C,
            'HFXOSTARTUPCTRL', 'CMU.HFXOSTARTUPCTRL', 'read-write',
            "",
            0xA1250060, 0xFFEFF87F)

        self.IBTRIMXOCORE = RM_Field_CMU_HFXOSTARTUPCTRL_IBTRIMXOCORE(self)
        self.zz_fdict['IBTRIMXOCORE'] = self.IBTRIMXOCORE
        self.CTUNE = RM_Field_CMU_HFXOSTARTUPCTRL_CTUNE(self)
        self.zz_fdict['CTUNE'] = self.CTUNE
        self.IBTRIMXOCOREWARM = RM_Field_CMU_HFXOSTARTUPCTRL_IBTRIMXOCOREWARM(self)
        self.zz_fdict['IBTRIMXOCOREWARM'] = self.IBTRIMXOCOREWARM
        self.REGISHWARM = RM_Field_CMU_HFXOSTARTUPCTRL_REGISHWARM(self)
        self.zz_fdict['REGISHWARM'] = self.REGISHWARM
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFXOSTEADYSTATECTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFXOSTEADYSTATECTRL, self).__init__(rmio, label,
            0x400e4000, 0x030,
            'HFXOSTEADYSTATECTRL', 'CMU.HFXOSTEADYSTATECTRL', 'read-write',
            "",
            0xA30AAD09, 0xF70FFFFF)

        self.IBTRIMXOCORE = RM_Field_CMU_HFXOSTEADYSTATECTRL_IBTRIMXOCORE(self)
        self.zz_fdict['IBTRIMXOCORE'] = self.IBTRIMXOCORE
        self.REGISH = RM_Field_CMU_HFXOSTEADYSTATECTRL_REGISH(self)
        self.zz_fdict['REGISH'] = self.REGISH
        self.CTUNE = RM_Field_CMU_HFXOSTEADYSTATECTRL_CTUNE(self)
        self.zz_fdict['CTUNE'] = self.CTUNE
        self.REGSELILOW = RM_Field_CMU_HFXOSTEADYSTATECTRL_REGSELILOW(self)
        self.zz_fdict['REGSELILOW'] = self.REGSELILOW
        self.PEAKDETEN = RM_Field_CMU_HFXOSTEADYSTATECTRL_PEAKDETEN(self)
        self.zz_fdict['PEAKDETEN'] = self.PEAKDETEN
        self.REGISHUPPER = RM_Field_CMU_HFXOSTEADYSTATECTRL_REGISHUPPER(self)
        self.zz_fdict['REGISHUPPER'] = self.REGISHUPPER
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFXOTIMEOUTCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFXOTIMEOUTCTRL, self).__init__(rmio, label,
            0x400e4000, 0x034,
            'HFXOTIMEOUTCTRL', 'CMU.HFXOTIMEOUTCTRL', 'read-write',
            "",
            0x00026667, 0x000FFFFF)

        self.STARTUPTIMEOUT = RM_Field_CMU_HFXOTIMEOUTCTRL_STARTUPTIMEOUT(self)
        self.zz_fdict['STARTUPTIMEOUT'] = self.STARTUPTIMEOUT
        self.STEADYTIMEOUT = RM_Field_CMU_HFXOTIMEOUTCTRL_STEADYTIMEOUT(self)
        self.zz_fdict['STEADYTIMEOUT'] = self.STEADYTIMEOUT
        self.WARMSTEADYTIMEOUT = RM_Field_CMU_HFXOTIMEOUTCTRL_WARMSTEADYTIMEOUT(self)
        self.zz_fdict['WARMSTEADYTIMEOUT'] = self.WARMSTEADYTIMEOUT
        self.PEAKDETTIMEOUT = RM_Field_CMU_HFXOTIMEOUTCTRL_PEAKDETTIMEOUT(self)
        self.zz_fdict['PEAKDETTIMEOUT'] = self.PEAKDETTIMEOUT
        self.SHUNTOPTTIMEOUT = RM_Field_CMU_HFXOTIMEOUTCTRL_SHUNTOPTTIMEOUT(self)
        self.zz_fdict['SHUNTOPTTIMEOUT'] = self.SHUNTOPTTIMEOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LFXOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LFXOCTRL, self).__init__(rmio, label,
            0x400e4000, 0x038,
            'LFXOCTRL', 'CMU.LFXOCTRL', 'read-write',
            "",
            0x07009000, 0x0713DB7F)

        self.TUNING = RM_Field_CMU_LFXOCTRL_TUNING(self)
        self.zz_fdict['TUNING'] = self.TUNING
        self.MODE = RM_Field_CMU_LFXOCTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.GAIN = RM_Field_CMU_LFXOCTRL_GAIN(self)
        self.zz_fdict['GAIN'] = self.GAIN
        self.HIGHAMPL = RM_Field_CMU_LFXOCTRL_HIGHAMPL(self)
        self.zz_fdict['HIGHAMPL'] = self.HIGHAMPL
        self.AGC = RM_Field_CMU_LFXOCTRL_AGC(self)
        self.zz_fdict['AGC'] = self.AGC
        self.CUR = RM_Field_CMU_LFXOCTRL_CUR(self)
        self.zz_fdict['CUR'] = self.CUR
        self.BUFCUR = RM_Field_CMU_LFXOCTRL_BUFCUR(self)
        self.zz_fdict['BUFCUR'] = self.BUFCUR
        self.TIMEOUT = RM_Field_CMU_LFXOCTRL_TIMEOUT(self)
        self.zz_fdict['TIMEOUT'] = self.TIMEOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_ULFRCOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_ULFRCOCTRL, self).__init__(rmio, label,
            0x400e4000, 0x03C,
            'ULFRCOCTRL', 'CMU.ULFRCOCTRL', 'read-write',
            "",
            0x00020020, 0x00030D3F)

        self.TUNING = RM_Field_CMU_ULFRCOCTRL_TUNING(self)
        self.zz_fdict['TUNING'] = self.TUNING
        self.EN = RM_Field_CMU_ULFRCOCTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.MODE = RM_Field_CMU_ULFRCOCTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESTRIM = RM_Field_CMU_ULFRCOCTRL_RESTRIM(self)
        self.zz_fdict['RESTRIM'] = self.RESTRIM
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_CALCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_CALCTRL, self).__init__(rmio, label,
            0x400e4000, 0x050,
            'CALCTRL', 'CMU.CALCTRL', 'read-write',
            "",
            0x00000000, 0x0F0F0177)

        self.UPSEL = RM_Field_CMU_CALCTRL_UPSEL(self)
        self.zz_fdict['UPSEL'] = self.UPSEL
        self.DOWNSEL = RM_Field_CMU_CALCTRL_DOWNSEL(self)
        self.zz_fdict['DOWNSEL'] = self.DOWNSEL
        self.CONT = RM_Field_CMU_CALCTRL_CONT(self)
        self.zz_fdict['CONT'] = self.CONT
        self.PRSUPSEL = RM_Field_CMU_CALCTRL_PRSUPSEL(self)
        self.zz_fdict['PRSUPSEL'] = self.PRSUPSEL
        self.PRSDOWNSEL = RM_Field_CMU_CALCTRL_PRSDOWNSEL(self)
        self.zz_fdict['PRSDOWNSEL'] = self.PRSDOWNSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_CALCNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_CALCNT, self).__init__(rmio, label,
            0x400e4000, 0x054,
            'CALCNT', 'CMU.CALCNT', 'read-write',
            "",
            0x00000000, 0x000FFFFF)

        self.CALCNT = RM_Field_CMU_CALCNT_CALCNT(self)
        self.zz_fdict['CALCNT'] = self.CALCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_OSCENCMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_OSCENCMD, self).__init__(rmio, label,
            0x400e4000, 0x060,
            'OSCENCMD', 'CMU.OSCENCMD', 'write-only',
            "",
            0x00000000, 0x000003FF)

        self.HFRCOEN = RM_Field_CMU_OSCENCMD_HFRCOEN(self)
        self.zz_fdict['HFRCOEN'] = self.HFRCOEN
        self.HFRCODIS = RM_Field_CMU_OSCENCMD_HFRCODIS(self)
        self.zz_fdict['HFRCODIS'] = self.HFRCODIS
        self.HFXOEN = RM_Field_CMU_OSCENCMD_HFXOEN(self)
        self.zz_fdict['HFXOEN'] = self.HFXOEN
        self.HFXODIS = RM_Field_CMU_OSCENCMD_HFXODIS(self)
        self.zz_fdict['HFXODIS'] = self.HFXODIS
        self.AUXHFRCOEN = RM_Field_CMU_OSCENCMD_AUXHFRCOEN(self)
        self.zz_fdict['AUXHFRCOEN'] = self.AUXHFRCOEN
        self.AUXHFRCODIS = RM_Field_CMU_OSCENCMD_AUXHFRCODIS(self)
        self.zz_fdict['AUXHFRCODIS'] = self.AUXHFRCODIS
        self.LFRCOEN = RM_Field_CMU_OSCENCMD_LFRCOEN(self)
        self.zz_fdict['LFRCOEN'] = self.LFRCOEN
        self.LFRCODIS = RM_Field_CMU_OSCENCMD_LFRCODIS(self)
        self.zz_fdict['LFRCODIS'] = self.LFRCODIS
        self.LFXOEN = RM_Field_CMU_OSCENCMD_LFXOEN(self)
        self.zz_fdict['LFXOEN'] = self.LFXOEN
        self.LFXODIS = RM_Field_CMU_OSCENCMD_LFXODIS(self)
        self.zz_fdict['LFXODIS'] = self.LFXODIS
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_CMD, self).__init__(rmio, label,
            0x400e4000, 0x064,
            'CMD', 'CMU.CMD', 'write-only',
            "",
            0x00000000, 0x00000033)

        self.CALSTART = RM_Field_CMU_CMD_CALSTART(self)
        self.zz_fdict['CALSTART'] = self.CALSTART
        self.CALSTOP = RM_Field_CMU_CMD_CALSTOP(self)
        self.zz_fdict['CALSTOP'] = self.CALSTOP
        self.HFXOPEAKDETSTART = RM_Field_CMU_CMD_HFXOPEAKDETSTART(self)
        self.zz_fdict['HFXOPEAKDETSTART'] = self.HFXOPEAKDETSTART
        self.HFXOSHUNTOPTSTART = RM_Field_CMU_CMD_HFXOSHUNTOPTSTART(self)
        self.zz_fdict['HFXOSHUNTOPTSTART'] = self.HFXOSHUNTOPTSTART
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_DBGCLKSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_DBGCLKSEL, self).__init__(rmio, label,
            0x400e4000, 0x070,
            'DBGCLKSEL', 'CMU.DBGCLKSEL', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.DBG = RM_Field_CMU_DBGCLKSEL_DBG(self)
        self.zz_fdict['DBG'] = self.DBG
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFCLKSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFCLKSEL, self).__init__(rmio, label,
            0x400e4000, 0x074,
            'HFCLKSEL', 'CMU.HFCLKSEL', 'write-only',
            "",
            0x00000000, 0x00000007)

        self.HF = RM_Field_CMU_HFCLKSEL_HF(self)
        self.zz_fdict['HF'] = self.HF
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LFACLKSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LFACLKSEL, self).__init__(rmio, label,
            0x400e4000, 0x080,
            'LFACLKSEL', 'CMU.LFACLKSEL', 'read-write',
            "",
            0x00000000, 0x00000007)

        self.LFA = RM_Field_CMU_LFACLKSEL_LFA(self)
        self.zz_fdict['LFA'] = self.LFA
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LFBCLKSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LFBCLKSEL, self).__init__(rmio, label,
            0x400e4000, 0x084,
            'LFBCLKSEL', 'CMU.LFBCLKSEL', 'read-write',
            "",
            0x00000000, 0x00000007)

        self.LFB = RM_Field_CMU_LFBCLKSEL_LFB(self)
        self.zz_fdict['LFB'] = self.LFB
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LFECLKSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LFECLKSEL, self).__init__(rmio, label,
            0x400e4000, 0x088,
            'LFECLKSEL', 'CMU.LFECLKSEL', 'read-write',
            "",
            0x00000000, 0x00000007)

        self.LFE = RM_Field_CMU_LFECLKSEL_LFE(self)
        self.zz_fdict['LFE'] = self.LFE
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_STATUS, self).__init__(rmio, label,
            0x400e4000, 0x090,
            'STATUS', 'CMU.STATUS', 'read-only',
            "",
            0x00010003, 0x07F103FF)

        self.HFRCOENS = RM_Field_CMU_STATUS_HFRCOENS(self)
        self.zz_fdict['HFRCOENS'] = self.HFRCOENS
        self.HFRCORDY = RM_Field_CMU_STATUS_HFRCORDY(self)
        self.zz_fdict['HFRCORDY'] = self.HFRCORDY
        self.HFXOENS = RM_Field_CMU_STATUS_HFXOENS(self)
        self.zz_fdict['HFXOENS'] = self.HFXOENS
        self.HFXORDY = RM_Field_CMU_STATUS_HFXORDY(self)
        self.zz_fdict['HFXORDY'] = self.HFXORDY
        self.AUXHFRCOENS = RM_Field_CMU_STATUS_AUXHFRCOENS(self)
        self.zz_fdict['AUXHFRCOENS'] = self.AUXHFRCOENS
        self.AUXHFRCORDY = RM_Field_CMU_STATUS_AUXHFRCORDY(self)
        self.zz_fdict['AUXHFRCORDY'] = self.AUXHFRCORDY
        self.LFRCOENS = RM_Field_CMU_STATUS_LFRCOENS(self)
        self.zz_fdict['LFRCOENS'] = self.LFRCOENS
        self.LFRCORDY = RM_Field_CMU_STATUS_LFRCORDY(self)
        self.zz_fdict['LFRCORDY'] = self.LFRCORDY
        self.LFXOENS = RM_Field_CMU_STATUS_LFXOENS(self)
        self.zz_fdict['LFXOENS'] = self.LFXOENS
        self.LFXORDY = RM_Field_CMU_STATUS_LFXORDY(self)
        self.zz_fdict['LFXORDY'] = self.LFXORDY
        self.CALRDY = RM_Field_CMU_STATUS_CALRDY(self)
        self.zz_fdict['CALRDY'] = self.CALRDY
        self.HFXOWARMS = RM_Field_CMU_STATUS_HFXOWARMS(self)
        self.zz_fdict['HFXOWARMS'] = self.HFXOWARMS
        self.HFXOREQ = RM_Field_CMU_STATUS_HFXOREQ(self)
        self.zz_fdict['HFXOREQ'] = self.HFXOREQ
        self.HFXOPEAKDETRDY = RM_Field_CMU_STATUS_HFXOPEAKDETRDY(self)
        self.zz_fdict['HFXOPEAKDETRDY'] = self.HFXOPEAKDETRDY
        self.HFXOSHUNTOPTRDY = RM_Field_CMU_STATUS_HFXOSHUNTOPTRDY(self)
        self.zz_fdict['HFXOSHUNTOPTRDY'] = self.HFXOSHUNTOPTRDY
        self.HFXOAMPHIGH = RM_Field_CMU_STATUS_HFXOAMPHIGH(self)
        self.zz_fdict['HFXOAMPHIGH'] = self.HFXOAMPHIGH
        self.HFXOAMPLOW = RM_Field_CMU_STATUS_HFXOAMPLOW(self)
        self.zz_fdict['HFXOAMPLOW'] = self.HFXOAMPLOW
        self.HFXOREGILOW = RM_Field_CMU_STATUS_HFXOREGILOW(self)
        self.zz_fdict['HFXOREGILOW'] = self.HFXOREGILOW
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFCLKSTATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFCLKSTATUS, self).__init__(rmio, label,
            0x400e4000, 0x094,
            'HFCLKSTATUS', 'CMU.HFCLKSTATUS', 'read-only',
            "",
            0x00000001, 0x00000007)

        self.SELECTED = RM_Field_CMU_HFCLKSTATUS_SELECTED(self)
        self.zz_fdict['SELECTED'] = self.SELECTED
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFXOTRIMSTATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFXOTRIMSTATUS, self).__init__(rmio, label,
            0x400e4000, 0x09C,
            'HFXOTRIMSTATUS', 'CMU.HFXOTRIMSTATUS', 'read-only',
            "",
            0x00000500, 0x000007FF)

        self.IBTRIMXOCORE = RM_Field_CMU_HFXOTRIMSTATUS_IBTRIMXOCORE(self)
        self.zz_fdict['IBTRIMXOCORE'] = self.IBTRIMXOCORE
        self.REGISH = RM_Field_CMU_HFXOTRIMSTATUS_REGISH(self)
        self.zz_fdict['REGISH'] = self.REGISH
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_IF, self).__init__(rmio, label,
            0x400e4000, 0x0A0,
            'IF', 'CMU.IF', 'read-only',
            "",
            0x00000001, 0x80007F7F)

        self.HFRCORDY = RM_Field_CMU_IF_HFRCORDY(self)
        self.zz_fdict['HFRCORDY'] = self.HFRCORDY
        self.HFXORDY = RM_Field_CMU_IF_HFXORDY(self)
        self.zz_fdict['HFXORDY'] = self.HFXORDY
        self.LFRCORDY = RM_Field_CMU_IF_LFRCORDY(self)
        self.zz_fdict['LFRCORDY'] = self.LFRCORDY
        self.LFXORDY = RM_Field_CMU_IF_LFXORDY(self)
        self.zz_fdict['LFXORDY'] = self.LFXORDY
        self.AUXHFRCORDY = RM_Field_CMU_IF_AUXHFRCORDY(self)
        self.zz_fdict['AUXHFRCORDY'] = self.AUXHFRCORDY
        self.CALRDY = RM_Field_CMU_IF_CALRDY(self)
        self.zz_fdict['CALRDY'] = self.CALRDY
        self.CALOF = RM_Field_CMU_IF_CALOF(self)
        self.zz_fdict['CALOF'] = self.CALOF
        self.HFXODISERR = RM_Field_CMU_IF_HFXODISERR(self)
        self.zz_fdict['HFXODISERR'] = self.HFXODISERR
        self.HFXOAUTOSW = RM_Field_CMU_IF_HFXOAUTOSW(self)
        self.zz_fdict['HFXOAUTOSW'] = self.HFXOAUTOSW
        self.HFXOPEAKDETERR = RM_Field_CMU_IF_HFXOPEAKDETERR(self)
        self.zz_fdict['HFXOPEAKDETERR'] = self.HFXOPEAKDETERR
        self.HFXOPEAKDETRDY = RM_Field_CMU_IF_HFXOPEAKDETRDY(self)
        self.zz_fdict['HFXOPEAKDETRDY'] = self.HFXOPEAKDETRDY
        self.HFXOSHUNTOPTRDY = RM_Field_CMU_IF_HFXOSHUNTOPTRDY(self)
        self.zz_fdict['HFXOSHUNTOPTRDY'] = self.HFXOSHUNTOPTRDY
        self.HFRCODIS = RM_Field_CMU_IF_HFRCODIS(self)
        self.zz_fdict['HFRCODIS'] = self.HFRCODIS
        self.LFTIMEOUTERR = RM_Field_CMU_IF_LFTIMEOUTERR(self)
        self.zz_fdict['LFTIMEOUTERR'] = self.LFTIMEOUTERR
        self.CMUERR = RM_Field_CMU_IF_CMUERR(self)
        self.zz_fdict['CMUERR'] = self.CMUERR
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_IFS, self).__init__(rmio, label,
            0x400e4000, 0x0A4,
            'IFS', 'CMU.IFS', 'write-only',
            "",
            0x00000000, 0x80007F7F)

        self.HFRCORDY = RM_Field_CMU_IFS_HFRCORDY(self)
        self.zz_fdict['HFRCORDY'] = self.HFRCORDY
        self.HFXORDY = RM_Field_CMU_IFS_HFXORDY(self)
        self.zz_fdict['HFXORDY'] = self.HFXORDY
        self.LFRCORDY = RM_Field_CMU_IFS_LFRCORDY(self)
        self.zz_fdict['LFRCORDY'] = self.LFRCORDY
        self.LFXORDY = RM_Field_CMU_IFS_LFXORDY(self)
        self.zz_fdict['LFXORDY'] = self.LFXORDY
        self.AUXHFRCORDY = RM_Field_CMU_IFS_AUXHFRCORDY(self)
        self.zz_fdict['AUXHFRCORDY'] = self.AUXHFRCORDY
        self.CALRDY = RM_Field_CMU_IFS_CALRDY(self)
        self.zz_fdict['CALRDY'] = self.CALRDY
        self.CALOF = RM_Field_CMU_IFS_CALOF(self)
        self.zz_fdict['CALOF'] = self.CALOF
        self.HFXODISERR = RM_Field_CMU_IFS_HFXODISERR(self)
        self.zz_fdict['HFXODISERR'] = self.HFXODISERR
        self.HFXOAUTOSW = RM_Field_CMU_IFS_HFXOAUTOSW(self)
        self.zz_fdict['HFXOAUTOSW'] = self.HFXOAUTOSW
        self.HFXOPEAKDETERR = RM_Field_CMU_IFS_HFXOPEAKDETERR(self)
        self.zz_fdict['HFXOPEAKDETERR'] = self.HFXOPEAKDETERR
        self.HFXOPEAKDETRDY = RM_Field_CMU_IFS_HFXOPEAKDETRDY(self)
        self.zz_fdict['HFXOPEAKDETRDY'] = self.HFXOPEAKDETRDY
        self.HFXOSHUNTOPTRDY = RM_Field_CMU_IFS_HFXOSHUNTOPTRDY(self)
        self.zz_fdict['HFXOSHUNTOPTRDY'] = self.HFXOSHUNTOPTRDY
        self.HFRCODIS = RM_Field_CMU_IFS_HFRCODIS(self)
        self.zz_fdict['HFRCODIS'] = self.HFRCODIS
        self.LFTIMEOUTERR = RM_Field_CMU_IFS_LFTIMEOUTERR(self)
        self.zz_fdict['LFTIMEOUTERR'] = self.LFTIMEOUTERR
        self.CMUERR = RM_Field_CMU_IFS_CMUERR(self)
        self.zz_fdict['CMUERR'] = self.CMUERR
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_IFC, self).__init__(rmio, label,
            0x400e4000, 0x0A8,
            'IFC', 'CMU.IFC', 'write-only',
            "",
            0x00000000, 0x80007F7F)

        self.HFRCORDY = RM_Field_CMU_IFC_HFRCORDY(self)
        self.zz_fdict['HFRCORDY'] = self.HFRCORDY
        self.HFXORDY = RM_Field_CMU_IFC_HFXORDY(self)
        self.zz_fdict['HFXORDY'] = self.HFXORDY
        self.LFRCORDY = RM_Field_CMU_IFC_LFRCORDY(self)
        self.zz_fdict['LFRCORDY'] = self.LFRCORDY
        self.LFXORDY = RM_Field_CMU_IFC_LFXORDY(self)
        self.zz_fdict['LFXORDY'] = self.LFXORDY
        self.AUXHFRCORDY = RM_Field_CMU_IFC_AUXHFRCORDY(self)
        self.zz_fdict['AUXHFRCORDY'] = self.AUXHFRCORDY
        self.CALRDY = RM_Field_CMU_IFC_CALRDY(self)
        self.zz_fdict['CALRDY'] = self.CALRDY
        self.CALOF = RM_Field_CMU_IFC_CALOF(self)
        self.zz_fdict['CALOF'] = self.CALOF
        self.HFXODISERR = RM_Field_CMU_IFC_HFXODISERR(self)
        self.zz_fdict['HFXODISERR'] = self.HFXODISERR
        self.HFXOAUTOSW = RM_Field_CMU_IFC_HFXOAUTOSW(self)
        self.zz_fdict['HFXOAUTOSW'] = self.HFXOAUTOSW
        self.HFXOPEAKDETERR = RM_Field_CMU_IFC_HFXOPEAKDETERR(self)
        self.zz_fdict['HFXOPEAKDETERR'] = self.HFXOPEAKDETERR
        self.HFXOPEAKDETRDY = RM_Field_CMU_IFC_HFXOPEAKDETRDY(self)
        self.zz_fdict['HFXOPEAKDETRDY'] = self.HFXOPEAKDETRDY
        self.HFXOSHUNTOPTRDY = RM_Field_CMU_IFC_HFXOSHUNTOPTRDY(self)
        self.zz_fdict['HFXOSHUNTOPTRDY'] = self.HFXOSHUNTOPTRDY
        self.HFRCODIS = RM_Field_CMU_IFC_HFRCODIS(self)
        self.zz_fdict['HFRCODIS'] = self.HFRCODIS
        self.LFTIMEOUTERR = RM_Field_CMU_IFC_LFTIMEOUTERR(self)
        self.zz_fdict['LFTIMEOUTERR'] = self.LFTIMEOUTERR
        self.CMUERR = RM_Field_CMU_IFC_CMUERR(self)
        self.zz_fdict['CMUERR'] = self.CMUERR
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_IEN, self).__init__(rmio, label,
            0x400e4000, 0x0AC,
            'IEN', 'CMU.IEN', 'read-write',
            "",
            0x00000000, 0x80007F7F)

        self.HFRCORDY = RM_Field_CMU_IEN_HFRCORDY(self)
        self.zz_fdict['HFRCORDY'] = self.HFRCORDY
        self.HFXORDY = RM_Field_CMU_IEN_HFXORDY(self)
        self.zz_fdict['HFXORDY'] = self.HFXORDY
        self.LFRCORDY = RM_Field_CMU_IEN_LFRCORDY(self)
        self.zz_fdict['LFRCORDY'] = self.LFRCORDY
        self.LFXORDY = RM_Field_CMU_IEN_LFXORDY(self)
        self.zz_fdict['LFXORDY'] = self.LFXORDY
        self.AUXHFRCORDY = RM_Field_CMU_IEN_AUXHFRCORDY(self)
        self.zz_fdict['AUXHFRCORDY'] = self.AUXHFRCORDY
        self.CALRDY = RM_Field_CMU_IEN_CALRDY(self)
        self.zz_fdict['CALRDY'] = self.CALRDY
        self.CALOF = RM_Field_CMU_IEN_CALOF(self)
        self.zz_fdict['CALOF'] = self.CALOF
        self.HFXODISERR = RM_Field_CMU_IEN_HFXODISERR(self)
        self.zz_fdict['HFXODISERR'] = self.HFXODISERR
        self.HFXOAUTOSW = RM_Field_CMU_IEN_HFXOAUTOSW(self)
        self.zz_fdict['HFXOAUTOSW'] = self.HFXOAUTOSW
        self.HFXOPEAKDETERR = RM_Field_CMU_IEN_HFXOPEAKDETERR(self)
        self.zz_fdict['HFXOPEAKDETERR'] = self.HFXOPEAKDETERR
        self.HFXOPEAKDETRDY = RM_Field_CMU_IEN_HFXOPEAKDETRDY(self)
        self.zz_fdict['HFXOPEAKDETRDY'] = self.HFXOPEAKDETRDY
        self.HFXOSHUNTOPTRDY = RM_Field_CMU_IEN_HFXOSHUNTOPTRDY(self)
        self.zz_fdict['HFXOSHUNTOPTRDY'] = self.HFXOSHUNTOPTRDY
        self.HFRCODIS = RM_Field_CMU_IEN_HFRCODIS(self)
        self.zz_fdict['HFRCODIS'] = self.HFRCODIS
        self.LFTIMEOUTERR = RM_Field_CMU_IEN_LFTIMEOUTERR(self)
        self.zz_fdict['LFTIMEOUTERR'] = self.LFTIMEOUTERR
        self.CMUERR = RM_Field_CMU_IEN_CMUERR(self)
        self.zz_fdict['CMUERR'] = self.CMUERR
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFBUSCLKEN0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFBUSCLKEN0, self).__init__(rmio, label,
            0x400e4000, 0x0B0,
            'HFBUSCLKEN0', 'CMU.HFBUSCLKEN0', 'read-write',
            "",
            0x00000000, 0x0000003F)

        self.LE = RM_Field_CMU_HFBUSCLKEN0_LE(self)
        self.zz_fdict['LE'] = self.LE
        self.CRYPTO = RM_Field_CMU_HFBUSCLKEN0_CRYPTO(self)
        self.zz_fdict['CRYPTO'] = self.CRYPTO
        self.GPIO = RM_Field_CMU_HFBUSCLKEN0_GPIO(self)
        self.zz_fdict['GPIO'] = self.GPIO
        self.PRS = RM_Field_CMU_HFBUSCLKEN0_PRS(self)
        self.zz_fdict['PRS'] = self.PRS
        self.LDMA = RM_Field_CMU_HFBUSCLKEN0_LDMA(self)
        self.zz_fdict['LDMA'] = self.LDMA
        self.GPCRC = RM_Field_CMU_HFBUSCLKEN0_GPCRC(self)
        self.zz_fdict['GPCRC'] = self.GPCRC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFPERCLKEN0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFPERCLKEN0, self).__init__(rmio, label,
            0x400e4000, 0x0C0,
            'HFPERCLKEN0', 'CMU.HFPERCLKEN0', 'read-write',
            "",
            0x00000000, 0x000007FF)

        self.TIMER0 = RM_Field_CMU_HFPERCLKEN0_TIMER0(self)
        self.zz_fdict['TIMER0'] = self.TIMER0
        self.TIMER1 = RM_Field_CMU_HFPERCLKEN0_TIMER1(self)
        self.zz_fdict['TIMER1'] = self.TIMER1
        self.USART0 = RM_Field_CMU_HFPERCLKEN0_USART0(self)
        self.zz_fdict['USART0'] = self.USART0
        self.USART1 = RM_Field_CMU_HFPERCLKEN0_USART1(self)
        self.zz_fdict['USART1'] = self.USART1
        self.ACMP0 = RM_Field_CMU_HFPERCLKEN0_ACMP0(self)
        self.zz_fdict['ACMP0'] = self.ACMP0
        self.ACMP1 = RM_Field_CMU_HFPERCLKEN0_ACMP1(self)
        self.zz_fdict['ACMP1'] = self.ACMP1
        self.CRYOTIMER = RM_Field_CMU_HFPERCLKEN0_CRYOTIMER(self)
        self.zz_fdict['CRYOTIMER'] = self.CRYOTIMER
        self.I2C0 = RM_Field_CMU_HFPERCLKEN0_I2C0(self)
        self.zz_fdict['I2C0'] = self.I2C0
        self.ADC0 = RM_Field_CMU_HFPERCLKEN0_ADC0(self)
        self.zz_fdict['ADC0'] = self.ADC0
        self.IDAC0 = RM_Field_CMU_HFPERCLKEN0_IDAC0(self)
        self.zz_fdict['IDAC0'] = self.IDAC0
        self.SYSCFG = RM_Field_CMU_HFPERCLKEN0_SYSCFG(self)
        self.zz_fdict['SYSCFG'] = self.SYSCFG
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFRADIOCLKEN0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFRADIOCLKEN0, self).__init__(rmio, label,
            0x400e4000, 0x0C8,
            'HFRADIOCLKEN0', 'CMU.HFRADIOCLKEN0', 'read-write',
            "",
            0x00000000, 0x000001FF)

        self.PROTIMER = RM_Field_CMU_HFRADIOCLKEN0_PROTIMER(self)
        self.zz_fdict['PROTIMER'] = self.PROTIMER
        self.RFSENSE = RM_Field_CMU_HFRADIOCLKEN0_RFSENSE(self)
        self.zz_fdict['RFSENSE'] = self.RFSENSE
        self.RAC = RM_Field_CMU_HFRADIOCLKEN0_RAC(self)
        self.zz_fdict['RAC'] = self.RAC
        self.FRC = RM_Field_CMU_HFRADIOCLKEN0_FRC(self)
        self.zz_fdict['FRC'] = self.FRC
        self.BUFC = RM_Field_CMU_HFRADIOCLKEN0_BUFC(self)
        self.zz_fdict['BUFC'] = self.BUFC
        self.CRC = RM_Field_CMU_HFRADIOCLKEN0_CRC(self)
        self.zz_fdict['CRC'] = self.CRC
        self.SYNTH = RM_Field_CMU_HFRADIOCLKEN0_SYNTH(self)
        self.zz_fdict['SYNTH'] = self.SYNTH
        self.MODEM = RM_Field_CMU_HFRADIOCLKEN0_MODEM(self)
        self.zz_fdict['MODEM'] = self.MODEM
        self.AGC = RM_Field_CMU_HFRADIOCLKEN0_AGC(self)
        self.zz_fdict['AGC'] = self.AGC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LFACLKEN0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LFACLKEN0, self).__init__(rmio, label,
            0x400e4000, 0x0E0,
            'LFACLKEN0', 'CMU.LFACLKEN0', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.LETIMER0 = RM_Field_CMU_LFACLKEN0_LETIMER0(self)
        self.zz_fdict['LETIMER0'] = self.LETIMER0
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LFBCLKEN0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LFBCLKEN0, self).__init__(rmio, label,
            0x400e4000, 0x0E8,
            'LFBCLKEN0', 'CMU.LFBCLKEN0', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.LEUART0 = RM_Field_CMU_LFBCLKEN0_LEUART0(self)
        self.zz_fdict['LEUART0'] = self.LEUART0
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LFECLKEN0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LFECLKEN0, self).__init__(rmio, label,
            0x400e4000, 0x0F0,
            'LFECLKEN0', 'CMU.LFECLKEN0', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.RTCC = RM_Field_CMU_LFECLKEN0_RTCC(self)
        self.zz_fdict['RTCC'] = self.RTCC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFPRESC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFPRESC, self).__init__(rmio, label,
            0x400e4000, 0x100,
            'HFPRESC', 'CMU.HFPRESC', 'read-write',
            "",
            0x00000000, 0x01001F00)

        self.PRESC = RM_Field_CMU_HFPRESC_PRESC(self)
        self.zz_fdict['PRESC'] = self.PRESC
        self.HFCLKLEPRESC = RM_Field_CMU_HFPRESC_HFCLKLEPRESC(self)
        self.zz_fdict['HFCLKLEPRESC'] = self.HFCLKLEPRESC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFCOREPRESC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFCOREPRESC, self).__init__(rmio, label,
            0x400e4000, 0x108,
            'HFCOREPRESC', 'CMU.HFCOREPRESC', 'read-write',
            "",
            0x00000000, 0x0001FF00)

        self.PRESC = RM_Field_CMU_HFCOREPRESC_PRESC(self)
        self.zz_fdict['PRESC'] = self.PRESC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFPERPRESC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFPERPRESC, self).__init__(rmio, label,
            0x400e4000, 0x10C,
            'HFPERPRESC', 'CMU.HFPERPRESC', 'read-write',
            "",
            0x00000000, 0x0001FF00)

        self.PRESC = RM_Field_CMU_HFPERPRESC_PRESC(self)
        self.zz_fdict['PRESC'] = self.PRESC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFRADIOPRESC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFRADIOPRESC, self).__init__(rmio, label,
            0x400e4000, 0x110,
            'HFRADIOPRESC', 'CMU.HFRADIOPRESC', 'read-write',
            "",
            0x00000000, 0x0001FF00)

        self.PRESC = RM_Field_CMU_HFRADIOPRESC_PRESC(self)
        self.zz_fdict['PRESC'] = self.PRESC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFEXPPRESC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFEXPPRESC, self).__init__(rmio, label,
            0x400e4000, 0x114,
            'HFEXPPRESC', 'CMU.HFEXPPRESC', 'read-write',
            "",
            0x00000000, 0x00001F00)

        self.PRESC = RM_Field_CMU_HFEXPPRESC_PRESC(self)
        self.zz_fdict['PRESC'] = self.PRESC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LFAPRESC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LFAPRESC0, self).__init__(rmio, label,
            0x400e4000, 0x120,
            'LFAPRESC0', 'CMU.LFAPRESC0', 'read-write',
            "",
            0x00000000, 0x0000000F)

        self.LETIMER0 = RM_Field_CMU_LFAPRESC0_LETIMER0(self)
        self.zz_fdict['LETIMER0'] = self.LETIMER0
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LFBPRESC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LFBPRESC0, self).__init__(rmio, label,
            0x400e4000, 0x128,
            'LFBPRESC0', 'CMU.LFBPRESC0', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.LEUART0 = RM_Field_CMU_LFBPRESC0_LEUART0(self)
        self.zz_fdict['LEUART0'] = self.LEUART0
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LFEPRESC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LFEPRESC0, self).__init__(rmio, label,
            0x400e4000, 0x130,
            'LFEPRESC0', 'CMU.LFEPRESC0', 'read-write',
            "",
            0x00000000, 0x0000000F)

        self.RTCC = RM_Field_CMU_LFEPRESC0_RTCC(self)
        self.zz_fdict['RTCC'] = self.RTCC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_SYNCBUSY(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_SYNCBUSY, self).__init__(rmio, label,
            0x400e4000, 0x140,
            'SYNCBUSY', 'CMU.SYNCBUSY', 'read-only',
            "",
            0x00000000, 0x3F050055)

        self.LFACLKEN0 = RM_Field_CMU_SYNCBUSY_LFACLKEN0(self)
        self.zz_fdict['LFACLKEN0'] = self.LFACLKEN0
        self.LFAPRESC0 = RM_Field_CMU_SYNCBUSY_LFAPRESC0(self)
        self.zz_fdict['LFAPRESC0'] = self.LFAPRESC0
        self.LFBCLKEN0 = RM_Field_CMU_SYNCBUSY_LFBCLKEN0(self)
        self.zz_fdict['LFBCLKEN0'] = self.LFBCLKEN0
        self.LFBPRESC0 = RM_Field_CMU_SYNCBUSY_LFBPRESC0(self)
        self.zz_fdict['LFBPRESC0'] = self.LFBPRESC0
        self.LFECLKEN0 = RM_Field_CMU_SYNCBUSY_LFECLKEN0(self)
        self.zz_fdict['LFECLKEN0'] = self.LFECLKEN0
        self.LFEPRESC0 = RM_Field_CMU_SYNCBUSY_LFEPRESC0(self)
        self.zz_fdict['LFEPRESC0'] = self.LFEPRESC0
        self.HFRCOBSY = RM_Field_CMU_SYNCBUSY_HFRCOBSY(self)
        self.zz_fdict['HFRCOBSY'] = self.HFRCOBSY
        self.AUXHFRCOBSY = RM_Field_CMU_SYNCBUSY_AUXHFRCOBSY(self)
        self.zz_fdict['AUXHFRCOBSY'] = self.AUXHFRCOBSY
        self.LFRCOBSY = RM_Field_CMU_SYNCBUSY_LFRCOBSY(self)
        self.zz_fdict['LFRCOBSY'] = self.LFRCOBSY
        self.LFRCOVREFBSY = RM_Field_CMU_SYNCBUSY_LFRCOVREFBSY(self)
        self.zz_fdict['LFRCOVREFBSY'] = self.LFRCOVREFBSY
        self.HFXOBSY = RM_Field_CMU_SYNCBUSY_HFXOBSY(self)
        self.zz_fdict['HFXOBSY'] = self.HFXOBSY
        self.LFXOBSY = RM_Field_CMU_SYNCBUSY_LFXOBSY(self)
        self.zz_fdict['LFXOBSY'] = self.LFXOBSY
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_FREEZE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_FREEZE, self).__init__(rmio, label,
            0x400e4000, 0x144,
            'FREEZE', 'CMU.FREEZE', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.REGFREEZE = RM_Field_CMU_FREEZE_REGFREEZE(self)
        self.zz_fdict['REGFREEZE'] = self.REGFREEZE
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_PCNTCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_PCNTCTRL, self).__init__(rmio, label,
            0x400e4000, 0x150,
            'PCNTCTRL', 'CMU.PCNTCTRL', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.PCNT0CLKEN = RM_Field_CMU_PCNTCTRL_PCNT0CLKEN(self)
        self.zz_fdict['PCNT0CLKEN'] = self.PCNT0CLKEN
        self.PCNT0CLKSEL = RM_Field_CMU_PCNTCTRL_PCNT0CLKSEL(self)
        self.zz_fdict['PCNT0CLKSEL'] = self.PCNT0CLKSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LCDCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LCDCTRL, self).__init__(rmio, label,
            0x400e4000, 0x154,
            'LCDCTRL', 'CMU.LCDCTRL', 'read-write',
            "",
            0x00000020, 0x0000007F)

        self.FDIV = RM_Field_CMU_LCDCTRL_FDIV(self)
        self.zz_fdict['FDIV'] = self.FDIV
        self.VBOOSTEN = RM_Field_CMU_LCDCTRL_VBOOSTEN(self)
        self.zz_fdict['VBOOSTEN'] = self.VBOOSTEN
        self.VBFDIV = RM_Field_CMU_LCDCTRL_VBFDIV(self)
        self.zz_fdict['VBFDIV'] = self.VBFDIV
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LVDSCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LVDSCTRL, self).__init__(rmio, label,
            0x400e4000, 0x158,
            'LVDSCTRL', 'CMU.LVDSCTRL', 'read-write',
            "",
            0x00000000, 0x00000007)

        self.EN = RM_Field_CMU_LVDSCTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.CLKSEL = RM_Field_CMU_LVDSCTRL_CLKSEL(self)
        self.zz_fdict['CLKSEL'] = self.CLKSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_ADCCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_ADCCTRL, self).__init__(rmio, label,
            0x400e4000, 0x15C,
            'ADCCTRL', 'CMU.ADCCTRL', 'read-write',
            "",
            0x00000000, 0x00000130)

        self.CLKSEL = RM_Field_CMU_ADCCTRL_CLKSEL(self)
        self.zz_fdict['CLKSEL'] = self.CLKSEL
        self.INV = RM_Field_CMU_ADCCTRL_INV(self)
        self.zz_fdict['INV'] = self.INV
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_ROUTEPEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_ROUTEPEN, self).__init__(rmio, label,
            0x400e4000, 0x170,
            'ROUTEPEN', 'CMU.ROUTEPEN', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.CLKOUT0PEN = RM_Field_CMU_ROUTEPEN_CLKOUT0PEN(self)
        self.zz_fdict['CLKOUT0PEN'] = self.CLKOUT0PEN
        self.CLKOUT1PEN = RM_Field_CMU_ROUTEPEN_CLKOUT1PEN(self)
        self.zz_fdict['CLKOUT1PEN'] = self.CLKOUT1PEN
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_ROUTELOC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_ROUTELOC0, self).__init__(rmio, label,
            0x400e4000, 0x174,
            'ROUTELOC0', 'CMU.ROUTELOC0', 'read-write',
            "",
            0x00000000, 0x00003F3F)

        self.CLKOUT0LOC = RM_Field_CMU_ROUTELOC0_CLKOUT0LOC(self)
        self.zz_fdict['CLKOUT0LOC'] = self.CLKOUT0LOC
        self.CLKOUT1LOC = RM_Field_CMU_ROUTELOC0_CLKOUT1LOC(self)
        self.zz_fdict['CLKOUT1LOC'] = self.CLKOUT1LOC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LOCK, self).__init__(rmio, label,
            0x400e4000, 0x180,
            'LOCK', 'CMU.LOCK', 'read-write',
            "",
            0x00000000, 0x8000FFFF)

        self.LOCKKEY = RM_Field_CMU_LOCK_LOCKKEY(self)
        self.zz_fdict['LOCKKEY'] = self.LOCKKEY
        self.LFOSCUNLOCK = RM_Field_CMU_LOCK_LFOSCUNLOCK(self)
        self.zz_fdict['LFOSCUNLOCK'] = self.LFOSCUNLOCK
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_RFLOCK0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_RFLOCK0, self).__init__(rmio, label,
            0x400e4000, 0x188,
            'RFLOCK0', 'CMU.RFLOCK0', 'read-write',
            "",
            0x80000000, 0xBDFFFFFF)

        self.SYNTHLODIVFREQCTRL = RM_Field_CMU_RFLOCK0_SYNTHLODIVFREQCTRL(self)
        self.zz_fdict['SYNTHLODIVFREQCTRL'] = self.SYNTHLODIVFREQCTRL
        self.RACIFLILTENABLE = RM_Field_CMU_RFLOCK0_RACIFLILTENABLE(self)
        self.zz_fdict['RACIFLILTENABLE'] = self.RACIFLILTENABLE
        self.RACAUXPLL = RM_Field_CMU_RFLOCK0_RACAUXPLL(self)
        self.zz_fdict['RACAUXPLL'] = self.RACAUXPLL
        self.MODEMDEC1 = RM_Field_CMU_RFLOCK0_MODEMDEC1(self)
        self.zz_fdict['MODEMDEC1'] = self.MODEMDEC1
        self.MODEMANTDIVMODE = RM_Field_CMU_RFLOCK0_MODEMANTDIVMODE(self)
        self.zz_fdict['MODEMANTDIVMODE'] = self.MODEMANTDIVMODE
        self.RACIFPGAENPGA = RM_Field_CMU_RFLOCK0_RACIFPGAENPGA(self)
        self.zz_fdict['RACIFPGAENPGA'] = self.RACIFPGAENPGA
        self.RACPASLICE = RM_Field_CMU_RFLOCK0_RACPASLICE(self)
        self.zz_fdict['RACPASLICE'] = self.RACPASLICE
        self.RACSGPAEN = RM_Field_CMU_RFLOCK0_RACSGPAEN(self)
        self.zz_fdict['RACSGPAEN'] = self.RACSGPAEN
        self.RACPAEN = RM_Field_CMU_RFLOCK0_RACPAEN(self)
        self.zz_fdict['RACPAEN'] = self.RACPAEN
        self.RACPAEN0DBM = RM_Field_CMU_RFLOCK0_RACPAEN0DBM(self)
        self.zz_fdict['RACPAEN0DBM'] = self.RACPAEN0DBM
        self.FRCCONVMODE = RM_Field_CMU_RFLOCK0_FRCCONVMODE(self)
        self.zz_fdict['FRCCONVMODE'] = self.FRCCONVMODE
        self.FRCPAUSING = RM_Field_CMU_RFLOCK0_FRCPAUSING(self)
        self.zz_fdict['FRCPAUSING'] = self.FRCPAUSING
        self.MODEMDSSS = RM_Field_CMU_RFLOCK0_MODEMDSSS(self)
        self.zz_fdict['MODEMDSSS'] = self.MODEMDSSS
        self.MODEMMODFORMAT = RM_Field_CMU_RFLOCK0_MODEMMODFORMAT(self)
        self.zz_fdict['MODEMMODFORMAT'] = self.MODEMMODFORMAT
        self.MODEMDUALSYNC = RM_Field_CMU_RFLOCK0_MODEMDUALSYNC(self)
        self.zz_fdict['MODEMDUALSYNC'] = self.MODEMDUALSYNC
        self.UNLOCKED = RM_Field_CMU_RFLOCK0_UNLOCKED(self)
        self.zz_fdict['UNLOCKED'] = self.UNLOCKED
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFBUSCLKENMASK0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFBUSCLKENMASK0, self).__init__(rmio, label,
            0x400e4000, 0x190,
            'HFBUSCLKENMASK0', 'CMU.HFBUSCLKENMASK0', 'read-write',
            "",
            0x00003FFF, 0x00000032)

        self.CRYPTO = RM_Field_CMU_HFBUSCLKENMASK0_CRYPTO(self)
        self.zz_fdict['CRYPTO'] = self.CRYPTO
        self.LDMA = RM_Field_CMU_HFBUSCLKENMASK0_LDMA(self)
        self.zz_fdict['LDMA'] = self.LDMA
        self.GPCRC = RM_Field_CMU_HFBUSCLKENMASK0_GPCRC(self)
        self.zz_fdict['GPCRC'] = self.GPCRC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFPERCLKENMASK0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFPERCLKENMASK0, self).__init__(rmio, label,
            0x400e4000, 0x198,
            'HFPERCLKENMASK0', 'CMU.HFPERCLKENMASK0', 'read-write',
            "",
            0x00007FFF, 0x000003FF)

        self.TIMER0 = RM_Field_CMU_HFPERCLKENMASK0_TIMER0(self)
        self.zz_fdict['TIMER0'] = self.TIMER0
        self.TIMER1 = RM_Field_CMU_HFPERCLKENMASK0_TIMER1(self)
        self.zz_fdict['TIMER1'] = self.TIMER1
        self.USART0 = RM_Field_CMU_HFPERCLKENMASK0_USART0(self)
        self.zz_fdict['USART0'] = self.USART0
        self.USART1 = RM_Field_CMU_HFPERCLKENMASK0_USART1(self)
        self.zz_fdict['USART1'] = self.USART1
        self.ACMP0 = RM_Field_CMU_HFPERCLKENMASK0_ACMP0(self)
        self.zz_fdict['ACMP0'] = self.ACMP0
        self.ACMP1 = RM_Field_CMU_HFPERCLKENMASK0_ACMP1(self)
        self.zz_fdict['ACMP1'] = self.ACMP1
        self.CRYOTIMER = RM_Field_CMU_HFPERCLKENMASK0_CRYOTIMER(self)
        self.zz_fdict['CRYOTIMER'] = self.CRYOTIMER
        self.I2C0 = RM_Field_CMU_HFPERCLKENMASK0_I2C0(self)
        self.zz_fdict['I2C0'] = self.I2C0
        self.ADC0 = RM_Field_CMU_HFPERCLKENMASK0_ADC0(self)
        self.zz_fdict['ADC0'] = self.ADC0
        self.IDAC0 = RM_Field_CMU_HFPERCLKENMASK0_IDAC0(self)
        self.zz_fdict['IDAC0'] = self.IDAC0
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_HFRADIOCLKENMASK0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_HFRADIOCLKENMASK0, self).__init__(rmio, label,
            0x400e4000, 0x1A4,
            'HFRADIOCLKENMASK0', 'CMU.HFRADIOCLKENMASK0', 'read-write',
            "",
            0x000001FF, 0x000001FF)

        self.PROTIMER = RM_Field_CMU_HFRADIOCLKENMASK0_PROTIMER(self)
        self.zz_fdict['PROTIMER'] = self.PROTIMER
        self.RFSENSE = RM_Field_CMU_HFRADIOCLKENMASK0_RFSENSE(self)
        self.zz_fdict['RFSENSE'] = self.RFSENSE
        self.RAC = RM_Field_CMU_HFRADIOCLKENMASK0_RAC(self)
        self.zz_fdict['RAC'] = self.RAC
        self.FRC = RM_Field_CMU_HFRADIOCLKENMASK0_FRC(self)
        self.zz_fdict['FRC'] = self.FRC
        self.BUFC = RM_Field_CMU_HFRADIOCLKENMASK0_BUFC(self)
        self.zz_fdict['BUFC'] = self.BUFC
        self.CRC = RM_Field_CMU_HFRADIOCLKENMASK0_CRC(self)
        self.zz_fdict['CRC'] = self.CRC
        self.SYNTH = RM_Field_CMU_HFRADIOCLKENMASK0_SYNTH(self)
        self.zz_fdict['SYNTH'] = self.SYNTH
        self.MODEM = RM_Field_CMU_HFRADIOCLKENMASK0_MODEM(self)
        self.zz_fdict['MODEM'] = self.MODEM
        self.AGC = RM_Field_CMU_HFRADIOCLKENMASK0_AGC(self)
        self.zz_fdict['AGC'] = self.AGC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LFACLKENMASK0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LFACLKENMASK0, self).__init__(rmio, label,
            0x400e4000, 0x1B4,
            'LFACLKENMASK0', 'CMU.LFACLKENMASK0', 'read-write',
            "",
            0x00000001, 0x00000001)

        self.LETIMER0 = RM_Field_CMU_LFACLKENMASK0_LETIMER0(self)
        self.zz_fdict['LETIMER0'] = self.LETIMER0
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LFBCLKENMASK0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LFBCLKENMASK0, self).__init__(rmio, label,
            0x400e4000, 0x1BC,
            'LFBCLKENMASK0', 'CMU.LFBCLKENMASK0', 'read-write',
            "",
            0x00000001, 0x00000001)

        self.LEUART0 = RM_Field_CMU_LFBCLKENMASK0_LEUART0(self)
        self.zz_fdict['LEUART0'] = self.LEUART0
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_LFECLKENMASK0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_LFECLKENMASK0, self).__init__(rmio, label,
            0x400e4000, 0x1C4,
            'LFECLKENMASK0', 'CMU.LFECLKENMASK0', 'read-write',
            "",
            0x00000001, 0x00000001)

        self.RTCC = RM_Field_CMU_LFECLKENMASK0_RTCC(self)
        self.zz_fdict['RTCC'] = self.RTCC
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_PCNTCLKENMASK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_PCNTCLKENMASK, self).__init__(rmio, label,
            0x400e4000, 0x1CC,
            'PCNTCLKENMASK', 'CMU.PCNTCLKENMASK', 'read-write',
            "",
            0x00000001, 0x00000001)

        self.PCNT0 = RM_Field_CMU_PCNTCLKENMASK_PCNT0(self)
        self.zz_fdict['PCNT0'] = self.PCNT0
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_TEST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_TEST, self).__init__(rmio, label,
            0x400e4000, 0x1D0,
            'TEST', 'CMU.TEST', 'read-write',
            "",
            0x00000000, 0x1F00FF01)

        self.EMUOSCLV = RM_Field_CMU_TEST_EMUOSCLV(self)
        self.zz_fdict['EMUOSCLV'] = self.EMUOSCLV
        self.CLKOUTHIDDENSEL = RM_Field_CMU_TEST_CLKOUTHIDDENSEL(self)
        self.zz_fdict['CLKOUTHIDDENSEL'] = self.CLKOUTHIDDENSEL
        self.OSCCTRLSEL = RM_Field_CMU_TEST_OSCCTRLSEL(self)
        self.zz_fdict['OSCCTRLSEL'] = self.OSCCTRLSEL
        self.LEWSYNCPRS = RM_Field_CMU_TEST_LEWSYNCPRS(self)
        self.zz_fdict['LEWSYNCPRS'] = self.LEWSYNCPRS
        self.LEWSYNCBLOCK = RM_Field_CMU_TEST_LEWSYNCBLOCK(self)
        self.zz_fdict['LEWSYNCBLOCK'] = self.LEWSYNCBLOCK
        self.LEWSYNCDELAY = RM_Field_CMU_TEST_LEWSYNCDELAY(self)
        self.zz_fdict['LEWSYNCDELAY'] = self.LEWSYNCDELAY
        self.LEWSYNCOBS = RM_Field_CMU_TEST_LEWSYNCOBS(self)
        self.zz_fdict['LEWSYNCOBS'] = self.LEWSYNCOBS
        self.LEWSYNCOBSINV = RM_Field_CMU_TEST_LEWSYNCOBSINV(self)
        self.zz_fdict['LEWSYNCOBSINV'] = self.LEWSYNCOBSINV
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_TESTHFRCOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_TESTHFRCOCTRL, self).__init__(rmio, label,
            0x400e4000, 0x1D4,
            'TESTHFRCOCTRL', 'CMU.TESTHFRCOCTRL', 'read-write',
            "",
            0x000000F0, 0x000001F1)

        self.CMPBIASSWDIS = RM_Field_CMU_TESTHFRCOCTRL_CMPBIASSWDIS(self)
        self.zz_fdict['CMPBIASSWDIS'] = self.CMPBIASSWDIS
        self.SPREADCAL = RM_Field_CMU_TESTHFRCOCTRL_SPREADCAL(self)
        self.zz_fdict['SPREADCAL'] = self.SPREADCAL
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_TESTAUXHFRCOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_TESTAUXHFRCOCTRL, self).__init__(rmio, label,
            0x400e4000, 0x1D8,
            'TESTAUXHFRCOCTRL', 'CMU.TESTAUXHFRCOCTRL', 'read-write',
            "",
            0x000000F0, 0x000001F1)

        self.CMPBIASSWDIS = RM_Field_CMU_TESTAUXHFRCOCTRL_CMPBIASSWDIS(self)
        self.zz_fdict['CMPBIASSWDIS'] = self.CMPBIASSWDIS
        self.SPREADCAL = RM_Field_CMU_TESTAUXHFRCOCTRL_SPREADCAL(self)
        self.zz_fdict['SPREADCAL'] = self.SPREADCAL
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_TESTLFRCOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_TESTLFRCOCTRL, self).__init__(rmio, label,
            0x400e4000, 0x1DC,
            'TESTLFRCOCTRL', 'CMU.TESTLFRCOCTRL', 'read-write',
            "",
            0x00000100, 0x0FF1FFF3)

        self.DISOSC = RM_Field_CMU_TESTLFRCOCTRL_DISOSC(self)
        self.zz_fdict['DISOSC'] = self.DISOSC
        self.DISSYNC = RM_Field_CMU_TESTLFRCOCTRL_DISSYNC(self)
        self.zz_fdict['DISSYNC'] = self.DISSYNC
        self.MODE = RM_Field_CMU_TESTLFRCOCTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.SELCLKDIV = RM_Field_CMU_TESTLFRCOCTRL_SELCLKDIV(self)
        self.zz_fdict['SELCLKDIV'] = self.SELCLKDIV
        self.VREFUPDATE = RM_Field_CMU_TESTLFRCOCTRL_VREFUPDATE(self)
        self.zz_fdict['VREFUPDATE'] = self.VREFUPDATE
        self.VREFPRECH = RM_Field_CMU_TESTLFRCOCTRL_VREFPRECH(self)
        self.zz_fdict['VREFPRECH'] = self.VREFPRECH
        self.FLIPCHOP = RM_Field_CMU_TESTLFRCOCTRL_FLIPCHOP(self)
        self.zz_fdict['FLIPCHOP'] = self.FLIPCHOP
        self.DEMCLKSEL = RM_Field_CMU_TESTLFRCOCTRL_DEMCLKSEL(self)
        self.zz_fdict['DEMCLKSEL'] = self.DEMCLKSEL
        self.WELLBUFDIS = RM_Field_CMU_TESTLFRCOCTRL_WELLBUFDIS(self)
        self.zz_fdict['WELLBUFDIS'] = self.WELLBUFDIS
        self.FORCECOMP = RM_Field_CMU_TESTLFRCOCTRL_FORCECOMP(self)
        self.zz_fdict['FORCECOMP'] = self.FORCECOMP
        self.BLOCKIREF = RM_Field_CMU_TESTLFRCOCTRL_BLOCKIREF(self)
        self.zz_fdict['BLOCKIREF'] = self.BLOCKIREF
        self.RNSHUNT = RM_Field_CMU_TESTLFRCOCTRL_RNSHUNT(self)
        self.zz_fdict['RNSHUNT'] = self.RNSHUNT
        self.RPSHUNT = RM_Field_CMU_TESTLFRCOCTRL_RPSHUNT(self)
        self.zz_fdict['RPSHUNT'] = self.RPSHUNT
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_TESTHFXOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_TESTHFXOCTRL, self).__init__(rmio, label,
            0x400e4000, 0x1E0,
            'TESTHFXOCTRL', 'CMU.TESTHFXOCTRL', 'read-write',
            "",
            0x00000100, 0x00003FFF)

        self.OVERRIDE = RM_Field_CMU_TESTHFXOCTRL_OVERRIDE(self)
        self.zz_fdict['OVERRIDE'] = self.OVERRIDE
        self.BIASEN = RM_Field_CMU_TESTHFXOCTRL_BIASEN(self)
        self.zz_fdict['BIASEN'] = self.BIASEN
        self.CLKDIGEN = RM_Field_CMU_TESTHFXOCTRL_CLKDIGEN(self)
        self.zz_fdict['CLKDIGEN'] = self.CLKDIGEN
        self.CLKAUXPLLEN = RM_Field_CMU_TESTHFXOCTRL_CLKAUXPLLEN(self)
        self.zz_fdict['CLKAUXPLLEN'] = self.CLKAUXPLLEN
        self.CLKIFADCEN = RM_Field_CMU_TESTHFXOCTRL_CLKIFADCEN(self)
        self.zz_fdict['CLKIFADCEN'] = self.CLKIFADCEN
        self.CLKSYEN = RM_Field_CMU_TESTHFXOCTRL_CLKSYEN(self)
        self.zz_fdict['CLKSYEN'] = self.CLKSYEN
        self.COREEN = RM_Field_CMU_TESTHFXOCTRL_COREEN(self)
        self.zz_fdict['COREEN'] = self.COREEN
        self.REGEN = RM_Field_CMU_TESTHFXOCTRL_REGEN(self)
        self.zz_fdict['REGEN'] = self.REGEN
        self.DOXTALKICK = RM_Field_CMU_TESTHFXOCTRL_DOXTALKICK(self)
        self.zz_fdict['DOXTALKICK'] = self.DOXTALKICK
        self.CLKDIGINV = RM_Field_CMU_TESTHFXOCTRL_CLKDIGINV(self)
        self.zz_fdict['CLKDIGINV'] = self.CLKDIGINV
        self.CLKAUXPLLINV = RM_Field_CMU_TESTHFXOCTRL_CLKAUXPLLINV(self)
        self.zz_fdict['CLKAUXPLLINV'] = self.CLKAUXPLLINV
        self.CLKIFADCINV = RM_Field_CMU_TESTHFXOCTRL_CLKIFADCINV(self)
        self.zz_fdict['CLKIFADCINV'] = self.CLKIFADCINV
        self.CLKSYINV = RM_Field_CMU_TESTHFXOCTRL_CLKSYINV(self)
        self.zz_fdict['CLKSYINV'] = self.CLKSYINV
        self.CLKDRIVERSDIS = RM_Field_CMU_TESTHFXOCTRL_CLKDRIVERSDIS(self)
        self.zz_fdict['CLKDRIVERSDIS'] = self.CLKDRIVERSDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_CMU_TESTLFXOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CMU_TESTLFXOCTRL, self).__init__(rmio, label,
            0x400e4000, 0x1E4,
            'TESTLFXOCTRL', 'CMU.TESTLFXOCTRL', 'read-write',
            "",
            0x00000001, 0x00000001)

        self.LFXOBLEEDER = RM_Field_CMU_TESTLFXOCTRL_LFXOBLEEDER(self)
        self.zz_fdict['LFXOBLEEDER'] = self.LFXOBLEEDER
        self.__dict__['zz_frozen'] = True


