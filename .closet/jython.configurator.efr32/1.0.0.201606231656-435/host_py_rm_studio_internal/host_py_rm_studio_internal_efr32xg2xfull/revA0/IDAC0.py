
__all__ = [ 'RM_Peripheral_IDAC0' ]

from static import Base_RM_Peripheral
from IDAC0_register import *

class RM_Peripheral_IDAC0(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_IDAC0, self).__init__(rmio, label,
            0x40006000, 'IDAC0',
            "")
        self.CTRL = RM_Register_IDAC0_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.CURPROG = RM_Register_IDAC0_CURPROG(self.zz_rmio, self.zz_label)
        self.zz_rdict['CURPROG'] = self.CURPROG
        self.DUTYCONFIG = RM_Register_IDAC0_DUTYCONFIG(self.zz_rmio, self.zz_label)
        self.zz_rdict['DUTYCONFIG'] = self.DUTYCONFIG
        self.DUTYFREQSEL = RM_Register_IDAC0_DUTYFREQSEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['DUTYFREQSEL'] = self.DUTYFREQSEL
        self.TESTCTRL = RM_Register_IDAC0_TESTCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['TESTCTRL'] = self.TESTCTRL
        self.STATUS = RM_Register_IDAC0_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.IF = RM_Register_IDAC0_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_IDAC0_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_IDAC0_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_IDAC0_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.APORTREQ = RM_Register_IDAC0_APORTREQ(self.zz_rmio, self.zz_label)
        self.zz_rdict['APORTREQ'] = self.APORTREQ
        self.APORTCONFLICT = RM_Register_IDAC0_APORTCONFLICT(self.zz_rmio, self.zz_label)
        self.zz_rdict['APORTCONFLICT'] = self.APORTCONFLICT
        self.__dict__['zz_frozen'] = True