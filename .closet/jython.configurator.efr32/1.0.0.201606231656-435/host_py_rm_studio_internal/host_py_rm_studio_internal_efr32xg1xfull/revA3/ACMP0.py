
__all__ = [ 'RM_Peripheral_ACMP0' ]

from static import Base_RM_Peripheral
from ACMP0_register import *

class RM_Peripheral_ACMP0(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_ACMP0, self).__init__(rmio, label,
            0x40000000, 'ACMP0',
            "")
        self.CTRL = RM_Register_ACMP0_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.INPUTSEL = RM_Register_ACMP0_INPUTSEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['INPUTSEL'] = self.INPUTSEL
        self.STATUS = RM_Register_ACMP0_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.IF = RM_Register_ACMP0_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_ACMP0_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_ACMP0_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_ACMP0_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.BUSREQ = RM_Register_ACMP0_BUSREQ(self.zz_rmio, self.zz_label)
        self.zz_rdict['BUSREQ'] = self.BUSREQ
        self.BUSCONFLICT = RM_Register_ACMP0_BUSCONFLICT(self.zz_rmio, self.zz_label)
        self.zz_rdict['BUSCONFLICT'] = self.BUSCONFLICT
        self.HYSTERESIS0 = RM_Register_ACMP0_HYSTERESIS0(self.zz_rmio, self.zz_label)
        self.zz_rdict['HYSTERESIS0'] = self.HYSTERESIS0
        self.HYSTERESIS1 = RM_Register_ACMP0_HYSTERESIS1(self.zz_rmio, self.zz_label)
        self.zz_rdict['HYSTERESIS1'] = self.HYSTERESIS1
        self.TEST = RM_Register_ACMP0_TEST(self.zz_rmio, self.zz_label)
        self.zz_rdict['TEST'] = self.TEST
        self.ROUTEPEN = RM_Register_ACMP0_ROUTEPEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTEPEN'] = self.ROUTEPEN
        self.ROUTELOC0 = RM_Register_ACMP0_ROUTELOC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC0'] = self.ROUTELOC0
        self.__dict__['zz_frozen'] = True