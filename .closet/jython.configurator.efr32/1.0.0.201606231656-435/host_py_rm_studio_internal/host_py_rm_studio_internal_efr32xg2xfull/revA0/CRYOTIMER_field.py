
from static import Base_RM_Field
from CRYOTIMER_enum import *


class RM_Field_CRYOTIMER_CTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYOTIMER_CTRL_EN, self).__init__(register,
            'EN', 'CRYOTIMER.CTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYOTIMER_CTRL_DEBUGRUN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYOTIMER_CTRL_DEBUGRUN, self).__init__(register,
            'DEBUGRUN', 'CRYOTIMER.CTRL.DEBUGRUN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYOTIMER_CTRL_OSCSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYOTIMER_CTRL_OSCSEL, self).__init__(register,
            'OSCSEL', 'CRYOTIMER.CTRL.OSCSEL', 'read-write',
            "",
            2, 2,
            RM_Enum_CRYOTIMER_CTRL_OSCSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYOTIMER_CTRL_PRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYOTIMER_CTRL_PRESC, self).__init__(register,
            'PRESC', 'CRYOTIMER.CTRL.PRESC', 'read-write',
            "",
            5, 3,
            RM_Enum_CRYOTIMER_CTRL_PRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYOTIMER_PERIODSEL_PERIODSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYOTIMER_PERIODSEL_PERIODSEL, self).__init__(register,
            'PERIODSEL', 'CRYOTIMER.PERIODSEL.PERIODSEL', 'read-write',
            "",
            0, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYOTIMER_CNT_CNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYOTIMER_CNT_CNT, self).__init__(register,
            'CNT', 'CRYOTIMER.CNT.CNT', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYOTIMER_EM4WUEN_EM4WU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYOTIMER_EM4WUEN_EM4WU, self).__init__(register,
            'EM4WU', 'CRYOTIMER.EM4WUEN.EM4WU', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYOTIMER_IF_PERIOD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYOTIMER_IF_PERIOD, self).__init__(register,
            'PERIOD', 'CRYOTIMER.IF.PERIOD', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYOTIMER_IFS_PERIOD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYOTIMER_IFS_PERIOD, self).__init__(register,
            'PERIOD', 'CRYOTIMER.IFS.PERIOD', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYOTIMER_IFC_PERIOD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYOTIMER_IFC_PERIOD, self).__init__(register,
            'PERIOD', 'CRYOTIMER.IFC.PERIOD', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYOTIMER_IEN_PERIOD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYOTIMER_IEN_PERIOD, self).__init__(register,
            'PERIOD', 'CRYOTIMER.IEN.PERIOD', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


