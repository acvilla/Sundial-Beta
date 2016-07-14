
__all__ = [ 'RM_Peripheral_ACMP1' ]

from static import Base_RM_Peripheral
from ACMP1_register import *

class RM_Peripheral_ACMP1(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_ACMP1, self).__init__(rmio, label,
            0x40000400, 'ACMP1',
            "")
        self.CTRL = RM_Register_ACMP1_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.INPUTSEL = RM_Register_ACMP1_INPUTSEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['INPUTSEL'] = self.INPUTSEL
        self.STATUS = RM_Register_ACMP1_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.IF = RM_Register_ACMP1_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_ACMP1_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_ACMP1_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_ACMP1_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.BUSREQ = RM_Register_ACMP1_BUSREQ(self.zz_rmio, self.zz_label)
        self.zz_rdict['BUSREQ'] = self.BUSREQ
        self.BUSCONFLICT = RM_Register_ACMP1_BUSCONFLICT(self.zz_rmio, self.zz_label)
        self.zz_rdict['BUSCONFLICT'] = self.BUSCONFLICT
        self.HYSTERESIS0 = RM_Register_ACMP1_HYSTERESIS0(self.zz_rmio, self.zz_label)
        self.zz_rdict['HYSTERESIS0'] = self.HYSTERESIS0
        self.HYSTERESIS1 = RM_Register_ACMP1_HYSTERESIS1(self.zz_rmio, self.zz_label)
        self.zz_rdict['HYSTERESIS1'] = self.HYSTERESIS1
        self.TEST = RM_Register_ACMP1_TEST(self.zz_rmio, self.zz_label)
        self.zz_rdict['TEST'] = self.TEST
        self.ROUTEPEN = RM_Register_ACMP1_ROUTEPEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTEPEN'] = self.ROUTEPEN
        self.ROUTELOC0 = RM_Register_ACMP1_ROUTELOC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC0'] = self.ROUTELOC0
        self.__dict__['zz_frozen'] = True