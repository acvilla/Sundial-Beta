
__all__ = [ 'RM_Peripheral_LETIMER0' ]

from static import Base_RM_Peripheral
from LETIMER0_register import *

class RM_Peripheral_LETIMER0(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_LETIMER0, self).__init__(rmio, label,
            0x40046000, 'LETIMER0',
            "")
        self.CTRL = RM_Register_LETIMER0_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.CMD = RM_Register_LETIMER0_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.STATUS = RM_Register_LETIMER0_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.CNT = RM_Register_LETIMER0_CNT(self.zz_rmio, self.zz_label)
        self.zz_rdict['CNT'] = self.CNT
        self.COMP0 = RM_Register_LETIMER0_COMP0(self.zz_rmio, self.zz_label)
        self.zz_rdict['COMP0'] = self.COMP0
        self.COMP1 = RM_Register_LETIMER0_COMP1(self.zz_rmio, self.zz_label)
        self.zz_rdict['COMP1'] = self.COMP1
        self.REP0 = RM_Register_LETIMER0_REP0(self.zz_rmio, self.zz_label)
        self.zz_rdict['REP0'] = self.REP0
        self.REP1 = RM_Register_LETIMER0_REP1(self.zz_rmio, self.zz_label)
        self.zz_rdict['REP1'] = self.REP1
        self.IF = RM_Register_LETIMER0_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_LETIMER0_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_LETIMER0_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_LETIMER0_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.SYNCBUSY = RM_Register_LETIMER0_SYNCBUSY(self.zz_rmio, self.zz_label)
        self.zz_rdict['SYNCBUSY'] = self.SYNCBUSY
        self.ROUTEPEN = RM_Register_LETIMER0_ROUTEPEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTEPEN'] = self.ROUTEPEN
        self.ROUTELOC0 = RM_Register_LETIMER0_ROUTELOC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC0'] = self.ROUTELOC0
        self.PRSSEL = RM_Register_LETIMER0_PRSSEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PRSSEL'] = self.PRSSEL
        self.__dict__['zz_frozen'] = True