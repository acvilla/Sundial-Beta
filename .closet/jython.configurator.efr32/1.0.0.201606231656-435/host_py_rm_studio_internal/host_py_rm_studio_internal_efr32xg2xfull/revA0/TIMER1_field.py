
from static import Base_RM_Field
from TIMER1_enum import *


class RM_Field_TIMER1_CTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CTRL_MODE, self).__init__(register,
            'MODE', 'TIMER1.CTRL.MODE', 'read-write',
            "",
            0, 2,
            RM_Enum_TIMER1_CTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CTRL_SYNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CTRL_SYNC, self).__init__(register,
            'SYNC', 'TIMER1.CTRL.SYNC', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CTRL_OSMEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CTRL_OSMEN, self).__init__(register,
            'OSMEN', 'TIMER1.CTRL.OSMEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CTRL_QDM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CTRL_QDM, self).__init__(register,
            'QDM', 'TIMER1.CTRL.QDM', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CTRL_DEBUGRUN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CTRL_DEBUGRUN, self).__init__(register,
            'DEBUGRUN', 'TIMER1.CTRL.DEBUGRUN', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CTRL_DMACLRACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CTRL_DMACLRACT, self).__init__(register,
            'DMACLRACT', 'TIMER1.CTRL.DMACLRACT', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CTRL_RISEA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CTRL_RISEA, self).__init__(register,
            'RISEA', 'TIMER1.CTRL.RISEA', 'read-write',
            "",
            8, 2,
            RM_Enum_TIMER1_CTRL_RISEA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CTRL_FALLA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CTRL_FALLA, self).__init__(register,
            'FALLA', 'TIMER1.CTRL.FALLA', 'read-write',
            "",
            10, 2,
            RM_Enum_TIMER1_CTRL_FALLA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CTRL_X2CNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CTRL_X2CNT, self).__init__(register,
            'X2CNT', 'TIMER1.CTRL.X2CNT', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CTRL_CLKSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CTRL_CLKSEL, self).__init__(register,
            'CLKSEL', 'TIMER1.CTRL.CLKSEL', 'read-write',
            "",
            16, 2,
            RM_Enum_TIMER1_CTRL_CLKSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CTRL_PRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CTRL_PRESC, self).__init__(register,
            'PRESC', 'TIMER1.CTRL.PRESC', 'read-write',
            "",
            24, 4,
            RM_Enum_TIMER1_CTRL_PRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CTRL_ATI(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CTRL_ATI, self).__init__(register,
            'ATI', 'TIMER1.CTRL.ATI', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CTRL_RSSCOIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CTRL_RSSCOIST, self).__init__(register,
            'RSSCOIST', 'TIMER1.CTRL.RSSCOIST', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CMD_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CMD_START, self).__init__(register,
            'START', 'TIMER1.CMD.START', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CMD_STOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CMD_STOP, self).__init__(register,
            'STOP', 'TIMER1.CMD.STOP', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_RUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_RUNNING, self).__init__(register,
            'RUNNING', 'TIMER1.STATUS.RUNNING', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_DIR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_DIR, self).__init__(register,
            'DIR', 'TIMER1.STATUS.DIR', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_TOPBV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_TOPBV, self).__init__(register,
            'TOPBV', 'TIMER1.STATUS.TOPBV', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_CCVBV0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_CCVBV0, self).__init__(register,
            'CCVBV0', 'TIMER1.STATUS.CCVBV0', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_CCVBV1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_CCVBV1, self).__init__(register,
            'CCVBV1', 'TIMER1.STATUS.CCVBV1', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_CCVBV2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_CCVBV2, self).__init__(register,
            'CCVBV2', 'TIMER1.STATUS.CCVBV2', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_CCVBV3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_CCVBV3, self).__init__(register,
            'CCVBV3', 'TIMER1.STATUS.CCVBV3', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_ICV0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_ICV0, self).__init__(register,
            'ICV0', 'TIMER1.STATUS.ICV0', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_ICV1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_ICV1, self).__init__(register,
            'ICV1', 'TIMER1.STATUS.ICV1', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_ICV2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_ICV2, self).__init__(register,
            'ICV2', 'TIMER1.STATUS.ICV2', 'read-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_ICV3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_ICV3, self).__init__(register,
            'ICV3', 'TIMER1.STATUS.ICV3', 'read-only',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_CCPOL0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_CCPOL0, self).__init__(register,
            'CCPOL0', 'TIMER1.STATUS.CCPOL0', 'read-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_CCPOL1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_CCPOL1, self).__init__(register,
            'CCPOL1', 'TIMER1.STATUS.CCPOL1', 'read-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_CCPOL2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_CCPOL2, self).__init__(register,
            'CCPOL2', 'TIMER1.STATUS.CCPOL2', 'read-only',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_STATUS_CCPOL3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_STATUS_CCPOL3, self).__init__(register,
            'CCPOL3', 'TIMER1.STATUS.CCPOL3', 'read-only',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IF_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IF_OF, self).__init__(register,
            'OF', 'TIMER1.IF.OF', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IF_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IF_UF, self).__init__(register,
            'UF', 'TIMER1.IF.UF', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IF_DIRCHG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IF_DIRCHG, self).__init__(register,
            'DIRCHG', 'TIMER1.IF.DIRCHG', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IF_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IF_CC0, self).__init__(register,
            'CC0', 'TIMER1.IF.CC0', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IF_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IF_CC1, self).__init__(register,
            'CC1', 'TIMER1.IF.CC1', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IF_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IF_CC2, self).__init__(register,
            'CC2', 'TIMER1.IF.CC2', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IF_CC3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IF_CC3, self).__init__(register,
            'CC3', 'TIMER1.IF.CC3', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IF_ICBOF0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IF_ICBOF0, self).__init__(register,
            'ICBOF0', 'TIMER1.IF.ICBOF0', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IF_ICBOF1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IF_ICBOF1, self).__init__(register,
            'ICBOF1', 'TIMER1.IF.ICBOF1', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IF_ICBOF2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IF_ICBOF2, self).__init__(register,
            'ICBOF2', 'TIMER1.IF.ICBOF2', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IF_ICBOF3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IF_ICBOF3, self).__init__(register,
            'ICBOF3', 'TIMER1.IF.ICBOF3', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFS_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFS_OF, self).__init__(register,
            'OF', 'TIMER1.IFS.OF', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFS_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFS_UF, self).__init__(register,
            'UF', 'TIMER1.IFS.UF', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFS_DIRCHG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFS_DIRCHG, self).__init__(register,
            'DIRCHG', 'TIMER1.IFS.DIRCHG', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFS_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFS_CC0, self).__init__(register,
            'CC0', 'TIMER1.IFS.CC0', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFS_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFS_CC1, self).__init__(register,
            'CC1', 'TIMER1.IFS.CC1', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFS_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFS_CC2, self).__init__(register,
            'CC2', 'TIMER1.IFS.CC2', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFS_CC3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFS_CC3, self).__init__(register,
            'CC3', 'TIMER1.IFS.CC3', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFS_ICBOF0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFS_ICBOF0, self).__init__(register,
            'ICBOF0', 'TIMER1.IFS.ICBOF0', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFS_ICBOF1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFS_ICBOF1, self).__init__(register,
            'ICBOF1', 'TIMER1.IFS.ICBOF1', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFS_ICBOF2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFS_ICBOF2, self).__init__(register,
            'ICBOF2', 'TIMER1.IFS.ICBOF2', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFS_ICBOF3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFS_ICBOF3, self).__init__(register,
            'ICBOF3', 'TIMER1.IFS.ICBOF3', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFC_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFC_OF, self).__init__(register,
            'OF', 'TIMER1.IFC.OF', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFC_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFC_UF, self).__init__(register,
            'UF', 'TIMER1.IFC.UF', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFC_DIRCHG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFC_DIRCHG, self).__init__(register,
            'DIRCHG', 'TIMER1.IFC.DIRCHG', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFC_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFC_CC0, self).__init__(register,
            'CC0', 'TIMER1.IFC.CC0', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFC_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFC_CC1, self).__init__(register,
            'CC1', 'TIMER1.IFC.CC1', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFC_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFC_CC2, self).__init__(register,
            'CC2', 'TIMER1.IFC.CC2', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFC_CC3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFC_CC3, self).__init__(register,
            'CC3', 'TIMER1.IFC.CC3', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFC_ICBOF0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFC_ICBOF0, self).__init__(register,
            'ICBOF0', 'TIMER1.IFC.ICBOF0', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFC_ICBOF1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFC_ICBOF1, self).__init__(register,
            'ICBOF1', 'TIMER1.IFC.ICBOF1', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFC_ICBOF2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFC_ICBOF2, self).__init__(register,
            'ICBOF2', 'TIMER1.IFC.ICBOF2', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IFC_ICBOF3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IFC_ICBOF3, self).__init__(register,
            'ICBOF3', 'TIMER1.IFC.ICBOF3', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IEN_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IEN_OF, self).__init__(register,
            'OF', 'TIMER1.IEN.OF', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IEN_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IEN_UF, self).__init__(register,
            'UF', 'TIMER1.IEN.UF', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IEN_DIRCHG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IEN_DIRCHG, self).__init__(register,
            'DIRCHG', 'TIMER1.IEN.DIRCHG', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IEN_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IEN_CC0, self).__init__(register,
            'CC0', 'TIMER1.IEN.CC0', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IEN_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IEN_CC1, self).__init__(register,
            'CC1', 'TIMER1.IEN.CC1', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IEN_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IEN_CC2, self).__init__(register,
            'CC2', 'TIMER1.IEN.CC2', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IEN_CC3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IEN_CC3, self).__init__(register,
            'CC3', 'TIMER1.IEN.CC3', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IEN_ICBOF0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IEN_ICBOF0, self).__init__(register,
            'ICBOF0', 'TIMER1.IEN.ICBOF0', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IEN_ICBOF1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IEN_ICBOF1, self).__init__(register,
            'ICBOF1', 'TIMER1.IEN.ICBOF1', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IEN_ICBOF2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IEN_ICBOF2, self).__init__(register,
            'ICBOF2', 'TIMER1.IEN.ICBOF2', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_IEN_ICBOF3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_IEN_ICBOF3, self).__init__(register,
            'ICBOF3', 'TIMER1.IEN.ICBOF3', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_TOP_TOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_TOP_TOP, self).__init__(register,
            'TOP', 'TIMER1.TOP.TOP', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_TOPB_TOPB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_TOPB_TOPB, self).__init__(register,
            'TOPB', 'TIMER1.TOPB.TOPB', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CNT_CNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CNT_CNT, self).__init__(register,
            'CNT', 'TIMER1.CNT.CNT', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_LOCK_TIMERLOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_LOCK_TIMERLOCKKEY, self).__init__(register,
            'TIMERLOCKKEY', 'TIMER1.LOCK.TIMERLOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_TIMER1_LOCK_TIMERLOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_ROUTEPEN_CC0PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_ROUTEPEN_CC0PEN, self).__init__(register,
            'CC0PEN', 'TIMER1.ROUTEPEN.CC0PEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_ROUTEPEN_CC1PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_ROUTEPEN_CC1PEN, self).__init__(register,
            'CC1PEN', 'TIMER1.ROUTEPEN.CC1PEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_ROUTEPEN_CC2PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_ROUTEPEN_CC2PEN, self).__init__(register,
            'CC2PEN', 'TIMER1.ROUTEPEN.CC2PEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_ROUTEPEN_CC3PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_ROUTEPEN_CC3PEN, self).__init__(register,
            'CC3PEN', 'TIMER1.ROUTEPEN.CC3PEN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_ROUTEPEN_CDTI0PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_ROUTEPEN_CDTI0PEN, self).__init__(register,
            'CDTI0PEN', 'TIMER1.ROUTEPEN.CDTI0PEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_ROUTEPEN_CDTI1PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_ROUTEPEN_CDTI1PEN, self).__init__(register,
            'CDTI1PEN', 'TIMER1.ROUTEPEN.CDTI1PEN', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_ROUTEPEN_CDTI2PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_ROUTEPEN_CDTI2PEN, self).__init__(register,
            'CDTI2PEN', 'TIMER1.ROUTEPEN.CDTI2PEN', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_ROUTELOC0_CC0LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_ROUTELOC0_CC0LOC, self).__init__(register,
            'CC0LOC', 'TIMER1.ROUTELOC0.CC0LOC', 'read-write',
            "",
            0, 6,
            RM_Enum_TIMER1_ROUTELOC0_CC0LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_ROUTELOC0_CC1LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_ROUTELOC0_CC1LOC, self).__init__(register,
            'CC1LOC', 'TIMER1.ROUTELOC0.CC1LOC', 'read-write',
            "",
            8, 6,
            RM_Enum_TIMER1_ROUTELOC0_CC1LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_ROUTELOC0_CC2LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_ROUTELOC0_CC2LOC, self).__init__(register,
            'CC2LOC', 'TIMER1.ROUTELOC0.CC2LOC', 'read-write',
            "",
            16, 6,
            RM_Enum_TIMER1_ROUTELOC0_CC2LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_ROUTELOC0_CC3LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_ROUTELOC0_CC3LOC, self).__init__(register,
            'CC3LOC', 'TIMER1.ROUTELOC0.CC3LOC', 'read-write',
            "",
            24, 6,
            RM_Enum_TIMER1_ROUTELOC0_CC3LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_ROUTELOC2_CDTI0LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_ROUTELOC2_CDTI0LOC, self).__init__(register,
            'CDTI0LOC', 'TIMER1.ROUTELOC2.CDTI0LOC', 'read-write',
            "",
            0, 6,
            RM_Enum_TIMER1_ROUTELOC2_CDTI0LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_ROUTELOC2_CDTI1LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_ROUTELOC2_CDTI1LOC, self).__init__(register,
            'CDTI1LOC', 'TIMER1.ROUTELOC2.CDTI1LOC', 'read-write',
            "",
            8, 6,
            RM_Enum_TIMER1_ROUTELOC2_CDTI1LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_ROUTELOC2_CDTI2LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_ROUTELOC2_CDTI2LOC, self).__init__(register,
            'CDTI2LOC', 'TIMER1.ROUTELOC2.CDTI2LOC', 'read-write',
            "",
            16, 6,
            RM_Enum_TIMER1_ROUTELOC2_CDTI2LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CTRL_MODE, self).__init__(register,
            'MODE', 'TIMER1.CC0_CTRL.MODE', 'read-write',
            "",
            0, 2,
            RM_Enum_TIMER1_CC0_CTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CTRL_OUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CTRL_OUTINV, self).__init__(register,
            'OUTINV', 'TIMER1.CC0_CTRL.OUTINV', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CTRL_COIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CTRL_COIST, self).__init__(register,
            'COIST', 'TIMER1.CC0_CTRL.COIST', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CTRL_CMOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CTRL_CMOA, self).__init__(register,
            'CMOA', 'TIMER1.CC0_CTRL.CMOA', 'read-write',
            "",
            8, 2,
            RM_Enum_TIMER1_CC0_CTRL_CMOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CTRL_COFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CTRL_COFOA, self).__init__(register,
            'COFOA', 'TIMER1.CC0_CTRL.COFOA', 'read-write',
            "",
            10, 2,
            RM_Enum_TIMER1_CC0_CTRL_COFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CTRL_CUFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CTRL_CUFOA, self).__init__(register,
            'CUFOA', 'TIMER1.CC0_CTRL.CUFOA', 'read-write',
            "",
            12, 2,
            RM_Enum_TIMER1_CC0_CTRL_CUFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'TIMER1.CC0_CTRL.PRSSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_TIMER1_CC0_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'TIMER1.CC0_CTRL.ICEDGE', 'read-write',
            "",
            24, 2,
            RM_Enum_TIMER1_CC0_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CTRL_ICEVCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CTRL_ICEVCTRL, self).__init__(register,
            'ICEVCTRL', 'TIMER1.CC0_CTRL.ICEVCTRL', 'read-write',
            "",
            26, 2,
            RM_Enum_TIMER1_CC0_CTRL_ICEVCTRL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CTRL_PRSCONF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CTRL_PRSCONF, self).__init__(register,
            'PRSCONF', 'TIMER1.CC0_CTRL.PRSCONF', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CTRL_INSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CTRL_INSEL, self).__init__(register,
            'INSEL', 'TIMER1.CC0_CTRL.INSEL', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CTRL_FILT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CTRL_FILT, self).__init__(register,
            'FILT', 'TIMER1.CC0_CTRL.FILT', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CCV_CCV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CCV_CCV, self).__init__(register,
            'CCV', 'TIMER1.CC0_CCV.CCV', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CCVP_CCVP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CCVP_CCVP, self).__init__(register,
            'CCVP', 'TIMER1.CC0_CCVP.CCVP', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC0_CCVB_CCVB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC0_CCVB_CCVB, self).__init__(register,
            'CCVB', 'TIMER1.CC0_CCVB.CCVB', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CTRL_MODE, self).__init__(register,
            'MODE', 'TIMER1.CC1_CTRL.MODE', 'read-write',
            "",
            0, 2,
            RM_Enum_TIMER1_CC1_CTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CTRL_OUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CTRL_OUTINV, self).__init__(register,
            'OUTINV', 'TIMER1.CC1_CTRL.OUTINV', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CTRL_COIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CTRL_COIST, self).__init__(register,
            'COIST', 'TIMER1.CC1_CTRL.COIST', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CTRL_CMOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CTRL_CMOA, self).__init__(register,
            'CMOA', 'TIMER1.CC1_CTRL.CMOA', 'read-write',
            "",
            8, 2,
            RM_Enum_TIMER1_CC1_CTRL_CMOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CTRL_COFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CTRL_COFOA, self).__init__(register,
            'COFOA', 'TIMER1.CC1_CTRL.COFOA', 'read-write',
            "",
            10, 2,
            RM_Enum_TIMER1_CC1_CTRL_COFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CTRL_CUFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CTRL_CUFOA, self).__init__(register,
            'CUFOA', 'TIMER1.CC1_CTRL.CUFOA', 'read-write',
            "",
            12, 2,
            RM_Enum_TIMER1_CC1_CTRL_CUFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'TIMER1.CC1_CTRL.PRSSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_TIMER1_CC1_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'TIMER1.CC1_CTRL.ICEDGE', 'read-write',
            "",
            24, 2,
            RM_Enum_TIMER1_CC1_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CTRL_ICEVCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CTRL_ICEVCTRL, self).__init__(register,
            'ICEVCTRL', 'TIMER1.CC1_CTRL.ICEVCTRL', 'read-write',
            "",
            26, 2,
            RM_Enum_TIMER1_CC1_CTRL_ICEVCTRL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CTRL_PRSCONF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CTRL_PRSCONF, self).__init__(register,
            'PRSCONF', 'TIMER1.CC1_CTRL.PRSCONF', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CTRL_INSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CTRL_INSEL, self).__init__(register,
            'INSEL', 'TIMER1.CC1_CTRL.INSEL', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CTRL_FILT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CTRL_FILT, self).__init__(register,
            'FILT', 'TIMER1.CC1_CTRL.FILT', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CCV_CCV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CCV_CCV, self).__init__(register,
            'CCV', 'TIMER1.CC1_CCV.CCV', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CCVP_CCVP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CCVP_CCVP, self).__init__(register,
            'CCVP', 'TIMER1.CC1_CCVP.CCVP', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC1_CCVB_CCVB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC1_CCVB_CCVB, self).__init__(register,
            'CCVB', 'TIMER1.CC1_CCVB.CCVB', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CTRL_MODE, self).__init__(register,
            'MODE', 'TIMER1.CC2_CTRL.MODE', 'read-write',
            "",
            0, 2,
            RM_Enum_TIMER1_CC2_CTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CTRL_OUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CTRL_OUTINV, self).__init__(register,
            'OUTINV', 'TIMER1.CC2_CTRL.OUTINV', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CTRL_COIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CTRL_COIST, self).__init__(register,
            'COIST', 'TIMER1.CC2_CTRL.COIST', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CTRL_CMOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CTRL_CMOA, self).__init__(register,
            'CMOA', 'TIMER1.CC2_CTRL.CMOA', 'read-write',
            "",
            8, 2,
            RM_Enum_TIMER1_CC2_CTRL_CMOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CTRL_COFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CTRL_COFOA, self).__init__(register,
            'COFOA', 'TIMER1.CC2_CTRL.COFOA', 'read-write',
            "",
            10, 2,
            RM_Enum_TIMER1_CC2_CTRL_COFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CTRL_CUFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CTRL_CUFOA, self).__init__(register,
            'CUFOA', 'TIMER1.CC2_CTRL.CUFOA', 'read-write',
            "",
            12, 2,
            RM_Enum_TIMER1_CC2_CTRL_CUFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'TIMER1.CC2_CTRL.PRSSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_TIMER1_CC2_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'TIMER1.CC2_CTRL.ICEDGE', 'read-write',
            "",
            24, 2,
            RM_Enum_TIMER1_CC2_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CTRL_ICEVCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CTRL_ICEVCTRL, self).__init__(register,
            'ICEVCTRL', 'TIMER1.CC2_CTRL.ICEVCTRL', 'read-write',
            "",
            26, 2,
            RM_Enum_TIMER1_CC2_CTRL_ICEVCTRL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CTRL_PRSCONF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CTRL_PRSCONF, self).__init__(register,
            'PRSCONF', 'TIMER1.CC2_CTRL.PRSCONF', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CTRL_INSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CTRL_INSEL, self).__init__(register,
            'INSEL', 'TIMER1.CC2_CTRL.INSEL', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CTRL_FILT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CTRL_FILT, self).__init__(register,
            'FILT', 'TIMER1.CC2_CTRL.FILT', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CCV_CCV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CCV_CCV, self).__init__(register,
            'CCV', 'TIMER1.CC2_CCV.CCV', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CCVP_CCVP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CCVP_CCVP, self).__init__(register,
            'CCVP', 'TIMER1.CC2_CCVP.CCVP', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC2_CCVB_CCVB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC2_CCVB_CCVB, self).__init__(register,
            'CCVB', 'TIMER1.CC2_CCVB.CCVB', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CTRL_MODE, self).__init__(register,
            'MODE', 'TIMER1.CC3_CTRL.MODE', 'read-write',
            "",
            0, 2,
            RM_Enum_TIMER1_CC3_CTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CTRL_OUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CTRL_OUTINV, self).__init__(register,
            'OUTINV', 'TIMER1.CC3_CTRL.OUTINV', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CTRL_COIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CTRL_COIST, self).__init__(register,
            'COIST', 'TIMER1.CC3_CTRL.COIST', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CTRL_CMOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CTRL_CMOA, self).__init__(register,
            'CMOA', 'TIMER1.CC3_CTRL.CMOA', 'read-write',
            "",
            8, 2,
            RM_Enum_TIMER1_CC3_CTRL_CMOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CTRL_COFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CTRL_COFOA, self).__init__(register,
            'COFOA', 'TIMER1.CC3_CTRL.COFOA', 'read-write',
            "",
            10, 2,
            RM_Enum_TIMER1_CC3_CTRL_COFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CTRL_CUFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CTRL_CUFOA, self).__init__(register,
            'CUFOA', 'TIMER1.CC3_CTRL.CUFOA', 'read-write',
            "",
            12, 2,
            RM_Enum_TIMER1_CC3_CTRL_CUFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'TIMER1.CC3_CTRL.PRSSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_TIMER1_CC3_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'TIMER1.CC3_CTRL.ICEDGE', 'read-write',
            "",
            24, 2,
            RM_Enum_TIMER1_CC3_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CTRL_ICEVCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CTRL_ICEVCTRL, self).__init__(register,
            'ICEVCTRL', 'TIMER1.CC3_CTRL.ICEVCTRL', 'read-write',
            "",
            26, 2,
            RM_Enum_TIMER1_CC3_CTRL_ICEVCTRL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CTRL_PRSCONF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CTRL_PRSCONF, self).__init__(register,
            'PRSCONF', 'TIMER1.CC3_CTRL.PRSCONF', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CTRL_INSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CTRL_INSEL, self).__init__(register,
            'INSEL', 'TIMER1.CC3_CTRL.INSEL', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CTRL_FILT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CTRL_FILT, self).__init__(register,
            'FILT', 'TIMER1.CC3_CTRL.FILT', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CCV_CCV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CCV_CCV, self).__init__(register,
            'CCV', 'TIMER1.CC3_CCV.CCV', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CCVP_CCVP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CCVP_CCVP, self).__init__(register,
            'CCVP', 'TIMER1.CC3_CCVP.CCVP', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_CC3_CCVB_CCVB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_CC3_CCVB_CCVB, self).__init__(register,
            'CCVB', 'TIMER1.CC3_CCVB.CCVB', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTCTRL_DTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTCTRL_DTEN, self).__init__(register,
            'DTEN', 'TIMER1.DTCTRL.DTEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTCTRL_DTDAS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTCTRL_DTDAS, self).__init__(register,
            'DTDAS', 'TIMER1.DTCTRL.DTDAS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTCTRL_DTIPOL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTCTRL_DTIPOL, self).__init__(register,
            'DTIPOL', 'TIMER1.DTCTRL.DTIPOL', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTCTRL_DTCINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTCTRL_DTCINV, self).__init__(register,
            'DTCINV', 'TIMER1.DTCTRL.DTCINV', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTCTRL_DTPRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTCTRL_DTPRSSEL, self).__init__(register,
            'DTPRSSEL', 'TIMER1.DTCTRL.DTPRSSEL', 'read-write',
            "",
            4, 4,
            RM_Enum_TIMER1_DTCTRL_DTPRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTCTRL_DTAR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTCTRL_DTAR, self).__init__(register,
            'DTAR', 'TIMER1.DTCTRL.DTAR', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTCTRL_DTFATS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTCTRL_DTFATS, self).__init__(register,
            'DTFATS', 'TIMER1.DTCTRL.DTFATS', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTCTRL_DTPRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTCTRL_DTPRSEN, self).__init__(register,
            'DTPRSEN', 'TIMER1.DTCTRL.DTPRSEN', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTTIME_DTPRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTTIME_DTPRESC, self).__init__(register,
            'DTPRESC', 'TIMER1.DTTIME.DTPRESC', 'read-write',
            "",
            0, 4,
            RM_Enum_TIMER1_DTTIME_DTPRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTTIME_DTRISET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTTIME_DTRISET, self).__init__(register,
            'DTRISET', 'TIMER1.DTTIME.DTRISET', 'read-write',
            "",
            8, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTTIME_DTFALLT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTTIME_DTFALLT, self).__init__(register,
            'DTFALLT', 'TIMER1.DTTIME.DTFALLT', 'read-write',
            "",
            16, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFC_DTPRS0FSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFC_DTPRS0FSEL, self).__init__(register,
            'DTPRS0FSEL', 'TIMER1.DTFC.DTPRS0FSEL', 'read-write',
            "",
            0, 4,
            RM_Enum_TIMER1_DTFC_DTPRS0FSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFC_DTPRS1FSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFC_DTPRS1FSEL, self).__init__(register,
            'DTPRS1FSEL', 'TIMER1.DTFC.DTPRS1FSEL', 'read-write',
            "",
            8, 4,
            RM_Enum_TIMER1_DTFC_DTPRS1FSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFC_DTFA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFC_DTFA, self).__init__(register,
            'DTFA', 'TIMER1.DTFC.DTFA', 'read-write',
            "",
            16, 2,
            RM_Enum_TIMER1_DTFC_DTFA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFC_DTPRS0FEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFC_DTPRS0FEN, self).__init__(register,
            'DTPRS0FEN', 'TIMER1.DTFC.DTPRS0FEN', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFC_DTPRS1FEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFC_DTPRS1FEN, self).__init__(register,
            'DTPRS1FEN', 'TIMER1.DTFC.DTPRS1FEN', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFC_DTDBGFEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFC_DTDBGFEN, self).__init__(register,
            'DTDBGFEN', 'TIMER1.DTFC.DTDBGFEN', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFC_DTLOCKUPFEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFC_DTLOCKUPFEN, self).__init__(register,
            'DTLOCKUPFEN', 'TIMER1.DTFC.DTLOCKUPFEN', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTOGEN_DTOGCC0EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTOGEN_DTOGCC0EN, self).__init__(register,
            'DTOGCC0EN', 'TIMER1.DTOGEN.DTOGCC0EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTOGEN_DTOGCC1EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTOGEN_DTOGCC1EN, self).__init__(register,
            'DTOGCC1EN', 'TIMER1.DTOGEN.DTOGCC1EN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTOGEN_DTOGCC2EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTOGEN_DTOGCC2EN, self).__init__(register,
            'DTOGCC2EN', 'TIMER1.DTOGEN.DTOGCC2EN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTOGEN_DTOGCDTI0EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTOGEN_DTOGCDTI0EN, self).__init__(register,
            'DTOGCDTI0EN', 'TIMER1.DTOGEN.DTOGCDTI0EN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTOGEN_DTOGCDTI1EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTOGEN_DTOGCDTI1EN, self).__init__(register,
            'DTOGCDTI1EN', 'TIMER1.DTOGEN.DTOGCDTI1EN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTOGEN_DTOGCDTI2EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTOGEN_DTOGCDTI2EN, self).__init__(register,
            'DTOGCDTI2EN', 'TIMER1.DTOGEN.DTOGCDTI2EN', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFAULT_DTPRS0F(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFAULT_DTPRS0F, self).__init__(register,
            'DTPRS0F', 'TIMER1.DTFAULT.DTPRS0F', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFAULT_DTPRS1F(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFAULT_DTPRS1F, self).__init__(register,
            'DTPRS1F', 'TIMER1.DTFAULT.DTPRS1F', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFAULT_DTDBGF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFAULT_DTDBGF, self).__init__(register,
            'DTDBGF', 'TIMER1.DTFAULT.DTDBGF', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFAULT_DTLOCKUPF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFAULT_DTLOCKUPF, self).__init__(register,
            'DTLOCKUPF', 'TIMER1.DTFAULT.DTLOCKUPF', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFAULTC_DTPRS0FC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFAULTC_DTPRS0FC, self).__init__(register,
            'DTPRS0FC', 'TIMER1.DTFAULTC.DTPRS0FC', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFAULTC_DTPRS1FC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFAULTC_DTPRS1FC, self).__init__(register,
            'DTPRS1FC', 'TIMER1.DTFAULTC.DTPRS1FC', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFAULTC_DTDBGFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFAULTC_DTDBGFC, self).__init__(register,
            'DTDBGFC', 'TIMER1.DTFAULTC.DTDBGFC', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTFAULTC_TLOCKUPFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTFAULTC_TLOCKUPFC, self).__init__(register,
            'TLOCKUPFC', 'TIMER1.DTFAULTC.TLOCKUPFC', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TIMER1_DTLOCK_LOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TIMER1_DTLOCK_LOCKKEY, self).__init__(register,
            'LOCKKEY', 'TIMER1.DTLOCK.LOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_TIMER1_DTLOCK_LOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


