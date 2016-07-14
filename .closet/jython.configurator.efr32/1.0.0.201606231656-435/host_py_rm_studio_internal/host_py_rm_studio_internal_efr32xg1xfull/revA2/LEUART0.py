
__all__ = [ 'RM_Peripheral_LEUART0' ]

from static import Base_RM_Peripheral
from LEUART0_register import *

class RM_Peripheral_LEUART0(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_LEUART0, self).__init__(rmio, label,
            0x4004A000, 'LEUART0',
            "")
        self.CTRL = RM_Register_LEUART0_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.CMD = RM_Register_LEUART0_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.STATUS = RM_Register_LEUART0_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.CLKDIV = RM_Register_LEUART0_CLKDIV(self.zz_rmio, self.zz_label)
        self.zz_rdict['CLKDIV'] = self.CLKDIV
        self.STARTFRAME = RM_Register_LEUART0_STARTFRAME(self.zz_rmio, self.zz_label)
        self.zz_rdict['STARTFRAME'] = self.STARTFRAME
        self.SIGFRAME = RM_Register_LEUART0_SIGFRAME(self.zz_rmio, self.zz_label)
        self.zz_rdict['SIGFRAME'] = self.SIGFRAME
        self.RXDATAX = RM_Register_LEUART0_RXDATAX(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXDATAX'] = self.RXDATAX
        self.RXDATA = RM_Register_LEUART0_RXDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXDATA'] = self.RXDATA
        self.RXDATAXP = RM_Register_LEUART0_RXDATAXP(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXDATAXP'] = self.RXDATAXP
        self.TXDATAX = RM_Register_LEUART0_TXDATAX(self.zz_rmio, self.zz_label)
        self.zz_rdict['TXDATAX'] = self.TXDATAX
        self.TXDATA = RM_Register_LEUART0_TXDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['TXDATA'] = self.TXDATA
        self.IF = RM_Register_LEUART0_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_LEUART0_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_LEUART0_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_LEUART0_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.PULSECTRL = RM_Register_LEUART0_PULSECTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PULSECTRL'] = self.PULSECTRL
        self.FREEZE = RM_Register_LEUART0_FREEZE(self.zz_rmio, self.zz_label)
        self.zz_rdict['FREEZE'] = self.FREEZE
        self.SYNCBUSY = RM_Register_LEUART0_SYNCBUSY(self.zz_rmio, self.zz_label)
        self.zz_rdict['SYNCBUSY'] = self.SYNCBUSY
        self.ROUTEPEN = RM_Register_LEUART0_ROUTEPEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTEPEN'] = self.ROUTEPEN
        self.ROUTELOC0 = RM_Register_LEUART0_ROUTELOC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC0'] = self.ROUTELOC0
        self.INPUT = RM_Register_LEUART0_INPUT(self.zz_rmio, self.zz_label)
        self.zz_rdict['INPUT'] = self.INPUT
        self.__dict__['zz_frozen'] = True