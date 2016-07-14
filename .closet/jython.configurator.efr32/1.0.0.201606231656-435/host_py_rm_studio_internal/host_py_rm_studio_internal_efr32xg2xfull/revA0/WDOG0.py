
__all__ = [ 'RM_Peripheral_WDOG0' ]

from static import Base_RM_Peripheral
from WDOG0_register import *

class RM_Peripheral_WDOG0(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_WDOG0, self).__init__(rmio, label,
            0x40052000, 'WDOG0',
            "")
        self.CTRL = RM_Register_WDOG0_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.CMD = RM_Register_WDOG0_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.SYNCBUSY = RM_Register_WDOG0_SYNCBUSY(self.zz_rmio, self.zz_label)
        self.zz_rdict['SYNCBUSY'] = self.SYNCBUSY
        self.PCH0_PRSCTRL = RM_Register_WDOG0_PCH0_PRSCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PCH0_PRSCTRL'] = self.PCH0_PRSCTRL
        self.PCH1_PRSCTRL = RM_Register_WDOG0_PCH1_PRSCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PCH1_PRSCTRL'] = self.PCH1_PRSCTRL
        self.IF = RM_Register_WDOG0_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_WDOG0_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_WDOG0_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_WDOG0_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.__dict__['zz_frozen'] = True