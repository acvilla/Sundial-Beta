
__all__ = [ 'RM_Peripheral_ETM' ]

from static import Base_RM_Peripheral
from ETM_register import *

class RM_Peripheral_ETM(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_ETM, self).__init__(rmio, label,
            0xE0041000, 'ETM',
            "")
        self.ETMCR = RM_Register_ETM_ETMCR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMCR'] = self.ETMCR
        self.ETMCCR = RM_Register_ETM_ETMCCR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMCCR'] = self.ETMCCR
        self.ETMTRIGGER = RM_Register_ETM_ETMTRIGGER(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMTRIGGER'] = self.ETMTRIGGER
        self.ETMSR = RM_Register_ETM_ETMSR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMSR'] = self.ETMSR
        self.ETMSCR = RM_Register_ETM_ETMSCR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMSCR'] = self.ETMSCR
        self.ETMTEEVR = RM_Register_ETM_ETMTEEVR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMTEEVR'] = self.ETMTEEVR
        self.ETMTECR1 = RM_Register_ETM_ETMTECR1(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMTECR1'] = self.ETMTECR1
        self.ETMFFLR = RM_Register_ETM_ETMFFLR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMFFLR'] = self.ETMFFLR
        self.ETMCNTRLDVR1 = RM_Register_ETM_ETMCNTRLDVR1(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMCNTRLDVR1'] = self.ETMCNTRLDVR1
        self.ETMSYNCFR = RM_Register_ETM_ETMSYNCFR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMSYNCFR'] = self.ETMSYNCFR
        self.ETMIDR = RM_Register_ETM_ETMIDR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMIDR'] = self.ETMIDR
        self.ETMCCER = RM_Register_ETM_ETMCCER(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMCCER'] = self.ETMCCER
        self.ETMTESSEICR = RM_Register_ETM_ETMTESSEICR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMTESSEICR'] = self.ETMTESSEICR
        self.ETMTSEVR = RM_Register_ETM_ETMTSEVR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMTSEVR'] = self.ETMTSEVR
        self.ETMTRACEIDR = RM_Register_ETM_ETMTRACEIDR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMTRACEIDR'] = self.ETMTRACEIDR
        self.ETMIDR2 = RM_Register_ETM_ETMIDR2(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMIDR2'] = self.ETMIDR2
        self.ETMPDSR = RM_Register_ETM_ETMPDSR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMPDSR'] = self.ETMPDSR
        self.ETMISCIN = RM_Register_ETM_ETMISCIN(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMISCIN'] = self.ETMISCIN
        self.ITTRIGOUT = RM_Register_ETM_ITTRIGOUT(self.zz_rmio, self.zz_label)
        self.zz_rdict['ITTRIGOUT'] = self.ITTRIGOUT
        self.ETMITATBCTR2 = RM_Register_ETM_ETMITATBCTR2(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMITATBCTR2'] = self.ETMITATBCTR2
        self.ETMITATBCTR0 = RM_Register_ETM_ETMITATBCTR0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMITATBCTR0'] = self.ETMITATBCTR0
        self.ETMITCTRL = RM_Register_ETM_ETMITCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMITCTRL'] = self.ETMITCTRL
        self.ETMCLAIMSET = RM_Register_ETM_ETMCLAIMSET(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMCLAIMSET'] = self.ETMCLAIMSET
        self.ETMCLAIMCLR = RM_Register_ETM_ETMCLAIMCLR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMCLAIMCLR'] = self.ETMCLAIMCLR
        self.ETMLAR = RM_Register_ETM_ETMLAR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMLAR'] = self.ETMLAR
        self.ETMLSR = RM_Register_ETM_ETMLSR(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMLSR'] = self.ETMLSR
        self.ETMAUTHSTATUS = RM_Register_ETM_ETMAUTHSTATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMAUTHSTATUS'] = self.ETMAUTHSTATUS
        self.ETMDEVTYPE = RM_Register_ETM_ETMDEVTYPE(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMDEVTYPE'] = self.ETMDEVTYPE
        self.ETMPIDR4 = RM_Register_ETM_ETMPIDR4(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMPIDR4'] = self.ETMPIDR4
        self.ETMPIDR0 = RM_Register_ETM_ETMPIDR0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMPIDR0'] = self.ETMPIDR0
        self.ETMPIDR1 = RM_Register_ETM_ETMPIDR1(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMPIDR1'] = self.ETMPIDR1
        self.ETMPIDR2 = RM_Register_ETM_ETMPIDR2(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMPIDR2'] = self.ETMPIDR2
        self.ETMPIDR3 = RM_Register_ETM_ETMPIDR3(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMPIDR3'] = self.ETMPIDR3
        self.ETMCIDR0 = RM_Register_ETM_ETMCIDR0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMCIDR0'] = self.ETMCIDR0
        self.ETMCIDR1 = RM_Register_ETM_ETMCIDR1(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMCIDR1'] = self.ETMCIDR1
        self.ETMCIDR2 = RM_Register_ETM_ETMCIDR2(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMCIDR2'] = self.ETMCIDR2
        self.ETMCIDR3 = RM_Register_ETM_ETMCIDR3(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETMCIDR3'] = self.ETMCIDR3
        self.__dict__['zz_frozen'] = True