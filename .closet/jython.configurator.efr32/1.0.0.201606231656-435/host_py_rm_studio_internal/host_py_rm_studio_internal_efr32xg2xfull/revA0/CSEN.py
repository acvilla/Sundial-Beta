
__all__ = [ 'RM_Peripheral_CSEN' ]

from static import Base_RM_Peripheral
from CSEN_register import *

class RM_Peripheral_CSEN(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_CSEN, self).__init__(rmio, label,
            0x4001F000, 'CSEN',
            "")
        self.CTRL = RM_Register_CSEN_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.TIMCTRL = RM_Register_CSEN_TIMCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['TIMCTRL'] = self.TIMCTRL
        self.CMD = RM_Register_CSEN_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.STATUS = RM_Register_CSEN_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.PRSSEL = RM_Register_CSEN_PRSSEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PRSSEL'] = self.PRSSEL
        self.DATA = RM_Register_CSEN_DATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATA'] = self.DATA
        self.SCANMASK0 = RM_Register_CSEN_SCANMASK0(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANMASK0'] = self.SCANMASK0
        self.SCANINPUTSEL0 = RM_Register_CSEN_SCANINPUTSEL0(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANINPUTSEL0'] = self.SCANINPUTSEL0
        self.SCANMASK1 = RM_Register_CSEN_SCANMASK1(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANMASK1'] = self.SCANMASK1
        self.SCANINPUTSEL1 = RM_Register_CSEN_SCANINPUTSEL1(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANINPUTSEL1'] = self.SCANINPUTSEL1
        self.APORTREQ = RM_Register_CSEN_APORTREQ(self.zz_rmio, self.zz_label)
        self.zz_rdict['APORTREQ'] = self.APORTREQ
        self.APORTCONFLICT = RM_Register_CSEN_APORTCONFLICT(self.zz_rmio, self.zz_label)
        self.zz_rdict['APORTCONFLICT'] = self.APORTCONFLICT
        self.CMPTHR = RM_Register_CSEN_CMPTHR(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMPTHR'] = self.CMPTHR
        self.EMA = RM_Register_CSEN_EMA(self.zz_rmio, self.zz_label)
        self.zz_rdict['EMA'] = self.EMA
        self.EMACTRL = RM_Register_CSEN_EMACTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['EMACTRL'] = self.EMACTRL
        self.SINGLECTRL = RM_Register_CSEN_SINGLECTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['SINGLECTRL'] = self.SINGLECTRL
        self.DMBASELINE = RM_Register_CSEN_DMBASELINE(self.zz_rmio, self.zz_label)
        self.zz_rdict['DMBASELINE'] = self.DMBASELINE
        self.DMCFG = RM_Register_CSEN_DMCFG(self.zz_rmio, self.zz_label)
        self.zz_rdict['DMCFG'] = self.DMCFG
        self.ANACTRL = RM_Register_CSEN_ANACTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANACTRL'] = self.ANACTRL
        self.ANATRIM = RM_Register_CSEN_ANATRIM(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANATRIM'] = self.ANATRIM
        self.TESTCFG = RM_Register_CSEN_TESTCFG(self.zz_rmio, self.zz_label)
        self.zz_rdict['TESTCFG'] = self.TESTCFG
        self.IF = RM_Register_CSEN_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_CSEN_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_CSEN_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_CSEN_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.__dict__['zz_frozen'] = True