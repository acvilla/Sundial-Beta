
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_CRYPTO_CTRL_INCWIDTH(Base_RM_Enum):
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
        super(RM_Enum_CRYPTO_CTRL_INCWIDTH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO_CTRL_DMA0MODE(Base_RM_Enum):
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
        super(RM_Enum_CRYPTO_CTRL_DMA0MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO_CTRL_DMA0RSEL(Base_RM_Enum):
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
        super(RM_Enum_CRYPTO_CTRL_DMA0RSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO_CTRL_DMA1MODE(Base_RM_Enum):
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
        super(RM_Enum_CRYPTO_CTRL_DMA1MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO_CTRL_DMA1RSEL(Base_RM_Enum):
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
        super(RM_Enum_CRYPTO_CTRL_DMA1RSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO_WAC_MODULUS(Base_RM_Enum):
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
        super(RM_Enum_CRYPTO_WAC_MODULUS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO_WAC_MULWIDTH(Base_RM_Enum):
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
        super(RM_Enum_CRYPTO_WAC_MULWIDTH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO_WAC_RESULTWIDTH(Base_RM_Enum):
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
        super(RM_Enum_CRYPTO_WAC_RESULTWIDTH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO_CMD_INSTR(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.END = 0x00000000
        zz_edict['END'] = self.END
        zz_desc['END'] = ""
        self.EXEC = 0x00000001
        zz_edict['EXEC'] = self.EXEC
        zz_desc['EXEC'] = ""
        self.DATA1INC = 0x00000003
        zz_edict['DATA1INC'] = self.DATA1INC
        zz_desc['DATA1INC'] = ""
        self.DATA1INCCLR = 0x00000004
        zz_edict['DATA1INCCLR'] = self.DATA1INCCLR
        zz_desc['DATA1INCCLR'] = ""
        self.AESENC = 0x00000005
        zz_edict['AESENC'] = self.AESENC
        zz_desc['AESENC'] = ""
        self.AESDEC = 0x00000006
        zz_edict['AESDEC'] = self.AESDEC
        zz_desc['AESDEC'] = ""
        self.SHA = 0x00000007
        zz_edict['SHA'] = self.SHA
        zz_desc['SHA'] = ""
        self.ADD = 0x00000008
        zz_edict['ADD'] = self.ADD
        zz_desc['ADD'] = ""
        self.ADDC = 0x00000009
        zz_edict['ADDC'] = self.ADDC
        zz_desc['ADDC'] = ""
        self.LADD = 0x0000000A
        zz_edict['LADD'] = self.LADD
        zz_desc['LADD'] = ""
        self.LADDC = 0x0000000B
        zz_edict['LADDC'] = self.LADDC
        zz_desc['LADDC'] = ""
        self.MADD = 0x0000000C
        zz_edict['MADD'] = self.MADD
        zz_desc['MADD'] = ""
        self.MADD32 = 0x0000000D
        zz_edict['MADD32'] = self.MADD32
        zz_desc['MADD32'] = ""
        self.SUB = 0x00000010
        zz_edict['SUB'] = self.SUB
        zz_desc['SUB'] = ""
        self.SUBC = 0x00000011
        zz_edict['SUBC'] = self.SUBC
        zz_desc['SUBC'] = ""
        self.LSUB = 0x00000012
        zz_edict['LSUB'] = self.LSUB
        zz_desc['LSUB'] = ""
        self.LSUBC = 0x00000013
        zz_edict['LSUBC'] = self.LSUBC
        zz_desc['LSUBC'] = ""
        self.MSUB = 0x00000014
        zz_edict['MSUB'] = self.MSUB
        zz_desc['MSUB'] = ""
        self.MUL = 0x00000018
        zz_edict['MUL'] = self.MUL
        zz_desc['MUL'] = ""
        self.MULC = 0x00000019
        zz_edict['MULC'] = self.MULC
        zz_desc['MULC'] = ""
        self.LMUL = 0x0000001A
        zz_edict['LMUL'] = self.LMUL
        zz_desc['LMUL'] = ""
        self.LMULC = 0x0000001B
        zz_edict['LMULC'] = self.LMULC
        zz_desc['LMULC'] = ""
        self.MMUL = 0x0000001C
        zz_edict['MMUL'] = self.MMUL
        zz_desc['MMUL'] = ""
        self.MULO = 0x0000001D
        zz_edict['MULO'] = self.MULO
        zz_desc['MULO'] = ""
        self.LMULO = 0x0000001F
        zz_edict['LMULO'] = self.LMULO
        zz_desc['LMULO'] = ""
        self.SHL = 0x00000020
        zz_edict['SHL'] = self.SHL
        zz_desc['SHL'] = ""
        self.SHLC = 0x00000021
        zz_edict['SHLC'] = self.SHLC
        zz_desc['SHLC'] = ""
        self.SHLB = 0x00000022
        zz_edict['SHLB'] = self.SHLB
        zz_desc['SHLB'] = ""
        self.SHL1 = 0x00000023
        zz_edict['SHL1'] = self.SHL1
        zz_desc['SHL1'] = ""
        self.SHR = 0x00000024
        zz_edict['SHR'] = self.SHR
        zz_desc['SHR'] = ""
        self.SHRC = 0x00000025
        zz_edict['SHRC'] = self.SHRC
        zz_desc['SHRC'] = ""
        self.SHRB = 0x00000026
        zz_edict['SHRB'] = self.SHRB
        zz_desc['SHRB'] = ""
        self.SHR1 = 0x00000027
        zz_edict['SHR1'] = self.SHR1
        zz_desc['SHR1'] = ""
        self.ADDO = 0x00000028
        zz_edict['ADDO'] = self.ADDO
        zz_desc['ADDO'] = ""
        self.ADDIC = 0x00000029
        zz_edict['ADDIC'] = self.ADDIC
        zz_desc['ADDIC'] = ""
        self.LADDO = 0x0000002A
        zz_edict['LADDO'] = self.LADDO
        zz_desc['LADDO'] = ""
        self.LADDIC = 0x0000002B
        zz_edict['LADDIC'] = self.LADDIC
        zz_desc['LADDIC'] = ""
        self.CLR = 0x00000030
        zz_edict['CLR'] = self.CLR
        zz_desc['CLR'] = ""
        self.XOR = 0x00000031
        zz_edict['XOR'] = self.XOR
        zz_desc['XOR'] = ""
        self.INV = 0x00000032
        zz_edict['INV'] = self.INV
        zz_desc['INV'] = ""
        self.CSET = 0x00000034
        zz_edict['CSET'] = self.CSET
        zz_desc['CSET'] = ""
        self.CCLR = 0x00000035
        zz_edict['CCLR'] = self.CCLR
        zz_desc['CCLR'] = ""
        self.BBSWAP128 = 0x00000036
        zz_edict['BBSWAP128'] = self.BBSWAP128
        zz_desc['BBSWAP128'] = ""
        self.INC = 0x00000038
        zz_edict['INC'] = self.INC
        zz_desc['INC'] = ""
        self.DEC = 0x00000039
        zz_edict['DEC'] = self.DEC
        zz_desc['DEC'] = ""
        self.LINC = 0x0000003A
        zz_edict['LINC'] = self.LINC
        zz_desc['LINC'] = ""
        self.LDEC = 0x0000003B
        zz_edict['LDEC'] = self.LDEC
        zz_desc['LDEC'] = ""
        self.SHRA = 0x0000003E
        zz_edict['SHRA'] = self.SHRA
        zz_desc['SHRA'] = ""
        self.DATA0TODATA0 = 0x00000040
        zz_edict['DATA0TODATA0'] = self.DATA0TODATA0
        zz_desc['DATA0TODATA0'] = ""
        self.DATA0TODATA0XOR = 0x00000041
        zz_edict['DATA0TODATA0XOR'] = self.DATA0TODATA0XOR
        zz_desc['DATA0TODATA0XOR'] = ""
        self.DATA0TODATA0XORLEN = 0x00000042
        zz_edict['DATA0TODATA0XORLEN'] = self.DATA0TODATA0XORLEN
        zz_desc['DATA0TODATA0XORLEN'] = ""
        self.DATA0TODATA1 = 0x00000044
        zz_edict['DATA0TODATA1'] = self.DATA0TODATA1
        zz_desc['DATA0TODATA1'] = ""
        self.DATA0TODATA2 = 0x00000045
        zz_edict['DATA0TODATA2'] = self.DATA0TODATA2
        zz_desc['DATA0TODATA2'] = ""
        self.DATA0TODATA3 = 0x00000046
        zz_edict['DATA0TODATA3'] = self.DATA0TODATA3
        zz_desc['DATA0TODATA3'] = ""
        self.DATA1TODATA0 = 0x00000048
        zz_edict['DATA1TODATA0'] = self.DATA1TODATA0
        zz_desc['DATA1TODATA0'] = ""
        self.DATA1TODATA0XOR = 0x00000049
        zz_edict['DATA1TODATA0XOR'] = self.DATA1TODATA0XOR
        zz_desc['DATA1TODATA0XOR'] = ""
        self.DATA1TODATA0XORLEN = 0x0000004A
        zz_edict['DATA1TODATA0XORLEN'] = self.DATA1TODATA0XORLEN
        zz_desc['DATA1TODATA0XORLEN'] = ""
        self.DATA1TODATA2 = 0x0000004D
        zz_edict['DATA1TODATA2'] = self.DATA1TODATA2
        zz_desc['DATA1TODATA2'] = ""
        self.DATA1TODATA3 = 0x0000004E
        zz_edict['DATA1TODATA3'] = self.DATA1TODATA3
        zz_desc['DATA1TODATA3'] = ""
        self.DATA2TODATA0 = 0x00000050
        zz_edict['DATA2TODATA0'] = self.DATA2TODATA0
        zz_desc['DATA2TODATA0'] = ""
        self.DATA2TODATA0XOR = 0x00000051
        zz_edict['DATA2TODATA0XOR'] = self.DATA2TODATA0XOR
        zz_desc['DATA2TODATA0XOR'] = ""
        self.DATA2TODATA0XORLEN = 0x00000052
        zz_edict['DATA2TODATA0XORLEN'] = self.DATA2TODATA0XORLEN
        zz_desc['DATA2TODATA0XORLEN'] = ""
        self.DATA2TODATA1 = 0x00000054
        zz_edict['DATA2TODATA1'] = self.DATA2TODATA1
        zz_desc['DATA2TODATA1'] = ""
        self.DATA2TODATA3 = 0x00000056
        zz_edict['DATA2TODATA3'] = self.DATA2TODATA3
        zz_desc['DATA2TODATA3'] = ""
        self.DATA3TODATA0 = 0x00000058
        zz_edict['DATA3TODATA0'] = self.DATA3TODATA0
        zz_desc['DATA3TODATA0'] = ""
        self.DATA3TODATA0XOR = 0x00000059
        zz_edict['DATA3TODATA0XOR'] = self.DATA3TODATA0XOR
        zz_desc['DATA3TODATA0XOR'] = ""
        self.DATA3TODATA0XORLEN = 0x0000005A
        zz_edict['DATA3TODATA0XORLEN'] = self.DATA3TODATA0XORLEN
        zz_desc['DATA3TODATA0XORLEN'] = ""
        self.DATA3TODATA1 = 0x0000005C
        zz_edict['DATA3TODATA1'] = self.DATA3TODATA1
        zz_desc['DATA3TODATA1'] = ""
        self.DATA3TODATA2 = 0x0000005D
        zz_edict['DATA3TODATA2'] = self.DATA3TODATA2
        zz_desc['DATA3TODATA2'] = ""
        self.DATATODMA0 = 0x00000063
        zz_edict['DATATODMA0'] = self.DATATODMA0
        zz_desc['DATATODMA0'] = ""
        self.DATA0TOBUF = 0x00000064
        zz_edict['DATA0TOBUF'] = self.DATA0TOBUF
        zz_desc['DATA0TOBUF'] = ""
        self.DATA0TOBUFXOR = 0x00000065
        zz_edict['DATA0TOBUFXOR'] = self.DATA0TOBUFXOR
        zz_desc['DATA0TOBUFXOR'] = ""
        self.DATATODMA1 = 0x0000006B
        zz_edict['DATATODMA1'] = self.DATATODMA1
        zz_desc['DATATODMA1'] = ""
        self.DATA1TOBUF = 0x0000006C
        zz_edict['DATA1TOBUF'] = self.DATA1TOBUF
        zz_desc['DATA1TOBUF'] = ""
        self.DATA1TOBUFXOR = 0x0000006D
        zz_edict['DATA1TOBUFXOR'] = self.DATA1TOBUFXOR
        zz_desc['DATA1TOBUFXOR'] = ""
        self.DMA0TODATA = 0x00000070
        zz_edict['DMA0TODATA'] = self.DMA0TODATA
        zz_desc['DMA0TODATA'] = ""
        self.DMA0TODATAXOR = 0x00000071
        zz_edict['DMA0TODATAXOR'] = self.DMA0TODATAXOR
        zz_desc['DMA0TODATAXOR'] = ""
        self.DMA1TODATA = 0x00000072
        zz_edict['DMA1TODATA'] = self.DMA1TODATA
        zz_desc['DMA1TODATA'] = ""
        self.BUFTODATA0 = 0x00000078
        zz_edict['BUFTODATA0'] = self.BUFTODATA0
        zz_desc['BUFTODATA0'] = ""
        self.BUFTODATA0XOR = 0x00000079
        zz_edict['BUFTODATA0XOR'] = self.BUFTODATA0XOR
        zz_desc['BUFTODATA0XOR'] = ""
        self.BUFTODATA1 = 0x0000007A
        zz_edict['BUFTODATA1'] = self.BUFTODATA1
        zz_desc['BUFTODATA1'] = ""
        self.DDATA0TODDATA1 = 0x00000081
        zz_edict['DDATA0TODDATA1'] = self.DDATA0TODDATA1
        zz_desc['DDATA0TODDATA1'] = ""
        self.DDATA0TODDATA2 = 0x00000082
        zz_edict['DDATA0TODDATA2'] = self.DDATA0TODDATA2
        zz_desc['DDATA0TODDATA2'] = ""
        self.DDATA0TODDATA3 = 0x00000083
        zz_edict['DDATA0TODDATA3'] = self.DDATA0TODDATA3
        zz_desc['DDATA0TODDATA3'] = ""
        self.DDATA0TODDATA4 = 0x00000084
        zz_edict['DDATA0TODDATA4'] = self.DDATA0TODDATA4
        zz_desc['DDATA0TODDATA4'] = ""
        self.DDATA0LTODATA0 = 0x00000085
        zz_edict['DDATA0LTODATA0'] = self.DDATA0LTODATA0
        zz_desc['DDATA0LTODATA0'] = ""
        self.DDATA0HTODATA1 = 0x00000086
        zz_edict['DDATA0HTODATA1'] = self.DDATA0HTODATA1
        zz_desc['DDATA0HTODATA1'] = ""
        self.DDATA0LTODATA2 = 0x00000087
        zz_edict['DDATA0LTODATA2'] = self.DDATA0LTODATA2
        zz_desc['DDATA0LTODATA2'] = ""
        self.DDATA1TODDATA0 = 0x00000088
        zz_edict['DDATA1TODDATA0'] = self.DDATA1TODDATA0
        zz_desc['DDATA1TODDATA0'] = ""
        self.DDATA1TODDATA2 = 0x0000008A
        zz_edict['DDATA1TODDATA2'] = self.DDATA1TODDATA2
        zz_desc['DDATA1TODDATA2'] = ""
        self.DDATA1TODDATA3 = 0x0000008B
        zz_edict['DDATA1TODDATA3'] = self.DDATA1TODDATA3
        zz_desc['DDATA1TODDATA3'] = ""
        self.DDATA1TODDATA4 = 0x0000008C
        zz_edict['DDATA1TODDATA4'] = self.DDATA1TODDATA4
        zz_desc['DDATA1TODDATA4'] = ""
        self.DDATA1LTODATA0 = 0x0000008D
        zz_edict['DDATA1LTODATA0'] = self.DDATA1LTODATA0
        zz_desc['DDATA1LTODATA0'] = ""
        self.DDATA1HTODATA1 = 0x0000008E
        zz_edict['DDATA1HTODATA1'] = self.DDATA1HTODATA1
        zz_desc['DDATA1HTODATA1'] = ""
        self.DDATA1LTODATA2 = 0x0000008F
        zz_edict['DDATA1LTODATA2'] = self.DDATA1LTODATA2
        zz_desc['DDATA1LTODATA2'] = ""
        self.DDATA2TODDATA0 = 0x00000090
        zz_edict['DDATA2TODDATA0'] = self.DDATA2TODDATA0
        zz_desc['DDATA2TODDATA0'] = ""
        self.DDATA2TODDATA1 = 0x00000091
        zz_edict['DDATA2TODDATA1'] = self.DDATA2TODDATA1
        zz_desc['DDATA2TODDATA1'] = ""
        self.DDATA2TODDATA3 = 0x00000093
        zz_edict['DDATA2TODDATA3'] = self.DDATA2TODDATA3
        zz_desc['DDATA2TODDATA3'] = ""
        self.DDATA2TODDATA4 = 0x00000094
        zz_edict['DDATA2TODDATA4'] = self.DDATA2TODDATA4
        zz_desc['DDATA2TODDATA4'] = ""
        self.DDATA2LTODATA2 = 0x00000097
        zz_edict['DDATA2LTODATA2'] = self.DDATA2LTODATA2
        zz_desc['DDATA2LTODATA2'] = ""
        self.DDATA3TODDATA0 = 0x00000098
        zz_edict['DDATA3TODDATA0'] = self.DDATA3TODDATA0
        zz_desc['DDATA3TODDATA0'] = ""
        self.DDATA3TODDATA1 = 0x00000099
        zz_edict['DDATA3TODDATA1'] = self.DDATA3TODDATA1
        zz_desc['DDATA3TODDATA1'] = ""
        self.DDATA3TODDATA2 = 0x0000009A
        zz_edict['DDATA3TODDATA2'] = self.DDATA3TODDATA2
        zz_desc['DDATA3TODDATA2'] = ""
        self.DDATA3TODDATA4 = 0x0000009C
        zz_edict['DDATA3TODDATA4'] = self.DDATA3TODDATA4
        zz_desc['DDATA3TODDATA4'] = ""
        self.DDATA3LTODATA0 = 0x0000009D
        zz_edict['DDATA3LTODATA0'] = self.DDATA3LTODATA0
        zz_desc['DDATA3LTODATA0'] = ""
        self.DDATA3HTODATA1 = 0x0000009E
        zz_edict['DDATA3HTODATA1'] = self.DDATA3HTODATA1
        zz_desc['DDATA3HTODATA1'] = ""
        self.DDATA4TODDATA0 = 0x000000A0
        zz_edict['DDATA4TODDATA0'] = self.DDATA4TODDATA0
        zz_desc['DDATA4TODDATA0'] = ""
        self.DDATA4TODDATA1 = 0x000000A1
        zz_edict['DDATA4TODDATA1'] = self.DDATA4TODDATA1
        zz_desc['DDATA4TODDATA1'] = ""
        self.DDATA4TODDATA2 = 0x000000A2
        zz_edict['DDATA4TODDATA2'] = self.DDATA4TODDATA2
        zz_desc['DDATA4TODDATA2'] = ""
        self.DDATA4TODDATA3 = 0x000000A3
        zz_edict['DDATA4TODDATA3'] = self.DDATA4TODDATA3
        zz_desc['DDATA4TODDATA3'] = ""
        self.DDATA4LTODATA0 = 0x000000A5
        zz_edict['DDATA4LTODATA0'] = self.DDATA4LTODATA0
        zz_desc['DDATA4LTODATA0'] = ""
        self.DDATA4HTODATA1 = 0x000000A6
        zz_edict['DDATA4HTODATA1'] = self.DDATA4HTODATA1
        zz_desc['DDATA4HTODATA1'] = ""
        self.DDATA4LTODATA2 = 0x000000A7
        zz_edict['DDATA4LTODATA2'] = self.DDATA4LTODATA2
        zz_desc['DDATA4LTODATA2'] = ""
        self.DATA0TODDATA0 = 0x000000A8
        zz_edict['DATA0TODDATA0'] = self.DATA0TODDATA0
        zz_desc['DATA0TODDATA0'] = ""
        self.DATA0TODDATA1 = 0x000000A9
        zz_edict['DATA0TODDATA1'] = self.DATA0TODDATA1
        zz_desc['DATA0TODDATA1'] = ""
        self.DATA1TODDATA0 = 0x000000B0
        zz_edict['DATA1TODDATA0'] = self.DATA1TODDATA0
        zz_desc['DATA1TODDATA0'] = ""
        self.DATA1TODDATA1 = 0x000000B1
        zz_edict['DATA1TODDATA1'] = self.DATA1TODDATA1
        zz_desc['DATA1TODDATA1'] = ""
        self.DATA2TODDATA0 = 0x000000B8
        zz_edict['DATA2TODDATA0'] = self.DATA2TODDATA0
        zz_desc['DATA2TODDATA0'] = ""
        self.DATA2TODDATA1 = 0x000000B9
        zz_edict['DATA2TODDATA1'] = self.DATA2TODDATA1
        zz_desc['DATA2TODDATA1'] = ""
        self.DATA2TODDATA2 = 0x000000BA
        zz_edict['DATA2TODDATA2'] = self.DATA2TODDATA2
        zz_desc['DATA2TODDATA2'] = ""
        self.SELDDATA0DDATA0 = 0x000000C0
        zz_edict['SELDDATA0DDATA0'] = self.SELDDATA0DDATA0
        zz_desc['SELDDATA0DDATA0'] = ""
        self.SELDDATA1DDATA0 = 0x000000C1
        zz_edict['SELDDATA1DDATA0'] = self.SELDDATA1DDATA0
        zz_desc['SELDDATA1DDATA0'] = ""
        self.SELDDATA2DDATA0 = 0x000000C2
        zz_edict['SELDDATA2DDATA0'] = self.SELDDATA2DDATA0
        zz_desc['SELDDATA2DDATA0'] = ""
        self.SELDDATA3DDATA0 = 0x000000C3
        zz_edict['SELDDATA3DDATA0'] = self.SELDDATA3DDATA0
        zz_desc['SELDDATA3DDATA0'] = ""
        self.SELDDATA4DDATA0 = 0x000000C4
        zz_edict['SELDDATA4DDATA0'] = self.SELDDATA4DDATA0
        zz_desc['SELDDATA4DDATA0'] = ""
        self.SELDATA0DDATA0 = 0x000000C5
        zz_edict['SELDATA0DDATA0'] = self.SELDATA0DDATA0
        zz_desc['SELDATA0DDATA0'] = ""
        self.SELDATA1DDATA0 = 0x000000C6
        zz_edict['SELDATA1DDATA0'] = self.SELDATA1DDATA0
        zz_desc['SELDATA1DDATA0'] = ""
        self.SELDATA2DDATA0 = 0x000000C7
        zz_edict['SELDATA2DDATA0'] = self.SELDATA2DDATA0
        zz_desc['SELDATA2DDATA0'] = ""
        self.SELDDATA0DDATA1 = 0x000000C8
        zz_edict['SELDDATA0DDATA1'] = self.SELDDATA0DDATA1
        zz_desc['SELDDATA0DDATA1'] = ""
        self.SELDDATA1DDATA1 = 0x000000C9
        zz_edict['SELDDATA1DDATA1'] = self.SELDDATA1DDATA1
        zz_desc['SELDDATA1DDATA1'] = ""
        self.SELDDATA2DDATA1 = 0x000000CA
        zz_edict['SELDDATA2DDATA1'] = self.SELDDATA2DDATA1
        zz_desc['SELDDATA2DDATA1'] = ""
        self.SELDDATA3DDATA1 = 0x000000CB
        zz_edict['SELDDATA3DDATA1'] = self.SELDDATA3DDATA1
        zz_desc['SELDDATA3DDATA1'] = ""
        self.SELDDATA4DDATA1 = 0x000000CC
        zz_edict['SELDDATA4DDATA1'] = self.SELDDATA4DDATA1
        zz_desc['SELDDATA4DDATA1'] = ""
        self.SELDATA0DDATA1 = 0x000000CD
        zz_edict['SELDATA0DDATA1'] = self.SELDATA0DDATA1
        zz_desc['SELDATA0DDATA1'] = ""
        self.SELDATA1DDATA1 = 0x000000CE
        zz_edict['SELDATA1DDATA1'] = self.SELDATA1DDATA1
        zz_desc['SELDATA1DDATA1'] = ""
        self.SELDATA2DDATA1 = 0x000000CF
        zz_edict['SELDATA2DDATA1'] = self.SELDATA2DDATA1
        zz_desc['SELDATA2DDATA1'] = ""
        self.SELDDATA0DDATA2 = 0x000000D0
        zz_edict['SELDDATA0DDATA2'] = self.SELDDATA0DDATA2
        zz_desc['SELDDATA0DDATA2'] = ""
        self.SELDDATA1DDATA2 = 0x000000D1
        zz_edict['SELDDATA1DDATA2'] = self.SELDDATA1DDATA2
        zz_desc['SELDDATA1DDATA2'] = ""
        self.SELDDATA2DDATA2 = 0x000000D2
        zz_edict['SELDDATA2DDATA2'] = self.SELDDATA2DDATA2
        zz_desc['SELDDATA2DDATA2'] = ""
        self.SELDDATA3DDATA2 = 0x000000D3
        zz_edict['SELDDATA3DDATA2'] = self.SELDDATA3DDATA2
        zz_desc['SELDDATA3DDATA2'] = ""
        self.SELDDATA4DDATA2 = 0x000000D4
        zz_edict['SELDDATA4DDATA2'] = self.SELDDATA4DDATA2
        zz_desc['SELDDATA4DDATA2'] = ""
        self.SELDATA0DDATA2 = 0x000000D5
        zz_edict['SELDATA0DDATA2'] = self.SELDATA0DDATA2
        zz_desc['SELDATA0DDATA2'] = ""
        self.SELDATA1DDATA2 = 0x000000D6
        zz_edict['SELDATA1DDATA2'] = self.SELDATA1DDATA2
        zz_desc['SELDATA1DDATA2'] = ""
        self.SELDATA2DDATA2 = 0x000000D7
        zz_edict['SELDATA2DDATA2'] = self.SELDATA2DDATA2
        zz_desc['SELDATA2DDATA2'] = ""
        self.SELDDATA0DDATA3 = 0x000000D8
        zz_edict['SELDDATA0DDATA3'] = self.SELDDATA0DDATA3
        zz_desc['SELDDATA0DDATA3'] = ""
        self.SELDDATA1DDATA3 = 0x000000D9
        zz_edict['SELDDATA1DDATA3'] = self.SELDDATA1DDATA3
        zz_desc['SELDDATA1DDATA3'] = ""
        self.SELDDATA2DDATA3 = 0x000000DA
        zz_edict['SELDDATA2DDATA3'] = self.SELDDATA2DDATA3
        zz_desc['SELDDATA2DDATA3'] = ""
        self.SELDDATA3DDATA3 = 0x000000DB
        zz_edict['SELDDATA3DDATA3'] = self.SELDDATA3DDATA3
        zz_desc['SELDDATA3DDATA3'] = ""
        self.SELDDATA4DDATA3 = 0x000000DC
        zz_edict['SELDDATA4DDATA3'] = self.SELDDATA4DDATA3
        zz_desc['SELDDATA4DDATA3'] = ""
        self.SELDATA0DDATA3 = 0x000000DD
        zz_edict['SELDATA0DDATA3'] = self.SELDATA0DDATA3
        zz_desc['SELDATA0DDATA3'] = ""
        self.SELDATA1DDATA3 = 0x000000DE
        zz_edict['SELDATA1DDATA3'] = self.SELDATA1DDATA3
        zz_desc['SELDATA1DDATA3'] = ""
        self.SELDATA2DDATA3 = 0x000000DF
        zz_edict['SELDATA2DDATA3'] = self.SELDATA2DDATA3
        zz_desc['SELDATA2DDATA3'] = ""
        self.SELDDATA0DDATA4 = 0x000000E0
        zz_edict['SELDDATA0DDATA4'] = self.SELDDATA0DDATA4
        zz_desc['SELDDATA0DDATA4'] = ""
        self.SELDDATA1DDATA4 = 0x000000E1
        zz_edict['SELDDATA1DDATA4'] = self.SELDDATA1DDATA4
        zz_desc['SELDDATA1DDATA4'] = ""
        self.SELDDATA2DDATA4 = 0x000000E2
        zz_edict['SELDDATA2DDATA4'] = self.SELDDATA2DDATA4
        zz_desc['SELDDATA2DDATA4'] = ""
        self.SELDDATA3DDATA4 = 0x000000E3
        zz_edict['SELDDATA3DDATA4'] = self.SELDDATA3DDATA4
        zz_desc['SELDDATA3DDATA4'] = ""
        self.SELDDATA4DDATA4 = 0x000000E4
        zz_edict['SELDDATA4DDATA4'] = self.SELDDATA4DDATA4
        zz_desc['SELDDATA4DDATA4'] = ""
        self.SELDATA0DDATA4 = 0x000000E5
        zz_edict['SELDATA0DDATA4'] = self.SELDATA0DDATA4
        zz_desc['SELDATA0DDATA4'] = ""
        self.SELDATA1DDATA4 = 0x000000E6
        zz_edict['SELDATA1DDATA4'] = self.SELDATA1DDATA4
        zz_desc['SELDATA1DDATA4'] = ""
        self.SELDATA2DDATA4 = 0x000000E7
        zz_edict['SELDATA2DDATA4'] = self.SELDATA2DDATA4
        zz_desc['SELDATA2DDATA4'] = ""
        self.SELDDATA0DATA0 = 0x000000E8
        zz_edict['SELDDATA0DATA0'] = self.SELDDATA0DATA0
        zz_desc['SELDDATA0DATA0'] = ""
        self.SELDDATA1DATA0 = 0x000000E9
        zz_edict['SELDDATA1DATA0'] = self.SELDDATA1DATA0
        zz_desc['SELDDATA1DATA0'] = ""
        self.SELDDATA2DATA0 = 0x000000EA
        zz_edict['SELDDATA2DATA0'] = self.SELDDATA2DATA0
        zz_desc['SELDDATA2DATA0'] = ""
        self.SELDDATA3DATA0 = 0x000000EB
        zz_edict['SELDDATA3DATA0'] = self.SELDDATA3DATA0
        zz_desc['SELDDATA3DATA0'] = ""
        self.SELDDATA4DATA0 = 0x000000EC
        zz_edict['SELDDATA4DATA0'] = self.SELDDATA4DATA0
        zz_desc['SELDDATA4DATA0'] = ""
        self.SELDATA0DATA0 = 0x000000ED
        zz_edict['SELDATA0DATA0'] = self.SELDATA0DATA0
        zz_desc['SELDATA0DATA0'] = ""
        self.SELDATA1DATA0 = 0x000000EE
        zz_edict['SELDATA1DATA0'] = self.SELDATA1DATA0
        zz_desc['SELDATA1DATA0'] = ""
        self.SELDATA2DATA0 = 0x000000EF
        zz_edict['SELDATA2DATA0'] = self.SELDATA2DATA0
        zz_desc['SELDATA2DATA0'] = ""
        self.SELDDATA0DATA1 = 0x000000F0
        zz_edict['SELDDATA0DATA1'] = self.SELDDATA0DATA1
        zz_desc['SELDDATA0DATA1'] = ""
        self.SELDDATA1DATA1 = 0x000000F1
        zz_edict['SELDDATA1DATA1'] = self.SELDDATA1DATA1
        zz_desc['SELDDATA1DATA1'] = ""
        self.SELDDATA2DATA1 = 0x000000F2
        zz_edict['SELDDATA2DATA1'] = self.SELDDATA2DATA1
        zz_desc['SELDDATA2DATA1'] = ""
        self.SELDDATA3DATA1 = 0x000000F3
        zz_edict['SELDDATA3DATA1'] = self.SELDDATA3DATA1
        zz_desc['SELDDATA3DATA1'] = ""
        self.SELDDATA4DATA1 = 0x000000F4
        zz_edict['SELDDATA4DATA1'] = self.SELDDATA4DATA1
        zz_desc['SELDDATA4DATA1'] = ""
        self.SELDATA0DATA1 = 0x000000F5
        zz_edict['SELDATA0DATA1'] = self.SELDATA0DATA1
        zz_desc['SELDATA0DATA1'] = ""
        self.SELDATA1DATA1 = 0x000000F6
        zz_edict['SELDATA1DATA1'] = self.SELDATA1DATA1
        zz_desc['SELDATA1DATA1'] = ""
        self.SELDATA2DATA1 = 0x000000F7
        zz_edict['SELDATA2DATA1'] = self.SELDATA2DATA1
        zz_desc['SELDATA2DATA1'] = ""
        self.EXECIFA = 0x000000F8
        zz_edict['EXECIFA'] = self.EXECIFA
        zz_desc['EXECIFA'] = ""
        self.EXECIFB = 0x000000F9
        zz_edict['EXECIFB'] = self.EXECIFB
        zz_desc['EXECIFB'] = ""
        self.EXECIFNLAST = 0x000000FA
        zz_edict['EXECIFNLAST'] = self.EXECIFNLAST
        zz_desc['EXECIFNLAST'] = ""
        self.EXECIFLAST = 0x000000FB
        zz_edict['EXECIFLAST'] = self.EXECIFLAST
        zz_desc['EXECIFLAST'] = ""
        self.EXECIFCARRY = 0x000000FC
        zz_edict['EXECIFCARRY'] = self.EXECIFCARRY
        zz_desc['EXECIFCARRY'] = ""
        self.EXECIFNCARRY = 0x000000FD
        zz_edict['EXECIFNCARRY'] = self.EXECIFNCARRY
        zz_desc['EXECIFNCARRY'] = ""
        self.EXECALWAYS = 0x000000FE
        zz_edict['EXECALWAYS'] = self.EXECALWAYS
        zz_desc['EXECALWAYS'] = ""
        super(RM_Enum_CRYPTO_CMD_INSTR, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO_DSTATUS_DATA0ZERO(Base_RM_Enum):
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
        super(RM_Enum_CRYPTO_DSTATUS_DATA0ZERO, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO_CSTATUS_V0(Base_RM_Enum):
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
        super(RM_Enum_CRYPTO_CSTATUS_V0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO_CSTATUS_V1(Base_RM_Enum):
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
        super(RM_Enum_CRYPTO_CSTATUS_V1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYPTO_SEQCTRL_BLOCKSIZE(Base_RM_Enum):
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
        super(RM_Enum_CRYPTO_SEQCTRL_BLOCKSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


