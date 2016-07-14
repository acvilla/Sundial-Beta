
from static import Base_RM_Field
from CMU_enum import *


class RM_Field_CMU_CTRL_CLKOUTSEL0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CTRL_CLKOUTSEL0, self).__init__(register,
            'CLKOUTSEL0', 'CMU.CTRL.CLKOUTSEL0', 'read-write',
            "",
            0, 4,
            RM_Enum_CMU_CTRL_CLKOUTSEL0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_CTRL_CLKOUTSEL1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CTRL_CLKOUTSEL1, self).__init__(register,
            'CLKOUTSEL1', 'CMU.CTRL.CLKOUTSEL1', 'read-write',
            "",
            5, 4,
            RM_Enum_CMU_CTRL_CLKOUTSEL1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_CTRL_WSHFLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CTRL_WSHFLE, self).__init__(register,
            'WSHFLE', 'CMU.CTRL.WSHFLE', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_CTRL_HFPERCLKEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CTRL_HFPERCLKEN, self).__init__(register,
            'HFPERCLKEN', 'CMU.CTRL.HFPERCLKEN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_CTRL_HFRADIOCLKEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CTRL_HFRADIOCLKEN, self).__init__(register,
            'HFRADIOCLKEN', 'CMU.CTRL.HFRADIOCLKEN', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRCOCTRL_TUNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRCOCTRL_TUNING, self).__init__(register,
            'TUNING', 'CMU.HFRCOCTRL.TUNING', 'read-write',
            "",
            0, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRCOCTRL_FINETUNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRCOCTRL_FINETUNING, self).__init__(register,
            'FINETUNING', 'CMU.HFRCOCTRL.FINETUNING', 'read-write',
            "",
            8, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRCOCTRL_FREQRANGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRCOCTRL_FREQRANGE, self).__init__(register,
            'FREQRANGE', 'CMU.HFRCOCTRL.FREQRANGE', 'read-write',
            "",
            16, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRCOCTRL_CMPBIAS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRCOCTRL_CMPBIAS, self).__init__(register,
            'CMPBIAS', 'CMU.HFRCOCTRL.CMPBIAS', 'read-write',
            "",
            21, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRCOCTRL_LDOHP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRCOCTRL_LDOHP, self).__init__(register,
            'LDOHP', 'CMU.HFRCOCTRL.LDOHP', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRCOCTRL_CLKDIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRCOCTRL_CLKDIV, self).__init__(register,
            'CLKDIV', 'CMU.HFRCOCTRL.CLKDIV', 'read-write',
            "",
            25, 2,
            RM_Enum_CMU_HFRCOCTRL_CLKDIV(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRCOCTRL_FINETUNINGEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRCOCTRL_FINETUNINGEN, self).__init__(register,
            'FINETUNINGEN', 'CMU.HFRCOCTRL.FINETUNINGEN', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRCOCTRL_VREFTC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRCOCTRL_VREFTC, self).__init__(register,
            'VREFTC', 'CMU.HFRCOCTRL.VREFTC', 'read-write',
            "",
            28, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRCOLDOCTRL_STANDBY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRCOLDOCTRL_STANDBY, self).__init__(register,
            'STANDBY', 'CMU.HFRCOLDOCTRL.STANDBY', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRCOLDOCTRL_PSRENHANCE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRCOLDOCTRL_PSRENHANCE, self).__init__(register,
            'PSRENHANCE', 'CMU.HFRCOLDOCTRL.PSRENHANCE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRCOLDOCTRL_PDDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRCOLDOCTRL_PDDIS, self).__init__(register,
            'PDDIS', 'CMU.HFRCOLDOCTRL.PDDIS', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRCOLDOCTRL_TRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRCOLDOCTRL_TRIM, self).__init__(register,
            'TRIM', 'CMU.HFRCOLDOCTRL.TRIM', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_AUXHFRCOCTRL_TUNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_AUXHFRCOCTRL_TUNING, self).__init__(register,
            'TUNING', 'CMU.AUXHFRCOCTRL.TUNING', 'read-write',
            "",
            0, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_AUXHFRCOCTRL_FINETUNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_AUXHFRCOCTRL_FINETUNING, self).__init__(register,
            'FINETUNING', 'CMU.AUXHFRCOCTRL.FINETUNING', 'read-write',
            "",
            8, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_AUXHFRCOCTRL_FREQRANGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_AUXHFRCOCTRL_FREQRANGE, self).__init__(register,
            'FREQRANGE', 'CMU.AUXHFRCOCTRL.FREQRANGE', 'read-write',
            "",
            16, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_AUXHFRCOCTRL_CMPBIAS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_AUXHFRCOCTRL_CMPBIAS, self).__init__(register,
            'CMPBIAS', 'CMU.AUXHFRCOCTRL.CMPBIAS', 'read-write',
            "",
            21, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_AUXHFRCOCTRL_LDOHP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_AUXHFRCOCTRL_LDOHP, self).__init__(register,
            'LDOHP', 'CMU.AUXHFRCOCTRL.LDOHP', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_AUXHFRCOCTRL_CLKDIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_AUXHFRCOCTRL_CLKDIV, self).__init__(register,
            'CLKDIV', 'CMU.AUXHFRCOCTRL.CLKDIV', 'read-write',
            "",
            25, 2,
            RM_Enum_CMU_AUXHFRCOCTRL_CLKDIV(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_AUXHFRCOCTRL_FINETUNINGEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_AUXHFRCOCTRL_FINETUNINGEN, self).__init__(register,
            'FINETUNINGEN', 'CMU.AUXHFRCOCTRL.FINETUNINGEN', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_AUXHFRCOCTRL_VREFTC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_AUXHFRCOCTRL_VREFTC, self).__init__(register,
            'VREFTC', 'CMU.AUXHFRCOCTRL.VREFTC', 'read-write',
            "",
            28, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_AUXHFRCOLDOCTRL_STANDBY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_AUXHFRCOLDOCTRL_STANDBY, self).__init__(register,
            'STANDBY', 'CMU.AUXHFRCOLDOCTRL.STANDBY', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_AUXHFRCOLDOCTRL_PSRENHANCE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_AUXHFRCOLDOCTRL_PSRENHANCE, self).__init__(register,
            'PSRENHANCE', 'CMU.AUXHFRCOLDOCTRL.PSRENHANCE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_AUXHFRCOLDOCTRL_PDDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_AUXHFRCOLDOCTRL_PDDIS, self).__init__(register,
            'PDDIS', 'CMU.AUXHFRCOLDOCTRL.PDDIS', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_AUXHFRCOLDOCTRL_TRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_AUXHFRCOLDOCTRL_TRIM, self).__init__(register,
            'TRIM', 'CMU.AUXHFRCOLDOCTRL.TRIM', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFRCOCTRL_TUNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFRCOCTRL_TUNING, self).__init__(register,
            'TUNING', 'CMU.LFRCOCTRL.TUNING', 'read-write',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFRCOCTRL_ENVREF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFRCOCTRL_ENVREF, self).__init__(register,
            'ENVREF', 'CMU.LFRCOCTRL.ENVREF', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFRCOCTRL_ENCHOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFRCOCTRL_ENCHOP, self).__init__(register,
            'ENCHOP', 'CMU.LFRCOCTRL.ENCHOP', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFRCOCTRL_ENDEM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFRCOCTRL_ENDEM, self).__init__(register,
            'ENDEM', 'CMU.LFRCOCTRL.ENDEM', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFRCOCTRL_VREFUPDATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFRCOCTRL_VREFUPDATE, self).__init__(register,
            'VREFUPDATE', 'CMU.LFRCOCTRL.VREFUPDATE', 'read-write',
            "",
            20, 2,
            RM_Enum_CMU_LFRCOCTRL_VREFUPDATE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFRCOCTRL_TIMEOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFRCOCTRL_TIMEOUT, self).__init__(register,
            'TIMEOUT', 'CMU.LFRCOCTRL.TIMEOUT', 'read-write',
            "",
            24, 2,
            RM_Enum_CMU_LFRCOCTRL_TIMEOUT(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFRCOCTRL_GMCCURTUNE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFRCOCTRL_GMCCURTUNE, self).__init__(register,
            'GMCCURTUNE', 'CMU.LFRCOCTRL.GMCCURTUNE', 'read-write',
            "",
            28, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOCTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOCTRL_MODE, self).__init__(register,
            'MODE', 'CMU.HFXOCTRL.MODE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOCTRL_PEAKDETSHUNTOPTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOCTRL_PEAKDETSHUNTOPTMODE, self).__init__(register,
            'PEAKDETSHUNTOPTMODE', 'CMU.HFXOCTRL.PEAKDETSHUNTOPTMODE', 'read-write',
            "",
            4, 2,
            RM_Enum_CMU_HFXOCTRL_PEAKDETSHUNTOPTMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOCTRL_LOWPOWER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOCTRL_LOWPOWER, self).__init__(register,
            'LOWPOWER', 'CMU.HFXOCTRL.LOWPOWER', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOCTRL_XTI2GND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOCTRL_XTI2GND, self).__init__(register,
            'XTI2GND', 'CMU.HFXOCTRL.XTI2GND', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOCTRL_XTO2GND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOCTRL_XTO2GND, self).__init__(register,
            'XTO2GND', 'CMU.HFXOCTRL.XTO2GND', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOCTRL_LFTIMEOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOCTRL_LFTIMEOUT, self).__init__(register,
            'LFTIMEOUT', 'CMU.HFXOCTRL.LFTIMEOUT', 'read-write',
            "",
            24, 3,
            RM_Enum_CMU_HFXOCTRL_LFTIMEOUT(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOCTRL_AUTOSTARTEM0EM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOCTRL_AUTOSTARTEM0EM1, self).__init__(register,
            'AUTOSTARTEM0EM1', 'CMU.HFXOCTRL.AUTOSTARTEM0EM1', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOCTRL_AUTOSTARTSELEM0EM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOCTRL_AUTOSTARTSELEM0EM1, self).__init__(register,
            'AUTOSTARTSELEM0EM1', 'CMU.HFXOCTRL.AUTOSTARTSELEM0EM1', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOCTRL_AUTOSTARTRDYSELRAC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOCTRL_AUTOSTARTRDYSELRAC, self).__init__(register,
            'AUTOSTARTRDYSELRAC', 'CMU.HFXOCTRL.AUTOSTARTRDYSELRAC', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOCTRL1_PEAKDETTHR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOCTRL1_PEAKDETTHR, self).__init__(register,
            'PEAKDETTHR', 'CMU.HFXOCTRL1.PEAKDETTHR', 'read-write',
            "",
            0, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOCTRL1_REGLVL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOCTRL1_REGLVL, self).__init__(register,
            'REGLVL', 'CMU.HFXOCTRL1.REGLVL', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOCTRL1_SQBLWPDCEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOCTRL1_SQBLWPDCEN, self).__init__(register,
            'SQBLWPDCEN', 'CMU.HFXOCTRL1.SQBLWPDCEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOCTRL1_XTIBIASEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOCTRL1_XTIBIASEN, self).__init__(register,
            'XTIBIASEN', 'CMU.HFXOCTRL1.XTIBIASEN', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOCTRL1_SQBMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOCTRL1_SQBMODE, self).__init__(register,
            'SQBMODE', 'CMU.HFXOCTRL1.SQBMODE', 'read-write',
            "",
            10, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOSTARTUPCTRL_IBTRIMXOCORE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOSTARTUPCTRL_IBTRIMXOCORE, self).__init__(register,
            'IBTRIMXOCORE', 'CMU.HFXOSTARTUPCTRL.IBTRIMXOCORE', 'read-write',
            "",
            0, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOSTARTUPCTRL_CTUNE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOSTARTUPCTRL_CTUNE, self).__init__(register,
            'CTUNE', 'CMU.HFXOSTARTUPCTRL.CTUNE', 'read-write',
            "",
            11, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOSTEADYSTATECTRL_IBTRIMXOCORE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOSTEADYSTATECTRL_IBTRIMXOCORE, self).__init__(register,
            'IBTRIMXOCORE', 'CMU.HFXOSTEADYSTATECTRL.IBTRIMXOCORE', 'read-write',
            "",
            0, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOSTEADYSTATECTRL_REGISH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOSTEADYSTATECTRL_REGISH, self).__init__(register,
            'REGISH', 'CMU.HFXOSTEADYSTATECTRL.REGISH', 'read-write',
            "",
            7, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOSTEADYSTATECTRL_CTUNE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOSTEADYSTATECTRL_CTUNE, self).__init__(register,
            'CTUNE', 'CMU.HFXOSTEADYSTATECTRL.CTUNE', 'read-write',
            "",
            11, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOSTEADYSTATECTRL_REGSELILOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOSTEADYSTATECTRL_REGSELILOW, self).__init__(register,
            'REGSELILOW', 'CMU.HFXOSTEADYSTATECTRL.REGSELILOW', 'read-write',
            "",
            24, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOSTEADYSTATECTRL_PEAKDETEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOSTEADYSTATECTRL_PEAKDETEN, self).__init__(register,
            'PEAKDETEN', 'CMU.HFXOSTEADYSTATECTRL.PEAKDETEN', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOSTEADYSTATECTRL_REGISHUPPER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOSTEADYSTATECTRL_REGISHUPPER, self).__init__(register,
            'REGISHUPPER', 'CMU.HFXOSTEADYSTATECTRL.REGISHUPPER', 'read-write',
            "",
            28, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOTIMEOUTCTRL_STARTUPTIMEOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOTIMEOUTCTRL_STARTUPTIMEOUT, self).__init__(register,
            'STARTUPTIMEOUT', 'CMU.HFXOTIMEOUTCTRL.STARTUPTIMEOUT', 'read-write',
            "",
            0, 4,
            RM_Enum_CMU_HFXOTIMEOUTCTRL_STARTUPTIMEOUT(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOTIMEOUTCTRL_STEADYTIMEOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOTIMEOUTCTRL_STEADYTIMEOUT, self).__init__(register,
            'STEADYTIMEOUT', 'CMU.HFXOTIMEOUTCTRL.STEADYTIMEOUT', 'read-write',
            "",
            4, 4,
            RM_Enum_CMU_HFXOTIMEOUTCTRL_STEADYTIMEOUT(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOTIMEOUTCTRL_PEAKDETTIMEOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOTIMEOUTCTRL_PEAKDETTIMEOUT, self).__init__(register,
            'PEAKDETTIMEOUT', 'CMU.HFXOTIMEOUTCTRL.PEAKDETTIMEOUT', 'read-write',
            "",
            12, 4,
            RM_Enum_CMU_HFXOTIMEOUTCTRL_PEAKDETTIMEOUT(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOTIMEOUTCTRL_SHUNTOPTTIMEOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOTIMEOUTCTRL_SHUNTOPTTIMEOUT, self).__init__(register,
            'SHUNTOPTTIMEOUT', 'CMU.HFXOTIMEOUTCTRL.SHUNTOPTTIMEOUT', 'read-write',
            "",
            16, 4,
            RM_Enum_CMU_HFXOTIMEOUTCTRL_SHUNTOPTTIMEOUT(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFXOCTRL_TUNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFXOCTRL_TUNING, self).__init__(register,
            'TUNING', 'CMU.LFXOCTRL.TUNING', 'read-write',
            "",
            0, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFXOCTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFXOCTRL_MODE, self).__init__(register,
            'MODE', 'CMU.LFXOCTRL.MODE', 'read-write',
            "",
            8, 2,
            RM_Enum_CMU_LFXOCTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFXOCTRL_GAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFXOCTRL_GAIN, self).__init__(register,
            'GAIN', 'CMU.LFXOCTRL.GAIN', 'read-write',
            "",
            11, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFXOCTRL_HIGHAMPL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFXOCTRL_HIGHAMPL, self).__init__(register,
            'HIGHAMPL', 'CMU.LFXOCTRL.HIGHAMPL', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFXOCTRL_AGC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFXOCTRL_AGC, self).__init__(register,
            'AGC', 'CMU.LFXOCTRL.AGC', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFXOCTRL_CUR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFXOCTRL_CUR, self).__init__(register,
            'CUR', 'CMU.LFXOCTRL.CUR', 'read-write',
            "",
            16, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFXOCTRL_BUFCUR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFXOCTRL_BUFCUR, self).__init__(register,
            'BUFCUR', 'CMU.LFXOCTRL.BUFCUR', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFXOCTRL_TIMEOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFXOCTRL_TIMEOUT, self).__init__(register,
            'TIMEOUT', 'CMU.LFXOCTRL.TIMEOUT', 'read-write',
            "",
            24, 3,
            RM_Enum_CMU_LFXOCTRL_TIMEOUT(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_ULFRCOCTRL_TUNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_ULFRCOCTRL_TUNING, self).__init__(register,
            'TUNING', 'CMU.ULFRCOCTRL.TUNING', 'read-write',
            "",
            0, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_ULFRCOCTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_ULFRCOCTRL_EN, self).__init__(register,
            'EN', 'CMU.ULFRCOCTRL.EN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_ULFRCOCTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_ULFRCOCTRL_MODE, self).__init__(register,
            'MODE', 'CMU.ULFRCOCTRL.MODE', 'read-write',
            "",
            10, 2,
            RM_Enum_CMU_ULFRCOCTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_ULFRCOCTRL_RESTRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_ULFRCOCTRL_RESTRIM, self).__init__(register,
            'RESTRIM', 'CMU.ULFRCOCTRL.RESTRIM', 'read-write',
            "",
            16, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_DPLLCTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_DPLLCTRL_MODE, self).__init__(register,
            'MODE', 'CMU.DPLLCTRL.MODE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_DPLLCTRL_EDGESEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_DPLLCTRL_EDGESEL, self).__init__(register,
            'EDGESEL', 'CMU.DPLLCTRL.EDGESEL', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_DPLLCTRL_AUTORECOVER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_DPLLCTRL_AUTORECOVER, self).__init__(register,
            'AUTORECOVER', 'CMU.DPLLCTRL.AUTORECOVER', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_DPLLCTRL_REFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_DPLLCTRL_REFSEL, self).__init__(register,
            'REFSEL', 'CMU.DPLLCTRL.REFSEL', 'read-write',
            "",
            3, 2,
            RM_Enum_CMU_DPLLCTRL_REFSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_DPLLCTRL1_M(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_DPLLCTRL1_M, self).__init__(register,
            'M', 'CMU.DPLLCTRL1.M', 'read-write',
            "",
            0, 12)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_DPLLCTRL1_N(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_DPLLCTRL1_N, self).__init__(register,
            'N', 'CMU.DPLLCTRL1.N', 'read-write',
            "",
            16, 12)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_CALCTRL_UPSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CALCTRL_UPSEL, self).__init__(register,
            'UPSEL', 'CMU.CALCTRL.UPSEL', 'read-write',
            "",
            0, 3,
            RM_Enum_CMU_CALCTRL_UPSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_CALCTRL_DOWNSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CALCTRL_DOWNSEL, self).__init__(register,
            'DOWNSEL', 'CMU.CALCTRL.DOWNSEL', 'read-write',
            "",
            4, 3,
            RM_Enum_CMU_CALCTRL_DOWNSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_CALCTRL_CONT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CALCTRL_CONT, self).__init__(register,
            'CONT', 'CMU.CALCTRL.CONT', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_CALCTRL_PRSUPSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CALCTRL_PRSUPSEL, self).__init__(register,
            'PRSUPSEL', 'CMU.CALCTRL.PRSUPSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_CMU_CALCTRL_PRSUPSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_CALCTRL_PRSDOWNSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CALCTRL_PRSDOWNSEL, self).__init__(register,
            'PRSDOWNSEL', 'CMU.CALCTRL.PRSDOWNSEL', 'read-write',
            "",
            24, 4,
            RM_Enum_CMU_CALCTRL_PRSDOWNSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_CALCNT_CALCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CALCNT_CALCNT, self).__init__(register,
            'CALCNT', 'CMU.CALCNT.CALCNT', 'read-write',
            "",
            0, 20)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_OSCENCMD_HFRCOEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_OSCENCMD_HFRCOEN, self).__init__(register,
            'HFRCOEN', 'CMU.OSCENCMD.HFRCOEN', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_OSCENCMD_HFRCODIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_OSCENCMD_HFRCODIS, self).__init__(register,
            'HFRCODIS', 'CMU.OSCENCMD.HFRCODIS', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_OSCENCMD_HFXOEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_OSCENCMD_HFXOEN, self).__init__(register,
            'HFXOEN', 'CMU.OSCENCMD.HFXOEN', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_OSCENCMD_HFXODIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_OSCENCMD_HFXODIS, self).__init__(register,
            'HFXODIS', 'CMU.OSCENCMD.HFXODIS', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_OSCENCMD_AUXHFRCOEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_OSCENCMD_AUXHFRCOEN, self).__init__(register,
            'AUXHFRCOEN', 'CMU.OSCENCMD.AUXHFRCOEN', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_OSCENCMD_AUXHFRCODIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_OSCENCMD_AUXHFRCODIS, self).__init__(register,
            'AUXHFRCODIS', 'CMU.OSCENCMD.AUXHFRCODIS', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_OSCENCMD_LFRCOEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_OSCENCMD_LFRCOEN, self).__init__(register,
            'LFRCOEN', 'CMU.OSCENCMD.LFRCOEN', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_OSCENCMD_LFRCODIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_OSCENCMD_LFRCODIS, self).__init__(register,
            'LFRCODIS', 'CMU.OSCENCMD.LFRCODIS', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_OSCENCMD_LFXOEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_OSCENCMD_LFXOEN, self).__init__(register,
            'LFXOEN', 'CMU.OSCENCMD.LFXOEN', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_OSCENCMD_LFXODIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_OSCENCMD_LFXODIS, self).__init__(register,
            'LFXODIS', 'CMU.OSCENCMD.LFXODIS', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_OSCENCMD_DPLLEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_OSCENCMD_DPLLEN, self).__init__(register,
            'DPLLEN', 'CMU.OSCENCMD.DPLLEN', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_OSCENCMD_DPLLDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_OSCENCMD_DPLLDIS, self).__init__(register,
            'DPLLDIS', 'CMU.OSCENCMD.DPLLDIS', 'write-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_CMD_CALSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CMD_CALSTART, self).__init__(register,
            'CALSTART', 'CMU.CMD.CALSTART', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_CMD_CALSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CMD_CALSTOP, self).__init__(register,
            'CALSTOP', 'CMU.CMD.CALSTOP', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_CMD_HFXOPEAKDETSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CMD_HFXOPEAKDETSTART, self).__init__(register,
            'HFXOPEAKDETSTART', 'CMU.CMD.HFXOPEAKDETSTART', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_CMD_HFXOSHUNTOPTSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_CMD_HFXOSHUNTOPTSTART, self).__init__(register,
            'HFXOSHUNTOPTSTART', 'CMU.CMD.HFXOSHUNTOPTSTART', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_DBGCLKSEL_DBG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_DBGCLKSEL_DBG, self).__init__(register,
            'DBG', 'CMU.DBGCLKSEL.DBG', 'read-write',
            "",
            0, 1,
            RM_Enum_CMU_DBGCLKSEL_DBG(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFCLKSEL_HF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFCLKSEL_HF, self).__init__(register,
            'HF', 'CMU.HFCLKSEL.HF', 'write-only',
            "",
            0, 3,
            RM_Enum_CMU_HFCLKSEL_HF(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFACLKSEL_LFA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFACLKSEL_LFA, self).__init__(register,
            'LFA', 'CMU.LFACLKSEL.LFA', 'read-write',
            "",
            0, 3,
            RM_Enum_CMU_LFACLKSEL_LFA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFBCLKSEL_LFB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFBCLKSEL_LFB, self).__init__(register,
            'LFB', 'CMU.LFBCLKSEL.LFB', 'read-write',
            "",
            0, 3,
            RM_Enum_CMU_LFBCLKSEL_LFB(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFECLKSEL_LFE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFECLKSEL_LFE, self).__init__(register,
            'LFE', 'CMU.LFECLKSEL.LFE', 'read-write',
            "",
            0, 3,
            RM_Enum_CMU_LFECLKSEL_LFE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_HFRCOENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_HFRCOENS, self).__init__(register,
            'HFRCOENS', 'CMU.STATUS.HFRCOENS', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_HFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_HFRCORDY, self).__init__(register,
            'HFRCORDY', 'CMU.STATUS.HFRCORDY', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_HFXOENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_HFXOENS, self).__init__(register,
            'HFXOENS', 'CMU.STATUS.HFXOENS', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_HFXORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_HFXORDY, self).__init__(register,
            'HFXORDY', 'CMU.STATUS.HFXORDY', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_AUXHFRCOENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_AUXHFRCOENS, self).__init__(register,
            'AUXHFRCOENS', 'CMU.STATUS.AUXHFRCOENS', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_AUXHFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_AUXHFRCORDY, self).__init__(register,
            'AUXHFRCORDY', 'CMU.STATUS.AUXHFRCORDY', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_LFRCOENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_LFRCOENS, self).__init__(register,
            'LFRCOENS', 'CMU.STATUS.LFRCOENS', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_LFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_LFRCORDY, self).__init__(register,
            'LFRCORDY', 'CMU.STATUS.LFRCORDY', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_LFXOENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_LFXOENS, self).__init__(register,
            'LFXOENS', 'CMU.STATUS.LFXOENS', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_LFXORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_LFXORDY, self).__init__(register,
            'LFXORDY', 'CMU.STATUS.LFXORDY', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_DPLLENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_DPLLENS, self).__init__(register,
            'DPLLENS', 'CMU.STATUS.DPLLENS', 'read-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_DPLLRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_DPLLRDY, self).__init__(register,
            'DPLLRDY', 'CMU.STATUS.DPLLRDY', 'read-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_CALRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_CALRDY, self).__init__(register,
            'CALRDY', 'CMU.STATUS.CALRDY', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_HFXOREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_HFXOREQ, self).__init__(register,
            'HFXOREQ', 'CMU.STATUS.HFXOREQ', 'read-only',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_HFXOPEAKDETRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_HFXOPEAKDETRDY, self).__init__(register,
            'HFXOPEAKDETRDY', 'CMU.STATUS.HFXOPEAKDETRDY', 'read-only',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_HFXOSHUNTOPTRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_HFXOSHUNTOPTRDY, self).__init__(register,
            'HFXOSHUNTOPTRDY', 'CMU.STATUS.HFXOSHUNTOPTRDY', 'read-only',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_HFXOAMPHIGH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_HFXOAMPHIGH, self).__init__(register,
            'HFXOAMPHIGH', 'CMU.STATUS.HFXOAMPHIGH', 'read-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_HFXOAMPLOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_HFXOAMPLOW, self).__init__(register,
            'HFXOAMPLOW', 'CMU.STATUS.HFXOAMPLOW', 'read-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_STATUS_HFXOREGILOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_STATUS_HFXOREGILOW, self).__init__(register,
            'HFXOREGILOW', 'CMU.STATUS.HFXOREGILOW', 'read-only',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFCLKSTATUS_SELECTED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFCLKSTATUS_SELECTED, self).__init__(register,
            'SELECTED', 'CMU.HFCLKSTATUS.SELECTED', 'read-only',
            "",
            0, 3,
            RM_Enum_CMU_HFCLKSTATUS_SELECTED(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOTRIMSTATUS_IBTRIMXOCORE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOTRIMSTATUS_IBTRIMXOCORE, self).__init__(register,
            'IBTRIMXOCORE', 'CMU.HFXOTRIMSTATUS.IBTRIMXOCORE', 'read-only',
            "",
            0, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFXOTRIMSTATUS_REGISH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFXOTRIMSTATUS_REGISH, self).__init__(register,
            'REGISH', 'CMU.HFXOTRIMSTATUS.REGISH', 'read-only',
            "",
            7, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_HFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_HFRCORDY, self).__init__(register,
            'HFRCORDY', 'CMU.IF.HFRCORDY', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_HFXORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_HFXORDY, self).__init__(register,
            'HFXORDY', 'CMU.IF.HFXORDY', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_LFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_LFRCORDY, self).__init__(register,
            'LFRCORDY', 'CMU.IF.LFRCORDY', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_LFXORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_LFXORDY, self).__init__(register,
            'LFXORDY', 'CMU.IF.LFXORDY', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_AUXHFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_AUXHFRCORDY, self).__init__(register,
            'AUXHFRCORDY', 'CMU.IF.AUXHFRCORDY', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_CALRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_CALRDY, self).__init__(register,
            'CALRDY', 'CMU.IF.CALRDY', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_CALOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_CALOF, self).__init__(register,
            'CALOF', 'CMU.IF.CALOF', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_HFXODISERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_HFXODISERR, self).__init__(register,
            'HFXODISERR', 'CMU.IF.HFXODISERR', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_HFXOAUTOSW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_HFXOAUTOSW, self).__init__(register,
            'HFXOAUTOSW', 'CMU.IF.HFXOAUTOSW', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_HFXOPEAKDETERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_HFXOPEAKDETERR, self).__init__(register,
            'HFXOPEAKDETERR', 'CMU.IF.HFXOPEAKDETERR', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_HFXOPEAKDETRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_HFXOPEAKDETRDY, self).__init__(register,
            'HFXOPEAKDETRDY', 'CMU.IF.HFXOPEAKDETRDY', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_HFXOSHUNTOPTRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_HFXOSHUNTOPTRDY, self).__init__(register,
            'HFXOSHUNTOPTRDY', 'CMU.IF.HFXOSHUNTOPTRDY', 'read-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_HFRCODIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_HFRCODIS, self).__init__(register,
            'HFRCODIS', 'CMU.IF.HFRCODIS', 'read-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_LFTIMEOUTERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_LFTIMEOUTERR, self).__init__(register,
            'LFTIMEOUTERR', 'CMU.IF.LFTIMEOUTERR', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_DPLLRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_DPLLRDY, self).__init__(register,
            'DPLLRDY', 'CMU.IF.DPLLRDY', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_DPLLLOCKFAILLOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_DPLLLOCKFAILLOW, self).__init__(register,
            'DPLLLOCKFAILLOW', 'CMU.IF.DPLLLOCKFAILLOW', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_DPLLLOCKFAILHIGH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_DPLLLOCKFAILHIGH, self).__init__(register,
            'DPLLLOCKFAILHIGH', 'CMU.IF.DPLLLOCKFAILHIGH', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IF_CMUERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IF_CMUERR, self).__init__(register,
            'CMUERR', 'CMU.IF.CMUERR', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_HFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_HFRCORDY, self).__init__(register,
            'HFRCORDY', 'CMU.IFS.HFRCORDY', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_HFXORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_HFXORDY, self).__init__(register,
            'HFXORDY', 'CMU.IFS.HFXORDY', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_LFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_LFRCORDY, self).__init__(register,
            'LFRCORDY', 'CMU.IFS.LFRCORDY', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_LFXORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_LFXORDY, self).__init__(register,
            'LFXORDY', 'CMU.IFS.LFXORDY', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_AUXHFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_AUXHFRCORDY, self).__init__(register,
            'AUXHFRCORDY', 'CMU.IFS.AUXHFRCORDY', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_CALRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_CALRDY, self).__init__(register,
            'CALRDY', 'CMU.IFS.CALRDY', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_CALOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_CALOF, self).__init__(register,
            'CALOF', 'CMU.IFS.CALOF', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_HFXODISERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_HFXODISERR, self).__init__(register,
            'HFXODISERR', 'CMU.IFS.HFXODISERR', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_HFXOAUTOSW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_HFXOAUTOSW, self).__init__(register,
            'HFXOAUTOSW', 'CMU.IFS.HFXOAUTOSW', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_HFXOPEAKDETERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_HFXOPEAKDETERR, self).__init__(register,
            'HFXOPEAKDETERR', 'CMU.IFS.HFXOPEAKDETERR', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_HFXOPEAKDETRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_HFXOPEAKDETRDY, self).__init__(register,
            'HFXOPEAKDETRDY', 'CMU.IFS.HFXOPEAKDETRDY', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_HFXOSHUNTOPTRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_HFXOSHUNTOPTRDY, self).__init__(register,
            'HFXOSHUNTOPTRDY', 'CMU.IFS.HFXOSHUNTOPTRDY', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_HFRCODIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_HFRCODIS, self).__init__(register,
            'HFRCODIS', 'CMU.IFS.HFRCODIS', 'write-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_LFTIMEOUTERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_LFTIMEOUTERR, self).__init__(register,
            'LFTIMEOUTERR', 'CMU.IFS.LFTIMEOUTERR', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_DPLLRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_DPLLRDY, self).__init__(register,
            'DPLLRDY', 'CMU.IFS.DPLLRDY', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_DPLLLOCKFAILLOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_DPLLLOCKFAILLOW, self).__init__(register,
            'DPLLLOCKFAILLOW', 'CMU.IFS.DPLLLOCKFAILLOW', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_DPLLLOCKFAILHIGH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_DPLLLOCKFAILHIGH, self).__init__(register,
            'DPLLLOCKFAILHIGH', 'CMU.IFS.DPLLLOCKFAILHIGH', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFS_CMUERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFS_CMUERR, self).__init__(register,
            'CMUERR', 'CMU.IFS.CMUERR', 'write-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_HFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_HFRCORDY, self).__init__(register,
            'HFRCORDY', 'CMU.IFC.HFRCORDY', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_HFXORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_HFXORDY, self).__init__(register,
            'HFXORDY', 'CMU.IFC.HFXORDY', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_LFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_LFRCORDY, self).__init__(register,
            'LFRCORDY', 'CMU.IFC.LFRCORDY', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_LFXORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_LFXORDY, self).__init__(register,
            'LFXORDY', 'CMU.IFC.LFXORDY', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_AUXHFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_AUXHFRCORDY, self).__init__(register,
            'AUXHFRCORDY', 'CMU.IFC.AUXHFRCORDY', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_CALRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_CALRDY, self).__init__(register,
            'CALRDY', 'CMU.IFC.CALRDY', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_CALOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_CALOF, self).__init__(register,
            'CALOF', 'CMU.IFC.CALOF', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_HFXODISERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_HFXODISERR, self).__init__(register,
            'HFXODISERR', 'CMU.IFC.HFXODISERR', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_HFXOAUTOSW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_HFXOAUTOSW, self).__init__(register,
            'HFXOAUTOSW', 'CMU.IFC.HFXOAUTOSW', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_HFXOPEAKDETERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_HFXOPEAKDETERR, self).__init__(register,
            'HFXOPEAKDETERR', 'CMU.IFC.HFXOPEAKDETERR', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_HFXOPEAKDETRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_HFXOPEAKDETRDY, self).__init__(register,
            'HFXOPEAKDETRDY', 'CMU.IFC.HFXOPEAKDETRDY', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_HFXOSHUNTOPTRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_HFXOSHUNTOPTRDY, self).__init__(register,
            'HFXOSHUNTOPTRDY', 'CMU.IFC.HFXOSHUNTOPTRDY', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_HFRCODIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_HFRCODIS, self).__init__(register,
            'HFRCODIS', 'CMU.IFC.HFRCODIS', 'write-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_LFTIMEOUTERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_LFTIMEOUTERR, self).__init__(register,
            'LFTIMEOUTERR', 'CMU.IFC.LFTIMEOUTERR', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_DPLLRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_DPLLRDY, self).__init__(register,
            'DPLLRDY', 'CMU.IFC.DPLLRDY', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_DPLLLOCKFAILLOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_DPLLLOCKFAILLOW, self).__init__(register,
            'DPLLLOCKFAILLOW', 'CMU.IFC.DPLLLOCKFAILLOW', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_DPLLLOCKFAILHIGH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_DPLLLOCKFAILHIGH, self).__init__(register,
            'DPLLLOCKFAILHIGH', 'CMU.IFC.DPLLLOCKFAILHIGH', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IFC_CMUERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IFC_CMUERR, self).__init__(register,
            'CMUERR', 'CMU.IFC.CMUERR', 'write-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_HFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_HFRCORDY, self).__init__(register,
            'HFRCORDY', 'CMU.IEN.HFRCORDY', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_HFXORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_HFXORDY, self).__init__(register,
            'HFXORDY', 'CMU.IEN.HFXORDY', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_LFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_LFRCORDY, self).__init__(register,
            'LFRCORDY', 'CMU.IEN.LFRCORDY', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_LFXORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_LFXORDY, self).__init__(register,
            'LFXORDY', 'CMU.IEN.LFXORDY', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_AUXHFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_AUXHFRCORDY, self).__init__(register,
            'AUXHFRCORDY', 'CMU.IEN.AUXHFRCORDY', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_CALRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_CALRDY, self).__init__(register,
            'CALRDY', 'CMU.IEN.CALRDY', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_CALOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_CALOF, self).__init__(register,
            'CALOF', 'CMU.IEN.CALOF', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_HFXODISERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_HFXODISERR, self).__init__(register,
            'HFXODISERR', 'CMU.IEN.HFXODISERR', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_HFXOAUTOSW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_HFXOAUTOSW, self).__init__(register,
            'HFXOAUTOSW', 'CMU.IEN.HFXOAUTOSW', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_HFXOPEAKDETERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_HFXOPEAKDETERR, self).__init__(register,
            'HFXOPEAKDETERR', 'CMU.IEN.HFXOPEAKDETERR', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_HFXOPEAKDETRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_HFXOPEAKDETRDY, self).__init__(register,
            'HFXOPEAKDETRDY', 'CMU.IEN.HFXOPEAKDETRDY', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_HFXOSHUNTOPTRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_HFXOSHUNTOPTRDY, self).__init__(register,
            'HFXOSHUNTOPTRDY', 'CMU.IEN.HFXOSHUNTOPTRDY', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_HFRCODIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_HFRCODIS, self).__init__(register,
            'HFRCODIS', 'CMU.IEN.HFRCODIS', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_LFTIMEOUTERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_LFTIMEOUTERR, self).__init__(register,
            'LFTIMEOUTERR', 'CMU.IEN.LFTIMEOUTERR', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_DPLLRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_DPLLRDY, self).__init__(register,
            'DPLLRDY', 'CMU.IEN.DPLLRDY', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_DPLLLOCKFAILLOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_DPLLLOCKFAILLOW, self).__init__(register,
            'DPLLLOCKFAILLOW', 'CMU.IEN.DPLLLOCKFAILLOW', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_DPLLLOCKFAILHIGH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_DPLLLOCKFAILHIGH, self).__init__(register,
            'DPLLLOCKFAILHIGH', 'CMU.IEN.DPLLLOCKFAILHIGH', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_IEN_CMUERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_IEN_CMUERR, self).__init__(register,
            'CMUERR', 'CMU.IEN.CMUERR', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKEN0_CRYPTO0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKEN0_CRYPTO0, self).__init__(register,
            'CRYPTO0', 'CMU.HFBUSCLKEN0.CRYPTO0', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKEN0_CRYPTO1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKEN0_CRYPTO1, self).__init__(register,
            'CRYPTO1', 'CMU.HFBUSCLKEN0.CRYPTO1', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKEN0_LE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKEN0_LE, self).__init__(register,
            'LE', 'CMU.HFBUSCLKEN0.LE', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKEN0_GPIO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKEN0_GPIO, self).__init__(register,
            'GPIO', 'CMU.HFBUSCLKEN0.GPIO', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKEN0_PRS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKEN0_PRS, self).__init__(register,
            'PRS', 'CMU.HFBUSCLKEN0.PRS', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKEN0_LDMA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKEN0_LDMA, self).__init__(register,
            'LDMA', 'CMU.HFBUSCLKEN0.LDMA', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKEN0_GPCRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKEN0_GPCRC, self).__init__(register,
            'GPCRC', 'CMU.HFBUSCLKEN0.GPCRC', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_TIMER0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_TIMER0, self).__init__(register,
            'TIMER0', 'CMU.HFPERCLKEN0.TIMER0', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_TIMER1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_TIMER1, self).__init__(register,
            'TIMER1', 'CMU.HFPERCLKEN0.TIMER1', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_WTIMER0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_WTIMER0, self).__init__(register,
            'WTIMER0', 'CMU.HFPERCLKEN0.WTIMER0', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_WTIMER1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_WTIMER1, self).__init__(register,
            'WTIMER1', 'CMU.HFPERCLKEN0.WTIMER1', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_USART0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_USART0, self).__init__(register,
            'USART0', 'CMU.HFPERCLKEN0.USART0', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_USART1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_USART1, self).__init__(register,
            'USART1', 'CMU.HFPERCLKEN0.USART1', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_USART2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_USART2, self).__init__(register,
            'USART2', 'CMU.HFPERCLKEN0.USART2', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_USART3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_USART3, self).__init__(register,
            'USART3', 'CMU.HFPERCLKEN0.USART3', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_I2C0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_I2C0, self).__init__(register,
            'I2C0', 'CMU.HFPERCLKEN0.I2C0', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_I2C1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_I2C1, self).__init__(register,
            'I2C1', 'CMU.HFPERCLKEN0.I2C1', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_ACMP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_ACMP0, self).__init__(register,
            'ACMP0', 'CMU.HFPERCLKEN0.ACMP0', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_ACMP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_ACMP1, self).__init__(register,
            'ACMP1', 'CMU.HFPERCLKEN0.ACMP1', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_CRYOTIMER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_CRYOTIMER, self).__init__(register,
            'CRYOTIMER', 'CMU.HFPERCLKEN0.CRYOTIMER', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_ADC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_ADC0, self).__init__(register,
            'ADC0', 'CMU.HFPERCLKEN0.ADC0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_IDAC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_IDAC0, self).__init__(register,
            'IDAC0', 'CMU.HFPERCLKEN0.IDAC0', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_VDAC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_VDAC0, self).__init__(register,
            'VDAC0', 'CMU.HFPERCLKEN0.VDAC0', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_CSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_CSEN, self).__init__(register,
            'CSEN', 'CMU.HFPERCLKEN0.CSEN', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_TRNG0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_TRNG0, self).__init__(register,
            'TRNG0', 'CMU.HFPERCLKEN0.TRNG0', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKEN0_SYSCFG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKEN0_SYSCFG, self).__init__(register,
            'SYSCFG', 'CMU.HFPERCLKEN0.SYSCFG', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKEN0_PROTIMER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKEN0_PROTIMER, self).__init__(register,
            'PROTIMER', 'CMU.HFRADIOCLKEN0.PROTIMER', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKEN0_RFSENSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKEN0_RFSENSE, self).__init__(register,
            'RFSENSE', 'CMU.HFRADIOCLKEN0.RFSENSE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKEN0_RAC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKEN0_RAC, self).__init__(register,
            'RAC', 'CMU.HFRADIOCLKEN0.RAC', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKEN0_FRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKEN0_FRC, self).__init__(register,
            'FRC', 'CMU.HFRADIOCLKEN0.FRC', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKEN0_CRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKEN0_CRC, self).__init__(register,
            'CRC', 'CMU.HFRADIOCLKEN0.CRC', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKEN0_SYNTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKEN0_SYNTH, self).__init__(register,
            'SYNTH', 'CMU.HFRADIOCLKEN0.SYNTH', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKEN0_MODEM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKEN0_MODEM, self).__init__(register,
            'MODEM', 'CMU.HFRADIOCLKEN0.MODEM', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKEN0_AGC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKEN0_AGC, self).__init__(register,
            'AGC', 'CMU.HFRADIOCLKEN0.AGC', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOALTCLKEN0_BUFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOALTCLKEN0_BUFC, self).__init__(register,
            'BUFC', 'CMU.HFRADIOALTCLKEN0.BUFC', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFACLKEN0_LETIMER0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFACLKEN0_LETIMER0, self).__init__(register,
            'LETIMER0', 'CMU.LFACLKEN0.LETIMER0', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFACLKEN0_LESENSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFACLKEN0_LESENSE, self).__init__(register,
            'LESENSE', 'CMU.LFACLKEN0.LESENSE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFBCLKEN0_SYSTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFBCLKEN0_SYSTICK, self).__init__(register,
            'SYSTICK', 'CMU.LFBCLKEN0.SYSTICK', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFBCLKEN0_LEUART0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFBCLKEN0_LEUART0, self).__init__(register,
            'LEUART0', 'CMU.LFBCLKEN0.LEUART0', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFBCLKEN0_CSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFBCLKEN0_CSEN, self).__init__(register,
            'CSEN', 'CMU.LFBCLKEN0.CSEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFECLKEN0_RTCC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFECLKEN0_RTCC, self).__init__(register,
            'RTCC', 'CMU.LFECLKEN0.RTCC', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPRESC_PRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPRESC_PRESC, self).__init__(register,
            'PRESC', 'CMU.HFPRESC.PRESC', 'read-write',
            "",
            8, 5,
            RM_Enum_CMU_HFPRESC_PRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPRESC_HFCLKLEPRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPRESC_HFCLKLEPRESC, self).__init__(register,
            'HFCLKLEPRESC', 'CMU.HFPRESC.HFCLKLEPRESC', 'read-write',
            "",
            24, 1,
            RM_Enum_CMU_HFPRESC_HFCLKLEPRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFCOREPRESC_PRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFCOREPRESC_PRESC, self).__init__(register,
            'PRESC', 'CMU.HFCOREPRESC.PRESC', 'read-write',
            "",
            8, 9,
            RM_Enum_CMU_HFCOREPRESC_PRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERPRESC_PRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERPRESC_PRESC, self).__init__(register,
            'PRESC', 'CMU.HFPERPRESC.PRESC', 'read-write',
            "",
            8, 9,
            RM_Enum_CMU_HFPERPRESC_PRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOPRESC_PRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOPRESC_PRESC, self).__init__(register,
            'PRESC', 'CMU.HFRADIOPRESC.PRESC', 'read-write',
            "",
            8, 9,
            RM_Enum_CMU_HFRADIOPRESC_PRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFEXPPRESC_PRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFEXPPRESC_PRESC, self).__init__(register,
            'PRESC', 'CMU.HFEXPPRESC.PRESC', 'read-write',
            "",
            8, 5,
            RM_Enum_CMU_HFEXPPRESC_PRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFAPRESC0_LETIMER0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFAPRESC0_LETIMER0, self).__init__(register,
            'LETIMER0', 'CMU.LFAPRESC0.LETIMER0', 'read-write',
            "",
            0, 4,
            RM_Enum_CMU_LFAPRESC0_LETIMER0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFAPRESC0_LESENSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFAPRESC0_LESENSE, self).__init__(register,
            'LESENSE', 'CMU.LFAPRESC0.LESENSE', 'read-write',
            "",
            4, 2,
            RM_Enum_CMU_LFAPRESC0_LESENSE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFBPRESC0_SYSTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFBPRESC0_SYSTICK, self).__init__(register,
            'SYSTICK', 'CMU.LFBPRESC0.SYSTICK', 'read-only',
            "",
            0, 4,
            RM_Enum_CMU_LFBPRESC0_SYSTICK(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFBPRESC0_LEUART0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFBPRESC0_LEUART0, self).__init__(register,
            'LEUART0', 'CMU.LFBPRESC0.LEUART0', 'read-write',
            "",
            4, 2,
            RM_Enum_CMU_LFBPRESC0_LEUART0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFBPRESC0_CSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFBPRESC0_CSEN, self).__init__(register,
            'CSEN', 'CMU.LFBPRESC0.CSEN', 'read-write',
            "",
            8, 2,
            RM_Enum_CMU_LFBPRESC0_CSEN(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFEPRESC0_RTCC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFEPRESC0_RTCC, self).__init__(register,
            'RTCC', 'CMU.LFEPRESC0.RTCC', 'read-write',
            "",
            0, 2,
            RM_Enum_CMU_LFEPRESC0_RTCC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOALTPRESC_PRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOALTPRESC_PRESC, self).__init__(register,
            'PRESC', 'CMU.HFRADIOALTPRESC.PRESC', 'read-write',
            "",
            8, 9,
            RM_Enum_CMU_HFRADIOALTPRESC_PRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_SYNCBUSY_LFACLKEN0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_SYNCBUSY_LFACLKEN0, self).__init__(register,
            'LFACLKEN0', 'CMU.SYNCBUSY.LFACLKEN0', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_SYNCBUSY_LFAPRESC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_SYNCBUSY_LFAPRESC0, self).__init__(register,
            'LFAPRESC0', 'CMU.SYNCBUSY.LFAPRESC0', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_SYNCBUSY_LFBCLKEN0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_SYNCBUSY_LFBCLKEN0, self).__init__(register,
            'LFBCLKEN0', 'CMU.SYNCBUSY.LFBCLKEN0', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_SYNCBUSY_LFBPRESC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_SYNCBUSY_LFBPRESC0, self).__init__(register,
            'LFBPRESC0', 'CMU.SYNCBUSY.LFBPRESC0', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_SYNCBUSY_LFECLKEN0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_SYNCBUSY_LFECLKEN0, self).__init__(register,
            'LFECLKEN0', 'CMU.SYNCBUSY.LFECLKEN0', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_SYNCBUSY_LFEPRESC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_SYNCBUSY_LFEPRESC0, self).__init__(register,
            'LFEPRESC0', 'CMU.SYNCBUSY.LFEPRESC0', 'read-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_SYNCBUSY_HFRCOBSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_SYNCBUSY_HFRCOBSY, self).__init__(register,
            'HFRCOBSY', 'CMU.SYNCBUSY.HFRCOBSY', 'read-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_SYNCBUSY_AUXHFRCOBSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_SYNCBUSY_AUXHFRCOBSY, self).__init__(register,
            'AUXHFRCOBSY', 'CMU.SYNCBUSY.AUXHFRCOBSY', 'read-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_SYNCBUSY_LFRCOBSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_SYNCBUSY_LFRCOBSY, self).__init__(register,
            'LFRCOBSY', 'CMU.SYNCBUSY.LFRCOBSY', 'read-only',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_SYNCBUSY_LFRCOVREFBSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_SYNCBUSY_LFRCOVREFBSY, self).__init__(register,
            'LFRCOVREFBSY', 'CMU.SYNCBUSY.LFRCOVREFBSY', 'read-only',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_SYNCBUSY_HFXOBSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_SYNCBUSY_HFXOBSY, self).__init__(register,
            'HFXOBSY', 'CMU.SYNCBUSY.HFXOBSY', 'read-only',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_SYNCBUSY_LFXOBSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_SYNCBUSY_LFXOBSY, self).__init__(register,
            'LFXOBSY', 'CMU.SYNCBUSY.LFXOBSY', 'read-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_FREEZE_REGFREEZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_FREEZE_REGFREEZE, self).__init__(register,
            'REGFREEZE', 'CMU.FREEZE.REGFREEZE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_PCNTCTRL_PCNT0CLKEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_PCNTCTRL_PCNT0CLKEN, self).__init__(register,
            'PCNT0CLKEN', 'CMU.PCNTCTRL.PCNT0CLKEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_PCNTCTRL_PCNT0CLKSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_PCNTCTRL_PCNT0CLKSEL, self).__init__(register,
            'PCNT0CLKSEL', 'CMU.PCNTCTRL.PCNT0CLKSEL', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_PCNTCTRL_PCNT1CLKEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_PCNTCTRL_PCNT1CLKEN, self).__init__(register,
            'PCNT1CLKEN', 'CMU.PCNTCTRL.PCNT1CLKEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_PCNTCTRL_PCNT1CLKSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_PCNTCTRL_PCNT1CLKSEL, self).__init__(register,
            'PCNT1CLKSEL', 'CMU.PCNTCTRL.PCNT1CLKSEL', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_PCNTCTRL_PCNT2CLKEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_PCNTCTRL_PCNT2CLKEN, self).__init__(register,
            'PCNT2CLKEN', 'CMU.PCNTCTRL.PCNT2CLKEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_PCNTCTRL_PCNT2CLKSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_PCNTCTRL_PCNT2CLKSEL, self).__init__(register,
            'PCNT2CLKSEL', 'CMU.PCNTCTRL.PCNT2CLKSEL', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LVDSCTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LVDSCTRL_EN, self).__init__(register,
            'EN', 'CMU.LVDSCTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LVDSCTRL_CLKSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LVDSCTRL_CLKSEL, self).__init__(register,
            'CLKSEL', 'CMU.LVDSCTRL.CLKSEL', 'read-write',
            "",
            1, 2,
            RM_Enum_CMU_LVDSCTRL_CLKSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_ADCCTRL_ADC0CLKSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_ADCCTRL_ADC0CLKSEL, self).__init__(register,
            'ADC0CLKSEL', 'CMU.ADCCTRL.ADC0CLKSEL', 'read-write',
            "",
            4, 2,
            RM_Enum_CMU_ADCCTRL_ADC0CLKSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_ADCCTRL_ADC0CLKINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_ADCCTRL_ADC0CLKINV, self).__init__(register,
            'ADC0CLKINV', 'CMU.ADCCTRL.ADC0CLKINV', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_ROUTEPEN_CLKOUT0PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_ROUTEPEN_CLKOUT0PEN, self).__init__(register,
            'CLKOUT0PEN', 'CMU.ROUTEPEN.CLKOUT0PEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_ROUTEPEN_CLKOUT1PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_ROUTEPEN_CLKOUT1PEN, self).__init__(register,
            'CLKOUT1PEN', 'CMU.ROUTEPEN.CLKOUT1PEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_ROUTEPEN_CLKIN0PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_ROUTEPEN_CLKIN0PEN, self).__init__(register,
            'CLKIN0PEN', 'CMU.ROUTEPEN.CLKIN0PEN', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_ROUTELOC0_CLKOUT0LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_ROUTELOC0_CLKOUT0LOC, self).__init__(register,
            'CLKOUT0LOC', 'CMU.ROUTELOC0.CLKOUT0LOC', 'read-write',
            "",
            0, 6,
            RM_Enum_CMU_ROUTELOC0_CLKOUT0LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_ROUTELOC0_CLKOUT1LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_ROUTELOC0_CLKOUT1LOC, self).__init__(register,
            'CLKOUT1LOC', 'CMU.ROUTELOC0.CLKOUT1LOC', 'read-write',
            "",
            8, 6,
            RM_Enum_CMU_ROUTELOC0_CLKOUT1LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_ROUTELOC1_CLKIN0LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_ROUTELOC1_CLKIN0LOC, self).__init__(register,
            'CLKIN0LOC', 'CMU.ROUTELOC1.CLKIN0LOC', 'read-write',
            "",
            0, 6,
            RM_Enum_CMU_ROUTELOC1_CLKIN0LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LOCK_LOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LOCK_LOCKKEY, self).__init__(register,
            'LOCKKEY', 'CMU.LOCK.LOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_CMU_LOCK_LOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LOCK_LFOSCUNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LOCK_LFOSCUNLOCK, self).__init__(register,
            'LFOSCUNLOCK', 'CMU.LOCK.LFOSCUNLOCK', 'write-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRCOSS_SSAMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRCOSS_SSAMP, self).__init__(register,
            'SSAMP', 'CMU.HFRCOSS.SSAMP', 'read-write',
            "",
            0, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRCOSS_SSINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRCOSS_SSINV, self).__init__(register,
            'SSINV', 'CMU.HFRCOSS.SSINV', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_SYNTHLODIVFREQCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_SYNTHLODIVFREQCTRL, self).__init__(register,
            'SYNTHLODIVFREQCTRL', 'CMU.RFLOCK0.SYNTHLODIVFREQCTRL', 'read-write',
            "",
            0, 9,
            RM_Enum_CMU_RFLOCK0_SYNTHLODIVFREQCTRL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_RACIFLILTENABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_RACIFLILTENABLE, self).__init__(register,
            'RACIFLILTENABLE', 'CMU.RFLOCK0.RACIFLILTENABLE', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_RACAUXPLL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_RACAUXPLL, self).__init__(register,
            'RACAUXPLL', 'CMU.RFLOCK0.RACAUXPLL', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_MODEMDEC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_MODEMDEC1, self).__init__(register,
            'MODEMDEC1', 'CMU.RFLOCK0.MODEMDEC1', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_MODEMANTDIVMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_MODEMANTDIVMODE, self).__init__(register,
            'MODEMANTDIVMODE', 'CMU.RFLOCK0.MODEMANTDIVMODE', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_RACIFPGAENPGA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_RACIFPGAENPGA, self).__init__(register,
            'RACIFPGAENPGA', 'CMU.RFLOCK0.RACIFPGAENPGA', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_RACPASLICE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_RACPASLICE, self).__init__(register,
            'RACPASLICE', 'CMU.RFLOCK0.RACPASLICE', 'read-write',
            "",
            14, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_RACSGPAEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_RACSGPAEN, self).__init__(register,
            'RACSGPAEN', 'CMU.RFLOCK0.RACSGPAEN', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_RACPAEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_RACPAEN, self).__init__(register,
            'RACPAEN', 'CMU.RFLOCK0.RACPAEN', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_RACPAEN0DBM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_RACPAEN0DBM, self).__init__(register,
            'RACPAEN0DBM', 'CMU.RFLOCK0.RACPAEN0DBM', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_FRCCONVMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_FRCCONVMODE, self).__init__(register,
            'FRCCONVMODE', 'CMU.RFLOCK0.FRCCONVMODE', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_FRCPAUSING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_FRCPAUSING, self).__init__(register,
            'FRCPAUSING', 'CMU.RFLOCK0.FRCPAUSING', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_MODEMDSSS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_MODEMDSSS, self).__init__(register,
            'MODEMDSSS', 'CMU.RFLOCK0.MODEMDSSS', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_MODEMMODFORMAT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_MODEMMODFORMAT, self).__init__(register,
            'MODEMMODFORMAT', 'CMU.RFLOCK0.MODEMMODFORMAT', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_MODEMDUALSYNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_MODEMDUALSYNC, self).__init__(register,
            'MODEMDUALSYNC', 'CMU.RFLOCK0.MODEMDUALSYNC', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_RFLOCK0_UNLOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_RFLOCK0_UNLOCKED, self).__init__(register,
            'UNLOCKED', 'CMU.RFLOCK0.UNLOCKED', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_CRYPTO0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_CRYPTO0, self).__init__(register,
            'CRYPTO0', 'CMU.HFBUSCLKENMASK0.CRYPTO0', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_CRYPTO1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_CRYPTO1, self).__init__(register,
            'CRYPTO1', 'CMU.HFBUSCLKENMASK0.CRYPTO1', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_LE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_LE, self).__init__(register,
            'LE', 'CMU.HFBUSCLKENMASK0.LE', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_GPIO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_GPIO, self).__init__(register,
            'GPIO', 'CMU.HFBUSCLKENMASK0.GPIO', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_PRS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_PRS, self).__init__(register,
            'PRS', 'CMU.HFBUSCLKENMASK0.PRS', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_LDMA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_LDMA, self).__init__(register,
            'LDMA', 'CMU.HFBUSCLKENMASK0.LDMA', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_GPCRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_GPCRC, self).__init__(register,
            'GPCRC', 'CMU.HFBUSCLKENMASK0.GPCRC', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_DMEM0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_DMEM0, self).__init__(register,
            'DMEM0', 'CMU.HFBUSCLKENMASK0.DMEM0', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_DMEM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_DMEM1, self).__init__(register,
            'DMEM1', 'CMU.HFBUSCLKENMASK0.DMEM1', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_DMEM2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_DMEM2, self).__init__(register,
            'DMEM2', 'CMU.HFBUSCLKENMASK0.DMEM2', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_BUSMATRIX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_BUSMATRIX, self).__init__(register,
            'BUSMATRIX', 'CMU.HFBUSCLKENMASK0.BUSMATRIX', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_DMEMSEQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_DMEMSEQ, self).__init__(register,
            'DMEMSEQ', 'CMU.HFBUSCLKENMASK0.DMEMSEQ', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_AHB2APB0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_AHB2APB0, self).__init__(register,
            'AHB2APB0', 'CMU.HFBUSCLKENMASK0.AHB2APB0', 'read-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_CMCTRL_RSYNC_COMB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_CMCTRL_RSYNC_COMB, self).__init__(register,
            'CMCTRL_RSYNC_COMB', 'CMU.HFBUSCLKENMASK0.CMCTRL_RSYNC_COMB', 'read-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_MSC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_MSC, self).__init__(register,
            'MSC', 'CMU.HFBUSCLKENMASK0.MSC', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_IMEM_FAST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_IMEM_FAST, self).__init__(register,
            'IMEM_FAST', 'CMU.HFBUSCLKENMASK0.IMEM_FAST', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFBUSCLKENMASK0_SMU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFBUSCLKENMASK0_SMU, self).__init__(register,
            'SMU', 'CMU.HFBUSCLKENMASK0.SMU', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFCORECLKENMASK0_CM4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFCORECLKENMASK0_CM4, self).__init__(register,
            'CM4', 'CMU.HFCORECLKENMASK0.CM4', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFCORECLKENMASK0_CM3_FREE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFCORECLKENMASK0_CM3_FREE, self).__init__(register,
            'CM3_FREE', 'CMU.HFCORECLKENMASK0.CM3_FREE', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFCORECLKENMASK0_CM3_FAST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFCORECLKENMASK0_CM3_FAST, self).__init__(register,
            'CM3_FAST', 'CMU.HFCORECLKENMASK0.CM3_FAST', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_TIMER0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_TIMER0, self).__init__(register,
            'TIMER0', 'CMU.HFPERCLKENMASK0.TIMER0', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_TIMER1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_TIMER1, self).__init__(register,
            'TIMER1', 'CMU.HFPERCLKENMASK0.TIMER1', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_WTIMER0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_WTIMER0, self).__init__(register,
            'WTIMER0', 'CMU.HFPERCLKENMASK0.WTIMER0', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_WTIMER1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_WTIMER1, self).__init__(register,
            'WTIMER1', 'CMU.HFPERCLKENMASK0.WTIMER1', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_USART0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_USART0, self).__init__(register,
            'USART0', 'CMU.HFPERCLKENMASK0.USART0', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_USART1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_USART1, self).__init__(register,
            'USART1', 'CMU.HFPERCLKENMASK0.USART1', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_USART2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_USART2, self).__init__(register,
            'USART2', 'CMU.HFPERCLKENMASK0.USART2', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_USART3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_USART3, self).__init__(register,
            'USART3', 'CMU.HFPERCLKENMASK0.USART3', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_I2C0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_I2C0, self).__init__(register,
            'I2C0', 'CMU.HFPERCLKENMASK0.I2C0', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_I2C1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_I2C1, self).__init__(register,
            'I2C1', 'CMU.HFPERCLKENMASK0.I2C1', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_ACMP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_ACMP0, self).__init__(register,
            'ACMP0', 'CMU.HFPERCLKENMASK0.ACMP0', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_ACMP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_ACMP1, self).__init__(register,
            'ACMP1', 'CMU.HFPERCLKENMASK0.ACMP1', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_CRYOTIMER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_CRYOTIMER, self).__init__(register,
            'CRYOTIMER', 'CMU.HFPERCLKENMASK0.CRYOTIMER', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_ADC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_ADC0, self).__init__(register,
            'ADC0', 'CMU.HFPERCLKENMASK0.ADC0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_IDAC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_IDAC0, self).__init__(register,
            'IDAC0', 'CMU.HFPERCLKENMASK0.IDAC0', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_VDAC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_VDAC0, self).__init__(register,
            'VDAC0', 'CMU.HFPERCLKENMASK0.VDAC0', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_CSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_CSEN, self).__init__(register,
            'CSEN', 'CMU.HFPERCLKENMASK0.CSEN', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_TRNG0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_TRNG0, self).__init__(register,
            'TRNG0', 'CMU.HFPERCLKENMASK0.TRNG0', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_SYSCFG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_SYSCFG, self).__init__(register,
            'SYSCFG', 'CMU.HFPERCLKENMASK0.SYSCFG', 'read-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_APB_RSYNC_COMB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_APB_RSYNC_COMB, self).__init__(register,
            'APB_RSYNC_COMB', 'CMU.HFPERCLKENMASK0.APB_RSYNC_COMB', 'read-only',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_EMU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_EMU, self).__init__(register,
            'EMU', 'CMU.HFPERCLKENMASK0.EMU', 'read-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_RMU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_RMU, self).__init__(register,
            'RMU', 'CMU.HFPERCLKENMASK0.RMU', 'read-only',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_CMU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_CMU, self).__init__(register,
            'CMU', 'CMU.HFPERCLKENMASK0.CMU', 'read-only',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFPERCLKENMASK0_APORT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFPERCLKENMASK0_APORT, self).__init__(register,
            'APORT', 'CMU.HFPERCLKENMASK0.APORT', 'read-only',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKENMASK0_PROTIMER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKENMASK0_PROTIMER, self).__init__(register,
            'PROTIMER', 'CMU.HFRADIOCLKENMASK0.PROTIMER', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKENMASK0_RFSENSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKENMASK0_RFSENSE, self).__init__(register,
            'RFSENSE', 'CMU.HFRADIOCLKENMASK0.RFSENSE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKENMASK0_RAC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKENMASK0_RAC, self).__init__(register,
            'RAC', 'CMU.HFRADIOCLKENMASK0.RAC', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKENMASK0_FRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKENMASK0_FRC, self).__init__(register,
            'FRC', 'CMU.HFRADIOCLKENMASK0.FRC', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKENMASK0_CRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKENMASK0_CRC, self).__init__(register,
            'CRC', 'CMU.HFRADIOCLKENMASK0.CRC', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKENMASK0_SYNTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKENMASK0_SYNTH, self).__init__(register,
            'SYNTH', 'CMU.HFRADIOCLKENMASK0.SYNTH', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKENMASK0_MODEM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKENMASK0_MODEM, self).__init__(register,
            'MODEM', 'CMU.HFRADIOCLKENMASK0.MODEM', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOCLKENMASK0_AGC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOCLKENMASK0_AGC, self).__init__(register,
            'AGC', 'CMU.HFRADIOCLKENMASK0.AGC', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFRADIOALTCLKENMASK0_BUFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFRADIOALTCLKENMASK0_BUFC, self).__init__(register,
            'BUFC', 'CMU.HFRADIOALTCLKENMASK0.BUFC', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFUNDIVCLKENMASK0_SYNTH_HFXO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFUNDIVCLKENMASK0_SYNTH_HFXO, self).__init__(register,
            'SYNTH_HFXO', 'CMU.HFUNDIVCLKENMASK0.SYNTH_HFXO', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFUNDIVCLKENMASK0_DEMOD_HFXO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFUNDIVCLKENMASK0_DEMOD_HFXO, self).__init__(register,
            'DEMOD_HFXO', 'CMU.HFUNDIVCLKENMASK0.DEMOD_HFXO', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_HFUNDIVCLKENMASK0_AGC_HFXO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_HFUNDIVCLKENMASK0_AGC_HFXO, self).__init__(register,
            'AGC_HFXO', 'CMU.HFUNDIVCLKENMASK0.AGC_HFXO', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFACLKENMASK0_LETIMER0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFACLKENMASK0_LETIMER0, self).__init__(register,
            'LETIMER0', 'CMU.LFACLKENMASK0.LETIMER0', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFACLKENMASK0_LESENSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFACLKENMASK0_LESENSE, self).__init__(register,
            'LESENSE', 'CMU.LFACLKENMASK0.LESENSE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFBCLKENMASK0_SYSTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFBCLKENMASK0_SYSTICK, self).__init__(register,
            'SYSTICK', 'CMU.LFBCLKENMASK0.SYSTICK', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFBCLKENMASK0_LEUART0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFBCLKENMASK0_LEUART0, self).__init__(register,
            'LEUART0', 'CMU.LFBCLKENMASK0.LEUART0', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFBCLKENMASK0_CSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFBCLKENMASK0_CSEN, self).__init__(register,
            'CSEN', 'CMU.LFBCLKENMASK0.CSEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_LFECLKENMASK0_RTCC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_LFECLKENMASK0_RTCC, self).__init__(register,
            'RTCC', 'CMU.LFECLKENMASK0.RTCC', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_PCNTCLKENMASK_PCNT0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_PCNTCLKENMASK_PCNT0, self).__init__(register,
            'PCNT0', 'CMU.PCNTCLKENMASK.PCNT0', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_PCNTCLKENMASK_PCNT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_PCNTCLKENMASK_PCNT1, self).__init__(register,
            'PCNT1', 'CMU.PCNTCLKENMASK.PCNT1', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_PCNTCLKENMASK_PCNT2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_PCNTCLKENMASK_PCNT2, self).__init__(register,
            'PCNT2', 'CMU.PCNTCLKENMASK.PCNT2', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TEST_EMUOSCLV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TEST_EMUOSCLV, self).__init__(register,
            'EMUOSCLV', 'CMU.TEST.EMUOSCLV', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TEST_CLKOUTHIDDENSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TEST_CLKOUTHIDDENSEL, self).__init__(register,
            'CLKOUTHIDDENSEL', 'CMU.TEST.CLKOUTHIDDENSEL', 'read-write',
            "",
            8, 4,
            RM_Enum_CMU_TEST_CLKOUTHIDDENSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TEST_OSCCTRLSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TEST_OSCCTRLSEL, self).__init__(register,
            'OSCCTRLSEL', 'CMU.TEST.OSCCTRLSEL', 'read-write',
            "",
            12, 4,
            RM_Enum_CMU_TEST_OSCCTRLSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TEST_LEWSYNCPRS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TEST_LEWSYNCPRS, self).__init__(register,
            'LEWSYNCPRS', 'CMU.TEST.LEWSYNCPRS', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TEST_LEWSYNCBLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TEST_LEWSYNCBLOCK, self).__init__(register,
            'LEWSYNCBLOCK', 'CMU.TEST.LEWSYNCBLOCK', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TEST_LEWSYNCOBS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TEST_LEWSYNCOBS, self).__init__(register,
            'LEWSYNCOBS', 'CMU.TEST.LEWSYNCOBS', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TEST_LEWSYNCOBSINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TEST_LEWSYNCOBSINV, self).__init__(register,
            'LEWSYNCOBSINV', 'CMU.TEST.LEWSYNCOBSINV', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFRCOCTRL_CMPBIASSWDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFRCOCTRL_CMPBIASSWDIS, self).__init__(register,
            'CMPBIASSWDIS', 'CMU.TESTHFRCOCTRL.CMPBIASSWDIS', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFRCOCTRL_SPREADCAL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFRCOCTRL_SPREADCAL, self).__init__(register,
            'SPREADCAL', 'CMU.TESTHFRCOCTRL.SPREADCAL', 'read-write',
            "",
            4, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTAUXHFRCOCTRL_CMPBIASSWDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTAUXHFRCOCTRL_CMPBIASSWDIS, self).__init__(register,
            'CMPBIASSWDIS', 'CMU.TESTAUXHFRCOCTRL.CMPBIASSWDIS', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTAUXHFRCOCTRL_SPREADCAL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTAUXHFRCOCTRL_SPREADCAL, self).__init__(register,
            'SPREADCAL', 'CMU.TESTAUXHFRCOCTRL.SPREADCAL', 'read-write',
            "",
            4, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTLFRCOCTRL_DISOSC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTLFRCOCTRL_DISOSC, self).__init__(register,
            'DISOSC', 'CMU.TESTLFRCOCTRL.DISOSC', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTLFRCOCTRL_DISSYNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTLFRCOCTRL_DISSYNC, self).__init__(register,
            'DISSYNC', 'CMU.TESTLFRCOCTRL.DISSYNC', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTLFRCOCTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTLFRCOCTRL_MODE, self).__init__(register,
            'MODE', 'CMU.TESTLFRCOCTRL.MODE', 'read-write',
            "",
            4, 2,
            RM_Enum_CMU_TESTLFRCOCTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTLFRCOCTRL_SELCLKDIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTLFRCOCTRL_SELCLKDIV, self).__init__(register,
            'SELCLKDIV', 'CMU.TESTLFRCOCTRL.SELCLKDIV', 'read-write',
            "",
            6, 2,
            RM_Enum_CMU_TESTLFRCOCTRL_SELCLKDIV(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTLFRCOCTRL_VREFPRECH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTLFRCOCTRL_VREFPRECH, self).__init__(register,
            'VREFPRECH', 'CMU.TESTLFRCOCTRL.VREFPRECH', 'read-write',
            "",
            10, 2,
            RM_Enum_CMU_TESTLFRCOCTRL_VREFPRECH(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTLFRCOCTRL_FLIPCHOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTLFRCOCTRL_FLIPCHOP, self).__init__(register,
            'FLIPCHOP', 'CMU.TESTLFRCOCTRL.FLIPCHOP', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTLFRCOCTRL_DEMCLKSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTLFRCOCTRL_DEMCLKSEL, self).__init__(register,
            'DEMCLKSEL', 'CMU.TESTLFRCOCTRL.DEMCLKSEL', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTLFRCOCTRL_WELLBUFDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTLFRCOCTRL_WELLBUFDIS, self).__init__(register,
            'WELLBUFDIS', 'CMU.TESTLFRCOCTRL.WELLBUFDIS', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTLFRCOCTRL_FORCECOMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTLFRCOCTRL_FORCECOMP, self).__init__(register,
            'FORCECOMP', 'CMU.TESTLFRCOCTRL.FORCECOMP', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTLFRCOCTRL_BLOCKIREF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTLFRCOCTRL_BLOCKIREF, self).__init__(register,
            'BLOCKIREF', 'CMU.TESTLFRCOCTRL.BLOCKIREF', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTLFRCOCTRL_RNSHUNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTLFRCOCTRL_RNSHUNT, self).__init__(register,
            'RNSHUNT', 'CMU.TESTLFRCOCTRL.RNSHUNT', 'read-write',
            "",
            20, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTLFRCOCTRL_RPSHUNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTLFRCOCTRL_RPSHUNT, self).__init__(register,
            'RPSHUNT', 'CMU.TESTLFRCOCTRL.RPSHUNT', 'read-write',
            "",
            24, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFXOCTRL_OVERRIDE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFXOCTRL_OVERRIDE, self).__init__(register,
            'OVERRIDE', 'CMU.TESTHFXOCTRL.OVERRIDE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFXOCTRL_BIASEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFXOCTRL_BIASEN, self).__init__(register,
            'BIASEN', 'CMU.TESTHFXOCTRL.BIASEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFXOCTRL_CLKDIGEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFXOCTRL_CLKDIGEN, self).__init__(register,
            'CLKDIGEN', 'CMU.TESTHFXOCTRL.CLKDIGEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFXOCTRL_CLKAUXPLLEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFXOCTRL_CLKAUXPLLEN, self).__init__(register,
            'CLKAUXPLLEN', 'CMU.TESTHFXOCTRL.CLKAUXPLLEN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFXOCTRL_CLKIFADCEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFXOCTRL_CLKIFADCEN, self).__init__(register,
            'CLKIFADCEN', 'CMU.TESTHFXOCTRL.CLKIFADCEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFXOCTRL_CLKSYEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFXOCTRL_CLKSYEN, self).__init__(register,
            'CLKSYEN', 'CMU.TESTHFXOCTRL.CLKSYEN', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFXOCTRL_COREEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFXOCTRL_COREEN, self).__init__(register,
            'COREEN', 'CMU.TESTHFXOCTRL.COREEN', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFXOCTRL_REGEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFXOCTRL_REGEN, self).__init__(register,
            'REGEN', 'CMU.TESTHFXOCTRL.REGEN', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFXOCTRL_DOXTALKICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFXOCTRL_DOXTALKICK, self).__init__(register,
            'DOXTALKICK', 'CMU.TESTHFXOCTRL.DOXTALKICK', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFXOCTRL_CLKDIGINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFXOCTRL_CLKDIGINV, self).__init__(register,
            'CLKDIGINV', 'CMU.TESTHFXOCTRL.CLKDIGINV', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFXOCTRL_CLKAUXPLLINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFXOCTRL_CLKAUXPLLINV, self).__init__(register,
            'CLKAUXPLLINV', 'CMU.TESTHFXOCTRL.CLKAUXPLLINV', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFXOCTRL_CLKIFADCINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFXOCTRL_CLKIFADCINV, self).__init__(register,
            'CLKIFADCINV', 'CMU.TESTHFXOCTRL.CLKIFADCINV', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFXOCTRL_CLKSYINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFXOCTRL_CLKSYINV, self).__init__(register,
            'CLKSYINV', 'CMU.TESTHFXOCTRL.CLKSYINV', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTHFXOCTRL_CLKDRIVERSDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTHFXOCTRL_CLKDRIVERSDIS, self).__init__(register,
            'CLKDRIVERSDIS', 'CMU.TESTHFXOCTRL.CLKDRIVERSDIS', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_TESTLFXOCTRL_LFXOBLEEDER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_TESTLFXOCTRL_LFXOBLEEDER, self).__init__(register,
            'LFXOBLEEDER', 'CMU.TESTLFXOCTRL.LFXOBLEEDER', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_DPLLOFFSET_UPDATEEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_DPLLOFFSET_UPDATEEN, self).__init__(register,
            'UPDATEEN', 'CMU.DPLLOFFSET.UPDATEEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_DPLLOFFSET_K0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_DPLLOFFSET_K0, self).__init__(register,
            'K0', 'CMU.DPLLOFFSET.K0', 'read-write',
            "",
            5, 11)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_DPLLOFFSET_COARSECOUNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_DPLLOFFSET_COARSECOUNT, self).__init__(register,
            'COARSECOUNT', 'CMU.DPLLOFFSET.COARSECOUNT', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CMU_DPLLOFFSET_MINCOARSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CMU_DPLLOFFSET_MINCOARSE, self).__init__(register,
            'MINCOARSE', 'CMU.DPLLOFFSET.MINCOARSE', 'read-write',
            "",
            20, 7)
        self.__dict__['zz_frozen'] = True


