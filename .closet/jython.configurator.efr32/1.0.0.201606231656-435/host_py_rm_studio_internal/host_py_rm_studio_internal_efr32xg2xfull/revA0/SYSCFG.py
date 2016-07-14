
__all__ = [ 'RM_Peripheral_SYSCFG' ]

from static import Base_RM_Peripheral
from SYSCFG_register import *

class RM_Peripheral_SYSCFG(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_SYSCFG, self).__init__(rmio, label,
            0x400E7000, 'SYSCFG',
            "")
        self.CTRLPMON = RM_Register_SYSCFG_CTRLPMON(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRLPMON'] = self.CTRLPMON
        self.AMUXCP = RM_Register_SYSCFG_AMUXCP(self.zz_rmio, self.zz_label)
        self.zz_rdict['AMUXCP'] = self.AMUXCP
        self.AMUXCPCTRL = RM_Register_SYSCFG_AMUXCPCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['AMUXCPCTRL'] = self.AMUXCPCTRL
        self.AMUXCPCAL = RM_Register_SYSCFG_AMUXCPCAL(self.zz_rmio, self.zz_label)
        self.zz_rdict['AMUXCPCAL'] = self.AMUXCPCAL
        self.IF = RM_Register_SYSCFG_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_SYSCFG_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_SYSCFG_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_SYSCFG_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.__dict__['zz_frozen'] = True