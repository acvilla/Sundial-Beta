
from static import Base_RM_Field
from RMU_enum import *


class RM_Field_RMU_CTRL_WDOGRMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_CTRL_WDOGRMODE, self).__init__(register,
            'WDOGRMODE', 'RMU.CTRL.WDOGRMODE', 'read-write',
            "",
            0, 3,
            RM_Enum_RMU_CTRL_WDOGRMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_CTRL_LOCKUPRMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_CTRL_LOCKUPRMODE, self).__init__(register,
            'LOCKUPRMODE', 'RMU.CTRL.LOCKUPRMODE', 'read-write',
            "",
            4, 3,
            RM_Enum_RMU_CTRL_LOCKUPRMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_CTRL_SYSRMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_CTRL_SYSRMODE, self).__init__(register,
            'SYSRMODE', 'RMU.CTRL.SYSRMODE', 'read-write',
            "",
            8, 3,
            RM_Enum_RMU_CTRL_SYSRMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_CTRL_PINRMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_CTRL_PINRMODE, self).__init__(register,
            'PINRMODE', 'RMU.CTRL.PINRMODE', 'read-write',
            "",
            12, 3,
            RM_Enum_RMU_CTRL_PINRMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_CTRL_RESETSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_CTRL_RESETSTATE, self).__init__(register,
            'RESETSTATE', 'RMU.CTRL.RESETSTATE', 'read-write',
            "",
            24, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_CTRL_RST_CMU_HS_TO_DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_CTRL_RST_CMU_HS_TO_DIS, self).__init__(register,
            'RST_CMU_HS_TO_DIS', 'RMU.CTRL.RST_CMU_HS_TO_DIS', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_RSTCAUSE_PORST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_RSTCAUSE_PORST, self).__init__(register,
            'PORST', 'RMU.RSTCAUSE.PORST', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_RSTCAUSE_AVDDBOD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_RSTCAUSE_AVDDBOD, self).__init__(register,
            'AVDDBOD', 'RMU.RSTCAUSE.AVDDBOD', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_RSTCAUSE_DVDDBOD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_RSTCAUSE_DVDDBOD, self).__init__(register,
            'DVDDBOD', 'RMU.RSTCAUSE.DVDDBOD', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_RSTCAUSE_DECBOD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_RSTCAUSE_DECBOD, self).__init__(register,
            'DECBOD', 'RMU.RSTCAUSE.DECBOD', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_RSTCAUSE_EXTRST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_RSTCAUSE_EXTRST, self).__init__(register,
            'EXTRST', 'RMU.RSTCAUSE.EXTRST', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_RSTCAUSE_LOCKUPRST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_RSTCAUSE_LOCKUPRST, self).__init__(register,
            'LOCKUPRST', 'RMU.RSTCAUSE.LOCKUPRST', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_RSTCAUSE_SYSREQRST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_RSTCAUSE_SYSREQRST, self).__init__(register,
            'SYSREQRST', 'RMU.RSTCAUSE.SYSREQRST', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_RSTCAUSE_WDOGRST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_RSTCAUSE_WDOGRST, self).__init__(register,
            'WDOGRST', 'RMU.RSTCAUSE.WDOGRST', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_RSTCAUSE_EM4RST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_RSTCAUSE_EM4RST, self).__init__(register,
            'EM4RST', 'RMU.RSTCAUSE.EM4RST', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_RSTCAUSE_AVDDEM4BOD_N(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_RSTCAUSE_AVDDEM4BOD_N, self).__init__(register,
            'AVDDEM4BOD_N', 'RMU.RSTCAUSE.AVDDEM4BOD_N', 'read-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_RSTCAUSE_FLASHBOD_N(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_RSTCAUSE_FLASHBOD_N, self).__init__(register,
            'FLASHBOD_N', 'RMU.RSTCAUSE.FLASHBOD_N', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_RSTCAUSE_DEC1BOD_N(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_RSTCAUSE_DEC1BOD_N, self).__init__(register,
            'DEC1BOD_N', 'RMU.RSTCAUSE.DEC1BOD_N', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_CMD_RCCLR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_CMD_RCCLR, self).__init__(register,
            'RCCLR', 'RMU.CMD.RCCLR', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_RST_RADIORST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_RST_RADIORST, self).__init__(register,
            'RADIORST', 'RMU.RST.RADIORST', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_RST_LFRST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_RST_LFRST, self).__init__(register,
            'LFRST', 'RMU.RST.LFRST', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RMU_LOCK_LOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RMU_LOCK_LOCKKEY, self).__init__(register,
            'LOCKKEY', 'RMU.LOCK.LOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_RMU_LOCK_LOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


