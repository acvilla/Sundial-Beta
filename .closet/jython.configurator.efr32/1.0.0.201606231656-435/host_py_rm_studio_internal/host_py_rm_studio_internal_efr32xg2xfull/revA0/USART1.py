
__all__ = [ 'RM_Peripheral_USART1' ]

from static import Base_RM_Peripheral
from USART1_register import *

class RM_Peripheral_USART1(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_USART1, self).__init__(rmio, label,
            0x40010400, 'USART1',
            "")
        self.CTRL = RM_Register_USART1_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.FRAME = RM_Register_USART1_FRAME(self.zz_rmio, self.zz_label)
        self.zz_rdict['FRAME'] = self.FRAME
        self.TRIGCTRL = RM_Register_USART1_TRIGCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['TRIGCTRL'] = self.TRIGCTRL
        self.CMD = RM_Register_USART1_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.STATUS = RM_Register_USART1_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.CLKDIV = RM_Register_USART1_CLKDIV(self.zz_rmio, self.zz_label)
        self.zz_rdict['CLKDIV'] = self.CLKDIV
        self.RXDATAX = RM_Register_USART1_RXDATAX(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXDATAX'] = self.RXDATAX
        self.RXDATA = RM_Register_USART1_RXDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXDATA'] = self.RXDATA
        self.RXDOUBLEX = RM_Register_USART1_RXDOUBLEX(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXDOUBLEX'] = self.RXDOUBLEX
        self.RXDOUBLE = RM_Register_USART1_RXDOUBLE(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXDOUBLE'] = self.RXDOUBLE
        self.RXDATAXP = RM_Register_USART1_RXDATAXP(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXDATAXP'] = self.RXDATAXP
        self.RXDOUBLEXP = RM_Register_USART1_RXDOUBLEXP(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXDOUBLEXP'] = self.RXDOUBLEXP
        self.TXDATAX = RM_Register_USART1_TXDATAX(self.zz_rmio, self.zz_label)
        self.zz_rdict['TXDATAX'] = self.TXDATAX
        self.TXDATA = RM_Register_USART1_TXDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['TXDATA'] = self.TXDATA
        self.TXDOUBLEX = RM_Register_USART1_TXDOUBLEX(self.zz_rmio, self.zz_label)
        self.zz_rdict['TXDOUBLEX'] = self.TXDOUBLEX
        self.TXDOUBLE = RM_Register_USART1_TXDOUBLE(self.zz_rmio, self.zz_label)
        self.zz_rdict['TXDOUBLE'] = self.TXDOUBLE
        self.IF = RM_Register_USART1_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_USART1_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_USART1_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_USART1_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.IRCTRL = RM_Register_USART1_IRCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['IRCTRL'] = self.IRCTRL
        self.INPUT = RM_Register_USART1_INPUT(self.zz_rmio, self.zz_label)
        self.zz_rdict['INPUT'] = self.INPUT
        self.I2SCTRL = RM_Register_USART1_I2SCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['I2SCTRL'] = self.I2SCTRL
        self.TIMING = RM_Register_USART1_TIMING(self.zz_rmio, self.zz_label)
        self.zz_rdict['TIMING'] = self.TIMING
        self.CTRLX = RM_Register_USART1_CTRLX(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRLX'] = self.CTRLX
        self.TIMECMP0 = RM_Register_USART1_TIMECMP0(self.zz_rmio, self.zz_label)
        self.zz_rdict['TIMECMP0'] = self.TIMECMP0
        self.TIMECMP1 = RM_Register_USART1_TIMECMP1(self.zz_rmio, self.zz_label)
        self.zz_rdict['TIMECMP1'] = self.TIMECMP1
        self.TIMECMP2 = RM_Register_USART1_TIMECMP2(self.zz_rmio, self.zz_label)
        self.zz_rdict['TIMECMP2'] = self.TIMECMP2
        self.ROUTEPEN = RM_Register_USART1_ROUTEPEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTEPEN'] = self.ROUTEPEN
        self.ROUTELOC0 = RM_Register_USART1_ROUTELOC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC0'] = self.ROUTELOC0
        self.ROUTELOC1 = RM_Register_USART1_ROUTELOC1(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC1'] = self.ROUTELOC1
        self.TEST = RM_Register_USART1_TEST(self.zz_rmio, self.zz_label)
        self.zz_rdict['TEST'] = self.TEST
        self.__dict__['zz_frozen'] = True