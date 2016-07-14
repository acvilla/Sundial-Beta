
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_EMU_LOCK_LOCKKEY(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.UNLOCKED = 0x00000000
        zz_edict['UNLOCKED'] = self.UNLOCKED
        zz_desc['UNLOCKED'] = ""
        self.LOCKED = 0x00000001
        zz_edict['LOCKED'] = self.LOCKED
        zz_desc['LOCKED'] = ""
        super(RM_Enum_EMU_LOCK_LOCKKEY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_MEMCTRL_RAMPOWERDOWN(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.BLK4 = 0x00000008
        zz_edict['BLK4'] = self.BLK4
        zz_desc['BLK4'] = ""
        self.BLK34 = 0x0000000C
        zz_edict['BLK34'] = self.BLK34
        zz_desc['BLK34'] = ""
        self.BLK234 = 0x0000000E
        zz_edict['BLK234'] = self.BLK234
        zz_desc['BLK234'] = ""
        self.BLK1234 = 0x0000000F
        zz_edict['BLK1234'] = self.BLK1234
        zz_desc['BLK1234'] = ""
        super(RM_Enum_EMU_MEMCTRL_RAMPOWERDOWN, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_EM4CTRL_EM4IO0RETMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.EM4EXIT = 0x00000001
        zz_edict['EM4EXIT'] = self.EM4EXIT
        zz_desc['EM4EXIT'] = ""
        self.SWUNLATCH = 0x00000002
        zz_edict['SWUNLATCH'] = self.SWUNLATCH
        zz_desc['SWUNLATCH'] = ""
        super(RM_Enum_EMU_EM4CTRL_EM4IO0RETMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_PWRLOCK_LOCKKEY(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.UNLOCKED = 0x00000000
        zz_edict['UNLOCKED'] = self.UNLOCKED
        zz_desc['UNLOCKED'] = ""
        self.LOCKED = 0x00000001
        zz_edict['LOCKED'] = self.LOCKED
        zz_desc['LOCKED'] = ""
        super(RM_Enum_EMU_PWRLOCK_LOCKKEY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_PWRCFG_PWRCFG(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.STARTUP = 0x00000000
        zz_edict['STARTUP'] = self.STARTUP
        zz_desc['STARTUP'] = ""
        self.NODCDC = 0x00000001
        zz_edict['NODCDC'] = self.NODCDC
        zz_desc['NODCDC'] = ""
        self.DCDCTODVDD = 0x00000002
        zz_edict['DCDCTODVDD'] = self.DCDCTODVDD
        zz_desc['DCDCTODVDD'] = ""
        self.DCDCTODECOUPLE = 0x00000003
        zz_edict['DCDCTODECOUPLE'] = self.DCDCTODECOUPLE
        zz_desc['DCDCTODECOUPLE'] = ""
        self.SOFTWARE = 0x0000000F
        zz_edict['SOFTWARE'] = self.SOFTWARE
        zz_desc['SOFTWARE'] = ""
        super(RM_Enum_EMU_PWRCFG_PWRCFG, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_PWRCTRL_PROBE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.AVDD = 0x00000002
        zz_edict['AVDD'] = self.AVDD
        zz_desc['AVDD'] = ""
        self.BU = 0x00000003
        zz_edict['BU'] = self.BU
        zz_desc['BU'] = ""
        self.DVDD = 0x00000004
        zz_edict['DVDD'] = self.DVDD
        zz_desc['DVDD'] = ""
        self.IO0 = 0x00000005
        zz_edict['IO0'] = self.IO0
        zz_desc['IO0'] = ""
        super(RM_Enum_EMU_PWRCTRL_PROBE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_DCDCCTRL_DCDCMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BYPASS = 0x00000000
        zz_edict['BYPASS'] = self.BYPASS
        zz_desc['BYPASS'] = ""
        self.LOWNOISE = 0x00000001
        zz_edict['LOWNOISE'] = self.LOWNOISE
        zz_desc['LOWNOISE'] = ""
        self.LOWPOWER = 0x00000002
        zz_edict['LOWPOWER'] = self.LOWPOWER
        zz_desc['LOWPOWER'] = ""
        self.OFF = 0x00000003
        zz_edict['OFF'] = self.OFF
        zz_desc['OFF'] = ""
        super(RM_Enum_EMU_DCDCCTRL_DCDCMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_DCDCMISCCTRL_LPCMPBIAS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BIAS0 = 0x00000000
        zz_edict['BIAS0'] = self.BIAS0
        zz_desc['BIAS0'] = ""
        self.BIAS1 = 0x00000001
        zz_edict['BIAS1'] = self.BIAS1
        zz_desc['BIAS1'] = ""
        self.BIAS2 = 0x00000002
        zz_edict['BIAS2'] = self.BIAS2
        zz_desc['BIAS2'] = ""
        self.BIAS3 = 0x00000003
        zz_edict['BIAS3'] = self.BIAS3
        zz_desc['BIAS3'] = ""
        super(RM_Enum_EMU_DCDCMISCCTRL_LPCMPBIAS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_DCDCTIMING_DUTYSCALE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIV1 = 0x00000000
        zz_edict['DIV1'] = self.DIV1
        zz_desc['DIV1'] = ""
        self.DIV2 = 0x00000001
        zz_edict['DIV2'] = self.DIV2
        zz_desc['DIV2'] = ""
        self.DIV4 = 0x00000002
        zz_edict['DIV4'] = self.DIV4
        zz_desc['DIV4'] = ""
        self.DIV8 = 0x00000003
        zz_edict['DIV8'] = self.DIV8
        zz_desc['DIV8'] = ""
        super(RM_Enum_EMU_DCDCTIMING_DUTYSCALE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_DCDCLPFREQCTRL_LPOSCDIV(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIV1 = 0x00000000
        zz_edict['DIV1'] = self.DIV1
        zz_desc['DIV1'] = ""
        self.DIV2 = 0x00000001
        zz_edict['DIV2'] = self.DIV2
        zz_desc['DIV2'] = ""
        self.DIV4 = 0x00000002
        zz_edict['DIV4'] = self.DIV4
        zz_desc['DIV4'] = ""
        self.DIV8 = 0x00000003
        zz_edict['DIV8'] = self.DIV8
        zz_desc['DIV8'] = ""
        super(RM_Enum_EMU_DCDCLPFREQCTRL_LPOSCDIV, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_DCDCRCOSC_RCOHOPPERIOD(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.HOP1 = 0x00000000
        zz_edict['HOP1'] = self.HOP1
        zz_desc['HOP1'] = ""
        self.HOP2 = 0x00000001
        zz_edict['HOP2'] = self.HOP2
        zz_desc['HOP2'] = ""
        self.HOP4 = 0x00000002
        zz_edict['HOP4'] = self.HOP4
        zz_desc['HOP4'] = ""
        self.HOP8 = 0x00000003
        zz_edict['HOP8'] = self.HOP8
        zz_desc['HOP8'] = ""
        super(RM_Enum_EMU_DCDCRCOSC_RCOHOPPERIOD, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_VMONCTRL_REFRESHRATE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '1KHZ' to 'E1KHZ'")
        self.E1KHZ = 0x00000000
        zz_edict['E1KHZ'] = self.E1KHZ
        zz_desc['E1KHZ'] = ""
        #print("WARNING: Aliasing enum '500HZ' to 'E500HZ'")
        self.E500HZ = 0x00000001
        zz_edict['E500HZ'] = self.E500HZ
        zz_desc['E500HZ'] = ""
        #print("WARNING: Aliasing enum '250HZ' to 'E250HZ'")
        self.E250HZ = 0x00000002
        zz_edict['E250HZ'] = self.E250HZ
        zz_desc['E250HZ'] = ""
        #print("WARNING: Aliasing enum '125HZ' to 'E125HZ'")
        self.E125HZ = 0x00000003
        zz_edict['E125HZ'] = self.E125HZ
        zz_desc['E125HZ'] = ""
        super(RM_Enum_EMU_VMONCTRL_REFRESHRATE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_PORBODREFRESH_PORBOD_REFRESHRATE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '1KHZ' to 'E1KHZ'")
        self.E1KHZ = 0x00000000
        zz_edict['E1KHZ'] = self.E1KHZ
        zz_desc['E1KHZ'] = ""
        #print("WARNING: Aliasing enum '500HZ' to 'E500HZ'")
        self.E500HZ = 0x00000001
        zz_edict['E500HZ'] = self.E500HZ
        zz_desc['E500HZ'] = ""
        #print("WARNING: Aliasing enum '250HZ' to 'E250HZ'")
        self.E250HZ = 0x00000002
        zz_edict['E250HZ'] = self.E250HZ
        zz_desc['E250HZ'] = ""
        #print("WARNING: Aliasing enum '125HZ' to 'E125HZ'")
        self.E125HZ = 0x00000003
        zz_edict['E125HZ'] = self.E125HZ
        zz_desc['E125HZ'] = ""
        super(RM_Enum_EMU_PORBODREFRESH_PORBOD_REFRESHRATE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_MEMFEATURE_RAM0DIV(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIV1 = 0x00000000
        zz_edict['DIV1'] = self.DIV1
        zz_desc['DIV1'] = ""
        self.DIV2 = 0x00000001
        zz_edict['DIV2'] = self.DIV2
        zz_desc['DIV2'] = ""
        self.DIV4 = 0x00000002
        zz_edict['DIV4'] = self.DIV4
        zz_desc['DIV4'] = ""
        self.DIV8 = 0x00000003
        zz_edict['DIV8'] = self.DIV8
        zz_desc['DIV8'] = ""
        super(RM_Enum_EMU_MEMFEATURE_RAM0DIV, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_MEMFEATURE_RAMSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.RAM0 = 0x00000001
        zz_edict['RAM0'] = self.RAM0
        zz_desc['RAM0'] = ""
        self.RAM01 = 0x00000003
        zz_edict['RAM01'] = self.RAM01
        zz_desc['RAM01'] = ""
        self.RAM012 = 0x00000007
        zz_edict['RAM012'] = self.RAM012
        zz_desc['RAM012'] = ""
        self.RAM0123 = 0x0000000F
        zz_edict['RAM0123'] = self.RAM0123
        zz_desc['RAM0123'] = ""
        self.RAM01234 = 0x0000001F
        zz_edict['RAM01234'] = self.RAM01234
        zz_desc['RAM01234'] = ""
        super(RM_Enum_EMU_MEMFEATURE_RAMSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_TESTLOCK_LOCKKEY(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.UNLOCKED = 0x00000000
        zz_edict['UNLOCKED'] = self.UNLOCKED
        zz_desc['UNLOCKED'] = ""
        self.LOCKED = 0x00000001
        zz_edict['LOCKED'] = self.LOCKED
        zz_desc['LOCKED'] = ""
        super(RM_Enum_EMU_TESTLOCK_LOCKKEY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_TESTCTRL_CMCTRLPRSSEL0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.POR = 0x00000000
        zz_edict['POR'] = self.POR
        zz_desc['POR'] = ""
        self.AVDDEM4BOD = 0x00000001
        zz_edict['AVDDEM4BOD'] = self.AVDDEM4BOD
        zz_desc['AVDDEM4BOD'] = ""
        self.AVDDBOD = 0x00000002
        zz_edict['AVDDBOD'] = self.AVDDBOD
        zz_desc['AVDDBOD'] = ""
        self.DVDDBOD = 0x00000003
        zz_edict['DVDDBOD'] = self.DVDDBOD
        zz_desc['DVDDBOD'] = ""
        self.FLASHBOD = 0x00000004
        zz_edict['FLASHBOD'] = self.FLASHBOD
        zz_desc['FLASHBOD'] = ""
        self.DEC0BOD = 0x00000005
        zz_edict['DEC0BOD'] = self.DEC0BOD
        zz_desc['DEC0BOD'] = ""
        self.DEC1BOD = 0x00000006
        zz_edict['DEC1BOD'] = self.DEC1BOD
        zz_desc['DEC1BOD'] = ""
        self.VMONAVDD = 0x00000007
        zz_edict['VMONAVDD'] = self.VMONAVDD
        zz_desc['VMONAVDD'] = ""
        self.VMONALTAVDD = 0x00000008
        zz_edict['VMONALTAVDD'] = self.VMONALTAVDD
        zz_desc['VMONALTAVDD'] = ""
        self.VMONDVDD = 0x00000009
        zz_edict['VMONDVDD'] = self.VMONDVDD
        zz_desc['VMONDVDD'] = ""
        self.VMONIO0 = 0x0000000A
        zz_edict['VMONIO0'] = self.VMONIO0
        zz_desc['VMONIO0'] = ""
        self.VMONPAVDD = 0x0000000B
        zz_edict['VMONPAVDD'] = self.VMONPAVDD
        zz_desc['VMONPAVDD'] = ""
        self.VMONFVDD = 0x0000000C
        zz_edict['VMONFVDD'] = self.VMONFVDD
        zz_desc['VMONFVDD'] = ""
        self.LEGACYPOR = 0x0000000D
        zz_edict['LEGACYPOR'] = self.LEGACYPOR
        zz_desc['LEGACYPOR'] = ""
        self.BIASRDY = 0x0000000E
        zz_edict['BIASRDY'] = self.BIASRDY
        zz_desc['BIASRDY'] = ""
        self.DCDCCMPRAW = 0x0000000F
        zz_edict['DCDCCMPRAW'] = self.DCDCCMPRAW
        zz_desc['DCDCCMPRAW'] = ""
        self.DCDCCMPOUT = 0x00000010
        zz_edict['DCDCCMPOUT'] = self.DCDCCMPOUT
        zz_desc['DCDCCMPOUT'] = ""
        self.DCDCTESTCLK = 0x00000011
        zz_edict['DCDCTESTCLK'] = self.DCDCTESTCLK
        zz_desc['DCDCTESTCLK'] = ""
        self.DCDCRCOCAL = 0x00000012
        zz_edict['DCDCRCOCAL'] = self.DCDCRCOCAL
        zz_desc['DCDCRCOCAL'] = ""
        self.EM01ACTIVE = 0x00000013
        zz_edict['EM01ACTIVE'] = self.EM01ACTIVE
        zz_desc['EM01ACTIVE'] = ""
        self.EM23REQ = 0x00000014
        zz_edict['EM23REQ'] = self.EM23REQ
        zz_desc['EM23REQ'] = ""
        self.EM23ACTIVE = 0x00000015
        zz_edict['EM23ACTIVE'] = self.EM23ACTIVE
        zz_desc['EM23ACTIVE'] = ""
        self.EM4ACTIVE = 0x00000016
        zz_edict['EM4ACTIVE'] = self.EM4ACTIVE
        zz_desc['EM4ACTIVE'] = ""
        self.HDREGBIAS = 0x00000017
        zz_edict['HDREGBIAS'] = self.HDREGBIAS
        zz_desc['HDREGBIAS'] = ""
        self.HDREGFUNC = 0x00000018
        zz_edict['HDREGFUNC'] = self.HDREGFUNC
        zz_desc['HDREGFUNC'] = ""
        self.HDREGVREG  = 0x00000019
        zz_edict['HDREGVREG '] = self.HDREGVREG 
        zz_desc['HDREGVREG '] = ""
        self.HDREGVREGRDY = 0x0000001A
        zz_edict['HDREGVREGRDY'] = self.HDREGVREGRDY
        zz_desc['HDREGVREGRDY'] = ""
        self.HDREGSW = 0x0000001B
        zz_edict['HDREGSW'] = self.HDREGSW
        zz_desc['HDREGSW'] = ""
        self.LDREGEN = 0x0000001C
        zz_edict['LDREGEN'] = self.LDREGEN
        zz_desc['LDREGEN'] = ""
        self.LDREGSW = 0x0000001D
        zz_edict['LDREGSW'] = self.LDREGSW
        zz_desc['LDREGSW'] = ""
        self.EMUOSC = 0x0000001E
        zz_edict['EMUOSC'] = self.EMUOSC
        zz_desc['EMUOSC'] = ""
        super(RM_Enum_EMU_TESTCTRL_CMCTRLPRSSEL0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_TESTCTRL_CMCTRLPRSSEL1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.POR = 0x00000000
        zz_edict['POR'] = self.POR
        zz_desc['POR'] = ""
        self.AVDDEM4BOD = 0x00000001
        zz_edict['AVDDEM4BOD'] = self.AVDDEM4BOD
        zz_desc['AVDDEM4BOD'] = ""
        self.AVDDBOD = 0x00000002
        zz_edict['AVDDBOD'] = self.AVDDBOD
        zz_desc['AVDDBOD'] = ""
        self.DVDDBOD = 0x00000003
        zz_edict['DVDDBOD'] = self.DVDDBOD
        zz_desc['DVDDBOD'] = ""
        self.FLASHBOD = 0x00000004
        zz_edict['FLASHBOD'] = self.FLASHBOD
        zz_desc['FLASHBOD'] = ""
        self.DEC0BOD = 0x00000005
        zz_edict['DEC0BOD'] = self.DEC0BOD
        zz_desc['DEC0BOD'] = ""
        self.DEC1BOD = 0x00000006
        zz_edict['DEC1BOD'] = self.DEC1BOD
        zz_desc['DEC1BOD'] = ""
        self.VMONAVDD = 0x00000007
        zz_edict['VMONAVDD'] = self.VMONAVDD
        zz_desc['VMONAVDD'] = ""
        self.VMONALTAVDD = 0x00000008
        zz_edict['VMONALTAVDD'] = self.VMONALTAVDD
        zz_desc['VMONALTAVDD'] = ""
        self.VMONDVDD = 0x00000009
        zz_edict['VMONDVDD'] = self.VMONDVDD
        zz_desc['VMONDVDD'] = ""
        self.VMONIO0 = 0x0000000A
        zz_edict['VMONIO0'] = self.VMONIO0
        zz_desc['VMONIO0'] = ""
        self.VMONPAVDD = 0x0000000B
        zz_edict['VMONPAVDD'] = self.VMONPAVDD
        zz_desc['VMONPAVDD'] = ""
        self.VMONFVDD = 0x0000000C
        zz_edict['VMONFVDD'] = self.VMONFVDD
        zz_desc['VMONFVDD'] = ""
        self.LEGACYPOR = 0x0000000D
        zz_edict['LEGACYPOR'] = self.LEGACYPOR
        zz_desc['LEGACYPOR'] = ""
        self.BIASRDY = 0x0000000E
        zz_edict['BIASRDY'] = self.BIASRDY
        zz_desc['BIASRDY'] = ""
        self.DCDCCMPRAW = 0x0000000F
        zz_edict['DCDCCMPRAW'] = self.DCDCCMPRAW
        zz_desc['DCDCCMPRAW'] = ""
        self.DCDCCMPOUT = 0x00000010
        zz_edict['DCDCCMPOUT'] = self.DCDCCMPOUT
        zz_desc['DCDCCMPOUT'] = ""
        self.DCDCTESTCLK = 0x00000011
        zz_edict['DCDCTESTCLK'] = self.DCDCTESTCLK
        zz_desc['DCDCTESTCLK'] = ""
        self.DCDCRCOCAL = 0x00000012
        zz_edict['DCDCRCOCAL'] = self.DCDCRCOCAL
        zz_desc['DCDCRCOCAL'] = ""
        self.EM01ACTIVE = 0x00000013
        zz_edict['EM01ACTIVE'] = self.EM01ACTIVE
        zz_desc['EM01ACTIVE'] = ""
        self.EM23REQ = 0x00000014
        zz_edict['EM23REQ'] = self.EM23REQ
        zz_desc['EM23REQ'] = ""
        self.EM23ACTIVE = 0x00000015
        zz_edict['EM23ACTIVE'] = self.EM23ACTIVE
        zz_desc['EM23ACTIVE'] = ""
        self.EM4ACTIVE = 0x00000016
        zz_edict['EM4ACTIVE'] = self.EM4ACTIVE
        zz_desc['EM4ACTIVE'] = ""
        self.HDREGBIAS = 0x00000017
        zz_edict['HDREGBIAS'] = self.HDREGBIAS
        zz_desc['HDREGBIAS'] = ""
        self.HDREGFUNC = 0x00000018
        zz_edict['HDREGFUNC'] = self.HDREGFUNC
        zz_desc['HDREGFUNC'] = ""
        self.HDREGVREG  = 0x00000019
        zz_edict['HDREGVREG '] = self.HDREGVREG 
        zz_desc['HDREGVREG '] = ""
        self.HDREGVREGRDY = 0x0000001A
        zz_edict['HDREGVREGRDY'] = self.HDREGVREGRDY
        zz_desc['HDREGVREGRDY'] = ""
        self.HDREGSW = 0x0000001B
        zz_edict['HDREGSW'] = self.HDREGSW
        zz_desc['HDREGSW'] = ""
        self.LDREGEN = 0x0000001C
        zz_edict['LDREGEN'] = self.LDREGEN
        zz_desc['LDREGEN'] = ""
        self.LDREGSW = 0x0000001D
        zz_edict['LDREGSW'] = self.LDREGSW
        zz_desc['LDREGSW'] = ""
        self.EMUOSC = 0x0000001E
        zz_edict['EMUOSC'] = self.EMUOSC
        zz_desc['EMUOSC'] = ""
        super(RM_Enum_EMU_TESTCTRL_CMCTRLPRSSEL1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_DIAGABLKTPSEL_GPBLK(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.ULFRCO = 0x00000001
        zz_edict['ULFRCO'] = self.ULFRCO
        zz_desc['ULFRCO'] = ""
        self.LFRCO = 0x00000002
        zz_edict['LFRCO'] = self.LFRCO
        zz_desc['LFRCO'] = ""
        self.LFXO = 0x00000003
        zz_edict['LFXO'] = self.LFXO
        zz_desc['LFXO'] = ""
        self.HFRCOA = 0x00000004
        zz_edict['HFRCOA'] = self.HFRCOA
        zz_desc['HFRCOA'] = ""
        self.HFRCOX = 0x00000005
        zz_edict['HFRCOX'] = self.HFRCOX
        zz_desc['HFRCOX'] = ""
        self.AUXHFRCOA = 0x00000006
        zz_edict['AUXHFRCOA'] = self.AUXHFRCOA
        zz_desc['AUXHFRCOA'] = ""
        self.AUXHFRCOX = 0x00000007
        zz_edict['AUXHFRCOX'] = self.AUXHFRCOX
        zz_desc['AUXHFRCOX'] = ""
        self.EMUOSC = 0x00000008
        zz_edict['EMUOSC'] = self.EMUOSC
        zz_desc['EMUOSC'] = ""
        self.BIAS = 0x00000009
        zz_edict['BIAS'] = self.BIAS
        zz_desc['BIAS'] = ""
        self.ADC0 = 0x0000000A
        zz_edict['ADC0'] = self.ADC0
        zz_desc['ADC0'] = ""
        self.ACMP0 = 0x0000000B
        zz_edict['ACMP0'] = self.ACMP0
        zz_desc['ACMP0'] = ""
        self.ACMP1 = 0x0000000C
        zz_edict['ACMP1'] = self.ACMP1
        zz_desc['ACMP1'] = ""
        self.PORBOD0 = 0x0000000D
        zz_edict['PORBOD0'] = self.PORBOD0
        zz_desc['PORBOD0'] = ""
        self.PORBOD1 = 0x0000000E
        zz_edict['PORBOD1'] = self.PORBOD1
        zz_desc['PORBOD1'] = ""
        self.IDAC = 0x0000000F
        zz_edict['IDAC'] = self.IDAC
        zz_desc['IDAC'] = ""
        self.GPDCDC0 = 0x00000010
        zz_edict['GPDCDC0'] = self.GPDCDC0
        zz_desc['GPDCDC0'] = ""
        self.GPDCDC1 = 0x00000011
        zz_edict['GPDCDC1'] = self.GPDCDC1
        zz_desc['GPDCDC1'] = ""
        self.HDREG = 0x00000012
        zz_edict['HDREG'] = self.HDREG
        zz_desc['HDREG'] = ""
        self.LDREG = 0x00000013
        zz_edict['LDREG'] = self.LDREG
        zz_desc['LDREG'] = ""
        self.VMON = 0x00000014
        zz_edict['VMON'] = self.VMON
        zz_desc['VMON'] = ""
        self.LVDS = 0x00000015
        zz_edict['LVDS'] = self.LVDS
        zz_desc['LVDS'] = ""
        self.AMUXCP = 0x00000016
        zz_edict['AMUXCP'] = self.AMUXCP
        zz_desc['AMUXCP'] = ""
        self.PWRCFG = 0x00000017
        zz_edict['PWRCFG'] = self.PWRCFG
        zz_desc['PWRCFG'] = ""
        super(RM_Enum_EMU_DIAGABLKTPSEL_GPBLK, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_DIAGABLKTPSEL_RFBLK(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.AUXPLL = 0x00000001
        zz_edict['AUXPLL'] = self.AUXPLL
        zz_desc['AUXPLL'] = ""
        self.IFADC1 = 0x00000002
        zz_edict['IFADC1'] = self.IFADC1
        zz_desc['IFADC1'] = ""
        self.IFADC2 = 0x00000003
        zz_edict['IFADC2'] = self.IFADC2
        zz_desc['IFADC2'] = ""
        self.IFFILT = 0x00000004
        zz_edict['IFFILT'] = self.IFFILT
        zz_desc['IFFILT'] = ""
        self.IFPGA = 0x00000005
        zz_edict['IFPGA'] = self.IFPGA
        zz_desc['IFPGA'] = ""
        self.ISVTR = 0x00000006
        zz_edict['ISVTR'] = self.ISVTR
        zz_desc['ISVTR'] = ""
        self.LNAMIX = 0x00000007
        zz_edict['LNAMIX'] = self.LNAMIX
        zz_desc['LNAMIX'] = ""
        self.RFSENSE = 0x00000008
        zz_edict['RFSENSE'] = self.RFSENSE
        zz_desc['RFSENSE'] = ""
        self.SGLNAMIX = 0x00000009
        zz_edict['SGLNAMIX'] = self.SGLNAMIX
        zz_desc['SGLNAMIX'] = ""
        self.SGPA = 0x0000000A
        zz_edict['SGPA'] = self.SGPA
        zz_desc['SGPA'] = ""
        self.SYCHP = 0x0000000B
        zz_edict['SYCHP'] = self.SYCHP
        zz_desc['SYCHP'] = ""
        self.SYLPF = 0x0000000C
        zz_edict['SYLPF'] = self.SYLPF
        zz_desc['SYLPF'] = ""
        self.SYMMD = 0x0000000D
        zz_edict['SYMMD'] = self.SYMMD
        zz_desc['SYMMD'] = ""
        self.SYVCO = 0x0000000E
        zz_edict['SYVCO'] = self.SYVCO
        zz_desc['SYVCO'] = ""
        self.SYXO = 0x0000000F
        zz_edict['SYXO'] = self.SYXO
        zz_desc['SYXO'] = ""
        self.TXPA = 0x00000010
        zz_edict['TXPA'] = self.TXPA
        zz_desc['TXPA'] = ""
        super(RM_Enum_EMU_DIAGABLKTPSEL_RFBLK, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_DIAGPNBLKSEL_PNRFBLK(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.IFFILT = 0x00000001
        zz_edict['IFFILT'] = self.IFFILT
        zz_desc['IFFILT'] = ""
        self.IFPGA = 0x00000002
        zz_edict['IFPGA'] = self.IFPGA
        zz_desc['IFPGA'] = ""
        self.LNAMIX = 0x00000003
        zz_edict['LNAMIX'] = self.LNAMIX
        zz_desc['LNAMIX'] = ""
        self.SGLNAMIX = 0x00000004
        zz_edict['SGLNAMIX'] = self.SGLNAMIX
        zz_desc['SGLNAMIX'] = ""
        self.SYLPF = 0x00000005
        zz_edict['SYLPF'] = self.SYLPF
        zz_desc['SYLPF'] = ""
        super(RM_Enum_EMU_DIAGPNBLKSEL_PNRFBLK, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_DIAGABRIDGESEL_ABUS_DIAGA_GP_SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GNDA = 0x00000000
        zz_edict['GNDA'] = self.GNDA
        zz_desc['GNDA'] = ""
        self.DIAGAGP = 0x00000001
        zz_edict['DIAGAGP'] = self.DIAGAGP
        zz_desc['DIAGAGP'] = ""
        self.DIAGAGPBUF = 0x00000002
        zz_edict['DIAGAGPBUF'] = self.DIAGAGPBUF
        zz_desc['DIAGAGPBUF'] = ""
        self.DIAGAGP1MOHM = 0x00000003
        zz_edict['DIAGAGP1MOHM'] = self.DIAGAGP1MOHM
        zz_desc['DIAGAGP1MOHM'] = ""
        super(RM_Enum_EMU_DIAGABRIDGESEL_ABUS_DIAGA_GP_SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_DIAGABRIDGESEL_ABUS_DIAGA_RF_SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GNDA = 0x00000000
        zz_edict['GNDA'] = self.GNDA
        zz_desc['GNDA'] = ""
        self.DIAGARF = 0x00000001
        zz_edict['DIAGARF'] = self.DIAGARF
        zz_desc['DIAGARF'] = ""
        self.DIAGARFBUF = 0x00000002
        zz_edict['DIAGARFBUF'] = self.DIAGARFBUF
        zz_desc['DIAGARFBUF'] = ""
        self.DIAGARF1MOHM = 0x00000003
        zz_edict['DIAGARF1MOHM'] = self.DIAGARF1MOHM
        zz_desc['DIAGARF1MOHM'] = ""
        super(RM_Enum_EMU_DIAGABRIDGESEL_ABUS_DIAGA_RF_SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


