
from static import Base_RM_Field
from TRNG0_enum import *


class RM_Field_TRNG0_CONTROL_ENABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_CONTROL_ENABLE, self).__init__(register,
            'ENABLE', 'TRNG0.CONTROL.ENABLE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_CONTROL_CONTROL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_CONTROL_CONTROL, self).__init__(register,
            'CONTROL', 'TRNG0.CONTROL.CONTROL', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_CONTROL_TESTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_CONTROL_TESTEN, self).__init__(register,
            'TESTEN', 'TRNG0.CONTROL.TESTEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_CONTROL_CONDBYPASS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_CONTROL_CONDBYPASS, self).__init__(register,
            'CONDBYPASS', 'TRNG0.CONTROL.CONDBYPASS', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_CONTROL_INTENREP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_CONTROL_INTENREP, self).__init__(register,
            'INTENREP', 'TRNG0.CONTROL.INTENREP', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_CONTROL_INTENPROP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_CONTROL_INTENPROP1, self).__init__(register,
            'INTENPROP1', 'TRNG0.CONTROL.INTENPROP1', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_CONTROL_INTENPROP2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_CONTROL_INTENPROP2, self).__init__(register,
            'INTENPROP2', 'TRNG0.CONTROL.INTENPROP2', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_CONTROL_INTENFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_CONTROL_INTENFULL, self).__init__(register,
            'INTENFULL', 'TRNG0.CONTROL.INTENFULL', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_CONTROL_SOFTRESET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_CONTROL_SOFTRESET, self).__init__(register,
            'SOFTRESET', 'TRNG0.CONTROL.SOFTRESET', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_CONTROL_INTENPRE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_CONTROL_INTENPRE, self).__init__(register,
            'INTENPRE', 'TRNG0.CONTROL.INTENPRE', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_CONTROL_INTENALM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_CONTROL_INTENALM, self).__init__(register,
            'INTENALM', 'TRNG0.CONTROL.INTENALM', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_CONTROL_FORCERUN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_CONTROL_FORCERUN, self).__init__(register,
            'FORCERUN', 'TRNG0.CONTROL.FORCERUN', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_CONTROL_BYPASSSTARTUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_CONTROL_BYPASSSTARTUP, self).__init__(register,
            'BYPASSSTARTUP', 'TRNG0.CONTROL.BYPASSSTARTUP', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_CONTROL_BYPASSAIS31(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_CONTROL_BYPASSAIS31, self).__init__(register,
            'BYPASSAIS31', 'TRNG0.CONTROL.BYPASSAIS31', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_FIFOLEVEL_VALUE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_FIFOLEVEL_VALUE, self).__init__(register,
            'VALUE', 'TRNG0.FIFOLEVEL.VALUE', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_FIFODEPTH_VALUE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_FIFODEPTH_VALUE, self).__init__(register,
            'VALUE', 'TRNG0.FIFODEPTH.VALUE', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_KEY0_VALUE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_KEY0_VALUE, self).__init__(register,
            'VALUE', 'TRNG0.KEY0.VALUE', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_KEY1_VALUE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_KEY1_VALUE, self).__init__(register,
            'VALUE', 'TRNG0.KEY1.VALUE', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_KEY2_VALUE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_KEY2_VALUE, self).__init__(register,
            'VALUE', 'TRNG0.KEY2.VALUE', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_KEY3_VALUE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_KEY3_VALUE, self).__init__(register,
            'VALUE', 'TRNG0.KEY3.VALUE', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_TESTDATA_VALUE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_TESTDATA_VALUE, self).__init__(register,
            'VALUE', 'TRNG0.TESTDATA.VALUE', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_REPTHRES_VALUE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_REPTHRES_VALUE, self).__init__(register,
            'VALUE', 'TRNG0.REPTHRES.VALUE', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_PROP1THRES_VALUE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_PROP1THRES_VALUE, self).__init__(register,
            'VALUE', 'TRNG0.PROP1THRES.VALUE', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_PROP2THRES_VALUE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_PROP2THRES_VALUE, self).__init__(register,
            'VALUE', 'TRNG0.PROP2THRES.VALUE', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_STATUS_TESTDATABUSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_STATUS_TESTDATABUSY, self).__init__(register,
            'TESTDATABUSY', 'TRNG0.STATUS.TESTDATABUSY', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_STATUS_REPFAIL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_STATUS_REPFAIL, self).__init__(register,
            'REPFAIL', 'TRNG0.STATUS.REPFAIL', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_STATUS_PROP1FAIL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_STATUS_PROP1FAIL, self).__init__(register,
            'PROP1FAIL', 'TRNG0.STATUS.PROP1FAIL', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_STATUS_PROP2FAIL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_STATUS_PROP2FAIL, self).__init__(register,
            'PROP2FAIL', 'TRNG0.STATUS.PROP2FAIL', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_STATUS_FULLINT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_STATUS_FULLINT, self).__init__(register,
            'FULLINT', 'TRNG0.STATUS.FULLINT', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_STATUS_PREINT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_STATUS_PREINT, self).__init__(register,
            'PREINT', 'TRNG0.STATUS.PREINT', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_STATUS_ALMINT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_STATUS_ALMINT, self).__init__(register,
            'ALMINT', 'TRNG0.STATUS.ALMINT', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_STATUS_STARTUPPASS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_STATUS_STARTUPPASS, self).__init__(register,
            'STARTUPPASS', 'TRNG0.STATUS.STARTUPPASS', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_INITWAITVAL_VALUE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_INITWAITVAL_VALUE, self).__init__(register,
            'VALUE', 'TRNG0.INITWAITVAL.VALUE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_TRNG0_FIFO_VALUE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_TRNG0_FIFO_VALUE, self).__init__(register,
            'VALUE', 'TRNG0.FIFO.VALUE', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


