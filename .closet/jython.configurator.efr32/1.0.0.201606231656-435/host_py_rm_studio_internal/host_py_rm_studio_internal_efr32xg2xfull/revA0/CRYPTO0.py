
__all__ = [ 'RM_Peripheral_CRYPTO0' ]

from static import Base_RM_Peripheral
from CRYPTO0_register import *

class RM_Peripheral_CRYPTO0(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_CRYPTO0, self).__init__(rmio, label,
            0x400F0000, 'CRYPTO0',
            "")
        self.CTRL = RM_Register_CRYPTO0_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.WAC = RM_Register_CRYPTO0_WAC(self.zz_rmio, self.zz_label)
        self.zz_rdict['WAC'] = self.WAC
        self.CMD = RM_Register_CRYPTO0_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.STATUS = RM_Register_CRYPTO0_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.DSTATUS = RM_Register_CRYPTO0_DSTATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['DSTATUS'] = self.DSTATUS
        self.CSTATUS = RM_Register_CRYPTO0_CSTATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['CSTATUS'] = self.CSTATUS
        self.KEY = RM_Register_CRYPTO0_KEY(self.zz_rmio, self.zz_label)
        self.zz_rdict['KEY'] = self.KEY
        self.KEYBUF = RM_Register_CRYPTO0_KEYBUF(self.zz_rmio, self.zz_label)
        self.zz_rdict['KEYBUF'] = self.KEYBUF
        self.SEQCTRL = RM_Register_CRYPTO0_SEQCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['SEQCTRL'] = self.SEQCTRL
        self.SEQCTRLB = RM_Register_CRYPTO0_SEQCTRLB(self.zz_rmio, self.zz_label)
        self.zz_rdict['SEQCTRLB'] = self.SEQCTRLB
        self.IF = RM_Register_CRYPTO0_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_CRYPTO0_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_CRYPTO0_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_CRYPTO0_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.SEQ0 = RM_Register_CRYPTO0_SEQ0(self.zz_rmio, self.zz_label)
        self.zz_rdict['SEQ0'] = self.SEQ0
        self.SEQ1 = RM_Register_CRYPTO0_SEQ1(self.zz_rmio, self.zz_label)
        self.zz_rdict['SEQ1'] = self.SEQ1
        self.SEQ2 = RM_Register_CRYPTO0_SEQ2(self.zz_rmio, self.zz_label)
        self.zz_rdict['SEQ2'] = self.SEQ2
        self.SEQ3 = RM_Register_CRYPTO0_SEQ3(self.zz_rmio, self.zz_label)
        self.zz_rdict['SEQ3'] = self.SEQ3
        self.SEQ4 = RM_Register_CRYPTO0_SEQ4(self.zz_rmio, self.zz_label)
        self.zz_rdict['SEQ4'] = self.SEQ4
        self.DATA0 = RM_Register_CRYPTO0_DATA0(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATA0'] = self.DATA0
        self.DATA1 = RM_Register_CRYPTO0_DATA1(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATA1'] = self.DATA1
        self.DATA2 = RM_Register_CRYPTO0_DATA2(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATA2'] = self.DATA2
        self.DATA3 = RM_Register_CRYPTO0_DATA3(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATA3'] = self.DATA3
        self.DATA0XOR = RM_Register_CRYPTO0_DATA0XOR(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATA0XOR'] = self.DATA0XOR
        self.DATA0BYTE = RM_Register_CRYPTO0_DATA0BYTE(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATA0BYTE'] = self.DATA0BYTE
        self.DATA1BYTE = RM_Register_CRYPTO0_DATA1BYTE(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATA1BYTE'] = self.DATA1BYTE
        self.DATA0XORBYTE = RM_Register_CRYPTO0_DATA0XORBYTE(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATA0XORBYTE'] = self.DATA0XORBYTE
        self.DATA0BYTE12 = RM_Register_CRYPTO0_DATA0BYTE12(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATA0BYTE12'] = self.DATA0BYTE12
        self.DATA0BYTE13 = RM_Register_CRYPTO0_DATA0BYTE13(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATA0BYTE13'] = self.DATA0BYTE13
        self.DATA0BYTE14 = RM_Register_CRYPTO0_DATA0BYTE14(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATA0BYTE14'] = self.DATA0BYTE14
        self.DATA0BYTE15 = RM_Register_CRYPTO0_DATA0BYTE15(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATA0BYTE15'] = self.DATA0BYTE15
        self.DDATA0 = RM_Register_CRYPTO0_DDATA0(self.zz_rmio, self.zz_label)
        self.zz_rdict['DDATA0'] = self.DDATA0
        self.DDATA1 = RM_Register_CRYPTO0_DDATA1(self.zz_rmio, self.zz_label)
        self.zz_rdict['DDATA1'] = self.DDATA1
        self.DDATA2 = RM_Register_CRYPTO0_DDATA2(self.zz_rmio, self.zz_label)
        self.zz_rdict['DDATA2'] = self.DDATA2
        self.DDATA3 = RM_Register_CRYPTO0_DDATA3(self.zz_rmio, self.zz_label)
        self.zz_rdict['DDATA3'] = self.DDATA3
        self.DDATA4 = RM_Register_CRYPTO0_DDATA4(self.zz_rmio, self.zz_label)
        self.zz_rdict['DDATA4'] = self.DDATA4
        self.DDATA0BIG = RM_Register_CRYPTO0_DDATA0BIG(self.zz_rmio, self.zz_label)
        self.zz_rdict['DDATA0BIG'] = self.DDATA0BIG
        self.DDATA0BYTE = RM_Register_CRYPTO0_DDATA0BYTE(self.zz_rmio, self.zz_label)
        self.zz_rdict['DDATA0BYTE'] = self.DDATA0BYTE
        self.DDATA1BYTE = RM_Register_CRYPTO0_DDATA1BYTE(self.zz_rmio, self.zz_label)
        self.zz_rdict['DDATA1BYTE'] = self.DDATA1BYTE
        self.DDATA0BYTE32 = RM_Register_CRYPTO0_DDATA0BYTE32(self.zz_rmio, self.zz_label)
        self.zz_rdict['DDATA0BYTE32'] = self.DDATA0BYTE32
        self.QDATA0 = RM_Register_CRYPTO0_QDATA0(self.zz_rmio, self.zz_label)
        self.zz_rdict['QDATA0'] = self.QDATA0
        self.QDATA1 = RM_Register_CRYPTO0_QDATA1(self.zz_rmio, self.zz_label)
        self.zz_rdict['QDATA1'] = self.QDATA1
        self.QDATA1BIG = RM_Register_CRYPTO0_QDATA1BIG(self.zz_rmio, self.zz_label)
        self.zz_rdict['QDATA1BIG'] = self.QDATA1BIG
        self.QDATA0BYTE = RM_Register_CRYPTO0_QDATA0BYTE(self.zz_rmio, self.zz_label)
        self.zz_rdict['QDATA0BYTE'] = self.QDATA0BYTE
        self.QDATA1BYTE = RM_Register_CRYPTO0_QDATA1BYTE(self.zz_rmio, self.zz_label)
        self.zz_rdict['QDATA1BYTE'] = self.QDATA1BYTE
        self.FEATURE = RM_Register_CRYPTO0_FEATURE(self.zz_rmio, self.zz_label)
        self.zz_rdict['FEATURE'] = self.FEATURE
        self.__dict__['zz_frozen'] = True