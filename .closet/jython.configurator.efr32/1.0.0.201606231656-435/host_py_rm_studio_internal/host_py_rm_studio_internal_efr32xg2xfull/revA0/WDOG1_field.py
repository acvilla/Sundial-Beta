
from static import Base_RM_Field
from WDOG1_enum import *


class RM_Field_WDOG1_CTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_CTRL_EN, self).__init__(register,
            'EN', 'WDOG1.CTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_CTRL_DEBUGRUN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_CTRL_DEBUGRUN, self).__init__(register,
            'DEBUGRUN', 'WDOG1.CTRL.DEBUGRUN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_CTRL_EM2RUN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_CTRL_EM2RUN, self).__init__(register,
            'EM2RUN', 'WDOG1.CTRL.EM2RUN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_CTRL_EM3RUN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_CTRL_EM3RUN, self).__init__(register,
            'EM3RUN', 'WDOG1.CTRL.EM3RUN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_CTRL_LOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_CTRL_LOCK, self).__init__(register,
            'LOCK', 'WDOG1.CTRL.LOCK', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_CTRL_EM4BLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_CTRL_EM4BLOCK, self).__init__(register,
            'EM4BLOCK', 'WDOG1.CTRL.EM4BLOCK', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_CTRL_SWOSCBLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_CTRL_SWOSCBLOCK, self).__init__(register,
            'SWOSCBLOCK', 'WDOG1.CTRL.SWOSCBLOCK', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_CTRL_PERSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_CTRL_PERSEL, self).__init__(register,
            'PERSEL', 'WDOG1.CTRL.PERSEL', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_CTRL_CLKSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_CTRL_CLKSEL, self).__init__(register,
            'CLKSEL', 'WDOG1.CTRL.CLKSEL', 'read-write',
            "",
            12, 2,
            RM_Enum_WDOG1_CTRL_CLKSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_CTRL_WARNSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_CTRL_WARNSEL, self).__init__(register,
            'WARNSEL', 'WDOG1.CTRL.WARNSEL', 'read-write',
            "",
            16, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_CTRL_WINSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_CTRL_WINSEL, self).__init__(register,
            'WINSEL', 'WDOG1.CTRL.WINSEL', 'read-write',
            "",
            24, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_CTRL_CLRSRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_CTRL_CLRSRC, self).__init__(register,
            'CLRSRC', 'WDOG1.CTRL.CLRSRC', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_CTRL_WDOGRSTDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_CTRL_WDOGRSTDIS, self).__init__(register,
            'WDOGRSTDIS', 'WDOG1.CTRL.WDOGRSTDIS', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_CMD_CLEAR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_CMD_CLEAR, self).__init__(register,
            'CLEAR', 'WDOG1.CMD.CLEAR', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_SYNCBUSY_CTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_SYNCBUSY_CTRL, self).__init__(register,
            'CTRL', 'WDOG1.SYNCBUSY.CTRL', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_SYNCBUSY_CMD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_SYNCBUSY_CMD, self).__init__(register,
            'CMD', 'WDOG1.SYNCBUSY.CMD', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_SYNCBUSY_PCH0_PRSCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_SYNCBUSY_PCH0_PRSCTRL, self).__init__(register,
            'PCH0_PRSCTRL', 'WDOG1.SYNCBUSY.PCH0_PRSCTRL', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_SYNCBUSY_PCH1_PRSCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_SYNCBUSY_PCH1_PRSCTRL, self).__init__(register,
            'PCH1_PRSCTRL', 'WDOG1.SYNCBUSY.PCH1_PRSCTRL', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_PCH0_PRSCTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_PCH0_PRSCTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'WDOG1.PCH0_PRSCTRL.PRSSEL', 'read-write',
            "",
            0, 4,
            RM_Enum_WDOG1_PCH0_PRSCTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_PCH0_PRSCTRL_PRSMISSRSTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_PCH0_PRSCTRL_PRSMISSRSTEN, self).__init__(register,
            'PRSMISSRSTEN', 'WDOG1.PCH0_PRSCTRL.PRSMISSRSTEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_PCH1_PRSCTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_PCH1_PRSCTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'WDOG1.PCH1_PRSCTRL.PRSSEL', 'read-write',
            "",
            0, 4,
            RM_Enum_WDOG1_PCH1_PRSCTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_PCH1_PRSCTRL_PRSMISSRSTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_PCH1_PRSCTRL_PRSMISSRSTEN, self).__init__(register,
            'PRSMISSRSTEN', 'WDOG1.PCH1_PRSCTRL.PRSMISSRSTEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IF_TOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IF_TOUT, self).__init__(register,
            'TOUT', 'WDOG1.IF.TOUT', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IF_WARN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IF_WARN, self).__init__(register,
            'WARN', 'WDOG1.IF.WARN', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IF_WIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IF_WIN, self).__init__(register,
            'WIN', 'WDOG1.IF.WIN', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IF_PEM0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IF_PEM0, self).__init__(register,
            'PEM0', 'WDOG1.IF.PEM0', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IF_PEM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IF_PEM1, self).__init__(register,
            'PEM1', 'WDOG1.IF.PEM1', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IFS_TOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IFS_TOUT, self).__init__(register,
            'TOUT', 'WDOG1.IFS.TOUT', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IFS_WARN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IFS_WARN, self).__init__(register,
            'WARN', 'WDOG1.IFS.WARN', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IFS_WIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IFS_WIN, self).__init__(register,
            'WIN', 'WDOG1.IFS.WIN', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IFS_PEM0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IFS_PEM0, self).__init__(register,
            'PEM0', 'WDOG1.IFS.PEM0', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IFS_PEM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IFS_PEM1, self).__init__(register,
            'PEM1', 'WDOG1.IFS.PEM1', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IFC_TOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IFC_TOUT, self).__init__(register,
            'TOUT', 'WDOG1.IFC.TOUT', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IFC_WARN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IFC_WARN, self).__init__(register,
            'WARN', 'WDOG1.IFC.WARN', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IFC_WIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IFC_WIN, self).__init__(register,
            'WIN', 'WDOG1.IFC.WIN', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IFC_PEM0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IFC_PEM0, self).__init__(register,
            'PEM0', 'WDOG1.IFC.PEM0', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IFC_PEM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IFC_PEM1, self).__init__(register,
            'PEM1', 'WDOG1.IFC.PEM1', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IEN_TOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IEN_TOUT, self).__init__(register,
            'TOUT', 'WDOG1.IEN.TOUT', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IEN_WARN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IEN_WARN, self).__init__(register,
            'WARN', 'WDOG1.IEN.WARN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IEN_WIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IEN_WIN, self).__init__(register,
            'WIN', 'WDOG1.IEN.WIN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IEN_PEM0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IEN_PEM0, self).__init__(register,
            'PEM0', 'WDOG1.IEN.PEM0', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG1_IEN_PEM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG1_IEN_PEM1, self).__init__(register,
            'PEM1', 'WDOG1.IEN.PEM1', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


