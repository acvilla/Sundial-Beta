
from static import Base_RM_Field
from BUFC_enum import *


class RM_Field_BUFC_BUF0_CTRL_SIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_CTRL_SIZE, self).__init__(register,
            'SIZE', 'BUFC.BUF0_CTRL.SIZE', 'read-write',
            "",
            0, 3,
            RM_Enum_BUFC_BUF0_CTRL_SIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_ADDR_ADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_ADDR_ADDR, self).__init__(register,
            'ADDR', 'BUFC.BUF0_ADDR.ADDR', 'read-write',
            "",
            0, 24)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_WRITEOFFSET_WRITEOFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_WRITEOFFSET_WRITEOFFSET, self).__init__(register,
            'WRITEOFFSET', 'BUFC.BUF0_WRITEOFFSET.WRITEOFFSET', 'read-write',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_READOFFSET_READOFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_READOFFSET_READOFFSET, self).__init__(register,
            'READOFFSET', 'BUFC.BUF0_READOFFSET.READOFFSET', 'read-write',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_WRITESTART_WRITESTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_WRITESTART_WRITESTART, self).__init__(register,
            'WRITESTART', 'BUFC.BUF0_WRITESTART.WRITESTART', 'read-only',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_READDATA_READDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_READDATA_READDATA, self).__init__(register,
            'READDATA', 'BUFC.BUF0_READDATA.READDATA', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_WRITEDATA_WRITEDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_WRITEDATA_WRITEDATA, self).__init__(register,
            'WRITEDATA', 'BUFC.BUF0_WRITEDATA.WRITEDATA', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_XWRITE_XORWRITEDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_XWRITE_XORWRITEDATA, self).__init__(register,
            'XORWRITEDATA', 'BUFC.BUF0_XWRITE.XORWRITEDATA', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_STATUS_BYTES(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_STATUS_BYTES, self).__init__(register,
            'BYTES', 'BUFC.BUF0_STATUS.BYTES', 'read-only',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_STATUS_RDATARDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_STATUS_RDATARDY, self).__init__(register,
            'RDATARDY', 'BUFC.BUF0_STATUS.RDATARDY', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_THRESHOLDCTRL_THRESHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_THRESHOLDCTRL_THRESHOLD, self).__init__(register,
            'THRESHOLD', 'BUFC.BUF0_THRESHOLDCTRL.THRESHOLD', 'read-write',
            "",
            0, 12)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_THRESHOLDCTRL_THRESHOLDMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_THRESHOLDCTRL_THRESHOLDMODE, self).__init__(register,
            'THRESHOLDMODE', 'BUFC.BUF0_THRESHOLDCTRL.THRESHOLDMODE', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_CMD_CLEAR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_CMD_CLEAR, self).__init__(register,
            'CLEAR', 'BUFC.BUF0_CMD.CLEAR', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_CMD_PREFETCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_CMD_PREFETCH, self).__init__(register,
            'PREFETCH', 'BUFC.BUF0_CMD.PREFETCH', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_CMD_UPDATEWRITESTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_CMD_UPDATEWRITESTART, self).__init__(register,
            'UPDATEWRITESTART', 'BUFC.BUF0_CMD.UPDATEWRITESTART', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF0_CMD_RESTOREWRITEOFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF0_CMD_RESTOREWRITEOFFSET, self).__init__(register,
            'RESTOREWRITEOFFSET', 'BUFC.BUF0_CMD.RESTOREWRITEOFFSET', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_CTRL_SIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_CTRL_SIZE, self).__init__(register,
            'SIZE', 'BUFC.BUF1_CTRL.SIZE', 'read-write',
            "",
            0, 3,
            RM_Enum_BUFC_BUF1_CTRL_SIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_ADDR_ADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_ADDR_ADDR, self).__init__(register,
            'ADDR', 'BUFC.BUF1_ADDR.ADDR', 'read-write',
            "",
            0, 24)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_WRITEOFFSET_WRITEOFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_WRITEOFFSET_WRITEOFFSET, self).__init__(register,
            'WRITEOFFSET', 'BUFC.BUF1_WRITEOFFSET.WRITEOFFSET', 'read-write',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_READOFFSET_READOFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_READOFFSET_READOFFSET, self).__init__(register,
            'READOFFSET', 'BUFC.BUF1_READOFFSET.READOFFSET', 'read-write',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_WRITESTART_WRITESTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_WRITESTART_WRITESTART, self).__init__(register,
            'WRITESTART', 'BUFC.BUF1_WRITESTART.WRITESTART', 'read-only',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_READDATA_READDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_READDATA_READDATA, self).__init__(register,
            'READDATA', 'BUFC.BUF1_READDATA.READDATA', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_WRITEDATA_WRITEDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_WRITEDATA_WRITEDATA, self).__init__(register,
            'WRITEDATA', 'BUFC.BUF1_WRITEDATA.WRITEDATA', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_XWRITE_XORWRITEDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_XWRITE_XORWRITEDATA, self).__init__(register,
            'XORWRITEDATA', 'BUFC.BUF1_XWRITE.XORWRITEDATA', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_STATUS_BYTES(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_STATUS_BYTES, self).__init__(register,
            'BYTES', 'BUFC.BUF1_STATUS.BYTES', 'read-only',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_STATUS_RDATARDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_STATUS_RDATARDY, self).__init__(register,
            'RDATARDY', 'BUFC.BUF1_STATUS.RDATARDY', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_THRESHOLDCTRL_THRESHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_THRESHOLDCTRL_THRESHOLD, self).__init__(register,
            'THRESHOLD', 'BUFC.BUF1_THRESHOLDCTRL.THRESHOLD', 'read-write',
            "",
            0, 12)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_THRESHOLDCTRL_THRESHOLDMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_THRESHOLDCTRL_THRESHOLDMODE, self).__init__(register,
            'THRESHOLDMODE', 'BUFC.BUF1_THRESHOLDCTRL.THRESHOLDMODE', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_CMD_CLEAR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_CMD_CLEAR, self).__init__(register,
            'CLEAR', 'BUFC.BUF1_CMD.CLEAR', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_CMD_PREFETCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_CMD_PREFETCH, self).__init__(register,
            'PREFETCH', 'BUFC.BUF1_CMD.PREFETCH', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_CMD_UPDATEWRITESTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_CMD_UPDATEWRITESTART, self).__init__(register,
            'UPDATEWRITESTART', 'BUFC.BUF1_CMD.UPDATEWRITESTART', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF1_CMD_RESTOREWRITEOFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF1_CMD_RESTOREWRITEOFFSET, self).__init__(register,
            'RESTOREWRITEOFFSET', 'BUFC.BUF1_CMD.RESTOREWRITEOFFSET', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_CTRL_SIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_CTRL_SIZE, self).__init__(register,
            'SIZE', 'BUFC.BUF2_CTRL.SIZE', 'read-write',
            "",
            0, 3,
            RM_Enum_BUFC_BUF2_CTRL_SIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_ADDR_ADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_ADDR_ADDR, self).__init__(register,
            'ADDR', 'BUFC.BUF2_ADDR.ADDR', 'read-write',
            "",
            0, 24)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_WRITEOFFSET_WRITEOFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_WRITEOFFSET_WRITEOFFSET, self).__init__(register,
            'WRITEOFFSET', 'BUFC.BUF2_WRITEOFFSET.WRITEOFFSET', 'read-write',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_READOFFSET_READOFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_READOFFSET_READOFFSET, self).__init__(register,
            'READOFFSET', 'BUFC.BUF2_READOFFSET.READOFFSET', 'read-write',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_WRITESTART_WRITESTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_WRITESTART_WRITESTART, self).__init__(register,
            'WRITESTART', 'BUFC.BUF2_WRITESTART.WRITESTART', 'read-only',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_READDATA_READDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_READDATA_READDATA, self).__init__(register,
            'READDATA', 'BUFC.BUF2_READDATA.READDATA', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_WRITEDATA_WRITEDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_WRITEDATA_WRITEDATA, self).__init__(register,
            'WRITEDATA', 'BUFC.BUF2_WRITEDATA.WRITEDATA', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_XWRITE_XORWRITEDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_XWRITE_XORWRITEDATA, self).__init__(register,
            'XORWRITEDATA', 'BUFC.BUF2_XWRITE.XORWRITEDATA', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_STATUS_BYTES(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_STATUS_BYTES, self).__init__(register,
            'BYTES', 'BUFC.BUF2_STATUS.BYTES', 'read-only',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_STATUS_RDATARDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_STATUS_RDATARDY, self).__init__(register,
            'RDATARDY', 'BUFC.BUF2_STATUS.RDATARDY', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_THRESHOLDCTRL_THRESHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_THRESHOLDCTRL_THRESHOLD, self).__init__(register,
            'THRESHOLD', 'BUFC.BUF2_THRESHOLDCTRL.THRESHOLD', 'read-write',
            "",
            0, 12)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_THRESHOLDCTRL_THRESHOLDMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_THRESHOLDCTRL_THRESHOLDMODE, self).__init__(register,
            'THRESHOLDMODE', 'BUFC.BUF2_THRESHOLDCTRL.THRESHOLDMODE', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_CMD_CLEAR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_CMD_CLEAR, self).__init__(register,
            'CLEAR', 'BUFC.BUF2_CMD.CLEAR', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_CMD_PREFETCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_CMD_PREFETCH, self).__init__(register,
            'PREFETCH', 'BUFC.BUF2_CMD.PREFETCH', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_CMD_UPDATEWRITESTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_CMD_UPDATEWRITESTART, self).__init__(register,
            'UPDATEWRITESTART', 'BUFC.BUF2_CMD.UPDATEWRITESTART', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF2_CMD_RESTOREWRITEOFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF2_CMD_RESTOREWRITEOFFSET, self).__init__(register,
            'RESTOREWRITEOFFSET', 'BUFC.BUF2_CMD.RESTOREWRITEOFFSET', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_CTRL_SIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_CTRL_SIZE, self).__init__(register,
            'SIZE', 'BUFC.BUF3_CTRL.SIZE', 'read-write',
            "",
            0, 3,
            RM_Enum_BUFC_BUF3_CTRL_SIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_ADDR_ADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_ADDR_ADDR, self).__init__(register,
            'ADDR', 'BUFC.BUF3_ADDR.ADDR', 'read-write',
            "",
            0, 24)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_WRITEOFFSET_WRITEOFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_WRITEOFFSET_WRITEOFFSET, self).__init__(register,
            'WRITEOFFSET', 'BUFC.BUF3_WRITEOFFSET.WRITEOFFSET', 'read-write',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_READOFFSET_READOFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_READOFFSET_READOFFSET, self).__init__(register,
            'READOFFSET', 'BUFC.BUF3_READOFFSET.READOFFSET', 'read-write',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_WRITESTART_WRITESTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_WRITESTART_WRITESTART, self).__init__(register,
            'WRITESTART', 'BUFC.BUF3_WRITESTART.WRITESTART', 'read-only',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_READDATA_READDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_READDATA_READDATA, self).__init__(register,
            'READDATA', 'BUFC.BUF3_READDATA.READDATA', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_WRITEDATA_WRITEDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_WRITEDATA_WRITEDATA, self).__init__(register,
            'WRITEDATA', 'BUFC.BUF3_WRITEDATA.WRITEDATA', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_XWRITE_XORWRITEDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_XWRITE_XORWRITEDATA, self).__init__(register,
            'XORWRITEDATA', 'BUFC.BUF3_XWRITE.XORWRITEDATA', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_STATUS_BYTES(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_STATUS_BYTES, self).__init__(register,
            'BYTES', 'BUFC.BUF3_STATUS.BYTES', 'read-only',
            "",
            0, 13)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_STATUS_RDATARDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_STATUS_RDATARDY, self).__init__(register,
            'RDATARDY', 'BUFC.BUF3_STATUS.RDATARDY', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_THRESHOLDCTRL_THRESHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_THRESHOLDCTRL_THRESHOLD, self).__init__(register,
            'THRESHOLD', 'BUFC.BUF3_THRESHOLDCTRL.THRESHOLD', 'read-write',
            "",
            0, 12)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_THRESHOLDCTRL_THRESHOLDMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_THRESHOLDCTRL_THRESHOLDMODE, self).__init__(register,
            'THRESHOLDMODE', 'BUFC.BUF3_THRESHOLDCTRL.THRESHOLDMODE', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_CMD_CLEAR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_CMD_CLEAR, self).__init__(register,
            'CLEAR', 'BUFC.BUF3_CMD.CLEAR', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_CMD_PREFETCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_CMD_PREFETCH, self).__init__(register,
            'PREFETCH', 'BUFC.BUF3_CMD.PREFETCH', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_CMD_UPDATEWRITESTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_CMD_UPDATEWRITESTART, self).__init__(register,
            'UPDATEWRITESTART', 'BUFC.BUF3_CMD.UPDATEWRITESTART', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_BUF3_CMD_RESTOREWRITEOFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_BUF3_CMD_RESTOREWRITEOFFSET, self).__init__(register,
            'RESTOREWRITEOFFSET', 'BUFC.BUF3_CMD.RESTOREWRITEOFFSET', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF0OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF0OF, self).__init__(register,
            'BUF0OF', 'BUFC.IF.BUF0OF', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF0UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF0UF, self).__init__(register,
            'BUF0UF', 'BUFC.IF.BUF0UF', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF0THR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF0THR, self).__init__(register,
            'BUF0THR', 'BUFC.IF.BUF0THR', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF0CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF0CORR, self).__init__(register,
            'BUF0CORR', 'BUFC.IF.BUF0CORR', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF1OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF1OF, self).__init__(register,
            'BUF1OF', 'BUFC.IF.BUF1OF', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF1UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF1UF, self).__init__(register,
            'BUF1UF', 'BUFC.IF.BUF1UF', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF1THR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF1THR, self).__init__(register,
            'BUF1THR', 'BUFC.IF.BUF1THR', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF1CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF1CORR, self).__init__(register,
            'BUF1CORR', 'BUFC.IF.BUF1CORR', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF2OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF2OF, self).__init__(register,
            'BUF2OF', 'BUFC.IF.BUF2OF', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF2UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF2UF, self).__init__(register,
            'BUF2UF', 'BUFC.IF.BUF2UF', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF2THR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF2THR, self).__init__(register,
            'BUF2THR', 'BUFC.IF.BUF2THR', 'read-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF2CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF2CORR, self).__init__(register,
            'BUF2CORR', 'BUFC.IF.BUF2CORR', 'read-only',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF3OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF3OF, self).__init__(register,
            'BUF3OF', 'BUFC.IF.BUF3OF', 'read-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF3UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF3UF, self).__init__(register,
            'BUF3UF', 'BUFC.IF.BUF3UF', 'read-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF3THR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF3THR, self).__init__(register,
            'BUF3THR', 'BUFC.IF.BUF3THR', 'read-only',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUF3CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUF3CORR, self).__init__(register,
            'BUF3CORR', 'BUFC.IF.BUF3CORR', 'read-only',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IF_BUSERROR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IF_BUSERROR, self).__init__(register,
            'BUSERROR', 'BUFC.IF.BUSERROR', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFS_BUF0OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFS_BUF0OF, self).__init__(register,
            'BUF0OF', 'BUFC.IFS.BUF0OF', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFS_BUF0UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFS_BUF0UF, self).__init__(register,
            'BUF0UF', 'BUFC.IFS.BUF0UF', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFS_BUF0CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFS_BUF0CORR, self).__init__(register,
            'BUF0CORR', 'BUFC.IFS.BUF0CORR', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFS_BUF1OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFS_BUF1OF, self).__init__(register,
            'BUF1OF', 'BUFC.IFS.BUF1OF', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFS_BUF1UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFS_BUF1UF, self).__init__(register,
            'BUF1UF', 'BUFC.IFS.BUF1UF', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFS_BUF1CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFS_BUF1CORR, self).__init__(register,
            'BUF1CORR', 'BUFC.IFS.BUF1CORR', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFS_BUF2OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFS_BUF2OF, self).__init__(register,
            'BUF2OF', 'BUFC.IFS.BUF2OF', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFS_BUF2UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFS_BUF2UF, self).__init__(register,
            'BUF2UF', 'BUFC.IFS.BUF2UF', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFS_BUF2CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFS_BUF2CORR, self).__init__(register,
            'BUF2CORR', 'BUFC.IFS.BUF2CORR', 'write-only',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFS_BUF3OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFS_BUF3OF, self).__init__(register,
            'BUF3OF', 'BUFC.IFS.BUF3OF', 'write-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFS_BUF3UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFS_BUF3UF, self).__init__(register,
            'BUF3UF', 'BUFC.IFS.BUF3UF', 'write-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFS_BUF3CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFS_BUF3CORR, self).__init__(register,
            'BUF3CORR', 'BUFC.IFS.BUF3CORR', 'write-only',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFS_BUSERROR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFS_BUSERROR, self).__init__(register,
            'BUSERROR', 'BUFC.IFS.BUSERROR', 'write-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFC_BUF0OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFC_BUF0OF, self).__init__(register,
            'BUF0OF', 'BUFC.IFC.BUF0OF', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFC_BUF0UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFC_BUF0UF, self).__init__(register,
            'BUF0UF', 'BUFC.IFC.BUF0UF', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFC_BUF0CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFC_BUF0CORR, self).__init__(register,
            'BUF0CORR', 'BUFC.IFC.BUF0CORR', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFC_BUF1OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFC_BUF1OF, self).__init__(register,
            'BUF1OF', 'BUFC.IFC.BUF1OF', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFC_BUF1UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFC_BUF1UF, self).__init__(register,
            'BUF1UF', 'BUFC.IFC.BUF1UF', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFC_BUF1CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFC_BUF1CORR, self).__init__(register,
            'BUF1CORR', 'BUFC.IFC.BUF1CORR', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFC_BUF2OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFC_BUF2OF, self).__init__(register,
            'BUF2OF', 'BUFC.IFC.BUF2OF', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFC_BUF2UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFC_BUF2UF, self).__init__(register,
            'BUF2UF', 'BUFC.IFC.BUF2UF', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFC_BUF2CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFC_BUF2CORR, self).__init__(register,
            'BUF2CORR', 'BUFC.IFC.BUF2CORR', 'write-only',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFC_BUF3OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFC_BUF3OF, self).__init__(register,
            'BUF3OF', 'BUFC.IFC.BUF3OF', 'write-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFC_BUF3UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFC_BUF3UF, self).__init__(register,
            'BUF3UF', 'BUFC.IFC.BUF3UF', 'write-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFC_BUF3CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFC_BUF3CORR, self).__init__(register,
            'BUF3CORR', 'BUFC.IFC.BUF3CORR', 'write-only',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IFC_BUSERROR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IFC_BUSERROR, self).__init__(register,
            'BUSERROR', 'BUFC.IFC.BUSERROR', 'write-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF0OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF0OF, self).__init__(register,
            'BUF0OF', 'BUFC.IEN.BUF0OF', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF0UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF0UF, self).__init__(register,
            'BUF0UF', 'BUFC.IEN.BUF0UF', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF0THR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF0THR, self).__init__(register,
            'BUF0THR', 'BUFC.IEN.BUF0THR', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF0CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF0CORR, self).__init__(register,
            'BUF0CORR', 'BUFC.IEN.BUF0CORR', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF1OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF1OF, self).__init__(register,
            'BUF1OF', 'BUFC.IEN.BUF1OF', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF1UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF1UF, self).__init__(register,
            'BUF1UF', 'BUFC.IEN.BUF1UF', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF1THR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF1THR, self).__init__(register,
            'BUF1THR', 'BUFC.IEN.BUF1THR', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF1CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF1CORR, self).__init__(register,
            'BUF1CORR', 'BUFC.IEN.BUF1CORR', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF2OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF2OF, self).__init__(register,
            'BUF2OF', 'BUFC.IEN.BUF2OF', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF2UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF2UF, self).__init__(register,
            'BUF2UF', 'BUFC.IEN.BUF2UF', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF2THR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF2THR, self).__init__(register,
            'BUF2THR', 'BUFC.IEN.BUF2THR', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF2CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF2CORR, self).__init__(register,
            'BUF2CORR', 'BUFC.IEN.BUF2CORR', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF3OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF3OF, self).__init__(register,
            'BUF3OF', 'BUFC.IEN.BUF3OF', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF3UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF3UF, self).__init__(register,
            'BUF3UF', 'BUFC.IEN.BUF3UF', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF3THR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF3THR, self).__init__(register,
            'BUF3THR', 'BUFC.IEN.BUF3THR', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUF3CORR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUF3CORR, self).__init__(register,
            'BUF3CORR', 'BUFC.IEN.BUF3CORR', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_BUFC_IEN_BUSERROR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_BUFC_IEN_BUSERROR, self).__init__(register,
            'BUSERROR', 'BUFC.IEN.BUSERROR', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


