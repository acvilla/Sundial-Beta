
from static import Base_RM_Register
from GPCRC_field import *


class RM_Register_GPCRC_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_CTRL, self).__init__(rmio, label,
            0x4001c000, 0x000,
            'CTRL', 'GPCRC.CTRL', 'read-write',
            "",
            0x00000000, 0x00002713)

        self.EN = RM_Field_GPCRC_CTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.PTECRCEN = RM_Field_GPCRC_CTRL_PTECRCEN(self)
        self.zz_fdict['PTECRCEN'] = self.PTECRCEN
        self.POLYSEL = RM_Field_GPCRC_CTRL_POLYSEL(self)
        self.zz_fdict['POLYSEL'] = self.POLYSEL
        self.BYTEMODE = RM_Field_GPCRC_CTRL_BYTEMODE(self)
        self.zz_fdict['BYTEMODE'] = self.BYTEMODE
        self.BITREVERSE = RM_Field_GPCRC_CTRL_BITREVERSE(self)
        self.zz_fdict['BITREVERSE'] = self.BITREVERSE
        self.BYTEREVERSE = RM_Field_GPCRC_CTRL_BYTEREVERSE(self)
        self.zz_fdict['BYTEREVERSE'] = self.BYTEREVERSE
        self.AUTOINIT = RM_Field_GPCRC_CTRL_AUTOINIT(self)
        self.zz_fdict['AUTOINIT'] = self.AUTOINIT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_CMD, self).__init__(rmio, label,
            0x4001c000, 0x004,
            'CMD', 'GPCRC.CMD', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.INIT = RM_Field_GPCRC_CMD_INIT(self)
        self.zz_fdict['INIT'] = self.INIT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_INIT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_INIT, self).__init__(rmio, label,
            0x4001c000, 0x008,
            'INIT', 'GPCRC.INIT', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.INIT = RM_Field_GPCRC_INIT_INIT(self)
        self.zz_fdict['INIT'] = self.INIT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_POLY(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_POLY, self).__init__(rmio, label,
            0x4001c000, 0x00C,
            'POLY', 'GPCRC.POLY', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.POLY = RM_Field_GPCRC_POLY_POLY(self)
        self.zz_fdict['POLY'] = self.POLY
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_INPUTDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_INPUTDATA, self).__init__(rmio, label,
            0x4001c000, 0x010,
            'INPUTDATA', 'GPCRC.INPUTDATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.INPUTDATA = RM_Field_GPCRC_INPUTDATA_INPUTDATA(self)
        self.zz_fdict['INPUTDATA'] = self.INPUTDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_INPUTDATAHWORD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_INPUTDATAHWORD, self).__init__(rmio, label,
            0x4001c000, 0x014,
            'INPUTDATAHWORD', 'GPCRC.INPUTDATAHWORD', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.INPUTDATAHWORD = RM_Field_GPCRC_INPUTDATAHWORD_INPUTDATAHWORD(self)
        self.zz_fdict['INPUTDATAHWORD'] = self.INPUTDATAHWORD
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_INPUTDATABYTE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_INPUTDATABYTE, self).__init__(rmio, label,
            0x4001c000, 0x018,
            'INPUTDATABYTE', 'GPCRC.INPUTDATABYTE', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.INPUTDATABYTE = RM_Field_GPCRC_INPUTDATABYTE_INPUTDATABYTE(self)
        self.zz_fdict['INPUTDATABYTE'] = self.INPUTDATABYTE
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_DATA, self).__init__(rmio, label,
            0x4001c000, 0x01C,
            'DATA', 'GPCRC.DATA', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_GPCRC_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_DATAREV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_DATAREV, self).__init__(rmio, label,
            0x4001c000, 0x020,
            'DATAREV', 'GPCRC.DATAREV', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATAREV = RM_Field_GPCRC_DATAREV_DATAREV(self)
        self.zz_fdict['DATAREV'] = self.DATAREV
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_DATABYTEREV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_DATABYTEREV, self).__init__(rmio, label,
            0x4001c000, 0x024,
            'DATABYTEREV', 'GPCRC.DATABYTEREV', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATABYTEREV = RM_Field_GPCRC_DATABYTEREV_DATABYTEREV(self)
        self.zz_fdict['DATABYTEREV'] = self.DATABYTEREV
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_SNOOP0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_SNOOP0_CTRL, self).__init__(rmio, label,
            0x4001c000, 0x028,
            'SNOOP0_CTRL', 'GPCRC.SNOOP0_CTRL', 'read-write',
            "",
            0x00000000, 0x0000000F)

        self.SNOOPEN = RM_Field_GPCRC_SNOOP0_CTRL_SNOOPEN(self)
        self.zz_fdict['SNOOPEN'] = self.SNOOPEN
        self.SNOOPRWB = RM_Field_GPCRC_SNOOP0_CTRL_SNOOPRWB(self)
        self.zz_fdict['SNOOPRWB'] = self.SNOOPRWB
        self.SNOOPSIZE = RM_Field_GPCRC_SNOOP0_CTRL_SNOOPSIZE(self)
        self.zz_fdict['SNOOPSIZE'] = self.SNOOPSIZE
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_SNOOP0_ADDR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_SNOOP0_ADDR, self).__init__(rmio, label,
            0x4001c000, 0x02C,
            'SNOOP0_ADDR', 'GPCRC.SNOOP0_ADDR', 'read-write',
            "",
            0x40000000, 0x001FFFFC)

        self.SNOOPADDR = RM_Field_GPCRC_SNOOP0_ADDR_SNOOPADDR(self)
        self.zz_fdict['SNOOPADDR'] = self.SNOOPADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_SNOOP1_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_SNOOP1_CTRL, self).__init__(rmio, label,
            0x4001c000, 0x030,
            'SNOOP1_CTRL', 'GPCRC.SNOOP1_CTRL', 'read-write',
            "",
            0x00000000, 0x0000000F)

        self.SNOOPEN = RM_Field_GPCRC_SNOOP1_CTRL_SNOOPEN(self)
        self.zz_fdict['SNOOPEN'] = self.SNOOPEN
        self.SNOOPRWB = RM_Field_GPCRC_SNOOP1_CTRL_SNOOPRWB(self)
        self.zz_fdict['SNOOPRWB'] = self.SNOOPRWB
        self.SNOOPSIZE = RM_Field_GPCRC_SNOOP1_CTRL_SNOOPSIZE(self)
        self.zz_fdict['SNOOPSIZE'] = self.SNOOPSIZE
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_SNOOP1_ADDR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_SNOOP1_ADDR, self).__init__(rmio, label,
            0x4001c000, 0x034,
            'SNOOP1_ADDR', 'GPCRC.SNOOP1_ADDR', 'read-write',
            "",
            0x40000000, 0x001FFFFC)

        self.SNOOPADDR = RM_Field_GPCRC_SNOOP1_ADDR_SNOOPADDR(self)
        self.zz_fdict['SNOOPADDR'] = self.SNOOPADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_SNOOP2_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_SNOOP2_CTRL, self).__init__(rmio, label,
            0x4001c000, 0x038,
            'SNOOP2_CTRL', 'GPCRC.SNOOP2_CTRL', 'read-write',
            "",
            0x00000000, 0x0000000F)

        self.SNOOPEN = RM_Field_GPCRC_SNOOP2_CTRL_SNOOPEN(self)
        self.zz_fdict['SNOOPEN'] = self.SNOOPEN
        self.SNOOPRWB = RM_Field_GPCRC_SNOOP2_CTRL_SNOOPRWB(self)
        self.zz_fdict['SNOOPRWB'] = self.SNOOPRWB
        self.SNOOPSIZE = RM_Field_GPCRC_SNOOP2_CTRL_SNOOPSIZE(self)
        self.zz_fdict['SNOOPSIZE'] = self.SNOOPSIZE
        self.__dict__['zz_frozen'] = True


class RM_Register_GPCRC_SNOOP2_ADDR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPCRC_SNOOP2_ADDR, self).__init__(rmio, label,
            0x4001c000, 0x03C,
            'SNOOP2_ADDR', 'GPCRC.SNOOP2_ADDR', 'read-write',
            "",
            0x40000000, 0x001FFFFC)

        self.SNOOPADDR = RM_Field_GPCRC_SNOOP2_ADDR_SNOOPADDR(self)
        self.zz_fdict['SNOOPADDR'] = self.SNOOPADDR
        self.__dict__['zz_frozen'] = True


