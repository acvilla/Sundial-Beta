
__all__ = [ 'RM_Peripheral_PRS' ]

from static import Base_RM_Peripheral
from PRS_register import *

class RM_Peripheral_PRS(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_PRS, self).__init__(rmio, label,
            0x400E6000, 'PRS',
            "")
        self.SWPULSE = RM_Register_PRS_SWPULSE(self.zz_rmio, self.zz_label)
        self.zz_rdict['SWPULSE'] = self.SWPULSE
        self.SWLEVEL = RM_Register_PRS_SWLEVEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['SWLEVEL'] = self.SWLEVEL
        self.ROUTEPEN = RM_Register_PRS_ROUTEPEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTEPEN'] = self.ROUTEPEN
        self.ROUTELOC0 = RM_Register_PRS_ROUTELOC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC0'] = self.ROUTELOC0
        self.ROUTELOC1 = RM_Register_PRS_ROUTELOC1(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC1'] = self.ROUTELOC1
        self.ROUTELOC2 = RM_Register_PRS_ROUTELOC2(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC2'] = self.ROUTELOC2
        self.CTRL = RM_Register_PRS_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.DMAREQ0 = RM_Register_PRS_DMAREQ0(self.zz_rmio, self.zz_label)
        self.zz_rdict['DMAREQ0'] = self.DMAREQ0
        self.DMAREQ1 = RM_Register_PRS_DMAREQ1(self.zz_rmio, self.zz_label)
        self.zz_rdict['DMAREQ1'] = self.DMAREQ1
        self.PEEK = RM_Register_PRS_PEEK(self.zz_rmio, self.zz_label)
        self.zz_rdict['PEEK'] = self.PEEK
        self.CH0_CTRL = RM_Register_PRS_CH0_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH0_CTRL'] = self.CH0_CTRL
        self.CH1_CTRL = RM_Register_PRS_CH1_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH1_CTRL'] = self.CH1_CTRL
        self.CH2_CTRL = RM_Register_PRS_CH2_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH2_CTRL'] = self.CH2_CTRL
        self.CH3_CTRL = RM_Register_PRS_CH3_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH3_CTRL'] = self.CH3_CTRL
        self.CH4_CTRL = RM_Register_PRS_CH4_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH4_CTRL'] = self.CH4_CTRL
        self.CH5_CTRL = RM_Register_PRS_CH5_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH5_CTRL'] = self.CH5_CTRL
        self.CH6_CTRL = RM_Register_PRS_CH6_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH6_CTRL'] = self.CH6_CTRL
        self.CH7_CTRL = RM_Register_PRS_CH7_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH7_CTRL'] = self.CH7_CTRL
        self.CH8_CTRL = RM_Register_PRS_CH8_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH8_CTRL'] = self.CH8_CTRL
        self.CH9_CTRL = RM_Register_PRS_CH9_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH9_CTRL'] = self.CH9_CTRL
        self.CH10_CTRL = RM_Register_PRS_CH10_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH10_CTRL'] = self.CH10_CTRL
        self.CH11_CTRL = RM_Register_PRS_CH11_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CH11_CTRL'] = self.CH11_CTRL
        self.__dict__['zz_frozen'] = True