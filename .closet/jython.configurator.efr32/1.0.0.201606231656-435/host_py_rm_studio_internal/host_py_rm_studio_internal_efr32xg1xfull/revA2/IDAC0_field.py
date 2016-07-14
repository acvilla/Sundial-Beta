
from static import Base_RM_Field
from IDAC0_enum import *


class RM_Field_IDAC0_CTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_CTRL_EN, self).__init__(register,
            'EN', 'IDAC0.CTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_CTRL_CURSINK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_CTRL_CURSINK, self).__init__(register,
            'CURSINK', 'IDAC0.CTRL.CURSINK', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_CTRL_MINOUTTRANS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_CTRL_MINOUTTRANS, self).__init__(register,
            'MINOUTTRANS', 'IDAC0.CTRL.MINOUTTRANS', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_CTRL_OUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_CTRL_OUTEN, self).__init__(register,
            'OUTEN', 'IDAC0.CTRL.OUTEN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_CTRL_OUTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_CTRL_OUTMODE, self).__init__(register,
            'OUTMODE', 'IDAC0.CTRL.OUTMODE', 'read-write',
            "",
            4, 8,
            RM_Enum_IDAC0_CTRL_OUTMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_CTRL_PWRSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_CTRL_PWRSEL, self).__init__(register,
            'PWRSEL', 'IDAC0.CTRL.PWRSEL', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_CTRL_EM2DELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_CTRL_EM2DELAY, self).__init__(register,
            'EM2DELAY', 'IDAC0.CTRL.EM2DELAY', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_CTRL_BUSMASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_CTRL_BUSMASTERDIS, self).__init__(register,
            'BUSMASTERDIS', 'IDAC0.CTRL.BUSMASTERDIS', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_CTRL_OUTENPRS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_CTRL_OUTENPRS, self).__init__(register,
            'OUTENPRS', 'IDAC0.CTRL.OUTENPRS', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'IDAC0.CTRL.PRSSEL', 'read-write',
            "",
            20, 4,
            RM_Enum_IDAC0_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_CURPROG_RANGESEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_CURPROG_RANGESEL, self).__init__(register,
            'RANGESEL', 'IDAC0.CURPROG.RANGESEL', 'read-write',
            "",
            0, 2,
            RM_Enum_IDAC0_CURPROG_RANGESEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_CURPROG_STEPSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_CURPROG_STEPSEL, self).__init__(register,
            'STEPSEL', 'IDAC0.CURPROG.STEPSEL', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_CURPROG_TUNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_CURPROG_TUNING, self).__init__(register,
            'TUNING', 'IDAC0.CURPROG.TUNING', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_DUTYCONFIG_EM2DUTYCYCLEDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_DUTYCONFIG_EM2DUTYCYCLEDIS, self).__init__(register,
            'EM2DUTYCYCLEDIS', 'IDAC0.DUTYCONFIG.EM2DUTYCYCLEDIS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_DUTYFREQSEL_REFRESHRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_DUTYFREQSEL_REFRESHRATE, self).__init__(register,
            'REFRESHRATE', 'IDAC0.DUTYFREQSEL.REFRESHRATE', 'read-write',
            "",
            0, 2,
            RM_Enum_IDAC0_DUTYFREQSEL_REFRESHRATE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_TESTCTRL_CASCODEDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_TESTCTRL_CASCODEDIS, self).__init__(register,
            'CASCODEDIS', 'IDAC0.TESTCTRL.CASCODEDIS', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_TESTCTRL_OPAMPDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_TESTCTRL_OPAMPDIS, self).__init__(register,
            'OPAMPDIS', 'IDAC0.TESTCTRL.OPAMPDIS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_TESTCTRL_PMOSCASCTUNE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_TESTCTRL_PMOSCASCTUNE, self).__init__(register,
            'PMOSCASCTUNE', 'IDAC0.TESTCTRL.PMOSCASCTUNE', 'read-write',
            "",
            2, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_STATUS_CURSTABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_STATUS_CURSTABLE, self).__init__(register,
            'CURSTABLE', 'IDAC0.STATUS.CURSTABLE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_STATUS_BUSCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_STATUS_BUSCONFLICT, self).__init__(register,
            'BUSCONFLICT', 'IDAC0.STATUS.BUSCONFLICT', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_IF_CURSTABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_IF_CURSTABLE, self).__init__(register,
            'CURSTABLE', 'IDAC0.IF.CURSTABLE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_IF_BUSCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_IF_BUSCONFLICT, self).__init__(register,
            'BUSCONFLICT', 'IDAC0.IF.BUSCONFLICT', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_IFS_CURSTABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_IFS_CURSTABLE, self).__init__(register,
            'CURSTABLE', 'IDAC0.IFS.CURSTABLE', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_IFS_BUSCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_IFS_BUSCONFLICT, self).__init__(register,
            'BUSCONFLICT', 'IDAC0.IFS.BUSCONFLICT', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_IFC_CURSTABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_IFC_CURSTABLE, self).__init__(register,
            'CURSTABLE', 'IDAC0.IFC.CURSTABLE', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_IFC_BUSCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_IFC_BUSCONFLICT, self).__init__(register,
            'BUSCONFLICT', 'IDAC0.IFC.BUSCONFLICT', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_IEN_CURSTABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_IEN_CURSTABLE, self).__init__(register,
            'CURSTABLE', 'IDAC0.IEN.CURSTABLE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_IEN_BUSCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_IEN_BUSCONFLICT, self).__init__(register,
            'BUSCONFLICT', 'IDAC0.IEN.BUSCONFLICT', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_BUSREQ_BUS1XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_BUSREQ_BUS1XREQ, self).__init__(register,
            'BUS1XREQ', 'IDAC0.BUSREQ.BUS1XREQ', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_BUSREQ_BUS1YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_BUSREQ_BUS1YREQ, self).__init__(register,
            'BUS1YREQ', 'IDAC0.BUSREQ.BUS1YREQ', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_BUSCONFLICT_BUS1XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_BUSCONFLICT_BUS1XCONFLICT, self).__init__(register,
            'BUS1XCONFLICT', 'IDAC0.BUSCONFLICT.BUS1XCONFLICT', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_IDAC0_BUSCONFLICT_BUS1YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_IDAC0_BUSCONFLICT_BUS1YCONFLICT, self).__init__(register,
            'BUS1YCONFLICT', 'IDAC0.BUSCONFLICT.BUS1YCONFLICT', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


