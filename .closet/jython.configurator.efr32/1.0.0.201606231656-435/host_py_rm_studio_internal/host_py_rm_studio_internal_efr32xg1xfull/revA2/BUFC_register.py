
from static import Base_RM_Register
from BUFC_field import *


class RM_Register_BUFC_BUF0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF0_CTRL, self).__init__(rmio, label,
            0x40081000, 0x000,
            'BUF0_CTRL', 'BUFC.BUF0_CTRL', 'read-write',
            "",
            0x00000000, 0x00000007)

        self.SIZE = RM_Field_BUFC_BUF0_CTRL_SIZE(self)
        self.zz_fdict['SIZE'] = self.SIZE
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF0_ADDR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF0_ADDR, self).__init__(rmio, label,
            0x40081000, 0x004,
            'BUF0_ADDR', 'BUFC.BUF0_ADDR', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.ADDR = RM_Field_BUFC_BUF0_ADDR_ADDR(self)
        self.zz_fdict['ADDR'] = self.ADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF0_WRITEOFFSET(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF0_WRITEOFFSET, self).__init__(rmio, label,
            0x40081000, 0x008,
            'BUF0_WRITEOFFSET', 'BUFC.BUF0_WRITEOFFSET', 'read-write',
            "",
            0x00000000, 0x00001FFF)

        self.WRITEOFFSET = RM_Field_BUFC_BUF0_WRITEOFFSET_WRITEOFFSET(self)
        self.zz_fdict['WRITEOFFSET'] = self.WRITEOFFSET
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF0_READOFFSET(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF0_READOFFSET, self).__init__(rmio, label,
            0x40081000, 0x00C,
            'BUF0_READOFFSET', 'BUFC.BUF0_READOFFSET', 'read-write',
            "",
            0x00000000, 0x00001FFF)

        self.READOFFSET = RM_Field_BUFC_BUF0_READOFFSET_READOFFSET(self)
        self.zz_fdict['READOFFSET'] = self.READOFFSET
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF0_WRITESTART(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF0_WRITESTART, self).__init__(rmio, label,
            0x40081000, 0x010,
            'BUF0_WRITESTART', 'BUFC.BUF0_WRITESTART', 'read-only',
            "",
            0x00000000, 0x00001FFF)

        self.WRITESTART = RM_Field_BUFC_BUF0_WRITESTART_WRITESTART(self)
        self.zz_fdict['WRITESTART'] = self.WRITESTART
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF0_READDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF0_READDATA, self).__init__(rmio, label,
            0x40081000, 0x014,
            'BUF0_READDATA', 'BUFC.BUF0_READDATA', 'read-only',
            "",
            0x00000000, 0x000000FF)

        self.READDATA = RM_Field_BUFC_BUF0_READDATA_READDATA(self)
        self.zz_fdict['READDATA'] = self.READDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF0_WRITEDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF0_WRITEDATA, self).__init__(rmio, label,
            0x40081000, 0x018,
            'BUF0_WRITEDATA', 'BUFC.BUF0_WRITEDATA', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.WRITEDATA = RM_Field_BUFC_BUF0_WRITEDATA_WRITEDATA(self)
        self.zz_fdict['WRITEDATA'] = self.WRITEDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF0_XWRITE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF0_XWRITE, self).__init__(rmio, label,
            0x40081000, 0x01C,
            'BUF0_XWRITE', 'BUFC.BUF0_XWRITE', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.XORWRITEDATA = RM_Field_BUFC_BUF0_XWRITE_XORWRITEDATA(self)
        self.zz_fdict['XORWRITEDATA'] = self.XORWRITEDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF0_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF0_STATUS, self).__init__(rmio, label,
            0x40081000, 0x020,
            'BUF0_STATUS', 'BUFC.BUF0_STATUS', 'read-only',
            "",
            0x00000000, 0x00011FFF)

        self.BYTES = RM_Field_BUFC_BUF0_STATUS_BYTES(self)
        self.zz_fdict['BYTES'] = self.BYTES
        self.RDATARDY = RM_Field_BUFC_BUF0_STATUS_RDATARDY(self)
        self.zz_fdict['RDATARDY'] = self.RDATARDY
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF0_THRESHOLDCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF0_THRESHOLDCTRL, self).__init__(rmio, label,
            0x40081000, 0x024,
            'BUF0_THRESHOLDCTRL', 'BUFC.BUF0_THRESHOLDCTRL', 'read-write',
            "",
            0x00000000, 0x00002FFF)

        self.THRESHOLD = RM_Field_BUFC_BUF0_THRESHOLDCTRL_THRESHOLD(self)
        self.zz_fdict['THRESHOLD'] = self.THRESHOLD
        self.THRESHOLDMODE = RM_Field_BUFC_BUF0_THRESHOLDCTRL_THRESHOLDMODE(self)
        self.zz_fdict['THRESHOLDMODE'] = self.THRESHOLDMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF0_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF0_CMD, self).__init__(rmio, label,
            0x40081000, 0x028,
            'BUF0_CMD', 'BUFC.BUF0_CMD', 'write-only',
            "",
            0x00000000, 0x0000000F)

        self.CLEAR = RM_Field_BUFC_BUF0_CMD_CLEAR(self)
        self.zz_fdict['CLEAR'] = self.CLEAR
        self.PREFETCH = RM_Field_BUFC_BUF0_CMD_PREFETCH(self)
        self.zz_fdict['PREFETCH'] = self.PREFETCH
        self.UPDATEWRITESTART = RM_Field_BUFC_BUF0_CMD_UPDATEWRITESTART(self)
        self.zz_fdict['UPDATEWRITESTART'] = self.UPDATEWRITESTART
        self.RESTOREWRITEOFFSET = RM_Field_BUFC_BUF0_CMD_RESTOREWRITEOFFSET(self)
        self.zz_fdict['RESTOREWRITEOFFSET'] = self.RESTOREWRITEOFFSET
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF1_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF1_CTRL, self).__init__(rmio, label,
            0x40081000, 0x030,
            'BUF1_CTRL', 'BUFC.BUF1_CTRL', 'read-write',
            "",
            0x00000000, 0x00000007)

        self.SIZE = RM_Field_BUFC_BUF1_CTRL_SIZE(self)
        self.zz_fdict['SIZE'] = self.SIZE
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF1_ADDR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF1_ADDR, self).__init__(rmio, label,
            0x40081000, 0x034,
            'BUF1_ADDR', 'BUFC.BUF1_ADDR', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.ADDR = RM_Field_BUFC_BUF1_ADDR_ADDR(self)
        self.zz_fdict['ADDR'] = self.ADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF1_WRITEOFFSET(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF1_WRITEOFFSET, self).__init__(rmio, label,
            0x40081000, 0x038,
            'BUF1_WRITEOFFSET', 'BUFC.BUF1_WRITEOFFSET', 'read-write',
            "",
            0x00000000, 0x00001FFF)

        self.WRITEOFFSET = RM_Field_BUFC_BUF1_WRITEOFFSET_WRITEOFFSET(self)
        self.zz_fdict['WRITEOFFSET'] = self.WRITEOFFSET
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF1_READOFFSET(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF1_READOFFSET, self).__init__(rmio, label,
            0x40081000, 0x03C,
            'BUF1_READOFFSET', 'BUFC.BUF1_READOFFSET', 'read-write',
            "",
            0x00000000, 0x00001FFF)

        self.READOFFSET = RM_Field_BUFC_BUF1_READOFFSET_READOFFSET(self)
        self.zz_fdict['READOFFSET'] = self.READOFFSET
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF1_WRITESTART(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF1_WRITESTART, self).__init__(rmio, label,
            0x40081000, 0x040,
            'BUF1_WRITESTART', 'BUFC.BUF1_WRITESTART', 'read-only',
            "",
            0x00000000, 0x00001FFF)

        self.WRITESTART = RM_Field_BUFC_BUF1_WRITESTART_WRITESTART(self)
        self.zz_fdict['WRITESTART'] = self.WRITESTART
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF1_READDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF1_READDATA, self).__init__(rmio, label,
            0x40081000, 0x044,
            'BUF1_READDATA', 'BUFC.BUF1_READDATA', 'read-only',
            "",
            0x00000000, 0x000000FF)

        self.READDATA = RM_Field_BUFC_BUF1_READDATA_READDATA(self)
        self.zz_fdict['READDATA'] = self.READDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF1_WRITEDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF1_WRITEDATA, self).__init__(rmio, label,
            0x40081000, 0x048,
            'BUF1_WRITEDATA', 'BUFC.BUF1_WRITEDATA', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.WRITEDATA = RM_Field_BUFC_BUF1_WRITEDATA_WRITEDATA(self)
        self.zz_fdict['WRITEDATA'] = self.WRITEDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF1_XWRITE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF1_XWRITE, self).__init__(rmio, label,
            0x40081000, 0x04C,
            'BUF1_XWRITE', 'BUFC.BUF1_XWRITE', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.XORWRITEDATA = RM_Field_BUFC_BUF1_XWRITE_XORWRITEDATA(self)
        self.zz_fdict['XORWRITEDATA'] = self.XORWRITEDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF1_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF1_STATUS, self).__init__(rmio, label,
            0x40081000, 0x050,
            'BUF1_STATUS', 'BUFC.BUF1_STATUS', 'read-only',
            "",
            0x00000000, 0x00011FFF)

        self.BYTES = RM_Field_BUFC_BUF1_STATUS_BYTES(self)
        self.zz_fdict['BYTES'] = self.BYTES
        self.RDATARDY = RM_Field_BUFC_BUF1_STATUS_RDATARDY(self)
        self.zz_fdict['RDATARDY'] = self.RDATARDY
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF1_THRESHOLDCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF1_THRESHOLDCTRL, self).__init__(rmio, label,
            0x40081000, 0x054,
            'BUF1_THRESHOLDCTRL', 'BUFC.BUF1_THRESHOLDCTRL', 'read-write',
            "",
            0x00000000, 0x00002FFF)

        self.THRESHOLD = RM_Field_BUFC_BUF1_THRESHOLDCTRL_THRESHOLD(self)
        self.zz_fdict['THRESHOLD'] = self.THRESHOLD
        self.THRESHOLDMODE = RM_Field_BUFC_BUF1_THRESHOLDCTRL_THRESHOLDMODE(self)
        self.zz_fdict['THRESHOLDMODE'] = self.THRESHOLDMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF1_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF1_CMD, self).__init__(rmio, label,
            0x40081000, 0x058,
            'BUF1_CMD', 'BUFC.BUF1_CMD', 'write-only',
            "",
            0x00000000, 0x0000000F)

        self.CLEAR = RM_Field_BUFC_BUF1_CMD_CLEAR(self)
        self.zz_fdict['CLEAR'] = self.CLEAR
        self.PREFETCH = RM_Field_BUFC_BUF1_CMD_PREFETCH(self)
        self.zz_fdict['PREFETCH'] = self.PREFETCH
        self.UPDATEWRITESTART = RM_Field_BUFC_BUF1_CMD_UPDATEWRITESTART(self)
        self.zz_fdict['UPDATEWRITESTART'] = self.UPDATEWRITESTART
        self.RESTOREWRITEOFFSET = RM_Field_BUFC_BUF1_CMD_RESTOREWRITEOFFSET(self)
        self.zz_fdict['RESTOREWRITEOFFSET'] = self.RESTOREWRITEOFFSET
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF2_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF2_CTRL, self).__init__(rmio, label,
            0x40081000, 0x060,
            'BUF2_CTRL', 'BUFC.BUF2_CTRL', 'read-write',
            "",
            0x00000000, 0x00000007)

        self.SIZE = RM_Field_BUFC_BUF2_CTRL_SIZE(self)
        self.zz_fdict['SIZE'] = self.SIZE
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF2_ADDR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF2_ADDR, self).__init__(rmio, label,
            0x40081000, 0x064,
            'BUF2_ADDR', 'BUFC.BUF2_ADDR', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.ADDR = RM_Field_BUFC_BUF2_ADDR_ADDR(self)
        self.zz_fdict['ADDR'] = self.ADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF2_WRITEOFFSET(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF2_WRITEOFFSET, self).__init__(rmio, label,
            0x40081000, 0x068,
            'BUF2_WRITEOFFSET', 'BUFC.BUF2_WRITEOFFSET', 'read-write',
            "",
            0x00000000, 0x00001FFF)

        self.WRITEOFFSET = RM_Field_BUFC_BUF2_WRITEOFFSET_WRITEOFFSET(self)
        self.zz_fdict['WRITEOFFSET'] = self.WRITEOFFSET
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF2_READOFFSET(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF2_READOFFSET, self).__init__(rmio, label,
            0x40081000, 0x06C,
            'BUF2_READOFFSET', 'BUFC.BUF2_READOFFSET', 'read-write',
            "",
            0x00000000, 0x00001FFF)

        self.READOFFSET = RM_Field_BUFC_BUF2_READOFFSET_READOFFSET(self)
        self.zz_fdict['READOFFSET'] = self.READOFFSET
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF2_WRITESTART(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF2_WRITESTART, self).__init__(rmio, label,
            0x40081000, 0x070,
            'BUF2_WRITESTART', 'BUFC.BUF2_WRITESTART', 'read-only',
            "",
            0x00000000, 0x00001FFF)

        self.WRITESTART = RM_Field_BUFC_BUF2_WRITESTART_WRITESTART(self)
        self.zz_fdict['WRITESTART'] = self.WRITESTART
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF2_READDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF2_READDATA, self).__init__(rmio, label,
            0x40081000, 0x074,
            'BUF2_READDATA', 'BUFC.BUF2_READDATA', 'read-only',
            "",
            0x00000000, 0x000000FF)

        self.READDATA = RM_Field_BUFC_BUF2_READDATA_READDATA(self)
        self.zz_fdict['READDATA'] = self.READDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF2_WRITEDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF2_WRITEDATA, self).__init__(rmio, label,
            0x40081000, 0x078,
            'BUF2_WRITEDATA', 'BUFC.BUF2_WRITEDATA', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.WRITEDATA = RM_Field_BUFC_BUF2_WRITEDATA_WRITEDATA(self)
        self.zz_fdict['WRITEDATA'] = self.WRITEDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF2_XWRITE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF2_XWRITE, self).__init__(rmio, label,
            0x40081000, 0x07C,
            'BUF2_XWRITE', 'BUFC.BUF2_XWRITE', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.XORWRITEDATA = RM_Field_BUFC_BUF2_XWRITE_XORWRITEDATA(self)
        self.zz_fdict['XORWRITEDATA'] = self.XORWRITEDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF2_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF2_STATUS, self).__init__(rmio, label,
            0x40081000, 0x080,
            'BUF2_STATUS', 'BUFC.BUF2_STATUS', 'read-only',
            "",
            0x00000000, 0x00011FFF)

        self.BYTES = RM_Field_BUFC_BUF2_STATUS_BYTES(self)
        self.zz_fdict['BYTES'] = self.BYTES
        self.RDATARDY = RM_Field_BUFC_BUF2_STATUS_RDATARDY(self)
        self.zz_fdict['RDATARDY'] = self.RDATARDY
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF2_THRESHOLDCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF2_THRESHOLDCTRL, self).__init__(rmio, label,
            0x40081000, 0x084,
            'BUF2_THRESHOLDCTRL', 'BUFC.BUF2_THRESHOLDCTRL', 'read-write',
            "",
            0x00000000, 0x00002FFF)

        self.THRESHOLD = RM_Field_BUFC_BUF2_THRESHOLDCTRL_THRESHOLD(self)
        self.zz_fdict['THRESHOLD'] = self.THRESHOLD
        self.THRESHOLDMODE = RM_Field_BUFC_BUF2_THRESHOLDCTRL_THRESHOLDMODE(self)
        self.zz_fdict['THRESHOLDMODE'] = self.THRESHOLDMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF2_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF2_CMD, self).__init__(rmio, label,
            0x40081000, 0x088,
            'BUF2_CMD', 'BUFC.BUF2_CMD', 'write-only',
            "",
            0x00000000, 0x0000000F)

        self.CLEAR = RM_Field_BUFC_BUF2_CMD_CLEAR(self)
        self.zz_fdict['CLEAR'] = self.CLEAR
        self.PREFETCH = RM_Field_BUFC_BUF2_CMD_PREFETCH(self)
        self.zz_fdict['PREFETCH'] = self.PREFETCH
        self.UPDATEWRITESTART = RM_Field_BUFC_BUF2_CMD_UPDATEWRITESTART(self)
        self.zz_fdict['UPDATEWRITESTART'] = self.UPDATEWRITESTART
        self.RESTOREWRITEOFFSET = RM_Field_BUFC_BUF2_CMD_RESTOREWRITEOFFSET(self)
        self.zz_fdict['RESTOREWRITEOFFSET'] = self.RESTOREWRITEOFFSET
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF3_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF3_CTRL, self).__init__(rmio, label,
            0x40081000, 0x090,
            'BUF3_CTRL', 'BUFC.BUF3_CTRL', 'read-write',
            "",
            0x00000000, 0x00000007)

        self.SIZE = RM_Field_BUFC_BUF3_CTRL_SIZE(self)
        self.zz_fdict['SIZE'] = self.SIZE
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF3_ADDR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF3_ADDR, self).__init__(rmio, label,
            0x40081000, 0x094,
            'BUF3_ADDR', 'BUFC.BUF3_ADDR', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.ADDR = RM_Field_BUFC_BUF3_ADDR_ADDR(self)
        self.zz_fdict['ADDR'] = self.ADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF3_WRITEOFFSET(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF3_WRITEOFFSET, self).__init__(rmio, label,
            0x40081000, 0x098,
            'BUF3_WRITEOFFSET', 'BUFC.BUF3_WRITEOFFSET', 'read-write',
            "",
            0x00000000, 0x00001FFF)

        self.WRITEOFFSET = RM_Field_BUFC_BUF3_WRITEOFFSET_WRITEOFFSET(self)
        self.zz_fdict['WRITEOFFSET'] = self.WRITEOFFSET
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF3_READOFFSET(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF3_READOFFSET, self).__init__(rmio, label,
            0x40081000, 0x09C,
            'BUF3_READOFFSET', 'BUFC.BUF3_READOFFSET', 'read-write',
            "",
            0x00000000, 0x00001FFF)

        self.READOFFSET = RM_Field_BUFC_BUF3_READOFFSET_READOFFSET(self)
        self.zz_fdict['READOFFSET'] = self.READOFFSET
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF3_WRITESTART(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF3_WRITESTART, self).__init__(rmio, label,
            0x40081000, 0x0A0,
            'BUF3_WRITESTART', 'BUFC.BUF3_WRITESTART', 'read-only',
            "",
            0x00000000, 0x00001FFF)

        self.WRITESTART = RM_Field_BUFC_BUF3_WRITESTART_WRITESTART(self)
        self.zz_fdict['WRITESTART'] = self.WRITESTART
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF3_READDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF3_READDATA, self).__init__(rmio, label,
            0x40081000, 0x0A4,
            'BUF3_READDATA', 'BUFC.BUF3_READDATA', 'read-only',
            "",
            0x00000000, 0x000000FF)

        self.READDATA = RM_Field_BUFC_BUF3_READDATA_READDATA(self)
        self.zz_fdict['READDATA'] = self.READDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF3_WRITEDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF3_WRITEDATA, self).__init__(rmio, label,
            0x40081000, 0x0A8,
            'BUF3_WRITEDATA', 'BUFC.BUF3_WRITEDATA', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.WRITEDATA = RM_Field_BUFC_BUF3_WRITEDATA_WRITEDATA(self)
        self.zz_fdict['WRITEDATA'] = self.WRITEDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF3_XWRITE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF3_XWRITE, self).__init__(rmio, label,
            0x40081000, 0x0AC,
            'BUF3_XWRITE', 'BUFC.BUF3_XWRITE', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.XORWRITEDATA = RM_Field_BUFC_BUF3_XWRITE_XORWRITEDATA(self)
        self.zz_fdict['XORWRITEDATA'] = self.XORWRITEDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF3_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF3_STATUS, self).__init__(rmio, label,
            0x40081000, 0x0B0,
            'BUF3_STATUS', 'BUFC.BUF3_STATUS', 'read-only',
            "",
            0x00000000, 0x00011FFF)

        self.BYTES = RM_Field_BUFC_BUF3_STATUS_BYTES(self)
        self.zz_fdict['BYTES'] = self.BYTES
        self.RDATARDY = RM_Field_BUFC_BUF3_STATUS_RDATARDY(self)
        self.zz_fdict['RDATARDY'] = self.RDATARDY
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF3_THRESHOLDCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF3_THRESHOLDCTRL, self).__init__(rmio, label,
            0x40081000, 0x0B4,
            'BUF3_THRESHOLDCTRL', 'BUFC.BUF3_THRESHOLDCTRL', 'read-write',
            "",
            0x00000000, 0x00002FFF)

        self.THRESHOLD = RM_Field_BUFC_BUF3_THRESHOLDCTRL_THRESHOLD(self)
        self.zz_fdict['THRESHOLD'] = self.THRESHOLD
        self.THRESHOLDMODE = RM_Field_BUFC_BUF3_THRESHOLDCTRL_THRESHOLDMODE(self)
        self.zz_fdict['THRESHOLDMODE'] = self.THRESHOLDMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_BUF3_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_BUF3_CMD, self).__init__(rmio, label,
            0x40081000, 0x0B8,
            'BUF3_CMD', 'BUFC.BUF3_CMD', 'write-only',
            "",
            0x00000000, 0x0000000F)

        self.CLEAR = RM_Field_BUFC_BUF3_CMD_CLEAR(self)
        self.zz_fdict['CLEAR'] = self.CLEAR
        self.PREFETCH = RM_Field_BUFC_BUF3_CMD_PREFETCH(self)
        self.zz_fdict['PREFETCH'] = self.PREFETCH
        self.UPDATEWRITESTART = RM_Field_BUFC_BUF3_CMD_UPDATEWRITESTART(self)
        self.zz_fdict['UPDATEWRITESTART'] = self.UPDATEWRITESTART
        self.RESTOREWRITEOFFSET = RM_Field_BUFC_BUF3_CMD_RESTOREWRITEOFFSET(self)
        self.zz_fdict['RESTOREWRITEOFFSET'] = self.RESTOREWRITEOFFSET
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_IF, self).__init__(rmio, label,
            0x40081000, 0x0E0,
            'IF', 'BUFC.IF', 'read-only',
            "",
            0x00000000, 0x8F0F0F0F)

        self.BUF0OF = RM_Field_BUFC_IF_BUF0OF(self)
        self.zz_fdict['BUF0OF'] = self.BUF0OF
        self.BUF0UF = RM_Field_BUFC_IF_BUF0UF(self)
        self.zz_fdict['BUF0UF'] = self.BUF0UF
        self.BUF0THR = RM_Field_BUFC_IF_BUF0THR(self)
        self.zz_fdict['BUF0THR'] = self.BUF0THR
        self.BUF0CORR = RM_Field_BUFC_IF_BUF0CORR(self)
        self.zz_fdict['BUF0CORR'] = self.BUF0CORR
        self.BUF1OF = RM_Field_BUFC_IF_BUF1OF(self)
        self.zz_fdict['BUF1OF'] = self.BUF1OF
        self.BUF1UF = RM_Field_BUFC_IF_BUF1UF(self)
        self.zz_fdict['BUF1UF'] = self.BUF1UF
        self.BUF1THR = RM_Field_BUFC_IF_BUF1THR(self)
        self.zz_fdict['BUF1THR'] = self.BUF1THR
        self.BUF1CORR = RM_Field_BUFC_IF_BUF1CORR(self)
        self.zz_fdict['BUF1CORR'] = self.BUF1CORR
        self.BUF2OF = RM_Field_BUFC_IF_BUF2OF(self)
        self.zz_fdict['BUF2OF'] = self.BUF2OF
        self.BUF2UF = RM_Field_BUFC_IF_BUF2UF(self)
        self.zz_fdict['BUF2UF'] = self.BUF2UF
        self.BUF2THR = RM_Field_BUFC_IF_BUF2THR(self)
        self.zz_fdict['BUF2THR'] = self.BUF2THR
        self.BUF2CORR = RM_Field_BUFC_IF_BUF2CORR(self)
        self.zz_fdict['BUF2CORR'] = self.BUF2CORR
        self.BUF3OF = RM_Field_BUFC_IF_BUF3OF(self)
        self.zz_fdict['BUF3OF'] = self.BUF3OF
        self.BUF3UF = RM_Field_BUFC_IF_BUF3UF(self)
        self.zz_fdict['BUF3UF'] = self.BUF3UF
        self.BUF3THR = RM_Field_BUFC_IF_BUF3THR(self)
        self.zz_fdict['BUF3THR'] = self.BUF3THR
        self.BUF3CORR = RM_Field_BUFC_IF_BUF3CORR(self)
        self.zz_fdict['BUF3CORR'] = self.BUF3CORR
        self.BUSERROR = RM_Field_BUFC_IF_BUSERROR(self)
        self.zz_fdict['BUSERROR'] = self.BUSERROR
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_IFS, self).__init__(rmio, label,
            0x40081000, 0x0E4,
            'IFS', 'BUFC.IFS', 'write-only',
            "",
            0x00000000, 0x8B0B0B0B)

        self.BUF0OF = RM_Field_BUFC_IFS_BUF0OF(self)
        self.zz_fdict['BUF0OF'] = self.BUF0OF
        self.BUF0UF = RM_Field_BUFC_IFS_BUF0UF(self)
        self.zz_fdict['BUF0UF'] = self.BUF0UF
        self.BUF0CORR = RM_Field_BUFC_IFS_BUF0CORR(self)
        self.zz_fdict['BUF0CORR'] = self.BUF0CORR
        self.BUF1OF = RM_Field_BUFC_IFS_BUF1OF(self)
        self.zz_fdict['BUF1OF'] = self.BUF1OF
        self.BUF1UF = RM_Field_BUFC_IFS_BUF1UF(self)
        self.zz_fdict['BUF1UF'] = self.BUF1UF
        self.BUF1CORR = RM_Field_BUFC_IFS_BUF1CORR(self)
        self.zz_fdict['BUF1CORR'] = self.BUF1CORR
        self.BUF2OF = RM_Field_BUFC_IFS_BUF2OF(self)
        self.zz_fdict['BUF2OF'] = self.BUF2OF
        self.BUF2UF = RM_Field_BUFC_IFS_BUF2UF(self)
        self.zz_fdict['BUF2UF'] = self.BUF2UF
        self.BUF2CORR = RM_Field_BUFC_IFS_BUF2CORR(self)
        self.zz_fdict['BUF2CORR'] = self.BUF2CORR
        self.BUF3OF = RM_Field_BUFC_IFS_BUF3OF(self)
        self.zz_fdict['BUF3OF'] = self.BUF3OF
        self.BUF3UF = RM_Field_BUFC_IFS_BUF3UF(self)
        self.zz_fdict['BUF3UF'] = self.BUF3UF
        self.BUF3CORR = RM_Field_BUFC_IFS_BUF3CORR(self)
        self.zz_fdict['BUF3CORR'] = self.BUF3CORR
        self.BUSERROR = RM_Field_BUFC_IFS_BUSERROR(self)
        self.zz_fdict['BUSERROR'] = self.BUSERROR
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_IFC, self).__init__(rmio, label,
            0x40081000, 0x0E8,
            'IFC', 'BUFC.IFC', 'write-only',
            "",
            0x00000000, 0x8B0B0B0B)

        self.BUF0OF = RM_Field_BUFC_IFC_BUF0OF(self)
        self.zz_fdict['BUF0OF'] = self.BUF0OF
        self.BUF0UF = RM_Field_BUFC_IFC_BUF0UF(self)
        self.zz_fdict['BUF0UF'] = self.BUF0UF
        self.BUF0CORR = RM_Field_BUFC_IFC_BUF0CORR(self)
        self.zz_fdict['BUF0CORR'] = self.BUF0CORR
        self.BUF1OF = RM_Field_BUFC_IFC_BUF1OF(self)
        self.zz_fdict['BUF1OF'] = self.BUF1OF
        self.BUF1UF = RM_Field_BUFC_IFC_BUF1UF(self)
        self.zz_fdict['BUF1UF'] = self.BUF1UF
        self.BUF1CORR = RM_Field_BUFC_IFC_BUF1CORR(self)
        self.zz_fdict['BUF1CORR'] = self.BUF1CORR
        self.BUF2OF = RM_Field_BUFC_IFC_BUF2OF(self)
        self.zz_fdict['BUF2OF'] = self.BUF2OF
        self.BUF2UF = RM_Field_BUFC_IFC_BUF2UF(self)
        self.zz_fdict['BUF2UF'] = self.BUF2UF
        self.BUF2CORR = RM_Field_BUFC_IFC_BUF2CORR(self)
        self.zz_fdict['BUF2CORR'] = self.BUF2CORR
        self.BUF3OF = RM_Field_BUFC_IFC_BUF3OF(self)
        self.zz_fdict['BUF3OF'] = self.BUF3OF
        self.BUF3UF = RM_Field_BUFC_IFC_BUF3UF(self)
        self.zz_fdict['BUF3UF'] = self.BUF3UF
        self.BUF3CORR = RM_Field_BUFC_IFC_BUF3CORR(self)
        self.zz_fdict['BUF3CORR'] = self.BUF3CORR
        self.BUSERROR = RM_Field_BUFC_IFC_BUSERROR(self)
        self.zz_fdict['BUSERROR'] = self.BUSERROR
        self.__dict__['zz_frozen'] = True


