
from static import Base_RM_Register
from RFSENSE_field import *


class RM_Register_RFSENSE_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RFSENSE_CTRL, self).__init__(rmio, label,
            0x40088000, 0x000,
            'CTRL', 'RFSENSE.CTRL', 'read-write',
            "",
            0x00000000, 0x0000006F)

        #print("WARNING: Aliasing field '2G4EN' to 'RF2G4EN'")
        self.RF2G4EN = RM_Field_RFSENSE_CTRL_2G4EN(self)
        self.zz_fdict['RF2G4EN'] = self.RF2G4EN
        self.SUBGEN = RM_Field_RFSENSE_CTRL_SUBGEN(self)
        self.zz_fdict['SUBGEN'] = self.SUBGEN
        self.OSCSEL = RM_Field_RFSENSE_CTRL_OSCSEL(self)
        self.zz_fdict['OSCSEL'] = self.OSCSEL
        self.REDSEN = RM_Field_RFSENSE_CTRL_REDSEN(self)
        self.zz_fdict['REDSEN'] = self.REDSEN
        self.RFOPA = RM_Field_RFSENSE_CTRL_RFOPA(self)
        self.zz_fdict['RFOPA'] = self.RFOPA
        self.__dict__['zz_frozen'] = True


class RM_Register_RFSENSE_PERIODSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RFSENSE_PERIODSEL, self).__init__(rmio, label,
            0x40088000, 0x004,
            'PERIODSEL', 'RFSENSE.PERIODSEL', 'read-write',
            "",
            0x0000000F, 0x0000000F)

        self.PERIODSEL = RM_Field_RFSENSE_PERIODSEL_PERIODSEL(self)
        self.zz_fdict['PERIODSEL'] = self.PERIODSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_RFSENSE_CNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RFSENSE_CNT, self).__init__(rmio, label,
            0x40088000, 0x008,
            'CNT', 'RFSENSE.CNT', 'read-only',
            "",
            0x00000000, 0x00007FFF)

        self.CNT = RM_Field_RFSENSE_CNT_CNT(self)
        self.zz_fdict['CNT'] = self.CNT
        self.__dict__['zz_frozen'] = True


class RM_Register_RFSENSE_EM4WUEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RFSENSE_EM4WUEN, self).__init__(rmio, label,
            0x40088000, 0x010,
            'EM4WUEN', 'RFSENSE.EM4WUEN', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.EM4WU = RM_Field_RFSENSE_EM4WUEN_EM4WU(self)
        self.zz_fdict['EM4WU'] = self.EM4WU
        self.__dict__['zz_frozen'] = True


class RM_Register_RFSENSE_CALIB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RFSENSE_CALIB, self).__init__(rmio, label,
            0x40088000, 0x014,
            'CALIB', 'RFSENSE.CALIB', 'read-write',
            "",
            0x00000000, 0x000001F7)

        self.OFFSETCOARSE = RM_Field_RFSENSE_CALIB_OFFSETCOARSE(self)
        self.zz_fdict['OFFSETCOARSE'] = self.OFFSETCOARSE
        self.OFFSETFINE = RM_Field_RFSENSE_CALIB_OFFSETFINE(self)
        self.zz_fdict['OFFSETFINE'] = self.OFFSETFINE
        self.__dict__['zz_frozen'] = True


class RM_Register_RFSENSE_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RFSENSE_IF, self).__init__(rmio, label,
            0x40088000, 0x018,
            'IF', 'RFSENSE.IF', 'read-only',
            "",
            0x00000000, 0x00000001)

        self.RF = RM_Field_RFSENSE_IF_RF(self)
        self.zz_fdict['RF'] = self.RF
        self.__dict__['zz_frozen'] = True


class RM_Register_RFSENSE_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RFSENSE_IFS, self).__init__(rmio, label,
            0x40088000, 0x01C,
            'IFS', 'RFSENSE.IFS', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.RF = RM_Field_RFSENSE_IFS_RF(self)
        self.zz_fdict['RF'] = self.RF
        self.__dict__['zz_frozen'] = True


class RM_Register_RFSENSE_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RFSENSE_IFC, self).__init__(rmio, label,
            0x40088000, 0x020,
            'IFC', 'RFSENSE.IFC', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.RF = RM_Field_RFSENSE_IFC_RF(self)
        self.zz_fdict['RF'] = self.RF
        self.__dict__['zz_frozen'] = True


class RM_Register_RFSENSE_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RFSENSE_IEN, self).__init__(rmio, label,
            0x40088000, 0x024,
            'IEN', 'RFSENSE.IEN', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.RF = RM_Field_RFSENSE_IEN_RF(self)
        self.zz_fdict['RF'] = self.RF
        self.__dict__['zz_frozen'] = True


