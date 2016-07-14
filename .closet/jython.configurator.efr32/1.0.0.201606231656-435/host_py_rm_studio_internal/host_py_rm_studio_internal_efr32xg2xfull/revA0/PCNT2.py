
__all__ = [ 'RM_Peripheral_PCNT2' ]

from static import Base_RM_Peripheral
from PCNT2_register import *

class RM_Peripheral_PCNT2(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_PCNT2, self).__init__(rmio, label,
            0x4004E800, 'PCNT2',
            "")
        self.CTRL = RM_Register_PCNT2_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.CMD = RM_Register_PCNT2_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.STATUS = RM_Register_PCNT2_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.CNT = RM_Register_PCNT2_CNT(self.zz_rmio, self.zz_label)
        self.zz_rdict['CNT'] = self.CNT
        self.TOP = RM_Register_PCNT2_TOP(self.zz_rmio, self.zz_label)
        self.zz_rdict['TOP'] = self.TOP
        self.TOPB = RM_Register_PCNT2_TOPB(self.zz_rmio, self.zz_label)
        self.zz_rdict['TOPB'] = self.TOPB
        self.IF = RM_Register_PCNT2_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_PCNT2_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_PCNT2_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_PCNT2_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.ROUTELOC0 = RM_Register_PCNT2_ROUTELOC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC0'] = self.ROUTELOC0
        self.FREEZE = RM_Register_PCNT2_FREEZE(self.zz_rmio, self.zz_label)
        self.zz_rdict['FREEZE'] = self.FREEZE
        self.SYNCBUSY = RM_Register_PCNT2_SYNCBUSY(self.zz_rmio, self.zz_label)
        self.zz_rdict['SYNCBUSY'] = self.SYNCBUSY
        self.AUXCNT = RM_Register_PCNT2_AUXCNT(self.zz_rmio, self.zz_label)
        self.zz_rdict['AUXCNT'] = self.AUXCNT
        self.INPUT = RM_Register_PCNT2_INPUT(self.zz_rmio, self.zz_label)
        self.zz_rdict['INPUT'] = self.INPUT
        self.OVSCFG = RM_Register_PCNT2_OVSCFG(self.zz_rmio, self.zz_label)
        self.zz_rdict['OVSCFG'] = self.OVSCFG
        self.__dict__['zz_frozen'] = True