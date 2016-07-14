
from static import Base_RM_Register
from TRNG0_field import *


class RM_Register_TRNG0_CONTROL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TRNG0_CONTROL, self).__init__(rmio, label,
            0x4001d000, 0x000,
            'CONTROL', 'TRNG0.CONTROL', 'read-write',
            "",
            0x00000000, 0x00003FFF)

        self.ENABLE = RM_Field_TRNG0_CONTROL_ENABLE(self)
        self.zz_fdict['ENABLE'] = self.ENABLE
        self.CONTROL = RM_Field_TRNG0_CONTROL_CONTROL(self)
        self.zz_fdict['CONTROL'] = self.CONTROL
        self.TESTEN = RM_Field_TRNG0_CONTROL_TESTEN(self)
        self.zz_fdict['TESTEN'] = self.TESTEN
        self.CONDBYPASS = RM_Field_TRNG0_CONTROL_CONDBYPASS(self)
        self.zz_fdict['CONDBYPASS'] = self.CONDBYPASS
        self.INTENREP = RM_Field_TRNG0_CONTROL_INTENREP(self)
        self.zz_fdict['INTENREP'] = self.INTENREP
        self.INTENPROP1 = RM_Field_TRNG0_CONTROL_INTENPROP1(self)
        self.zz_fdict['INTENPROP1'] = self.INTENPROP1
        self.INTENPROP2 = RM_Field_TRNG0_CONTROL_INTENPROP2(self)
        self.zz_fdict['INTENPROP2'] = self.INTENPROP2
        self.INTENFULL = RM_Field_TRNG0_CONTROL_INTENFULL(self)
        self.zz_fdict['INTENFULL'] = self.INTENFULL
        self.SOFTRESET = RM_Field_TRNG0_CONTROL_SOFTRESET(self)
        self.zz_fdict['SOFTRESET'] = self.SOFTRESET
        self.INTENPRE = RM_Field_TRNG0_CONTROL_INTENPRE(self)
        self.zz_fdict['INTENPRE'] = self.INTENPRE
        self.INTENALM = RM_Field_TRNG0_CONTROL_INTENALM(self)
        self.zz_fdict['INTENALM'] = self.INTENALM
        self.FORCERUN = RM_Field_TRNG0_CONTROL_FORCERUN(self)
        self.zz_fdict['FORCERUN'] = self.FORCERUN
        self.BYPASSSTARTUP = RM_Field_TRNG0_CONTROL_BYPASSSTARTUP(self)
        self.zz_fdict['BYPASSSTARTUP'] = self.BYPASSSTARTUP
        self.BYPASSAIS31 = RM_Field_TRNG0_CONTROL_BYPASSAIS31(self)
        self.zz_fdict['BYPASSAIS31'] = self.BYPASSAIS31
        self.__dict__['zz_frozen'] = True


class RM_Register_TRNG0_FIFOLEVEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TRNG0_FIFOLEVEL, self).__init__(rmio, label,
            0x4001d000, 0x004,
            'FIFOLEVEL', 'TRNG0.FIFOLEVEL', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.VALUE = RM_Field_TRNG0_FIFOLEVEL_VALUE(self)
        self.zz_fdict['VALUE'] = self.VALUE
        self.__dict__['zz_frozen'] = True


class RM_Register_TRNG0_FIFODEPTH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TRNG0_FIFODEPTH, self).__init__(rmio, label,
            0x4001d000, 0x00C,
            'FIFODEPTH', 'TRNG0.FIFODEPTH', 'read-only',
            "",
            0x00000040, 0xFFFFFFFF)

        self.VALUE = RM_Field_TRNG0_FIFODEPTH_VALUE(self)
        self.zz_fdict['VALUE'] = self.VALUE
        self.__dict__['zz_frozen'] = True


