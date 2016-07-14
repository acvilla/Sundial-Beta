
__all__ = [ 'RM_Peripheral_FPUEH' ]

from static import Base_RM_Peripheral
from FPUEH_register import *

class RM_Peripheral_FPUEH(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_FPUEH, self).__init__(rmio, label,
            0x400E1000, 'FPUEH',
            "")
        self.IF = RM_Register_FPUEH_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_FPUEH_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_FPUEH_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_FPUEH_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.__dict__['zz_frozen'] = True