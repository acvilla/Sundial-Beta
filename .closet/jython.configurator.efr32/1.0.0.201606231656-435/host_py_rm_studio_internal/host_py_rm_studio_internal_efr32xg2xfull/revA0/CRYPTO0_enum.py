
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_CRYPTO0_CTRL_INCWIDTH(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.INCWIDTH1 = 0x00000000
        zz_edict['INCWIDTH1'] = self.INCWIDTH1
        zz_desc['INCWIDTH1'] = ""
        self.INCWIDTH2 = 0x00000001
        zz_edict['INCWIDTH2'] = self.INCWIDTH2
        zz_desc['INCWIDTH2'] = ""
        self.INCWIDTH3 = 0x00000002
        zz_edict['INCWIDTH3'] = self.INCWIDTH3
        zz_desc['INCWIDTH3'] = ""
        self.INCWIDTH4 = 0x00000003
        zz_edict['INCWIDTH4'] = self.INCWIDTH4
        zz_desc['INCWIDTH4'] = ""
        super(RM_Enum_CRYPTO0_CTRL_INCWIDTH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO0_CTRL_DMA0MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.FULL = 0x00000000
        zz_edict['FULL'] = self.FULL
        zz_desc['FULL'] = ""
        self.LENLIMIT = 0x00000001
        zz_edict['LENLIMIT'] = self.LENLIMIT
        zz_desc['LENLIMIT'] = ""
        self.FULLBYTE = 0x00000002
        zz_edict['FULLBYTE'] = self.FULLBYTE
        zz_desc['FULLBYTE'] = ""
        self.LENLIMITBYTE = 0x00000003
        zz_edict['LENLIMITBYTE'] = self.LENLIMITBYTE
        zz_desc['LENLIMITBYTE'] = ""
        super(RM_Enum_CRYPTO0_CTRL_DMA0MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO0_CTRL_DMA0RSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DATA0 = 0x00000000
        zz_edict['DATA0'] = self.DATA0
        zz_desc['DATA0'] = ""
        self.DDATA0 = 0x00000001
        zz_edict['DDATA0'] = self.DDATA0
        zz_desc['DDATA0'] = ""
        self.DDATA0BIG = 0x00000002
        zz_edict['DDATA0BIG'] = self.DDATA0BIG
        zz_desc['DDATA0BIG'] = ""
        self.QDATA0 = 0x00000003
        zz_edict['QDATA0'] = self.QDATA0
        zz_desc['QDATA0'] = ""
        super(RM_Enum_CRYPTO0_CTRL_DMA0RSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO0_CTRL_DMA1MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.FULL = 0x00000000
        zz_edict['FULL'] = self.FULL
        zz_desc['FULL'] = ""
        self.LENLIMIT = 0x00000001
        zz_edict['LENLIMIT'] = self.LENLIMIT
        zz_desc['LENLIMIT'] = ""
        self.FULLBYTE = 0x00000002
        zz_edict['FULLBYTE'] = self.FULLBYTE
        zz_desc['FULLBYTE'] = ""
        self.LENLIMITBYTE = 0x00000003
        zz_edict['LENLIMITBYTE'] = self.LENLIMITBYTE
        zz_desc['LENLIMITBYTE'] = ""
        super(RM_Enum_CRYPTO0_CTRL_DMA1MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO0_CTRL_DMA1RSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DATA1 = 0x00000000
        zz_edict['DATA1'] = self.DATA1
        zz_desc['DATA1'] = ""
        self.DDATA1 = 0x00000001
        zz_edict['DDATA1'] = self.DDATA1
        zz_desc['DDATA1'] = ""
        self.QDATA1 = 0x00000002
        zz_edict['QDATA1'] = self.QDATA1
        zz_desc['QDATA1'] = ""
        self.QDATA1BIG = 0x00000003
        zz_edict['QDATA1BIG'] = self.QDATA1BIG
        zz_desc['QDATA1BIG'] = ""
        super(RM_Enum_CRYPTO0_CTRL_DMA1RSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO0_WAC_MODULUS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BIN256 = 0x00000000
        zz_edict['BIN256'] = self.BIN256
        zz_desc['BIN256'] = ""
        self.BIN128 = 0x00000001
        zz_edict['BIN128'] = self.BIN128
        zz_desc['BIN128'] = ""
        self.ECCBIN233P = 0x00000002
        zz_edict['ECCBIN233P'] = self.ECCBIN233P
        zz_desc['ECCBIN233P'] = ""
        self.ECCBIN163P = 0x00000003
        zz_edict['ECCBIN163P'] = self.ECCBIN163P
        zz_desc['ECCBIN163P'] = ""
        self.GCMBIN128 = 0x00000004
        zz_edict['GCMBIN128'] = self.GCMBIN128
        zz_desc['GCMBIN128'] = ""
        self.ECCPRIME256P = 0x00000005
        zz_edict['ECCPRIME256P'] = self.ECCPRIME256P
        zz_desc['ECCPRIME256P'] = ""
        self.ECCPRIME224P = 0x00000006
        zz_edict['ECCPRIME224P'] = self.ECCPRIME224P
        zz_desc['ECCPRIME224P'] = ""
        self.ECCPRIME192P = 0x00000007
        zz_edict['ECCPRIME192P'] = self.ECCPRIME192P
        zz_desc['ECCPRIME192P'] = ""
        self.ECCBIN233N = 0x00000008
        zz_edict['ECCBIN233N'] = self.ECCBIN233N
        zz_desc['ECCBIN233N'] = ""
        self.ECCBIN233KN = 0x00000009
        zz_edict['ECCBIN233KN'] = self.ECCBIN233KN
        zz_desc['ECCBIN233KN'] = ""
        self.ECCBIN163N = 0x0000000A
        zz_edict['ECCBIN163N'] = self.ECCBIN163N
        zz_desc['ECCBIN163N'] = ""
        self.ECCBIN163KN = 0x0000000B
        zz_edict['ECCBIN163KN'] = self.ECCBIN163KN
        zz_desc['ECCBIN163KN'] = ""
        self.ECCPRIME256N = 0x0000000C
        zz_edict['ECCPRIME256N'] = self.ECCPRIME256N
        zz_desc['ECCPRIME256N'] = ""
        self.ECCPRIME224N = 0x0000000D
        zz_edict['ECCPRIME224N'] = self.ECCPRIME224N
        zz_desc['ECCPRIME224N'] = ""
        self.ECCPRIME192N = 0x0000000E
        zz_edict['ECCPRIME192N'] = self.ECCPRIME192N
        zz_desc['ECCPRIME192N'] = ""
        super(RM_Enum_CRYPTO0_WAC_MODULUS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO0_WAC_MULWIDTH(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.MUL256 = 0x00000000
        zz_edict['MUL256'] = self.MUL256
        zz_desc['MUL256'] = ""
        self.MUL128 = 0x00000001
        zz_edict['MUL128'] = self.MUL128
        zz_desc['MUL128'] = ""
        self.MULMOD = 0x00000002
        zz_edict['MULMOD'] = self.MULMOD
        zz_desc['MULMOD'] = ""
        super(RM_Enum_CRYPTO0_WAC_MULWIDTH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO0_WAC_RESULTWIDTH(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '256BIT' to 'E256BIT'")
        self.E256BIT = 0x00000000
        zz_edict['E256BIT'] = self.E256BIT
        zz_desc['E256BIT'] = ""
        #print("WARNING: Aliasing enum '128BIT' to 'E128BIT'")
        self.E128BIT = 0x00000001
        zz_edict['E128BIT'] = self.E128BIT
        zz_desc['E128BIT'] = ""
        #print("WARNING: Aliasing enum '260BIT' to 'E260BIT'")
        self.E260BIT = 0x00000002
        zz_edict['E260BIT'] = self.E260BIT
        zz_desc['E260BIT'] = ""
        super(RM_Enum_CRYPTO0_WAC_RESULTWIDTH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO0_DSTATUS_DATA0ZERO(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ZERO0TO31 = 0x00000001
        zz_edict['ZERO0TO31'] = self.ZERO0TO31
        zz_desc['ZERO0TO31'] = ""
        self.ZERO32TO63 = 0x00000002
        zz_edict['ZERO32TO63'] = self.ZERO32TO63
        zz_desc['ZERO32TO63'] = ""
        self.ZERO64TO95 = 0x00000004
        zz_edict['ZERO64TO95'] = self.ZERO64TO95
        zz_desc['ZERO64TO95'] = ""
        self.ZERO96TO127 = 0x00000008
        zz_edict['ZERO96TO127'] = self.ZERO96TO127
        zz_desc['ZERO96TO127'] = ""
        super(RM_Enum_CRYPTO0_DSTATUS_DATA0ZERO, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO0_CSTATUS_V0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DDATA0 = 0x00000000
        zz_edict['DDATA0'] = self.DDATA0
        zz_desc['DDATA0'] = ""
        self.DDATA1 = 0x00000001
        zz_edict['DDATA1'] = self.DDATA1
        zz_desc['DDATA1'] = ""
        self.DDATA2 = 0x00000002
        zz_edict['DDATA2'] = self.DDATA2
        zz_desc['DDATA2'] = ""
        self.DDATA3 = 0x00000003
        zz_edict['DDATA3'] = self.DDATA3
        zz_desc['DDATA3'] = ""
        self.DDATA4 = 0x00000004
        zz_edict['DDATA4'] = self.DDATA4
        zz_desc['DDATA4'] = ""
        self.DATA0 = 0x00000005
        zz_edict['DATA0'] = self.DATA0
        zz_desc['DATA0'] = ""
        self.DATA1 = 0x00000006
        zz_edict['DATA1'] = self.DATA1
        zz_desc['DATA1'] = ""
        self.DATA2 = 0x00000007
        zz_edict['DATA2'] = self.DATA2
        zz_desc['DATA2'] = ""
        super(RM_Enum_CRYPTO0_CSTATUS_V0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO0_CSTATUS_V1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DDATA0 = 0x00000000
        zz_edict['DDATA0'] = self.DDATA0
        zz_desc['DDATA0'] = ""
        self.DDATA1 = 0x00000001
        zz_edict['DDATA1'] = self.DDATA1
        zz_desc['DDATA1'] = ""
        self.DDATA2 = 0x00000002
        zz_edict['DDATA2'] = self.DDATA2
        zz_desc['DDATA2'] = ""
        self.DDATA3 = 0x00000003
        zz_edict['DDATA3'] = self.DDATA3
        zz_desc['DDATA3'] = ""
        self.DDATA4 = 0x00000004
        zz_edict['DDATA4'] = self.DDATA4
        zz_desc['DDATA4'] = ""
        self.DATA0 = 0x00000005
        zz_edict['DATA0'] = self.DATA0
        zz_desc['DATA0'] = ""
        self.DATA1 = 0x00000006
        zz_edict['DATA1'] = self.DATA1
        zz_desc['DATA1'] = ""
        self.DATA2 = 0x00000007
        zz_edict['DATA2'] = self.DATA2
        zz_desc['DATA2'] = ""
        super(RM_Enum_CRYPTO0_CSTATUS_V1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO0_SEQCTRL_BLOCKSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '16BYTES' to 'E16BYTES'")
        self.E16BYTES = 0x00000000
        zz_edict['E16BYTES'] = self.E16BYTES
        zz_desc['E16BYTES'] = ""
        #print("WARNING: Aliasing enum '32BYTES' to 'E32BYTES'")
        self.E32BYTES = 0x00000001
        zz_edict['E32BYTES'] = self.E32BYTES
        zz_desc['E32BYTES'] = ""
        #print("WARNING: Aliasing enum '64BYTES' to 'E64BYTES'")
        self.E64BYTES = 0x00000002
        zz_edict['E64BYTES'] = self.E64BYTES
        zz_desc['E64BYTES'] = ""
        super(RM_Enum_CRYPTO0_SEQCTRL_BLOCKSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


