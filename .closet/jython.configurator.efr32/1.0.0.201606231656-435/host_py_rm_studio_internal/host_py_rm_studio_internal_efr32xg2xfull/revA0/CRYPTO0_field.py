
from static import Base_RM_Field
from CRYPTO0_enum import *


class RM_Field_CRYPTO0_CTRL_AES(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CTRL_AES, self).__init__(register,
            'AES', 'CRYPTO0.CTRL.AES', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CTRL_KEYBUFDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CTRL_KEYBUFDIS, self).__init__(register,
            'KEYBUFDIS', 'CRYPTO0.CTRL.KEYBUFDIS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CTRL_SHA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CTRL_SHA, self).__init__(register,
            'SHA', 'CRYPTO0.CTRL.SHA', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CTRL_READBUFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CTRL_READBUFSEL, self).__init__(register,
            'READBUFSEL', 'CRYPTO0.CTRL.READBUFSEL', 'read-write',
            "",
            4, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CTRL_WRITEBUFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CTRL_WRITEBUFSEL, self).__init__(register,
            'WRITEBUFSEL', 'CRYPTO0.CTRL.WRITEBUFSEL', 'read-write',
            "",
            7, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CTRL_NOBUSYSTALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CTRL_NOBUSYSTALL, self).__init__(register,
            'NOBUSYSTALL', 'CRYPTO0.CTRL.NOBUSYSTALL', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CTRL_DATA0TOBUFXOROW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CTRL_DATA0TOBUFXOROW, self).__init__(register,
            'DATA0TOBUFXOROW', 'CRYPTO0.CTRL.DATA0TOBUFXOROW', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CTRL_DATA1TOBUFXOROW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CTRL_DATA1TOBUFXOROW, self).__init__(register,
            'DATA1TOBUFXOROW', 'CRYPTO0.CTRL.DATA1TOBUFXOROW', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CTRL_INCWIDTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CTRL_INCWIDTH, self).__init__(register,
            'INCWIDTH', 'CRYPTO0.CTRL.INCWIDTH', 'read-write',
            "",
            14, 2,
            RM_Enum_CRYPTO0_CTRL_INCWIDTH(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CTRL_DMA0MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CTRL_DMA0MODE, self).__init__(register,
            'DMA0MODE', 'CRYPTO0.CTRL.DMA0MODE', 'read-write',
            "",
            16, 2,
            RM_Enum_CRYPTO0_CTRL_DMA0MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CTRL_DMA0RSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CTRL_DMA0RSEL, self).__init__(register,
            'DMA0RSEL', 'CRYPTO0.CTRL.DMA0RSEL', 'read-write',
            "",
            20, 2,
            RM_Enum_CRYPTO0_CTRL_DMA0RSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CTRL_DMA1MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CTRL_DMA1MODE, self).__init__(register,
            'DMA1MODE', 'CRYPTO0.CTRL.DMA1MODE', 'read-write',
            "",
            24, 2,
            RM_Enum_CRYPTO0_CTRL_DMA1MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CTRL_DMA1RSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CTRL_DMA1RSEL, self).__init__(register,
            'DMA1RSEL', 'CRYPTO0.CTRL.DMA1RSEL', 'read-write',
            "",
            28, 2,
            RM_Enum_CRYPTO0_CTRL_DMA1RSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CTRL_COMBDMA0WEREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CTRL_COMBDMA0WEREQ, self).__init__(register,
            'COMBDMA0WEREQ', 'CRYPTO0.CTRL.COMBDMA0WEREQ', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_WAC_MODULUS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_WAC_MODULUS, self).__init__(register,
            'MODULUS', 'CRYPTO0.WAC.MODULUS', 'read-write',
            "",
            0, 4,
            RM_Enum_CRYPTO0_WAC_MODULUS(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_WAC_MODOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_WAC_MODOP, self).__init__(register,
            'MODOP', 'CRYPTO0.WAC.MODOP', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_WAC_MULWIDTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_WAC_MULWIDTH, self).__init__(register,
            'MULWIDTH', 'CRYPTO0.WAC.MULWIDTH', 'read-write',
            "",
            8, 2,
            RM_Enum_CRYPTO0_WAC_MULWIDTH(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_WAC_RESULTWIDTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_WAC_RESULTWIDTH, self).__init__(register,
            'RESULTWIDTH', 'CRYPTO0.WAC.RESULTWIDTH', 'read-write',
            "",
            10, 2,
            RM_Enum_CRYPTO0_WAC_RESULTWIDTH(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CMD_INSTR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CMD_INSTR, self).__init__(register,
            'INSTR', 'CRYPTO0.CMD.INSTR', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CMD_SEQSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CMD_SEQSTART, self).__init__(register,
            'SEQSTART', 'CRYPTO0.CMD.SEQSTART', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CMD_SEQSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CMD_SEQSTOP, self).__init__(register,
            'SEQSTOP', 'CRYPTO0.CMD.SEQSTOP', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CMD_SEQSTEP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CMD_SEQSTEP, self).__init__(register,
            'SEQSTEP', 'CRYPTO0.CMD.SEQSTEP', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_STATUS_SEQRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_STATUS_SEQRUNNING, self).__init__(register,
            'SEQRUNNING', 'CRYPTO0.STATUS.SEQRUNNING', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_STATUS_INSTRRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_STATUS_INSTRRUNNING, self).__init__(register,
            'INSTRRUNNING', 'CRYPTO0.STATUS.INSTRRUNNING', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_STATUS_DMAACTIVE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_STATUS_DMAACTIVE, self).__init__(register,
            'DMAACTIVE', 'CRYPTO0.STATUS.DMAACTIVE', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_STATUS_BUFACTIVE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_STATUS_BUFACTIVE, self).__init__(register,
            'BUFACTIVE', 'CRYPTO0.STATUS.BUFACTIVE', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DSTATUS_DATA0ZERO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DSTATUS_DATA0ZERO, self).__init__(register,
            'DATA0ZERO', 'CRYPTO0.DSTATUS.DATA0ZERO', 'read-only',
            "",
            0, 4,
            RM_Enum_CRYPTO0_DSTATUS_DATA0ZERO(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DSTATUS_DDATA0LSBS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DSTATUS_DDATA0LSBS, self).__init__(register,
            'DDATA0LSBS', 'CRYPTO0.DSTATUS.DDATA0LSBS', 'read-only',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DSTATUS_DDATA0MSBS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DSTATUS_DDATA0MSBS, self).__init__(register,
            'DDATA0MSBS', 'CRYPTO0.DSTATUS.DDATA0MSBS', 'read-only',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DSTATUS_DDATA1MSB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DSTATUS_DDATA1MSB, self).__init__(register,
            'DDATA1MSB', 'CRYPTO0.DSTATUS.DDATA1MSB', 'read-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DSTATUS_CARRY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DSTATUS_CARRY, self).__init__(register,
            'CARRY', 'CRYPTO0.DSTATUS.CARRY', 'read-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CSTATUS_V0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CSTATUS_V0, self).__init__(register,
            'V0', 'CRYPTO0.CSTATUS.V0', 'read-only',
            "",
            0, 3,
            RM_Enum_CRYPTO0_CSTATUS_V0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CSTATUS_V1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CSTATUS_V1, self).__init__(register,
            'V1', 'CRYPTO0.CSTATUS.V1', 'read-only',
            "",
            8, 3,
            RM_Enum_CRYPTO0_CSTATUS_V1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CSTATUS_SEQPART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CSTATUS_SEQPART, self).__init__(register,
            'SEQPART', 'CRYPTO0.CSTATUS.SEQPART', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CSTATUS_SEQSKIP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CSTATUS_SEQSKIP, self).__init__(register,
            'SEQSKIP', 'CRYPTO0.CSTATUS.SEQSKIP', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_CSTATUS_SEQIP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_CSTATUS_SEQIP, self).__init__(register,
            'SEQIP', 'CRYPTO0.CSTATUS.SEQIP', 'read-only',
            "",
            20, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_KEY_KEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_KEY_KEY, self).__init__(register,
            'KEY', 'CRYPTO0.KEY.KEY', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_KEYBUF_KEYBUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_KEYBUF_KEYBUF, self).__init__(register,
            'KEYBUF', 'CRYPTO0.KEYBUF.KEYBUF', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQCTRL_LENGTHA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQCTRL_LENGTHA, self).__init__(register,
            'LENGTHA', 'CRYPTO0.SEQCTRL.LENGTHA', 'read-write',
            "",
            0, 14)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQCTRL_BLOCKSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQCTRL_BLOCKSIZE, self).__init__(register,
            'BLOCKSIZE', 'CRYPTO0.SEQCTRL.BLOCKSIZE', 'read-write',
            "",
            20, 2,
            RM_Enum_CRYPTO0_SEQCTRL_BLOCKSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQCTRL_DMA0SKIP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQCTRL_DMA0SKIP, self).__init__(register,
            'DMA0SKIP', 'CRYPTO0.SEQCTRL.DMA0SKIP', 'read-write',
            "",
            24, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQCTRL_DMA1SKIP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQCTRL_DMA1SKIP, self).__init__(register,
            'DMA1SKIP', 'CRYPTO0.SEQCTRL.DMA1SKIP', 'read-write',
            "",
            26, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQCTRL_DMA0PRESA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQCTRL_DMA0PRESA, self).__init__(register,
            'DMA0PRESA', 'CRYPTO0.SEQCTRL.DMA0PRESA', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQCTRL_DMA1PRESA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQCTRL_DMA1PRESA, self).__init__(register,
            'DMA1PRESA', 'CRYPTO0.SEQCTRL.DMA1PRESA', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQCTRL_HALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQCTRL_HALT, self).__init__(register,
            'HALT', 'CRYPTO0.SEQCTRL.HALT', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQCTRLB_LENGTHB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQCTRLB_LENGTHB, self).__init__(register,
            'LENGTHB', 'CRYPTO0.SEQCTRLB.LENGTHB', 'read-write',
            "",
            0, 14)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQCTRLB_DMA0PRESB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQCTRLB_DMA0PRESB, self).__init__(register,
            'DMA0PRESB', 'CRYPTO0.SEQCTRLB.DMA0PRESB', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQCTRLB_DMA1PRESB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQCTRLB_DMA1PRESB, self).__init__(register,
            'DMA1PRESB', 'CRYPTO0.SEQCTRLB.DMA1PRESB', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IF_INSTRDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IF_INSTRDONE, self).__init__(register,
            'INSTRDONE', 'CRYPTO0.IF.INSTRDONE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IF_SEQDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IF_SEQDONE, self).__init__(register,
            'SEQDONE', 'CRYPTO0.IF.SEQDONE', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IF_BUFOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IF_BUFOF, self).__init__(register,
            'BUFOF', 'CRYPTO0.IF.BUFOF', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IF_BUFUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IF_BUFUF, self).__init__(register,
            'BUFUF', 'CRYPTO0.IF.BUFUF', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IFS_INSTRDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IFS_INSTRDONE, self).__init__(register,
            'INSTRDONE', 'CRYPTO0.IFS.INSTRDONE', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IFS_SEQDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IFS_SEQDONE, self).__init__(register,
            'SEQDONE', 'CRYPTO0.IFS.SEQDONE', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IFS_BUFOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IFS_BUFOF, self).__init__(register,
            'BUFOF', 'CRYPTO0.IFS.BUFOF', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IFS_BUFUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IFS_BUFUF, self).__init__(register,
            'BUFUF', 'CRYPTO0.IFS.BUFUF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IFC_INSTRDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IFC_INSTRDONE, self).__init__(register,
            'INSTRDONE', 'CRYPTO0.IFC.INSTRDONE', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IFC_SEQDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IFC_SEQDONE, self).__init__(register,
            'SEQDONE', 'CRYPTO0.IFC.SEQDONE', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IFC_BUFOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IFC_BUFOF, self).__init__(register,
            'BUFOF', 'CRYPTO0.IFC.BUFOF', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IFC_BUFUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IFC_BUFUF, self).__init__(register,
            'BUFUF', 'CRYPTO0.IFC.BUFUF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IEN_INSTRDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IEN_INSTRDONE, self).__init__(register,
            'INSTRDONE', 'CRYPTO0.IEN.INSTRDONE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IEN_SEQDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IEN_SEQDONE, self).__init__(register,
            'SEQDONE', 'CRYPTO0.IEN.SEQDONE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IEN_BUFOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IEN_BUFOF, self).__init__(register,
            'BUFOF', 'CRYPTO0.IEN.BUFOF', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_IEN_BUFUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_IEN_BUFUF, self).__init__(register,
            'BUFUF', 'CRYPTO0.IEN.BUFUF', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ0_INSTR0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ0_INSTR0, self).__init__(register,
            'INSTR0', 'CRYPTO0.SEQ0.INSTR0', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ0_INSTR1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ0_INSTR1, self).__init__(register,
            'INSTR1', 'CRYPTO0.SEQ0.INSTR1', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ0_INSTR2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ0_INSTR2, self).__init__(register,
            'INSTR2', 'CRYPTO0.SEQ0.INSTR2', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ0_INSTR3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ0_INSTR3, self).__init__(register,
            'INSTR3', 'CRYPTO0.SEQ0.INSTR3', 'read-write',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ1_INSTR4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ1_INSTR4, self).__init__(register,
            'INSTR4', 'CRYPTO0.SEQ1.INSTR4', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ1_INSTR5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ1_INSTR5, self).__init__(register,
            'INSTR5', 'CRYPTO0.SEQ1.INSTR5', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ1_INSTR6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ1_INSTR6, self).__init__(register,
            'INSTR6', 'CRYPTO0.SEQ1.INSTR6', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ1_INSTR7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ1_INSTR7, self).__init__(register,
            'INSTR7', 'CRYPTO0.SEQ1.INSTR7', 'read-write',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ2_INSTR8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ2_INSTR8, self).__init__(register,
            'INSTR8', 'CRYPTO0.SEQ2.INSTR8', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ2_INSTR9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ2_INSTR9, self).__init__(register,
            'INSTR9', 'CRYPTO0.SEQ2.INSTR9', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ2_INSTR10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ2_INSTR10, self).__init__(register,
            'INSTR10', 'CRYPTO0.SEQ2.INSTR10', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ2_INSTR11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ2_INSTR11, self).__init__(register,
            'INSTR11', 'CRYPTO0.SEQ2.INSTR11', 'read-write',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ3_INSTR12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ3_INSTR12, self).__init__(register,
            'INSTR12', 'CRYPTO0.SEQ3.INSTR12', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ3_INSTR13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ3_INSTR13, self).__init__(register,
            'INSTR13', 'CRYPTO0.SEQ3.INSTR13', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ3_INSTR14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ3_INSTR14, self).__init__(register,
            'INSTR14', 'CRYPTO0.SEQ3.INSTR14', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ3_INSTR15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ3_INSTR15, self).__init__(register,
            'INSTR15', 'CRYPTO0.SEQ3.INSTR15', 'read-write',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ4_INSTR16(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ4_INSTR16, self).__init__(register,
            'INSTR16', 'CRYPTO0.SEQ4.INSTR16', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ4_INSTR17(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ4_INSTR17, self).__init__(register,
            'INSTR17', 'CRYPTO0.SEQ4.INSTR17', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ4_INSTR18(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ4_INSTR18, self).__init__(register,
            'INSTR18', 'CRYPTO0.SEQ4.INSTR18', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_SEQ4_INSTR19(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_SEQ4_INSTR19, self).__init__(register,
            'INSTR19', 'CRYPTO0.SEQ4.INSTR19', 'read-write',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DATA0_DATA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DATA0_DATA0, self).__init__(register,
            'DATA0', 'CRYPTO0.DATA0.DATA0', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DATA1_DATA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DATA1_DATA1, self).__init__(register,
            'DATA1', 'CRYPTO0.DATA1.DATA1', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DATA2_DATA2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DATA2_DATA2, self).__init__(register,
            'DATA2', 'CRYPTO0.DATA2.DATA2', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DATA3_DATA3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DATA3_DATA3, self).__init__(register,
            'DATA3', 'CRYPTO0.DATA3.DATA3', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DATA0XOR_DATA0XOR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DATA0XOR_DATA0XOR, self).__init__(register,
            'DATA0XOR', 'CRYPTO0.DATA0XOR.DATA0XOR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DATA0BYTE_DATA0BYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DATA0BYTE_DATA0BYTE, self).__init__(register,
            'DATA0BYTE', 'CRYPTO0.DATA0BYTE.DATA0BYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DATA1BYTE_DATA1BYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DATA1BYTE_DATA1BYTE, self).__init__(register,
            'DATA1BYTE', 'CRYPTO0.DATA1BYTE.DATA1BYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DATA0XORBYTE_DATA0XORBYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DATA0XORBYTE_DATA0XORBYTE, self).__init__(register,
            'DATA0XORBYTE', 'CRYPTO0.DATA0XORBYTE.DATA0XORBYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DATA0BYTE12_DATA0BYTE12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DATA0BYTE12_DATA0BYTE12, self).__init__(register,
            'DATA0BYTE12', 'CRYPTO0.DATA0BYTE12.DATA0BYTE12', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DATA0BYTE13_DATA0BYTE13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DATA0BYTE13_DATA0BYTE13, self).__init__(register,
            'DATA0BYTE13', 'CRYPTO0.DATA0BYTE13.DATA0BYTE13', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DATA0BYTE14_DATA0BYTE14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DATA0BYTE14_DATA0BYTE14, self).__init__(register,
            'DATA0BYTE14', 'CRYPTO0.DATA0BYTE14.DATA0BYTE14', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DATA0BYTE15_DATA0BYTE15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DATA0BYTE15_DATA0BYTE15, self).__init__(register,
            'DATA0BYTE15', 'CRYPTO0.DATA0BYTE15.DATA0BYTE15', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DDATA0_DDATA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DDATA0_DDATA0, self).__init__(register,
            'DDATA0', 'CRYPTO0.DDATA0.DDATA0', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DDATA1_DDATA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DDATA1_DDATA1, self).__init__(register,
            'DDATA1', 'CRYPTO0.DDATA1.DDATA1', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DDATA2_DDATA2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DDATA2_DDATA2, self).__init__(register,
            'DDATA2', 'CRYPTO0.DDATA2.DDATA2', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DDATA3_DDATA3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DDATA3_DDATA3, self).__init__(register,
            'DDATA3', 'CRYPTO0.DDATA3.DDATA3', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DDATA4_DDATA4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DDATA4_DDATA4, self).__init__(register,
            'DDATA4', 'CRYPTO0.DDATA4.DDATA4', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DDATA0BIG_DDATA0BIG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DDATA0BIG_DDATA0BIG, self).__init__(register,
            'DDATA0BIG', 'CRYPTO0.DDATA0BIG.DDATA0BIG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DDATA0BYTE_DDATA0BYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DDATA0BYTE_DDATA0BYTE, self).__init__(register,
            'DDATA0BYTE', 'CRYPTO0.DDATA0BYTE.DDATA0BYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DDATA1BYTE_DDATA1BYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DDATA1BYTE_DDATA1BYTE, self).__init__(register,
            'DDATA1BYTE', 'CRYPTO0.DDATA1BYTE.DDATA1BYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_DDATA0BYTE32_DDATA0BYTE32(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_DDATA0BYTE32_DDATA0BYTE32, self).__init__(register,
            'DDATA0BYTE32', 'CRYPTO0.DDATA0BYTE32.DDATA0BYTE32', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_QDATA0_QDATA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_QDATA0_QDATA0, self).__init__(register,
            'QDATA0', 'CRYPTO0.QDATA0.QDATA0', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_QDATA1_QDATA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_QDATA1_QDATA1, self).__init__(register,
            'QDATA1', 'CRYPTO0.QDATA1.QDATA1', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_QDATA1BIG_QDATA1BIG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_QDATA1BIG_QDATA1BIG, self).__init__(register,
            'QDATA1BIG', 'CRYPTO0.QDATA1BIG.QDATA1BIG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_QDATA0BYTE_QDATA0BYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_QDATA0BYTE_QDATA0BYTE, self).__init__(register,
            'QDATA0BYTE', 'CRYPTO0.QDATA0BYTE.QDATA0BYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_QDATA1BYTE_QDATA1BYTE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_QDATA1BYTE_QDATA1BYTE, self).__init__(register,
            'QDATA1BYTE', 'CRYPTO0.QDATA1BYTE.QDATA1BYTE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_FEATURE_AES256DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_FEATURE_AES256DIS, self).__init__(register,
            'AES256DIS', 'CRYPTO0.FEATURE.AES256DIS', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_FEATURE_SHADIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_FEATURE_SHADIS, self).__init__(register,
            'SHADIS', 'CRYPTO0.FEATURE.SHADIS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_FEATURE_MODOPDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_FEATURE_MODOPDIS, self).__init__(register,
            'MODOPDIS', 'CRYPTO0.FEATURE.MODOPDIS', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_FEATURE_ECCBIN233DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_FEATURE_ECCBIN233DIS, self).__init__(register,
            'ECCBIN233DIS', 'CRYPTO0.FEATURE.ECCBIN233DIS', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_FEATURE_ECCBIN233KDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_FEATURE_ECCBIN233KDIS, self).__init__(register,
            'ECCBIN233KDIS', 'CRYPTO0.FEATURE.ECCBIN233KDIS', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_FEATURE_ECCBIN163DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_FEATURE_ECCBIN163DIS, self).__init__(register,
            'ECCBIN163DIS', 'CRYPTO0.FEATURE.ECCBIN163DIS', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_FEATURE_ECCBIN163KDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_FEATURE_ECCBIN163KDIS, self).__init__(register,
            'ECCBIN163KDIS', 'CRYPTO0.FEATURE.ECCBIN163KDIS', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_FEATURE_GCMBIN128DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_FEATURE_GCMBIN128DIS, self).__init__(register,
            'GCMBIN128DIS', 'CRYPTO0.FEATURE.GCMBIN128DIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_FEATURE_ECCPRIME256DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_FEATURE_ECCPRIME256DIS, self).__init__(register,
            'ECCPRIME256DIS', 'CRYPTO0.FEATURE.ECCPRIME256DIS', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_FEATURE_ECCPRIME224DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_FEATURE_ECCPRIME224DIS, self).__init__(register,
            'ECCPRIME224DIS', 'CRYPTO0.FEATURE.ECCPRIME224DIS', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CRYPTO0_FEATURE_ECCPRIME192DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CRYPTO0_FEATURE_ECCPRIME192DIS, self).__init__(register,
            'ECCPRIME192DIS', 'CRYPTO0.FEATURE.ECCPRIME192DIS', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


