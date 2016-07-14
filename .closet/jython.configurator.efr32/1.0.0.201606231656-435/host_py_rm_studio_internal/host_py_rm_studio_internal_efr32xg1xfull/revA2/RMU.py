
__all__ = [ 'RM_Peripheral_RMU' ]

from static import Base_RM_Peripheral
from RMU_register import *

class RM_Peripheral_RMU(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_RMU, self).__init__(rmio, label,
            0x400E5000, 'RMU',
            "")
        self.CTRL = RM_Register_RMU_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.RSTCAUSE = RM_Register_RMU_RSTCAUSE(self.zz_rmio, self.zz_label)
        self.zz_rdict['RSTCAUSE'] = self.RSTCAUSE
        self.CMD = RM_Register_RMU_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.RST = RM_Register_RMU_RST(self.zz_rmio, self.zz_label)
        self.zz_rdict['RST'] = self.RST
        self.LOCK = RM_Register_RMU_LOCK(self.zz_rmio, self.zz_label)
        self.zz_rdict['LOCK'] = self.LOCK
        self.__dict__['zz_frozen'] = True