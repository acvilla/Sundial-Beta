
from static import Base_RM_Field
from RFSENSE_enum import *


class RM_Field_RFSENSE_CTRL_2G4EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RFSENSE_CTRL_2G4EN, self).__init__(register,
            '2G4EN', 'RFSENSE.CTRL.2G4EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RFSENSE_CTRL_SUBGEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RFSENSE_CTRL_SUBGEN, self).__init__(register,
            'SUBGEN', 'RFSENSE.CTRL.SUBGEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RFSENSE_CTRL_OSCSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RFSENSE_CTRL_OSCSEL, self).__init__(register,
            'OSCSEL', 'RFSENSE.CTRL.OSCSEL', 'read-write',
            "",
            2, 2,
            RM_Enum_RFSENSE_CTRL_OSCSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RFSENSE_CTRL_REDSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RFSENSE_CTRL_REDSEN, self).__init__(register,
            'REDSEN', 'RFSENSE.CTRL.REDSEN', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RFSENSE_CTRL_RFOPA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RFSENSE_CTRL_RFOPA, self).__init__(register,
            'RFOPA', 'RFSENSE.CTRL.RFOPA', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RFSENSE_PERIODSEL_PERIODSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RFSENSE_PERIODSEL_PERIODSEL, self).__init__(register,
            'PERIODSEL', 'RFSENSE.PERIODSEL.PERIODSEL', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RFSENSE_CNT_CNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RFSENSE_CNT_CNT, self).__init__(register,
            'CNT', 'RFSENSE.CNT.CNT', 'read-only',
            "",
            0, 15)
        self.__dict__['zz_frozen'] = True


class RM_Field_RFSENSE_EM4WUEN_EM4WU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RFSENSE_EM4WUEN_EM4WU, self).__init__(register,
            'EM4WU', 'RFSENSE.EM4WUEN.EM4WU', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RFSENSE_CALIB_OFFSETCOARSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RFSENSE_CALIB_OFFSETCOARSE, self).__init__(register,
            'OFFSETCOARSE', 'RFSENSE.CALIB.OFFSETCOARSE', 'read-write',
            "",
            0, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_RFSENSE_CALIB_OFFSETFINE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RFSENSE_CALIB_OFFSETFINE, self).__init__(register,
            'OFFSETFINE', 'RFSENSE.CALIB.OFFSETFINE', 'read-write',
            "",
            4, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_RFSENSE_IF_RF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RFSENSE_IF_RF, self).__init__(register,
            'RF', 'RFSENSE.IF.RF', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RFSENSE_IFS_RF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RFSENSE_IFS_RF, self).__init__(register,
            'RF', 'RFSENSE.IFS.RF', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RFSENSE_IFC_RF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RFSENSE_IFC_RF, self).__init__(register,
            'RF', 'RFSENSE.IFC.RF', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RFSENSE_IEN_RF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RFSENSE_IEN_RF, self).__init__(register,
            'RF', 'RFSENSE.IEN.RF', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


