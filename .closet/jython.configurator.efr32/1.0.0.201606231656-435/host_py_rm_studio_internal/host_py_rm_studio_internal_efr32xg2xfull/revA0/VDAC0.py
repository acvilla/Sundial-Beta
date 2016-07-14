
__all__ = [ 'RM_Peripheral_VDAC0' ]

from static import Base_RM_Peripheral
from VDAC0_register import *

class RM_Peripheral_VDAC0(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_VDAC0, self).__init__(rmio, label,
            0x40008000, 'VDAC0',
            "")
        self.CTRL = RM_Register_VDAC0_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.STATUS = RM_Register_VDAC0_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.CH0CTRL = RM_Register_VDAC0_CH0CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH0CTRL'] = self.CH0CTRL
        self.CH1CTRL = RM_Register_VDAC0_CH1CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH1CTRL'] = self.CH1CTRL
        self.CMD = RM_Register_VDAC0_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.IF = RM_Register_VDAC0_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_VDAC0_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_VDAC0_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_VDAC0_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.CH0DATA = RM_Register_VDAC0_CH0DATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH0DATA'] = self.CH0DATA
        self.CH1DATA = RM_Register_VDAC0_CH1DATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH1DATA'] = self.CH1DATA
        self.COMBDATA = RM_Register_VDAC0_COMBDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['COMBDATA'] = self.COMBDATA
        self.CAL = RM_Register_VDAC0_CAL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CAL'] = self.CAL
        self.DBGCTRL = RM_Register_VDAC0_DBGCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['DBGCTRL'] = self.DBGCTRL
        self.BIASPROG = RM_Register_VDAC0_BIASPROG(self.zz_rmio, self.zz_label)
        self.zz_rdict['BIASPROG'] = self.BIASPROG
        self.REFENTIME = RM_Register_VDAC0_REFENTIME(self.zz_rmio, self.zz_label)
        self.zz_rdict['REFENTIME'] = self.REFENTIME
        self.TEST = RM_Register_VDAC0_TEST(self.zz_rmio, self.zz_label)
        self.zz_rdict['TEST'] = self.TEST
        self.OPAPRESC = RM_Register_VDAC0_OPAPRESC(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPAPRESC'] = self.OPAPRESC
        self.OPA0_APORTREQ = RM_Register_VDAC0_OPA0_APORTREQ(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA0_APORTREQ'] = self.OPA0_APORTREQ
        self.OPA0_APORTCONFLICT = RM_Register_VDAC0_OPA0_APORTCONFLICT(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA0_APORTCONFLICT'] = self.OPA0_APORTCONFLICT
        self.OPA0_CTRL = RM_Register_VDAC0_OPA0_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA0_CTRL'] = self.OPA0_CTRL
        self.OPA0_TIMER = RM_Register_VDAC0_OPA0_TIMER(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA0_TIMER'] = self.OPA0_TIMER
        self.OPA0_MUX = RM_Register_VDAC0_OPA0_MUX(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA0_MUX'] = self.OPA0_MUX
        self.OPA0_OUT = RM_Register_VDAC0_OPA0_OUT(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA0_OUT'] = self.OPA0_OUT
        self.OPA0_CAL = RM_Register_VDAC0_OPA0_CAL(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA0_CAL'] = self.OPA0_CAL
        self.OPA1_APORTREQ = RM_Register_VDAC0_OPA1_APORTREQ(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA1_APORTREQ'] = self.OPA1_APORTREQ
        self.OPA1_APORTCONFLICT = RM_Register_VDAC0_OPA1_APORTCONFLICT(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA1_APORTCONFLICT'] = self.OPA1_APORTCONFLICT
        self.OPA1_CTRL = RM_Register_VDAC0_OPA1_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA1_CTRL'] = self.OPA1_CTRL
        self.OPA1_TIMER = RM_Register_VDAC0_OPA1_TIMER(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA1_TIMER'] = self.OPA1_TIMER
        self.OPA1_MUX = RM_Register_VDAC0_OPA1_MUX(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA1_MUX'] = self.OPA1_MUX
        self.OPA1_OUT = RM_Register_VDAC0_OPA1_OUT(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA1_OUT'] = self.OPA1_OUT
        self.OPA1_CAL = RM_Register_VDAC0_OPA1_CAL(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA1_CAL'] = self.OPA1_CAL
        self.OPA2_APORTREQ = RM_Register_VDAC0_OPA2_APORTREQ(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA2_APORTREQ'] = self.OPA2_APORTREQ
        self.OPA2_APORTCONFLICT = RM_Register_VDAC0_OPA2_APORTCONFLICT(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA2_APORTCONFLICT'] = self.OPA2_APORTCONFLICT
        self.OPA2_CTRL = RM_Register_VDAC0_OPA2_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA2_CTRL'] = self.OPA2_CTRL
        self.OPA2_TIMER = RM_Register_VDAC0_OPA2_TIMER(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA2_TIMER'] = self.OPA2_TIMER
        self.OPA2_MUX = RM_Register_VDAC0_OPA2_MUX(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA2_MUX'] = self.OPA2_MUX
        self.OPA2_OUT = RM_Register_VDAC0_OPA2_OUT(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA2_OUT'] = self.OPA2_OUT
        self.OPA2_CAL = RM_Register_VDAC0_OPA2_CAL(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA2_CAL'] = self.OPA2_CAL
        self.OPA3_APORTREQ = RM_Register_VDAC0_OPA3_APORTREQ(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA3_APORTREQ'] = self.OPA3_APORTREQ
        self.OPA3_APORTCONFLICT = RM_Register_VDAC0_OPA3_APORTCONFLICT(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA3_APORTCONFLICT'] = self.OPA3_APORTCONFLICT
        self.OPA3_CTRL = RM_Register_VDAC0_OPA3_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA3_CTRL'] = self.OPA3_CTRL
        self.OPA3_TIMER = RM_Register_VDAC0_OPA3_TIMER(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA3_TIMER'] = self.OPA3_TIMER
        self.OPA3_MUX = RM_Register_VDAC0_OPA3_MUX(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA3_MUX'] = self.OPA3_MUX
        self.OPA3_OUT = RM_Register_VDAC0_OPA3_OUT(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA3_OUT'] = self.OPA3_OUT
        self.OPA3_CAL = RM_Register_VDAC0_OPA3_CAL(self.zz_rmio, self.zz_label)
        self.zz_rdict['OPA3_CAL'] = self.OPA3_CAL
        self.__dict__['zz_frozen'] = True