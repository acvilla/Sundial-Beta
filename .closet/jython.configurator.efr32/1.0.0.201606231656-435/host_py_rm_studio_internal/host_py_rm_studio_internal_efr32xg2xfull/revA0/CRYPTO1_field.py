
from static import Base_RM_Field
from CRYPTO1_enum import *


class RM_Field_CRYPTO1_CTRL_AES(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CTRL_AES, self).__init__(register,
            'AES', 'CRYPTO1.CTRL.AES', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CTRL_KEYBUFDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CTRL_KEYBUFDIS, self).__init__(register,
            'KEYBUFDIS', 'CRYPTO1.CTRL.KEYBUFDIS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CTRL_SHA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CTRL_SHA, self).__init__(register,
            'SHA', 'CRYPTO1.CTRL.SHA', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CTRL_READBUFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CTRL_READBUFSEL, self).__init__(register,
            'READBUFSEL', 'CRYPTO1.CTRL.READBUFSEL', 'read-write',
            "",
            4, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CTRL_WRITEBUFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CTRL_WRITEBUFSEL, self).__init__(register,
            'WRITEBUFSEL', 'CRYPTO1.CTRL.WRITEBUFSEL', 'read-write',
            "",
            7, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CTRL_NOBUSYSTALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CTRL_NOBUSYSTALL, self).__init__(register,
            'NOBUSYSTALL', 'CRYPTO1.CTRL.NOBUSYSTALL', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CTRL_DATA0TOBUFXOROW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CTRL_DATA0TOBUFXOROW, self).__init__(register,
            'DATA0TOBUFXOROW', 'CRYPTO1.CTRL.DATA0TOBUFXOROW', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CTRL_DATA1TOBUFXOROW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CTRL_DATA1TOBUFXOROW, self).__init__(register,
            'DATA1TOBUFXOROW', 'CRYPTO1.CTRL.DATA1TOBUFXOROW', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CTRL_INCWIDTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CTRL_INCWIDTH, self).__init__(register,
            'INCWIDTH', 'CRYPTO1.CTRL.INCWIDTH', 'read-write',
            "",
            14, 2,
            RM_Enum_CRYPTO1_CTRL_INCWIDTH(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CTRL_DMA0MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CTRL_DMA0MODE, self).__init__(register,
            'DMA0MODE', 'CRYPTO1.CTRL.DMA0MODE', 'read-write',
            "",
            16, 2,
            RM_Enum_CRYPTO1_CTRL_DMA0MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CTRL_DMA0RSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CTRL_DMA0RSEL, self).__init__(register,
            'DMA0RSEL', 'CRYPTO1.CTRL.DMA0RSEL', 'read-write',
            "",
            20, 2,
            RM_Enum_CRYPTO1_CTRL_DMA0RSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CTRL_DMA1MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CTRL_DMA1MODE, self).__init__(register,
            'DMA1MODE', 'CRYPTO1.CTRL.DMA1MODE', 'read-write',
            "",
            24, 2,
            RM_Enum_CRYPTO1_CTRL_DMA1MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CTRL_DMA1RSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CTRL_DMA1RSEL, self).__init__(register,
            'DMA1RSEL', 'CRYPTO1.CTRL.DMA1RSEL', 'read-write',
            "",
            28, 2,
            RM_Enum_CRYPTO1_CTRL_DMA1RSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CTRL_COMBDMA0WEREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CTRL_COMBDMA0WEREQ, self).__init__(register,
            'COMBDMA0WEREQ', 'CRYPTO1.CTRL.COMBDMA0WEREQ', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_WAC_MODULUS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_WAC_MODULUS, self).__init__(register,
            'MODULUS', 'CRYPTO1.WAC.MODULUS', 'read-write',
            "",
            0, 4,
            RM_Enum_CRYPTO1_WAC_MODULUS(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_WAC_MODOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_WAC_MODOP, self).__init__(register,
            'MODOP', 'CRYPTO1.WAC.MODOP', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_WAC_MULWIDTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_WAC_MULWIDTH, self).__init__(register,
            'MULWIDTH', 'CRYPTO1.WAC.MULWIDTH', 'read-write',
            "",
            8, 2,
            RM_Enum_CRYPTO1_WAC_MULWIDTH(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_WAC_RESULTWIDTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_WAC_RESULTWIDTH, self).__init__(register,
            'RESULTWIDTH', 'CRYPTO1.WAC.RESULTWIDTH', 'read-write',
            "",
            10, 2,
            RM_Enum_CRYPTO1_WAC_RESULTWIDTH(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CMD_INSTR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CMD_INSTR, self).__init__(register,
            'INSTR', 'CRYPTO1.CMD.INSTR', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CMD_SEQSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CMD_SEQSTART, self).__init__(register,
            'SEQSTART', 'CRYPTO1.CMD.SEQSTART', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CMD_SEQSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CMD_SEQSTOP, self).__init__(register,
            'SEQSTOP', 'CRYPTO1.CMD.SEQSTOP', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CMD_SEQSTEP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CMD_SEQSTEP, self).__init__(register,
            'SEQSTEP', 'CRYPTO1.CMD.SEQSTEP', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_STATUS_SEQRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_STATUS_SEQRUNNING, self).__init__(register,
            'SEQRUNNING', 'CRYPTO1.STATUS.SEQRUNNING', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_STATUS_INSTRRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_STATUS_INSTRRUNNING, self).__init__(register,
            'INSTRRUNNING', 'CRYPTO1.STATUS.INSTRRUNNING', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_STATUS_DMAACTIVE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_STATUS_DMAACTIVE, self).__init__(register,
            'DMAACTIVE', 'CRYPTO1.STATUS.DMAACTIVE', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_STATUS_BUFACTIVE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_STATUS_BUFACTIVE, self).__init__(register,
            'BUFACTIVE', 'CRYPTO1.STATUS.BUFACTIVE', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DSTATUS_DATA0ZERO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DSTATUS_DATA0ZERO, self).__init__(register,
            'DATA0ZERO', 'CRYPTO1.DSTATUS.DATA0ZERO', 'read-only',
            "",
            0, 4,
            RM_Enum_CRYPTO1_DSTATUS_DATA0ZERO(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DSTATUS_DDATA0LSBS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DSTATUS_DDATA0LSBS, self).__init__(register,
            'DDATA0LSBS', 'CRYPTO1.DSTATUS.DDATA0LSBS', 'read-only',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DSTATUS_DDATA0MSBS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DSTATUS_DDATA0MSBS, self).__init__(register,
            'DDATA0MSBS', 'CRYPTO1.DSTATUS.DDATA0MSBS', 'read-only',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DSTATUS_DDATA1MSB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DSTATUS_DDATA1MSB, self).__init__(register,
            'DDATA1MSB', 'CRYPTO1.DSTATUS.DDATA1MSB', 'read-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DSTATUS_CARRY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DSTATUS_CARRY, self).__init__(register,
            'CARRY', 'CRYPTO1.DSTATUS.CARRY', 'read-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CSTATUS_V0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CSTATUS_V0, self).__init__(register,
            'V0', 'CRYPTO1.CSTATUS.V0', 'read-only',
            "",
            0, 3,
            RM_Enum_CRYPTO1_CSTATUS_V0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CSTATUS_V1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CSTATUS_V1, self).__init__(register,
            'V1', 'CRYPTO1.CSTATUS.V1', 'read-only',
            "",
            8, 3,
            RM_Enum_CRYPTO1_CSTATUS_V1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CSTATUS_SEQPART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CSTATUS_SEQPART, self).__init__(register,
            'SEQPART', 'CRYPTO1.CSTATUS.SEQPART', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CSTATUS_SEQSKIP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CSTATUS_SEQSKIP, self).__init__(register,
            'SEQSKIP', 'CRYPTO1.CSTATUS.SEQSKIP', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_CSTATUS_SEQIP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_CSTATUS_SEQIP, self).__init__(register,
            'SEQIP', 'CRYPTO1.CSTATUS.SEQIP', 'read-only',
            "",
            20, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_KEY_KEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_KEY_KEY, self).__init__(register,
            'KEY', 'CRYPTO1.KEY.KEY', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_KEYBUF_KEYBUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_KEYBUF_KEYBUF, self).__init__(register,
            'KEYBUF', 'CRYPTO1.KEYBUF.KEYBUF', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQCTRL_LENGTHA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQCTRL_LENGTHA, self).__init__(register,
            'LENGTHA', 'CRYPTO1.SEQCTRL.LENGTHA', 'read-write',
            "",
            0, 14)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQCTRL_BLOCKSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQCTRL_BLOCKSIZE, self).__init__(register,
            'BLOCKSIZE', 'CRYPTO1.SEQCTRL.BLOCKSIZE', 'read-write',
            "",
            20, 2,
            RM_Enum_CRYPTO1_SEQCTRL_BLOCKSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQCTRL_DMA0SKIP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQCTRL_DMA0SKIP, self).__init__(register,
            'DMA0SKIP', 'CRYPTO1.SEQCTRL.DMA0SKIP', 'read-write',
            "",
            24, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQCTRL_DMA1SKIP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQCTRL_DMA1SKIP, self).__init__(register,
            'DMA1SKIP', 'CRYPTO1.SEQCTRL.DMA1SKIP', 'read-write',
            "",
            26, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQCTRL_DMA0PRESA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQCTRL_DMA0PRESA, self).__init__(register,
            'DMA0PRESA', 'CRYPTO1.SEQCTRL.DMA0PRESA', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQCTRL_DMA1PRESA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQCTRL_DMA1PRESA, self).__init__(register,
            'DMA1PRESA', 'CRYPTO1.SEQCTRL.DMA1PRESA', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQCTRL_HALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQCTRL_HALT, self).__init__(register,
            'HALT', 'CRYPTO1.SEQCTRL.HALT', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQCTRLB_LENGTHB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQCTRLB_LENGTHB, self).__init__(register,
            'LENGTHB', 'CRYPTO1.SEQCTRLB.LENGTHB', 'read-write',
            "",
            0, 14)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQCTRLB_DMA0PRESB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQCTRLB_DMA0PRESB, self).__init__(register,
            'DMA0PRESB', 'CRYPTO1.SEQCTRLB.DMA0PRESB', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQCTRLB_DMA1PRESB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQCTRLB_DMA1PRESB, self).__init__(register,
            'DMA1PRESB', 'CRYPTO1.SEQCTRLB.DMA1PRESB', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IF_INSTRDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IF_INSTRDONE, self).__init__(register,
            'INSTRDONE', 'CRYPTO1.IF.INSTRDONE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IF_SEQDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IF_SEQDONE, self).__init__(register,
            'SEQDONE', 'CRYPTO1.IF.SEQDONE', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IF_BUFOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IF_BUFOF, self).__init__(register,
            'BUFOF', 'CRYPTO1.IF.BUFOF', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IF_BUFUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IF_BUFUF, self).__init__(register,
            'BUFUF', 'CRYPTO1.IF.BUFUF', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IFS_INSTRDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IFS_INSTRDONE, self).__init__(register,
            'INSTRDONE', 'CRYPTO1.IFS.INSTRDONE', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IFS_SEQDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IFS_SEQDONE, self).__init__(register,
            'SEQDONE', 'CRYPTO1.IFS.SEQDONE', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IFS_BUFOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IFS_BUFOF, self).__init__(register,
            'BUFOF', 'CRYPTO1.IFS.BUFOF', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IFS_BUFUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IFS_BUFUF, self).__init__(register,
            'BUFUF', 'CRYPTO1.IFS.BUFUF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IFC_INSTRDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IFC_INSTRDONE, self).__init__(register,
            'INSTRDONE', 'CRYPTO1.IFC.INSTRDONE', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IFC_SEQDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IFC_SEQDONE, self).__init__(register,
            'SEQDONE', 'CRYPTO1.IFC.SEQDONE', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IFC_BUFOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IFC_BUFOF, self).__init__(register,
            'BUFOF', 'CRYPTO1.IFC.BUFOF', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IFC_BUFUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IFC_BUFUF, self).__init__(register,
            'BUFUF', 'CRYPTO1.IFC.BUFUF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IEN_INSTRDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IEN_INSTRDONE, self).__init__(register,
            'INSTRDONE', 'CRYPTO1.IEN.INSTRDONE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IEN_SEQDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IEN_SEQDONE, self).__init__(register,
            'SEQDONE', 'CRYPTO1.IEN.SEQDONE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IEN_BUFOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IEN_BUFOF, self).__init__(register,
            'BUFOF', 'CRYPTO1.IEN.BUFOF', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_IEN_BUFUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_IEN_BUFUF, self).__init__(register,
            'BUFUF', 'CRYPTO1.IEN.BUFUF', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ0_INSTR0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ0_INSTR0, self).__init__(register,
            'INSTR0', 'CRYPTO1.SEQ0.INSTR0', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ0_INSTR1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ0_INSTR1, self).__init__(register,
            'INSTR1', 'CRYPTO1.SEQ0.INSTR1', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ0_INSTR2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ0_INSTR2, self).__init__(register,
            'INSTR2', 'CRYPTO1.SEQ0.INSTR2', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ0_INSTR3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ0_INSTR3, self).__init__(register,
            'INSTR3', 'CRYPTO1.SEQ0.INSTR3', 'read-write',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ1_INSTR4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ1_INSTR4, self).__init__(register,
            'INSTR4', 'CRYPTO1.SEQ1.INSTR4', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ1_INSTR5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ1_INSTR5, self).__init__(register,
            'INSTR5', 'CRYPTO1.SEQ1.INSTR5', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ1_INSTR6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ1_INSTR6, self).__init__(register,
            'INSTR6', 'CRYPTO1.SEQ1.INSTR6', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ1_INSTR7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ1_INSTR7, self).__init__(register,
            'INSTR7', 'CRYPTO1.SEQ1.INSTR7', 'read-write',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ2_INSTR8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ2_INSTR8, self).__init__(register,
            'INSTR8', 'CRYPTO1.SEQ2.INSTR8', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ2_INSTR9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ2_INSTR9, self).__init__(register,
            'INSTR9', 'CRYPTO1.SEQ2.INSTR9', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ2_INSTR10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ2_INSTR10, self).__init__(register,
            'INSTR10', 'CRYPTO1.SEQ2.INSTR10', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ2_INSTR11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ2_INSTR11, self).__init__(register,
            'INSTR11', 'CRYPTO1.SEQ2.INSTR11', 'read-write',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ3_INSTR12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ3_INSTR12, self).__init__(register,
            'INSTR12', 'CRYPTO1.SEQ3.INSTR12', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ3_INSTR13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ3_INSTR13, self).__init__(register,
            'INSTR13', 'CRYPTO1.SEQ3.INSTR13', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ3_INSTR14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ3_INSTR14, self).__init__(register,
            'INSTR14', 'CRYPTO1.SEQ3.INSTR14', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ3_INSTR15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ3_INSTR15, self).__init__(register,
            'INSTR15', 'CRYPTO1.SEQ3.INSTR15', 'read-write',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ4_INSTR16(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ4_INSTR16, self).__init__(register,
            'INSTR16', 'CRYPTO1.SEQ4.INSTR16', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ4_INSTR17(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ4_INSTR17, self).__init__(register,
            'INSTR17', 'CRYPTO1.SEQ4.INSTR17', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ4_INSTR18(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ4_INSTR18, self).__init__(register,
            'INSTR18', 'CRYPTO1.SEQ4.INSTR18', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_SEQ4_INSTR19(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_SEQ4_INSTR19, self).__init__(register,
            'INSTR19', 'CRYPTO1.SEQ4.INSTR19', 'read-write',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DATA0_DATA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DATA0_DATA0, self).__init__(register,
            'DATA0', 'CRYPTO1.DATA0.DATA0', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DATA1_DATA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DATA1_DATA1, self).__init__(register,
            'DATA1', 'CRYPTO1.DATA1.DATA1', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DATA2_DATA2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DATA2_DATA2, self).__init__(register,
            'DATA2', 'CRYPTO1.DATA2.DATA2', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DATA3_DATA3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DATA3_DATA3, self).__init__(register,
            'DATA3', 'CRYPTO1.DATA3.DATA3', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DATA0XOR_DATA0XOR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DATA0XOR_DATA0XOR, self).__init__(register,
            'DATA0XOR', 'CRYPTO1.DATA0XOR.DATA0XOR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DATA0BYTE_DATA0BYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DATA0BYTE_DATA0BYTE, self).__init__(register,
            'DATA0BYTE', 'CRYPTO1.DATA0BYTE.DATA0BYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DATA1BYTE_DATA1BYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DATA1BYTE_DATA1BYTE, self).__init__(register,
            'DATA1BYTE', 'CRYPTO1.DATA1BYTE.DATA1BYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DATA0XORBYTE_DATA0XORBYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DATA0XORBYTE_DATA0XORBYTE, self).__init__(register,
            'DATA0XORBYTE', 'CRYPTO1.DATA0XORBYTE.DATA0XORBYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DATA0BYTE12_DATA0BYTE12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DATA0BYTE12_DATA0BYTE12, self).__init__(register,
            'DATA0BYTE12', 'CRYPTO1.DATA0BYTE12.DATA0BYTE12', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DATA0BYTE13_DATA0BYTE13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DATA0BYTE13_DATA0BYTE13, self).__init__(register,
            'DATA0BYTE13', 'CRYPTO1.DATA0BYTE13.DATA0BYTE13', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DATA0BYTE14_DATA0BYTE14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DATA0BYTE14_DATA0BYTE14, self).__init__(register,
            'DATA0BYTE14', 'CRYPTO1.DATA0BYTE14.DATA0BYTE14', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DATA0BYTE15_DATA0BYTE15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DATA0BYTE15_DATA0BYTE15, self).__init__(register,
            'DATA0BYTE15', 'CRYPTO1.DATA0BYTE15.DATA0BYTE15', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DDATA0_DDATA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DDATA0_DDATA0, self).__init__(register,
            'DDATA0', 'CRYPTO1.DDATA0.DDATA0', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DDATA1_DDATA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DDATA1_DDATA1, self).__init__(register,
            'DDATA1', 'CRYPTO1.DDATA1.DDATA1', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DDATA2_DDATA2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DDATA2_DDATA2, self).__init__(register,
            'DDATA2', 'CRYPTO1.DDATA2.DDATA2', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DDATA3_DDATA3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DDATA3_DDATA3, self).__init__(register,
            'DDATA3', 'CRYPTO1.DDATA3.DDATA3', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DDATA4_DDATA4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DDATA4_DDATA4, self).__init__(register,
            'DDATA4', 'CRYPTO1.DDATA4.DDATA4', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DDATA0BIG_DDATA0BIG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DDATA0BIG_DDATA0BIG, self).__init__(register,
            'DDATA0BIG', 'CRYPTO1.DDATA0BIG.DDATA0BIG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DDATA0BYTE_DDATA0BYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DDATA0BYTE_DDATA0BYTE, self).__init__(register,
            'DDATA0BYTE', 'CRYPTO1.DDATA0BYTE.DDATA0BYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DDATA1BYTE_DDATA1BYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DDATA1BYTE_DDATA1BYTE, self).__init__(register,
            'DDATA1BYTE', 'CRYPTO1.DDATA1BYTE.DDATA1BYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_DDATA0BYTE32_DDATA0BYTE32(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_DDATA0BYTE32_DDATA0BYTE32, self).__init__(register,
            'DDATA0BYTE32', 'CRYPTO1.DDATA0BYTE32.DDATA0BYTE32', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_QDATA0_QDATA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_QDATA0_QDATA0, self).__init__(register,
            'QDATA0', 'CRYPTO1.QDATA0.QDATA0', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_QDATA1_QDATA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_QDATA1_QDATA1, self).__init__(register,
            'QDATA1', 'CRYPTO1.QDATA1.QDATA1', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_QDATA1BIG_QDATA1BIG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_QDATA1BIG_QDATA1BIG, self).__init__(register,
            'QDATA1BIG', 'CRYPTO1.QDATA1BIG.QDATA1BIG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_QDATA0BYTE_QDATA0BYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_QDATA0BYTE_QDATA0BYTE, self).__init__(register,
            'QDATA0BYTE', 'CRYPTO1.QDATA0BYTE.QDATA0BYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_QDATA1BYTE_QDATA1BYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_QDATA1BYTE_QDATA1BYTE, self).__init__(register,
            'QDATA1BYTE', 'CRYPTO1.QDATA1BYTE.QDATA1BYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_FEATURE_AES256DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_FEATURE_AES256DIS, self).__init__(register,
            'AES256DIS', 'CRYPTO1.FEATURE.AES256DIS', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_FEATURE_SHADIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_FEATURE_SHADIS, self).__init__(register,
            'SHADIS', 'CRYPTO1.FEATURE.SHADIS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_FEATURE_MODOPDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_FEATURE_MODOPDIS, self).__init__(register,
            'MODOPDIS', 'CRYPTO1.FEATURE.MODOPDIS', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_FEATURE_ECCBIN233DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_FEATURE_ECCBIN233DIS, self).__init__(register,
            'ECCBIN233DIS', 'CRYPTO1.FEATURE.ECCBIN233DIS', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_FEATURE_ECCBIN233KDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_FEATURE_ECCBIN233KDIS, self).__init__(register,
            'ECCBIN233KDIS', 'CRYPTO1.FEATURE.ECCBIN233KDIS', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_FEATURE_ECCBIN163DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_FEATURE_ECCBIN163DIS, self).__init__(register,
            'ECCBIN163DIS', 'CRYPTO1.FEATURE.ECCBIN163DIS', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_FEATURE_ECCBIN163KDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_FEATURE_ECCBIN163KDIS, self).__init__(register,
            'ECCBIN163KDIS', 'CRYPTO1.FEATURE.ECCBIN163KDIS', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_FEATURE_GCMBIN128DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_FEATURE_GCMBIN128DIS, self).__init__(register,
            'GCMBIN128DIS', 'CRYPTO1.FEATURE.GCMBIN128DIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_FEATURE_ECCPRIME256DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_FEATURE_ECCPRIME256DIS, self).__init__(register,
            'ECCPRIME256DIS', 'CRYPTO1.FEATURE.ECCPRIME256DIS', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_FEATURE_ECCPRIME224DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_FEATURE_ECCPRIME224DIS, self).__init__(register,
            'ECCPRIME224DIS', 'CRYPTO1.FEATURE.ECCPRIME224DIS', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO1_FEATURE_ECCPRIME192DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO1_FEATURE_ECCPRIME192DIS, self).__init__(register,
            'ECCPRIME192DIS', 'CRYPTO1.FEATURE.ECCPRIME192DIS', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


