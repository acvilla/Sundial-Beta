
__all__ = [ 'RM_Peripheral_WDOG1' ]

from static import Base_RM_Peripheral
from WDOG1_register import *

class RM_Peripheral_WDOG1(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_WDOG1, self).__init__(rmio, label,
            0x40052400, 'WDOG1',
            "")
        self.CTRL = RM_Register_WDOG1_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.CMD = RM_Register_WDOG1_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.SYNCBUSY = RM_Register_WDOG1_SYNCBUSY(self.zz_rmio, self.zz_label)
        self.zz_rdict['SYNCBUSY'] = self.SYNCBUSY
        self.PCH0_PRSCTRL = RM_Register_WDOG1_PCH0_PRSCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PCH0_PRSCTRL'] = self.PCH0_PRSCTRL
        self.PCH1_PRSCTRL = RM_Register_WDOG1_PCH1_PRSCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PCH1_PRSCTRL'] = self.PCH1_PRSCTRL
        self.IF = RM_Register_WDOG1_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_WDOG1_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_WDOG1_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_WDOG1_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.__dict__['zz_frozen'] = True