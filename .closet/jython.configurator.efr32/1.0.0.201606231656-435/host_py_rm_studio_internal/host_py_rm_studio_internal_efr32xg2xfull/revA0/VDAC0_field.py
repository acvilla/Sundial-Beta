
from static import Base_RM_Field
from VDAC0_enum import *


class RM_Field_VDAC0_CTRL_DIFF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CTRL_DIFF, self).__init__(register,
            'DIFF', 'VDAC0.CTRL.DIFF', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CTRL_SINEMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CTRL_SINEMODE, self).__init__(register,
            'SINEMODE', 'VDAC0.CTRL.SINEMODE', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CTRL_OUTENPRS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CTRL_OUTENPRS, self).__init__(register,
            'OUTENPRS', 'VDAC0.CTRL.OUTENPRS', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CTRL_CH0PRESCRST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CTRL_CH0PRESCRST, self).__init__(register,
            'CH0PRESCRST', 'VDAC0.CTRL.CH0PRESCRST', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CTRL_REFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CTRL_REFSEL, self).__init__(register,
            'REFSEL', 'VDAC0.CTRL.REFSEL', 'read-write',
            "",
            8, 3,
            RM_Enum_VDAC0_CTRL_REFSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CTRL_PRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CTRL_PRESC, self).__init__(register,
            'PRESC', 'VDAC0.CTRL.PRESC', 'read-write',
            "",
            16, 7,
            RM_Enum_VDAC0_CTRL_PRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CTRL_REFRESHPERIOD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CTRL_REFRESHPERIOD, self).__init__(register,
            'REFRESHPERIOD', 'VDAC0.CTRL.REFRESHPERIOD', 'read-write',
            "",
            24, 2,
            RM_Enum_VDAC0_CTRL_REFRESHPERIOD(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CTRL_WARMUPMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CTRL_WARMUPMODE, self).__init__(register,
            'WARMUPMODE', 'VDAC0.CTRL.WARMUPMODE', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CTRL_DACCLKMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CTRL_DACCLKMODE, self).__init__(register,
            'DACCLKMODE', 'VDAC0.CTRL.DACCLKMODE', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_CH0ENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_CH0ENS, self).__init__(register,
            'CH0ENS', 'VDAC0.STATUS.CH0ENS', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_CH1ENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_CH1ENS, self).__init__(register,
            'CH1ENS', 'VDAC0.STATUS.CH1ENS', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_CH0BL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_CH0BL, self).__init__(register,
            'CH0BL', 'VDAC0.STATUS.CH0BL', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_CH1BL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_CH1BL, self).__init__(register,
            'CH1BL', 'VDAC0.STATUS.CH1BL', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_CH0WARM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_CH0WARM, self).__init__(register,
            'CH0WARM', 'VDAC0.STATUS.CH0WARM', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_CH1WARM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_CH1WARM, self).__init__(register,
            'CH1WARM', 'VDAC0.STATUS.CH1WARM', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_OPA0APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_OPA0APORTCONFLICT, self).__init__(register,
            'OPA0APORTCONFLICT', 'VDAC0.STATUS.OPA0APORTCONFLICT', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_OPA1APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_OPA1APORTCONFLICT, self).__init__(register,
            'OPA1APORTCONFLICT', 'VDAC0.STATUS.OPA1APORTCONFLICT', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_OPA2APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_OPA2APORTCONFLICT, self).__init__(register,
            'OPA2APORTCONFLICT', 'VDAC0.STATUS.OPA2APORTCONFLICT', 'read-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_OPA0ENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_OPA0ENS, self).__init__(register,
            'OPA0ENS', 'VDAC0.STATUS.OPA0ENS', 'read-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_OPA1ENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_OPA1ENS, self).__init__(register,
            'OPA1ENS', 'VDAC0.STATUS.OPA1ENS', 'read-only',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_OPA2ENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_OPA2ENS, self).__init__(register,
            'OPA2ENS', 'VDAC0.STATUS.OPA2ENS', 'read-only',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_OPA0WARM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_OPA0WARM, self).__init__(register,
            'OPA0WARM', 'VDAC0.STATUS.OPA0WARM', 'read-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_OPA1WARM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_OPA1WARM, self).__init__(register,
            'OPA1WARM', 'VDAC0.STATUS.OPA1WARM', 'read-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_OPA2WARM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_OPA2WARM, self).__init__(register,
            'OPA2WARM', 'VDAC0.STATUS.OPA2WARM', 'read-only',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_OPA0OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_OPA0OUTVALID, self).__init__(register,
            'OPA0OUTVALID', 'VDAC0.STATUS.OPA0OUTVALID', 'read-only',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_OPA1OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_OPA1OUTVALID, self).__init__(register,
            'OPA1OUTVALID', 'VDAC0.STATUS.OPA1OUTVALID', 'read-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_STATUS_OPA2OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_STATUS_OPA2OUTVALID, self).__init__(register,
            'OPA2OUTVALID', 'VDAC0.STATUS.OPA2OUTVALID', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CH0CTRL_CONVMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CH0CTRL_CONVMODE, self).__init__(register,
            'CONVMODE', 'VDAC0.CH0CTRL.CONVMODE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CH0CTRL_TRIGMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CH0CTRL_TRIGMODE, self).__init__(register,
            'TRIGMODE', 'VDAC0.CH0CTRL.TRIGMODE', 'read-write',
            "",
            4, 3,
            RM_Enum_VDAC0_CH0CTRL_TRIGMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CH0CTRL_PRSASYNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CH0CTRL_PRSASYNC, self).__init__(register,
            'PRSASYNC', 'VDAC0.CH0CTRL.PRSASYNC', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CH0CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CH0CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'VDAC0.CH0CTRL.PRSSEL', 'read-write',
            "",
            12, 4,
            RM_Enum_VDAC0_CH0CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CH1CTRL_CONVMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CH1CTRL_CONVMODE, self).__init__(register,
            'CONVMODE', 'VDAC0.CH1CTRL.CONVMODE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CH1CTRL_TRIGMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CH1CTRL_TRIGMODE, self).__init__(register,
            'TRIGMODE', 'VDAC0.CH1CTRL.TRIGMODE', 'read-write',
            "",
            4, 3,
            RM_Enum_VDAC0_CH1CTRL_TRIGMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CH1CTRL_PRSASYNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CH1CTRL_PRSASYNC, self).__init__(register,
            'PRSASYNC', 'VDAC0.CH1CTRL.PRSASYNC', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CH1CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CH1CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'VDAC0.CH1CTRL.PRSSEL', 'read-write',
            "",
            12, 4,
            RM_Enum_VDAC0_CH1CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CMD_CH0EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CMD_CH0EN, self).__init__(register,
            'CH0EN', 'VDAC0.CMD.CH0EN', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CMD_CH0DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CMD_CH0DIS, self).__init__(register,
            'CH0DIS', 'VDAC0.CMD.CH0DIS', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CMD_CH1EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CMD_CH1EN, self).__init__(register,
            'CH1EN', 'VDAC0.CMD.CH1EN', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CMD_CH1DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CMD_CH1DIS, self).__init__(register,
            'CH1DIS', 'VDAC0.CMD.CH1DIS', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CMD_OPA0EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CMD_OPA0EN, self).__init__(register,
            'OPA0EN', 'VDAC0.CMD.OPA0EN', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CMD_OPA0DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CMD_OPA0DIS, self).__init__(register,
            'OPA0DIS', 'VDAC0.CMD.OPA0DIS', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CMD_OPA1EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CMD_OPA1EN, self).__init__(register,
            'OPA1EN', 'VDAC0.CMD.OPA1EN', 'write-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CMD_OPA1DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CMD_OPA1DIS, self).__init__(register,
            'OPA1DIS', 'VDAC0.CMD.OPA1DIS', 'write-only',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CMD_OPA2EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CMD_OPA2EN, self).__init__(register,
            'OPA2EN', 'VDAC0.CMD.OPA2EN', 'write-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CMD_OPA2DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CMD_OPA2DIS, self).__init__(register,
            'OPA2DIS', 'VDAC0.CMD.OPA2DIS', 'write-only',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_CH0CD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_CH0CD, self).__init__(register,
            'CH0CD', 'VDAC0.IF.CH0CD', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_CH1CD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_CH1CD, self).__init__(register,
            'CH1CD', 'VDAC0.IF.CH1CD', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_CH0OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_CH0OF, self).__init__(register,
            'CH0OF', 'VDAC0.IF.CH0OF', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_CH1OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_CH1OF, self).__init__(register,
            'CH1OF', 'VDAC0.IF.CH1OF', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_CH0UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_CH0UF, self).__init__(register,
            'CH0UF', 'VDAC0.IF.CH0UF', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_CH1UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_CH1UF, self).__init__(register,
            'CH1UF', 'VDAC0.IF.CH1UF', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_CH0BL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_CH0BL, self).__init__(register,
            'CH0BL', 'VDAC0.IF.CH0BL', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_CH1BL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_CH1BL, self).__init__(register,
            'CH1BL', 'VDAC0.IF.CH1BL', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_EM23ERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_EM23ERR, self).__init__(register,
            'EM23ERR', 'VDAC0.IF.EM23ERR', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_OPA0APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_OPA0APORTCONFLICT, self).__init__(register,
            'OPA0APORTCONFLICT', 'VDAC0.IF.OPA0APORTCONFLICT', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_OPA1APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_OPA1APORTCONFLICT, self).__init__(register,
            'OPA1APORTCONFLICT', 'VDAC0.IF.OPA1APORTCONFLICT', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_OPA2APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_OPA2APORTCONFLICT, self).__init__(register,
            'OPA2APORTCONFLICT', 'VDAC0.IF.OPA2APORTCONFLICT', 'read-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_OPA0PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_OPA0PRSTIMEDERR, self).__init__(register,
            'OPA0PRSTIMEDERR', 'VDAC0.IF.OPA0PRSTIMEDERR', 'read-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_OPA1PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_OPA1PRSTIMEDERR, self).__init__(register,
            'OPA1PRSTIMEDERR', 'VDAC0.IF.OPA1PRSTIMEDERR', 'read-only',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_OPA2PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_OPA2PRSTIMEDERR, self).__init__(register,
            'OPA2PRSTIMEDERR', 'VDAC0.IF.OPA2PRSTIMEDERR', 'read-only',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_OPA0OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_OPA0OUTVALID, self).__init__(register,
            'OPA0OUTVALID', 'VDAC0.IF.OPA0OUTVALID', 'read-only',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_OPA1OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_OPA1OUTVALID, self).__init__(register,
            'OPA1OUTVALID', 'VDAC0.IF.OPA1OUTVALID', 'read-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IF_OPA2OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IF_OPA2OUTVALID, self).__init__(register,
            'OPA2OUTVALID', 'VDAC0.IF.OPA2OUTVALID', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_CH0CD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_CH0CD, self).__init__(register,
            'CH0CD', 'VDAC0.IFS.CH0CD', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_CH1CD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_CH1CD, self).__init__(register,
            'CH1CD', 'VDAC0.IFS.CH1CD', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_CH0OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_CH0OF, self).__init__(register,
            'CH0OF', 'VDAC0.IFS.CH0OF', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_CH1OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_CH1OF, self).__init__(register,
            'CH1OF', 'VDAC0.IFS.CH1OF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_CH0UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_CH0UF, self).__init__(register,
            'CH0UF', 'VDAC0.IFS.CH0UF', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_CH1UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_CH1UF, self).__init__(register,
            'CH1UF', 'VDAC0.IFS.CH1UF', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_EM23ERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_EM23ERR, self).__init__(register,
            'EM23ERR', 'VDAC0.IFS.EM23ERR', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_OPA0APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_OPA0APORTCONFLICT, self).__init__(register,
            'OPA0APORTCONFLICT', 'VDAC0.IFS.OPA0APORTCONFLICT', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_OPA1APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_OPA1APORTCONFLICT, self).__init__(register,
            'OPA1APORTCONFLICT', 'VDAC0.IFS.OPA1APORTCONFLICT', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_OPA2APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_OPA2APORTCONFLICT, self).__init__(register,
            'OPA2APORTCONFLICT', 'VDAC0.IFS.OPA2APORTCONFLICT', 'write-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_OPA0PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_OPA0PRSTIMEDERR, self).__init__(register,
            'OPA0PRSTIMEDERR', 'VDAC0.IFS.OPA0PRSTIMEDERR', 'write-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_OPA1PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_OPA1PRSTIMEDERR, self).__init__(register,
            'OPA1PRSTIMEDERR', 'VDAC0.IFS.OPA1PRSTIMEDERR', 'write-only',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_OPA2PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_OPA2PRSTIMEDERR, self).__init__(register,
            'OPA2PRSTIMEDERR', 'VDAC0.IFS.OPA2PRSTIMEDERR', 'write-only',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_OPA0OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_OPA0OUTVALID, self).__init__(register,
            'OPA0OUTVALID', 'VDAC0.IFS.OPA0OUTVALID', 'write-only',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_OPA1OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_OPA1OUTVALID, self).__init__(register,
            'OPA1OUTVALID', 'VDAC0.IFS.OPA1OUTVALID', 'write-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFS_OPA2OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFS_OPA2OUTVALID, self).__init__(register,
            'OPA2OUTVALID', 'VDAC0.IFS.OPA2OUTVALID', 'write-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_CH0CD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_CH0CD, self).__init__(register,
            'CH0CD', 'VDAC0.IFC.CH0CD', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_CH1CD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_CH1CD, self).__init__(register,
            'CH1CD', 'VDAC0.IFC.CH1CD', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_CH0OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_CH0OF, self).__init__(register,
            'CH0OF', 'VDAC0.IFC.CH0OF', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_CH1OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_CH1OF, self).__init__(register,
            'CH1OF', 'VDAC0.IFC.CH1OF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_CH0UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_CH0UF, self).__init__(register,
            'CH0UF', 'VDAC0.IFC.CH0UF', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_CH1UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_CH1UF, self).__init__(register,
            'CH1UF', 'VDAC0.IFC.CH1UF', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_EM23ERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_EM23ERR, self).__init__(register,
            'EM23ERR', 'VDAC0.IFC.EM23ERR', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_OPA0APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_OPA0APORTCONFLICT, self).__init__(register,
            'OPA0APORTCONFLICT', 'VDAC0.IFC.OPA0APORTCONFLICT', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_OPA1APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_OPA1APORTCONFLICT, self).__init__(register,
            'OPA1APORTCONFLICT', 'VDAC0.IFC.OPA1APORTCONFLICT', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_OPA2APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_OPA2APORTCONFLICT, self).__init__(register,
            'OPA2APORTCONFLICT', 'VDAC0.IFC.OPA2APORTCONFLICT', 'write-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_OPA0PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_OPA0PRSTIMEDERR, self).__init__(register,
            'OPA0PRSTIMEDERR', 'VDAC0.IFC.OPA0PRSTIMEDERR', 'write-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_OPA1PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_OPA1PRSTIMEDERR, self).__init__(register,
            'OPA1PRSTIMEDERR', 'VDAC0.IFC.OPA1PRSTIMEDERR', 'write-only',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_OPA2PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_OPA2PRSTIMEDERR, self).__init__(register,
            'OPA2PRSTIMEDERR', 'VDAC0.IFC.OPA2PRSTIMEDERR', 'write-only',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_OPA0OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_OPA0OUTVALID, self).__init__(register,
            'OPA0OUTVALID', 'VDAC0.IFC.OPA0OUTVALID', 'write-only',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_OPA1OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_OPA1OUTVALID, self).__init__(register,
            'OPA1OUTVALID', 'VDAC0.IFC.OPA1OUTVALID', 'write-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IFC_OPA2OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IFC_OPA2OUTVALID, self).__init__(register,
            'OPA2OUTVALID', 'VDAC0.IFC.OPA2OUTVALID', 'write-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_CH0CD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_CH0CD, self).__init__(register,
            'CH0CD', 'VDAC0.IEN.CH0CD', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_CH1CD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_CH1CD, self).__init__(register,
            'CH1CD', 'VDAC0.IEN.CH1CD', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_CH0OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_CH0OF, self).__init__(register,
            'CH0OF', 'VDAC0.IEN.CH0OF', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_CH1OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_CH1OF, self).__init__(register,
            'CH1OF', 'VDAC0.IEN.CH1OF', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_CH0UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_CH0UF, self).__init__(register,
            'CH0UF', 'VDAC0.IEN.CH0UF', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_CH1UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_CH1UF, self).__init__(register,
            'CH1UF', 'VDAC0.IEN.CH1UF', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_CH0BL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_CH0BL, self).__init__(register,
            'CH0BL', 'VDAC0.IEN.CH0BL', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_CH1BL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_CH1BL, self).__init__(register,
            'CH1BL', 'VDAC0.IEN.CH1BL', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_EM23ERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_EM23ERR, self).__init__(register,
            'EM23ERR', 'VDAC0.IEN.EM23ERR', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_OPA0APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_OPA0APORTCONFLICT, self).__init__(register,
            'OPA0APORTCONFLICT', 'VDAC0.IEN.OPA0APORTCONFLICT', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_OPA1APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_OPA1APORTCONFLICT, self).__init__(register,
            'OPA1APORTCONFLICT', 'VDAC0.IEN.OPA1APORTCONFLICT', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_OPA2APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_OPA2APORTCONFLICT, self).__init__(register,
            'OPA2APORTCONFLICT', 'VDAC0.IEN.OPA2APORTCONFLICT', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_OPA0PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_OPA0PRSTIMEDERR, self).__init__(register,
            'OPA0PRSTIMEDERR', 'VDAC0.IEN.OPA0PRSTIMEDERR', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_OPA1PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_OPA1PRSTIMEDERR, self).__init__(register,
            'OPA1PRSTIMEDERR', 'VDAC0.IEN.OPA1PRSTIMEDERR', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_OPA2PRSTIMEDERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_OPA2PRSTIMEDERR, self).__init__(register,
            'OPA2PRSTIMEDERR', 'VDAC0.IEN.OPA2PRSTIMEDERR', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_OPA0OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_OPA0OUTVALID, self).__init__(register,
            'OPA0OUTVALID', 'VDAC0.IEN.OPA0OUTVALID', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_OPA1OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_OPA1OUTVALID, self).__init__(register,
            'OPA1OUTVALID', 'VDAC0.IEN.OPA1OUTVALID', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_IEN_OPA2OUTVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_IEN_OPA2OUTVALID, self).__init__(register,
            'OPA2OUTVALID', 'VDAC0.IEN.OPA2OUTVALID', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CH0DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CH0DATA_DATA, self).__init__(register,
            'DATA', 'VDAC0.CH0DATA.DATA', 'read-write',
            "",
            0, 12)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CH1DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CH1DATA_DATA, self).__init__(register,
            'DATA', 'VDAC0.CH1DATA.DATA', 'read-write',
            "",
            0, 12)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_COMBDATA_CH0DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_COMBDATA_CH0DATA, self).__init__(register,
            'CH0DATA', 'VDAC0.COMBDATA.CH0DATA', 'read-write',
            "",
            0, 12)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_COMBDATA_CH1DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_COMBDATA_CH1DATA, self).__init__(register,
            'CH1DATA', 'VDAC0.COMBDATA.CH1DATA', 'read-write',
            "",
            16, 12)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CAL_OFFSETTRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CAL_OFFSETTRIM, self).__init__(register,
            'OFFSETTRIM', 'VDAC0.CAL.OFFSETTRIM', 'read-write',
            "",
            0, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CAL_GAINERRTRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CAL_GAINERRTRIM, self).__init__(register,
            'GAINERRTRIM', 'VDAC0.CAL.GAINERRTRIM', 'read-write',
            "",
            8, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_CAL_GAINERRTRIMCH1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_CAL_GAINERRTRIMCH1, self).__init__(register,
            'GAINERRTRIMCH1', 'VDAC0.CAL.GAINERRTRIMCH1', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_DBGCTRL_FORCEBIAS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_DBGCTRL_FORCEBIAS, self).__init__(register,
            'FORCEBIAS', 'VDAC0.DBGCTRL.FORCEBIAS', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_DBGCTRL_REFRESHRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_DBGCTRL_REFRESHRATE, self).__init__(register,
            'REFRESHRATE', 'VDAC0.DBGCTRL.REFRESHRATE', 'read-write',
            "",
            2, 2,
            RM_Enum_VDAC0_DBGCTRL_REFRESHRATE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_DBGCTRL_STARTUPBOOSTDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_DBGCTRL_STARTUPBOOSTDIS, self).__init__(register,
            'STARTUPBOOSTDIS', 'VDAC0.DBGCTRL.STARTUPBOOSTDIS', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_DBGCTRL_FORCEEMUOSC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_DBGCTRL_FORCEEMUOSC, self).__init__(register,
            'FORCEEMUOSC', 'VDAC0.DBGCTRL.FORCEEMUOSC', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_BIASPROG_GPBIASACC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_BIASPROG_GPBIASACC, self).__init__(register,
            'GPBIASACC', 'VDAC0.BIASPROG.GPBIASACC', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_REFENTIME_BGRREQTIME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_REFENTIME_BGRREQTIME, self).__init__(register,
            'BGRREQTIME', 'VDAC0.REFENTIME.BGRREQTIME', 'read-write',
            "",
            0, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_REFENTIME_EM2REFTIME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_REFENTIME_EM2REFTIME, self).__init__(register,
            'EM2REFTIME', 'VDAC0.REFENTIME.EM2REFTIME', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_TEST_DACFORCEEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_TEST_DACFORCEEN, self).__init__(register,
            'DACFORCEEN', 'VDAC0.TEST.DACFORCEEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_TEST_OPA0FORCEEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_TEST_OPA0FORCEEN, self).__init__(register,
            'OPA0FORCEEN', 'VDAC0.TEST.OPA0FORCEEN', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_TEST_OPA1FORCEEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_TEST_OPA1FORCEEN, self).__init__(register,
            'OPA1FORCEEN', 'VDAC0.TEST.OPA1FORCEEN', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_TEST_OPA2FORCEEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_TEST_OPA2FORCEEN, self).__init__(register,
            'OPA2FORCEEN', 'VDAC0.TEST.OPA2FORCEEN', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_TEST_OPA3FORCEEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_TEST_OPA3FORCEEN, self).__init__(register,
            'OPA3FORCEEN', 'VDAC0.TEST.OPA3FORCEEN', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_TEST_OPA0FORCEOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_TEST_OPA0FORCEOUTEN, self).__init__(register,
            'OPA0FORCEOUTEN', 'VDAC0.TEST.OPA0FORCEOUTEN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_TEST_OPA1FORCEOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_TEST_OPA1FORCEOUTEN, self).__init__(register,
            'OPA1FORCEOUTEN', 'VDAC0.TEST.OPA1FORCEOUTEN', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_TEST_OPA2FORCEOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_TEST_OPA2FORCEOUTEN, self).__init__(register,
            'OPA2FORCEOUTEN', 'VDAC0.TEST.OPA2FORCEOUTEN', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_TEST_OPA3FORCEOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_TEST_OPA3FORCEOUTEN, self).__init__(register,
            'OPA3FORCEOUTEN', 'VDAC0.TEST.OPA3FORCEOUTEN', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPAPRESC_PRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPAPRESC_PRESC, self).__init__(register,
            'PRESC', 'VDAC0.OPAPRESC.PRESC', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTREQ_APORT1XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTREQ_APORT1XREQ, self).__init__(register,
            'APORT1XREQ', 'VDAC0.OPA0_APORTREQ.APORT1XREQ', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTREQ_APORT1YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTREQ_APORT1YREQ, self).__init__(register,
            'APORT1YREQ', 'VDAC0.OPA0_APORTREQ.APORT1YREQ', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTREQ_APORT2XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTREQ_APORT2XREQ, self).__init__(register,
            'APORT2XREQ', 'VDAC0.OPA0_APORTREQ.APORT2XREQ', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTREQ_APORT2YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTREQ_APORT2YREQ, self).__init__(register,
            'APORT2YREQ', 'VDAC0.OPA0_APORTREQ.APORT2YREQ', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTREQ_APORT3XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTREQ_APORT3XREQ, self).__init__(register,
            'APORT3XREQ', 'VDAC0.OPA0_APORTREQ.APORT3XREQ', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTREQ_APORT3YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTREQ_APORT3YREQ, self).__init__(register,
            'APORT3YREQ', 'VDAC0.OPA0_APORTREQ.APORT3YREQ', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTREQ_APORT4XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTREQ_APORT4XREQ, self).__init__(register,
            'APORT4XREQ', 'VDAC0.OPA0_APORTREQ.APORT4XREQ', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTREQ_APORT4YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTREQ_APORT4YREQ, self).__init__(register,
            'APORT4YREQ', 'VDAC0.OPA0_APORTREQ.APORT4YREQ', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT1XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT1XCONFLICT, self).__init__(register,
            'APORT1XCONFLICT', 'VDAC0.OPA0_APORTCONFLICT.APORT1XCONFLICT', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT1YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT1YCONFLICT, self).__init__(register,
            'APORT1YCONFLICT', 'VDAC0.OPA0_APORTCONFLICT.APORT1YCONFLICT', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT2XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT2XCONFLICT, self).__init__(register,
            'APORT2XCONFLICT', 'VDAC0.OPA0_APORTCONFLICT.APORT2XCONFLICT', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT2YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT2YCONFLICT, self).__init__(register,
            'APORT2YCONFLICT', 'VDAC0.OPA0_APORTCONFLICT.APORT2YCONFLICT', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT3XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT3XCONFLICT, self).__init__(register,
            'APORT3XCONFLICT', 'VDAC0.OPA0_APORTCONFLICT.APORT3XCONFLICT', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT3YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT3YCONFLICT, self).__init__(register,
            'APORT3YCONFLICT', 'VDAC0.OPA0_APORTCONFLICT.APORT3YCONFLICT', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT4XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT4XCONFLICT, self).__init__(register,
            'APORT4XCONFLICT', 'VDAC0.OPA0_APORTCONFLICT.APORT4XCONFLICT', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT4YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT4YCONFLICT, self).__init__(register,
            'APORT4YCONFLICT', 'VDAC0.OPA0_APORTCONFLICT.APORT4YCONFLICT', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'VDAC0.OPA0_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 2,
            RM_Enum_VDAC0_OPA0_CTRL_DRIVESTRENGTH(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CTRL_INCBW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CTRL_INCBW, self).__init__(register,
            'INCBW', 'VDAC0.OPA0_CTRL.INCBW', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CTRL_HCMDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CTRL_HCMDIS, self).__init__(register,
            'HCMDIS', 'VDAC0.OPA0_CTRL.HCMDIS', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CTRL_OUTSCALE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CTRL_OUTSCALE, self).__init__(register,
            'OUTSCALE', 'VDAC0.OPA0_CTRL.OUTSCALE', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CTRL_PRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CTRL_PRSEN, self).__init__(register,
            'PRSEN', 'VDAC0.OPA0_CTRL.PRSEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CTRL_PRSMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CTRL_PRSMODE, self).__init__(register,
            'PRSMODE', 'VDAC0.OPA0_CTRL.PRSMODE', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'VDAC0.OPA0_CTRL.PRSSEL', 'read-write',
            "",
            10, 4,
            RM_Enum_VDAC0_OPA0_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CTRL_PRSOUTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CTRL_PRSOUTMODE, self).__init__(register,
            'PRSOUTMODE', 'VDAC0.OPA0_CTRL.PRSOUTMODE', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CTRL_APORTXMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CTRL_APORTXMASTERDIS, self).__init__(register,
            'APORTXMASTERDIS', 'VDAC0.OPA0_CTRL.APORTXMASTERDIS', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CTRL_APORTYMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CTRL_APORTYMASTERDIS, self).__init__(register,
            'APORTYMASTERDIS', 'VDAC0.OPA0_CTRL.APORTYMASTERDIS', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_TIMER_STARTUPDLY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_TIMER_STARTUPDLY, self).__init__(register,
            'STARTUPDLY', 'VDAC0.OPA0_TIMER.STARTUPDLY', 'read-write',
            "",
            0, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_TIMER_WARMUPTIME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_TIMER_WARMUPTIME, self).__init__(register,
            'WARMUPTIME', 'VDAC0.OPA0_TIMER.WARMUPTIME', 'read-write',
            "",
            8, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_TIMER_SETTLETIME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_TIMER_SETTLETIME, self).__init__(register,
            'SETTLETIME', 'VDAC0.OPA0_TIMER.SETTLETIME', 'read-write',
            "",
            16, 10)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_MUX_POSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_MUX_POSSEL, self).__init__(register,
            'POSSEL', 'VDAC0.OPA0_MUX.POSSEL', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_MUX_NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_MUX_NEGSEL, self).__init__(register,
            'NEGSEL', 'VDAC0.OPA0_MUX.NEGSEL', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_MUX_RESINMUX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_MUX_RESINMUX, self).__init__(register,
            'RESINMUX', 'VDAC0.OPA0_MUX.RESINMUX', 'read-write',
            "",
            16, 3,
            RM_Enum_VDAC0_OPA0_MUX_RESINMUX(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_MUX_GAIN3X(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_MUX_GAIN3X, self).__init__(register,
            'GAIN3X', 'VDAC0.OPA0_MUX.GAIN3X', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_MUX_RESSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_MUX_RESSEL, self).__init__(register,
            'RESSEL', 'VDAC0.OPA0_MUX.RESSEL', 'read-write',
            "",
            24, 3,
            RM_Enum_VDAC0_OPA0_MUX_RESSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_OUT_MAINOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_OUT_MAINOUTEN, self).__init__(register,
            'MAINOUTEN', 'VDAC0.OPA0_OUT.MAINOUTEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_OUT_ALTOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_OUT_ALTOUTEN, self).__init__(register,
            'ALTOUTEN', 'VDAC0.OPA0_OUT.ALTOUTEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_OUT_APORTOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_OUT_APORTOUTEN, self).__init__(register,
            'APORTOUTEN', 'VDAC0.OPA0_OUT.APORTOUTEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_OUT_SHORT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_OUT_SHORT, self).__init__(register,
            'SHORT', 'VDAC0.OPA0_OUT.SHORT', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_OUT_ALTOUTPADEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_OUT_ALTOUTPADEN, self).__init__(register,
            'ALTOUTPADEN', 'VDAC0.OPA0_OUT.ALTOUTPADEN', 'read-write',
            "",
            4, 5,
            RM_Enum_VDAC0_OPA0_OUT_ALTOUTPADEN(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_OUT_APORTOUTSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_OUT_APORTOUTSEL, self).__init__(register,
            'APORTOUTSEL', 'VDAC0.OPA0_OUT.APORTOUTSEL', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CAL_CM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CAL_CM1, self).__init__(register,
            'CM1', 'VDAC0.OPA0_CAL.CM1', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CAL_CM2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CAL_CM2, self).__init__(register,
            'CM2', 'VDAC0.OPA0_CAL.CM2', 'read-write',
            "",
            5, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CAL_CM3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CAL_CM3, self).__init__(register,
            'CM3', 'VDAC0.OPA0_CAL.CM3', 'read-write',
            "",
            10, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CAL_GM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CAL_GM, self).__init__(register,
            'GM', 'VDAC0.OPA0_CAL.GM', 'read-write',
            "",
            13, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CAL_GM3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CAL_GM3, self).__init__(register,
            'GM3', 'VDAC0.OPA0_CAL.GM3', 'read-write',
            "",
            17, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CAL_OFFSETP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CAL_OFFSETP, self).__init__(register,
            'OFFSETP', 'VDAC0.OPA0_CAL.OFFSETP', 'read-write',
            "",
            20, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA0_CAL_OFFSETN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA0_CAL_OFFSETN, self).__init__(register,
            'OFFSETN', 'VDAC0.OPA0_CAL.OFFSETN', 'read-write',
            "",
            26, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTREQ_APORT1XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTREQ_APORT1XREQ, self).__init__(register,
            'APORT1XREQ', 'VDAC0.OPA1_APORTREQ.APORT1XREQ', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTREQ_APORT1YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTREQ_APORT1YREQ, self).__init__(register,
            'APORT1YREQ', 'VDAC0.OPA1_APORTREQ.APORT1YREQ', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTREQ_APORT2XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTREQ_APORT2XREQ, self).__init__(register,
            'APORT2XREQ', 'VDAC0.OPA1_APORTREQ.APORT2XREQ', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTREQ_APORT2YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTREQ_APORT2YREQ, self).__init__(register,
            'APORT2YREQ', 'VDAC0.OPA1_APORTREQ.APORT2YREQ', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTREQ_APORT3XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTREQ_APORT3XREQ, self).__init__(register,
            'APORT3XREQ', 'VDAC0.OPA1_APORTREQ.APORT3XREQ', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTREQ_APORT3YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTREQ_APORT3YREQ, self).__init__(register,
            'APORT3YREQ', 'VDAC0.OPA1_APORTREQ.APORT3YREQ', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTREQ_APORT4XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTREQ_APORT4XREQ, self).__init__(register,
            'APORT4XREQ', 'VDAC0.OPA1_APORTREQ.APORT4XREQ', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTREQ_APORT4YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTREQ_APORT4YREQ, self).__init__(register,
            'APORT4YREQ', 'VDAC0.OPA1_APORTREQ.APORT4YREQ', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT1XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT1XCONFLICT, self).__init__(register,
            'APORT1XCONFLICT', 'VDAC0.OPA1_APORTCONFLICT.APORT1XCONFLICT', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT1YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT1YCONFLICT, self).__init__(register,
            'APORT1YCONFLICT', 'VDAC0.OPA1_APORTCONFLICT.APORT1YCONFLICT', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT2XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT2XCONFLICT, self).__init__(register,
            'APORT2XCONFLICT', 'VDAC0.OPA1_APORTCONFLICT.APORT2XCONFLICT', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT2YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT2YCONFLICT, self).__init__(register,
            'APORT2YCONFLICT', 'VDAC0.OPA1_APORTCONFLICT.APORT2YCONFLICT', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT3XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT3XCONFLICT, self).__init__(register,
            'APORT3XCONFLICT', 'VDAC0.OPA1_APORTCONFLICT.APORT3XCONFLICT', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT3YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT3YCONFLICT, self).__init__(register,
            'APORT3YCONFLICT', 'VDAC0.OPA1_APORTCONFLICT.APORT3YCONFLICT', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT4XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT4XCONFLICT, self).__init__(register,
            'APORT4XCONFLICT', 'VDAC0.OPA1_APORTCONFLICT.APORT4XCONFLICT', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT4YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT4YCONFLICT, self).__init__(register,
            'APORT4YCONFLICT', 'VDAC0.OPA1_APORTCONFLICT.APORT4YCONFLICT', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'VDAC0.OPA1_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 2,
            RM_Enum_VDAC0_OPA1_CTRL_DRIVESTRENGTH(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CTRL_INCBW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CTRL_INCBW, self).__init__(register,
            'INCBW', 'VDAC0.OPA1_CTRL.INCBW', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CTRL_HCMDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CTRL_HCMDIS, self).__init__(register,
            'HCMDIS', 'VDAC0.OPA1_CTRL.HCMDIS', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CTRL_OUTSCALE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CTRL_OUTSCALE, self).__init__(register,
            'OUTSCALE', 'VDAC0.OPA1_CTRL.OUTSCALE', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CTRL_PRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CTRL_PRSEN, self).__init__(register,
            'PRSEN', 'VDAC0.OPA1_CTRL.PRSEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CTRL_PRSMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CTRL_PRSMODE, self).__init__(register,
            'PRSMODE', 'VDAC0.OPA1_CTRL.PRSMODE', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'VDAC0.OPA1_CTRL.PRSSEL', 'read-write',
            "",
            10, 4,
            RM_Enum_VDAC0_OPA1_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CTRL_PRSOUTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CTRL_PRSOUTMODE, self).__init__(register,
            'PRSOUTMODE', 'VDAC0.OPA1_CTRL.PRSOUTMODE', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CTRL_APORTXMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CTRL_APORTXMASTERDIS, self).__init__(register,
            'APORTXMASTERDIS', 'VDAC0.OPA1_CTRL.APORTXMASTERDIS', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CTRL_APORTYMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CTRL_APORTYMASTERDIS, self).__init__(register,
            'APORTYMASTERDIS', 'VDAC0.OPA1_CTRL.APORTYMASTERDIS', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_TIMER_STARTUPDLY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_TIMER_STARTUPDLY, self).__init__(register,
            'STARTUPDLY', 'VDAC0.OPA1_TIMER.STARTUPDLY', 'read-write',
            "",
            0, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_TIMER_WARMUPTIME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_TIMER_WARMUPTIME, self).__init__(register,
            'WARMUPTIME', 'VDAC0.OPA1_TIMER.WARMUPTIME', 'read-write',
            "",
            8, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_TIMER_SETTLETIME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_TIMER_SETTLETIME, self).__init__(register,
            'SETTLETIME', 'VDAC0.OPA1_TIMER.SETTLETIME', 'read-write',
            "",
            16, 10)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_MUX_POSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_MUX_POSSEL, self).__init__(register,
            'POSSEL', 'VDAC0.OPA1_MUX.POSSEL', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_MUX_NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_MUX_NEGSEL, self).__init__(register,
            'NEGSEL', 'VDAC0.OPA1_MUX.NEGSEL', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_MUX_RESINMUX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_MUX_RESINMUX, self).__init__(register,
            'RESINMUX', 'VDAC0.OPA1_MUX.RESINMUX', 'read-write',
            "",
            16, 3,
            RM_Enum_VDAC0_OPA1_MUX_RESINMUX(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_MUX_GAIN3X(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_MUX_GAIN3X, self).__init__(register,
            'GAIN3X', 'VDAC0.OPA1_MUX.GAIN3X', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_MUX_RESSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_MUX_RESSEL, self).__init__(register,
            'RESSEL', 'VDAC0.OPA1_MUX.RESSEL', 'read-write',
            "",
            24, 3,
            RM_Enum_VDAC0_OPA1_MUX_RESSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_OUT_MAINOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_OUT_MAINOUTEN, self).__init__(register,
            'MAINOUTEN', 'VDAC0.OPA1_OUT.MAINOUTEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_OUT_ALTOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_OUT_ALTOUTEN, self).__init__(register,
            'ALTOUTEN', 'VDAC0.OPA1_OUT.ALTOUTEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_OUT_APORTOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_OUT_APORTOUTEN, self).__init__(register,
            'APORTOUTEN', 'VDAC0.OPA1_OUT.APORTOUTEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_OUT_SHORT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_OUT_SHORT, self).__init__(register,
            'SHORT', 'VDAC0.OPA1_OUT.SHORT', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_OUT_ALTOUTPADEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_OUT_ALTOUTPADEN, self).__init__(register,
            'ALTOUTPADEN', 'VDAC0.OPA1_OUT.ALTOUTPADEN', 'read-write',
            "",
            4, 5,
            RM_Enum_VDAC0_OPA1_OUT_ALTOUTPADEN(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_OUT_APORTOUTSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_OUT_APORTOUTSEL, self).__init__(register,
            'APORTOUTSEL', 'VDAC0.OPA1_OUT.APORTOUTSEL', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CAL_CM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CAL_CM1, self).__init__(register,
            'CM1', 'VDAC0.OPA1_CAL.CM1', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CAL_CM2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CAL_CM2, self).__init__(register,
            'CM2', 'VDAC0.OPA1_CAL.CM2', 'read-write',
            "",
            5, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CAL_CM3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CAL_CM3, self).__init__(register,
            'CM3', 'VDAC0.OPA1_CAL.CM3', 'read-write',
            "",
            10, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CAL_GM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CAL_GM, self).__init__(register,
            'GM', 'VDAC0.OPA1_CAL.GM', 'read-write',
            "",
            13, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CAL_GM3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CAL_GM3, self).__init__(register,
            'GM3', 'VDAC0.OPA1_CAL.GM3', 'read-write',
            "",
            17, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CAL_OFFSETP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CAL_OFFSETP, self).__init__(register,
            'OFFSETP', 'VDAC0.OPA1_CAL.OFFSETP', 'read-write',
            "",
            20, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA1_CAL_OFFSETN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA1_CAL_OFFSETN, self).__init__(register,
            'OFFSETN', 'VDAC0.OPA1_CAL.OFFSETN', 'read-write',
            "",
            26, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTREQ_APORT1XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTREQ_APORT1XREQ, self).__init__(register,
            'APORT1XREQ', 'VDAC0.OPA2_APORTREQ.APORT1XREQ', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTREQ_APORT1YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTREQ_APORT1YREQ, self).__init__(register,
            'APORT1YREQ', 'VDAC0.OPA2_APORTREQ.APORT1YREQ', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTREQ_APORT2XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTREQ_APORT2XREQ, self).__init__(register,
            'APORT2XREQ', 'VDAC0.OPA2_APORTREQ.APORT2XREQ', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTREQ_APORT2YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTREQ_APORT2YREQ, self).__init__(register,
            'APORT2YREQ', 'VDAC0.OPA2_APORTREQ.APORT2YREQ', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTREQ_APORT3XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTREQ_APORT3XREQ, self).__init__(register,
            'APORT3XREQ', 'VDAC0.OPA2_APORTREQ.APORT3XREQ', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTREQ_APORT3YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTREQ_APORT3YREQ, self).__init__(register,
            'APORT3YREQ', 'VDAC0.OPA2_APORTREQ.APORT3YREQ', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTREQ_APORT4XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTREQ_APORT4XREQ, self).__init__(register,
            'APORT4XREQ', 'VDAC0.OPA2_APORTREQ.APORT4XREQ', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTREQ_APORT4YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTREQ_APORT4YREQ, self).__init__(register,
            'APORT4YREQ', 'VDAC0.OPA2_APORTREQ.APORT4YREQ', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT1XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT1XCONFLICT, self).__init__(register,
            'APORT1XCONFLICT', 'VDAC0.OPA2_APORTCONFLICT.APORT1XCONFLICT', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT1YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT1YCONFLICT, self).__init__(register,
            'APORT1YCONFLICT', 'VDAC0.OPA2_APORTCONFLICT.APORT1YCONFLICT', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT2XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT2XCONFLICT, self).__init__(register,
            'APORT2XCONFLICT', 'VDAC0.OPA2_APORTCONFLICT.APORT2XCONFLICT', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT2YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT2YCONFLICT, self).__init__(register,
            'APORT2YCONFLICT', 'VDAC0.OPA2_APORTCONFLICT.APORT2YCONFLICT', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT3XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT3XCONFLICT, self).__init__(register,
            'APORT3XCONFLICT', 'VDAC0.OPA2_APORTCONFLICT.APORT3XCONFLICT', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT3YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT3YCONFLICT, self).__init__(register,
            'APORT3YCONFLICT', 'VDAC0.OPA2_APORTCONFLICT.APORT3YCONFLICT', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT4XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT4XCONFLICT, self).__init__(register,
            'APORT4XCONFLICT', 'VDAC0.OPA2_APORTCONFLICT.APORT4XCONFLICT', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT4YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT4YCONFLICT, self).__init__(register,
            'APORT4YCONFLICT', 'VDAC0.OPA2_APORTCONFLICT.APORT4YCONFLICT', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'VDAC0.OPA2_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 2,
            RM_Enum_VDAC0_OPA2_CTRL_DRIVESTRENGTH(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CTRL_INCBW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CTRL_INCBW, self).__init__(register,
            'INCBW', 'VDAC0.OPA2_CTRL.INCBW', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CTRL_HCMDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CTRL_HCMDIS, self).__init__(register,
            'HCMDIS', 'VDAC0.OPA2_CTRL.HCMDIS', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CTRL_OUTSCALE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CTRL_OUTSCALE, self).__init__(register,
            'OUTSCALE', 'VDAC0.OPA2_CTRL.OUTSCALE', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CTRL_PRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CTRL_PRSEN, self).__init__(register,
            'PRSEN', 'VDAC0.OPA2_CTRL.PRSEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CTRL_PRSMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CTRL_PRSMODE, self).__init__(register,
            'PRSMODE', 'VDAC0.OPA2_CTRL.PRSMODE', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'VDAC0.OPA2_CTRL.PRSSEL', 'read-write',
            "",
            10, 4,
            RM_Enum_VDAC0_OPA2_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CTRL_PRSOUTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CTRL_PRSOUTMODE, self).__init__(register,
            'PRSOUTMODE', 'VDAC0.OPA2_CTRL.PRSOUTMODE', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CTRL_APORTXMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CTRL_APORTXMASTERDIS, self).__init__(register,
            'APORTXMASTERDIS', 'VDAC0.OPA2_CTRL.APORTXMASTERDIS', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CTRL_APORTYMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CTRL_APORTYMASTERDIS, self).__init__(register,
            'APORTYMASTERDIS', 'VDAC0.OPA2_CTRL.APORTYMASTERDIS', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_TIMER_STARTUPDLY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_TIMER_STARTUPDLY, self).__init__(register,
            'STARTUPDLY', 'VDAC0.OPA2_TIMER.STARTUPDLY', 'read-write',
            "",
            0, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_TIMER_WARMUPTIME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_TIMER_WARMUPTIME, self).__init__(register,
            'WARMUPTIME', 'VDAC0.OPA2_TIMER.WARMUPTIME', 'read-write',
            "",
            8, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_TIMER_SETTLETIME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_TIMER_SETTLETIME, self).__init__(register,
            'SETTLETIME', 'VDAC0.OPA2_TIMER.SETTLETIME', 'read-write',
            "",
            16, 10)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_MUX_POSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_MUX_POSSEL, self).__init__(register,
            'POSSEL', 'VDAC0.OPA2_MUX.POSSEL', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_MUX_NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_MUX_NEGSEL, self).__init__(register,
            'NEGSEL', 'VDAC0.OPA2_MUX.NEGSEL', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_MUX_RESINMUX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_MUX_RESINMUX, self).__init__(register,
            'RESINMUX', 'VDAC0.OPA2_MUX.RESINMUX', 'read-write',
            "",
            16, 3,
            RM_Enum_VDAC0_OPA2_MUX_RESINMUX(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_MUX_GAIN3X(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_MUX_GAIN3X, self).__init__(register,
            'GAIN3X', 'VDAC0.OPA2_MUX.GAIN3X', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_MUX_RESSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_MUX_RESSEL, self).__init__(register,
            'RESSEL', 'VDAC0.OPA2_MUX.RESSEL', 'read-write',
            "",
            24, 3,
            RM_Enum_VDAC0_OPA2_MUX_RESSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_OUT_MAINOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_OUT_MAINOUTEN, self).__init__(register,
            'MAINOUTEN', 'VDAC0.OPA2_OUT.MAINOUTEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_OUT_ALTOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_OUT_ALTOUTEN, self).__init__(register,
            'ALTOUTEN', 'VDAC0.OPA2_OUT.ALTOUTEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_OUT_APORTOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_OUT_APORTOUTEN, self).__init__(register,
            'APORTOUTEN', 'VDAC0.OPA2_OUT.APORTOUTEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_OUT_SHORT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_OUT_SHORT, self).__init__(register,
            'SHORT', 'VDAC0.OPA2_OUT.SHORT', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_OUT_ALTOUTPADEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_OUT_ALTOUTPADEN, self).__init__(register,
            'ALTOUTPADEN', 'VDAC0.OPA2_OUT.ALTOUTPADEN', 'read-write',
            "",
            4, 5,
            RM_Enum_VDAC0_OPA2_OUT_ALTOUTPADEN(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_OUT_APORTOUTSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_OUT_APORTOUTSEL, self).__init__(register,
            'APORTOUTSEL', 'VDAC0.OPA2_OUT.APORTOUTSEL', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CAL_CM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CAL_CM1, self).__init__(register,
            'CM1', 'VDAC0.OPA2_CAL.CM1', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CAL_CM2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CAL_CM2, self).__init__(register,
            'CM2', 'VDAC0.OPA2_CAL.CM2', 'read-write',
            "",
            5, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CAL_CM3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CAL_CM3, self).__init__(register,
            'CM3', 'VDAC0.OPA2_CAL.CM3', 'read-write',
            "",
            10, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CAL_GM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CAL_GM, self).__init__(register,
            'GM', 'VDAC0.OPA2_CAL.GM', 'read-write',
            "",
            13, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CAL_GM3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CAL_GM3, self).__init__(register,
            'GM3', 'VDAC0.OPA2_CAL.GM3', 'read-write',
            "",
            17, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CAL_OFFSETP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CAL_OFFSETP, self).__init__(register,
            'OFFSETP', 'VDAC0.OPA2_CAL.OFFSETP', 'read-write',
            "",
            20, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA2_CAL_OFFSETN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA2_CAL_OFFSETN, self).__init__(register,
            'OFFSETN', 'VDAC0.OPA2_CAL.OFFSETN', 'read-write',
            "",
            26, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTREQ_APORT1XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTREQ_APORT1XREQ, self).__init__(register,
            'APORT1XREQ', 'VDAC0.OPA3_APORTREQ.APORT1XREQ', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTREQ_APORT1YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTREQ_APORT1YREQ, self).__init__(register,
            'APORT1YREQ', 'VDAC0.OPA3_APORTREQ.APORT1YREQ', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTREQ_APORT2XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTREQ_APORT2XREQ, self).__init__(register,
            'APORT2XREQ', 'VDAC0.OPA3_APORTREQ.APORT2XREQ', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTREQ_APORT2YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTREQ_APORT2YREQ, self).__init__(register,
            'APORT2YREQ', 'VDAC0.OPA3_APORTREQ.APORT2YREQ', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTREQ_APORT3XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTREQ_APORT3XREQ, self).__init__(register,
            'APORT3XREQ', 'VDAC0.OPA3_APORTREQ.APORT3XREQ', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTREQ_APORT3YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTREQ_APORT3YREQ, self).__init__(register,
            'APORT3YREQ', 'VDAC0.OPA3_APORTREQ.APORT3YREQ', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTREQ_APORT4XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTREQ_APORT4XREQ, self).__init__(register,
            'APORT4XREQ', 'VDAC0.OPA3_APORTREQ.APORT4XREQ', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTREQ_APORT4YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTREQ_APORT4YREQ, self).__init__(register,
            'APORT4YREQ', 'VDAC0.OPA3_APORTREQ.APORT4YREQ', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT1XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT1XCONFLICT, self).__init__(register,
            'APORT1XCONFLICT', 'VDAC0.OPA3_APORTCONFLICT.APORT1XCONFLICT', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT1YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT1YCONFLICT, self).__init__(register,
            'APORT1YCONFLICT', 'VDAC0.OPA3_APORTCONFLICT.APORT1YCONFLICT', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT2XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT2XCONFLICT, self).__init__(register,
            'APORT2XCONFLICT', 'VDAC0.OPA3_APORTCONFLICT.APORT2XCONFLICT', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT2YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT2YCONFLICT, self).__init__(register,
            'APORT2YCONFLICT', 'VDAC0.OPA3_APORTCONFLICT.APORT2YCONFLICT', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT3XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT3XCONFLICT, self).__init__(register,
            'APORT3XCONFLICT', 'VDAC0.OPA3_APORTCONFLICT.APORT3XCONFLICT', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT3YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT3YCONFLICT, self).__init__(register,
            'APORT3YCONFLICT', 'VDAC0.OPA3_APORTCONFLICT.APORT3YCONFLICT', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT4XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT4XCONFLICT, self).__init__(register,
            'APORT4XCONFLICT', 'VDAC0.OPA3_APORTCONFLICT.APORT4XCONFLICT', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT4YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT4YCONFLICT, self).__init__(register,
            'APORT4YCONFLICT', 'VDAC0.OPA3_APORTCONFLICT.APORT4YCONFLICT', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'VDAC0.OPA3_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 2,
            RM_Enum_VDAC0_OPA3_CTRL_DRIVESTRENGTH(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CTRL_INCBW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CTRL_INCBW, self).__init__(register,
            'INCBW', 'VDAC0.OPA3_CTRL.INCBW', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CTRL_HCMDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CTRL_HCMDIS, self).__init__(register,
            'HCMDIS', 'VDAC0.OPA3_CTRL.HCMDIS', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CTRL_OUTSCALE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CTRL_OUTSCALE, self).__init__(register,
            'OUTSCALE', 'VDAC0.OPA3_CTRL.OUTSCALE', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CTRL_PRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CTRL_PRSEN, self).__init__(register,
            'PRSEN', 'VDAC0.OPA3_CTRL.PRSEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CTRL_PRSMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CTRL_PRSMODE, self).__init__(register,
            'PRSMODE', 'VDAC0.OPA3_CTRL.PRSMODE', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'VDAC0.OPA3_CTRL.PRSSEL', 'read-write',
            "",
            10, 4,
            RM_Enum_VDAC0_OPA3_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CTRL_PRSOUTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CTRL_PRSOUTMODE, self).__init__(register,
            'PRSOUTMODE', 'VDAC0.OPA3_CTRL.PRSOUTMODE', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CTRL_APORTXMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CTRL_APORTXMASTERDIS, self).__init__(register,
            'APORTXMASTERDIS', 'VDAC0.OPA3_CTRL.APORTXMASTERDIS', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CTRL_APORTYMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CTRL_APORTYMASTERDIS, self).__init__(register,
            'APORTYMASTERDIS', 'VDAC0.OPA3_CTRL.APORTYMASTERDIS', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_TIMER_STARTUPDLY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_TIMER_STARTUPDLY, self).__init__(register,
            'STARTUPDLY', 'VDAC0.OPA3_TIMER.STARTUPDLY', 'read-write',
            "",
            0, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_TIMER_WARMUPTIME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_TIMER_WARMUPTIME, self).__init__(register,
            'WARMUPTIME', 'VDAC0.OPA3_TIMER.WARMUPTIME', 'read-write',
            "",
            8, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_TIMER_SETTLETIME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_TIMER_SETTLETIME, self).__init__(register,
            'SETTLETIME', 'VDAC0.OPA3_TIMER.SETTLETIME', 'read-write',
            "",
            16, 10)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_MUX_POSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_MUX_POSSEL, self).__init__(register,
            'POSSEL', 'VDAC0.OPA3_MUX.POSSEL', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_MUX_NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_MUX_NEGSEL, self).__init__(register,
            'NEGSEL', 'VDAC0.OPA3_MUX.NEGSEL', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_MUX_RESINMUX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_MUX_RESINMUX, self).__init__(register,
            'RESINMUX', 'VDAC0.OPA3_MUX.RESINMUX', 'read-write',
            "",
            16, 3,
            RM_Enum_VDAC0_OPA3_MUX_RESINMUX(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_MUX_GAIN3X(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_MUX_GAIN3X, self).__init__(register,
            'GAIN3X', 'VDAC0.OPA3_MUX.GAIN3X', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_MUX_RESSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_MUX_RESSEL, self).__init__(register,
            'RESSEL', 'VDAC0.OPA3_MUX.RESSEL', 'read-write',
            "",
            24, 3,
            RM_Enum_VDAC0_OPA3_MUX_RESSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_OUT_MAINOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_OUT_MAINOUTEN, self).__init__(register,
            'MAINOUTEN', 'VDAC0.OPA3_OUT.MAINOUTEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_OUT_ALTOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_OUT_ALTOUTEN, self).__init__(register,
            'ALTOUTEN', 'VDAC0.OPA3_OUT.ALTOUTEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_OUT_APORTOUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_OUT_APORTOUTEN, self).__init__(register,
            'APORTOUTEN', 'VDAC0.OPA3_OUT.APORTOUTEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_OUT_SHORT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_OUT_SHORT, self).__init__(register,
            'SHORT', 'VDAC0.OPA3_OUT.SHORT', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_OUT_ALTOUTPADEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_OUT_ALTOUTPADEN, self).__init__(register,
            'ALTOUTPADEN', 'VDAC0.OPA3_OUT.ALTOUTPADEN', 'read-write',
            "",
            4, 5,
            RM_Enum_VDAC0_OPA3_OUT_ALTOUTPADEN(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_OUT_APORTOUTSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_OUT_APORTOUTSEL, self).__init__(register,
            'APORTOUTSEL', 'VDAC0.OPA3_OUT.APORTOUTSEL', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CAL_CM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CAL_CM1, self).__init__(register,
            'CM1', 'VDAC0.OPA3_CAL.CM1', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CAL_CM2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CAL_CM2, self).__init__(register,
            'CM2', 'VDAC0.OPA3_CAL.CM2', 'read-write',
            "",
            5, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CAL_CM3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CAL_CM3, self).__init__(register,
            'CM3', 'VDAC0.OPA3_CAL.CM3', 'read-write',
            "",
            10, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CAL_GM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CAL_GM, self).__init__(register,
            'GM', 'VDAC0.OPA3_CAL.GM', 'read-write',
            "",
            13, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CAL_GM3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CAL_GM3, self).__init__(register,
            'GM3', 'VDAC0.OPA3_CAL.GM3', 'read-write',
            "",
            17, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CAL_OFFSETP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CAL_OFFSETP, self).__init__(register,
            'OFFSETP', 'VDAC0.OPA3_CAL.OFFSETP', 'read-write',
            "",
            20, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_VDAC0_OPA3_CAL_OFFSETN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_VDAC0_OPA3_CAL_OFFSETN, self).__init__(register,
            'OFFSETN', 'VDAC0.OPA3_CAL.OFFSETN', 'read-write',
            "",
            26, 5)
        self.__dict__['zz_frozen'] = True


