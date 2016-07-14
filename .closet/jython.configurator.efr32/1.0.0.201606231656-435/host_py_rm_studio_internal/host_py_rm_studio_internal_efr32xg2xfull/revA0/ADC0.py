
__all__ = [ 'RM_Peripheral_ADC0' ]

from static import Base_RM_Peripheral
from ADC0_register import *

class RM_Peripheral_ADC0(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_ADC0, self).__init__(rmio, label,
            0x40002000, 'ADC0',
            "")
        self.CTRL = RM_Register_ADC0_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.CMD = RM_Register_ADC0_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.STATUS = RM_Register_ADC0_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.SINGLECTRL = RM_Register_ADC0_SINGLECTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['SINGLECTRL'] = self.SINGLECTRL
        self.SINGLECTRLX = RM_Register_ADC0_SINGLECTRLX(self.zz_rmio, self.zz_label)
        self.zz_rdict['SINGLECTRLX'] = self.SINGLECTRLX
        self.SCANCTRL = RM_Register_ADC0_SCANCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANCTRL'] = self.SCANCTRL
        self.SCANCTRLX = RM_Register_ADC0_SCANCTRLX(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANCTRLX'] = self.SCANCTRLX
        self.SCANMASK = RM_Register_ADC0_SCANMASK(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANMASK'] = self.SCANMASK
        self.SCANINPUTSEL = RM_Register_ADC0_SCANINPUTSEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANINPUTSEL'] = self.SCANINPUTSEL
        self.SCANNEGSEL = RM_Register_ADC0_SCANNEGSEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANNEGSEL'] = self.SCANNEGSEL
        self.CMPTHR = RM_Register_ADC0_CMPTHR(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMPTHR'] = self.CMPTHR
        self.BIASPROG = RM_Register_ADC0_BIASPROG(self.zz_rmio, self.zz_label)
        self.zz_rdict['BIASPROG'] = self.BIASPROG
        self.CAL = RM_Register_ADC0_CAL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CAL'] = self.CAL
        self.IF = RM_Register_ADC0_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_ADC0_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_ADC0_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_ADC0_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.SINGLEDATA = RM_Register_ADC0_SINGLEDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['SINGLEDATA'] = self.SINGLEDATA
        self.SCANDATA = RM_Register_ADC0_SCANDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANDATA'] = self.SCANDATA
        self.SINGLEDATAP = RM_Register_ADC0_SINGLEDATAP(self.zz_rmio, self.zz_label)
        self.zz_rdict['SINGLEDATAP'] = self.SINGLEDATAP
        self.SCANDATAP = RM_Register_ADC0_SCANDATAP(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANDATAP'] = self.SCANDATAP
        self.SCANDATAX = RM_Register_ADC0_SCANDATAX(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANDATAX'] = self.SCANDATAX
        self.SCANDATAXP = RM_Register_ADC0_SCANDATAXP(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANDATAXP'] = self.SCANDATAXP
        self.TEST = RM_Register_ADC0_TEST(self.zz_rmio, self.zz_label)
        self.zz_rdict['TEST'] = self.TEST
        self.APORTREQ = RM_Register_ADC0_APORTREQ(self.zz_rmio, self.zz_label)
        self.zz_rdict['APORTREQ'] = self.APORTREQ
        self.APORTCONFLICT = RM_Register_ADC0_APORTCONFLICT(self.zz_rmio, self.zz_label)
        self.zz_rdict['APORTCONFLICT'] = self.APORTCONFLICT
        self.SINGLEFIFOCOUNT = RM_Register_ADC0_SINGLEFIFOCOUNT(self.zz_rmio, self.zz_label)
        self.zz_rdict['SINGLEFIFOCOUNT'] = self.SINGLEFIFOCOUNT
        self.SCANFIFOCOUNT = RM_Register_ADC0_SCANFIFOCOUNT(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANFIFOCOUNT'] = self.SCANFIFOCOUNT
        self.SINGLEFIFOCLEAR = RM_Register_ADC0_SINGLEFIFOCLEAR(self.zz_rmio, self.zz_label)
        self.zz_rdict['SINGLEFIFOCLEAR'] = self.SINGLEFIFOCLEAR
        self.SCANFIFOCLEAR = RM_Register_ADC0_SCANFIFOCLEAR(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCANFIFOCLEAR'] = self.SCANFIFOCLEAR
        self.APORTMASTERDIS = RM_Register_ADC0_APORTMASTERDIS(self.zz_rmio, self.zz_label)
        self.zz_rdict['APORTMASTERDIS'] = self.APORTMASTERDIS
        self.__dict__['zz_frozen'] = True