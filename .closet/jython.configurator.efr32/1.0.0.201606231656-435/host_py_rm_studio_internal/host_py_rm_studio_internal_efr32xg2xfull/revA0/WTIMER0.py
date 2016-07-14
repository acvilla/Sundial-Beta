
__all__ = [ 'RM_Peripheral_WTIMER0' ]

from static import Base_RM_Peripheral
from WTIMER0_register import *

class RM_Peripheral_WTIMER0(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_WTIMER0, self).__init__(rmio, label,
            0x4001A000, 'WTIMER0',
            "")
        self.CTRL = RM_Register_WTIMER0_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.CMD = RM_Register_WTIMER0_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.STATUS = RM_Register_WTIMER0_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.IF = RM_Register_WTIMER0_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_WTIMER0_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_WTIMER0_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_WTIMER0_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.TOP = RM_Register_WTIMER0_TOP(self.zz_rmio, self.zz_label)
        self.zz_rdict['TOP'] = self.TOP
        self.TOPB = RM_Register_WTIMER0_TOPB(self.zz_rmio, self.zz_label)
        self.zz_rdict['TOPB'] = self.TOPB
        self.CNT = RM_Register_WTIMER0_CNT(self.zz_rmio, self.zz_label)
        self.zz_rdict['CNT'] = self.CNT
        self.LOCK = RM_Register_WTIMER0_LOCK(self.zz_rmio, self.zz_label)
        self.zz_rdict['LOCK'] = self.LOCK
        self.ROUTEPEN = RM_Register_WTIMER0_ROUTEPEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTEPEN'] = self.ROUTEPEN
        self.ROUTELOC0 = RM_Register_WTIMER0_ROUTELOC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC0'] = self.ROUTELOC0
        self.ROUTELOC2 = RM_Register_WTIMER0_ROUTELOC2(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC2'] = self.ROUTELOC2
        self.CC0_CTRL = RM_Register_WTIMER0_CC0_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC0_CTRL'] = self.CC0_CTRL
        self.CC0_CCV = RM_Register_WTIMER0_CC0_CCV(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC0_CCV'] = self.CC0_CCV
        self.CC0_CCVP = RM_Register_WTIMER0_CC0_CCVP(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC0_CCVP'] = self.CC0_CCVP
        self.CC0_CCVB = RM_Register_WTIMER0_CC0_CCVB(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC0_CCVB'] = self.CC0_CCVB
        self.CC1_CTRL = RM_Register_WTIMER0_CC1_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC1_CTRL'] = self.CC1_CTRL
        self.CC1_CCV = RM_Register_WTIMER0_CC1_CCV(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC1_CCV'] = self.CC1_CCV
        self.CC1_CCVP = RM_Register_WTIMER0_CC1_CCVP(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC1_CCVP'] = self.CC1_CCVP
        self.CC1_CCVB = RM_Register_WTIMER0_CC1_CCVB(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC1_CCVB'] = self.CC1_CCVB
        self.CC2_CTRL = RM_Register_WTIMER0_CC2_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC2_CTRL'] = self.CC2_CTRL
        self.CC2_CCV = RM_Register_WTIMER0_CC2_CCV(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC2_CCV'] = self.CC2_CCV
        self.CC2_CCVP = RM_Register_WTIMER0_CC2_CCVP(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC2_CCVP'] = self.CC2_CCVP
        self.CC2_CCVB = RM_Register_WTIMER0_CC2_CCVB(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC2_CCVB'] = self.CC2_CCVB
        self.CC3_CTRL = RM_Register_WTIMER0_CC3_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC3_CTRL'] = self.CC3_CTRL
        self.CC3_CCV = RM_Register_WTIMER0_CC3_CCV(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC3_CCV'] = self.CC3_CCV
        self.CC3_CCVP = RM_Register_WTIMER0_CC3_CCVP(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC3_CCVP'] = self.CC3_CCVP
        self.CC3_CCVB = RM_Register_WTIMER0_CC3_CCVB(self.zz_rmio, self.zz_label)
        self.zz_rdict['CC3_CCVB'] = self.CC3_CCVB
        self.DTCTRL = RM_Register_WTIMER0_DTCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['DTCTRL'] = self.DTCTRL
        self.DTTIME = RM_Register_WTIMER0_DTTIME(self.zz_rmio, self.zz_label)
        self.zz_rdict['DTTIME'] = self.DTTIME
        self.DTFC = RM_Register_WTIMER0_DTFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['DTFC'] = self.DTFC
        self.DTOGEN = RM_Register_WTIMER0_DTOGEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['DTOGEN'] = self.DTOGEN
        self.DTFAULT = RM_Register_WTIMER0_DTFAULT(self.zz_rmio, self.zz_label)
        self.zz_rdict['DTFAULT'] = self.DTFAULT
        self.DTFAULTC = RM_Register_WTIMER0_DTFAULTC(self.zz_rmio, self.zz_label)
        self.zz_rdict['DTFAULTC'] = self.DTFAULTC
        self.DTLOCK = RM_Register_WTIMER0_DTLOCK(self.zz_rmio, self.zz_label)
        self.zz_rdict['DTLOCK'] = self.DTLOCK
        self.__dict__['zz_frozen'] = True