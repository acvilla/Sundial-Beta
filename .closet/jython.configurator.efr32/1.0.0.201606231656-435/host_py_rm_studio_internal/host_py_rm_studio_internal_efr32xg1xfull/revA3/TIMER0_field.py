
from static import Base_RM_Field
from TIMER0_enum import *


class RM_Field_TIMER0_CTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CTRL_MODE, self).__init__(register,
            'MODE', 'TIMER0.CTRL.MODE', 'read-write',
            "",
            0, 2,
            RM_Enum_TIMER0_CTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CTRL_SYNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CTRL_SYNC, self).__init__(register,
            'SYNC', 'TIMER0.CTRL.SYNC', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CTRL_OSMEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CTRL_OSMEN, self).__init__(register,
            'OSMEN', 'TIMER0.CTRL.OSMEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CTRL_QDM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CTRL_QDM, self).__init__(register,
            'QDM', 'TIMER0.CTRL.QDM', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CTRL_DEBUGRUN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CTRL_DEBUGRUN, self).__init__(register,
            'DEBUGRUN', 'TIMER0.CTRL.DEBUGRUN', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CTRL_DMACLRACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CTRL_DMACLRACT, self).__init__(register,
            'DMACLRACT', 'TIMER0.CTRL.DMACLRACT', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CTRL_RISEA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CTRL_RISEA, self).__init__(register,
            'RISEA', 'TIMER0.CTRL.RISEA', 'read-write',
            "",
            8, 2,
            RM_Enum_TIMER0_CTRL_RISEA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CTRL_FALLA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CTRL_FALLA, self).__init__(register,
            'FALLA', 'TIMER0.CTRL.FALLA', 'read-write',
            "",
            10, 2,
            RM_Enum_TIMER0_CTRL_FALLA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CTRL_X2CNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CTRL_X2CNT, self).__init__(register,
            'X2CNT', 'TIMER0.CTRL.X2CNT', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CTRL_CLKSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CTRL_CLKSEL, self).__init__(register,
            'CLKSEL', 'TIMER0.CTRL.CLKSEL', 'read-write',
            "",
            16, 2,
            RM_Enum_TIMER0_CTRL_CLKSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CTRL_PRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CTRL_PRESC, self).__init__(register,
            'PRESC', 'TIMER0.CTRL.PRESC', 'read-write',
            "",
            24, 4,
            RM_Enum_TIMER0_CTRL_PRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CTRL_ATI(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CTRL_ATI, self).__init__(register,
            'ATI', 'TIMER0.CTRL.ATI', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CTRL_RSSCOIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CTRL_RSSCOIST, self).__init__(register,
            'RSSCOIST', 'TIMER0.CTRL.RSSCOIST', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CMD_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CMD_START, self).__init__(register,
            'START', 'TIMER0.CMD.START', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CMD_STOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CMD_STOP, self).__init__(register,
            'STOP', 'TIMER0.CMD.STOP', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_RUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_RUNNING, self).__init__(register,
            'RUNNING', 'TIMER0.STATUS.RUNNING', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_DIR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_DIR, self).__init__(register,
            'DIR', 'TIMER0.STATUS.DIR', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_TOPBV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_TOPBV, self).__init__(register,
            'TOPBV', 'TIMER0.STATUS.TOPBV', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_CCVBV0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_CCVBV0, self).__init__(register,
            'CCVBV0', 'TIMER0.STATUS.CCVBV0', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_CCVBV1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_CCVBV1, self).__init__(register,
            'CCVBV1', 'TIMER0.STATUS.CCVBV1', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_CCVBV2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_CCVBV2, self).__init__(register,
            'CCVBV2', 'TIMER0.STATUS.CCVBV2', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_CCVBV3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_CCVBV3, self).__init__(register,
            'CCVBV3', 'TIMER0.STATUS.CCVBV3', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_ICV0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_ICV0, self).__init__(register,
            'ICV0', 'TIMER0.STATUS.ICV0', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_ICV1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_ICV1, self).__init__(register,
            'ICV1', 'TIMER0.STATUS.ICV1', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_ICV2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_ICV2, self).__init__(register,
            'ICV2', 'TIMER0.STATUS.ICV2', 'read-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_ICV3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_ICV3, self).__init__(register,
            'ICV3', 'TIMER0.STATUS.ICV3', 'read-only',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_CCPOL0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_CCPOL0, self).__init__(register,
            'CCPOL0', 'TIMER0.STATUS.CCPOL0', 'read-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_CCPOL1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_CCPOL1, self).__init__(register,
            'CCPOL1', 'TIMER0.STATUS.CCPOL1', 'read-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_CCPOL2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_CCPOL2, self).__init__(register,
            'CCPOL2', 'TIMER0.STATUS.CCPOL2', 'read-only',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_STATUS_CCPOL3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_STATUS_CCPOL3, self).__init__(register,
            'CCPOL3', 'TIMER0.STATUS.CCPOL3', 'read-only',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IF_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IF_OF, self).__init__(register,
            'OF', 'TIMER0.IF.OF', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IF_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IF_UF, self).__init__(register,
            'UF', 'TIMER0.IF.UF', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IF_DIRCHG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IF_DIRCHG, self).__init__(register,
            'DIRCHG', 'TIMER0.IF.DIRCHG', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IF_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IF_CC0, self).__init__(register,
            'CC0', 'TIMER0.IF.CC0', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IF_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IF_CC1, self).__init__(register,
            'CC1', 'TIMER0.IF.CC1', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IF_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IF_CC2, self).__init__(register,
            'CC2', 'TIMER0.IF.CC2', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IF_CC3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IF_CC3, self).__init__(register,
            'CC3', 'TIMER0.IF.CC3', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IF_ICBOF0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IF_ICBOF0, self).__init__(register,
            'ICBOF0', 'TIMER0.IF.ICBOF0', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IF_ICBOF1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IF_ICBOF1, self).__init__(register,
            'ICBOF1', 'TIMER0.IF.ICBOF1', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IF_ICBOF2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IF_ICBOF2, self).__init__(register,
            'ICBOF2', 'TIMER0.IF.ICBOF2', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IF_ICBOF3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IF_ICBOF3, self).__init__(register,
            'ICBOF3', 'TIMER0.IF.ICBOF3', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFS_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFS_OF, self).__init__(register,
            'OF', 'TIMER0.IFS.OF', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFS_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFS_UF, self).__init__(register,
            'UF', 'TIMER0.IFS.UF', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFS_DIRCHG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFS_DIRCHG, self).__init__(register,
            'DIRCHG', 'TIMER0.IFS.DIRCHG', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFS_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFS_CC0, self).__init__(register,
            'CC0', 'TIMER0.IFS.CC0', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFS_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFS_CC1, self).__init__(register,
            'CC1', 'TIMER0.IFS.CC1', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFS_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFS_CC2, self).__init__(register,
            'CC2', 'TIMER0.IFS.CC2', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFS_CC3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFS_CC3, self).__init__(register,
            'CC3', 'TIMER0.IFS.CC3', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFS_ICBOF0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFS_ICBOF0, self).__init__(register,
            'ICBOF0', 'TIMER0.IFS.ICBOF0', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFS_ICBOF1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFS_ICBOF1, self).__init__(register,
            'ICBOF1', 'TIMER0.IFS.ICBOF1', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFS_ICBOF2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFS_ICBOF2, self).__init__(register,
            'ICBOF2', 'TIMER0.IFS.ICBOF2', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFS_ICBOF3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFS_ICBOF3, self).__init__(register,
            'ICBOF3', 'TIMER0.IFS.ICBOF3', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFC_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFC_OF, self).__init__(register,
            'OF', 'TIMER0.IFC.OF', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFC_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFC_UF, self).__init__(register,
            'UF', 'TIMER0.IFC.UF', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFC_DIRCHG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFC_DIRCHG, self).__init__(register,
            'DIRCHG', 'TIMER0.IFC.DIRCHG', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFC_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFC_CC0, self).__init__(register,
            'CC0', 'TIMER0.IFC.CC0', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFC_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFC_CC1, self).__init__(register,
            'CC1', 'TIMER0.IFC.CC1', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFC_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFC_CC2, self).__init__(register,
            'CC2', 'TIMER0.IFC.CC2', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFC_CC3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFC_CC3, self).__init__(register,
            'CC3', 'TIMER0.IFC.CC3', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFC_ICBOF0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFC_ICBOF0, self).__init__(register,
            'ICBOF0', 'TIMER0.IFC.ICBOF0', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFC_ICBOF1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFC_ICBOF1, self).__init__(register,
            'ICBOF1', 'TIMER0.IFC.ICBOF1', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFC_ICBOF2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFC_ICBOF2, self).__init__(register,
            'ICBOF2', 'TIMER0.IFC.ICBOF2', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IFC_ICBOF3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IFC_ICBOF3, self).__init__(register,
            'ICBOF3', 'TIMER0.IFC.ICBOF3', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IEN_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IEN_OF, self).__init__(register,
            'OF', 'TIMER0.IEN.OF', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IEN_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IEN_UF, self).__init__(register,
            'UF', 'TIMER0.IEN.UF', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IEN_DIRCHG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IEN_DIRCHG, self).__init__(register,
            'DIRCHG', 'TIMER0.IEN.DIRCHG', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IEN_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IEN_CC0, self).__init__(register,
            'CC0', 'TIMER0.IEN.CC0', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IEN_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IEN_CC1, self).__init__(register,
            'CC1', 'TIMER0.IEN.CC1', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IEN_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IEN_CC2, self).__init__(register,
            'CC2', 'TIMER0.IEN.CC2', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IEN_CC3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IEN_CC3, self).__init__(register,
            'CC3', 'TIMER0.IEN.CC3', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IEN_ICBOF0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IEN_ICBOF0, self).__init__(register,
            'ICBOF0', 'TIMER0.IEN.ICBOF0', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IEN_ICBOF1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IEN_ICBOF1, self).__init__(register,
            'ICBOF1', 'TIMER0.IEN.ICBOF1', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IEN_ICBOF2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IEN_ICBOF2, self).__init__(register,
            'ICBOF2', 'TIMER0.IEN.ICBOF2', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_IEN_ICBOF3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_IEN_ICBOF3, self).__init__(register,
            'ICBOF3', 'TIMER0.IEN.ICBOF3', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_TOP_TOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_TOP_TOP, self).__init__(register,
            'TOP', 'TIMER0.TOP.TOP', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_TOPB_TOPB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_TOPB_TOPB, self).__init__(register,
            'TOPB', 'TIMER0.TOPB.TOPB', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CNT_CNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CNT_CNT, self).__init__(register,
            'CNT', 'TIMER0.CNT.CNT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_LOCK_TIMERLOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_LOCK_TIMERLOCKKEY, self).__init__(register,
            'TIMERLOCKKEY', 'TIMER0.LOCK.TIMERLOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_TIMER0_LOCK_TIMERLOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_ROUTEPEN_CC0PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_ROUTEPEN_CC0PEN, self).__init__(register,
            'CC0PEN', 'TIMER0.ROUTEPEN.CC0PEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_ROUTEPEN_CC1PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_ROUTEPEN_CC1PEN, self).__init__(register,
            'CC1PEN', 'TIMER0.ROUTEPEN.CC1PEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_ROUTEPEN_CC2PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_ROUTEPEN_CC2PEN, self).__init__(register,
            'CC2PEN', 'TIMER0.ROUTEPEN.CC2PEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_ROUTEPEN_CC3PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_ROUTEPEN_CC3PEN, self).__init__(register,
            'CC3PEN', 'TIMER0.ROUTEPEN.CC3PEN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_ROUTEPEN_CDTI0PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_ROUTEPEN_CDTI0PEN, self).__init__(register,
            'CDTI0PEN', 'TIMER0.ROUTEPEN.CDTI0PEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_ROUTEPEN_CDTI1PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_ROUTEPEN_CDTI1PEN, self).__init__(register,
            'CDTI1PEN', 'TIMER0.ROUTEPEN.CDTI1PEN', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_ROUTEPEN_CDTI2PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_ROUTEPEN_CDTI2PEN, self).__init__(register,
            'CDTI2PEN', 'TIMER0.ROUTEPEN.CDTI2PEN', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_ROUTELOC0_CC0LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_ROUTELOC0_CC0LOC, self).__init__(register,
            'CC0LOC', 'TIMER0.ROUTELOC0.CC0LOC', 'read-write',
            "",
            0, 6,
            RM_Enum_TIMER0_ROUTELOC0_CC0LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_ROUTELOC0_CC1LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_ROUTELOC0_CC1LOC, self).__init__(register,
            'CC1LOC', 'TIMER0.ROUTELOC0.CC1LOC', 'read-write',
            "",
            8, 6,
            RM_Enum_TIMER0_ROUTELOC0_CC1LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_ROUTELOC0_CC2LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_ROUTELOC0_CC2LOC, self).__init__(register,
            'CC2LOC', 'TIMER0.ROUTELOC0.CC2LOC', 'read-write',
            "",
            16, 6,
            RM_Enum_TIMER0_ROUTELOC0_CC2LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_ROUTELOC0_CC3LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_ROUTELOC0_CC3LOC, self).__init__(register,
            'CC3LOC', 'TIMER0.ROUTELOC0.CC3LOC', 'read-write',
            "",
            24, 6,
            RM_Enum_TIMER0_ROUTELOC0_CC3LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_ROUTELOC2_CDTI0LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_ROUTELOC2_CDTI0LOC, self).__init__(register,
            'CDTI0LOC', 'TIMER0.ROUTELOC2.CDTI0LOC', 'read-write',
            "",
            0, 6,
            RM_Enum_TIMER0_ROUTELOC2_CDTI0LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_ROUTELOC2_CDTI1LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_ROUTELOC2_CDTI1LOC, self).__init__(register,
            'CDTI1LOC', 'TIMER0.ROUTELOC2.CDTI1LOC', 'read-write',
            "",
            8, 6,
            RM_Enum_TIMER0_ROUTELOC2_CDTI1LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_ROUTELOC2_CDTI2LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_ROUTELOC2_CDTI2LOC, self).__init__(register,
            'CDTI2LOC', 'TIMER0.ROUTELOC2.CDTI2LOC', 'read-write',
            "",
            16, 6,
            RM_Enum_TIMER0_ROUTELOC2_CDTI2LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CTRL_MODE, self).__init__(register,
            'MODE', 'TIMER0.CC0_CTRL.MODE', 'read-write',
            "",
            0, 2,
            RM_Enum_TIMER0_CC0_CTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CTRL_OUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CTRL_OUTINV, self).__init__(register,
            'OUTINV', 'TIMER0.CC0_CTRL.OUTINV', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CTRL_COIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CTRL_COIST, self).__init__(register,
            'COIST', 'TIMER0.CC0_CTRL.COIST', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CTRL_CMOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CTRL_CMOA, self).__init__(register,
            'CMOA', 'TIMER0.CC0_CTRL.CMOA', 'read-write',
            "",
            8, 2,
            RM_Enum_TIMER0_CC0_CTRL_CMOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CTRL_COFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CTRL_COFOA, self).__init__(register,
            'COFOA', 'TIMER0.CC0_CTRL.COFOA', 'read-write',
            "",
            10, 2,
            RM_Enum_TIMER0_CC0_CTRL_COFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CTRL_CUFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CTRL_CUFOA, self).__init__(register,
            'CUFOA', 'TIMER0.CC0_CTRL.CUFOA', 'read-write',
            "",
            12, 2,
            RM_Enum_TIMER0_CC0_CTRL_CUFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'TIMER0.CC0_CTRL.PRSSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_TIMER0_CC0_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'TIMER0.CC0_CTRL.ICEDGE', 'read-write',
            "",
            24, 2,
            RM_Enum_TIMER0_CC0_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CTRL_ICEVCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CTRL_ICEVCTRL, self).__init__(register,
            'ICEVCTRL', 'TIMER0.CC0_CTRL.ICEVCTRL', 'read-write',
            "",
            26, 2,
            RM_Enum_TIMER0_CC0_CTRL_ICEVCTRL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CTRL_PRSCONF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CTRL_PRSCONF, self).__init__(register,
            'PRSCONF', 'TIMER0.CC0_CTRL.PRSCONF', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CTRL_INSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CTRL_INSEL, self).__init__(register,
            'INSEL', 'TIMER0.CC0_CTRL.INSEL', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CTRL_FILT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CTRL_FILT, self).__init__(register,
            'FILT', 'TIMER0.CC0_CTRL.FILT', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CCV_CCV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CCV_CCV, self).__init__(register,
            'CCV', 'TIMER0.CC0_CCV.CCV', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CCVP_CCVP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CCVP_CCVP, self).__init__(register,
            'CCVP', 'TIMER0.CC0_CCVP.CCVP', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC0_CCVB_CCVB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC0_CCVB_CCVB, self).__init__(register,
            'CCVB', 'TIMER0.CC0_CCVB.CCVB', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CTRL_MODE, self).__init__(register,
            'MODE', 'TIMER0.CC1_CTRL.MODE', 'read-write',
            "",
            0, 2,
            RM_Enum_TIMER0_CC1_CTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CTRL_OUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CTRL_OUTINV, self).__init__(register,
            'OUTINV', 'TIMER0.CC1_CTRL.OUTINV', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CTRL_COIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CTRL_COIST, self).__init__(register,
            'COIST', 'TIMER0.CC1_CTRL.COIST', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CTRL_CMOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CTRL_CMOA, self).__init__(register,
            'CMOA', 'TIMER0.CC1_CTRL.CMOA', 'read-write',
            "",
            8, 2,
            RM_Enum_TIMER0_CC1_CTRL_CMOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CTRL_COFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CTRL_COFOA, self).__init__(register,
            'COFOA', 'TIMER0.CC1_CTRL.COFOA', 'read-write',
            "",
            10, 2,
            RM_Enum_TIMER0_CC1_CTRL_COFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CTRL_CUFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CTRL_CUFOA, self).__init__(register,
            'CUFOA', 'TIMER0.CC1_CTRL.CUFOA', 'read-write',
            "",
            12, 2,
            RM_Enum_TIMER0_CC1_CTRL_CUFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'TIMER0.CC1_CTRL.PRSSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_TIMER0_CC1_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'TIMER0.CC1_CTRL.ICEDGE', 'read-write',
            "",
            24, 2,
            RM_Enum_TIMER0_CC1_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CTRL_ICEVCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CTRL_ICEVCTRL, self).__init__(register,
            'ICEVCTRL', 'TIMER0.CC1_CTRL.ICEVCTRL', 'read-write',
            "",
            26, 2,
            RM_Enum_TIMER0_CC1_CTRL_ICEVCTRL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CTRL_PRSCONF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CTRL_PRSCONF, self).__init__(register,
            'PRSCONF', 'TIMER0.CC1_CTRL.PRSCONF', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CTRL_INSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CTRL_INSEL, self).__init__(register,
            'INSEL', 'TIMER0.CC1_CTRL.INSEL', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CTRL_FILT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CTRL_FILT, self).__init__(register,
            'FILT', 'TIMER0.CC1_CTRL.FILT', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CCV_CCV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CCV_CCV, self).__init__(register,
            'CCV', 'TIMER0.CC1_CCV.CCV', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CCVP_CCVP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CCVP_CCVP, self).__init__(register,
            'CCVP', 'TIMER0.CC1_CCVP.CCVP', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC1_CCVB_CCVB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC1_CCVB_CCVB, self).__init__(register,
            'CCVB', 'TIMER0.CC1_CCVB.CCVB', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CTRL_MODE, self).__init__(register,
            'MODE', 'TIMER0.CC2_CTRL.MODE', 'read-write',
            "",
            0, 2,
            RM_Enum_TIMER0_CC2_CTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CTRL_OUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CTRL_OUTINV, self).__init__(register,
            'OUTINV', 'TIMER0.CC2_CTRL.OUTINV', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CTRL_COIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CTRL_COIST, self).__init__(register,
            'COIST', 'TIMER0.CC2_CTRL.COIST', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CTRL_CMOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CTRL_CMOA, self).__init__(register,
            'CMOA', 'TIMER0.CC2_CTRL.CMOA', 'read-write',
            "",
            8, 2,
            RM_Enum_TIMER0_CC2_CTRL_CMOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CTRL_COFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CTRL_COFOA, self).__init__(register,
            'COFOA', 'TIMER0.CC2_CTRL.COFOA', 'read-write',
            "",
            10, 2,
            RM_Enum_TIMER0_CC2_CTRL_COFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CTRL_CUFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CTRL_CUFOA, self).__init__(register,
            'CUFOA', 'TIMER0.CC2_CTRL.CUFOA', 'read-write',
            "",
            12, 2,
            RM_Enum_TIMER0_CC2_CTRL_CUFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'TIMER0.CC2_CTRL.PRSSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_TIMER0_CC2_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'TIMER0.CC2_CTRL.ICEDGE', 'read-write',
            "",
            24, 2,
            RM_Enum_TIMER0_CC2_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CTRL_ICEVCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CTRL_ICEVCTRL, self).__init__(register,
            'ICEVCTRL', 'TIMER0.CC2_CTRL.ICEVCTRL', 'read-write',
            "",
            26, 2,
            RM_Enum_TIMER0_CC2_CTRL_ICEVCTRL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CTRL_PRSCONF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CTRL_PRSCONF, self).__init__(register,
            'PRSCONF', 'TIMER0.CC2_CTRL.PRSCONF', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CTRL_INSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CTRL_INSEL, self).__init__(register,
            'INSEL', 'TIMER0.CC2_CTRL.INSEL', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CTRL_FILT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CTRL_FILT, self).__init__(register,
            'FILT', 'TIMER0.CC2_CTRL.FILT', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CCV_CCV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CCV_CCV, self).__init__(register,
            'CCV', 'TIMER0.CC2_CCV.CCV', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CCVP_CCVP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CCVP_CCVP, self).__init__(register,
            'CCVP', 'TIMER0.CC2_CCVP.CCVP', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC2_CCVB_CCVB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC2_CCVB_CCVB, self).__init__(register,
            'CCVB', 'TIMER0.CC2_CCVB.CCVB', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CTRL_MODE, self).__init__(register,
            'MODE', 'TIMER0.CC3_CTRL.MODE', 'read-write',
            "",
            0, 2,
            RM_Enum_TIMER0_CC3_CTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CTRL_OUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CTRL_OUTINV, self).__init__(register,
            'OUTINV', 'TIMER0.CC3_CTRL.OUTINV', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CTRL_COIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CTRL_COIST, self).__init__(register,
            'COIST', 'TIMER0.CC3_CTRL.COIST', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CTRL_CMOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CTRL_CMOA, self).__init__(register,
            'CMOA', 'TIMER0.CC3_CTRL.CMOA', 'read-write',
            "",
            8, 2,
            RM_Enum_TIMER0_CC3_CTRL_CMOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CTRL_COFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CTRL_COFOA, self).__init__(register,
            'COFOA', 'TIMER0.CC3_CTRL.COFOA', 'read-write',
            "",
            10, 2,
            RM_Enum_TIMER0_CC3_CTRL_COFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CTRL_CUFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CTRL_CUFOA, self).__init__(register,
            'CUFOA', 'TIMER0.CC3_CTRL.CUFOA', 'read-write',
            "",
            12, 2,
            RM_Enum_TIMER0_CC3_CTRL_CUFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'TIMER0.CC3_CTRL.PRSSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_TIMER0_CC3_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'TIMER0.CC3_CTRL.ICEDGE', 'read-write',
            "",
            24, 2,
            RM_Enum_TIMER0_CC3_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CTRL_ICEVCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CTRL_ICEVCTRL, self).__init__(register,
            'ICEVCTRL', 'TIMER0.CC3_CTRL.ICEVCTRL', 'read-write',
            "",
            26, 2,
            RM_Enum_TIMER0_CC3_CTRL_ICEVCTRL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CTRL_PRSCONF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CTRL_PRSCONF, self).__init__(register,
            'PRSCONF', 'TIMER0.CC3_CTRL.PRSCONF', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CTRL_INSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CTRL_INSEL, self).__init__(register,
            'INSEL', 'TIMER0.CC3_CTRL.INSEL', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CTRL_FILT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CTRL_FILT, self).__init__(register,
            'FILT', 'TIMER0.CC3_CTRL.FILT', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CCV_CCV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CCV_CCV, self).__init__(register,
            'CCV', 'TIMER0.CC3_CCV.CCV', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CCVP_CCVP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CCVP_CCVP, self).__init__(register,
            'CCVP', 'TIMER0.CC3_CCVP.CCVP', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_CC3_CCVB_CCVB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_CC3_CCVB_CCVB, self).__init__(register,
            'CCVB', 'TIMER0.CC3_CCVB.CCVB', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTCTRL_DTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTCTRL_DTEN, self).__init__(register,
            'DTEN', 'TIMER0.DTCTRL.DTEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTCTRL_DTDAS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTCTRL_DTDAS, self).__init__(register,
            'DTDAS', 'TIMER0.DTCTRL.DTDAS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTCTRL_DTIPOL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTCTRL_DTIPOL, self).__init__(register,
            'DTIPOL', 'TIMER0.DTCTRL.DTIPOL', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTCTRL_DTCINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTCTRL_DTCINV, self).__init__(register,
            'DTCINV', 'TIMER0.DTCTRL.DTCINV', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTCTRL_DTPRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTCTRL_DTPRSSEL, self).__init__(register,
            'DTPRSSEL', 'TIMER0.DTCTRL.DTPRSSEL', 'read-write',
            "",
            4, 4,
            RM_Enum_TIMER0_DTCTRL_DTPRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTCTRL_DTAR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTCTRL_DTAR, self).__init__(register,
            'DTAR', 'TIMER0.DTCTRL.DTAR', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTCTRL_DTFATS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTCTRL_DTFATS, self).__init__(register,
            'DTFATS', 'TIMER0.DTCTRL.DTFATS', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTCTRL_DTPRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTCTRL_DTPRSEN, self).__init__(register,
            'DTPRSEN', 'TIMER0.DTCTRL.DTPRSEN', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTTIME_DTPRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTTIME_DTPRESC, self).__init__(register,
            'DTPRESC', 'TIMER0.DTTIME.DTPRESC', 'read-write',
            "",
            0, 4,
            RM_Enum_TIMER0_DTTIME_DTPRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTTIME_DTRISET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTTIME_DTRISET, self).__init__(register,
            'DTRISET', 'TIMER0.DTTIME.DTRISET', 'read-write',
            "",
            8, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTTIME_DTFALLT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTTIME_DTFALLT, self).__init__(register,
            'DTFALLT', 'TIMER0.DTTIME.DTFALLT', 'read-write',
            "",
            16, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFC_DTPRS0FSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFC_DTPRS0FSEL, self).__init__(register,
            'DTPRS0FSEL', 'TIMER0.DTFC.DTPRS0FSEL', 'read-write',
            "",
            0, 4,
            RM_Enum_TIMER0_DTFC_DTPRS0FSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFC_DTPRS1FSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFC_DTPRS1FSEL, self).__init__(register,
            'DTPRS1FSEL', 'TIMER0.DTFC.DTPRS1FSEL', 'read-write',
            "",
            8, 4,
            RM_Enum_TIMER0_DTFC_DTPRS1FSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFC_DTFA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFC_DTFA, self).__init__(register,
            'DTFA', 'TIMER0.DTFC.DTFA', 'read-write',
            "",
            16, 2,
            RM_Enum_TIMER0_DTFC_DTFA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFC_DTPRS0FEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFC_DTPRS0FEN, self).__init__(register,
            'DTPRS0FEN', 'TIMER0.DTFC.DTPRS0FEN', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFC_DTPRS1FEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFC_DTPRS1FEN, self).__init__(register,
            'DTPRS1FEN', 'TIMER0.DTFC.DTPRS1FEN', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFC_DTDBGFEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFC_DTDBGFEN, self).__init__(register,
            'DTDBGFEN', 'TIMER0.DTFC.DTDBGFEN', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFC_DTLOCKUPFEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFC_DTLOCKUPFEN, self).__init__(register,
            'DTLOCKUPFEN', 'TIMER0.DTFC.DTLOCKUPFEN', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTOGEN_DTOGCC0EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTOGEN_DTOGCC0EN, self).__init__(register,
            'DTOGCC0EN', 'TIMER0.DTOGEN.DTOGCC0EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTOGEN_DTOGCC1EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTOGEN_DTOGCC1EN, self).__init__(register,
            'DTOGCC1EN', 'TIMER0.DTOGEN.DTOGCC1EN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTOGEN_DTOGCC2EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTOGEN_DTOGCC2EN, self).__init__(register,
            'DTOGCC2EN', 'TIMER0.DTOGEN.DTOGCC2EN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTOGEN_DTOGCDTI0EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTOGEN_DTOGCDTI0EN, self).__init__(register,
            'DTOGCDTI0EN', 'TIMER0.DTOGEN.DTOGCDTI0EN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTOGEN_DTOGCDTI1EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTOGEN_DTOGCDTI1EN, self).__init__(register,
            'DTOGCDTI1EN', 'TIMER0.DTOGEN.DTOGCDTI1EN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTOGEN_DTOGCDTI2EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTOGEN_DTOGCDTI2EN, self).__init__(register,
            'DTOGCDTI2EN', 'TIMER0.DTOGEN.DTOGCDTI2EN', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFAULT_DTPRS0F(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFAULT_DTPRS0F, self).__init__(register,
            'DTPRS0F', 'TIMER0.DTFAULT.DTPRS0F', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFAULT_DTPRS1F(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFAULT_DTPRS1F, self).__init__(register,
            'DTPRS1F', 'TIMER0.DTFAULT.DTPRS1F', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFAULT_DTDBGF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFAULT_DTDBGF, self).__init__(register,
            'DTDBGF', 'TIMER0.DTFAULT.DTDBGF', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFAULT_DTLOCKUPF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFAULT_DTLOCKUPF, self).__init__(register,
            'DTLOCKUPF', 'TIMER0.DTFAULT.DTLOCKUPF', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFAULTC_DTPRS0FC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFAULTC_DTPRS0FC, self).__init__(register,
            'DTPRS0FC', 'TIMER0.DTFAULTC.DTPRS0FC', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFAULTC_DTPRS1FC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFAULTC_DTPRS1FC, self).__init__(register,
            'DTPRS1FC', 'TIMER0.DTFAULTC.DTPRS1FC', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFAULTC_DTDBGFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFAULTC_DTDBGFC, self).__init__(register,
            'DTDBGFC', 'TIMER0.DTFAULTC.DTDBGFC', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTFAULTC_TLOCKUPFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTFAULTC_TLOCKUPFC, self).__init__(register,
            'TLOCKUPFC', 'TIMER0.DTFAULTC.TLOCKUPFC', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER0_DTLOCK_LOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER0_DTLOCK_LOCKKEY, self).__init__(register,
            'LOCKKEY', 'TIMER0.DTLOCK.LOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_TIMER0_DTLOCK_LOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