class RM_Register_TRNG0_KEY0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TRNG0_KEY0, self).__init__(rmio, label,
            0x4001d000, 0x010,
            'KEY0', 'TRNG0.KEY0', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.VALUE = RM_Field_TRNG0_KEY0_VALUE(self)
        self.zz_fdict['VALUE'] = self.VALUE
        self.__dict__['zz_frozen'] = True


class RM_Register_TRNG0_KEY1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TRNG0_KEY1, self).__init__(rmio, label,
            0x4001d000, 0x014,
            'KEY1', 'TRNG0.KEY1', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.VALUE = RM_Field_TRNG0_KEY1_VALUE(self)
        self.zz_fdict['VALUE'] = self.VALUE
        self.__dict__['zz_frozen'] = True


class RM_Register_TRNG0_KEY2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TRNG0_KEY2, self).__init__(rmio, label,
            0x4001d000, 0x018,
            'KEY2', 'TRNG0.KEY2', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.VALUE = RM_Field_TRNG0_KEY2_VALUE(self)
        self.zz_fdict['VALUE'] = self.VALUE
        self.__dict__['zz_frozen'] = True


class RM_Register_TRNG0_KEY3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TRNG0_KEY3, self).__init__(rmio, label,
            0x4001d000, 0x01C,
            'KEY3', 'TRNG0.KEY3', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.VALUE = RM_Field_TRNG0_KEY3_VALUE(self)
        self.zz_fdict['VALUE'] = self.VALUE
        self.__dict__['zz_frozen'] = True


class RM_Register_TRNG0_TESTDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TRNG0_TESTDATA, self).__init__(rmio, label,
            0x4001d000, 0x020,
            'TESTDATA', 'TRNG0.TESTDATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.VALUE = RM_Field_TRNG0_TESTDATA_VALUE(self)
        self.zz_fdict['VALUE'] = self.VALUE
        self.__dict__['zz_frozen'] = True


class RM_Register_TRNG0_REPTHRES(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TRNG0_REPTHRES, self).__init__(rmio, label,
            0x4001d000, 0x024,
            'REPTHRES', 'TRNG0.REPTHRES', 'read-write',
            "",
            0x0000003D, 0xFFFFFFFF)

        self.VALUE = RM_Field_TRNG0_REPTHRES_VALUE(self)
        self.zz_fdict['VALUE'] = self.VALUE
        self.__dict__['zz_frozen'] = True


class RM_Register_TRNG0_PROP1THRES(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TRNG0_PROP1THRES, self).__init__(rmio, label,
            0x4001d000, 0x028,
            'PROP1THRES', 'TRNG0.PROP1THRES', 'read-write',
            "",
            0x00000033, 0xFFFFFFFF)

        self.VALUE = RM_Field_TRNG0_PROP1THRES_VALUE(self)
        self.zz_fdict['VALUE'] = self.VALUE
        self.__dict__['zz_frozen'] = True


class RM_Register_TRNG0_PROP2THRES(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TRNG0_PROP2THRES, self).__init__(rmio, label,
            0x4001d000, 0x02C,
            'PROP2THRES', 'TRNG0.PROP2THRES', 'read-write',
            "",
            0x000008C0, 0xFFFFFFFF)

        self.VALUE = RM_Field_TRNG0_PROP2THRES_VALUE(self)
        self.zz_fdict['VALUE'] = self.VALUE
        self.__dict__['zz_frozen'] = True


class RM_Register_TRNG0_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TRNG0_STATUS, self).__init__(rmio, label,
            0x4001d000, 0x030,
            'STATUS', 'TRNG0.STATUS', 'read-only',
            "",
            0x00000000, 0x000007F1)

        self.TESTDATABUSY = RM_Field_TRNG0_STATUS_TESTDATABUSY(self)
        self.zz_fdict['TESTDATABUSY'] = self.TESTDATABUSY
        self.REPFAIL = RM_Field_TRNG0_STATUS_REPFAIL(self)
        self.zz_fdict['REPFAIL'] = self.REPFAIL
        self.PROP1FAIL = RM_Field_TRNG0_STATUS_PROP1FAIL(self)
        self.zz_fdict['PROP1FAIL'] = self.PROP1FAIL
        self.PROP2FAIL = RM_Field_TRNG0_STATUS_PROP2FAIL(self)
        self.zz_fdict['PROP2FAIL'] = self.PROP2FAIL
        self.FULLINT = RM_Field_TRNG0_STATUS_FULLINT(self)
        self.zz_fdict['FULLINT'] = self.FULLINT
        self.PREINT = RM_Field_TRNG0_STATUS_PREINT(self)
        self.zz_fdict['PREINT'] = self.PREINT
        self.ALMINT = RM_Field_TRNG0_STATUS_ALMINT(self)
        self.zz_fdict['ALMINT'] = self.ALMINT
        self.STARTUPPASS = RM_Field_TRNG0_STATUS_STARTUPPASS(self)
        self.zz_fdict['STARTUPPASS'] = self.STARTUPPASS
        self.__dict__['zz_frozen'] = True


class RM_Register_TRNG0_INITWAITVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TRNG0_INITWAITVAL, self).__init__(rmio, label,
            0x4001d000, 0x034,
            'INITWAITVAL', 'TRNG0.INITWAITVAL', 'read-write',
            "",
            0x000000FF, 0x000000FF)

        self.VALUE = RM_Field_TRNG0_INITWAITVAL_VALUE(self)
        self.zz_fdict['VALUE'] = self.VALUE
        self.__dict__['zz_frozen'] = True


class RM_Register_TRNG0_FIFO(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TRNG0_FIFO, self).__init__(rmio, label,
            0x4001d000, 0x100,
            'FIFO', 'TRNG0.FIFO', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.VALUE = RM_Field_TRNG0_FIFO_VALUE(self)
        self.zz_fdict['VALUE'] = self.VALUE
        self.__dict__['zz_frozen'] = True