class RM_Register_BUFC_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_BUFC_IEN, self).__init__(rmio, label,
            0x40081000, 0x0EC,
            'IEN', 'BUFC.IEN', 'read-write',
            "",
            0x00000000, 0x8F0F0F0F)

        self.BUF0OF = RM_Field_BUFC_IEN_BUF0OF(self)
        self.zz_fdict['BUF0OF'] = self.BUF0OF
        self.BUF0UF = RM_Field_BUFC_IEN_BUF0UF(self)
        self.zz_fdict['BUF0UF'] = self.BUF0UF
        self.BUF0THR = RM_Field_BUFC_IEN_BUF0THR(self)
        self.zz_fdict['BUF0THR'] = self.BUF0THR
        self.BUF0CORR = RM_Field_BUFC_IEN_BUF0CORR(self)
        self.zz_fdict['BUF0CORR'] = self.BUF0CORR
        self.BUF1OF = RM_Field_BUFC_IEN_BUF1OF(self)
        self.zz_fdict['BUF1OF'] = self.BUF1OF
        self.BUF1UF = RM_Field_BUFC_IEN_BUF1UF(self)
        self.zz_fdict['BUF1UF'] = self.BUF1UF
        self.BUF1THR = RM_Field_BUFC_IEN_BUF1THR(self)
        self.zz_fdict['BUF1THR'] = self.BUF1THR
        self.BUF1CORR = RM_Field_BUFC_IEN_BUF1CORR(self)
        self.zz_fdict['BUF1CORR'] = self.BUF1CORR
        self.BUF2OF = RM_Field_BUFC_IEN_BUF2OF(self)
        self.zz_fdict['BUF2OF'] = self.BUF2OF
        self.BUF2UF = RM_Field_BUFC_IEN_BUF2UF(self)
        self.zz_fdict['BUF2UF'] = self.BUF2UF
        self.BUF2THR = RM_Field_BUFC_IEN_BUF2THR(self)
        self.zz_fdict['BUF2THR'] = self.BUF2THR
        self.BUF2CORR = RM_Field_BUFC_IEN_BUF2CORR(self)
        self.zz_fdict['BUF2CORR'] = self.BUF2CORR
        self.BUF3OF = RM_Field_BUFC_IEN_BUF3OF(self)
        self.zz_fdict['BUF3OF'] = self.BUF3OF
        self.BUF3UF = RM_Field_BUFC_IEN_BUF3UF(self)
        self.zz_fdict['BUF3UF'] = self.BUF3UF
        self.BUF3THR = RM_Field_BUFC_IEN_BUF3THR(self)
        self.zz_fdict['BUF3THR'] = self.BUF3THR
        self.BUF3CORR = RM_Field_BUFC_IEN_BUF3CORR(self)
        self.zz_fdict['BUF3CORR'] = self.BUF3CORR
        self.BUSERROR = RM_Field_BUFC_IEN_BUSERROR(self)
        self.zz_fdict['BUSERROR'] = self.BUSERROR
        self.__dict__['zz_frozen'] = True


