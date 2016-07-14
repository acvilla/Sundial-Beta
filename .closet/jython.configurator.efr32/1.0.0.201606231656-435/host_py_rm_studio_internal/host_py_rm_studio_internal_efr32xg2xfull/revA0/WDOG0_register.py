
from static import Base_RM_Register
from WDOG0_field import *


class RM_Register_WDOG0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_WDOG0_CTRL, self).__init__(rmio, label,
            0x40052000, 0x000,
            'CTRL', 'WDOG0.CTRL', 'read-write',
            "",
            0x00000F00, 0xC7033F7F)

        self.EN = RM_Field_WDOG0_CTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.DEBUGRUN = RM_Field_WDOG0_CTRL_DEBUGRUN(self)
        self.zz_fdict['DEBUGRUN'] = self.DEBUGRUN
        self.EM2RUN = RM_Field_WDOG0_CTRL_EM2RUN(self)
        self.zz_fdict['EM2RUN'] = self.EM2RUN
        self.EM3RUN = RM_Field_WDOG0_CTRL_EM3RUN(self)
        self.zz_fdict['EM3RUN'] = self.EM3RUN
        self.LOCK = RM_Field_WDOG0_CTRL_LOCK(self)
        self.zz_fdict['LOCK'] = self.LOCK
        self.EM4BLOCK = RM_Field_WDOG0_CTRL_EM4BLOCK(self)
        self.zz_fdict['EM4BLOCK'] = self.EM4BLOCK
        self.SWOSCBLOCK = RM_Field_WDOG0_CTRL_SWOSCBLOCK(self)
        self.zz_fdict['SWOSCBLOCK'] = self.SWOSCBLOCK
        self.PERSEL = RM_Field_WDOG0_CTRL_PERSEL(self)
        self.zz_fdict['PERSEL'] = self.PERSEL
        self.CLKSEL = RM_Field_WDOG0_CTRL_CLKSEL(self)
        self.zz_fdict['CLKSEL'] = self.CLKSEL
        self.WARNSEL = RM_Field_WDOG0_CTRL_WARNSEL(self)
        self.zz_fdict['WARNSEL'] = self.WARNSEL
        self.WINSEL = RM_Field_WDOG0_CTRL_WINSEL(self)
        self.zz_fdict['WINSEL'] = self.WINSEL
        self.CLRSRC = RM_Field_WDOG0_CTRL_CLRSRC(self)
        self.zz_fdict['CLRSRC'] = self.CLRSRC
        self.WDOGRSTDIS = RM_Field_WDOG0_CTRL_WDOGRSTDIS(self)
        self.zz_fdict['WDOGRSTDIS'] = self.WDOGRSTDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_WDOG0_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_WDOG0_CMD, self).__init__(rmio, label,
            0x40052000, 0x004,
            'CMD', 'WDOG0.CMD', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.CLEAR = RM_Field_WDOG0_CMD_CLEAR(self)
        self.zz_fdict['CLEAR'] = self.CLEAR
        self.__dict__['zz_frozen'] = True


class RM_Register_WDOG0_SYNCBUSY(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_WDOG0_SYNCBUSY, self).__init__(rmio, label,
            0x40052000, 0x008,
            'SYNCBUSY', 'WDOG0.SYNCBUSY', 'read-only',
            "",
            0x00000000, 0x0000000F)

        self.CTRL = RM_Field_WDOG0_SYNCBUSY_CTRL(self)
        self.zz_fdict['CTRL'] = self.CTRL
        self.CMD = RM_Field_WDOG0_SYNCBUSY_CMD(self)
        self.zz_fdict['CMD'] = self.CMD
        self.PCH0_PRSCTRL = RM_Field_WDOG0_SYNCBUSY_PCH0_PRSCTRL(self)
        self.zz_fdict['PCH0_PRSCTRL'] = self.PCH0_PRSCTRL
        self.PCH1_PRSCTRL = RM_Field_WDOG0_SYNCBUSY_PCH1_PRSCTRL(self)
        self.zz_fdict['PCH1_PRSCTRL'] = self.PCH1_PRSCTRL
        self.__dict__['zz_frozen'] = True


class RM_Register_WDOG0_PCH0_PRSCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_WDOG0_PCH0_PRSCTRL, self).__init__(rmio, label,
            0x40052000, 0x00C,
            'PCH0_PRSCTRL', 'WDOG0.PCH0_PRSCTRL', 'read-write',
            "",
            0x00000000, 0x0000010F)

        self.PRSSEL = RM_Field_WDOG0_PCH0_PRSCTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.PRSMISSRSTEN = RM_Field_WDOG0_PCH0_PRSCTRL_PRSMISSRSTEN(self)
        self.zz_fdict['PRSMISSRSTEN'] = self.PRSMISSRSTEN
        self.__dict__['zz_frozen'] = True


