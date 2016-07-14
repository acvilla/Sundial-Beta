
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


class RM_Field_ADC0_CTRL_CHCONMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CTRL_CHCONMODE, self).__init__(register,
            'CHCONMODE', 'ADC0.CTRL.CHCONMODE', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_CTRL_CHCONIDLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_CTRL_CHCONIDLE, self).__init__(register,
            'CHCONIDLE', 'ADC0.CTRL.CHCONIDLE', 'read-write',
            "",
            30, 2,
            RM_Enum_ADC0_CTRL_CHCONIDLE(register.zz_label))
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
            8, 8,
            RM_Enum_ADC0_SINGLECTRL_POSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRL_NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRL_NEGSEL, self).__init__(register,
            'NEGSEL', 'ADC0.SINGLECTRL.NEGSEL', 'read-write',
            "",
            16, 8,
            RM_Enum_ADC0_SINGLECTRL_NEGSEL(register.zz_label))
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
            24, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SINGLECTRLX_CONVSTARTDELAYEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SINGLECTRLX_CONVSTARTDELAYEN, self).__init__(register,
            'CONVSTARTDELAYEN', 'ADC0.SINGLECTRLX.CONVSTARTDELAYEN', 'read-write',
            "",
            27, 1)
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


class RM_Field_ADC0_SCANCTRLX_REPDELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRLX_REPDELAY, self).__init__(register,
            'REPDELAY', 'ADC0.SCANCTRLX.REPDELAY', 'read-write',
            "",
            24, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCTRLX_CONVSTARTDELAYEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCTRLX_CONVSTARTDELAYEN, self).__init__(register,
            'CONVSTARTDELAYEN', 'ADC0.SCANCTRLX.CONVSTARTDELAYEN', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANMASK_SCANMASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANMASK_SCANMASK, self).__init__(register,
            'SCANMASK', 'ADC0.SCANMASK.SCANMASK', 'read-write',
            "",
            0, 32,
            RM_Enum_ADC0_SCANMASK_SCANMASK(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCHCONF_CH0TO7SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCHCONF_CH0TO7SEL, self).__init__(register,
            'CH0TO7SEL', 'ADC0.SCANCHCONF.CH0TO7SEL', 'read-write',
            "",
            0, 5,
            RM_Enum_ADC0_SCANCHCONF_CH0TO7SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCHCONF_CH8TO15SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCHCONF_CH8TO15SEL, self).__init__(register,
            'CH8TO15SEL', 'ADC0.SCANCHCONF.CH8TO15SEL', 'read-write',
            "",
            8, 5,
            RM_Enum_ADC0_SCANCHCONF_CH8TO15SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCHCONF_CH16TO23SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCHCONF_CH16TO23SEL, self).__init__(register,
            'CH16TO23SEL', 'ADC0.SCANCHCONF.CH16TO23SEL', 'read-write',
            "",
            16, 5,
            RM_Enum_ADC0_SCANCHCONF_CH16TO23SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANCHCONF_CH24TO31SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANCHCONF_CH24TO31SEL, self).__init__(register,
            'CH24TO31SEL', 'ADC0.SCANCHCONF.CH24TO31SEL', 'read-write',
            "",
            24, 5,
            RM_Enum_ADC0_SCANCHCONF_CH24TO31SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNSEL_CH0NSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNSEL_CH0NSEL, self).__init__(register,
            'CH0NSEL', 'ADC0.SCANNSEL.CH0NSEL', 'read-write',
            "",
            0, 2,
            RM_Enum_ADC0_SCANNSEL_CH0NSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNSEL_CH2NSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNSEL_CH2NSEL, self).__init__(register,
            'CH2NSEL', 'ADC0.SCANNSEL.CH2NSEL', 'read-write',
            "",
            2, 2,
            RM_Enum_ADC0_SCANNSEL_CH2NSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNSEL_CH4NSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNSEL_CH4NSEL, self).__init__(register,
            'CH4NSEL', 'ADC0.SCANNSEL.CH4NSEL', 'read-write',
            "",
            4, 2,
            RM_Enum_ADC0_SCANNSEL_CH4NSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNSEL_CH6NSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNSEL_CH6NSEL, self).__init__(register,
            'CH6NSEL', 'ADC0.SCANNSEL.CH6NSEL', 'read-write',
            "",
            6, 2,
            RM_Enum_ADC0_SCANNSEL_CH6NSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNSEL_CH9NSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNSEL_CH9NSEL, self).__init__(register,
            'CH9NSEL', 'ADC0.SCANNSEL.CH9NSEL', 'read-write',
            "",
            8, 2,
            RM_Enum_ADC0_SCANNSEL_CH9NSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNSEL_CH11NSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNSEL_CH11NSEL, self).__init__(register,
            'CH11NSEL', 'ADC0.SCANNSEL.CH11NSEL', 'read-write',
            "",
            10, 2,
            RM_Enum_ADC0_SCANNSEL_CH11NSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNSEL_CH13NSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNSEL_CH13NSEL, self).__init__(register,
            'CH13NSEL', 'ADC0.SCANNSEL.CH13NSEL', 'read-write',
            "",
            12, 2,
            RM_Enum_ADC0_SCANNSEL_CH13NSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_SCANNSEL_CH15NSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANNSEL_CH15NSEL, self).__init__(register,
            'CH15NSEL', 'ADC0.SCANNSEL.CH15NSEL', 'read-write',
            "",
            14, 2,
            RM_Enum_ADC0_SCANNSEL_CH15NSEL(register.zz_label))
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
            0, 4)
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


