
from static import Base_RM_Register
from IDAC0_field import *


class RM_Register_IDAC0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_CTRL, self).__init__(rmio, label,
            0x40006000, 0x000,
            'CTRL', 'IDAC0.CTRL', 'read-write',
            "",
            0x00000000, 0x00F17FFF)

        self.EN = RM_Field_IDAC0_CTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.CURSINK = RM_Field_IDAC0_CTRL_CURSINK(self)
        self.zz_fdict['CURSINK'] = self.CURSINK
        self.MINOUTTRANS = RM_Field_IDAC0_CTRL_MINOUTTRANS(self)
        self.zz_fdict['MINOUTTRANS'] = self.MINOUTTRANS
        self.OUTEN = RM_Field_IDAC0_CTRL_OUTEN(self)
        self.zz_fdict['OUTEN'] = self.OUTEN
        self.OUTMODE = RM_Field_IDAC0_CTRL_OUTMODE(self)
        self.zz_fdict['OUTMODE'] = self.OUTMODE
        self.PWRSEL = RM_Field_IDAC0_CTRL_PWRSEL(self)
        self.zz_fdict['PWRSEL'] = self.PWRSEL
        self.EM2DELAY = RM_Field_IDAC0_CTRL_EM2DELAY(self)
        self.zz_fdict['EM2DELAY'] = self.EM2DELAY
        self.BUSMASTERDIS = RM_Field_IDAC0_CTRL_BUSMASTERDIS(self)
        self.zz_fdict['BUSMASTERDIS'] = self.BUSMASTERDIS
        self.OUTENPRS = RM_Field_IDAC0_CTRL_OUTENPRS(self)
        self.zz_fdict['OUTENPRS'] = self.OUTENPRS
        self.PRSSEL = RM_Field_IDAC0_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_IDAC0_CURPROG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_CURPROG, self).__init__(rmio, label,
            0x40006000, 0x004,
            'CURPROG', 'IDAC0.CURPROG', 'read-write',
            "",
            0x009B0000, 0x00FF1F03)

        self.RANGESEL = RM_Field_IDAC0_CURPROG_RANGESEL(self)
        self.zz_fdict['RANGESEL'] = self.RANGESEL
        self.STEPSEL = RM_Field_IDAC0_CURPROG_STEPSEL(self)
        self.zz_fdict['STEPSEL'] = self.STEPSEL
        self.TUNING = RM_Field_IDAC0_CURPROG_TUNING(self)
        self.zz_fdict['TUNING'] = self.TUNING
        self.__dict__['zz_frozen'] = True


class RM_Register_IDAC0_DUTYCONFIG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_DUTYCONFIG, self).__init__(rmio, label,
            0x40006000, 0x00C,
            'DUTYCONFIG', 'IDAC0.DUTYCONFIG', 'read-write',
            "",
            0x00000000, 0x00000002)

        self.EM2DUTYCYCLEDIS = RM_Field_IDAC0_DUTYCONFIG_EM2DUTYCYCLEDIS(self)
        self.zz_fdict['EM2DUTYCYCLEDIS'] = self.EM2DUTYCYCLEDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_IDAC0_DUTYFREQSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_DUTYFREQSEL, self).__init__(rmio, label,
            0x40006000, 0x010,
            'DUTYFREQSEL', 'IDAC0.DUTYFREQSEL', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.REFRESHRATE = RM_Field_IDAC0_DUTYFREQSEL_REFRESHRATE(self)
        self.zz_fdict['REFRESHRATE'] = self.REFRESHRATE
        self.__dict__['zz_frozen'] = True


class RM_Register_IDAC0_TESTCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_TESTCTRL, self).__init__(rmio, label,
            0x40006000, 0x014,
            'TESTCTRL', 'IDAC0.TESTCTRL', 'read-write',
            "",
            0x00000000, 0x0000001F)

        self.CASCODEDIS = RM_Field_IDAC0_TESTCTRL_CASCODEDIS(self)
        self.zz_fdict['CASCODEDIS'] = self.CASCODEDIS
        self.OPAMPDIS = RM_Field_IDAC0_TESTCTRL_OPAMPDIS(self)
        self.zz_fdict['OPAMPDIS'] = self.OPAMPDIS
        self.PMOSCASCTUNE = RM_Field_IDAC0_TESTCTRL_PMOSCASCTUNE(self)
        self.zz_fdict['PMOSCASCTUNE'] = self.PMOSCASCTUNE
        self.__dict__['zz_frozen'] = True


