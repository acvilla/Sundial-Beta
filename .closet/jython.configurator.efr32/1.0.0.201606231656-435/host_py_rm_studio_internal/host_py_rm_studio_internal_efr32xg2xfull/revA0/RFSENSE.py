
__all__ = [ 'RM_Peripheral_RFSENSE' ]

from static import Base_RM_Peripheral
from RFSENSE_register import *

class RM_Peripheral_RFSENSE(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_RFSENSE, self).__init__(rmio, label,
            0x40088000, 'RFSENSE',
            "")
        self.CTRL = RM_Register_RFSENSE_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.PERIODSEL = RM_Register_RFSENSE_PERIODSEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PERIODSEL'] = self.PERIODSEL
        self.CNT = RM_Register_RFSENSE_CNT(self.zz_rmio, self.zz_label)
        self.zz_rdict['CNT'] = self.CNT
        self.EM4WUEN = RM_Register_RFSENSE_EM4WUEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['EM4WUEN'] = self.EM4WUEN
        self.CALIB = RM_Register_RFSENSE_CALIB(self.zz_rmio, self.zz_label)
        self.zz_rdict['CALIB'] = self.CALIB
        self.IF = RM_Register_RFSENSE_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_RFSENSE_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_RFSENSE_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_RFSENSE_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.__dict__['zz_frozen'] = True