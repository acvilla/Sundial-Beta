
from static import Base_RM_Register
from ACMP0_field import *


class RM_Register_ACMP0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_CTRL, self).__init__(rmio, label,
            0x40000000, 0x000,
            'CTRL', 'ACMP0.CTRL', 'read-write',
            "",
            0x07000000, 0xBF3CF73D)

        self.EN = RM_Field_ACMP0_CTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.INACTVAL = RM_Field_ACMP0_CTRL_INACTVAL(self)
        self.zz_fdict['INACTVAL'] = self.INACTVAL
        self.GPIOINV = RM_Field_ACMP0_CTRL_GPIOINV(self)
        self.zz_fdict['GPIOINV'] = self.GPIOINV
        self.REFRESHRATE = RM_Field_ACMP0_CTRL_REFRESHRATE(self)
        self.zz_fdict['REFRESHRATE'] = self.REFRESHRATE
        self.APORTXMASTERDIS = RM_Field_ACMP0_CTRL_APORTXMASTERDIS(self)
        self.zz_fdict['APORTXMASTERDIS'] = self.APORTXMASTERDIS
        self.APORTYMASTERDIS = RM_Field_ACMP0_CTRL_APORTYMASTERDIS(self)
        self.zz_fdict['APORTYMASTERDIS'] = self.APORTYMASTERDIS
        self.APORTVMASTERDIS = RM_Field_ACMP0_CTRL_APORTVMASTERDIS(self)
        self.zz_fdict['APORTVMASTERDIS'] = self.APORTVMASTERDIS
        self.PWRSEL = RM_Field_ACMP0_CTRL_PWRSEL(self)
        self.zz_fdict['PWRSEL'] = self.PWRSEL
        self.ACCURACY = RM_Field_ACMP0_CTRL_ACCURACY(self)
        self.zz_fdict['ACCURACY'] = self.ACCURACY
        self.INPUTRANGE = RM_Field_ACMP0_CTRL_INPUTRANGE(self)
        self.zz_fdict['INPUTRANGE'] = self.INPUTRANGE
        self.IRISE = RM_Field_ACMP0_CTRL_IRISE(self)
        self.zz_fdict['IRISE'] = self.IRISE
        self.IFALL = RM_Field_ACMP0_CTRL_IFALL(self)
        self.zz_fdict['IFALL'] = self.IFALL
        self.BIASPROG = RM_Field_ACMP0_CTRL_BIASPROG(self)
        self.zz_fdict['BIASPROG'] = self.BIASPROG
        self.FULLBIAS = RM_Field_ACMP0_CTRL_FULLBIAS(self)
        self.zz_fdict['FULLBIAS'] = self.FULLBIAS
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP0_INPUTSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_INPUTSEL, self).__init__(rmio, label,
            0x40000000, 0x004,
            'INPUTSEL', 'ACMP0.INPUTSEL', 'read-write',
            "",
            0x00000000, 0x757FFFFF)

        self.POSSEL = RM_Field_ACMP0_INPUTSEL_POSSEL(self)
        self.zz_fdict['POSSEL'] = self.POSSEL
        self.NEGSEL = RM_Field_ACMP0_INPUTSEL_NEGSEL(self)
        self.zz_fdict['NEGSEL'] = self.NEGSEL
        self.VASEL = RM_Field_ACMP0_INPUTSEL_VASEL(self)
        self.zz_fdict['VASEL'] = self.VASEL
        self.VBSEL = RM_Field_ACMP0_INPUTSEL_VBSEL(self)
        self.zz_fdict['VBSEL'] = self.VBSEL
        self.VLPSEL = RM_Field_ACMP0_INPUTSEL_VLPSEL(self)
        self.zz_fdict['VLPSEL'] = self.VLPSEL
        self.CSRESEN = RM_Field_ACMP0_INPUTSEL_CSRESEN(self)
        self.zz_fdict['CSRESEN'] = self.CSRESEN
        self.CSRESSEL = RM_Field_ACMP0_INPUTSEL_CSRESSEL(self)
        self.zz_fdict['CSRESSEL'] = self.CSRESSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP0_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_STATUS, self).__init__(rmio, label,
            0x40000000, 0x008,
            'STATUS', 'ACMP0.STATUS', 'read-only',
            "",
            0x00000000, 0x0000000F)

        self.ACMPACT = RM_Field_ACMP0_STATUS_ACMPACT(self)
        self.zz_fdict['ACMPACT'] = self.ACMPACT
        self.ACMPOUT = RM_Field_ACMP0_STATUS_ACMPOUT(self)
        self.zz_fdict['ACMPOUT'] = self.ACMPOUT
        self.APORTCONFLICT = RM_Field_ACMP0_STATUS_APORTCONFLICT(self)
        self.zz_fdict['APORTCONFLICT'] = self.APORTCONFLICT
        self.EXTIFACT = RM_Field_ACMP0_STATUS_EXTIFACT(self)
        self.zz_fdict['EXTIFACT'] = self.EXTIFACT
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP0_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_IF, self).__init__(rmio, label,
            0x40000000, 0x00C,
            'IF', 'ACMP0.IF', 'read-only',
            "",
            0x00000000, 0x00000007)

        self.EDGE = RM_Field_ACMP0_IF_EDGE(self)
        self.zz_fdict['EDGE'] = self.EDGE
        self.WARMUP = RM_Field_ACMP0_IF_WARMUP(self)
        self.zz_fdict['WARMUP'] = self.WARMUP
        self.APORTCONFLICT = RM_Field_ACMP0_IF_APORTCONFLICT(self)
        self.zz_fdict['APORTCONFLICT'] = self.APORTCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP0_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_IFS, self).__init__(rmio, label,
            0x40000000, 0x010,
            'IFS', 'ACMP0.IFS', 'write-only',
            "",
            0x00000000, 0x00000007)

        self.EDGE = RM_Field_ACMP0_IFS_EDGE(self)
        self.zz_fdict['EDGE'] = self.EDGE
        self.WARMUP = RM_Field_ACMP0_IFS_WARMUP(self)
        self.zz_fdict['WARMUP'] = self.WARMUP
        self.APORTCONFLICT = RM_Field_ACMP0_IFS_APORTCONFLICT(self)
        self.zz_fdict['APORTCONFLICT'] = self.APORTCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP0_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_IFC, self).__init__(rmio, label,
            0x40000000, 0x014,
            'IFC', 'ACMP0.IFC', 'write-only',
            "",
            0x00000000, 0x00000007)

        self.EDGE = RM_Field_ACMP0_IFC_EDGE(self)
        self.zz_fdict['EDGE'] = self.EDGE
        self.WARMUP = RM_Field_ACMP0_IFC_WARMUP(self)
        self.zz_fdict['WARMUP'] = self.WARMUP
        self.APORTCONFLICT = RM_Field_ACMP0_IFC_APORTCONFLICT(self)
        self.zz_fdict['APORTCONFLICT'] = self.APORTCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP0_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_IEN, self).__init__(rmio, label,
            0x40000000, 0x018,
            'IEN', 'ACMP0.IEN', 'read-write',
            "",
            0x00000000, 0x00000007)

        self.EDGE = RM_Field_ACMP0_IEN_EDGE(self)
        self.zz_fdict['EDGE'] = self.EDGE
        self.WARMUP = RM_Field_ACMP0_IEN_WARMUP(self)
        self.zz_fdict['WARMUP'] = self.WARMUP
        self.APORTCONFLICT = RM_Field_ACMP0_IEN_APORTCONFLICT(self)
        self.zz_fdict['APORTCONFLICT'] = self.APORTCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP0_APORTREQ(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_APORTREQ, self).__init__(rmio, label,
            0x40000000, 0x020,
            'APORTREQ', 'ACMP0.APORTREQ', 'read-only',
            "",
            0x00000000, 0x000003FF)

        self.APORT0XREQ = RM_Field_ACMP0_APORTREQ_APORT0XREQ(self)
        self.zz_fdict['APORT0XREQ'] = self.APORT0XREQ
        self.APORT0YREQ = RM_Field_ACMP0_APORTREQ_APORT0YREQ(self)
        self.zz_fdict['APORT0YREQ'] = self.APORT0YREQ
        self.APORT1XREQ = RM_Field_ACMP0_APORTREQ_APORT1XREQ(self)
        self.zz_fdict['APORT1XREQ'] = self.APORT1XREQ
        self.APORT1YREQ = RM_Field_ACMP0_APORTREQ_APORT1YREQ(self)
        self.zz_fdict['APORT1YREQ'] = self.APORT1YREQ
        self.APORT2XREQ = RM_Field_ACMP0_APORTREQ_APORT2XREQ(self)
        self.zz_fdict['APORT2XREQ'] = self.APORT2XREQ
        self.APORT2YREQ = RM_Field_ACMP0_APORTREQ_APORT2YREQ(self)
        self.zz_fdict['APORT2YREQ'] = self.APORT2YREQ
        self.APORT3XREQ = RM_Field_ACMP0_APORTREQ_APORT3XREQ(self)
        self.zz_fdict['APORT3XREQ'] = self.APORT3XREQ
        self.APORT3YREQ = RM_Field_ACMP0_APORTREQ_APORT3YREQ(self)
        self.zz_fdict['APORT3YREQ'] = self.APORT3YREQ
        self.APORT4XREQ = RM_Field_ACMP0_APORTREQ_APORT4XREQ(self)
        self.zz_fdict['APORT4XREQ'] = self.APORT4XREQ
        self.APORT4YREQ = RM_Field_ACMP0_APORTREQ_APORT4YREQ(self)
        self.zz_fdict['APORT4YREQ'] = self.APORT4YREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP0_APORTCONFLICT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_APORTCONFLICT, self).__init__(rmio, label,
            0x40000000, 0x024,
            'APORTCONFLICT', 'ACMP0.APORTCONFLICT', 'read-only',
            "",
            0x00000000, 0x000003FF)

        self.APORT0XCONFLICT = RM_Field_ACMP0_APORTCONFLICT_APORT0XCONFLICT(self)
        self.zz_fdict['APORT0XCONFLICT'] = self.APORT0XCONFLICT
        self.APORT0YCONFLICT = RM_Field_ACMP0_APORTCONFLICT_APORT0YCONFLICT(self)
        self.zz_fdict['APORT0YCONFLICT'] = self.APORT0YCONFLICT
        self.APORT1XCONFLICT = RM_Field_ACMP0_APORTCONFLICT_APORT1XCONFLICT(self)
        self.zz_fdict['APORT1XCONFLICT'] = self.APORT1XCONFLICT
        self.APORT1YCONFLICT = RM_Field_ACMP0_APORTCONFLICT_APORT1YCONFLICT(self)
        self.zz_fdict['APORT1YCONFLICT'] = self.APORT1YCONFLICT
        self.APORT2XCONFLICT = RM_Field_ACMP0_APORTCONFLICT_APORT2XCONFLICT(self)
        self.zz_fdict['APORT2XCONFLICT'] = self.APORT2XCONFLICT
        self.APORT2YCONFLICT = RM_Field_ACMP0_APORTCONFLICT_APORT2YCONFLICT(self)
        self.zz_fdict['APORT2YCONFLICT'] = self.APORT2YCONFLICT
        self.APORT3XCONFLICT = RM_Field_ACMP0_APORTCONFLICT_APORT3XCONFLICT(self)
        self.zz_fdict['APORT3XCONFLICT'] = self.APORT3XCONFLICT
        self.APORT3YCONFLICT = RM_Field_ACMP0_APORTCONFLICT_APORT3YCONFLICT(self)
        self.zz_fdict['APORT3YCONFLICT'] = self.APORT3YCONFLICT
        self.APORT4XCONFLICT = RM_Field_ACMP0_APORTCONFLICT_APORT4XCONFLICT(self)
        self.zz_fdict['APORT4XCONFLICT'] = self.APORT4XCONFLICT
        self.APORT4YCONFLICT = RM_Field_ACMP0_APORTCONFLICT_APORT4YCONFLICT(self)
        self.zz_fdict['APORT4YCONFLICT'] = self.APORT4YCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP0_HYSTERESIS0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_HYSTERESIS0, self).__init__(rmio, label,
            0x40000000, 0x028,
            'HYSTERESIS0', 'ACMP0.HYSTERESIS0', 'read-write',
            "",
            0x00000000, 0x3F3F000F)

        self.HYST = RM_Field_ACMP0_HYSTERESIS0_HYST(self)
        self.zz_fdict['HYST'] = self.HYST
        self.DIVVA = RM_Field_ACMP0_HYSTERESIS0_DIVVA(self)
        self.zz_fdict['DIVVA'] = self.DIVVA
        self.DIVVB = RM_Field_ACMP0_HYSTERESIS0_DIVVB(self)
        self.zz_fdict['DIVVB'] = self.DIVVB
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP0_HYSTERESIS1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_HYSTERESIS1, self).__init__(rmio, label,
            0x40000000, 0x02C,
            'HYSTERESIS1', 'ACMP0.HYSTERESIS1', 'read-write',
            "",
            0x00000000, 0x3F3F000F)

        self.HYST = RM_Field_ACMP0_HYSTERESIS1_HYST(self)
        self.zz_fdict['HYST'] = self.HYST
        self.DIVVA = RM_Field_ACMP0_HYSTERESIS1_DIVVA(self)
        self.zz_fdict['DIVVA'] = self.DIVVA
        self.DIVVB = RM_Field_ACMP0_HYSTERESIS1_DIVVB(self)
        self.zz_fdict['DIVVB'] = self.DIVVB
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP0_TEST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_TEST, self).__init__(rmio, label,
            0x40000000, 0x030,
            'TEST', 'ACMP0.TEST', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.VDDCP4MUXDIS = RM_Field_ACMP0_TEST_VDDCP4MUXDIS(self)
        self.zz_fdict['VDDCP4MUXDIS'] = self.VDDCP4MUXDIS
        self.VDDCP4VBGDIVDIS = RM_Field_ACMP0_TEST_VDDCP4VBGDIVDIS(self)
        self.zz_fdict['VDDCP4VBGDIVDIS'] = self.VDDCP4VBGDIVDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP0_ROUTEPEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_ROUTEPEN, self).__init__(rmio, label,
            0x40000000, 0x040,
            'ROUTEPEN', 'ACMP0.ROUTEPEN', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.OUTPEN = RM_Field_ACMP0_ROUTEPEN_OUTPEN(self)
        self.zz_fdict['OUTPEN'] = self.OUTPEN
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP0_ROUTELOC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_ROUTELOC0, self).__init__(rmio, label,
            0x40000000, 0x044,
            'ROUTELOC0', 'ACMP0.ROUTELOC0', 'read-write',
            "",
            0x00000000, 0x0000003F)

        self.OUTLOC = RM_Field_ACMP0_ROUTELOC0_OUTLOC(self)
        self.zz_fdict['OUTLOC'] = self.OUTLOC
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP0_EXTIFCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP0_EXTIFCTRL, self).__init__(rmio, label,
            0x40000000, 0x048,
            'EXTIFCTRL', 'ACMP0.EXTIFCTRL', 'read-write',
            "",
            0x00000000, 0x000000F1)

        self.EN = RM_Field_ACMP0_EXTIFCTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.APORTSEL = RM_Field_ACMP0_EXTIFCTRL_APORTSEL(self)
        self.zz_fdict['APORTSEL'] = self.APORTSEL
        self.__dict__['zz_frozen'] = True