class RM_Register_IDAC0_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_STATUS, self).__init__(rmio, label,
            0x40006000, 0x018,
            'STATUS', 'IDAC0.STATUS', 'read-only',
            "",
            0x00000000, 0x00000003)

        self.CURSTABLE = RM_Field_IDAC0_STATUS_CURSTABLE(self)
        self.zz_fdict['CURSTABLE'] = self.CURSTABLE
        self.BUSCONFLICT = RM_Field_IDAC0_STATUS_BUSCONFLICT(self)
        self.zz_fdict['BUSCONFLICT'] = self.BUSCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_IDAC0_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_IF, self).__init__(rmio, label,
            0x40006000, 0x020,
            'IF', 'IDAC0.IF', 'read-only',
            "",
            0x00000000, 0x00000003)

        self.CURSTABLE = RM_Field_IDAC0_IF_CURSTABLE(self)
        self.zz_fdict['CURSTABLE'] = self.CURSTABLE
        self.BUSCONFLICT = RM_Field_IDAC0_IF_BUSCONFLICT(self)
        self.zz_fdict['BUSCONFLICT'] = self.BUSCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_IDAC0_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_IFS, self).__init__(rmio, label,
            0x40006000, 0x024,
            'IFS', 'IDAC0.IFS', 'write-only',
            "",
            0x00000000, 0x00000003)

        self.CURSTABLE = RM_Field_IDAC0_IFS_CURSTABLE(self)
        self.zz_fdict['CURSTABLE'] = self.CURSTABLE
        self.BUSCONFLICT = RM_Field_IDAC0_IFS_BUSCONFLICT(self)
        self.zz_fdict['BUSCONFLICT'] = self.BUSCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_IDAC0_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_IFC, self).__init__(rmio, label,
            0x40006000, 0x028,
            'IFC', 'IDAC0.IFC', 'write-only',
            "",
            0x00000000, 0x00000003)

        self.CURSTABLE = RM_Field_IDAC0_IFC_CURSTABLE(self)
        self.zz_fdict['CURSTABLE'] = self.CURSTABLE
        self.BUSCONFLICT = RM_Field_IDAC0_IFC_BUSCONFLICT(self)
        self.zz_fdict['BUSCONFLICT'] = self.BUSCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_IDAC0_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_IEN, self).__init__(rmio, label,
            0x40006000, 0x02C,
            'IEN', 'IDAC0.IEN', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.CURSTABLE = RM_Field_IDAC0_IEN_CURSTABLE(self)
        self.zz_fdict['CURSTABLE'] = self.CURSTABLE
        self.BUSCONFLICT = RM_Field_IDAC0_IEN_BUSCONFLICT(self)
        self.zz_fdict['BUSCONFLICT'] = self.BUSCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_IDAC0_BUSREQ(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_BUSREQ, self).__init__(rmio, label,
            0x40006000, 0x034,
            'BUSREQ', 'IDAC0.BUSREQ', 'read-only',
            "",
            0x00000000, 0x0000000C)

        self.BUS1XREQ = RM_Field_IDAC0_BUSREQ_BUS1XREQ(self)
        self.zz_fdict['BUS1XREQ'] = self.BUS1XREQ
        self.BUS1YREQ = RM_Field_IDAC0_BUSREQ_BUS1YREQ(self)
        self.zz_fdict['BUS1YREQ'] = self.BUS1YREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_IDAC0_BUSCONFLICT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_BUSCONFLICT, self).__init__(rmio, label,
            0x40006000, 0x038,
            'BUSCONFLICT', 'IDAC0.BUSCONFLICT', 'read-only',
            "",
            0x00000000, 0x0000000C)

        self.BUS1XCONFLICT = RM_Field_IDAC0_BUSCONFLICT_BUS1XCONFLICT(self)
        self.zz_fdict['BUS1XCONFLICT'] = self.BUS1XCONFLICT
        self.BUS1YCONFLICT = RM_Field_IDAC0_BUSCONFLICT_BUS1YCONFLICT(self)
        self.zz_fdict['BUS1YCONFLICT'] = self.BUS1YCONFLICT
        self.__dict__['zz_frozen'] = True


