
from static import Base_RM_Register
from ACMP1_field import *


class RM_Register_ACMP1_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP1_CTRL, self).__init__(rmio, label,
            0x40000400, 0x000,
            'CTRL', 'ACMP1.CTRL', 'read-write',
            "",
            0x07000000, 0xBF3CF73D)

        self.EN = RM_Field_ACMP1_CTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.INACTVAL = RM_Field_ACMP1_CTRL_INACTVAL(self)
        self.zz_fdict['INACTVAL'] = self.INACTVAL
        self.GPIOINV = RM_Field_ACMP1_CTRL_GPIOINV(self)
        self.zz_fdict['GPIOINV'] = self.GPIOINV
        self.DUTYFSEL = RM_Field_ACMP1_CTRL_DUTYFSEL(self)
        self.zz_fdict['DUTYFSEL'] = self.DUTYFSEL
        self.BUSXMASTERDIS = RM_Field_ACMP1_CTRL_BUSXMASTERDIS(self)
        self.zz_fdict['BUSXMASTERDIS'] = self.BUSXMASTERDIS
        self.BUSYMASTERDIS = RM_Field_ACMP1_CTRL_BUSYMASTERDIS(self)
        self.zz_fdict['BUSYMASTERDIS'] = self.BUSYMASTERDIS
        self.BUSVMASTERDIS = RM_Field_ACMP1_CTRL_BUSVMASTERDIS(self)
        self.zz_fdict['BUSVMASTERDIS'] = self.BUSVMASTERDIS
        self.PWRSEL = RM_Field_ACMP1_CTRL_PWRSEL(self)
        self.zz_fdict['PWRSEL'] = self.PWRSEL
        self.ACCURACY = RM_Field_ACMP1_CTRL_ACCURACY(self)
        self.zz_fdict['ACCURACY'] = self.ACCURACY
        self.INPUTRANGE = RM_Field_ACMP1_CTRL_INPUTRANGE(self)
        self.zz_fdict['INPUTRANGE'] = self.INPUTRANGE
        self.IRISE = RM_Field_ACMP1_CTRL_IRISE(self)
        self.zz_fdict['IRISE'] = self.IRISE
        self.IFALL = RM_Field_ACMP1_CTRL_IFALL(self)
        self.zz_fdict['IFALL'] = self.IFALL
        self.BIASPROG = RM_Field_ACMP1_CTRL_BIASPROG(self)
        self.zz_fdict['BIASPROG'] = self.BIASPROG
        self.FULLBIAS = RM_Field_ACMP1_CTRL_FULLBIAS(self)
        self.zz_fdict['FULLBIAS'] = self.FULLBIAS
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP1_INPUTSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP1_INPUTSEL, self).__init__(rmio, label,
            0x40000400, 0x004,
            'INPUTSEL', 'ACMP1.INPUTSEL', 'read-write',
            "",
            0x00000000, 0x757FFFFF)

        self.POSSEL = RM_Field_ACMP1_INPUTSEL_POSSEL(self)
        self.zz_fdict['POSSEL'] = self.POSSEL
        self.NEGSEL = RM_Field_ACMP1_INPUTSEL_NEGSEL(self)
        self.zz_fdict['NEGSEL'] = self.NEGSEL
        self.VASEL = RM_Field_ACMP1_INPUTSEL_VASEL(self)
        self.zz_fdict['VASEL'] = self.VASEL
        self.VBSEL = RM_Field_ACMP1_INPUTSEL_VBSEL(self)
        self.zz_fdict['VBSEL'] = self.VBSEL
        self.VLPSEL = RM_Field_ACMP1_INPUTSEL_VLPSEL(self)
        self.zz_fdict['VLPSEL'] = self.VLPSEL
        self.CSRESEN = RM_Field_ACMP1_INPUTSEL_CSRESEN(self)
        self.zz_fdict['CSRESEN'] = self.CSRESEN
        self.CSRESSEL = RM_Field_ACMP1_INPUTSEL_CSRESSEL(self)
        self.zz_fdict['CSRESSEL'] = self.CSRESSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP1_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP1_STATUS, self).__init__(rmio, label,
            0x40000400, 0x008,
            'STATUS', 'ACMP1.STATUS', 'read-only',
            "",
            0x00000000, 0x00000007)

        self.ACMPACT = RM_Field_ACMP1_STATUS_ACMPACT(self)
        self.zz_fdict['ACMPACT'] = self.ACMPACT
        self.ACMPOUT = RM_Field_ACMP1_STATUS_ACMPOUT(self)
        self.zz_fdict['ACMPOUT'] = self.ACMPOUT
        self.BUSCONFLICT = RM_Field_ACMP1_STATUS_BUSCONFLICT(self)
        self.zz_fdict['BUSCONFLICT'] = self.BUSCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP1_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP1_IF, self).__init__(rmio, label,
            0x40000400, 0x00C,
            'IF', 'ACMP1.IF', 'read-only',
            "",
            0x00000000, 0x00000007)

        self.EDGE = RM_Field_ACMP1_IF_EDGE(self)
        self.zz_fdict['EDGE'] = self.EDGE
        self.WARMUP = RM_Field_ACMP1_IF_WARMUP(self)
        self.zz_fdict['WARMUP'] = self.WARMUP
        self.BUSCONFLICT = RM_Field_ACMP1_IF_BUSCONFLICT(self)
        self.zz_fdict['BUSCONFLICT'] = self.BUSCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP1_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP1_IFS, self).__init__(rmio, label,
            0x40000400, 0x010,
            'IFS', 'ACMP1.IFS', 'write-only',
            "",
            0x00000000, 0x00000007)

        self.EDGE = RM_Field_ACMP1_IFS_EDGE(self)
        self.zz_fdict['EDGE'] = self.EDGE
        self.WARMUP = RM_Field_ACMP1_IFS_WARMUP(self)
        self.zz_fdict['WARMUP'] = self.WARMUP
        self.BUSCONFLICT = RM_Field_ACMP1_IFS_BUSCONFLICT(self)
        self.zz_fdict['BUSCONFLICT'] = self.BUSCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP1_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP1_IFC, self).__init__(rmio, label,
            0x40000400, 0x014,
            'IFC', 'ACMP1.IFC', 'write-only',
            "",
            0x00000000, 0x00000007)

        self.EDGE = RM_Field_ACMP1_IFC_EDGE(self)
        self.zz_fdict['EDGE'] = self.EDGE
        self.WARMUP = RM_Field_ACMP1_IFC_WARMUP(self)
        self.zz_fdict['WARMUP'] = self.WARMUP
        self.BUSCONFLICT = RM_Field_ACMP1_IFC_BUSCONFLICT(self)
        self.zz_fdict['BUSCONFLICT'] = self.BUSCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP1_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP1_IEN, self).__init__(rmio, label,
            0x40000400, 0x018,
            'IEN', 'ACMP1.IEN', 'read-write',
            "",
            0x00000000, 0x00000007)

        self.EDGE = RM_Field_ACMP1_IEN_EDGE(self)
        self.zz_fdict['EDGE'] = self.EDGE
        self.WARMUP = RM_Field_ACMP1_IEN_WARMUP(self)
        self.zz_fdict['WARMUP'] = self.WARMUP
        self.BUSCONFLICT = RM_Field_ACMP1_IEN_BUSCONFLICT(self)
        self.zz_fdict['BUSCONFLICT'] = self.BUSCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP1_BUSREQ(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP1_BUSREQ, self).__init__(rmio, label,
            0x40000400, 0x020,
            'BUSREQ', 'ACMP1.BUSREQ', 'read-only',
            "",
            0x00000000, 0x000003FF)

        self.BUS0XREQ = RM_Field_ACMP1_BUSREQ_BUS0XREQ(self)
        self.zz_fdict['BUS0XREQ'] = self.BUS0XREQ
        self.BUS0YREQ = RM_Field_ACMP1_BUSREQ_BUS0YREQ(self)
        self.zz_fdict['BUS0YREQ'] = self.BUS0YREQ
        self.BUS1XREQ = RM_Field_ACMP1_BUSREQ_BUS1XREQ(self)
        self.zz_fdict['BUS1XREQ'] = self.BUS1XREQ
        self.BUS1YREQ = RM_Field_ACMP1_BUSREQ_BUS1YREQ(self)
        self.zz_fdict['BUS1YREQ'] = self.BUS1YREQ
        self.BUS2XREQ = RM_Field_ACMP1_BUSREQ_BUS2XREQ(self)
        self.zz_fdict['BUS2XREQ'] = self.BUS2XREQ
        self.BUS2YREQ = RM_Field_ACMP1_BUSREQ_BUS2YREQ(self)
        self.zz_fdict['BUS2YREQ'] = self.BUS2YREQ
        self.BUS3XREQ = RM_Field_ACMP1_BUSREQ_BUS3XREQ(self)
        self.zz_fdict['BUS3XREQ'] = self.BUS3XREQ
        self.BUS3YREQ = RM_Field_ACMP1_BUSREQ_BUS3YREQ(self)
        self.zz_fdict['BUS3YREQ'] = self.BUS3YREQ
        self.BUS4XREQ = RM_Field_ACMP1_BUSREQ_BUS4XREQ(self)
        self.zz_fdict['BUS4XREQ'] = self.BUS4XREQ
        self.BUS4YREQ = RM_Field_ACMP1_BUSREQ_BUS4YREQ(self)
        self.zz_fdict['BUS4YREQ'] = self.BUS4YREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP1_BUSCONFLICT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP1_BUSCONFLICT, self).__init__(rmio, label,
            0x40000400, 0x024,
            'BUSCONFLICT', 'ACMP1.BUSCONFLICT', 'read-only',
            "",
            0x00000000, 0x000003FF)

        self.BUS0XCONFLICT = RM_Field_ACMP1_BUSCONFLICT_BUS0XCONFLICT(self)
        self.zz_fdict['BUS0XCONFLICT'] = self.BUS0XCONFLICT
        self.BUS0YCONFLICT = RM_Field_ACMP1_BUSCONFLICT_BUS0YCONFLICT(self)
        self.zz_fdict['BUS0YCONFLICT'] = self.BUS0YCONFLICT
        self.BUS1XCONFLICT = RM_Field_ACMP1_BUSCONFLICT_BUS1XCONFLICT(self)
        self.zz_fdict['BUS1XCONFLICT'] = self.BUS1XCONFLICT
        self.BUS1YCONFLICT = RM_Field_ACMP1_BUSCONFLICT_BUS1YCONFLICT(self)
        self.zz_fdict['BUS1YCONFLICT'] = self.BUS1YCONFLICT
        self.BUS2XCONFLICT = RM_Field_ACMP1_BUSCONFLICT_BUS2XCONFLICT(self)
        self.zz_fdict['BUS2XCONFLICT'] = self.BUS2XCONFLICT
        self.BUS2YCONFLICT = RM_Field_ACMP1_BUSCONFLICT_BUS2YCONFLICT(self)
        self.zz_fdict['BUS2YCONFLICT'] = self.BUS2YCONFLICT
        self.BUS3XCONFLICT = RM_Field_ACMP1_BUSCONFLICT_BUS3XCONFLICT(self)
        self.zz_fdict['BUS3XCONFLICT'] = self.BUS3XCONFLICT
        self.BUS3YCONFLICT = RM_Field_ACMP1_BUSCONFLICT_BUS3YCONFLICT(self)
        self.zz_fdict['BUS3YCONFLICT'] = self.BUS3YCONFLICT
        self.BUS4XCONFLICT = RM_Field_ACMP1_BUSCONFLICT_BUS4XCONFLICT(self)
        self.zz_fdict['BUS4XCONFLICT'] = self.BUS4XCONFLICT
        self.BUS4YCONFLICT = RM_Field_ACMP1_BUSCONFLICT_BUS4YCONFLICT(self)
        self.zz_fdict['BUS4YCONFLICT'] = self.BUS4YCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP1_HYSTERESIS0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP1_HYSTERESIS0, self).__init__(rmio, label,
            0x40000400, 0x028,
            'HYSTERESIS0', 'ACMP1.HYSTERESIS0', 'read-write',
            "",
            0x00000000, 0x3F3F000F)

        self.HYST = RM_Field_ACMP1_HYSTERESIS0_HYST(self)
        self.zz_fdict['HYST'] = self.HYST
        self.DIVVA = RM_Field_ACMP1_HYSTERESIS0_DIVVA(self)
        self.zz_fdict['DIVVA'] = self.DIVVA
        self.DIVVB = RM_Field_ACMP1_HYSTERESIS0_DIVVB(self)
        self.zz_fdict['DIVVB'] = self.DIVVB
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP1_HYSTERESIS1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP1_HYSTERESIS1, self).__init__(rmio, label,
            0x40000400, 0x02C,
            'HYSTERESIS1', 'ACMP1.HYSTERESIS1', 'read-write',
            "",
            0x00000000, 0x3F3F000F)

        self.HYST = RM_Field_ACMP1_HYSTERESIS1_HYST(self)
        self.zz_fdict['HYST'] = self.HYST
        self.DIVVA = RM_Field_ACMP1_HYSTERESIS1_DIVVA(self)
        self.zz_fdict['DIVVA'] = self.DIVVA
        self.DIVVB = RM_Field_ACMP1_HYSTERESIS1_DIVVB(self)
        self.zz_fdict['DIVVB'] = self.DIVVB
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP1_TEST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP1_TEST, self).__init__(rmio, label,
            0x40000400, 0x030,
            'TEST', 'ACMP1.TEST', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.VDDCP4MUXDIS = RM_Field_ACMP1_TEST_VDDCP4MUXDIS(self)
        self.zz_fdict['VDDCP4MUXDIS'] = self.VDDCP4MUXDIS
        self.VDDCP4VBGDIVDIS = RM_Field_ACMP1_TEST_VDDCP4VBGDIVDIS(self)
        self.zz_fdict['VDDCP4VBGDIVDIS'] = self.VDDCP4VBGDIVDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP1_ROUTEPEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP1_ROUTEPEN, self).__init__(rmio, label,
            0x40000400, 0x040,
            'ROUTEPEN', 'ACMP1.ROUTEPEN', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.OUTPEN = RM_Field_ACMP1_ROUTEPEN_OUTPEN(self)
        self.zz_fdict['OUTPEN'] = self.OUTPEN
        self.__dict__['zz_frozen'] = True


class RM_Register_ACMP1_ROUTELOC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ACMP1_ROUTELOC0, self).__init__(rmio, label,
            0x40000400, 0x044,
            'ROUTELOC0', 'ACMP1.ROUTELOC0', 'read-write',
            "",
            0x00000000, 0x0000003F)

        self.OUTLOC = RM_Field_ACMP1_ROUTELOC0_OUTLOC(self)
        self.zz_fdict['OUTLOC'] = self.OUTLOC
        self.__dict__['zz_frozen'] = True


