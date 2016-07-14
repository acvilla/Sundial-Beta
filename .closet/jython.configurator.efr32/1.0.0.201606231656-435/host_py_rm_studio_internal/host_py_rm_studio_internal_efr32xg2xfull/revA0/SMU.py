
__all__ = [ 'RM_Peripheral_SMU' ]

from static import Base_RM_Peripheral
from SMU_register import *

class RM_Peripheral_SMU(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_SMU, self).__init__(rmio, label,
            0x40022000, 'SMU',
            "")
        self.IF = RM_Register_SMU_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_SMU_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_SMU_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_SMU_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.SPBGCTRL = RM_Register_SMU_SPBGCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['SPBGCTRL'] = self.SPBGCTRL
        self.SPBGPATD0 = RM_Register_SMU_SPBGPATD0(self.zz_rmio, self.zz_label)
        self.zz_rdict['SPBGPATD0'] = self.SPBGPATD0
        self.SPBGPATD1 = RM_Register_SMU_SPBGPATD1(self.zz_rmio, self.zz_label)
        self.zz_rdict['SPBGPATD1'] = self.SPBGPATD1
        self.SPBGFS = RM_Register_SMU_SPBGFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['SPBGFS'] = self.SPBGFS
        self.__dict__['zz_frozen'] = True