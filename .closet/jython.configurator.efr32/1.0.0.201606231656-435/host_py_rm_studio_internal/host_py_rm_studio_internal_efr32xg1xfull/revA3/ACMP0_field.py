
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


class RM_Field_ACMP0_CTRL_DUTYFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_DUTYFSEL, self).__init__(register,
            'DUTYFSEL', 'ACMP0.CTRL.DUTYFSEL', 'read-write',
            "",
            4, 2,
            RM_Enum_ACMP0_CTRL_DUTYFSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_BUSXMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_BUSXMASTERDIS, self).__init__(register,
            'BUSXMASTERDIS', 'ACMP0.CTRL.BUSXMASTERDIS', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_BUSYMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_BUSYMASTERDIS, self).__init__(register,
            'BUSYMASTERDIS', 'ACMP0.CTRL.BUSYMASTERDIS', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_CTRL_BUSVMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_CTRL_BUSVMASTERDIS, self).__init__(register,
            'BUSVMASTERDIS', 'ACMP0.CTRL.BUSVMASTERDIS', 'read-write',
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
            0, 8,
            RM_Enum_ACMP0_INPUTSEL_POSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_INPUTSEL_NEGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_INPUTSEL_NEGSEL, self).__init__(register,
            'NEGSEL', 'ACMP0.INPUTSEL.NEGSEL', 'read-write',
            "",
            8, 8,
            RM_Enum_ACMP0_INPUTSEL_NEGSEL(register.zz_label))
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


class RM_Field_ACMP0_STATUS_BUSCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_STATUS_BUSCONFLICT, self).__init__(register,
            'BUSCONFLICT', 'ACMP0.STATUS.BUSCONFLICT', 'read-only',
            "",
            2, 1)
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


class RM_Field_ACMP0_IF_BUSCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IF_BUSCONFLICT, self).__init__(register,
            'BUSCONFLICT', 'ACMP0.IF.BUSCONFLICT', 'read-only',
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


class RM_Field_ACMP0_IFS_BUSCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IFS_BUSCONFLICT, self).__init__(register,
            'BUSCONFLICT', 'ACMP0.IFS.BUSCONFLICT', 'write-only',
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


class RM_Field_ACMP0_IFC_BUSCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IFC_BUSCONFLICT, self).__init__(register,
            'BUSCONFLICT', 'ACMP0.IFC.BUSCONFLICT', 'write-only',
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


class RM_Field_ACMP0_IEN_BUSCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_IEN_BUSCONFLICT, self).__init__(register,
            'BUSCONFLICT', 'ACMP0.IEN.BUSCONFLICT', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSREQ_BUS0XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSREQ_BUS0XREQ, self).__init__(register,
            'BUS0XREQ', 'ACMP0.BUSREQ.BUS0XREQ', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSREQ_BUS0YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSREQ_BUS0YREQ, self).__init__(register,
            'BUS0YREQ', 'ACMP0.BUSREQ.BUS0YREQ', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSREQ_BUS1XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSREQ_BUS1XREQ, self).__init__(register,
            'BUS1XREQ', 'ACMP0.BUSREQ.BUS1XREQ', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSREQ_BUS1YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSREQ_BUS1YREQ, self).__init__(register,
            'BUS1YREQ', 'ACMP0.BUSREQ.BUS1YREQ', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSREQ_BUS2XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSREQ_BUS2XREQ, self).__init__(register,
            'BUS2XREQ', 'ACMP0.BUSREQ.BUS2XREQ', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSREQ_BUS2YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSREQ_BUS2YREQ, self).__init__(register,
            'BUS2YREQ', 'ACMP0.BUSREQ.BUS2YREQ', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSREQ_BUS3XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSREQ_BUS3XREQ, self).__init__(register,
            'BUS3XREQ', 'ACMP0.BUSREQ.BUS3XREQ', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSREQ_BUS3YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSREQ_BUS3YREQ, self).__init__(register,
            'BUS3YREQ', 'ACMP0.BUSREQ.BUS3YREQ', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSREQ_BUS4XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSREQ_BUS4XREQ, self).__init__(register,
            'BUS4XREQ', 'ACMP0.BUSREQ.BUS4XREQ', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSREQ_BUS4YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSREQ_BUS4YREQ, self).__init__(register,
            'BUS4YREQ', 'ACMP0.BUSREQ.BUS4YREQ', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSCONFLICT_BUS0XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSCONFLICT_BUS0XCONFLICT, self).__init__(register,
            'BUS0XCONFLICT', 'ACMP0.BUSCONFLICT.BUS0XCONFLICT', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSCONFLICT_BUS0YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSCONFLICT_BUS0YCONFLICT, self).__init__(register,
            'BUS0YCONFLICT', 'ACMP0.BUSCONFLICT.BUS0YCONFLICT', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSCONFLICT_BUS1XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSCONFLICT_BUS1XCONFLICT, self).__init__(register,
            'BUS1XCONFLICT', 'ACMP0.BUSCONFLICT.BUS1XCONFLICT', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSCONFLICT_BUS1YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSCONFLICT_BUS1YCONFLICT, self).__init__(register,
            'BUS1YCONFLICT', 'ACMP0.BUSCONFLICT.BUS1YCONFLICT', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSCONFLICT_BUS2XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSCONFLICT_BUS2XCONFLICT, self).__init__(register,
            'BUS2XCONFLICT', 'ACMP0.BUSCONFLICT.BUS2XCONFLICT', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSCONFLICT_BUS2YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSCONFLICT_BUS2YCONFLICT, self).__init__(register,
            'BUS2YCONFLICT', 'ACMP0.BUSCONFLICT.BUS2YCONFLICT', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSCONFLICT_BUS3XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSCONFLICT_BUS3XCONFLICT, self).__init__(register,
            'BUS3XCONFLICT', 'ACMP0.BUSCONFLICT.BUS3XCONFLICT', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSCONFLICT_BUS3YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSCONFLICT_BUS3YCONFLICT, self).__init__(register,
            'BUS3YCONFLICT', 'ACMP0.BUSCONFLICT.BUS3YCONFLICT', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSCONFLICT_BUS4XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSCONFLICT_BUS4XCONFLICT, self).__init__(register,
            'BUS4XCONFLICT', 'ACMP0.BUSCONFLICT.BUS4XCONFLICT', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ACMP0_BUSCONFLICT_BUS4YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ACMP0_BUSCONFLICT_BUS4YCONFLICT, self).__init__(register,
            'BUS4YCONFLICT', 'ACMP0.BUSCONFLICT.BUS4YCONFLICT', 'read-only',
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


