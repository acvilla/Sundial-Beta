
__all__ = [ 'RM_Peripheral_GPCRC' ]

from static import Base_RM_Peripheral
from GPCRC_register import *

class RM_Peripheral_GPCRC(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_GPCRC, self).__init__(rmio, label,
            0x4001C000, 'GPCRC',
            "")
        self.CTRL = RM_Register_GPCRC_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.CMD = RM_Register_GPCRC_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.INIT = RM_Register_GPCRC_INIT(self.zz_rmio, self.zz_label)
        self.zz_rdict['INIT'] = self.INIT
        self.POLY = RM_Register_GPCRC_POLY(self.zz_rmio, self.zz_label)
        self.zz_rdict['POLY'] = self.POLY
        self.INPUTDATA = RM_Register_GPCRC_INPUTDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['INPUTDATA'] = self.INPUTDATA
        self.INPUTDATAHWORD = RM_Register_GPCRC_INPUTDATAHWORD(self.zz_rmio, self.zz_label)
        self.zz_rdict['INPUTDATAHWORD'] = self.INPUTDATAHWORD
        self.INPUTDATABYTE = RM_Register_GPCRC_INPUTDATABYTE(self.zz_rmio, self.zz_label)
        self.zz_rdict['INPUTDATABYTE'] = self.INPUTDATABYTE
        self.DATA = RM_Register_GPCRC_DATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATA'] = self.DATA
        self.DATAREV = RM_Register_GPCRC_DATAREV(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATAREV'] = self.DATAREV
        self.DATABYTEREV = RM_Register_GPCRC_DATABYTEREV(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATABYTEREV'] = self.DATABYTEREV
        self.SNOOP0_CTRL = RM_Register_GPCRC_SNOOP0_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['SNOOP0_CTRL'] = self.SNOOP0_CTRL
        self.SNOOP0_ADDR = RM_Register_GPCRC_SNOOP0_ADDR(self.zz_rmio, self.zz_label)
        self.zz_rdict['SNOOP0_ADDR'] = self.SNOOP0_ADDR
        self.SNOOP1_CTRL = RM_Register_GPCRC_SNOOP1_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['SNOOP1_CTRL'] = self.SNOOP1_CTRL
        self.SNOOP1_ADDR = RM_Register_GPCRC_SNOOP1_ADDR(self.zz_rmio, self.zz_label)
        self.zz_rdict['SNOOP1_ADDR'] = self.SNOOP1_ADDR
        self.SNOOP2_CTRL = RM_Register_GPCRC_SNOOP2_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['SNOOP2_CTRL'] = self.SNOOP2_CTRL
        self.SNOOP2_ADDR = RM_Register_GPCRC_SNOOP2_ADDR(self.zz_rmio, self.zz_label)
        self.zz_rdict['SNOOP2_ADDR'] = self.SNOOP2_ADDR
        self.__dict__['zz_frozen'] = True