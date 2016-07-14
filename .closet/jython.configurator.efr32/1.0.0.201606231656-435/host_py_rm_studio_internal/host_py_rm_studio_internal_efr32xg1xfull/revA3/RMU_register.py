
from static import Base_RM_Register
from RMU_field import *


class RM_Register_RMU_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RMU_CTRL, self).__init__(rmio, label,
            0x400e5000, 0x000,
            'CTRL', 'RMU.CTRL', 'read-write',
            "",
            0x00004224, 0x13007777)

        self.WDOGRMODE = RM_Field_RMU_CTRL_WDOGRMODE(self)
        self.zz_fdict['WDOGRMODE'] = self.WDOGRMODE
        self.LOCKUPRMODE = RM_Field_RMU_CTRL_LOCKUPRMODE(self)
        self.zz_fdict['LOCKUPRMODE'] = self.LOCKUPRMODE
        self.SYSRMODE = RM_Field_RMU_CTRL_SYSRMODE(self)
        self.zz_fdict['SYSRMODE'] = self.SYSRMODE
        self.PINRMODE = RM_Field_RMU_CTRL_PINRMODE(self)
        self.zz_fdict['PINRMODE'] = self.PINRMODE
        self.RESETSTATE = RM_Field_RMU_CTRL_RESETSTATE(self)
        self.zz_fdict['RESETSTATE'] = self.RESETSTATE
        self.RST_CMU_HS_TO_DIS = RM_Field_RMU_CTRL_RST_CMU_HS_TO_DIS(self)
        self.zz_fdict['RST_CMU_HS_TO_DIS'] = self.RST_CMU_HS_TO_DIS
        self.__dict__['zz_frozen'] = True


class RM_Register_RMU_RSTCAUSE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RMU_RSTCAUSE, self).__init__(rmio, label,
            0x400e5000, 0x004,
            'RSTCAUSE', 'RMU.RSTCAUSE', 'read-only',
            "",
            0x00000000, 0xE0010F1D)

        self.PORST = RM_Field_RMU_RSTCAUSE_PORST(self)
        self.zz_fdict['PORST'] = self.PORST
        self.AVDDBOD = RM_Field_RMU_RSTCAUSE_AVDDBOD(self)
        self.zz_fdict['AVDDBOD'] = self.AVDDBOD
        self.DVDDBOD = RM_Field_RMU_RSTCAUSE_DVDDBOD(self)
        self.zz_fdict['DVDDBOD'] = self.DVDDBOD
        self.DECBOD = RM_Field_RMU_RSTCAUSE_DECBOD(self)
        self.zz_fdict['DECBOD'] = self.DECBOD
        self.EXTRST = RM_Field_RMU_RSTCAUSE_EXTRST(self)
        self.zz_fdict['EXTRST'] = self.EXTRST
        self.LOCKUPRST = RM_Field_RMU_RSTCAUSE_LOCKUPRST(self)
        self.zz_fdict['LOCKUPRST'] = self.LOCKUPRST
        self.SYSREQRST = RM_Field_RMU_RSTCAUSE_SYSREQRST(self)
        self.zz_fdict['SYSREQRST'] = self.SYSREQRST
        self.WDOGRST = RM_Field_RMU_RSTCAUSE_WDOGRST(self)
        self.zz_fdict['WDOGRST'] = self.WDOGRST
        self.EM4RST = RM_Field_RMU_RSTCAUSE_EM4RST(self)
        self.zz_fdict['EM4RST'] = self.EM4RST
        self.AVDDEM4BOD_N = RM_Field_RMU_RSTCAUSE_AVDDEM4BOD_N(self)
        self.zz_fdict['AVDDEM4BOD_N'] = self.AVDDEM4BOD_N
        self.FLASHBOD_N = RM_Field_RMU_RSTCAUSE_FLASHBOD_N(self)
        self.zz_fdict['FLASHBOD_N'] = self.FLASHBOD_N
        self.DEC1BOD_N = RM_Field_RMU_RSTCAUSE_DEC1BOD_N(self)
        self.zz_fdict['DEC1BOD_N'] = self.DEC1BOD_N
        self.__dict__['zz_frozen'] = True


class RM_Register_RMU_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RMU_CMD, self).__init__(rmio, label,
            0x400e5000, 0x008,
            'CMD', 'RMU.CMD', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.RCCLR = RM_Field_RMU_CMD_RCCLR(self)
        self.zz_fdict['RCCLR'] = self.RCCLR
        self.__dict__['zz_frozen'] = True


class RM_Register_RMU_RST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RMU_RST, self).__init__(rmio, label,
            0x400e5000, 0x00C,
            'RST', 'RMU.RST', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.RADIORST = RM_Field_RMU_RST_RADIORST(self)
        self.zz_fdict['RADIORST'] = self.RADIORST
        self.LFRST = RM_Field_RMU_RST_LFRST(self)
        self.zz_fdict['LFRST'] = self.LFRST
        self.__dict__['zz_frozen'] = True


class RM_Register_RMU_LOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RMU_LOCK, self).__init__(rmio, label,
            0x400e5000, 0x010,
            'LOCK', 'RMU.LOCK', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.LOCKKEY = RM_Field_RMU_LOCK_LOCKKEY(self)
        self.zz_fdict['LOCKKEY'] = self.LOCKKEY
        self.__dict__['zz_frozen'] = True