class RM_Register_WDOG0_PCH1_PRSCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_WDOG0_PCH1_PRSCTRL, self).__init__(rmio, label,
            0x40052000, 0x010,
            'PCH1_PRSCTRL', 'WDOG0.PCH1_PRSCTRL', 'read-write',
            "",
            0x00000000, 0x0000010F)

        self.PRSSEL = RM_Field_WDOG0_PCH1_PRSCTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.PRSMISSRSTEN = RM_Field_WDOG0_PCH1_PRSCTRL_PRSMISSRSTEN(self)
        self.zz_fdict['PRSMISSRSTEN'] = self.PRSMISSRSTEN
        self.__dict__['zz_frozen'] = True


class RM_Register_WDOG0_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_WDOG0_IF, self).__init__(rmio, label,
            0x40052000, 0x01C,
            'IF', 'WDOG0.IF', 'read-only',
            "",
            0x00000000, 0x0000001F)

        self.TOUT = RM_Field_WDOG0_IF_TOUT(self)
        self.zz_fdict['TOUT'] = self.TOUT
        self.WARN = RM_Field_WDOG0_IF_WARN(self)
        self.zz_fdict['WARN'] = self.WARN
        self.WIN = RM_Field_WDOG0_IF_WIN(self)
        self.zz_fdict['WIN'] = self.WIN
        self.PEM0 = RM_Field_WDOG0_IF_PEM0(self)
        self.zz_fdict['PEM0'] = self.PEM0
        self.PEM1 = RM_Field_WDOG0_IF_PEM1(self)
        self.zz_fdict['PEM1'] = self.PEM1
        self.__dict__['zz_frozen'] = True


class RM_Register_WDOG0_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_WDOG0_IFS, self).__init__(rmio, label,
            0x40052000, 0x020,
            'IFS', 'WDOG0.IFS', 'write-only',
            "",
            0x00000000, 0x0000001F)

        self.TOUT = RM_Field_WDOG0_IFS_TOUT(self)
        self.zz_fdict['TOUT'] = self.TOUT
        self.WARN = RM_Field_WDOG0_IFS_WARN(self)
        self.zz_fdict['WARN'] = self.WARN
        self.WIN = RM_Field_WDOG0_IFS_WIN(self)
        self.zz_fdict['WIN'] = self.WIN
        self.PEM0 = RM_Field_WDOG0_IFS_PEM0(self)
        self.zz_fdict['PEM0'] = self.PEM0
        self.PEM1 = RM_Field_WDOG0_IFS_PEM1(self)
        self.zz_fdict['PEM1'] = self.PEM1
        self.__dict__['zz_frozen'] = True


class RM_Register_WDOG0_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_WDOG0_IFC, self).__init__(rmio, label,
            0x40052000, 0x024,
            'IFC', 'WDOG0.IFC', 'write-only',
            "",
            0x00000000, 0x0000001F)

        self.TOUT = RM_Field_WDOG0_IFC_TOUT(self)
        self.zz_fdict['TOUT'] = self.TOUT
        self.WARN = RM_Field_WDOG0_IFC_WARN(self)
        self.zz_fdict['WARN'] = self.WARN
        self.WIN = RM_Field_WDOG0_IFC_WIN(self)
        self.zz_fdict['WIN'] = self.WIN
        self.PEM0 = RM_Field_WDOG0_IFC_PEM0(self)
        self.zz_fdict['PEM0'] = self.PEM0
        self.PEM1 = RM_Field_WDOG0_IFC_PEM1(self)
        self.zz_fdict['PEM1'] = self.PEM1
        self.__dict__['zz_frozen'] = True


class RM_Register_WDOG0_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_WDOG0_IEN, self).__init__(rmio, label,
            0x40052000, 0x028,
            'IEN', 'WDOG0.IEN', 'read-write',
            "",
            0x00000000, 0x0000001F)

        self.TOUT = RM_Field_WDOG0_IEN_TOUT(self)
        self.zz_fdict['TOUT'] = self.TOUT
        self.WARN = RM_Field_WDOG0_IEN_WARN(self)
        self.zz_fdict['WARN'] = self.WARN
        self.WIN = RM_Field_WDOG0_IEN_WIN(self)
        self.zz_fdict['WIN'] = self.WIN
        self.PEM0 = RM_Field_WDOG0_IEN_PEM0(self)
        self.zz_fdict['PEM0'] = self.PEM0
        self.PEM1 = RM_Field_WDOG0_IEN_PEM1(self)
        self.zz_fdict['PEM1'] = self.PEM1
        self.__dict__['zz_frozen'] = True


