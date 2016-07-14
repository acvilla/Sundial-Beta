
from static import Base_RM_Field
from WDOG_enum import *


class RM_Field_WDOG_CTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_CTRL_EN, self).__init__(register,
            'EN', 'WDOG.CTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_CTRL_DEBUGRUN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_CTRL_DEBUGRUN, self).__init__(register,
            'DEBUGRUN', 'WDOG.CTRL.DEBUGRUN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_CTRL_EM2RUN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_CTRL_EM2RUN, self).__init__(register,
            'EM2RUN', 'WDOG.CTRL.EM2RUN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_CTRL_EM3RUN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_CTRL_EM3RUN, self).__init__(register,
            'EM3RUN', 'WDOG.CTRL.EM3RUN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_CTRL_LOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_CTRL_LOCK, self).__init__(register,
            'LOCK', 'WDOG.CTRL.LOCK', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_CTRL_EM4BLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_CTRL_EM4BLOCK, self).__init__(register,
            'EM4BLOCK', 'WDOG.CTRL.EM4BLOCK', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_CTRL_SWOSCBLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_CTRL_SWOSCBLOCK, self).__init__(register,
            'SWOSCBLOCK', 'WDOG.CTRL.SWOSCBLOCK', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_CTRL_PERSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_CTRL_PERSEL, self).__init__(register,
            'PERSEL', 'WDOG.CTRL.PERSEL', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_CTRL_CLKSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_CTRL_CLKSEL, self).__init__(register,
            'CLKSEL', 'WDOG.CTRL.CLKSEL', 'read-write',
            "",
            12, 2,
            RM_Enum_WDOG_CTRL_CLKSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_CTRL_WARNSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_CTRL_WARNSEL, self).__init__(register,
            'WARNSEL', 'WDOG.CTRL.WARNSEL', 'read-write',
            "",
            16, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_CTRL_WINSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_CTRL_WINSEL, self).__init__(register,
            'WINSEL', 'WDOG.CTRL.WINSEL', 'read-write',
            "",
            24, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_CTRL_CLRSRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_CTRL_CLRSRC, self).__init__(register,
            'CLRSRC', 'WDOG.CTRL.CLRSRC', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_CTRL_WDOGRSTDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_CTRL_WDOGRSTDIS, self).__init__(register,
            'WDOGRSTDIS', 'WDOG.CTRL.WDOGRSTDIS', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_CMD_CLEAR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_CMD_CLEAR, self).__init__(register,
            'CLEAR', 'WDOG.CMD.CLEAR', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_SYNCBUSY_CTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_SYNCBUSY_CTRL, self).__init__(register,
            'CTRL', 'WDOG.SYNCBUSY.CTRL', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_SYNCBUSY_CMD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_SYNCBUSY_CMD, self).__init__(register,
            'CMD', 'WDOG.SYNCBUSY.CMD', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_SYNCBUSY_PCH0_PRSCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_SYNCBUSY_PCH0_PRSCTRL, self).__init__(register,
            'PCH0_PRSCTRL', 'WDOG.SYNCBUSY.PCH0_PRSCTRL', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_SYNCBUSY_PCH1_PRSCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_SYNCBUSY_PCH1_PRSCTRL, self).__init__(register,
            'PCH1_PRSCTRL', 'WDOG.SYNCBUSY.PCH1_PRSCTRL', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_PCH0_PRSCTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_PCH0_PRSCTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'WDOG.PCH0_PRSCTRL.PRSSEL', 'read-write',
            "",
            0, 4,
            RM_Enum_WDOG_PCH0_PRSCTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_PCH0_PRSCTRL_PRSMISSRSTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_PCH0_PRSCTRL_PRSMISSRSTEN, self).__init__(register,
            'PRSMISSRSTEN', 'WDOG.PCH0_PRSCTRL.PRSMISSRSTEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_PCH1_PRSCTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_PCH1_PRSCTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'WDOG.PCH1_PRSCTRL.PRSSEL', 'read-write',
            "",
            0, 4,
            RM_Enum_WDOG_PCH1_PRSCTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_PCH1_PRSCTRL_PRSMISSRSTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_PCH1_PRSCTRL_PRSMISSRSTEN, self).__init__(register,
            'PRSMISSRSTEN', 'WDOG.PCH1_PRSCTRL.PRSMISSRSTEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IF_TOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IF_TOUT, self).__init__(register,
            'TOUT', 'WDOG.IF.TOUT', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IF_WARN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IF_WARN, self).__init__(register,
            'WARN', 'WDOG.IF.WARN', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IF_WIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IF_WIN, self).__init__(register,
            'WIN', 'WDOG.IF.WIN', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IF_PEM0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IF_PEM0, self).__init__(register,
            'PEM0', 'WDOG.IF.PEM0', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IF_PEM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IF_PEM1, self).__init__(register,
            'PEM1', 'WDOG.IF.PEM1', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IFS_TOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IFS_TOUT, self).__init__(register,
            'TOUT', 'WDOG.IFS.TOUT', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IFS_WARN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IFS_WARN, self).__init__(register,
            'WARN', 'WDOG.IFS.WARN', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IFS_WIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IFS_WIN, self).__init__(register,
            'WIN', 'WDOG.IFS.WIN', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IFS_PEM0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IFS_PEM0, self).__init__(register,
            'PEM0', 'WDOG.IFS.PEM0', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IFS_PEM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IFS_PEM1, self).__init__(register,
            'PEM1', 'WDOG.IFS.PEM1', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IFC_TOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IFC_TOUT, self).__init__(register,
            'TOUT', 'WDOG.IFC.TOUT', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IFC_WARN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IFC_WARN, self).__init__(register,
            'WARN', 'WDOG.IFC.WARN', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IFC_WIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IFC_WIN, self).__init__(register,
            'WIN', 'WDOG.IFC.WIN', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IFC_PEM0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IFC_PEM0, self).__init__(register,
            'PEM0', 'WDOG.IFC.PEM0', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IFC_PEM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IFC_PEM1, self).__init__(register,
            'PEM1', 'WDOG.IFC.PEM1', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IEN_TOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IEN_TOUT, self).__init__(register,
            'TOUT', 'WDOG.IEN.TOUT', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IEN_WARN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IEN_WARN, self).__init__(register,
            'WARN', 'WDOG.IEN.WARN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IEN_WIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IEN_WIN, self).__init__(register,
            'WIN', 'WDOG.IEN.WIN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IEN_PEM0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IEN_PEM0, self).__init__(register,
            'PEM0', 'WDOG.IEN.PEM0', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_WDOG_IEN_PEM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_WDOG_IEN_PEM1, self).__init__(register,
            'PEM1', 'WDOG.IEN.PEM1', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


