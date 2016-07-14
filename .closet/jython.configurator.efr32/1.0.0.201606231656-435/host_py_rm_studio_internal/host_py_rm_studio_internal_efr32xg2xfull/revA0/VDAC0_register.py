
from static import Base_RM_Register
from VDAC0_field import *


class RM_Register_VDAC0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_CTRL, self).__init__(rmio, label,
            0x40008000, 0x000,
            'CTRL', 'VDAC0.CTRL', 'read-write',
            "",
            0x00000000, 0x937F0771)

        self.DIFF = RM_Field_VDAC0_CTRL_DIFF(self)
        self.zz_fdict['DIFF'] = self.DIFF
        self.SINEMODE = RM_Field_VDAC0_CTRL_SINEMODE(self)
        self.zz_fdict['SINEMODE'] = self.SINEMODE
        self.OUTENPRS = RM_Field_VDAC0_CTRL_OUTENPRS(self)
        self.zz_fdict['OUTENPRS'] = self.OUTENPRS
        self.CH0PRESCRST = RM_Field_VDAC0_CTRL_CH0PRESCRST(self)
        self.zz_fdict['CH0PRESCRST'] = self.CH0PRESCRST
        self.REFSEL = RM_Field_VDAC0_CTRL_REFSEL(self)
        self.zz_fdict['REFSEL'] = self.REFSEL
        self.PRESC = RM_Field_VDAC0_CTRL_PRESC(self)
        self.zz_fdict['PRESC'] = self.PRESC
        self.REFRESHPERIOD = RM_Field_VDAC0_CTRL_REFRESHPERIOD(self)
        self.zz_fdict['REFRESHPERIOD'] = self.REFRESHPERIOD
        self.WARMUPMODE = RM_Field_VDAC0_CTRL_WARMUPMODE(self)
        self.zz_fdict['WARMUPMODE'] = self.WARMUPMODE
        self.DACCLKMODE = RM_Field_VDAC0_CTRL_DACCLKMODE(self)
        self.zz_fdict['DACCLKMODE'] = self.DACCLKMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_STATUS, self).__init__(rmio, label,
            0x40008000, 0x004,
            'STATUS', 'VDAC0.STATUS', 'read-only',
            "",
            0x0000000C, 0x7777003F)

        self.CH0ENS = RM_Field_VDAC0_STATUS_CH0ENS(self)
        self.zz_fdict['CH0ENS'] = self.CH0ENS
        self.CH1ENS = RM_Field_VDAC0_STATUS_CH1ENS(self)
        self.zz_fdict['CH1ENS'] = self.CH1ENS
        self.CH0BL = RM_Field_VDAC0_STATUS_CH0BL(self)
        self.zz_fdict['CH0BL'] = self.CH0BL
        self.CH1BL = RM_Field_VDAC0_STATUS_CH1BL(self)
        self.zz_fdict['CH1BL'] = self.CH1BL
        self.CH0WARM = RM_Field_VDAC0_STATUS_CH0WARM(self)
        self.zz_fdict['CH0WARM'] = self.CH0WARM
        self.CH1WARM = RM_Field_VDAC0_STATUS_CH1WARM(self)
        self.zz_fdict['CH1WARM'] = self.CH1WARM
        self.OPA0APORTCONFLICT = RM_Field_VDAC0_STATUS_OPA0APORTCONFLICT(self)
        self.zz_fdict['OPA0APORTCONFLICT'] = self.OPA0APORTCONFLICT
        self.OPA1APORTCONFLICT = RM_Field_VDAC0_STATUS_OPA1APORTCONFLICT(self)
        self.zz_fdict['OPA1APORTCONFLICT'] = self.OPA1APORTCONFLICT
        self.OPA2APORTCONFLICT = RM_Field_VDAC0_STATUS_OPA2APORTCONFLICT(self)
        self.zz_fdict['OPA2APORTCONFLICT'] = self.OPA2APORTCONFLICT
        self.OPA0ENS = RM_Field_VDAC0_STATUS_OPA0ENS(self)
        self.zz_fdict['OPA0ENS'] = self.OPA0ENS
        self.OPA1ENS = RM_Field_VDAC0_STATUS_OPA1ENS(self)
        self.zz_fdict['OPA1ENS'] = self.OPA1ENS
        self.OPA2ENS = RM_Field_VDAC0_STATUS_OPA2ENS(self)
        self.zz_fdict['OPA2ENS'] = self.OPA2ENS
        self.OPA0WARM = RM_Field_VDAC0_STATUS_OPA0WARM(self)
        self.zz_fdict['OPA0WARM'] = self.OPA0WARM
        self.OPA1WARM = RM_Field_VDAC0_STATUS_OPA1WARM(self)
        self.zz_fdict['OPA1WARM'] = self.OPA1WARM
        self.OPA2WARM = RM_Field_VDAC0_STATUS_OPA2WARM(self)
        self.zz_fdict['OPA2WARM'] = self.OPA2WARM
        self.OPA0OUTVALID = RM_Field_VDAC0_STATUS_OPA0OUTVALID(self)
        self.zz_fdict['OPA0OUTVALID'] = self.OPA0OUTVALID
        self.OPA1OUTVALID = RM_Field_VDAC0_STATUS_OPA1OUTVALID(self)
        self.zz_fdict['OPA1OUTVALID'] = self.OPA1OUTVALID
        self.OPA2OUTVALID = RM_Field_VDAC0_STATUS_OPA2OUTVALID(self)
        self.zz_fdict['OPA2OUTVALID'] = self.OPA2OUTVALID
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_CH0CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_CH0CTRL, self).__init__(rmio, label,
            0x40008000, 0x008,
            'CH0CTRL', 'VDAC0.CH0CTRL', 'read-write',
            "",
            0x00000000, 0x0000F171)

        self.CONVMODE = RM_Field_VDAC0_CH0CTRL_CONVMODE(self)
        self.zz_fdict['CONVMODE'] = self.CONVMODE
        self.TRIGMODE = RM_Field_VDAC0_CH0CTRL_TRIGMODE(self)
        self.zz_fdict['TRIGMODE'] = self.TRIGMODE
        self.PRSASYNC = RM_Field_VDAC0_CH0CTRL_PRSASYNC(self)
        self.zz_fdict['PRSASYNC'] = self.PRSASYNC
        self.PRSSEL = RM_Field_VDAC0_CH0CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_CH1CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_CH1CTRL, self).__init__(rmio, label,
            0x40008000, 0x00C,
            'CH1CTRL', 'VDAC0.CH1CTRL', 'read-write',
            "",
            0x00000000, 0x0000F171)

        self.CONVMODE = RM_Field_VDAC0_CH1CTRL_CONVMODE(self)
        self.zz_fdict['CONVMODE'] = self.CONVMODE
        self.TRIGMODE = RM_Field_VDAC0_CH1CTRL_TRIGMODE(self)
        self.zz_fdict['TRIGMODE'] = self.TRIGMODE
        self.PRSASYNC = RM_Field_VDAC0_CH1CTRL_PRSASYNC(self)
        self.zz_fdict['PRSASYNC'] = self.PRSASYNC
        self.PRSSEL = RM_Field_VDAC0_CH1CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_CMD, self).__init__(rmio, label,
            0x40008000, 0x010,
            'CMD', 'VDAC0.CMD', 'write-only',
            "",
            0x00000000, 0x003F000F)

        self.CH0EN = RM_Field_VDAC0_CMD_CH0EN(self)
        self.zz_fdict['CH0EN'] = self.CH0EN
        self.CH0DIS = RM_Field_VDAC0_CMD_CH0DIS(self)
        self.zz_fdict['CH0DIS'] = self.CH0DIS
        self.CH1EN = RM_Field_VDAC0_CMD_CH1EN(self)
        self.zz_fdict['CH1EN'] = self.CH1EN
        self.CH1DIS = RM_Field_VDAC0_CMD_CH1DIS(self)
        self.zz_fdict['CH1DIS'] = self.CH1DIS
        self.OPA0EN = RM_Field_VDAC0_CMD_OPA0EN(self)
        self.zz_fdict['OPA0EN'] = self.OPA0EN
        self.OPA0DIS = RM_Field_VDAC0_CMD_OPA0DIS(self)
        self.zz_fdict['OPA0DIS'] = self.OPA0DIS
        self.OPA1EN = RM_Field_VDAC0_CMD_OPA1EN(self)
        self.zz_fdict['OPA1EN'] = self.OPA1EN
        self.OPA1DIS = RM_Field_VDAC0_CMD_OPA1DIS(self)
        self.zz_fdict['OPA1DIS'] = self.OPA1DIS
        self.OPA2EN = RM_Field_VDAC0_CMD_OPA2EN(self)
        self.zz_fdict['OPA2EN'] = self.OPA2EN
        self.OPA2DIS = RM_Field_VDAC0_CMD_OPA2DIS(self)
        self.zz_fdict['OPA2DIS'] = self.OPA2DIS
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_IF, self).__init__(rmio, label,
            0x40008000, 0x014,
            'IF', 'VDAC0.IF', 'read-only',
            "",
            0x000000C0, 0x707780FF)

        self.CH0CD = RM_Field_VDAC0_IF_CH0CD(self)
        self.zz_fdict['CH0CD'] = self.CH0CD
        self.CH1CD = RM_Field_VDAC0_IF_CH1CD(self)
        self.zz_fdict['CH1CD'] = self.CH1CD
        self.CH0OF = RM_Field_VDAC0_IF_CH0OF(self)
        self.zz_fdict['CH0OF'] = self.CH0OF
        self.CH1OF = RM_Field_VDAC0_IF_CH1OF(self)
        self.zz_fdict['CH1OF'] = self.CH1OF
        self.CH0UF = RM_Field_VDAC0_IF_CH0UF(self)
        self.zz_fdict['CH0UF'] = self.CH0UF
        self.CH1UF = RM_Field_VDAC0_IF_CH1UF(self)
        self.zz_fdict['CH1UF'] = self.CH1UF
        self.CH0BL = RM_Field_VDAC0_IF_CH0BL(self)
        self.zz_fdict['CH0BL'] = self.CH0BL
        self.CH1BL = RM_Field_VDAC0_IF_CH1BL(self)
        self.zz_fdict['CH1BL'] = self.CH1BL
        self.EM23ERR = RM_Field_VDAC0_IF_EM23ERR(self)
        self.zz_fdict['EM23ERR'] = self.EM23ERR
        self.OPA0APORTCONFLICT = RM_Field_VDAC0_IF_OPA0APORTCONFLICT(self)
        self.zz_fdict['OPA0APORTCONFLICT'] = self.OPA0APORTCONFLICT
        self.OPA1APORTCONFLICT = RM_Field_VDAC0_IF_OPA1APORTCONFLICT(self)
        self.zz_fdict['OPA1APORTCONFLICT'] = self.OPA1APORTCONFLICT
        self.OPA2APORTCONFLICT = RM_Field_VDAC0_IF_OPA2APORTCONFLICT(self)
        self.zz_fdict['OPA2APORTCONFLICT'] = self.OPA2APORTCONFLICT
        self.OPA0PRSTIMEDERR = RM_Field_VDAC0_IF_OPA0PRSTIMEDERR(self)
        self.zz_fdict['OPA0PRSTIMEDERR'] = self.OPA0PRSTIMEDERR
        self.OPA1PRSTIMEDERR = RM_Field_VDAC0_IF_OPA1PRSTIMEDERR(self)
        self.zz_fdict['OPA1PRSTIMEDERR'] = self.OPA1PRSTIMEDERR
        self.OPA2PRSTIMEDERR = RM_Field_VDAC0_IF_OPA2PRSTIMEDERR(self)
        self.zz_fdict['OPA2PRSTIMEDERR'] = self.OPA2PRSTIMEDERR
        self.OPA0OUTVALID = RM_Field_VDAC0_IF_OPA0OUTVALID(self)
        self.zz_fdict['OPA0OUTVALID'] = self.OPA0OUTVALID
        self.OPA1OUTVALID = RM_Field_VDAC0_IF_OPA1OUTVALID(self)
        self.zz_fdict['OPA1OUTVALID'] = self.OPA1OUTVALID
        self.OPA2OUTVALID = RM_Field_VDAC0_IF_OPA2OUTVALID(self)
        self.zz_fdict['OPA2OUTVALID'] = self.OPA2OUTVALID
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_IFS, self).__init__(rmio, label,
            0x40008000, 0x018,
            'IFS', 'VDAC0.IFS', 'write-only',
            "",
            0x00000000, 0x7077803F)

        self.CH0CD = RM_Field_VDAC0_IFS_CH0CD(self)
        self.zz_fdict['CH0CD'] = self.CH0CD
        self.CH1CD = RM_Field_VDAC0_IFS_CH1CD(self)
        self.zz_fdict['CH1CD'] = self.CH1CD
        self.CH0OF = RM_Field_VDAC0_IFS_CH0OF(self)
        self.zz_fdict['CH0OF'] = self.CH0OF
        self.CH1OF = RM_Field_VDAC0_IFS_CH1OF(self)
        self.zz_fdict['CH1OF'] = self.CH1OF
        self.CH0UF = RM_Field_VDAC0_IFS_CH0UF(self)
        self.zz_fdict['CH0UF'] = self.CH0UF
        self.CH1UF = RM_Field_VDAC0_IFS_CH1UF(self)
        self.zz_fdict['CH1UF'] = self.CH1UF
        self.EM23ERR = RM_Field_VDAC0_IFS_EM23ERR(self)
        self.zz_fdict['EM23ERR'] = self.EM23ERR
        self.OPA0APORTCONFLICT = RM_Field_VDAC0_IFS_OPA0APORTCONFLICT(self)
        self.zz_fdict['OPA0APORTCONFLICT'] = self.OPA0APORTCONFLICT
        self.OPA1APORTCONFLICT = RM_Field_VDAC0_IFS_OPA1APORTCONFLICT(self)
        self.zz_fdict['OPA1APORTCONFLICT'] = self.OPA1APORTCONFLICT
        self.OPA2APORTCONFLICT = RM_Field_VDAC0_IFS_OPA2APORTCONFLICT(self)
        self.zz_fdict['OPA2APORTCONFLICT'] = self.OPA2APORTCONFLICT
        self.OPA0PRSTIMEDERR = RM_Field_VDAC0_IFS_OPA0PRSTIMEDERR(self)
        self.zz_fdict['OPA0PRSTIMEDERR'] = self.OPA0PRSTIMEDERR
        self.OPA1PRSTIMEDERR = RM_Field_VDAC0_IFS_OPA1PRSTIMEDERR(self)
        self.zz_fdict['OPA1PRSTIMEDERR'] = self.OPA1PRSTIMEDERR
        self.OPA2PRSTIMEDERR = RM_Field_VDAC0_IFS_OPA2PRSTIMEDERR(self)
        self.zz_fdict['OPA2PRSTIMEDERR'] = self.OPA2PRSTIMEDERR
        self.OPA0OUTVALID = RM_Field_VDAC0_IFS_OPA0OUTVALID(self)
        self.zz_fdict['OPA0OUTVALID'] = self.OPA0OUTVALID
        self.OPA1OUTVALID = RM_Field_VDAC0_IFS_OPA1OUTVALID(self)
        self.zz_fdict['OPA1OUTVALID'] = self.OPA1OUTVALID
        self.OPA2OUTVALID = RM_Field_VDAC0_IFS_OPA2OUTVALID(self)
        self.zz_fdict['OPA2OUTVALID'] = self.OPA2OUTVALID
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_IFC, self).__init__(rmio, label,
            0x40008000, 0x01C,
            'IFC', 'VDAC0.IFC', 'write-only',
            "",
            0x00000000, 0x7077803F)

        self.CH0CD = RM_Field_VDAC0_IFC_CH0CD(self)
        self.zz_fdict['CH0CD'] = self.CH0CD
        self.CH1CD = RM_Field_VDAC0_IFC_CH1CD(self)
        self.zz_fdict['CH1CD'] = self.CH1CD
        self.CH0OF = RM_Field_VDAC0_IFC_CH0OF(self)
        self.zz_fdict['CH0OF'] = self.CH0OF
        self.CH1OF = RM_Field_VDAC0_IFC_CH1OF(self)
        self.zz_fdict['CH1OF'] = self.CH1OF
        self.CH0UF = RM_Field_VDAC0_IFC_CH0UF(self)
        self.zz_fdict['CH0UF'] = self.CH0UF
        self.CH1UF = RM_Field_VDAC0_IFC_CH1UF(self)
        self.zz_fdict['CH1UF'] = self.CH1UF
        self.EM23ERR = RM_Field_VDAC0_IFC_EM23ERR(self)
        self.zz_fdict['EM23ERR'] = self.EM23ERR
        self.OPA0APORTCONFLICT = RM_Field_VDAC0_IFC_OPA0APORTCONFLICT(self)
        self.zz_fdict['OPA0APORTCONFLICT'] = self.OPA0APORTCONFLICT
        self.OPA1APORTCONFLICT = RM_Field_VDAC0_IFC_OPA1APORTCONFLICT(self)
        self.zz_fdict['OPA1APORTCONFLICT'] = self.OPA1APORTCONFLICT
        self.OPA2APORTCONFLICT = RM_Field_VDAC0_IFC_OPA2APORTCONFLICT(self)
        self.zz_fdict['OPA2APORTCONFLICT'] = self.OPA2APORTCONFLICT
        self.OPA0PRSTIMEDERR = RM_Field_VDAC0_IFC_OPA0PRSTIMEDERR(self)
        self.zz_fdict['OPA0PRSTIMEDERR'] = self.OPA0PRSTIMEDERR
        self.OPA1PRSTIMEDERR = RM_Field_VDAC0_IFC_OPA1PRSTIMEDERR(self)
        self.zz_fdict['OPA1PRSTIMEDERR'] = self.OPA1PRSTIMEDERR
        self.OPA2PRSTIMEDERR = RM_Field_VDAC0_IFC_OPA2PRSTIMEDERR(self)
        self.zz_fdict['OPA2PRSTIMEDERR'] = self.OPA2PRSTIMEDERR
        self.OPA0OUTVALID = RM_Field_VDAC0_IFC_OPA0OUTVALID(self)
        self.zz_fdict['OPA0OUTVALID'] = self.OPA0OUTVALID
        self.OPA1OUTVALID = RM_Field_VDAC0_IFC_OPA1OUTVALID(self)
        self.zz_fdict['OPA1OUTVALID'] = self.OPA1OUTVALID
        self.OPA2OUTVALID = RM_Field_VDAC0_IFC_OPA2OUTVALID(self)
        self.zz_fdict['OPA2OUTVALID'] = self.OPA2OUTVALID
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_IEN, self).__init__(rmio, label,
            0x40008000, 0x020,
            'IEN', 'VDAC0.IEN', 'read-write',
            "",
            0x00000000, 0x707780FF)

        self.CH0CD = RM_Field_VDAC0_IEN_CH0CD(self)
        self.zz_fdict['CH0CD'] = self.CH0CD
        self.CH1CD = RM_Field_VDAC0_IEN_CH1CD(self)
        self.zz_fdict['CH1CD'] = self.CH1CD
        self.CH0OF = RM_Field_VDAC0_IEN_CH0OF(self)
        self.zz_fdict['CH0OF'] = self.CH0OF
        self.CH1OF = RM_Field_VDAC0_IEN_CH1OF(self)
        self.zz_fdict['CH1OF'] = self.CH1OF
        self.CH0UF = RM_Field_VDAC0_IEN_CH0UF(self)
        self.zz_fdict['CH0UF'] = self.CH0UF
        self.CH1UF = RM_Field_VDAC0_IEN_CH1UF(self)
        self.zz_fdict['CH1UF'] = self.CH1UF
        self.CH0BL = RM_Field_VDAC0_IEN_CH0BL(self)
        self.zz_fdict['CH0BL'] = self.CH0BL
        self.CH1BL = RM_Field_VDAC0_IEN_CH1BL(self)
        self.zz_fdict['CH1BL'] = self.CH1BL
        self.EM23ERR = RM_Field_VDAC0_IEN_EM23ERR(self)
        self.zz_fdict['EM23ERR'] = self.EM23ERR
        self.OPA0APORTCONFLICT = RM_Field_VDAC0_IEN_OPA0APORTCONFLICT(self)
        self.zz_fdict['OPA0APORTCONFLICT'] = self.OPA0APORTCONFLICT
        self.OPA1APORTCONFLICT = RM_Field_VDAC0_IEN_OPA1APORTCONFLICT(self)
        self.zz_fdict['OPA1APORTCONFLICT'] = self.OPA1APORTCONFLICT
        self.OPA2APORTCONFLICT = RM_Field_VDAC0_IEN_OPA2APORTCONFLICT(self)
        self.zz_fdict['OPA2APORTCONFLICT'] = self.OPA2APORTCONFLICT
        self.OPA0PRSTIMEDERR = RM_Field_VDAC0_IEN_OPA0PRSTIMEDERR(self)
        self.zz_fdict['OPA0PRSTIMEDERR'] = self.OPA0PRSTIMEDERR
        self.OPA1PRSTIMEDERR = RM_Field_VDAC0_IEN_OPA1PRSTIMEDERR(self)
        self.zz_fdict['OPA1PRSTIMEDERR'] = self.OPA1PRSTIMEDERR
        self.OPA2PRSTIMEDERR = RM_Field_VDAC0_IEN_OPA2PRSTIMEDERR(self)
        self.zz_fdict['OPA2PRSTIMEDERR'] = self.OPA2PRSTIMEDERR
        self.OPA0OUTVALID = RM_Field_VDAC0_IEN_OPA0OUTVALID(self)
        self.zz_fdict['OPA0OUTVALID'] = self.OPA0OUTVALID
        self.OPA1OUTVALID = RM_Field_VDAC0_IEN_OPA1OUTVALID(self)
        self.zz_fdict['OPA1OUTVALID'] = self.OPA1OUTVALID
        self.OPA2OUTVALID = RM_Field_VDAC0_IEN_OPA2OUTVALID(self)
        self.zz_fdict['OPA2OUTVALID'] = self.OPA2OUTVALID
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_CH0DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_CH0DATA, self).__init__(rmio, label,
            0x40008000, 0x024,
            'CH0DATA', 'VDAC0.CH0DATA', 'read-write',
            "",
            0x00000800, 0x00000FFF)

        self.DATA = RM_Field_VDAC0_CH0DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_CH1DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_CH1DATA, self).__init__(rmio, label,
            0x40008000, 0x028,
            'CH1DATA', 'VDAC0.CH1DATA', 'read-write',
            "",
            0x00000800, 0x00000FFF)

        self.DATA = RM_Field_VDAC0_CH1DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_COMBDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_COMBDATA, self).__init__(rmio, label,
            0x40008000, 0x02C,
            'COMBDATA', 'VDAC0.COMBDATA', 'read-write',
            "",
            0x08000800, 0x0FFF0FFF)

        self.CH0DATA = RM_Field_VDAC0_COMBDATA_CH0DATA(self)
        self.zz_fdict['CH0DATA'] = self.CH0DATA
        self.CH1DATA = RM_Field_VDAC0_COMBDATA_CH1DATA(self)
        self.zz_fdict['CH1DATA'] = self.CH1DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_CAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_CAL, self).__init__(rmio, label,
            0x40008000, 0x030,
            'CAL', 'VDAC0.CAL', 'read-write',
            "",
            0x00082004, 0x000F3F07)

        self.OFFSETTRIM = RM_Field_VDAC0_CAL_OFFSETTRIM(self)
        self.zz_fdict['OFFSETTRIM'] = self.OFFSETTRIM
        self.GAINERRTRIM = RM_Field_VDAC0_CAL_GAINERRTRIM(self)
        self.zz_fdict['GAINERRTRIM'] = self.GAINERRTRIM
        self.GAINERRTRIMCH1 = RM_Field_VDAC0_CAL_GAINERRTRIMCH1(self)
        self.zz_fdict['GAINERRTRIMCH1'] = self.GAINERRTRIMCH1
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_DBGCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_DBGCTRL, self).__init__(rmio, label,
            0x40008000, 0x040,
            'DBGCTRL', 'VDAC0.DBGCTRL', 'read-write',
            "",
            0x00000000, 0x0000011D)

        self.FORCEBIAS = RM_Field_VDAC0_DBGCTRL_FORCEBIAS(self)
        self.zz_fdict['FORCEBIAS'] = self.FORCEBIAS
        self.REFRESHRATE = RM_Field_VDAC0_DBGCTRL_REFRESHRATE(self)
        self.zz_fdict['REFRESHRATE'] = self.REFRESHRATE
        self.STARTUPBOOSTDIS = RM_Field_VDAC0_DBGCTRL_STARTUPBOOSTDIS(self)
        self.zz_fdict['STARTUPBOOSTDIS'] = self.STARTUPBOOSTDIS
        self.FORCEEMUOSC = RM_Field_VDAC0_DBGCTRL_FORCEEMUOSC(self)
        self.zz_fdict['FORCEEMUOSC'] = self.FORCEEMUOSC
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_BIASPROG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_BIASPROG, self).__init__(rmio, label,
            0x40008000, 0x044,
            'BIASPROG', 'VDAC0.BIASPROG', 'read-write',
            "",
            0x00000001, 0x00000001)

        self.GPBIASACC = RM_Field_VDAC0_BIASPROG_GPBIASACC(self)
        self.zz_fdict['GPBIASACC'] = self.GPBIASACC
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_REFENTIME(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_REFENTIME, self).__init__(rmio, label,
            0x40008000, 0x048,
            'REFENTIME', 'VDAC0.REFENTIME', 'read-write',
            "",
            0x00000901, 0x00001F1F)

        self.BGRREQTIME = RM_Field_VDAC0_REFENTIME_BGRREQTIME(self)
        self.zz_fdict['BGRREQTIME'] = self.BGRREQTIME
        self.EM2REFTIME = RM_Field_VDAC0_REFENTIME_EM2REFTIME(self)
        self.zz_fdict['EM2REFTIME'] = self.EM2REFTIME
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_TEST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_TEST, self).__init__(rmio, label,
            0x40008000, 0x04C,
            'TEST', 'VDAC0.TEST', 'read-write',
            "",
            0x00000000, 0x00FF0001)

        self.DACFORCEEN = RM_Field_VDAC0_TEST_DACFORCEEN(self)
        self.zz_fdict['DACFORCEEN'] = self.DACFORCEEN
        self.OPA0FORCEEN = RM_Field_VDAC0_TEST_OPA0FORCEEN(self)
        self.zz_fdict['OPA0FORCEEN'] = self.OPA0FORCEEN
        self.OPA1FORCEEN = RM_Field_VDAC0_TEST_OPA1FORCEEN(self)
        self.zz_fdict['OPA1FORCEEN'] = self.OPA1FORCEEN
        self.OPA2FORCEEN = RM_Field_VDAC0_TEST_OPA2FORCEEN(self)
        self.zz_fdict['OPA2FORCEEN'] = self.OPA2FORCEEN
        self.OPA3FORCEEN = RM_Field_VDAC0_TEST_OPA3FORCEEN(self)
        self.zz_fdict['OPA3FORCEEN'] = self.OPA3FORCEEN
        self.OPA0FORCEOUTEN = RM_Field_VDAC0_TEST_OPA0FORCEOUTEN(self)
        self.zz_fdict['OPA0FORCEOUTEN'] = self.OPA0FORCEOUTEN
        self.OPA1FORCEOUTEN = RM_Field_VDAC0_TEST_OPA1FORCEOUTEN(self)
        self.zz_fdict['OPA1FORCEOUTEN'] = self.OPA1FORCEOUTEN
        self.OPA2FORCEOUTEN = RM_Field_VDAC0_TEST_OPA2FORCEOUTEN(self)
        self.zz_fdict['OPA2FORCEOUTEN'] = self.OPA2FORCEOUTEN
        self.OPA3FORCEOUTEN = RM_Field_VDAC0_TEST_OPA3FORCEOUTEN(self)
        self.zz_fdict['OPA3FORCEOUTEN'] = self.OPA3FORCEOUTEN
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPAPRESC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPAPRESC, self).__init__(rmio, label,
            0x40008000, 0x050,
            'OPAPRESC', 'VDAC0.OPAPRESC', 'read-write',
            "",
            0x0000000B, 0x0000000F)

        self.PRESC = RM_Field_VDAC0_OPAPRESC_PRESC(self)
        self.zz_fdict['PRESC'] = self.PRESC
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA0_APORTREQ(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA0_APORTREQ, self).__init__(rmio, label,
            0x40008000, 0x0A0,
            'OPA0_APORTREQ', 'VDAC0.OPA0_APORTREQ', 'read-only',
            "",
            0x00000000, 0x000003FC)

        self.APORT1XREQ = RM_Field_VDAC0_OPA0_APORTREQ_APORT1XREQ(self)
        self.zz_fdict['APORT1XREQ'] = self.APORT1XREQ
        self.APORT1YREQ = RM_Field_VDAC0_OPA0_APORTREQ_APORT1YREQ(self)
        self.zz_fdict['APORT1YREQ'] = self.APORT1YREQ
        self.APORT2XREQ = RM_Field_VDAC0_OPA0_APORTREQ_APORT2XREQ(self)
        self.zz_fdict['APORT2XREQ'] = self.APORT2XREQ
        self.APORT2YREQ = RM_Field_VDAC0_OPA0_APORTREQ_APORT2YREQ(self)
        self.zz_fdict['APORT2YREQ'] = self.APORT2YREQ
        self.APORT3XREQ = RM_Field_VDAC0_OPA0_APORTREQ_APORT3XREQ(self)
        self.zz_fdict['APORT3XREQ'] = self.APORT3XREQ
        self.APORT3YREQ = RM_Field_VDAC0_OPA0_APORTREQ_APORT3YREQ(self)
        self.zz_fdict['APORT3YREQ'] = self.APORT3YREQ
        self.APORT4XREQ = RM_Field_VDAC0_OPA0_APORTREQ_APORT4XREQ(self)
        self.zz_fdict['APORT4XREQ'] = self.APORT4XREQ
        self.APORT4YREQ = RM_Field_VDAC0_OPA0_APORTREQ_APORT4YREQ(self)
        self.zz_fdict['APORT4YREQ'] = self.APORT4YREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA0_APORTCONFLICT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA0_APORTCONFLICT, self).__init__(rmio, label,
            0x40008000, 0x0A4,
            'OPA0_APORTCONFLICT', 'VDAC0.OPA0_APORTCONFLICT', 'read-only',
            "",
            0x00000000, 0x000003FC)

        self.APORT1XCONFLICT = RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT1XCONFLICT(self)
        self.zz_fdict['APORT1XCONFLICT'] = self.APORT1XCONFLICT
        self.APORT1YCONFLICT = RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT1YCONFLICT(self)
        self.zz_fdict['APORT1YCONFLICT'] = self.APORT1YCONFLICT
        self.APORT2XCONFLICT = RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT2XCONFLICT(self)
        self.zz_fdict['APORT2XCONFLICT'] = self.APORT2XCONFLICT
        self.APORT2YCONFLICT = RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT2YCONFLICT(self)
        self.zz_fdict['APORT2YCONFLICT'] = self.APORT2YCONFLICT
        self.APORT3XCONFLICT = RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT3XCONFLICT(self)
        self.zz_fdict['APORT3XCONFLICT'] = self.APORT3XCONFLICT
        self.APORT3YCONFLICT = RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT3YCONFLICT(self)
        self.zz_fdict['APORT3YCONFLICT'] = self.APORT3YCONFLICT
        self.APORT4XCONFLICT = RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT4XCONFLICT(self)
        self.zz_fdict['APORT4XCONFLICT'] = self.APORT4XCONFLICT
        self.APORT4YCONFLICT = RM_Field_VDAC0_OPA0_APORTCONFLICT_APORT4YCONFLICT(self)
        self.zz_fdict['APORT4YCONFLICT'] = self.APORT4YCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA0_CTRL, self).__init__(rmio, label,
            0x40008000, 0x0A8,
            'OPA0_CTRL', 'VDAC0.OPA0_CTRL', 'read-write',
            "",
            0x0000000E, 0x00313F1F)

        self.DRIVESTRENGTH = RM_Field_VDAC0_OPA0_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.INCBW = RM_Field_VDAC0_OPA0_CTRL_INCBW(self)
        self.zz_fdict['INCBW'] = self.INCBW
        self.HCMDIS = RM_Field_VDAC0_OPA0_CTRL_HCMDIS(self)
        self.zz_fdict['HCMDIS'] = self.HCMDIS
        self.OUTSCALE = RM_Field_VDAC0_OPA0_CTRL_OUTSCALE(self)
        self.zz_fdict['OUTSCALE'] = self.OUTSCALE
        self.PRSEN = RM_Field_VDAC0_OPA0_CTRL_PRSEN(self)
        self.zz_fdict['PRSEN'] = self.PRSEN
        self.PRSMODE = RM_Field_VDAC0_OPA0_CTRL_PRSMODE(self)
        self.zz_fdict['PRSMODE'] = self.PRSMODE
        self.PRSSEL = RM_Field_VDAC0_OPA0_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.PRSOUTMODE = RM_Field_VDAC0_OPA0_CTRL_PRSOUTMODE(self)
        self.zz_fdict['PRSOUTMODE'] = self.PRSOUTMODE
        self.APORTXMASTERDIS = RM_Field_VDAC0_OPA0_CTRL_APORTXMASTERDIS(self)
        self.zz_fdict['APORTXMASTERDIS'] = self.APORTXMASTERDIS
        self.APORTYMASTERDIS = RM_Field_VDAC0_OPA0_CTRL_APORTYMASTERDIS(self)
        self.zz_fdict['APORTYMASTERDIS'] = self.APORTYMASTERDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA0_TIMER(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA0_TIMER, self).__init__(rmio, label,
            0x40008000, 0x0AC,
            'OPA0_TIMER', 'VDAC0.OPA0_TIMER', 'read-write',
            "",
            0x00010700, 0x03FF7F3F)

        self.STARTUPDLY = RM_Field_VDAC0_OPA0_TIMER_STARTUPDLY(self)
        self.zz_fdict['STARTUPDLY'] = self.STARTUPDLY
        self.WARMUPTIME = RM_Field_VDAC0_OPA0_TIMER_WARMUPTIME(self)
        self.zz_fdict['WARMUPTIME'] = self.WARMUPTIME
        self.SETTLETIME = RM_Field_VDAC0_OPA0_TIMER_SETTLETIME(self)
        self.zz_fdict['SETTLETIME'] = self.SETTLETIME
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA0_MUX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA0_MUX, self).__init__(rmio, label,
            0x40008000, 0x0B0,
            'OPA0_MUX', 'VDAC0.OPA0_MUX', 'read-write',
            "",
            0x0016F2F1, 0x0717FFFF)

        self.POSSEL = RM_Field_VDAC0_OPA0_MUX_POSSEL(self)
        self.zz_fdict['POSSEL'] = self.POSSEL
        self.NEGSEL = RM_Field_VDAC0_OPA0_MUX_NEGSEL(self)
        self.zz_fdict['NEGSEL'] = self.NEGSEL
        self.RESINMUX = RM_Field_VDAC0_OPA0_MUX_RESINMUX(self)
        self.zz_fdict['RESINMUX'] = self.RESINMUX
        self.GAIN3X = RM_Field_VDAC0_OPA0_MUX_GAIN3X(self)
        self.zz_fdict['GAIN3X'] = self.GAIN3X
        self.RESSEL = RM_Field_VDAC0_OPA0_MUX_RESSEL(self)
        self.zz_fdict['RESSEL'] = self.RESSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA0_OUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA0_OUT, self).__init__(rmio, label,
            0x40008000, 0x0B4,
            'OPA0_OUT', 'VDAC0.OPA0_OUT', 'read-write',
            "",
            0x00000001, 0x00FF01FF)

        self.MAINOUTEN = RM_Field_VDAC0_OPA0_OUT_MAINOUTEN(self)
        self.zz_fdict['MAINOUTEN'] = self.MAINOUTEN
        self.ALTOUTEN = RM_Field_VDAC0_OPA0_OUT_ALTOUTEN(self)
        self.zz_fdict['ALTOUTEN'] = self.ALTOUTEN
        self.APORTOUTEN = RM_Field_VDAC0_OPA0_OUT_APORTOUTEN(self)
        self.zz_fdict['APORTOUTEN'] = self.APORTOUTEN
        self.SHORT = RM_Field_VDAC0_OPA0_OUT_SHORT(self)
        self.zz_fdict['SHORT'] = self.SHORT
        self.ALTOUTPADEN = RM_Field_VDAC0_OPA0_OUT_ALTOUTPADEN(self)
        self.zz_fdict['ALTOUTPADEN'] = self.ALTOUTPADEN
        self.APORTOUTSEL = RM_Field_VDAC0_OPA0_OUT_APORTOUTSEL(self)
        self.zz_fdict['APORTOUTSEL'] = self.APORTOUTSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA0_CAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA0_CAL, self).__init__(rmio, label,
            0x40008000, 0x0B8,
            'OPA0_CAL', 'VDAC0.OPA0_CAL', 'read-write',
            "",
            0x000080E7, 0x7DF6EDEF)

        self.CM1 = RM_Field_VDAC0_OPA0_CAL_CM1(self)
        self.zz_fdict['CM1'] = self.CM1
        self.CM2 = RM_Field_VDAC0_OPA0_CAL_CM2(self)
        self.zz_fdict['CM2'] = self.CM2
        self.CM3 = RM_Field_VDAC0_OPA0_CAL_CM3(self)
        self.zz_fdict['CM3'] = self.CM3
        self.GM = RM_Field_VDAC0_OPA0_CAL_GM(self)
        self.zz_fdict['GM'] = self.GM
        self.GM3 = RM_Field_VDAC0_OPA0_CAL_GM3(self)
        self.zz_fdict['GM3'] = self.GM3
        self.OFFSETP = RM_Field_VDAC0_OPA0_CAL_OFFSETP(self)
        self.zz_fdict['OFFSETP'] = self.OFFSETP
        self.OFFSETN = RM_Field_VDAC0_OPA0_CAL_OFFSETN(self)
        self.zz_fdict['OFFSETN'] = self.OFFSETN
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA1_APORTREQ(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA1_APORTREQ, self).__init__(rmio, label,
            0x40008000, 0x0C0,
            'OPA1_APORTREQ', 'VDAC0.OPA1_APORTREQ', 'read-only',
            "",
            0x00000000, 0x000003FC)

        self.APORT1XREQ = RM_Field_VDAC0_OPA1_APORTREQ_APORT1XREQ(self)
        self.zz_fdict['APORT1XREQ'] = self.APORT1XREQ
        self.APORT1YREQ = RM_Field_VDAC0_OPA1_APORTREQ_APORT1YREQ(self)
        self.zz_fdict['APORT1YREQ'] = self.APORT1YREQ
        self.APORT2XREQ = RM_Field_VDAC0_OPA1_APORTREQ_APORT2XREQ(self)
        self.zz_fdict['APORT2XREQ'] = self.APORT2XREQ
        self.APORT2YREQ = RM_Field_VDAC0_OPA1_APORTREQ_APORT2YREQ(self)
        self.zz_fdict['APORT2YREQ'] = self.APORT2YREQ
        self.APORT3XREQ = RM_Field_VDAC0_OPA1_APORTREQ_APORT3XREQ(self)
        self.zz_fdict['APORT3XREQ'] = self.APORT3XREQ
        self.APORT3YREQ = RM_Field_VDAC0_OPA1_APORTREQ_APORT3YREQ(self)
        self.zz_fdict['APORT3YREQ'] = self.APORT3YREQ
        self.APORT4XREQ = RM_Field_VDAC0_OPA1_APORTREQ_APORT4XREQ(self)
        self.zz_fdict['APORT4XREQ'] = self.APORT4XREQ
        self.APORT4YREQ = RM_Field_VDAC0_OPA1_APORTREQ_APORT4YREQ(self)
        self.zz_fdict['APORT4YREQ'] = self.APORT4YREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA1_APORTCONFLICT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA1_APORTCONFLICT, self).__init__(rmio, label,
            0x40008000, 0x0C4,
            'OPA1_APORTCONFLICT', 'VDAC0.OPA1_APORTCONFLICT', 'read-only',
            "",
            0x00000000, 0x000003FC)

        self.APORT1XCONFLICT = RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT1XCONFLICT(self)
        self.zz_fdict['APORT1XCONFLICT'] = self.APORT1XCONFLICT
        self.APORT1YCONFLICT = RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT1YCONFLICT(self)
        self.zz_fdict['APORT1YCONFLICT'] = self.APORT1YCONFLICT
        self.APORT2XCONFLICT = RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT2XCONFLICT(self)
        self.zz_fdict['APORT2XCONFLICT'] = self.APORT2XCONFLICT
        self.APORT2YCONFLICT = RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT2YCONFLICT(self)
        self.zz_fdict['APORT2YCONFLICT'] = self.APORT2YCONFLICT
        self.APORT3XCONFLICT = RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT3XCONFLICT(self)
        self.zz_fdict['APORT3XCONFLICT'] = self.APORT3XCONFLICT
        self.APORT3YCONFLICT = RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT3YCONFLICT(self)
        self.zz_fdict['APORT3YCONFLICT'] = self.APORT3YCONFLICT
        self.APORT4XCONFLICT = RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT4XCONFLICT(self)
        self.zz_fdict['APORT4XCONFLICT'] = self.APORT4XCONFLICT
        self.APORT4YCONFLICT = RM_Field_VDAC0_OPA1_APORTCONFLICT_APORT4YCONFLICT(self)
        self.zz_fdict['APORT4YCONFLICT'] = self.APORT4YCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA1_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA1_CTRL, self).__init__(rmio, label,
            0x40008000, 0x0C8,
            'OPA1_CTRL', 'VDAC0.OPA1_CTRL', 'read-write',
            "",
            0x0000000E, 0x00313F1F)

        self.DRIVESTRENGTH = RM_Field_VDAC0_OPA1_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.INCBW = RM_Field_VDAC0_OPA1_CTRL_INCBW(self)
        self.zz_fdict['INCBW'] = self.INCBW
        self.HCMDIS = RM_Field_VDAC0_OPA1_CTRL_HCMDIS(self)
        self.zz_fdict['HCMDIS'] = self.HCMDIS
        self.OUTSCALE = RM_Field_VDAC0_OPA1_CTRL_OUTSCALE(self)
        self.zz_fdict['OUTSCALE'] = self.OUTSCALE
        self.PRSEN = RM_Field_VDAC0_OPA1_CTRL_PRSEN(self)
        self.zz_fdict['PRSEN'] = self.PRSEN
        self.PRSMODE = RM_Field_VDAC0_OPA1_CTRL_PRSMODE(self)
        self.zz_fdict['PRSMODE'] = self.PRSMODE
        self.PRSSEL = RM_Field_VDAC0_OPA1_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.PRSOUTMODE = RM_Field_VDAC0_OPA1_CTRL_PRSOUTMODE(self)
        self.zz_fdict['PRSOUTMODE'] = self.PRSOUTMODE
        self.APORTXMASTERDIS = RM_Field_VDAC0_OPA1_CTRL_APORTXMASTERDIS(self)
        self.zz_fdict['APORTXMASTERDIS'] = self.APORTXMASTERDIS
        self.APORTYMASTERDIS = RM_Field_VDAC0_OPA1_CTRL_APORTYMASTERDIS(self)
        self.zz_fdict['APORTYMASTERDIS'] = self.APORTYMASTERDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA1_TIMER(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA1_TIMER, self).__init__(rmio, label,
            0x40008000, 0x0CC,
            'OPA1_TIMER', 'VDAC0.OPA1_TIMER', 'read-write',
            "",
            0x00010700, 0x03FF7F3F)

        self.STARTUPDLY = RM_Field_VDAC0_OPA1_TIMER_STARTUPDLY(self)
        self.zz_fdict['STARTUPDLY'] = self.STARTUPDLY
        self.WARMUPTIME = RM_Field_VDAC0_OPA1_TIMER_WARMUPTIME(self)
        self.zz_fdict['WARMUPTIME'] = self.WARMUPTIME
        self.SETTLETIME = RM_Field_VDAC0_OPA1_TIMER_SETTLETIME(self)
        self.zz_fdict['SETTLETIME'] = self.SETTLETIME
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA1_MUX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA1_MUX, self).__init__(rmio, label,
            0x40008000, 0x0D0,
            'OPA1_MUX', 'VDAC0.OPA1_MUX', 'read-write',
            "",
            0x0016F2F1, 0x0717FFFF)

        self.POSSEL = RM_Field_VDAC0_OPA1_MUX_POSSEL(self)
        self.zz_fdict['POSSEL'] = self.POSSEL
        self.NEGSEL = RM_Field_VDAC0_OPA1_MUX_NEGSEL(self)
        self.zz_fdict['NEGSEL'] = self.NEGSEL
        self.RESINMUX = RM_Field_VDAC0_OPA1_MUX_RESINMUX(self)
        self.zz_fdict['RESINMUX'] = self.RESINMUX
        self.GAIN3X = RM_Field_VDAC0_OPA1_MUX_GAIN3X(self)
        self.zz_fdict['GAIN3X'] = self.GAIN3X
        self.RESSEL = RM_Field_VDAC0_OPA1_MUX_RESSEL(self)
        self.zz_fdict['RESSEL'] = self.RESSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA1_OUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA1_OUT, self).__init__(rmio, label,
            0x40008000, 0x0D4,
            'OPA1_OUT', 'VDAC0.OPA1_OUT', 'read-write',
            "",
            0x00000001, 0x00FF01FF)

        self.MAINOUTEN = RM_Field_VDAC0_OPA1_OUT_MAINOUTEN(self)
        self.zz_fdict['MAINOUTEN'] = self.MAINOUTEN
        self.ALTOUTEN = RM_Field_VDAC0_OPA1_OUT_ALTOUTEN(self)
        self.zz_fdict['ALTOUTEN'] = self.ALTOUTEN
        self.APORTOUTEN = RM_Field_VDAC0_OPA1_OUT_APORTOUTEN(self)
        self.zz_fdict['APORTOUTEN'] = self.APORTOUTEN
        self.SHORT = RM_Field_VDAC0_OPA1_OUT_SHORT(self)
        self.zz_fdict['SHORT'] = self.SHORT
        self.ALTOUTPADEN = RM_Field_VDAC0_OPA1_OUT_ALTOUTPADEN(self)
        self.zz_fdict['ALTOUTPADEN'] = self.ALTOUTPADEN
        self.APORTOUTSEL = RM_Field_VDAC0_OPA1_OUT_APORTOUTSEL(self)
        self.zz_fdict['APORTOUTSEL'] = self.APORTOUTSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA1_CAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA1_CAL, self).__init__(rmio, label,
            0x40008000, 0x0D8,
            'OPA1_CAL', 'VDAC0.OPA1_CAL', 'read-write',
            "",
            0x000080E7, 0x7DF6EDEF)

        self.CM1 = RM_Field_VDAC0_OPA1_CAL_CM1(self)
        self.zz_fdict['CM1'] = self.CM1
        self.CM2 = RM_Field_VDAC0_OPA1_CAL_CM2(self)
        self.zz_fdict['CM2'] = self.CM2
        self.CM3 = RM_Field_VDAC0_OPA1_CAL_CM3(self)
        self.zz_fdict['CM3'] = self.CM3
        self.GM = RM_Field_VDAC0_OPA1_CAL_GM(self)
        self.zz_fdict['GM'] = self.GM
        self.GM3 = RM_Field_VDAC0_OPA1_CAL_GM3(self)
        self.zz_fdict['GM3'] = self.GM3
        self.OFFSETP = RM_Field_VDAC0_OPA1_CAL_OFFSETP(self)
        self.zz_fdict['OFFSETP'] = self.OFFSETP
        self.OFFSETN = RM_Field_VDAC0_OPA1_CAL_OFFSETN(self)
        self.zz_fdict['OFFSETN'] = self.OFFSETN
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA2_APORTREQ(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA2_APORTREQ, self).__init__(rmio, label,
            0x40008000, 0x0E0,
            'OPA2_APORTREQ', 'VDAC0.OPA2_APORTREQ', 'read-only',
            "",
            0x00000000, 0x000003FC)

        self.APORT1XREQ = RM_Field_VDAC0_OPA2_APORTREQ_APORT1XREQ(self)
        self.zz_fdict['APORT1XREQ'] = self.APORT1XREQ
        self.APORT1YREQ = RM_Field_VDAC0_OPA2_APORTREQ_APORT1YREQ(self)
        self.zz_fdict['APORT1YREQ'] = self.APORT1YREQ
        self.APORT2XREQ = RM_Field_VDAC0_OPA2_APORTREQ_APORT2XREQ(self)
        self.zz_fdict['APORT2XREQ'] = self.APORT2XREQ
        self.APORT2YREQ = RM_Field_VDAC0_OPA2_APORTREQ_APORT2YREQ(self)
        self.zz_fdict['APORT2YREQ'] = self.APORT2YREQ
        self.APORT3XREQ = RM_Field_VDAC0_OPA2_APORTREQ_APORT3XREQ(self)
        self.zz_fdict['APORT3XREQ'] = self.APORT3XREQ
        self.APORT3YREQ = RM_Field_VDAC0_OPA2_APORTREQ_APORT3YREQ(self)
        self.zz_fdict['APORT3YREQ'] = self.APORT3YREQ
        self.APORT4XREQ = RM_Field_VDAC0_OPA2_APORTREQ_APORT4XREQ(self)
        self.zz_fdict['APORT4XREQ'] = self.APORT4XREQ
        self.APORT4YREQ = RM_Field_VDAC0_OPA2_APORTREQ_APORT4YREQ(self)
        self.zz_fdict['APORT4YREQ'] = self.APORT4YREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA2_APORTCONFLICT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA2_APORTCONFLICT, self).__init__(rmio, label,
            0x40008000, 0x0E4,
            'OPA2_APORTCONFLICT', 'VDAC0.OPA2_APORTCONFLICT', 'read-only',
            "",
            0x00000000, 0x000003FC)

        self.APORT1XCONFLICT = RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT1XCONFLICT(self)
        self.zz_fdict['APORT1XCONFLICT'] = self.APORT1XCONFLICT
        self.APORT1YCONFLICT = RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT1YCONFLICT(self)
        self.zz_fdict['APORT1YCONFLICT'] = self.APORT1YCONFLICT
        self.APORT2XCONFLICT = RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT2XCONFLICT(self)
        self.zz_fdict['APORT2XCONFLICT'] = self.APORT2XCONFLICT
        self.APORT2YCONFLICT = RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT2YCONFLICT(self)
        self.zz_fdict['APORT2YCONFLICT'] = self.APORT2YCONFLICT
        self.APORT3XCONFLICT = RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT3XCONFLICT(self)
        self.zz_fdict['APORT3XCONFLICT'] = self.APORT3XCONFLICT
        self.APORT3YCONFLICT = RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT3YCONFLICT(self)
        self.zz_fdict['APORT3YCONFLICT'] = self.APORT3YCONFLICT
        self.APORT4XCONFLICT = RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT4XCONFLICT(self)
        self.zz_fdict['APORT4XCONFLICT'] = self.APORT4XCONFLICT
        self.APORT4YCONFLICT = RM_Field_VDAC0_OPA2_APORTCONFLICT_APORT4YCONFLICT(self)
        self.zz_fdict['APORT4YCONFLICT'] = self.APORT4YCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA2_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA2_CTRL, self).__init__(rmio, label,
            0x40008000, 0x0E8,
            'OPA2_CTRL', 'VDAC0.OPA2_CTRL', 'read-write',
            "",
            0x0000000E, 0x00313F1F)

        self.DRIVESTRENGTH = RM_Field_VDAC0_OPA2_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.INCBW = RM_Field_VDAC0_OPA2_CTRL_INCBW(self)
        self.zz_fdict['INCBW'] = self.INCBW
        self.HCMDIS = RM_Field_VDAC0_OPA2_CTRL_HCMDIS(self)
        self.zz_fdict['HCMDIS'] = self.HCMDIS
        self.OUTSCALE = RM_Field_VDAC0_OPA2_CTRL_OUTSCALE(self)
        self.zz_fdict['OUTSCALE'] = self.OUTSCALE
        self.PRSEN = RM_Field_VDAC0_OPA2_CTRL_PRSEN(self)
        self.zz_fdict['PRSEN'] = self.PRSEN
        self.PRSMODE = RM_Field_VDAC0_OPA2_CTRL_PRSMODE(self)
        self.zz_fdict['PRSMODE'] = self.PRSMODE
        self.PRSSEL = RM_Field_VDAC0_OPA2_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.PRSOUTMODE = RM_Field_VDAC0_OPA2_CTRL_PRSOUTMODE(self)
        self.zz_fdict['PRSOUTMODE'] = self.PRSOUTMODE
        self.APORTXMASTERDIS = RM_Field_VDAC0_OPA2_CTRL_APORTXMASTERDIS(self)
        self.zz_fdict['APORTXMASTERDIS'] = self.APORTXMASTERDIS
        self.APORTYMASTERDIS = RM_Field_VDAC0_OPA2_CTRL_APORTYMASTERDIS(self)
        self.zz_fdict['APORTYMASTERDIS'] = self.APORTYMASTERDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA2_TIMER(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA2_TIMER, self).__init__(rmio, label,
            0x40008000, 0x0EC,
            'OPA2_TIMER', 'VDAC0.OPA2_TIMER', 'read-write',
            "",
            0x00010700, 0x03FF7F3F)

        self.STARTUPDLY = RM_Field_VDAC0_OPA2_TIMER_STARTUPDLY(self)
        self.zz_fdict['STARTUPDLY'] = self.STARTUPDLY
        self.WARMUPTIME = RM_Field_VDAC0_OPA2_TIMER_WARMUPTIME(self)
        self.zz_fdict['WARMUPTIME'] = self.WARMUPTIME
        self.SETTLETIME = RM_Field_VDAC0_OPA2_TIMER_SETTLETIME(self)
        self.zz_fdict['SETTLETIME'] = self.SETTLETIME
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA2_MUX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA2_MUX, self).__init__(rmio, label,
            0x40008000, 0x0F0,
            'OPA2_MUX', 'VDAC0.OPA2_MUX', 'read-write',
            "",
            0x0016F2F1, 0x0717FFFF)

        self.POSSEL = RM_Field_VDAC0_OPA2_MUX_POSSEL(self)
        self.zz_fdict['POSSEL'] = self.POSSEL
        self.NEGSEL = RM_Field_VDAC0_OPA2_MUX_NEGSEL(self)
        self.zz_fdict['NEGSEL'] = self.NEGSEL
        self.RESINMUX = RM_Field_VDAC0_OPA2_MUX_RESINMUX(self)
        self.zz_fdict['RESINMUX'] = self.RESINMUX
        self.GAIN3X = RM_Field_VDAC0_OPA2_MUX_GAIN3X(self)
        self.zz_fdict['GAIN3X'] = self.GAIN3X
        self.RESSEL = RM_Field_VDAC0_OPA2_MUX_RESSEL(self)
        self.zz_fdict['RESSEL'] = self.RESSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA2_OUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA2_OUT, self).__init__(rmio, label,
            0x40008000, 0x0F4,
            'OPA2_OUT', 'VDAC0.OPA2_OUT', 'read-write',
            "",
            0x00000001, 0x00FF01FF)

        self.MAINOUTEN = RM_Field_VDAC0_OPA2_OUT_MAINOUTEN(self)
        self.zz_fdict['MAINOUTEN'] = self.MAINOUTEN
        self.ALTOUTEN = RM_Field_VDAC0_OPA2_OUT_ALTOUTEN(self)
        self.zz_fdict['ALTOUTEN'] = self.ALTOUTEN
        self.APORTOUTEN = RM_Field_VDAC0_OPA2_OUT_APORTOUTEN(self)
        self.zz_fdict['APORTOUTEN'] = self.APORTOUTEN
        self.SHORT = RM_Field_VDAC0_OPA2_OUT_SHORT(self)
        self.zz_fdict['SHORT'] = self.SHORT
        self.ALTOUTPADEN = RM_Field_VDAC0_OPA2_OUT_ALTOUTPADEN(self)
        self.zz_fdict['ALTOUTPADEN'] = self.ALTOUTPADEN
        self.APORTOUTSEL = RM_Field_VDAC0_OPA2_OUT_APORTOUTSEL(self)
        self.zz_fdict['APORTOUTSEL'] = self.APORTOUTSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA2_CAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA2_CAL, self).__init__(rmio, label,
            0x40008000, 0x0F8,
            'OPA2_CAL', 'VDAC0.OPA2_CAL', 'read-write',
            "",
            0x000080E7, 0x7DF6EDEF)

        self.CM1 = RM_Field_VDAC0_OPA2_CAL_CM1(self)
        self.zz_fdict['CM1'] = self.CM1
        self.CM2 = RM_Field_VDAC0_OPA2_CAL_CM2(self)
        self.zz_fdict['CM2'] = self.CM2
        self.CM3 = RM_Field_VDAC0_OPA2_CAL_CM3(self)
        self.zz_fdict['CM3'] = self.CM3
        self.GM = RM_Field_VDAC0_OPA2_CAL_GM(self)
        self.zz_fdict['GM'] = self.GM
        self.GM3 = RM_Field_VDAC0_OPA2_CAL_GM3(self)
        self.zz_fdict['GM3'] = self.GM3
        self.OFFSETP = RM_Field_VDAC0_OPA2_CAL_OFFSETP(self)
        self.zz_fdict['OFFSETP'] = self.OFFSETP
        self.OFFSETN = RM_Field_VDAC0_OPA2_CAL_OFFSETN(self)
        self.zz_fdict['OFFSETN'] = self.OFFSETN
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA3_APORTREQ(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA3_APORTREQ, self).__init__(rmio, label,
            0x40008000, 0x100,
            'OPA3_APORTREQ', 'VDAC0.OPA3_APORTREQ', 'read-only',
            "",
            0x00000000, 0x000003FC)

        self.APORT1XREQ = RM_Field_VDAC0_OPA3_APORTREQ_APORT1XREQ(self)
        self.zz_fdict['APORT1XREQ'] = self.APORT1XREQ
        self.APORT1YREQ = RM_Field_VDAC0_OPA3_APORTREQ_APORT1YREQ(self)
        self.zz_fdict['APORT1YREQ'] = self.APORT1YREQ
        self.APORT2XREQ = RM_Field_VDAC0_OPA3_APORTREQ_APORT2XREQ(self)
        self.zz_fdict['APORT2XREQ'] = self.APORT2XREQ
        self.APORT2YREQ = RM_Field_VDAC0_OPA3_APORTREQ_APORT2YREQ(self)
        self.zz_fdict['APORT2YREQ'] = self.APORT2YREQ
        self.APORT3XREQ = RM_Field_VDAC0_OPA3_APORTREQ_APORT3XREQ(self)
        self.zz_fdict['APORT3XREQ'] = self.APORT3XREQ
        self.APORT3YREQ = RM_Field_VDAC0_OPA3_APORTREQ_APORT3YREQ(self)
        self.zz_fdict['APORT3YREQ'] = self.APORT3YREQ
        self.APORT4XREQ = RM_Field_VDAC0_OPA3_APORTREQ_APORT4XREQ(self)
        self.zz_fdict['APORT4XREQ'] = self.APORT4XREQ
        self.APORT4YREQ = RM_Field_VDAC0_OPA3_APORTREQ_APORT4YREQ(self)
        self.zz_fdict['APORT4YREQ'] = self.APORT4YREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA3_APORTCONFLICT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA3_APORTCONFLICT, self).__init__(rmio, label,
            0x40008000, 0x104,
            'OPA3_APORTCONFLICT', 'VDAC0.OPA3_APORTCONFLICT', 'read-only',
            "",
            0x00000000, 0x000003FC)

        self.APORT1XCONFLICT = RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT1XCONFLICT(self)
        self.zz_fdict['APORT1XCONFLICT'] = self.APORT1XCONFLICT
        self.APORT1YCONFLICT = RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT1YCONFLICT(self)
        self.zz_fdict['APORT1YCONFLICT'] = self.APORT1YCONFLICT
        self.APORT2XCONFLICT = RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT2XCONFLICT(self)
        self.zz_fdict['APORT2XCONFLICT'] = self.APORT2XCONFLICT
        self.APORT2YCONFLICT = RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT2YCONFLICT(self)
        self.zz_fdict['APORT2YCONFLICT'] = self.APORT2YCONFLICT
        self.APORT3XCONFLICT = RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT3XCONFLICT(self)
        self.zz_fdict['APORT3XCONFLICT'] = self.APORT3XCONFLICT
        self.APORT3YCONFLICT = RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT3YCONFLICT(self)
        self.zz_fdict['APORT3YCONFLICT'] = self.APORT3YCONFLICT
        self.APORT4XCONFLICT = RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT4XCONFLICT(self)
        self.zz_fdict['APORT4XCONFLICT'] = self.APORT4XCONFLICT
        self.APORT4YCONFLICT = RM_Field_VDAC0_OPA3_APORTCONFLICT_APORT4YCONFLICT(self)
        self.zz_fdict['APORT4YCONFLICT'] = self.APORT4YCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA3_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA3_CTRL, self).__init__(rmio, label,
            0x40008000, 0x108,
            'OPA3_CTRL', 'VDAC0.OPA3_CTRL', 'read-write',
            "",
            0x0000000E, 0x00313F1F)

        self.DRIVESTRENGTH = RM_Field_VDAC0_OPA3_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.INCBW = RM_Field_VDAC0_OPA3_CTRL_INCBW(self)
        self.zz_fdict['INCBW'] = self.INCBW
        self.HCMDIS = RM_Field_VDAC0_OPA3_CTRL_HCMDIS(self)
        self.zz_fdict['HCMDIS'] = self.HCMDIS
        self.OUTSCALE = RM_Field_VDAC0_OPA3_CTRL_OUTSCALE(self)
        self.zz_fdict['OUTSCALE'] = self.OUTSCALE
        self.PRSEN = RM_Field_VDAC0_OPA3_CTRL_PRSEN(self)
        self.zz_fdict['PRSEN'] = self.PRSEN
        self.PRSMODE = RM_Field_VDAC0_OPA3_CTRL_PRSMODE(self)
        self.zz_fdict['PRSMODE'] = self.PRSMODE
        self.PRSSEL = RM_Field_VDAC0_OPA3_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.PRSOUTMODE = RM_Field_VDAC0_OPA3_CTRL_PRSOUTMODE(self)
        self.zz_fdict['PRSOUTMODE'] = self.PRSOUTMODE
        self.APORTXMASTERDIS = RM_Field_VDAC0_OPA3_CTRL_APORTXMASTERDIS(self)
        self.zz_fdict['APORTXMASTERDIS'] = self.APORTXMASTERDIS
        self.APORTYMASTERDIS = RM_Field_VDAC0_OPA3_CTRL_APORTYMASTERDIS(self)
        self.zz_fdict['APORTYMASTERDIS'] = self.APORTYMASTERDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA3_TIMER(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA3_TIMER, self).__init__(rmio, label,
            0x40008000, 0x10C,
            'OPA3_TIMER', 'VDAC0.OPA3_TIMER', 'read-write',
            "",
            0x00010700, 0x03FF7F3F)

        self.STARTUPDLY = RM_Field_VDAC0_OPA3_TIMER_STARTUPDLY(self)
        self.zz_fdict['STARTUPDLY'] = self.STARTUPDLY
        self.WARMUPTIME = RM_Field_VDAC0_OPA3_TIMER_WARMUPTIME(self)
        self.zz_fdict['WARMUPTIME'] = self.WARMUPTIME
        self.SETTLETIME = RM_Field_VDAC0_OPA3_TIMER_SETTLETIME(self)
        self.zz_fdict['SETTLETIME'] = self.SETTLETIME
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA3_MUX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA3_MUX, self).__init__(rmio, label,
            0x40008000, 0x110,
            'OPA3_MUX', 'VDAC0.OPA3_MUX', 'read-write',
            "",
            0x0016F2F1, 0x0717FFFF)

        self.POSSEL = RM_Field_VDAC0_OPA3_MUX_POSSEL(self)
        self.zz_fdict['POSSEL'] = self.POSSEL
        self.NEGSEL = RM_Field_VDAC0_OPA3_MUX_NEGSEL(self)
        self.zz_fdict['NEGSEL'] = self.NEGSEL
        self.RESINMUX = RM_Field_VDAC0_OPA3_MUX_RESINMUX(self)
        self.zz_fdict['RESINMUX'] = self.RESINMUX
        self.GAIN3X = RM_Field_VDAC0_OPA3_MUX_GAIN3X(self)
        self.zz_fdict['GAIN3X'] = self.GAIN3X
        self.RESSEL = RM_Field_VDAC0_OPA3_MUX_RESSEL(self)
        self.zz_fdict['RESSEL'] = self.RESSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA3_OUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA3_OUT, self).__init__(rmio, label,
            0x40008000, 0x114,
            'OPA3_OUT', 'VDAC0.OPA3_OUT', 'read-write',
            "",
            0x00000001, 0x00FF01FF)

        self.MAINOUTEN = RM_Field_VDAC0_OPA3_OUT_MAINOUTEN(self)
        self.zz_fdict['MAINOUTEN'] = self.MAINOUTEN
        self.ALTOUTEN = RM_Field_VDAC0_OPA3_OUT_ALTOUTEN(self)
        self.zz_fdict['ALTOUTEN'] = self.ALTOUTEN
        self.APORTOUTEN = RM_Field_VDAC0_OPA3_OUT_APORTOUTEN(self)
        self.zz_fdict['APORTOUTEN'] = self.APORTOUTEN
        self.SHORT = RM_Field_VDAC0_OPA3_OUT_SHORT(self)
        self.zz_fdict['SHORT'] = self.SHORT
        self.ALTOUTPADEN = RM_Field_VDAC0_OPA3_OUT_ALTOUTPADEN(self)
        self.zz_fdict['ALTOUTPADEN'] = self.ALTOUTPADEN
        self.APORTOUTSEL = RM_Field_VDAC0_OPA3_OUT_APORTOUTSEL(self)
        self.zz_fdict['APORTOUTSEL'] = self.APORTOUTSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_VDAC0_OPA3_CAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_VDAC0_OPA3_CAL, self).__init__(rmio, label,
            0x40008000, 0x118,
            'OPA3_CAL', 'VDAC0.OPA3_CAL', 'read-write',
            "",
            0x000080E7, 0x7DF6EDEF)

        self.CM1 = RM_Field_VDAC0_OPA3_CAL_CM1(self)
        self.zz_fdict['CM1'] = self.CM1
        self.CM2 = RM_Field_VDAC0_OPA3_CAL_CM2(self)
        self.zz_fdict['CM2'] = self.CM2
        self.CM3 = RM_Field_VDAC0_OPA3_CAL_CM3(self)
        self.zz_fdict['CM3'] = self.CM3
        self.GM = RM_Field_VDAC0_OPA3_CAL_GM(self)
        self.zz_fdict['GM'] = self.GM
        self.GM3 = RM_Field_VDAC0_OPA3_CAL_GM3(self)
        self.zz_fdict['GM3'] = self.GM3
        self.OFFSETP = RM_Field_VDAC0_OPA3_CAL_OFFSETP(self)
        self.zz_fdict['OFFSETP'] = self.OFFSETP
        self.OFFSETN = RM_Field_VDAC0_OPA3_CAL_OFFSETN(self)
        self.zz_fdict['OFFSETN'] = self.OFFSETN
        self.__dict__['zz_frozen'] = True


