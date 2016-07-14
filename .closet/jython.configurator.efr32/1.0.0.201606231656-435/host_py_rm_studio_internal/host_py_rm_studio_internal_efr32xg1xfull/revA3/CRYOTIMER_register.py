
from static import Base_RM_Register
from CRYOTIMER_field import *


class RM_Register_CRYOTIMER_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYOTIMER_CTRL, self).__init__(rmio, label,
            0x4001e000, 0x000,
            'CTRL', 'CRYOTIMER.CTRL', 'read-write',
            "",
            0x00000000, 0x000000EF)

        self.EN = RM_Field_CRYOTIMER_CTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.DEBUGRUN = RM_Field_CRYOTIMER_CTRL_DEBUGRUN(self)
        self.zz_fdict['DEBUGRUN'] = self.DEBUGRUN
        self.OSCSEL = RM_Field_CRYOTIMER_CTRL_OSCSEL(self)
        self.zz_fdict['OSCSEL'] = self.OSCSEL
        self.PRESC = RM_Field_CRYOTIMER_CTRL_PRESC(self)
        self.zz_fdict['PRESC'] = self.PRESC
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYOTIMER_PERIODSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYOTIMER_PERIODSEL, self).__init__(rmio, label,
            0x4001e000, 0x004,
            'PERIODSEL', 'CRYOTIMER.PERIODSEL', 'read-write',
            "",
            0x00000020, 0x0000003F)

        self.PERIODSEL = RM_Field_CRYOTIMER_PERIODSEL_PERIODSEL(self)
        self.zz_fdict['PERIODSEL'] = self.PERIODSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYOTIMER_CNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYOTIMER_CNT, self).__init__(rmio, label,
            0x4001e000, 0x008,
            'CNT', 'CRYOTIMER.CNT', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.CNT = RM_Field_CRYOTIMER_CNT_CNT(self)
        self.zz_fdict['CNT'] = self.CNT
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYOTIMER_EM4WUEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYOTIMER_EM4WUEN, self).__init__(rmio, label,
            0x4001e000, 0x00C,
            'EM4WUEN', 'CRYOTIMER.EM4WUEN', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.EM4WU = RM_Field_CRYOTIMER_EM4WUEN_EM4WU(self)
        self.zz_fdict['EM4WU'] = self.EM4WU
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYOTIMER_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYOTIMER_IF, self).__init__(rmio, label,
            0x4001e000, 0x010,
            'IF', 'CRYOTIMER.IF', 'read-only',
            "",
            0x00000000, 0x00000001)

        self.PERIOD = RM_Field_CRYOTIMER_IF_PERIOD(self)
        self.zz_fdict['PERIOD'] = self.PERIOD
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYOTIMER_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYOTIMER_IFS, self).__init__(rmio, label,
            0x4001e000, 0x014,
            'IFS', 'CRYOTIMER.IFS', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.PERIOD = RM_Field_CRYOTIMER_IFS_PERIOD(self)
        self.zz_fdict['PERIOD'] = self.PERIOD
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYOTIMER_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYOTIMER_IFC, self).__init__(rmio, label,
            0x4001e000, 0x018,
            'IFC', 'CRYOTIMER.IFC', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.PERIOD = RM_Field_CRYOTIMER_IFC_PERIOD(self)
        self.zz_fdict['PERIOD'] = self.PERIOD
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYOTIMER_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYOTIMER_IEN, self).__init__(rmio, label,
            0x4001e000, 0x01C,
            'IEN', 'CRYOTIMER.IEN', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.PERIOD = RM_Field_CRYOTIMER_IEN_PERIOD(self)
        self.zz_fdict['PERIOD'] = self.PERIOD
        self.__dict__['zz_frozen'] = True


