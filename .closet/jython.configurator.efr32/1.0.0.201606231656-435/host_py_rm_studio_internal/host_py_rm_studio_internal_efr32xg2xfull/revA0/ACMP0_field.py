
from static import Base_RM_Field
from ACMP0_enum import *


class RM_Field_ACMP0_CTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_EN, self).__init__(register,
            'EN', 'ACMP0.CTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_INACTVAL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_INACTVAL, self).__init__(register,
            'INACTVAL', 'ACMP0.CTRL.INACTVAL', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_GPIOINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_GPIOINV, self).__init__(register,
            'GPIOINV', 'ACMP0.CTRL.GPIOINV', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_REFRESHRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_REFRESHRATE, self).__init__(register,
            'REFRESHRATE', 'ACMP0.CTRL.REFRESHRATE', 'read-write',
            "",
            4, 2,
            RM_Enum_ACMP0_CTRL_REFRESHRATE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_APORTXMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_APORTXMASTERDIS, self).__init__(register,
            'APORTXMASTERDIS', 'ACMP0.CTRL.APORTXMASTERDIS', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_APORTYMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_APORTYMASTERDIS, self).__init__(register,
            'APORTYMASTERDIS', 'ACMP0.CTRL.APORTYMASTERDIS', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_APORTVMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_APORTVMASTERDIS, self).__init__(register,
            'APORTVMASTERDIS', 'ACMP0.CTRL.APORTVMASTERDIS', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_PWRSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_PWRSEL, self).__init__(register,
            'PWRSEL', 'ACMP0.CTRL.PWRSEL', 'read-write',
            "",
            12, 3,
            RM_Enum_ACMP0_CTRL_PWRSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_ACCURACY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_ACCURACY, self).__init__(register,
            'ACCURACY', 'ACMP0.CTRL.ACCURACY', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_INPUTRANGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_INPUTRANGE, self).__init__(register,
            'INPUTRANGE', 'ACMP0.CTRL.INPUTRANGE', 'read-write',
            "",
            18, 2,
            RM_Enum_ACMP0_CTRL_INPUTRANGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_IRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_IRISE, self).__init__(register,
            'IRISE', 'ACMP0.CTRL.IRISE', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_IFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_IFALL, self).__init__(register,
            'IFALL', 'ACMP0.CTRL.IFALL', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_BIASPROG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_BIASPROG, self).__init__(register,
            'BIASPROG', 'ACMP0.CTRL.BIASPROG', 'read-write',
            "",
            24, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_FULLBIAS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_FULLBIAS, self).__init__(register,
            'FULLBIAS', 'ACMP0.CTRL.FULLBIAS', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_INPUTSEL_POSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_INPUTSEL_POSSEL, self).__init__(register,
            'POSSEL', 'ACMP0.INPUTSEL.POSSEL', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_INPUTSEL_NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_INPUTSEL_NEGSEL, self).__init__(register,
            'NEGSEL', 'ACMP0.INPUTSEL.NEGSEL', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_INPUTSEL_VASEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_INPUTSEL_VASEL, self).__init__(register,
            'VASEL', 'ACMP0.INPUTSEL.VASEL', 'read-write',
            "",
            16, 6,
            RM_Enum_ACMP0_INPUTSEL_VASEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_INPUTSEL_VBSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_INPUTSEL_VBSEL, self).__init__(register,
            'VBSEL', 'ACMP0.INPUTSEL.VBSEL', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_INPUTSEL_VLPSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_INPUTSEL_VLPSEL, self).__init__(register,
            'VLPSEL', 'ACMP0.INPUTSEL.VLPSEL', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_INPUTSEL_CSRESEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_INPUTSEL_CSRESEN, self).__init__(register,
            'CSRESEN', 'ACMP0.INPUTSEL.CSRESEN', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_INPUTSEL_CSRESSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_INPUTSEL_CSRESSEL, self).__init__(register,
            'CSRESSEL', 'ACMP0.INPUTSEL.CSRESSEL', 'read-write',
            "",
            28, 3,
            RM_Enum_ACMP0_INPUTSEL_CSRESSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_STATUS_ACMPACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_STATUS_ACMPACT, self).__init__(register,
            'ACMPACT', 'ACMP0.STATUS.ACMPACT', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_STATUS_ACMPOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_STATUS_ACMPOUT, self).__init__(register,
            'ACMPOUT', 'ACMP0.STATUS.ACMPOUT', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_STATUS_APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_STATUS_APORTCONFLICT, self).__init__(register,
            'APORTCONFLICT', 'ACMP0.STATUS.APORTCONFLICT', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_STATUS_EXTIFACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_STATUS_EXTIFACT, self).__init__(register,
            'EXTIFACT', 'ACMP0.STATUS.EXTIFACT', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_IF_EDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IF_EDGE, self).__init__(register,
            'EDGE', 'ACMP0.IF.EDGE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_IF_WARMUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IF_WARMUP, self).__init__(register,
            'WARMUP', 'ACMP0.IF.WARMUP', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_IF_APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IF_APORTCONFLICT, self).__init__(register,
            'APORTCONFLICT', 'ACMP0.IF.APORTCONFLICT', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_IFS_EDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IFS_EDGE, self).__init__(register,
            'EDGE', 'ACMP0.IFS.EDGE', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_IFS_WARMUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IFS_WARMUP, self).__init__(register,
            'WARMUP', 'ACMP0.IFS.WARMUP', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_IFS_APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IFS_APORTCONFLICT, self).__init__(register,
            'APORTCONFLICT', 'ACMP0.IFS.APORTCONFLICT', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_IFC_EDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IFC_EDGE, self).__init__(register,
            'EDGE', 'ACMP0.IFC.EDGE', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_IFC_WARMUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IFC_WARMUP, self).__init__(register,
            'WARMUP', 'ACMP0.IFC.WARMUP', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_IFC_APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IFC_APORTCONFLICT, self).__init__(register,
            'APORTCONFLICT', 'ACMP0.IFC.APORTCONFLICT', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_IEN_EDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IEN_EDGE, self).__init__(register,
            'EDGE', 'ACMP0.IEN.EDGE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_IEN_WARMUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IEN_WARMUP, self).__init__(register,
            'WARMUP', 'ACMP0.IEN.WARMUP', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_IEN_APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IEN_APORTCONFLICT, self).__init__(register,
            'APORTCONFLICT', 'ACMP0.IEN.APORTCONFLICT', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTREQ_APORT0XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTREQ_APORT0XREQ, self).__init__(register,
            'APORT0XREQ', 'ACMP0.APORTREQ.APORT0XREQ', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTREQ_APORT0YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTREQ_APORT0YREQ, self).__init__(register,
            'APORT0YREQ', 'ACMP0.APORTREQ.APORT0YREQ', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTREQ_APORT1XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTREQ_APORT1XREQ, self).__init__(register,
            'APORT1XREQ', 'ACMP0.APORTREQ.APORT1XREQ', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTREQ_APORT1YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTREQ_APORT1YREQ, self).__init__(register,
            'APORT1YREQ', 'ACMP0.APORTREQ.APORT1YREQ', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTREQ_APORT2XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTREQ_APORT2XREQ, self).__init__(register,
            'APORT2XREQ', 'ACMP0.APORTREQ.APORT2XREQ', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTREQ_APORT2YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTREQ_APORT2YREQ, self).__init__(register,
            'APORT2YREQ', 'ACMP0.APORTREQ.APORT2YREQ', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTREQ_APORT3XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTREQ_APORT3XREQ, self).__init__(register,
            'APORT3XREQ', 'ACMP0.APORTREQ.APORT3XREQ', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTREQ_APORT3YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTREQ_APORT3YREQ, self).__init__(register,
            'APORT3YREQ', 'ACMP0.APORTREQ.APORT3YREQ', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTREQ_APORT4XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTREQ_APORT4XREQ, self).__init__(register,
            'APORT4XREQ', 'ACMP0.APORTREQ.APORT4XREQ', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTREQ_APORT4YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTREQ_APORT4YREQ, self).__init__(register,
            'APORT4YREQ', 'ACMP0.APORTREQ.APORT4YREQ', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTCONFLICT_APORT0XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTCONFLICT_APORT0XCONFLICT, self).__init__(register,
            'APORT0XCONFLICT', 'ACMP0.APORTCONFLICT.APORT0XCONFLICT', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTCONFLICT_APORT0YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTCONFLICT_APORT0YCONFLICT, self).__init__(register,
            'APORT0YCONFLICT', 'ACMP0.APORTCONFLICT.APORT0YCONFLICT', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTCONFLICT_APORT1XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTCONFLICT_APORT1XCONFLICT, self).__init__(register,
            'APORT1XCONFLICT', 'ACMP0.APORTCONFLICT.APORT1XCONFLICT', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTCONFLICT_APORT1YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTCONFLICT_APORT1YCONFLICT, self).__init__(register,
            'APORT1YCONFLICT', 'ACMP0.APORTCONFLICT.APORT1YCONFLICT', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTCONFLICT_APORT2XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTCONFLICT_APORT2XCONFLICT, self).__init__(register,
            'APORT2XCONFLICT', 'ACMP0.APORTCONFLICT.APORT2XCONFLICT', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTCONFLICT_APORT2YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTCONFLICT_APORT2YCONFLICT, self).__init__(register,
            'APORT2YCONFLICT', 'ACMP0.APORTCONFLICT.APORT2YCONFLICT', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTCONFLICT_APORT3XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTCONFLICT_APORT3XCONFLICT, self).__init__(register,
            'APORT3XCONFLICT', 'ACMP0.APORTCONFLICT.APORT3XCONFLICT', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTCONFLICT_APORT3YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTCONFLICT_APORT3YCONFLICT, self).__init__(register,
            'APORT3YCONFLICT', 'ACMP0.APORTCONFLICT.APORT3YCONFLICT', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTCONFLICT_APORT4XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTCONFLICT_APORT4XCONFLICT, self).__init__(register,
            'APORT4XCONFLICT', 'ACMP0.APORTCONFLICT.APORT4XCONFLICT', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_APORTCONFLICT_APORT4YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_APORTCONFLICT_APORT4YCONFLICT, self).__init__(register,
            'APORT4YCONFLICT', 'ACMP0.APORTCONFLICT.APORT4YCONFLICT', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_HYSTERESIS0_HYST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_HYSTERESIS0_HYST, self).__init__(register,
            'HYST', 'ACMP0.HYSTERESIS0.HYST', 'read-write',
            "",
            0, 4,
            RM_Enum_ACMP0_HYSTERESIS0_HYST(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_HYSTERESIS0_DIVVA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_HYSTERESIS0_DIVVA, self).__init__(register,
            'DIVVA', 'ACMP0.HYSTERESIS0.DIVVA', 'read-write',
            "",
            16, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_HYSTERESIS0_DIVVB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_HYSTERESIS0_DIVVB, self).__init__(register,
            'DIVVB', 'ACMP0.HYSTERESIS0.DIVVB', 'read-write',
            "",
            24, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_HYSTERESIS1_HYST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_HYSTERESIS1_HYST, self).__init__(register,
            'HYST', 'ACMP0.HYSTERESIS1.HYST', 'read-write',
            "",
            0, 4,
            RM_Enum_ACMP0_HYSTERESIS1_HYST(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_HYSTERESIS1_DIVVA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_HYSTERESIS1_DIVVA, self).__init__(register,
            'DIVVA', 'ACMP0.HYSTERESIS1.DIVVA', 'read-write',
            "",
            16, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_HYSTERESIS1_DIVVB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_HYSTERESIS1_DIVVB, self).__init__(register,
            'DIVVB', 'ACMP0.HYSTERESIS1.DIVVB', 'read-write',
            "",
            24, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_TEST_VDDCP4MUXDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_TEST_VDDCP4MUXDIS, self).__init__(register,
            'VDDCP4MUXDIS', 'ACMP0.TEST.VDDCP4MUXDIS', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_TEST_VDDCP4VBGDIVDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_TEST_VDDCP4VBGDIVDIS, self).__init__(register,
            'VDDCP4VBGDIVDIS', 'ACMP0.TEST.VDDCP4VBGDIVDIS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_ROUTEPEN_OUTPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_ROUTEPEN_OUTPEN, self).__init__(register,
            'OUTPEN', 'ACMP0.ROUTEPEN.OUTPEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_ROUTELOC0_OUTLOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_ROUTELOC0_OUTLOC, self).__init__(register,
            'OUTLOC', 'ACMP0.ROUTELOC0.OUTLOC', 'read-write',
            "",
            0, 6,
            RM_Enum_ACMP0_ROUTELOC0_OUTLOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_EXTIFCTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_EXTIFCTRL_EN, self).__init__(register,
            'EN', 'ACMP0.EXTIFCTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_EXTIFCTRL_APORTSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_EXTIFCTRL_APORTSEL, self).__init__(register,
            'APORTSEL', 'ACMP0.EXTIFCTRL.APORTSEL', 'read-write',
            "",
            4, 4,
            RM_Enum_ACMP0_EXTIFCTRL_APORTSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


