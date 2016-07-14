
__all__ = [ 'RM_Peripheral_I2C0' ]

from static import Base_RM_Peripheral
from I2C0_register import *

class RM_Peripheral_I2C0(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_I2C0, self).__init__(rmio, label,
            0x4000C000, 'I2C0',
            "")
        self.CTRL = RM_Register_I2C0_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.CMD = RM_Register_I2C0_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.STATE = RM_Register_I2C0_STATE(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATE'] = self.STATE
        self.STATUS = RM_Register_I2C0_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.CLKDIV = RM_Register_I2C0_CLKDIV(self.zz_rmio, self.zz_label)
        self.zz_rdict['CLKDIV'] = self.CLKDIV
        self.SADDR = RM_Register_I2C0_SADDR(self.zz_rmio, self.zz_label)
        self.zz_rdict['SADDR'] = self.SADDR
        self.SADDRMASK = RM_Register_I2C0_SADDRMASK(self.zz_rmio, self.zz_label)
        self.zz_rdict['SADDRMASK'] = self.SADDRMASK
        self.RXDATA = RM_Register_I2C0_RXDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXDATA'] = self.RXDATA
        self.RXDOUBLE = RM_Register_I2C0_RXDOUBLE(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXDOUBLE'] = self.RXDOUBLE
        self.RXDATAP = RM_Register_I2C0_RXDATAP(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXDATAP'] = self.RXDATAP
        self.RXDOUBLEP = RM_Register_I2C0_RXDOUBLEP(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXDOUBLEP'] = self.RXDOUBLEP
        self.TXDATA = RM_Register_I2C0_TXDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['TXDATA'] = self.TXDATA
        self.TXDOUBLE = RM_Register_I2C0_TXDOUBLE(self.zz_rmio, self.zz_label)
        self.zz_rdict['TXDOUBLE'] = self.TXDOUBLE
        self.IF = RM_Register_I2C0_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_I2C0_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_I2C0_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_I2C0_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.ROUTEPEN = RM_Register_I2C0_ROUTEPEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTEPEN'] = self.ROUTEPEN
        self.ROUTELOC0 = RM_Register_I2C0_ROUTELOC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC0'] = self.ROUTELOC0
        self.__dict__['zz_frozen'] = True