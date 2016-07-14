
__all__ = [ 'RM_Peripheral_CRYOTIMER' ]

from static import Base_RM_Peripheral
from CRYOTIMER_register import *

class RM_Peripheral_CRYOTIMER(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_CRYOTIMER, self).__init__(rmio, label,
            0x4001E000, 'CRYOTIMER',
            "")
        self.CTRL = RM_Register_CRYOTIMER_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.PERIODSEL = RM_Register_CRYOTIMER_PERIODSEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PERIODSEL'] = self.PERIODSEL
        self.CNT = RM_Register_CRYOTIMER_CNT(self.zz_rmio, self.zz_label)
        self.zz_rdict['CNT'] = self.CNT
        self.EM4WUEN = RM_Register_CRYOTIMER_EM4WUEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['EM4WUEN'] = self.EM4WUEN
        self.IF = RM_Register_CRYOTIMER_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_CRYOTIMER_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_CRYOTIMER_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_CRYOTIMER_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.__dict__['zz_frozen'] = True