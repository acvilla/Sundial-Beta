
__all__ = [ 'RM_Peripheral_CM4' ]

from static import Base_RM_Peripheral
from CM4_register import *

class RM_Peripheral_CM4(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_CM4, self).__init__(rmio, label,
            0xE0000000, 'CM4',
            "")
        self.NVICAUXCTRL = RM_Register_CM4_NVICAUXCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICAUXCTRL'] = self.NVICAUXCTRL
        self.NVICVECTSETIEN = RM_Register_CM4_NVICVECTSETIEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICVECTSETIEN'] = self.NVICVECTSETIEN
        self.NVICVECTSETIEN1 = RM_Register_CM4_NVICVECTSETIEN1(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICVECTSETIEN1'] = self.NVICVECTSETIEN1
        self.NVICVECTSETIDIS = RM_Register_CM4_NVICVECTSETIDIS(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICVECTSETIDIS'] = self.NVICVECTSETIDIS
        self.NVICVECTSETIDIS1 = RM_Register_CM4_NVICVECTSETIDIS1(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICVECTSETIDIS1'] = self.NVICVECTSETIDIS1
        self.NVICVECTSETPEND = RM_Register_CM4_NVICVECTSETPEND(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICVECTSETPEND'] = self.NVICVECTSETPEND
        self.NVICVECTSETPEND1 = RM_Register_CM4_NVICVECTSETPEND1(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICVECTSETPEND1'] = self.NVICVECTSETPEND1
        self.NVICVECTCLEARPEND = RM_Register_CM4_NVICVECTCLEARPEND(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICVECTCLEARPEND'] = self.NVICVECTCLEARPEND
        self.NVICVECTCLEARPEND1 = RM_Register_CM4_NVICVECTCLEARPEND1(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICVECTCLEARPEND1'] = self.NVICVECTCLEARPEND1
        self.NVICPRI0 = RM_Register_CM4_NVICPRI0(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICPRI0'] = self.NVICPRI0
        self.NVICISCR = RM_Register_CM4_NVICISCR(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICISCR'] = self.NVICISCR
        self.NVICVECTTABOFF = RM_Register_CM4_NVICVECTTABOFF(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICVECTTABOFF'] = self.NVICVECTTABOFF
        self.NVICSYSCTRL = RM_Register_CM4_NVICSYSCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICSYSCTRL'] = self.NVICSYSCTRL
        self.NVICSYSHANDLER = RM_Register_CM4_NVICSYSHANDLER(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICSYSHANDLER'] = self.NVICSYSHANDLER
        self.NVICCFSR = RM_Register_CM4_NVICCFSR(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICCFSR'] = self.NVICCFSR
        self.NVICHFSR = RM_Register_CM4_NVICHFSR(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICHFSR'] = self.NVICHFSR
        self.NVICAIRC = RM_Register_CM4_NVICAIRC(self.zz_rmio, self.zz_label)
        self.zz_rdict['NVICAIRC'] = self.NVICAIRC
        self.CHIPREVMAJORLSB = RM_Register_CM4_CHIPREVMAJORLSB(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHIPREVMAJORLSB'] = self.CHIPREVMAJORLSB
        self.CHIPREVMAJORMSB = RM_Register_CM4_CHIPREVMAJORMSB(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHIPREVMAJORMSB'] = self.CHIPREVMAJORMSB
        self.CHIPREVMINORMSB = RM_Register_CM4_CHIPREVMINORMSB(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHIPREVMINORMSB'] = self.CHIPREVMINORMSB
        self.CHIPREVMINORLSB = RM_Register_CM4_CHIPREVMINORLSB(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHIPREVMINORLSB'] = self.CHIPREVMINORLSB
        self.__dict__['zz_frozen'] = True