class RM_Field_ADC0_SCANDATAX_SCANDATASRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANDATAX_SCANDATASRC, self).__init__(register,
            'SCANDATASRC', 'ADC0.SCANDATAX.SCANDATASRC', 'read-only',
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


class RM_Field_ADC0_SCANDATAXP_SCANDATASRCPEEK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_SCANDATAXP_SCANDATASRCPEEK, self).__init__(register,
            'SCANDATASRCPEEK', 'ADC0.SCANDATAXP.SCANDATASRCPEEK', 'read-only',
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


class RM_Field_ADC0_TEST_ILTCEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_TEST_ILTCEN, self).__init__(register,
            'ILTCEN', 'ADC0.TEST.ILTCEN', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_TEST_IVGRSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_TEST_IVGRSEL, self).__init__(register,
            'IVGRSEL', 'ADC0.TEST.IVGRSEL', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSREQ_BUS0XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSREQ_BUS0XREQ, self).__init__(register,
            'BUS0XREQ', 'ADC0.BUSREQ.BUS0XREQ', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSREQ_BUS0YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSREQ_BUS0YREQ, self).__init__(register,
            'BUS0YREQ', 'ADC0.BUSREQ.BUS0YREQ', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSREQ_BUS1XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSREQ_BUS1XREQ, self).__init__(register,
            'BUS1XREQ', 'ADC0.BUSREQ.BUS1XREQ', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSREQ_BUS1YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSREQ_BUS1YREQ, self).__init__(register,
            'BUS1YREQ', 'ADC0.BUSREQ.BUS1YREQ', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSREQ_BUS2XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSREQ_BUS2XREQ, self).__init__(register,
            'BUS2XREQ', 'ADC0.BUSREQ.BUS2XREQ', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSREQ_BUS2YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSREQ_BUS2YREQ, self).__init__(register,
            'BUS2YREQ', 'ADC0.BUSREQ.BUS2YREQ', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSREQ_BUS3XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSREQ_BUS3XREQ, self).__init__(register,
            'BUS3XREQ', 'ADC0.BUSREQ.BUS3XREQ', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSREQ_BUS3YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSREQ_BUS3YREQ, self).__init__(register,
            'BUS3YREQ', 'ADC0.BUSREQ.BUS3YREQ', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSREQ_BUS4XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSREQ_BUS4XREQ, self).__init__(register,
            'BUS4XREQ', 'ADC0.BUSREQ.BUS4XREQ', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSREQ_BUS4YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSREQ_BUS4YREQ, self).__init__(register,
            'BUS4YREQ', 'ADC0.BUSREQ.BUS4YREQ', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSCONFLICT_BUS0XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSCONFLICT_BUS0XCONFLICT, self).__init__(register,
            'BUS0XCONFLICT', 'ADC0.BUSCONFLICT.BUS0XCONFLICT', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSCONFLICT_BUS0YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSCONFLICT_BUS0YCONFLICT, self).__init__(register,
            'BUS0YCONFLICT', 'ADC0.BUSCONFLICT.BUS0YCONFLICT', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSCONFLICT_BUS1XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSCONFLICT_BUS1XCONFLICT, self).__init__(register,
            'BUS1XCONFLICT', 'ADC0.BUSCONFLICT.BUS1XCONFLICT', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSCONFLICT_BUS1YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSCONFLICT_BUS1YCONFLICT, self).__init__(register,
            'BUS1YCONFLICT', 'ADC0.BUSCONFLICT.BUS1YCONFLICT', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSCONFLICT_BUS2XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSCONFLICT_BUS2XCONFLICT, self).__init__(register,
            'BUS2XCONFLICT', 'ADC0.BUSCONFLICT.BUS2XCONFLICT', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSCONFLICT_BUS2YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSCONFLICT_BUS2YCONFLICT, self).__init__(register,
            'BUS2YCONFLICT', 'ADC0.BUSCONFLICT.BUS2YCONFLICT', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSCONFLICT_BUS3XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSCONFLICT_BUS3XCONFLICT, self).__init__(register,
            'BUS3XCONFLICT', 'ADC0.BUSCONFLICT.BUS3XCONFLICT', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSCONFLICT_BUS3YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSCONFLICT_BUS3YCONFLICT, self).__init__(register,
            'BUS3YCONFLICT', 'ADC0.BUSCONFLICT.BUS3YCONFLICT', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSCONFLICT_BUS4XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSCONFLICT_BUS4XCONFLICT, self).__init__(register,
            'BUS4XCONFLICT', 'ADC0.BUSCONFLICT.BUS4XCONFLICT', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ADC0_BUSCONFLICT_BUS4YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ADC0_BUSCONFLICT_BUS4YCONFLICT, self).__init__(register,
            'BUS4YCONFLICT', 'ADC0.BUSCONFLICT.BUS4YCONFLICT', 'read-only',
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


