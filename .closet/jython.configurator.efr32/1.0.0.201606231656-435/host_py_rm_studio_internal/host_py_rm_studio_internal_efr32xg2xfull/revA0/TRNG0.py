
__all__ = [ 'RM_Peripheral_TRNG0' ]

from static import Base_RM_Peripheral
from TRNG0_register import *

class RM_Peripheral_TRNG0(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_TRNG0, self).__init__(rmio, label,
            0x4001D000, 'TRNG0',
            "")
        self.CONTROL = RM_Register_TRNG0_CONTROL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CONTROL'] = self.CONTROL
        self.FIFOLEVEL = RM_Register_TRNG0_FIFOLEVEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['FIFOLEVEL'] = self.FIFOLEVEL
        self.FIFODEPTH = RM_Register_TRNG0_FIFODEPTH(self.zz_rmio, self.zz_label)
        self.zz_rdict['FIFODEPTH'] = self.FIFODEPTH
        self.KEY0 = RM_Register_TRNG0_KEY0(self.zz_rmio, self.zz_label)
        self.zz_rdict['KEY0'] = self.KEY0
        self.KEY1 = RM_Register_TRNG0_KEY1(self.zz_rmio, self.zz_label)
        self.zz_rdict['KEY1'] = self.KEY1
        self.KEY2 = RM_Register_TRNG0_KEY2(self.zz_rmio, self.zz_label)
        self.zz_rdict['KEY2'] = self.KEY2
        self.KEY3 = RM_Register_TRNG0_KEY3(self.zz_rmio, self.zz_label)
        self.zz_rdict['KEY3'] = self.KEY3
        self.TESTDATA = RM_Register_TRNG0_TESTDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['TESTDATA'] = self.TESTDATA
        self.REPTHRES = RM_Register_TRNG0_REPTHRES(self.zz_rmio, self.zz_label)
        self.zz_rdict['REPTHRES'] = self.REPTHRES
        self.PROP1THRES = RM_Register_TRNG0_PROP1THRES(self.zz_rmio, self.zz_label)
        self.zz_rdict['PROP1THRES'] = self.PROP1THRES
        self.PROP2THRES = RM_Register_TRNG0_PROP2THRES(self.zz_rmio, self.zz_label)
        self.zz_rdict['PROP2THRES'] = self.PROP2THRES
        self.STATUS = RM_Register_TRNG0_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.INITWAITVAL = RM_Register_TRNG0_INITWAITVAL(self.zz_rmio, self.zz_label)
        self.zz_rdict['INITWAITVAL'] = self.INITWAITVAL
        self.FIFO = RM_Register_TRNG0_FIFO(self.zz_rmio, self.zz_label)
        self.zz_rdict['FIFO'] = self.FIFO
        self.__dict__['zz_frozen'] = True