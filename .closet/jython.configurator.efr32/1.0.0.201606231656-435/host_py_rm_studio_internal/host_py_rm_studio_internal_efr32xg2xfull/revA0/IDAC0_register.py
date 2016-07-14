
from static import Base_RM_Register
from IDAC0_field import *


class RM_Register_IDAC0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_CTRL, self).__init__(rmio, label,
            0x40006000, 0x000,
            'CTRL', 'IDAC0.CTRL', 'read-write',
            "",
            0x00000000, 0x00FD7FFF)

        self.EN = RM_Field_IDAC0_CTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.CURSINK = RM_Field_IDAC0_CTRL_CURSINK(self)
        self.zz_fdict['CURSINK'] = self.CURSINK
        self.MINOUTTRANS = RM_Field_IDAC0_CTRL_MINOUTTRANS(self)
        self.zz_fdict['MINOUTTRANS'] = self.MINOUTTRANS
        self.APORTOUTEN = RM_Field_IDAC0_CTRL_APORTOUTEN(self)
        self.zz_fdict['APORTOUTEN'] = self.APORTOUTEN
        self.APORTOUTSEL = RM_Field_IDAC0_CTRL_APORTOUTSEL(self)
        self.zz_fdict['APORTOUTSEL'] = self.APORTOUTSEL
        self.PWRSEL = RM_Field_IDAC0_CTRL_PWRSEL(self)
        self.zz_fdict['PWRSEL'] = self.PWRSEL
        self.EM2DELAY = RM_Field_IDAC0_CTRL_EM2DELAY(self)
        self.zz_fdict['EM2DELAY'] = self.EM2DELAY
        self.APORTMASTERDIS = RM_Field_IDAC0_CTRL_APORTMASTERDIS(self)
        self.zz_fdict['APORTMASTERDIS'] = self.APORTMASTERDIS
        self.APORTOUTENPRS = RM_Field_IDAC0_CTRL_APORTOUTENPRS(self)
        self.zz_fdict['APORTOUTENPRS'] = self.APORTOUTENPRS
        self.MAINOUTEN = RM_Field_IDAC0_CTRL_MAINOUTEN(self)
        self.zz_fdict['MAINOUTEN'] = self.MAINOUTEN
        self.MAINOUTENPRS = RM_Field_IDAC0_CTRL_MAINOUTENPRS(self)
        self.zz_fdict['MAINOUTENPRS'] = self.MAINOUTENPRS
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
        self.APORTCONFLICT = RM_Field_IDAC0_STATUS_APORTCONFLICT(self)
        self.zz_fdict['APORTCONFLICT'] = self.APORTCONFLICT
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
        self.APORTCONFLICT = RM_Field_IDAC0_IF_APORTCONFLICT(self)
        self.zz_fdict['APORTCONFLICT'] = self.APORTCONFLICT
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
        self.APORTCONFLICT = RM_Field_IDAC0_IFS_APORTCONFLICT(self)
        self.zz_fdict['APORTCONFLICT'] = self.APORTCONFLICT
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
        self.APORTCONFLICT = RM_Field_IDAC0_IFC_APORTCONFLICT(self)
        self.zz_fdict['APORTCONFLICT'] = self.APORTCONFLICT
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
        self.APORTCONFLICT = RM_Field_IDAC0_IEN_APORTCONFLICT(self)
        self.zz_fdict['APORTCONFLICT'] = self.APORTCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_IDAC0_APORTREQ(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_APORTREQ, self).__init__(rmio, label,
            0x40006000, 0x034,
            'APORTREQ', 'IDAC0.APORTREQ', 'read-only',
            "",
            0x00000000, 0x0000000C)

        self.APORT1XREQ = RM_Field_IDAC0_APORTREQ_APORT1XREQ(self)
        self.zz_fdict['APORT1XREQ'] = self.APORT1XREQ
        self.APORT1YREQ = RM_Field_IDAC0_APORTREQ_APORT1YREQ(self)
        self.zz_fdict['APORT1YREQ'] = self.APORT1YREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_IDAC0_APORTCONFLICT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_IDAC0_APORTCONFLICT, self).__init__(rmio, label,
            0x40006000, 0x038,
            'APORTCONFLICT', 'IDAC0.APORTCONFLICT', 'read-only',
            "",
            0x00000000, 0x0000000C)

        self.APORT1XCONFLICT = RM_Field_IDAC0_APORTCONFLICT_APORT1XCONFLICT(self)
        self.zz_fdict['APORT1XCONFLICT'] = self.APORT1XCONFLICT
        self.APORT1YCONFLICT = RM_Field_IDAC0_APORTCONFLICT_APORT1YCONFLICT(self)
        self.zz_fdict['APORT1YCONFLICT'] = self.APORT1YCONFLICT
        self.__dict__['zz_frozen'] = True


