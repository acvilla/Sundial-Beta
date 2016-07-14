
from static import Base_RM_Field
from CRC_enum import *


class RM_Field_CRC_CTRL_INPUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRC_CTRL_INPUTINV, self).__init__(register,
            'INPUTINV', 'CRC.CTRL.INPUTINV', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRC_CTRL_OUTPUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRC_CTRL_OUTPUTINV, self).__init__(register,
            'OUTPUTINV', 'CRC.CTRL.OUTPUTINV', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRC_CTRL_CRCWIDTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRC_CTRL_CRCWIDTH, self).__init__(register,
            'CRCWIDTH', 'CRC.CTRL.CRCWIDTH', 'read-write',
            "",
            2, 2,
            RM_Enum_CRC_CTRL_CRCWIDTH(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRC_CTRL_INPUTBITORDER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRC_CTRL_INPUTBITORDER, self).__init__(register,
            'INPUTBITORDER', 'CRC.CTRL.INPUTBITORDER', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRC_CTRL_BYTEREVERSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRC_CTRL_BYTEREVERSE, self).__init__(register,
            'BYTEREVERSE', 'CRC.CTRL.BYTEREVERSE', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRC_CTRL_BITREVERSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRC_CTRL_BITREVERSE, self).__init__(register,
            'BITREVERSE', 'CRC.CTRL.BITREVERSE', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRC_CTRL_BITSPERWORD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRC_CTRL_BITSPERWORD, self).__init__(register,
            'BITSPERWORD', 'CRC.CTRL.BITSPERWORD', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRC_CTRL_PADCRCINPUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRC_CTRL_PADCRCINPUT, self).__init__(register,
            'PADCRCINPUT', 'CRC.CTRL.PADCRCINPUT', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRC_STATUS_BUSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRC_STATUS_BUSY, self).__init__(register,
            'BUSY', 'CRC.STATUS.BUSY', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRC_CMD_INITIALIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRC_CMD_INITIALIZE, self).__init__(register,
            'INITIALIZE', 'CRC.CMD.INITIALIZE', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRC_INPUTDATA_INPUTDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRC_INPUTDATA_INPUTDATA, self).__init__(register,
            'INPUTDATA', 'CRC.INPUTDATA.INPUTDATA', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRC_INIT_INIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRC_INIT_INIT, self).__init__(register,
            'INIT', 'CRC.INIT.INIT', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRC_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRC_DATA_DATA, self).__init__(register,
            'DATA', 'CRC.DATA.DATA', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRC_POLY_POLY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRC_POLY_POLY, self).__init__(register,
            'POLY', 'CRC.POLY.POLY', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


