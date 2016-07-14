
from static import Base_RM_Register
from CRYPTO1_field import *


class RM_Register_CRYPTO1_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_CTRL, self).__init__(rmio, label,
            0x400f0400, 0x000,
            'CTRL', 'CRYPTO1.CTRL', 'read-write',
            "",
            0x00000000, 0xB333F5B7)

        self.AES = RM_Field_CRYPTO1_CTRL_AES(self)
        self.zz_fdict['AES'] = self.AES
        self.KEYBUFDIS = RM_Field_CRYPTO1_CTRL_KEYBUFDIS(self)
        self.zz_fdict['KEYBUFDIS'] = self.KEYBUFDIS
        self.SHA = RM_Field_CRYPTO1_CTRL_SHA(self)
        self.zz_fdict['SHA'] = self.SHA
        self.READBUFSEL = RM_Field_CRYPTO1_CTRL_READBUFSEL(self)
        self.zz_fdict['READBUFSEL'] = self.READBUFSEL
        self.WRITEBUFSEL = RM_Field_CRYPTO1_CTRL_WRITEBUFSEL(self)
        self.zz_fdict['WRITEBUFSEL'] = self.WRITEBUFSEL
        self.NOBUSYSTALL = RM_Field_CRYPTO1_CTRL_NOBUSYSTALL(self)
        self.zz_fdict['NOBUSYSTALL'] = self.NOBUSYSTALL
        self.DATA0TOBUFXOROW = RM_Field_CRYPTO1_CTRL_DATA0TOBUFXOROW(self)
        self.zz_fdict['DATA0TOBUFXOROW'] = self.DATA0TOBUFXOROW
        self.DATA1TOBUFXOROW = RM_Field_CRYPTO1_CTRL_DATA1TOBUFXOROW(self)
        self.zz_fdict['DATA1TOBUFXOROW'] = self.DATA1TOBUFXOROW
        self.INCWIDTH = RM_Field_CRYPTO1_CTRL_INCWIDTH(self)
        self.zz_fdict['INCWIDTH'] = self.INCWIDTH
        self.DMA0MODE = RM_Field_CRYPTO1_CTRL_DMA0MODE(self)
        self.zz_fdict['DMA0MODE'] = self.DMA0MODE
        self.DMA0RSEL = RM_Field_CRYPTO1_CTRL_DMA0RSEL(self)
        self.zz_fdict['DMA0RSEL'] = self.DMA0RSEL
        self.DMA1MODE = RM_Field_CRYPTO1_CTRL_DMA1MODE(self)
        self.zz_fdict['DMA1MODE'] = self.DMA1MODE
        self.DMA1RSEL = RM_Field_CRYPTO1_CTRL_DMA1RSEL(self)
        self.zz_fdict['DMA1RSEL'] = self.DMA1RSEL
        self.COMBDMA0WEREQ = RM_Field_CRYPTO1_CTRL_COMBDMA0WEREQ(self)
        self.zz_fdict['COMBDMA0WEREQ'] = self.COMBDMA0WEREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_WAC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_WAC, self).__init__(rmio, label,
            0x400f0400, 0x004,
            'WAC', 'CRYPTO1.WAC', 'read-write',
            "",
            0x00000000, 0x00000F1F)

        self.MODULUS = RM_Field_CRYPTO1_WAC_MODULUS(self)
        self.zz_fdict['MODULUS'] = self.MODULUS
        self.MODOP = RM_Field_CRYPTO1_WAC_MODOP(self)
        self.zz_fdict['MODOP'] = self.MODOP
        self.MULWIDTH = RM_Field_CRYPTO1_WAC_MULWIDTH(self)
        self.zz_fdict['MULWIDTH'] = self.MULWIDTH
        self.RESULTWIDTH = RM_Field_CRYPTO1_WAC_RESULTWIDTH(self)
        self.zz_fdict['RESULTWIDTH'] = self.RESULTWIDTH
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_CMD, self).__init__(rmio, label,
            0x400f0400, 0x008,
            'CMD', 'CRYPTO1.CMD', 'read-write',
            "",
            0x00000000, 0x00000EFF)

        self.INSTR = RM_Field_CRYPTO1_CMD_INSTR(self)
        self.zz_fdict['INSTR'] = self.INSTR
        self.SEQSTART = RM_Field_CRYPTO1_CMD_SEQSTART(self)
        self.zz_fdict['SEQSTART'] = self.SEQSTART
        self.SEQSTOP = RM_Field_CRYPTO1_CMD_SEQSTOP(self)
        self.zz_fdict['SEQSTOP'] = self.SEQSTOP
        self.SEQSTEP = RM_Field_CRYPTO1_CMD_SEQSTEP(self)
        self.zz_fdict['SEQSTEP'] = self.SEQSTEP
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_STATUS, self).__init__(rmio, label,
            0x400f0400, 0x010,
            'STATUS', 'CRYPTO1.STATUS', 'read-only',
            "",
            0x00000000, 0x0000000F)

        self.SEQRUNNING = RM_Field_CRYPTO1_STATUS_SEQRUNNING(self)
        self.zz_fdict['SEQRUNNING'] = self.SEQRUNNING
        self.INSTRRUNNING = RM_Field_CRYPTO1_STATUS_INSTRRUNNING(self)
        self.zz_fdict['INSTRRUNNING'] = self.INSTRRUNNING
        self.DMAACTIVE = RM_Field_CRYPTO1_STATUS_DMAACTIVE(self)
        self.zz_fdict['DMAACTIVE'] = self.DMAACTIVE
        self.BUFACTIVE = RM_Field_CRYPTO1_STATUS_BUFACTIVE(self)
        self.zz_fdict['BUFACTIVE'] = self.BUFACTIVE
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DSTATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DSTATUS, self).__init__(rmio, label,
            0x400f0400, 0x014,
            'DSTATUS', 'CRYPTO1.DSTATUS', 'read-only',
            "",
            0x00000000, 0x011F0F0F)

        self.DATA0ZERO = RM_Field_CRYPTO1_DSTATUS_DATA0ZERO(self)
        self.zz_fdict['DATA0ZERO'] = self.DATA0ZERO
        self.DDATA0LSBS = RM_Field_CRYPTO1_DSTATUS_DDATA0LSBS(self)
        self.zz_fdict['DDATA0LSBS'] = self.DDATA0LSBS
        self.DDATA0MSBS = RM_Field_CRYPTO1_DSTATUS_DDATA0MSBS(self)
        self.zz_fdict['DDATA0MSBS'] = self.DDATA0MSBS
        self.DDATA1MSB = RM_Field_CRYPTO1_DSTATUS_DDATA1MSB(self)
        self.zz_fdict['DDATA1MSB'] = self.DDATA1MSB
        self.CARRY = RM_Field_CRYPTO1_DSTATUS_CARRY(self)
        self.zz_fdict['CARRY'] = self.CARRY
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_CSTATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_CSTATUS, self).__init__(rmio, label,
            0x400f0400, 0x018,
            'CSTATUS', 'CRYPTO1.CSTATUS', 'read-only',
            "",
            0x00000201, 0x01F30707)

        self.V0 = RM_Field_CRYPTO1_CSTATUS_V0(self)
        self.zz_fdict['V0'] = self.V0
        self.V1 = RM_Field_CRYPTO1_CSTATUS_V1(self)
        self.zz_fdict['V1'] = self.V1
        self.SEQPART = RM_Field_CRYPTO1_CSTATUS_SEQPART(self)
        self.zz_fdict['SEQPART'] = self.SEQPART
        self.SEQSKIP = RM_Field_CRYPTO1_CSTATUS_SEQSKIP(self)
        self.zz_fdict['SEQSKIP'] = self.SEQSKIP
        self.SEQIP = RM_Field_CRYPTO1_CSTATUS_SEQIP(self)
        self.zz_fdict['SEQIP'] = self.SEQIP
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_KEY(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_KEY, self).__init__(rmio, label,
            0x400f0400, 0x020,
            'KEY', 'CRYPTO1.KEY', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.KEY = RM_Field_CRYPTO1_KEY_KEY(self)
        self.zz_fdict['KEY'] = self.KEY
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_KEYBUF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_KEYBUF, self).__init__(rmio, label,
            0x400f0400, 0x024,
            'KEYBUF', 'CRYPTO1.KEYBUF', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.KEYBUF = RM_Field_CRYPTO1_KEYBUF_KEYBUF(self)
        self.zz_fdict['KEYBUF'] = self.KEYBUF
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_SEQCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_SEQCTRL, self).__init__(rmio, label,
            0x400f0400, 0x030,
            'SEQCTRL', 'CRYPTO1.SEQCTRL', 'read-write',
            "",
            0x00000000, 0xBF303FFF)

        self.LENGTHA = RM_Field_CRYPTO1_SEQCTRL_LENGTHA(self)
        self.zz_fdict['LENGTHA'] = self.LENGTHA
        self.BLOCKSIZE = RM_Field_CRYPTO1_SEQCTRL_BLOCKSIZE(self)
        self.zz_fdict['BLOCKSIZE'] = self.BLOCKSIZE
        self.DMA0SKIP = RM_Field_CRYPTO1_SEQCTRL_DMA0SKIP(self)
        self.zz_fdict['DMA0SKIP'] = self.DMA0SKIP
        self.DMA1SKIP = RM_Field_CRYPTO1_SEQCTRL_DMA1SKIP(self)
        self.zz_fdict['DMA1SKIP'] = self.DMA1SKIP
        self.DMA0PRESA = RM_Field_CRYPTO1_SEQCTRL_DMA0PRESA(self)
        self.zz_fdict['DMA0PRESA'] = self.DMA0PRESA
        self.DMA1PRESA = RM_Field_CRYPTO1_SEQCTRL_DMA1PRESA(self)
        self.zz_fdict['DMA1PRESA'] = self.DMA1PRESA
        self.HALT = RM_Field_CRYPTO1_SEQCTRL_HALT(self)
        self.zz_fdict['HALT'] = self.HALT
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_SEQCTRLB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_SEQCTRLB, self).__init__(rmio, label,
            0x400f0400, 0x034,
            'SEQCTRLB', 'CRYPTO1.SEQCTRLB', 'read-write',
            "",
            0x00000000, 0x30003FFF)

        self.LENGTHB = RM_Field_CRYPTO1_SEQCTRLB_LENGTHB(self)
        self.zz_fdict['LENGTHB'] = self.LENGTHB
        self.DMA0PRESB = RM_Field_CRYPTO1_SEQCTRLB_DMA0PRESB(self)
        self.zz_fdict['DMA0PRESB'] = self.DMA0PRESB
        self.DMA1PRESB = RM_Field_CRYPTO1_SEQCTRLB_DMA1PRESB(self)
        self.zz_fdict['DMA1PRESB'] = self.DMA1PRESB
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_IF, self).__init__(rmio, label,
            0x400f0400, 0x040,
            'IF', 'CRYPTO1.IF', 'read-only',
            "",
            0x00000000, 0x0000000F)

        self.INSTRDONE = RM_Field_CRYPTO1_IF_INSTRDONE(self)
        self.zz_fdict['INSTRDONE'] = self.INSTRDONE
        self.SEQDONE = RM_Field_CRYPTO1_IF_SEQDONE(self)
        self.zz_fdict['SEQDONE'] = self.SEQDONE
        self.BUFOF = RM_Field_CRYPTO1_IF_BUFOF(self)
        self.zz_fdict['BUFOF'] = self.BUFOF
        self.BUFUF = RM_Field_CRYPTO1_IF_BUFUF(self)
        self.zz_fdict['BUFUF'] = self.BUFUF
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_IFS, self).__init__(rmio, label,
            0x400f0400, 0x044,
            'IFS', 'CRYPTO1.IFS', 'write-only',
            "",
            0x00000000, 0x0000000F)

        self.INSTRDONE = RM_Field_CRYPTO1_IFS_INSTRDONE(self)
        self.zz_fdict['INSTRDONE'] = self.INSTRDONE
        self.SEQDONE = RM_Field_CRYPTO1_IFS_SEQDONE(self)
        self.zz_fdict['SEQDONE'] = self.SEQDONE
        self.BUFOF = RM_Field_CRYPTO1_IFS_BUFOF(self)
        self.zz_fdict['BUFOF'] = self.BUFOF
        self.BUFUF = RM_Field_CRYPTO1_IFS_BUFUF(self)
        self.zz_fdict['BUFUF'] = self.BUFUF
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_IFC, self).__init__(rmio, label,
            0x400f0400, 0x048,
            'IFC', 'CRYPTO1.IFC', 'write-only',
            "",
            0x00000000, 0x0000000F)

        self.INSTRDONE = RM_Field_CRYPTO1_IFC_INSTRDONE(self)
        self.zz_fdict['INSTRDONE'] = self.INSTRDONE
        self.SEQDONE = RM_Field_CRYPTO1_IFC_SEQDONE(self)
        self.zz_fdict['SEQDONE'] = self.SEQDONE
        self.BUFOF = RM_Field_CRYPTO1_IFC_BUFOF(self)
        self.zz_fdict['BUFOF'] = self.BUFOF
        self.BUFUF = RM_Field_CRYPTO1_IFC_BUFUF(self)
        self.zz_fdict['BUFUF'] = self.BUFUF
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_IEN, self).__init__(rmio, label,
            0x400f0400, 0x04C,
            'IEN', 'CRYPTO1.IEN', 'read-write',
            "",
            0x00000000, 0x0000000F)

        self.INSTRDONE = RM_Field_CRYPTO1_IEN_INSTRDONE(self)
        self.zz_fdict['INSTRDONE'] = self.INSTRDONE
        self.SEQDONE = RM_Field_CRYPTO1_IEN_SEQDONE(self)
        self.zz_fdict['SEQDONE'] = self.SEQDONE
        self.BUFOF = RM_Field_CRYPTO1_IEN_BUFOF(self)
        self.zz_fdict['BUFOF'] = self.BUFOF
        self.BUFUF = RM_Field_CRYPTO1_IEN_BUFUF(self)
        self.zz_fdict['BUFUF'] = self.BUFUF
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_SEQ0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_SEQ0, self).__init__(rmio, label,
            0x400f0400, 0x050,
            'SEQ0', 'CRYPTO1.SEQ0', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.INSTR0 = RM_Field_CRYPTO1_SEQ0_INSTR0(self)
        self.zz_fdict['INSTR0'] = self.INSTR0
        self.INSTR1 = RM_Field_CRYPTO1_SEQ0_INSTR1(self)
        self.zz_fdict['INSTR1'] = self.INSTR1
        self.INSTR2 = RM_Field_CRYPTO1_SEQ0_INSTR2(self)
        self.zz_fdict['INSTR2'] = self.INSTR2
        self.INSTR3 = RM_Field_CRYPTO1_SEQ0_INSTR3(self)
        self.zz_fdict['INSTR3'] = self.INSTR3
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_SEQ1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_SEQ1, self).__init__(rmio, label,
            0x400f0400, 0x054,
            'SEQ1', 'CRYPTO1.SEQ1', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.INSTR4 = RM_Field_CRYPTO1_SEQ1_INSTR4(self)
        self.zz_fdict['INSTR4'] = self.INSTR4
        self.INSTR5 = RM_Field_CRYPTO1_SEQ1_INSTR5(self)
        self.zz_fdict['INSTR5'] = self.INSTR5
        self.INSTR6 = RM_Field_CRYPTO1_SEQ1_INSTR6(self)
        self.zz_fdict['INSTR6'] = self.INSTR6
        self.INSTR7 = RM_Field_CRYPTO1_SEQ1_INSTR7(self)
        self.zz_fdict['INSTR7'] = self.INSTR7
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_SEQ2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_SEQ2, self).__init__(rmio, label,
            0x400f0400, 0x058,
            'SEQ2', 'CRYPTO1.SEQ2', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.INSTR8 = RM_Field_CRYPTO1_SEQ2_INSTR8(self)
        self.zz_fdict['INSTR8'] = self.INSTR8
        self.INSTR9 = RM_Field_CRYPTO1_SEQ2_INSTR9(self)
        self.zz_fdict['INSTR9'] = self.INSTR9
        self.INSTR10 = RM_Field_CRYPTO1_SEQ2_INSTR10(self)
        self.zz_fdict['INSTR10'] = self.INSTR10
        self.INSTR11 = RM_Field_CRYPTO1_SEQ2_INSTR11(self)
        self.zz_fdict['INSTR11'] = self.INSTR11
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_SEQ3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_SEQ3, self).__init__(rmio, label,
            0x400f0400, 0x05C,
            'SEQ3', 'CRYPTO1.SEQ3', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.INSTR12 = RM_Field_CRYPTO1_SEQ3_INSTR12(self)
        self.zz_fdict['INSTR12'] = self.INSTR12
        self.INSTR13 = RM_Field_CRYPTO1_SEQ3_INSTR13(self)
        self.zz_fdict['INSTR13'] = self.INSTR13
        self.INSTR14 = RM_Field_CRYPTO1_SEQ3_INSTR14(self)
        self.zz_fdict['INSTR14'] = self.INSTR14
        self.INSTR15 = RM_Field_CRYPTO1_SEQ3_INSTR15(self)
        self.zz_fdict['INSTR15'] = self.INSTR15
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_SEQ4(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_SEQ4, self).__init__(rmio, label,
            0x400f0400, 0x060,
            'SEQ4', 'CRYPTO1.SEQ4', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.INSTR16 = RM_Field_CRYPTO1_SEQ4_INSTR16(self)
        self.zz_fdict['INSTR16'] = self.INSTR16
        self.INSTR17 = RM_Field_CRYPTO1_SEQ4_INSTR17(self)
        self.zz_fdict['INSTR17'] = self.INSTR17
        self.INSTR18 = RM_Field_CRYPTO1_SEQ4_INSTR18(self)
        self.zz_fdict['INSTR18'] = self.INSTR18
        self.INSTR19 = RM_Field_CRYPTO1_SEQ4_INSTR19(self)
        self.zz_fdict['INSTR19'] = self.INSTR19
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DATA0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DATA0, self).__init__(rmio, label,
            0x400f0400, 0x080,
            'DATA0', 'CRYPTO1.DATA0', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA0 = RM_Field_CRYPTO1_DATA0_DATA0(self)
        self.zz_fdict['DATA0'] = self.DATA0
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DATA1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DATA1, self).__init__(rmio, label,
            0x400f0400, 0x084,
            'DATA1', 'CRYPTO1.DATA1', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA1 = RM_Field_CRYPTO1_DATA1_DATA1(self)
        self.zz_fdict['DATA1'] = self.DATA1
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DATA2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DATA2, self).__init__(rmio, label,
            0x400f0400, 0x088,
            'DATA2', 'CRYPTO1.DATA2', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA2 = RM_Field_CRYPTO1_DATA2_DATA2(self)
        self.zz_fdict['DATA2'] = self.DATA2
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DATA3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DATA3, self).__init__(rmio, label,
            0x400f0400, 0x08C,
            'DATA3', 'CRYPTO1.DATA3', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA3 = RM_Field_CRYPTO1_DATA3_DATA3(self)
        self.zz_fdict['DATA3'] = self.DATA3
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DATA0XOR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DATA0XOR, self).__init__(rmio, label,
            0x400f0400, 0x0A0,
            'DATA0XOR', 'CRYPTO1.DATA0XOR', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA0XOR = RM_Field_CRYPTO1_DATA0XOR_DATA0XOR(self)
        self.zz_fdict['DATA0XOR'] = self.DATA0XOR
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DATA0BYTE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DATA0BYTE, self).__init__(rmio, label,
            0x400f0400, 0x0B0,
            'DATA0BYTE', 'CRYPTO1.DATA0BYTE', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.DATA0BYTE = RM_Field_CRYPTO1_DATA0BYTE_DATA0BYTE(self)
        self.zz_fdict['DATA0BYTE'] = self.DATA0BYTE
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DATA1BYTE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DATA1BYTE, self).__init__(rmio, label,
            0x400f0400, 0x0B4,
            'DATA1BYTE', 'CRYPTO1.DATA1BYTE', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.DATA1BYTE = RM_Field_CRYPTO1_DATA1BYTE_DATA1BYTE(self)
        self.zz_fdict['DATA1BYTE'] = self.DATA1BYTE
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DATA0XORBYTE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DATA0XORBYTE, self).__init__(rmio, label,
            0x400f0400, 0x0BC,
            'DATA0XORBYTE', 'CRYPTO1.DATA0XORBYTE', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.DATA0XORBYTE = RM_Field_CRYPTO1_DATA0XORBYTE_DATA0XORBYTE(self)
        self.zz_fdict['DATA0XORBYTE'] = self.DATA0XORBYTE
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DATA0BYTE12(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DATA0BYTE12, self).__init__(rmio, label,
            0x400f0400, 0x0C0,
            'DATA0BYTE12', 'CRYPTO1.DATA0BYTE12', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.DATA0BYTE12 = RM_Field_CRYPTO1_DATA0BYTE12_DATA0BYTE12(self)
        self.zz_fdict['DATA0BYTE12'] = self.DATA0BYTE12
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DATA0BYTE13(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DATA0BYTE13, self).__init__(rmio, label,
            0x400f0400, 0x0C4,
            'DATA0BYTE13', 'CRYPTO1.DATA0BYTE13', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.DATA0BYTE13 = RM_Field_CRYPTO1_DATA0BYTE13_DATA0BYTE13(self)
        self.zz_fdict['DATA0BYTE13'] = self.DATA0BYTE13
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DATA0BYTE14(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DATA0BYTE14, self).__init__(rmio, label,
            0x400f0400, 0x0C8,
            'DATA0BYTE14', 'CRYPTO1.DATA0BYTE14', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.DATA0BYTE14 = RM_Field_CRYPTO1_DATA0BYTE14_DATA0BYTE14(self)
        self.zz_fdict['DATA0BYTE14'] = self.DATA0BYTE14
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DATA0BYTE15(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DATA0BYTE15, self).__init__(rmio, label,
            0x400f0400, 0x0CC,
            'DATA0BYTE15', 'CRYPTO1.DATA0BYTE15', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.DATA0BYTE15 = RM_Field_CRYPTO1_DATA0BYTE15_DATA0BYTE15(self)
        self.zz_fdict['DATA0BYTE15'] = self.DATA0BYTE15
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DDATA0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DDATA0, self).__init__(rmio, label,
            0x400f0400, 0x100,
            'DDATA0', 'CRYPTO1.DDATA0', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DDATA0 = RM_Field_CRYPTO1_DDATA0_DDATA0(self)
        self.zz_fdict['DDATA0'] = self.DDATA0
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DDATA1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DDATA1, self).__init__(rmio, label,
            0x400f0400, 0x104,
            'DDATA1', 'CRYPTO1.DDATA1', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DDATA1 = RM_Field_CRYPTO1_DDATA1_DDATA1(self)
        self.zz_fdict['DDATA1'] = self.DDATA1
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DDATA2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DDATA2, self).__init__(rmio, label,
            0x400f0400, 0x108,
            'DDATA2', 'CRYPTO1.DDATA2', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DDATA2 = RM_Field_CRYPTO1_DDATA2_DDATA2(self)
        self.zz_fdict['DDATA2'] = self.DDATA2
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DDATA3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DDATA3, self).__init__(rmio, label,
            0x400f0400, 0x10C,
            'DDATA3', 'CRYPTO1.DDATA3', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DDATA3 = RM_Field_CRYPTO1_DDATA3_DDATA3(self)
        self.zz_fdict['DDATA3'] = self.DDATA3
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DDATA4(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DDATA4, self).__init__(rmio, label,
            0x400f0400, 0x110,
            'DDATA4', 'CRYPTO1.DDATA4', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DDATA4 = RM_Field_CRYPTO1_DDATA4_DDATA4(self)
        self.zz_fdict['DDATA4'] = self.DDATA4
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DDATA0BIG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DDATA0BIG, self).__init__(rmio, label,
            0x400f0400, 0x130,
            'DDATA0BIG', 'CRYPTO1.DDATA0BIG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DDATA0BIG = RM_Field_CRYPTO1_DDATA0BIG_DDATA0BIG(self)
        self.zz_fdict['DDATA0BIG'] = self.DDATA0BIG
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DDATA0BYTE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DDATA0BYTE, self).__init__(rmio, label,
            0x400f0400, 0x140,
            'DDATA0BYTE', 'CRYPTO1.DDATA0BYTE', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.DDATA0BYTE = RM_Field_CRYPTO1_DDATA0BYTE_DDATA0BYTE(self)
        self.zz_fdict['DDATA0BYTE'] = self.DDATA0BYTE
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DDATA1BYTE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DDATA1BYTE, self).__init__(rmio, label,
            0x400f0400, 0x144,
            'DDATA1BYTE', 'CRYPTO1.DDATA1BYTE', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.DDATA1BYTE = RM_Field_CRYPTO1_DDATA1BYTE_DDATA1BYTE(self)
        self.zz_fdict['DDATA1BYTE'] = self.DDATA1BYTE
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_DDATA0BYTE32(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_DDATA0BYTE32, self).__init__(rmio, label,
            0x400f0400, 0x148,
            'DDATA0BYTE32', 'CRYPTO1.DDATA0BYTE32', 'read-write',
            "",
            0x00000000, 0x0000000F)

        self.DDATA0BYTE32 = RM_Field_CRYPTO1_DDATA0BYTE32_DDATA0BYTE32(self)
        self.zz_fdict['DDATA0BYTE32'] = self.DDATA0BYTE32
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_QDATA0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_QDATA0, self).__init__(rmio, label,
            0x400f0400, 0x180,
            'QDATA0', 'CRYPTO1.QDATA0', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.QDATA0 = RM_Field_CRYPTO1_QDATA0_QDATA0(self)
        self.zz_fdict['QDATA0'] = self.QDATA0
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_QDATA1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_QDATA1, self).__init__(rmio, label,
            0x400f0400, 0x184,
            'QDATA1', 'CRYPTO1.QDATA1', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.QDATA1 = RM_Field_CRYPTO1_QDATA1_QDATA1(self)
        self.zz_fdict['QDATA1'] = self.QDATA1
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_QDATA1BIG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_QDATA1BIG, self).__init__(rmio, label,
            0x400f0400, 0x1A4,
            'QDATA1BIG', 'CRYPTO1.QDATA1BIG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.QDATA1BIG = RM_Field_CRYPTO1_QDATA1BIG_QDATA1BIG(self)
        self.zz_fdict['QDATA1BIG'] = self.QDATA1BIG
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_QDATA0BYTE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_QDATA0BYTE, self).__init__(rmio, label,
            0x400f0400, 0x1C0,
            'QDATA0BYTE', 'CRYPTO1.QDATA0BYTE', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.QDATA0BYTE = RM_Field_CRYPTO1_QDATA0BYTE_QDATA0BYTE(self)
        self.zz_fdict['QDATA0BYTE'] = self.QDATA0BYTE
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_QDATA1BYTE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_QDATA1BYTE, self).__init__(rmio, label,
            0x400f0400, 0x1C4,
            'QDATA1BYTE', 'CRYPTO1.QDATA1BYTE', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.QDATA1BYTE = RM_Field_CRYPTO1_QDATA1BYTE_QDATA1BYTE(self)
        self.zz_fdict['QDATA1BYTE'] = self.QDATA1BYTE
        self.__dict__['zz_frozen'] = True


class RM_Register_CRYPTO1_FEATURE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CRYPTO1_FEATURE, self).__init__(rmio, label,
            0x400f0400, 0x1F0,
            'FEATURE', 'CRYPTO1.FEATURE', 'read-write',
            "",
            0x00000000, 0x0000FF07)

        self.AES256DIS = RM_Field_CRYPTO1_FEATURE_AES256DIS(self)
        self.zz_fdict['AES256DIS'] = self.AES256DIS
        self.SHADIS = RM_Field_CRYPTO1_FEATURE_SHADIS(self)
        self.zz_fdict['SHADIS'] = self.SHADIS
        self.MODOPDIS = RM_Field_CRYPTO1_FEATURE_MODOPDIS(self)
        self.zz_fdict['MODOPDIS'] = self.MODOPDIS
        self.ECCBIN233DIS = RM_Field_CRYPTO1_FEATURE_ECCBIN233DIS(self)
        self.zz_fdict['ECCBIN233DIS'] = self.ECCBIN233DIS
        self.ECCBIN233KDIS = RM_Field_CRYPTO1_FEATURE_ECCBIN233KDIS(self)
        self.zz_fdict['ECCBIN233KDIS'] = self.ECCBIN233KDIS
        self.ECCBIN163DIS = RM_Field_CRYPTO1_FEATURE_ECCBIN163DIS(self)
        self.zz_fdict['ECCBIN163DIS'] = self.ECCBIN163DIS
        self.ECCBIN163KDIS = RM_Field_CRYPTO1_FEATURE_ECCBIN163KDIS(self)
        self.zz_fdict['ECCBIN163KDIS'] = self.ECCBIN163KDIS
        self.GCMBIN128DIS = RM_Field_CRYPTO1_FEATURE_GCMBIN128DIS(self)
        self.zz_fdict['GCMBIN128DIS'] = self.GCMBIN128DIS
        self.ECCPRIME256DIS = RM_Field_CRYPTO1_FEATURE_ECCPRIME256DIS(self)
        self.zz_fdict['ECCPRIME256DIS'] = self.ECCPRIME256DIS
        self.ECCPRIME224DIS = RM_Field_CRYPTO1_FEATURE_ECCPRIME224DIS(self)
        self.zz_fdict['ECCPRIME224DIS'] = self.ECCPRIME224DIS
        self.ECCPRIME192DIS = RM_Field_CRYPTO1_FEATURE_ECCPRIME192DIS(self)
        self.zz_fdict['ECCPRIME192DIS'] = self.ECCPRIME192DIS
        self.__dict__['zz_frozen'] = True


