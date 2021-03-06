
__all__ = [ 'RM_Peripheral_CMU' ]

from static import Base_RM_Peripheral
from CMU_register import *

class RM_Peripheral_CMU(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_CMU, self).__init__(rmio, label,
            0x400E4000, 'CMU',
            "")
        self.CTRL = RM_Register_CMU_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.HFRCOCTRL = RM_Register_CMU_HFRCOCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFRCOCTRL'] = self.HFRCOCTRL
        self.HFRCOLDOCTRL = RM_Register_CMU_HFRCOLDOCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFRCOLDOCTRL'] = self.HFRCOLDOCTRL
        self.AUXHFRCOCTRL = RM_Register_CMU_AUXHFRCOCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['AUXHFRCOCTRL'] = self.AUXHFRCOCTRL
        self.AUXHFRCOLDOCTRL = RM_Register_CMU_AUXHFRCOLDOCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['AUXHFRCOLDOCTRL'] = self.AUXHFRCOLDOCTRL
        self.LFRCOCTRL = RM_Register_CMU_LFRCOCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['LFRCOCTRL'] = self.LFRCOCTRL
        self.HFXOCTRL = RM_Register_CMU_HFXOCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFXOCTRL'] = self.HFXOCTRL
        self.HFXOCTRL1 = RM_Register_CMU_HFXOCTRL1(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFXOCTRL1'] = self.HFXOCTRL1
        self.HFXOSTARTUPCTRL = RM_Register_CMU_HFXOSTARTUPCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFXOSTARTUPCTRL'] = self.HFXOSTARTUPCTRL
        self.HFXOSTEADYSTATECTRL = RM_Register_CMU_HFXOSTEADYSTATECTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFXOSTEADYSTATECTRL'] = self.HFXOSTEADYSTATECTRL
        self.HFXOTIMEOUTCTRL = RM_Register_CMU_HFXOTIMEOUTCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFXOTIMEOUTCTRL'] = self.HFXOTIMEOUTCTRL
        self.LFXOCTRL = RM_Register_CMU_LFXOCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['LFXOCTRL'] = self.LFXOCTRL
        self.ULFRCOCTRL = RM_Register_CMU_ULFRCOCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['ULFRCOCTRL'] = self.ULFRCOCTRL
        self.DPLLCTRL = RM_Register_CMU_DPLLCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['DPLLCTRL'] = self.DPLLCTRL
        self.DPLLCTRL1 = RM_Register_CMU_DPLLCTRL1(self.zz_rmio, self.zz_label)
        self.zz_rdict['DPLLCTRL1'] = self.DPLLCTRL1
        self.CALCTRL = RM_Register_CMU_CALCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CALCTRL'] = self.CALCTRL
        self.CALCNT = RM_Register_CMU_CALCNT(self.zz_rmio, self.zz_label)
        self.zz_rdict['CALCNT'] = self.CALCNT
        self.OSCENCMD = RM_Register_CMU_OSCENCMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['OSCENCMD'] = self.OSCENCMD
        self.CMD = RM_Register_CMU_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.DBGCLKSEL = RM_Register_CMU_DBGCLKSEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['DBGCLKSEL'] = self.DBGCLKSEL
        self.HFCLKSEL = RM_Register_CMU_HFCLKSEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFCLKSEL'] = self.HFCLKSEL
        self.LFACLKSEL = RM_Register_CMU_LFACLKSEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['LFACLKSEL'] = self.LFACLKSEL
        self.LFBCLKSEL = RM_Register_CMU_LFBCLKSEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['LFBCLKSEL'] = self.LFBCLKSEL
        self.LFECLKSEL = RM_Register_CMU_LFECLKSEL(self.zz_rmio, self.zz_label)
        self.zz_rdict['LFECLKSEL'] = self.LFECLKSEL
        self.STATUS = RM_Register_CMU_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.HFCLKSTATUS = RM_Register_CMU_HFCLKSTATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFCLKSTATUS'] = self.HFCLKSTATUS
        self.HFXOTRIMSTATUS = RM_Register_CMU_HFXOTRIMSTATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFXOTRIMSTATUS'] = self.HFXOTRIMSTATUS
        self.IF = RM_Register_CMU_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IFS = RM_Register_CMU_IFS(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFS'] = self.IFS
        self.IFC = RM_Register_CMU_IFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['IFC'] = self.IFC
        self.IEN = RM_Register_CMU_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.HFBUSCLKEN0 = RM_Register_CMU_HFBUSCLKEN0(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFBUSCLKEN0'] = self.HFBUSCLKEN0
        self.HFPERCLKEN0 = RM_Register_CMU_HFPERCLKEN0(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFPERCLKEN0'] = self.HFPERCLKEN0
        self.HFRADIOCLKEN0 = RM_Register_CMU_HFRADIOCLKEN0(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFRADIOCLKEN0'] = self.HFRADIOCLKEN0
        self.HFRADIOALTCLKEN0 = RM_Register_CMU_HFRADIOALTCLKEN0(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFRADIOALTCLKEN0'] = self.HFRADIOALTCLKEN0
        self.LFACLKEN0 = RM_Register_CMU_LFACLKEN0(self.zz_rmio, self.zz_label)
        self.zz_rdict['LFACLKEN0'] = self.LFACLKEN0
        self.LFBCLKEN0 = RM_Register_CMU_LFBCLKEN0(self.zz_rmio, self.zz_label)
        self.zz_rdict['LFBCLKEN0'] = self.LFBCLKEN0
        self.LFECLKEN0 = RM_Register_CMU_LFECLKEN0(self.zz_rmio, self.zz_label)
        self.zz_rdict['LFECLKEN0'] = self.LFECLKEN0
        self.HFPRESC = RM_Register_CMU_HFPRESC(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFPRESC'] = self.HFPRESC
        self.HFCOREPRESC = RM_Register_CMU_HFCOREPRESC(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFCOREPRESC'] = self.HFCOREPRESC
        self.HFPERPRESC = RM_Register_CMU_HFPERPRESC(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFPERPRESC'] = self.HFPERPRESC
        self.HFRADIOPRESC = RM_Register_CMU_HFRADIOPRESC(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFRADIOPRESC'] = self.HFRADIOPRESC
        self.HFEXPPRESC = RM_Register_CMU_HFEXPPRESC(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFEXPPRESC'] = self.HFEXPPRESC
        self.LFAPRESC0 = RM_Register_CMU_LFAPRESC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['LFAPRESC0'] = self.LFAPRESC0
        self.LFBPRESC0 = RM_Register_CMU_LFBPRESC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['LFBPRESC0'] = self.LFBPRESC0
        self.LFEPRESC0 = RM_Register_CMU_LFEPRESC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['LFEPRESC0'] = self.LFEPRESC0
        self.HFRADIOALTPRESC = RM_Register_CMU_HFRADIOALTPRESC(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFRADIOALTPRESC'] = self.HFRADIOALTPRESC
        self.SYNCBUSY = RM_Register_CMU_SYNCBUSY(self.zz_rmio, self.zz_label)
        self.zz_rdict['SYNCBUSY'] = self.SYNCBUSY
        self.FREEZE = RM_Register_CMU_FREEZE(self.zz_rmio, self.zz_label)
        self.zz_rdict['FREEZE'] = self.FREEZE
        self.PCNTCTRL = RM_Register_CMU_PCNTCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PCNTCTRL'] = self.PCNTCTRL
        self.LVDSCTRL = RM_Register_CMU_LVDSCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['LVDSCTRL'] = self.LVDSCTRL
        self.ADCCTRL = RM_Register_CMU_ADCCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADCCTRL'] = self.ADCCTRL
        self.ROUTEPEN = RM_Register_CMU_ROUTEPEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTEPEN'] = self.ROUTEPEN
        self.ROUTELOC0 = RM_Register_CMU_ROUTELOC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC0'] = self.ROUTELOC0
        self.ROUTELOC1 = RM_Register_CMU_ROUTELOC1(self.zz_rmio, self.zz_label)
        self.zz_rdict['ROUTELOC1'] = self.ROUTELOC1
        self.LOCK = RM_Register_CMU_LOCK(self.zz_rmio, self.zz_label)
        self.zz_rdict['LOCK'] = self.LOCK
        self.HFRCOSS = RM_Register_CMU_HFRCOSS(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFRCOSS'] = self.HFRCOSS
        self.RFLOCK0 = RM_Register_CMU_RFLOCK0(self.zz_rmio, self.zz_label)
        self.zz_rdict['RFLOCK0'] = self.RFLOCK0
        self.HFBUSCLKENMASK0 = RM_Register_CMU_HFBUSCLKENMASK0(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFBUSCLKENMASK0'] = self.HFBUSCLKENMASK0
        self.HFCORECLKENMASK0 = RM_Register_CMU_HFCORECLKENMASK0(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFCORECLKENMASK0'] = self.HFCORECLKENMASK0
        self.HFPERCLKENMASK0 = RM_Register_CMU_HFPERCLKENMASK0(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFPERCLKENMASK0'] = self.HFPERCLKENMASK0
        self.HFRADIOCLKENMASK0 = RM_Register_CMU_HFRADIOCLKENMASK0(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFRADIOCLKENMASK0'] = self.HFRADIOCLKENMASK0
        self.HFRADIOALTCLKENMASK0 = RM_Register_CMU_HFRADIOALTCLKENMASK0(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFRADIOALTCLKENMASK0'] = self.HFRADIOALTCLKENMASK0
        self.HFUNDIVCLKENMASK0 = RM_Register_CMU_HFUNDIVCLKENMASK0(self.zz_rmio, self.zz_label)
        self.zz_rdict['HFUNDIVCLKENMASK0'] = self.HFUNDIVCLKENMASK0
        self.LFACLKENMASK0 = RM_Register_CMU_LFACLKENMASK0(self.zz_rmio, self.zz_label)
        self.zz_rdict['LFACLKENMASK0'] = self.LFACLKENMASK0
        self.LFBCLKENMASK0 = RM_Register_CMU_LFBCLKENMASK0(self.zz_rmio, self.zz_label)
        self.zz_rdict['LFBCLKENMASK0'] = self.LFBCLKENMASK0
        self.LFECLKENMASK0 = RM_Register_CMU_LFECLKENMASK0(self.zz_rmio, self.zz_label)
        self.zz_rdict['LFECLKENMASK0'] = self.LFECLKENMASK0
        self.PCNTCLKENMASK = RM_Register_CMU_PCNTCLKENMASK(self.zz_rmio, self.zz_label)
        self.zz_rdict['PCNTCLKENMASK'] = self.PCNTCLKENMASK
        self.TEST = RM_Register_CMU_TEST(self.zz_rmio, self.zz_label)
        self.zz_rdict['TEST'] = self.TEST
        self.TESTHFRCOCTRL = RM_Register_CMU_TESTHFRCOCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['TESTHFRCOCTRL'] = self.TESTHFRCOCTRL
        self.TESTAUXHFRCOCTRL = RM_Register_CMU_TESTAUXHFRCOCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['TESTAUXHFRCOCTRL'] = self.TESTAUXHFRCOCTRL
        self.TESTLFRCOCTRL = RM_Register_CMU_TESTLFRCOCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['TESTLFRCOCTRL'] = self.TESTLFRCOCTRL
        self.TESTHFXOCTRL = RM_Register_CMU_TESTHFXOCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['TESTHFXOCTRL'] = self.TESTHFXOCTRL
        self.TESTLFXOCTRL = RM_Register_CMU_TESTLFXOCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['TESTLFXOCTRL'] = self.TESTLFXOCTRL
        self.DPLLOFFSET = RM_Register_CMU_DPLLOFFSET(self.zz_rmio, self.zz_label)
        self.zz_rdict['DPLLOFFSET'] = self.DPLLOFFSET
        self.__dict__['zz_frozen'] = True