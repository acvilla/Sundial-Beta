
from static import Base_RM_Field
from GPCRC_enum import *


class RM_Field_GPCRC_CTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_CTRL_EN, self).__init__(register,
            'EN', 'GPCRC.CTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_CTRL_PTECRCEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_CTRL_PTECRCEN, self).__init__(register,
            'PTECRCEN', 'GPCRC.CTRL.PTECRCEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_CTRL_POLYSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_CTRL_POLYSEL, self).__init__(register,
            'POLYSEL', 'GPCRC.CTRL.POLYSEL', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_CTRL_BYTEMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_CTRL_BYTEMODE, self).__init__(register,
            'BYTEMODE', 'GPCRC.CTRL.BYTEMODE', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_CTRL_BITREVERSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_CTRL_BITREVERSE, self).__init__(register,
            'BITREVERSE', 'GPCRC.CTRL.BITREVERSE', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_CTRL_BYTEREVERSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_CTRL_BYTEREVERSE, self).__init__(register,
            'BYTEREVERSE', 'GPCRC.CTRL.BYTEREVERSE', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_CTRL_AUTOINIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_CTRL_AUTOINIT, self).__init__(register,
            'AUTOINIT', 'GPCRC.CTRL.AUTOINIT', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_CMD_INIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_CMD_INIT, self).__init__(register,
            'INIT', 'GPCRC.CMD.INIT', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_INIT_INIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_INIT_INIT, self).__init__(register,
            'INIT', 'GPCRC.INIT.INIT', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_POLY_POLY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_POLY_POLY, self).__init__(register,
            'POLY', 'GPCRC.POLY.POLY', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_INPUTDATA_INPUTDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_INPUTDATA_INPUTDATA, self).__init__(register,
            'INPUTDATA', 'GPCRC.INPUTDATA.INPUTDATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_INPUTDATAHWORD_INPUTDATAHWORD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_INPUTDATAHWORD_INPUTDATAHWORD, self).__init__(register,
            'INPUTDATAHWORD', 'GPCRC.INPUTDATAHWORD.INPUTDATAHWORD', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_INPUTDATABYTE_INPUTDATABYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_INPUTDATABYTE_INPUTDATABYTE, self).__init__(register,
            'INPUTDATABYTE', 'GPCRC.INPUTDATABYTE.INPUTDATABYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_DATA_DATA, self).__init__(register,
            'DATA', 'GPCRC.DATA.DATA', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_DATAREV_DATAREV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_DATAREV_DATAREV, self).__init__(register,
            'DATAREV', 'GPCRC.DATAREV.DATAREV', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_DATABYTEREV_DATABYTEREV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_DATABYTEREV_DATABYTEREV, self).__init__(register,
            'DATABYTEREV', 'GPCRC.DATABYTEREV.DATABYTEREV', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_SNOOP0_CTRL_SNOOPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_SNOOP0_CTRL_SNOOPEN, self).__init__(register,
            'SNOOPEN', 'GPCRC.SNOOP0_CTRL.SNOOPEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_SNOOP0_CTRL_SNOOPRWB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_SNOOP0_CTRL_SNOOPRWB, self).__init__(register,
            'SNOOPRWB', 'GPCRC.SNOOP0_CTRL.SNOOPRWB', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_SNOOP0_CTRL_SNOOPSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_SNOOP0_CTRL_SNOOPSIZE, self).__init__(register,
            'SNOOPSIZE', 'GPCRC.SNOOP0_CTRL.SNOOPSIZE', 'read-write',
            "",
            2, 2,
            RM_Enum_GPCRC_SNOOP0_CTRL_SNOOPSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_SNOOP0_ADDR_SNOOPADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_SNOOP0_ADDR_SNOOPADDR, self).__init__(register,
            'SNOOPADDR', 'GPCRC.SNOOP0_ADDR.SNOOPADDR', 'read-write',
            "",
            2, 19)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_SNOOP1_CTRL_SNOOPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_SNOOP1_CTRL_SNOOPEN, self).__init__(register,
            'SNOOPEN', 'GPCRC.SNOOP1_CTRL.SNOOPEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_SNOOP1_CTRL_SNOOPRWB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_SNOOP1_CTRL_SNOOPRWB, self).__init__(register,
            'SNOOPRWB', 'GPCRC.SNOOP1_CTRL.SNOOPRWB', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_SNOOP1_CTRL_SNOOPSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_SNOOP1_CTRL_SNOOPSIZE, self).__init__(register,
            'SNOOPSIZE', 'GPCRC.SNOOP1_CTRL.SNOOPSIZE', 'read-write',
            "",
            2, 2,
            RM_Enum_GPCRC_SNOOP1_CTRL_SNOOPSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_SNOOP1_ADDR_SNOOPADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_SNOOP1_ADDR_SNOOPADDR, self).__init__(register,
            'SNOOPADDR', 'GPCRC.SNOOP1_ADDR.SNOOPADDR', 'read-write',
            "",
            2, 19)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_SNOOP2_CTRL_SNOOPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_SNOOP2_CTRL_SNOOPEN, self).__init__(register,
            'SNOOPEN', 'GPCRC.SNOOP2_CTRL.SNOOPEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_SNOOP2_CTRL_SNOOPRWB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_SNOOP2_CTRL_SNOOPRWB, self).__init__(register,
            'SNOOPRWB', 'GPCRC.SNOOP2_CTRL.SNOOPRWB', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_SNOOP2_CTRL_SNOOPSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_SNOOP2_CTRL_SNOOPSIZE, self).__init__(register,
            'SNOOPSIZE', 'GPCRC.SNOOP2_CTRL.SNOOPSIZE', 'read-write',
            "",
            2, 2,
            RM_Enum_GPCRC_SNOOP2_CTRL_SNOOPSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPCRC_SNOOP2_ADDR_SNOOPADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPCRC_SNOOP2_ADDR_SNOOPADDR, self).__init__(register,
            'SNOOPADDR', 'GPCRC.SNOOP2_ADDR.SNOOPADDR', 'read-write',
            "",
            2, 19)
        self.__dict__['zz_frozen'] = True


