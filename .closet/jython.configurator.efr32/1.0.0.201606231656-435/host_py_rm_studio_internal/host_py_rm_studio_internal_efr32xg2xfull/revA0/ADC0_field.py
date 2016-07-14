
from static import Base_RM_Field
from ADC0_enum import *


class RM_Field_ADC0_CTRL_WARMUPMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CTRL_WARMUPMODE, self).__init__(register,
            'WARMUPMODE', 'ADC0.CTRL.WARMUPMODE', 'read-write',
            "",
            0, 2,
            RM_Enum_ADC0_CTRL_WARMUPMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CTRL_SINGLEDMAWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CTRL_SINGLEDMAWU, self).__init__(register,
            'SINGLEDMAWU', 'ADC0.CTRL.SINGLEDMAWU', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CTRL_SCANDMAWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CTRL_SCANDMAWU, self).__init__(register,
            'SCANDMAWU', 'ADC0.CTRL.SCANDMAWU', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CTRL_TAILGATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CTRL_TAILGATE, self).__init__(register,
            'TAILGATE', 'ADC0.CTRL.TAILGATE', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CTRL_ASYNCCLKEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CTRL_ASYNCCLKEN, self).__init__(register,
            'ASYNCCLKEN', 'ADC0.CTRL.ASYNCCLKEN', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CTRL_ADCCLKMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CTRL_ADCCLKMODE, self).__init__(register,
            'ADCCLKMODE', 'ADC0.CTRL.ADCCLKMODE', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CTRL_PRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CTRL_PRESC, self).__init__(register,
            'PRESC', 'ADC0.CTRL.PRESC', 'read-write',
            "",
            8, 7,
            RM_Enum_ADC0_CTRL_PRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CTRL_TIMEBASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CTRL_TIMEBASE, self).__init__(register,
            'TIMEBASE', 'ADC0.CTRL.TIMEBASE', 'read-write',
            "",
            16, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CTRL_OVSRSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CTRL_OVSRSEL, self).__init__(register,
            'OVSRSEL', 'ADC0.CTRL.OVSRSEL', 'read-write',
            "",
            24, 4,
            RM_Enum_ADC0_CTRL_OVSRSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CTRL_DBGHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CTRL_DBGHALT, self).__init__(register,
            'DBGHALT', 'ADC0.CTRL.DBGHALT', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CTRL_CHCONMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CTRL_CHCONMODE, self).__init__(register,
            'CHCONMODE', 'ADC0.CTRL.CHCONMODE', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CTRL_CHCONREFWARMIDLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CTRL_CHCONREFWARMIDLE, self).__init__(register,
            'CHCONREFWARMIDLE', 'ADC0.CTRL.CHCONREFWARMIDLE', 'read-write',
            "",
            30, 2,
            RM_Enum_ADC0_CTRL_CHCONREFWARMIDLE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CMD_SINGLESTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CMD_SINGLESTART, self).__init__(register,
            'SINGLESTART', 'ADC0.CMD.SINGLESTART', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CMD_SINGLESTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CMD_SINGLESTOP, self).__init__(register,
            'SINGLESTOP', 'ADC0.CMD.SINGLESTOP', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CMD_SCANSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CMD_SCANSTART, self).__init__(register,
            'SCANSTART', 'ADC0.CMD.SCANSTART', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CMD_SCANSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CMD_SCANSTOP, self).__init__(register,
            'SCANSTOP', 'ADC0.CMD.SCANSTOP', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_STATUS_SINGLEACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_STATUS_SINGLEACT, self).__init__(register,
            'SINGLEACT', 'ADC0.STATUS.SINGLEACT', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_STATUS_SCANACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_STATUS_SCANACT, self).__init__(register,
            'SCANACT', 'ADC0.STATUS.SCANACT', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_STATUS_SCANPENDING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_STATUS_SCANPENDING, self).__init__(register,
            'SCANPENDING', 'ADC0.STATUS.SCANPENDING', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_STATUS_SINGLEREFWARM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_STATUS_SINGLEREFWARM, self).__init__(register,
            'SINGLEREFWARM', 'ADC0.STATUS.SINGLEREFWARM', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_STATUS_SCANREFWARM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_STATUS_SCANREFWARM, self).__init__(register,
            'SCANREFWARM', 'ADC0.STATUS.SCANREFWARM', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_STATUS_PROGERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_STATUS_PROGERR, self).__init__(register,
            'PROGERR', 'ADC0.STATUS.PROGERR', 'read-only',
            "",
            10, 2,
            RM_Enum_ADC0_STATUS_PROGERR(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_STATUS_WARM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_STATUS_WARM, self).__init__(register,
            'WARM', 'ADC0.STATUS.WARM', 'read-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_STATUS_SINGLEDV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_STATUS_SINGLEDV, self).__init__(register,
            'SINGLEDV', 'ADC0.STATUS.SINGLEDV', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_STATUS_SCANDV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_STATUS_SCANDV, self).__init__(register,
            'SCANDV', 'ADC0.STATUS.SCANDV', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRL_REP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRL_REP, self).__init__(register,
            'REP', 'ADC0.SINGLECTRL.REP', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRL_DIFF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRL_DIFF, self).__init__(register,
            'DIFF', 'ADC0.SINGLECTRL.DIFF', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRL_ADJ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRL_ADJ, self).__init__(register,
            'ADJ', 'ADC0.SINGLECTRL.ADJ', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRL_RES(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRL_RES, self).__init__(register,
            'RES', 'ADC0.SINGLECTRL.RES', 'read-write',
            "",
            3, 2,
            RM_Enum_ADC0_SINGLECTRL_RES(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRL_REF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRL_REF, self).__init__(register,
            'REF', 'ADC0.SINGLECTRL.REF', 'read-write',
            "",
            5, 3,
            RM_Enum_ADC0_SINGLECTRL_REF(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRL_POSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRL_POSSEL, self).__init__(register,
            'POSSEL', 'ADC0.SINGLECTRL.POSSEL', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRL_NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRL_NEGSEL, self).__init__(register,
            'NEGSEL', 'ADC0.SINGLECTRL.NEGSEL', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRL_AT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRL_AT, self).__init__(register,
            'AT', 'ADC0.SINGLECTRL.AT', 'read-write',
            "",
            24, 4,
            RM_Enum_ADC0_SINGLECTRL_AT(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRL_PRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRL_PRSEN, self).__init__(register,
            'PRSEN', 'ADC0.SINGLECTRL.PRSEN', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRL_CMPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRL_CMPEN, self).__init__(register,
            'CMPEN', 'ADC0.SINGLECTRL.CMPEN', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRLX_VREFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRLX_VREFSEL, self).__init__(register,
            'VREFSEL', 'ADC0.SINGLECTRLX.VREFSEL', 'read-write',
            "",
            0, 3,
            RM_Enum_ADC0_SINGLECTRLX_VREFSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRLX_VREFATTFIX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRLX_VREFATTFIX, self).__init__(register,
            'VREFATTFIX', 'ADC0.SINGLECTRLX.VREFATTFIX', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRLX_VREFATT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRLX_VREFATT, self).__init__(register,
            'VREFATT', 'ADC0.SINGLECTRLX.VREFATT', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRLX_VINATT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRLX_VINATT, self).__init__(register,
            'VINATT', 'ADC0.SINGLECTRLX.VINATT', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRLX_DVL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRLX_DVL, self).__init__(register,
            'DVL', 'ADC0.SINGLECTRLX.DVL', 'read-write',
            "",
            12, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRLX_FIFOOFACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRLX_FIFOOFACT, self).__init__(register,
            'FIFOOFACT', 'ADC0.SINGLECTRLX.FIFOOFACT', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRLX_PRSMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRLX_PRSMODE, self).__init__(register,
            'PRSMODE', 'ADC0.SINGLECTRLX.PRSMODE', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRLX_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRLX_PRSSEL, self).__init__(register,
            'PRSSEL', 'ADC0.SINGLECTRLX.PRSSEL', 'read-write',
            "",
            17, 4,
            RM_Enum_ADC0_SINGLECTRLX_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRLX_CONVSTARTDELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRLX_CONVSTARTDELAY, self).__init__(register,
            'CONVSTARTDELAY', 'ADC0.SINGLECTRLX.CONVSTARTDELAY', 'read-write',
            "",
            22, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRLX_CONVSTARTDELAYEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRLX_CONVSTARTDELAYEN, self).__init__(register,
            'CONVSTARTDELAYEN', 'ADC0.SINGLECTRLX.CONVSTARTDELAYEN', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRLX_REPDELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRLX_REPDELAY, self).__init__(register,
            'REPDELAY', 'ADC0.SINGLECTRLX.REPDELAY', 'read-write',
            "",
            29, 3,
            RM_Enum_ADC0_SINGLECTRLX_REPDELAY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRL_REP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRL_REP, self).__init__(register,
            'REP', 'ADC0.SCANCTRL.REP', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRL_DIFF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRL_DIFF, self).__init__(register,
            'DIFF', 'ADC0.SCANCTRL.DIFF', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRL_ADJ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRL_ADJ, self).__init__(register,
            'ADJ', 'ADC0.SCANCTRL.ADJ', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRL_RES(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRL_RES, self).__init__(register,
            'RES', 'ADC0.SCANCTRL.RES', 'read-write',
            "",
            3, 2,
            RM_Enum_ADC0_SCANCTRL_RES(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRL_REF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRL_REF, self).__init__(register,
            'REF', 'ADC0.SCANCTRL.REF', 'read-write',
            "",
            5, 3,
            RM_Enum_ADC0_SCANCTRL_REF(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRL_AT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRL_AT, self).__init__(register,
            'AT', 'ADC0.SCANCTRL.AT', 'read-write',
            "",
            24, 4,
            RM_Enum_ADC0_SCANCTRL_AT(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRL_PRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRL_PRSEN, self).__init__(register,
            'PRSEN', 'ADC0.SCANCTRL.PRSEN', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRL_CMPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRL_CMPEN, self).__init__(register,
            'CMPEN', 'ADC0.SCANCTRL.CMPEN', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRLX_VREFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRLX_VREFSEL, self).__init__(register,
            'VREFSEL', 'ADC0.SCANCTRLX.VREFSEL', 'read-write',
            "",
            0, 3,
            RM_Enum_ADC0_SCANCTRLX_VREFSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRLX_VREFATTFIX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRLX_VREFATTFIX, self).__init__(register,
            'VREFATTFIX', 'ADC0.SCANCTRLX.VREFATTFIX', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRLX_VREFATT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRLX_VREFATT, self).__init__(register,
            'VREFATT', 'ADC0.SCANCTRLX.VREFATT', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRLX_VINATT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRLX_VINATT, self).__init__(register,
            'VINATT', 'ADC0.SCANCTRLX.VINATT', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRLX_DVL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRLX_DVL, self).__init__(register,
            'DVL', 'ADC0.SCANCTRLX.DVL', 'read-write',
            "",
            12, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRLX_FIFOOFACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRLX_FIFOOFACT, self).__init__(register,
            'FIFOOFACT', 'ADC0.SCANCTRLX.FIFOOFACT', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRLX_PRSMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRLX_PRSMODE, self).__init__(register,
            'PRSMODE', 'ADC0.SCANCTRLX.PRSMODE', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRLX_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRLX_PRSSEL, self).__init__(register,
            'PRSSEL', 'ADC0.SCANCTRLX.PRSSEL', 'read-write',
            "",
            17, 4,
            RM_Enum_ADC0_SCANCTRLX_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRLX_CONVSTARTDELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRLX_CONVSTARTDELAY, self).__init__(register,
            'CONVSTARTDELAY', 'ADC0.SCANCTRLX.CONVSTARTDELAY', 'read-write',
            "",
            22, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRLX_CONVSTARTDELAYEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRLX_CONVSTARTDELAYEN, self).__init__(register,
            'CONVSTARTDELAYEN', 'ADC0.SCANCTRLX.CONVSTARTDELAYEN', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRLX_REPDELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRLX_REPDELAY, self).__init__(register,
            'REPDELAY', 'ADC0.SCANCTRLX.REPDELAY', 'read-write',
            "",
            29, 3,
            RM_Enum_ADC0_SCANCTRLX_REPDELAY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANMASK_SCANINPUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANMASK_SCANINPUTEN, self).__init__(register,
            'SCANINPUTEN', 'ADC0.SCANMASK.SCANINPUTEN', 'read-write',
            "",
            0, 32,
            RM_Enum_ADC0_SCANMASK_SCANINPUTEN(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANINPUTSEL_INPUT0TO7SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANINPUTSEL_INPUT0TO7SEL, self).__init__(register,
            'INPUT0TO7SEL', 'ADC0.SCANINPUTSEL.INPUT0TO7SEL', 'read-write',
            "",
            0, 5,
            RM_Enum_ADC0_SCANINPUTSEL_INPUT0TO7SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANINPUTSEL_INPUT8TO15SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANINPUTSEL_INPUT8TO15SEL, self).__init__(register,
            'INPUT8TO15SEL', 'ADC0.SCANINPUTSEL.INPUT8TO15SEL', 'read-write',
            "",
            8, 5,
            RM_Enum_ADC0_SCANINPUTSEL_INPUT8TO15SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANINPUTSEL_INPUT16TO23SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANINPUTSEL_INPUT16TO23SEL, self).__init__(register,
            'INPUT16TO23SEL', 'ADC0.SCANINPUTSEL.INPUT16TO23SEL', 'read-write',
            "",
            16, 5,
            RM_Enum_ADC0_SCANINPUTSEL_INPUT16TO23SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANINPUTSEL_INPUT24TO31SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANINPUTSEL_INPUT24TO31SEL, self).__init__(register,
            'INPUT24TO31SEL', 'ADC0.SCANINPUTSEL.INPUT24TO31SEL', 'read-write',
            "",
            24, 5,
            RM_Enum_ADC0_SCANINPUTSEL_INPUT24TO31SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNEGSEL_INPUT0NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNEGSEL_INPUT0NEGSEL, self).__init__(register,
            'INPUT0NEGSEL', 'ADC0.SCANNEGSEL.INPUT0NEGSEL', 'read-write',
            "",
            0, 2,
            RM_Enum_ADC0_SCANNEGSEL_INPUT0NEGSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNEGSEL_INPUT2NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNEGSEL_INPUT2NEGSEL, self).__init__(register,
            'INPUT2NEGSEL', 'ADC0.SCANNEGSEL.INPUT2NEGSEL', 'read-write',
            "",
            2, 2,
            RM_Enum_ADC0_SCANNEGSEL_INPUT2NEGSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNEGSEL_INPUT4NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNEGSEL_INPUT4NEGSEL, self).__init__(register,
            'INPUT4NEGSEL', 'ADC0.SCANNEGSEL.INPUT4NEGSEL', 'read-write',
            "",
            4, 2,
            RM_Enum_ADC0_SCANNEGSEL_INPUT4NEGSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNEGSEL_INPUT6NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNEGSEL_INPUT6NEGSEL, self).__init__(register,
            'INPUT6NEGSEL', 'ADC0.SCANNEGSEL.INPUT6NEGSEL', 'read-write',
            "",
            6, 2,
            RM_Enum_ADC0_SCANNEGSEL_INPUT6NEGSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNEGSEL_INPUT9NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNEGSEL_INPUT9NEGSEL, self).__init__(register,
            'INPUT9NEGSEL', 'ADC0.SCANNEGSEL.INPUT9NEGSEL', 'read-write',
            "",
            8, 2,
            RM_Enum_ADC0_SCANNEGSEL_INPUT9NEGSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNEGSEL_INPUT11NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNEGSEL_INPUT11NEGSEL, self).__init__(register,
            'INPUT11NEGSEL', 'ADC0.SCANNEGSEL.INPUT11NEGSEL', 'read-write',
            "",
            10, 2,
            RM_Enum_ADC0_SCANNEGSEL_INPUT11NEGSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNEGSEL_INPUT13NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNEGSEL_INPUT13NEGSEL, self).__init__(register,
            'INPUT13NEGSEL', 'ADC0.SCANNEGSEL.INPUT13NEGSEL', 'read-write',
            "",
            12, 2,
            RM_Enum_ADC0_SCANNEGSEL_INPUT13NEGSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNEGSEL_INPUT15NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNEGSEL_INPUT15NEGSEL, self).__init__(register,
            'INPUT15NEGSEL', 'ADC0.SCANNEGSEL.INPUT15NEGSEL', 'read-write',
            "",
            14, 2,
            RM_Enum_ADC0_SCANNEGSEL_INPUT15NEGSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CMPTHR_ADLT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CMPTHR_ADLT, self).__init__(register,
            'ADLT', 'ADC0.CMPTHR.ADLT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CMPTHR_ADGT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CMPTHR_ADGT, self).__init__(register,
            'ADGT', 'ADC0.CMPTHR.ADGT', 'read-write',
            "",
            16, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BIASPROG_ADCBIASPROG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BIASPROG_ADCBIASPROG, self).__init__(register,
            'ADCBIASPROG', 'ADC0.BIASPROG.ADCBIASPROG', 'read-write',
            "",
            0, 4,
            RM_Enum_ADC0_BIASPROG_ADCBIASPROG(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BIASPROG_CONVSPEED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BIASPROG_CONVSPEED, self).__init__(register,
            'CONVSPEED', 'ADC0.BIASPROG.CONVSPEED', 'read-write',
            "",
            4, 2,
            RM_Enum_ADC0_BIASPROG_CONVSPEED(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BIASPROG_VREGSHUNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BIASPROG_VREGSHUNT, self).__init__(register,
            'VREGSHUNT', 'ADC0.BIASPROG.VREGSHUNT', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BIASPROG_VFAULTCLR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BIASPROG_VFAULTCLR, self).__init__(register,
            'VFAULTCLR', 'ADC0.BIASPROG.VFAULTCLR', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BIASPROG_GPBIASACC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BIASPROG_GPBIASACC, self).__init__(register,
            'GPBIASACC', 'ADC0.BIASPROG.GPBIASACC', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CAL_SINGLEOFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CAL_SINGLEOFFSET, self).__init__(register,
            'SINGLEOFFSET', 'ADC0.CAL.SINGLEOFFSET', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CAL_SINGLEOFFSETINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CAL_SINGLEOFFSETINV, self).__init__(register,
            'SINGLEOFFSETINV', 'ADC0.CAL.SINGLEOFFSETINV', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CAL_SINGLEGAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CAL_SINGLEGAIN, self).__init__(register,
            'SINGLEGAIN', 'ADC0.CAL.SINGLEGAIN', 'read-write',
            "",
            8, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CAL_OFFSETINVMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CAL_OFFSETINVMODE, self).__init__(register,
            'OFFSETINVMODE', 'ADC0.CAL.OFFSETINVMODE', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CAL_SCANOFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CAL_SCANOFFSET, self).__init__(register,
            'SCANOFFSET', 'ADC0.CAL.SCANOFFSET', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CAL_SCANOFFSETINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CAL_SCANOFFSETINV, self).__init__(register,
            'SCANOFFSETINV', 'ADC0.CAL.SCANOFFSETINV', 'read-write',
            "",
            20, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CAL_SCANGAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CAL_SCANGAIN, self).__init__(register,
            'SCANGAIN', 'ADC0.CAL.SCANGAIN', 'read-write',
            "",
            24, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CAL_CALEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CAL_CALEN, self).__init__(register,
            'CALEN', 'ADC0.CAL.CALEN', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IF_SINGLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IF_SINGLE, self).__init__(register,
            'SINGLE', 'ADC0.IF.SINGLE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IF_SCAN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IF_SCAN, self).__init__(register,
            'SCAN', 'ADC0.IF.SCAN', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IF_SINGLEOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IF_SINGLEOF, self).__init__(register,
            'SINGLEOF', 'ADC0.IF.SINGLEOF', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IF_SCANOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IF_SCANOF, self).__init__(register,
            'SCANOF', 'ADC0.IF.SCANOF', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IF_SINGLEUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IF_SINGLEUF, self).__init__(register,
            'SINGLEUF', 'ADC0.IF.SINGLEUF', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IF_SCANUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IF_SCANUF, self).__init__(register,
            'SCANUF', 'ADC0.IF.SCANUF', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IF_SINGLECMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IF_SINGLECMP, self).__init__(register,
            'SINGLECMP', 'ADC0.IF.SINGLECMP', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IF_SCANCMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IF_SCANCMP, self).__init__(register,
            'SCANCMP', 'ADC0.IF.SCANCMP', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IF_VREFOV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IF_VREFOV, self).__init__(register,
            'VREFOV', 'ADC0.IF.VREFOV', 'read-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IF_PROGERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IF_PROGERR, self).__init__(register,
            'PROGERR', 'ADC0.IF.PROGERR', 'read-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IF_SCANEXTPEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IF_SCANEXTPEND, self).__init__(register,
            'SCANEXTPEND', 'ADC0.IF.SCANEXTPEND', 'read-only',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IF_SCANPEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IF_SCANPEND, self).__init__(register,
            'SCANPEND', 'ADC0.IF.SCANPEND', 'read-only',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IF_PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IF_PRSTIMEDERR, self).__init__(register,
            'PRSTIMEDERR', 'ADC0.IF.PRSTIMEDERR', 'read-only',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IF_EM23ERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IF_EM23ERR, self).__init__(register,
            'EM23ERR', 'ADC0.IF.EM23ERR', 'read-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFS_SINGLEOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFS_SINGLEOF, self).__init__(register,
            'SINGLEOF', 'ADC0.IFS.SINGLEOF', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFS_SCANOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFS_SCANOF, self).__init__(register,
            'SCANOF', 'ADC0.IFS.SCANOF', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFS_SINGLEUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFS_SINGLEUF, self).__init__(register,
            'SINGLEUF', 'ADC0.IFS.SINGLEUF', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFS_SCANUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFS_SCANUF, self).__init__(register,
            'SCANUF', 'ADC0.IFS.SCANUF', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFS_SINGLECMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFS_SINGLECMP, self).__init__(register,
            'SINGLECMP', 'ADC0.IFS.SINGLECMP', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFS_SCANCMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFS_SCANCMP, self).__init__(register,
            'SCANCMP', 'ADC0.IFS.SCANCMP', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFS_VREFOV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFS_VREFOV, self).__init__(register,
            'VREFOV', 'ADC0.IFS.VREFOV', 'write-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFS_PROGERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFS_PROGERR, self).__init__(register,
            'PROGERR', 'ADC0.IFS.PROGERR', 'write-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFS_SCANEXTPEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFS_SCANEXTPEND, self).__init__(register,
            'SCANEXTPEND', 'ADC0.IFS.SCANEXTPEND', 'write-only',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFS_SCANPEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFS_SCANPEND, self).__init__(register,
            'SCANPEND', 'ADC0.IFS.SCANPEND', 'write-only',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFS_PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFS_PRSTIMEDERR, self).__init__(register,
            'PRSTIMEDERR', 'ADC0.IFS.PRSTIMEDERR', 'write-only',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFS_EM23ERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFS_EM23ERR, self).__init__(register,
            'EM23ERR', 'ADC0.IFS.EM23ERR', 'write-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFC_SINGLEOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFC_SINGLEOF, self).__init__(register,
            'SINGLEOF', 'ADC0.IFC.SINGLEOF', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFC_SCANOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFC_SCANOF, self).__init__(register,
            'SCANOF', 'ADC0.IFC.SCANOF', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFC_SINGLEUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFC_SINGLEUF, self).__init__(register,
            'SINGLEUF', 'ADC0.IFC.SINGLEUF', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFC_SCANUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFC_SCANUF, self).__init__(register,
            'SCANUF', 'ADC0.IFC.SCANUF', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFC_SINGLECMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFC_SINGLECMP, self).__init__(register,
            'SINGLECMP', 'ADC0.IFC.SINGLECMP', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFC_SCANCMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFC_SCANCMP, self).__init__(register,
            'SCANCMP', 'ADC0.IFC.SCANCMP', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFC_VREFOV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFC_VREFOV, self).__init__(register,
            'VREFOV', 'ADC0.IFC.VREFOV', 'write-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFC_PROGERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFC_PROGERR, self).__init__(register,
            'PROGERR', 'ADC0.IFC.PROGERR', 'write-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFC_SCANEXTPEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFC_SCANEXTPEND, self).__init__(register,
            'SCANEXTPEND', 'ADC0.IFC.SCANEXTPEND', 'write-only',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFC_SCANPEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFC_SCANPEND, self).__init__(register,
            'SCANPEND', 'ADC0.IFC.SCANPEND', 'write-only',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFC_PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFC_PRSTIMEDERR, self).__init__(register,
            'PRSTIMEDERR', 'ADC0.IFC.PRSTIMEDERR', 'write-only',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IFC_EM23ERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IFC_EM23ERR, self).__init__(register,
            'EM23ERR', 'ADC0.IFC.EM23ERR', 'write-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IEN_SINGLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IEN_SINGLE, self).__init__(register,
            'SINGLE', 'ADC0.IEN.SINGLE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IEN_SCAN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IEN_SCAN, self).__init__(register,
            'SCAN', 'ADC0.IEN.SCAN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IEN_SINGLEOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IEN_SINGLEOF, self).__init__(register,
            'SINGLEOF', 'ADC0.IEN.SINGLEOF', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IEN_SCANOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IEN_SCANOF, self).__init__(register,
            'SCANOF', 'ADC0.IEN.SCANOF', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IEN_SINGLEUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IEN_SINGLEUF, self).__init__(register,
            'SINGLEUF', 'ADC0.IEN.SINGLEUF', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IEN_SCANUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IEN_SCANUF, self).__init__(register,
            'SCANUF', 'ADC0.IEN.SCANUF', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IEN_SINGLECMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IEN_SINGLECMP, self).__init__(register,
            'SINGLECMP', 'ADC0.IEN.SINGLECMP', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IEN_SCANCMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IEN_SCANCMP, self).__init__(register,
            'SCANCMP', 'ADC0.IEN.SCANCMP', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IEN_VREFOV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IEN_VREFOV, self).__init__(register,
            'VREFOV', 'ADC0.IEN.VREFOV', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IEN_PROGERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IEN_PROGERR, self).__init__(register,
            'PROGERR', 'ADC0.IEN.PROGERR', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IEN_SCANEXTPEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IEN_SCANEXTPEND, self).__init__(register,
            'SCANEXTPEND', 'ADC0.IEN.SCANEXTPEND', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IEN_SCANPEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IEN_SCANPEND, self).__init__(register,
            'SCANPEND', 'ADC0.IEN.SCANPEND', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IEN_PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IEN_PRSTIMEDERR, self).__init__(register,
            'PRSTIMEDERR', 'ADC0.IEN.PRSTIMEDERR', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_IEN_EM23ERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_IEN_EM23ERR, self).__init__(register,
            'EM23ERR', 'ADC0.IEN.EM23ERR', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLEDATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLEDATA_DATA, self).__init__(register,
            'DATA', 'ADC0.SINGLEDATA.DATA', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANDATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANDATA_DATA, self).__init__(register,
            'DATA', 'ADC0.SCANDATA.DATA', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLEDATAP_DATAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLEDATAP_DATAP, self).__init__(register,
            'DATAP', 'ADC0.SINGLEDATAP.DATAP', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANDATAP_DATAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANDATAP_DATAP, self).__init__(register,
            'DATAP', 'ADC0.SCANDATAP.DATAP', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANDATAX_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANDATAX_DATA, self).__init__(register,
            'DATA', 'ADC0.SCANDATAX.DATA', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANDATAX_SCANINPUTID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANDATAX_SCANINPUTID, self).__init__(register,
            'SCANINPUTID', 'ADC0.SCANDATAX.SCANINPUTID', 'read-only',
            "",
            16, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANDATAXP_DATAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANDATAXP_DATAP, self).__init__(register,
            'DATAP', 'ADC0.SCANDATAXP.DATAP', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANDATAXP_SCANINPUTIDPEEK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANDATAXP_SCANINPUTIDPEEK, self).__init__(register,
            'SCANINPUTIDPEEK', 'ADC0.SCANDATAXP.SCANINPUTIDPEEK', 'read-only',
            "",
            16, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_TEST_VRPROTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_TEST_VRPROTEN, self).__init__(register,
            'VRPROTEN', 'ADC0.TEST.VRPROTEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_TEST_REFSAMPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_TEST_REFSAMPEN, self).__init__(register,
            'REFSAMPEN', 'ADC0.TEST.REFSAMPEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_TEST_THERMOFF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_TEST_THERMOFF, self).__init__(register,
            'THERMOFF', 'ADC0.TEST.THERMOFF', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_TEST_SAMPSYNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_TEST_SAMPSYNC, self).__init__(register,
            'SAMPSYNC', 'ADC0.TEST.SAMPSYNC', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_TEST_AZDISABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_TEST_AZDISABLE, self).__init__(register,
            'AZDISABLE', 'ADC0.TEST.AZDISABLE', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_TEST_TEMPSENSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_TEST_TEMPSENSEN, self).__init__(register,
            'TEMPSENSEN', 'ADC0.TEST.TEMPSENSEN', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_TEST_LDOPDDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_TEST_LDOPDDIS, self).__init__(register,
            'LDOPDDIS', 'ADC0.TEST.LDOPDDIS', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_TEST_GAINONVEXT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_TEST_GAINONVEXT, self).__init__(register,
            'GAINONVEXT', 'ADC0.TEST.GAINONVEXT', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_TEST_VREGSTEP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_TEST_VREGSTEP, self).__init__(register,
            'VREGSTEP', 'ADC0.TEST.VREGSTEP', 'read-write',
            "",
            16, 2,
            RM_Enum_ADC0_TEST_VREGSTEP(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_TEST_VREGRAIL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_TEST_VREGRAIL, self).__init__(register,
            'VREGRAIL', 'ADC0.TEST.VREGRAIL', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_TEST_VCMSTEP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_TEST_VCMSTEP, self).__init__(register,
            'VCMSTEP', 'ADC0.TEST.VCMSTEP', 'read-write',
            "",
            20, 2,
            RM_Enum_ADC0_TEST_VCMSTEP(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_TEST_IVGRSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_TEST_IVGRSEL, self).__init__(register,
            'IVGRSEL', 'ADC0.TEST.IVGRSEL', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTREQ_APORT0XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTREQ_APORT0XREQ, self).__init__(register,
            'APORT0XREQ', 'ADC0.APORTREQ.APORT0XREQ', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTREQ_APORT0YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTREQ_APORT0YREQ, self).__init__(register,
            'APORT0YREQ', 'ADC0.APORTREQ.APORT0YREQ', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTREQ_APORT1XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTREQ_APORT1XREQ, self).__init__(register,
            'APORT1XREQ', 'ADC0.APORTREQ.APORT1XREQ', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTREQ_APORT1YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTREQ_APORT1YREQ, self).__init__(register,
            'APORT1YREQ', 'ADC0.APORTREQ.APORT1YREQ', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTREQ_APORT2XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTREQ_APORT2XREQ, self).__init__(register,
            'APORT2XREQ', 'ADC0.APORTREQ.APORT2XREQ', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTREQ_APORT2YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTREQ_APORT2YREQ, self).__init__(register,
            'APORT2YREQ', 'ADC0.APORTREQ.APORT2YREQ', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTREQ_APORT3XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTREQ_APORT3XREQ, self).__init__(register,
            'APORT3XREQ', 'ADC0.APORTREQ.APORT3XREQ', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTREQ_APORT3YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTREQ_APORT3YREQ, self).__init__(register,
            'APORT3YREQ', 'ADC0.APORTREQ.APORT3YREQ', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTREQ_APORT4XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTREQ_APORT4XREQ, self).__init__(register,
            'APORT4XREQ', 'ADC0.APORTREQ.APORT4XREQ', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTREQ_APORT4YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTREQ_APORT4YREQ, self).__init__(register,
            'APORT4YREQ', 'ADC0.APORTREQ.APORT4YREQ', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTCONFLICT_APORT0XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTCONFLICT_APORT0XCONFLICT, self).__init__(register,
            'APORT0XCONFLICT', 'ADC0.APORTCONFLICT.APORT0XCONFLICT', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTCONFLICT_APORT0YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTCONFLICT_APORT0YCONFLICT, self).__init__(register,
            'APORT0YCONFLICT', 'ADC0.APORTCONFLICT.APORT0YCONFLICT', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTCONFLICT_APORT1XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTCONFLICT_APORT1XCONFLICT, self).__init__(register,
            'APORT1XCONFLICT', 'ADC0.APORTCONFLICT.APORT1XCONFLICT', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTCONFLICT_APORT1YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTCONFLICT_APORT1YCONFLICT, self).__init__(register,
            'APORT1YCONFLICT', 'ADC0.APORTCONFLICT.APORT1YCONFLICT', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTCONFLICT_APORT2XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTCONFLICT_APORT2XCONFLICT, self).__init__(register,
            'APORT2XCONFLICT', 'ADC0.APORTCONFLICT.APORT2XCONFLICT', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTCONFLICT_APORT2YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTCONFLICT_APORT2YCONFLICT, self).__init__(register,
            'APORT2YCONFLICT', 'ADC0.APORTCONFLICT.APORT2YCONFLICT', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTCONFLICT_APORT3XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTCONFLICT_APORT3XCONFLICT, self).__init__(register,
            'APORT3XCONFLICT', 'ADC0.APORTCONFLICT.APORT3XCONFLICT', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTCONFLICT_APORT3YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTCONFLICT_APORT3YCONFLICT, self).__init__(register,
            'APORT3YCONFLICT', 'ADC0.APORTCONFLICT.APORT3YCONFLICT', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTCONFLICT_APORT4XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTCONFLICT_APORT4XCONFLICT, self).__init__(register,
            'APORT4XCONFLICT', 'ADC0.APORTCONFLICT.APORT4XCONFLICT', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTCONFLICT_APORT4YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTCONFLICT_APORT4YCONFLICT, self).__init__(register,
            'APORT4YCONFLICT', 'ADC0.APORTCONFLICT.APORT4YCONFLICT', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLEFIFOCOUNT_SINGLEDC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLEFIFOCOUNT_SINGLEDC, self).__init__(register,
            'SINGLEDC', 'ADC0.SINGLEFIFOCOUNT.SINGLEDC', 'read-only',
            "",
            0, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANFIFOCOUNT_SCANDC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANFIFOCOUNT_SCANDC, self).__init__(register,
            'SCANDC', 'ADC0.SCANFIFOCOUNT.SCANDC', 'read-only',
            "",
            0, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLEFIFOCLEAR_SINGLEFIFOCLEAR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLEFIFOCLEAR_SINGLEFIFOCLEAR, self).__init__(register,
            'SINGLEFIFOCLEAR', 'ADC0.SINGLEFIFOCLEAR.SINGLEFIFOCLEAR', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANFIFOCLEAR_SCANFIFOCLEAR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANFIFOCLEAR_SCANFIFOCLEAR, self).__init__(register,
            'SCANFIFOCLEAR', 'ADC0.SCANFIFOCLEAR.SCANFIFOCLEAR', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTMASTERDIS_APORT1XMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTMASTERDIS_APORT1XMASTERDIS, self).__init__(register,
            'APORT1XMASTERDIS', 'ADC0.APORTMASTERDIS.APORT1XMASTERDIS', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTMASTERDIS_APORT1YMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTMASTERDIS_APORT1YMASTERDIS, self).__init__(register,
            'APORT1YMASTERDIS', 'ADC0.APORTMASTERDIS.APORT1YMASTERDIS', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTMASTERDIS_APORT2XMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTMASTERDIS_APORT2XMASTERDIS, self).__init__(register,
            'APORT2XMASTERDIS', 'ADC0.APORTMASTERDIS.APORT2XMASTERDIS', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTMASTERDIS_APORT2YMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTMASTERDIS_APORT2YMASTERDIS, self).__init__(register,
            'APORT2YMASTERDIS', 'ADC0.APORTMASTERDIS.APORT2YMASTERDIS', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTMASTERDIS_APORT3XMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTMASTERDIS_APORT3XMASTERDIS, self).__init__(register,
            'APORT3XMASTERDIS', 'ADC0.APORTMASTERDIS.APORT3XMASTERDIS', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTMASTERDIS_APORT3YMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTMASTERDIS_APORT3YMASTERDIS, self).__init__(register,
            'APORT3YMASTERDIS', 'ADC0.APORTMASTERDIS.APORT3YMASTERDIS', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTMASTERDIS_APORT4XMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTMASTERDIS_APORT4XMASTERDIS, self).__init__(register,
            'APORT4XMASTERDIS', 'ADC0.APORTMASTERDIS.APORT4XMASTERDIS', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_APORTMASTERDIS_APORT4YMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_APORTMASTERDIS_APORT4YMASTERDIS, self).__init__(register,
            'APORT4YMASTERDIS', 'ADC0.APORTMASTERDIS.APORT4YMASTERDIS', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


