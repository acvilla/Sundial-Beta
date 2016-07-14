
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_EMU_CTRL_EM23VSCALE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.VSCALE2 = 0x00000000
        zz_edict['VSCALE2'] = self.VSCALE2
        zz_desc['VSCALE2'] = ""
        self.VSCALE1 = 0x00000001
        zz_edict['VSCALE1'] = self.VSCALE1
        zz_desc['VSCALE1'] = ""
        self.VSCALE0 = 0x00000002
        zz_edict['VSCALE0'] = self.VSCALE0
        zz_desc['VSCALE0'] = ""
        self.RESV = 0x00000003
        zz_edict['RESV'] = self.RESV
        zz_desc['RESV'] = ""
        super(RM_Enum_EMU_CTRL_EM23VSCALE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_CTRL_EM4HVSCALE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.VSCALE2 = 0x00000000
        zz_edict['VSCALE2'] = self.VSCALE2
        zz_desc['VSCALE2'] = ""
        self.VSCALE1 = 0x00000001
        zz_edict['VSCALE1'] = self.VSCALE1
        zz_desc['VSCALE1'] = ""
        self.VSCALE0 = 0x00000002
        zz_edict['VSCALE0'] = self.VSCALE0
        zz_desc['VSCALE0'] = ""
        self.RESV = 0x00000003
        zz_edict['RESV'] = self.RESV
        zz_desc['RESV'] = ""
        super(RM_Enum_EMU_CTRL_EM4HVSCALE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_STATUS_VSCALE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.VSCALE2 = 0x00000000
        zz_edict['VSCALE2'] = self.VSCALE2
        zz_desc['VSCALE2'] = ""
        self.VSCALE1 = 0x00000001
        zz_edict['VSCALE1'] = self.VSCALE1
        zz_desc['VSCALE1'] = ""
        self.VSCALE0 = 0x00000002
        zz_edict['VSCALE0'] = self.VSCALE0
        zz_desc['VSCALE0'] = ""
        self.RESV = 0x00000003
        zz_edict['RESV'] = self.RESV
        zz_desc['RESV'] = ""
        super(RM_Enum_EMU_STATUS_VSCALE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


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


class RM_Enum_EMU_RAM0CTRL_RAMPOWERDOWN(Base_RM_Enum):
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
        self.BLK3TO4 = 0x0000000C
        zz_edict['BLK3TO4'] = self.BLK3TO4
        zz_desc['BLK3TO4'] = ""
        self.BLK2TO4 = 0x0000000E
        zz_edict['BLK2TO4'] = self.BLK2TO4
        zz_desc['BLK2TO4'] = ""
        self.BLK1TO4 = 0x0000000F
        zz_edict['BLK1TO4'] = self.BLK1TO4
        zz_desc['BLK1TO4'] = ""
        super(RM_Enum_EMU_RAM0CTRL_RAMPOWERDOWN, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_RAM0CTRL_SEQRAMPOWERDOWN(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.SEQBLK1 = 0x00000002
        zz_edict['SEQBLK1'] = self.SEQBLK1
        zz_desc['SEQBLK1'] = ""
        self.SEQBLK0TO1 = 0x00000003
        zz_edict['SEQBLK0TO1'] = self.SEQBLK0TO1
        zz_desc['SEQBLK0TO1'] = ""
        super(RM_Enum_EMU_RAM0CTRL_SEQRAMPOWERDOWN, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_EM4CTRL_EM4IORETMODE(Base_RM_Enum):
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
        super(RM_Enum_EMU_EM4CTRL_EM4IORETMODE, self).__init__(
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
        self.UNCONFIGURED = 0x00000000
        zz_edict['UNCONFIGURED'] = self.UNCONFIGURED
        zz_desc['UNCONFIGURED'] = ""
        self.NODCDC = 0x00000001
        zz_edict['NODCDC'] = self.NODCDC
        zz_desc['NODCDC'] = ""
        self.DCDCTODVDD = 0x00000002
        zz_edict['DCDCTODVDD'] = self.DCDCTODVDD
        zz_desc['DCDCTODVDD'] = ""
        self.SOFTWARE = 0x0000000F
        zz_edict['SOFTWARE'] = self.SOFTWARE
        zz_desc['SOFTWARE'] = ""
        super(RM_Enum_EMU_PWRCFG_PWRCFG, self).__init__(
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


class RM_Enum_EMU_DCDCMISCCTRL_LPCMPBIASEM234H(Base_RM_Enum):
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
        super(RM_Enum_EMU_DCDCMISCCTRL_LPCMPBIASEM234H, self).__init__(
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


class RM_Enum_EMU_RAM1CTRL_RAMPOWERDOWN(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.BLK1 = 0x00000002
        zz_edict['BLK1'] = self.BLK1
        zz_desc['BLK1'] = ""
        self.BLK0TO1 = 0x00000003
        zz_edict['BLK0TO1'] = self.BLK0TO1
        zz_desc['BLK0TO1'] = ""
        super(RM_Enum_EMU_RAM1CTRL_RAMPOWERDOWN, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_RAM2CTRL_RAMPOWERDOWN(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.BLK = 0x00000001
        zz_edict['BLK'] = self.BLK
        zz_desc['BLK'] = ""
        super(RM_Enum_EMU_RAM2CTRL_RAMPOWERDOWN, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_DCDCLPEM01CFG_LPCMPBIASEM01(Base_RM_Enum):
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
        super(RM_Enum_EMU_DCDCLPEM01CFG_LPCMPBIASEM01, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_DCDCPRSSEL_DCDCPRSSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PRSCH0 = 0x00000000
        zz_edict['PRSCH0'] = self.PRSCH0
        zz_desc['PRSCH0'] = ""
        self.PRSCH1 = 0x00000001
        zz_edict['PRSCH1'] = self.PRSCH1
        zz_desc['PRSCH1'] = ""
        self.PRSCH2 = 0x00000002
        zz_edict['PRSCH2'] = self.PRSCH2
        zz_desc['PRSCH2'] = ""
        self.PRSCH3 = 0x00000003
        zz_edict['PRSCH3'] = self.PRSCH3
        zz_desc['PRSCH3'] = ""
        self.PRSCH4 = 0x00000004
        zz_edict['PRSCH4'] = self.PRSCH4
        zz_desc['PRSCH4'] = ""
        self.PRSCH5 = 0x00000005
        zz_edict['PRSCH5'] = self.PRSCH5
        zz_desc['PRSCH5'] = ""
        self.PRSCH6 = 0x00000006
        zz_edict['PRSCH6'] = self.PRSCH6
        zz_desc['PRSCH6'] = ""
        self.PRSCH7 = 0x00000007
        zz_edict['PRSCH7'] = self.PRSCH7
        zz_desc['PRSCH7'] = ""
        self.PRSCH8 = 0x00000008
        zz_edict['PRSCH8'] = self.PRSCH8
        zz_desc['PRSCH8'] = ""
        self.PRSCH9 = 0x00000009
        zz_edict['PRSCH9'] = self.PRSCH9
        zz_desc['PRSCH9'] = ""
        self.PRSCH10 = 0x0000000A
        zz_edict['PRSCH10'] = self.PRSCH10
        zz_desc['PRSCH10'] = ""
        self.PRSCH11 = 0x0000000B
        zz_edict['PRSCH11'] = self.PRSCH11
        zz_desc['PRSCH11'] = ""
        super(RM_Enum_EMU_DCDCPRSSEL_DCDCPRSSEL, self).__init__(
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


class RM_Enum_EMU_BIASPERIOD_BIAS_REFRESH_PERIOD_EM03(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '1MS' to 'E1MS'")
        self.E1MS = 0x00000000
        zz_edict['E1MS'] = self.E1MS
        zz_desc['E1MS'] = ""
        #print("WARNING: Aliasing enum '2MS' to 'E2MS'")
        self.E2MS = 0x00000001
        zz_edict['E2MS'] = self.E2MS
        zz_desc['E2MS'] = ""
        #print("WARNING: Aliasing enum '4MS' to 'E4MS'")
        self.E4MS = 0x00000002
        zz_edict['E4MS'] = self.E4MS
        zz_desc['E4MS'] = ""
        #print("WARNING: Aliasing enum '8MS' to 'E8MS'")
        self.E8MS = 0x00000003
        zz_edict['E8MS'] = self.E8MS
        zz_desc['E8MS'] = ""
        super(RM_Enum_EMU_BIASPERIOD_BIAS_REFRESH_PERIOD_EM03, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_BIASPERIOD_BIAS_REFRESH_PERIOD_EM4H(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '1MS' to 'E1MS'")
        self.E1MS = 0x00000000
        zz_edict['E1MS'] = self.E1MS
        zz_desc['E1MS'] = ""
        #print("WARNING: Aliasing enum '2MS' to 'E2MS'")
        self.E2MS = 0x00000001
        zz_edict['E2MS'] = self.E2MS
        zz_desc['E2MS'] = ""
        #print("WARNING: Aliasing enum '4MS' to 'E4MS'")
        self.E4MS = 0x00000002
        zz_edict['E4MS'] = self.E4MS
        zz_desc['E4MS'] = ""
        #print("WARNING: Aliasing enum '8MS' to 'E8MS'")
        self.E8MS = 0x00000003
        zz_edict['E8MS'] = self.E8MS
        zz_desc['E8MS'] = ""
        super(RM_Enum_EMU_BIASPERIOD_BIAS_REFRESH_PERIOD_EM4H, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_BIASPERIOD_BIAS_GMC_CALIB_PERIOD_EM03(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '125MS' to 'E125MS'")
        self.E125MS = 0x00000000
        zz_edict['E125MS'] = self.E125MS
        zz_desc['E125MS'] = ""
        #print("WARNING: Aliasing enum '250MS' to 'E250MS'")
        self.E250MS = 0x00000001
        zz_edict['E250MS'] = self.E250MS
        zz_desc['E250MS'] = ""
        #print("WARNING: Aliasing enum '500MS' to 'E500MS'")
        self.E500MS = 0x00000002
        zz_edict['E500MS'] = self.E500MS
        zz_desc['E500MS'] = ""
        #print("WARNING: Aliasing enum '1S' to 'E1S'")
        self.E1S = 0x00000003
        zz_edict['E1S'] = self.E1S
        zz_desc['E1S'] = ""
        #print("WARNING: Aliasing enum '2S' to 'E2S'")
        self.E2S = 0x00000004
        zz_edict['E2S'] = self.E2S
        zz_desc['E2S'] = ""
        #print("WARNING: Aliasing enum '4S' to 'E4S'")
        self.E4S = 0x00000005
        zz_edict['E4S'] = self.E4S
        zz_desc['E4S'] = ""
        #print("WARNING: Aliasing enum '8S' to 'E8S'")
        self.E8S = 0x00000006
        zz_edict['E8S'] = self.E8S
        zz_desc['E8S'] = ""
        super(RM_Enum_EMU_BIASPERIOD_BIAS_GMC_CALIB_PERIOD_EM03, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_BIASPERIOD_BIAS_GMC_CALIB_PERIOD_EM4H(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '125MS' to 'E125MS'")
        self.E125MS = 0x00000000
        zz_edict['E125MS'] = self.E125MS
        zz_desc['E125MS'] = ""
        #print("WARNING: Aliasing enum '250MS' to 'E250MS'")
        self.E250MS = 0x00000001
        zz_edict['E250MS'] = self.E250MS
        zz_desc['E250MS'] = ""
        #print("WARNING: Aliasing enum '500MS' to 'E500MS'")
        self.E500MS = 0x00000002
        zz_edict['E500MS'] = self.E500MS
        zz_desc['E500MS'] = ""
        #print("WARNING: Aliasing enum '1S' to 'E1S'")
        self.E1S = 0x00000003
        zz_edict['E1S'] = self.E1S
        zz_desc['E1S'] = ""
        #print("WARNING: Aliasing enum '2S' to 'E2S'")
        self.E2S = 0x00000004
        zz_edict['E2S'] = self.E2S
        zz_desc['E2S'] = ""
        #print("WARNING: Aliasing enum '4S' to 'E4S'")
        self.E4S = 0x00000005
        zz_edict['E4S'] = self.E4S
        zz_desc['E4S'] = ""
        #print("WARNING: Aliasing enum '8S' to 'E8S'")
        self.E8S = 0x00000006
        zz_edict['E8S'] = self.E8S
        zz_desc['E8S'] = ""
        super(RM_Enum_EMU_BIASPERIOD_BIAS_GMC_CALIB_PERIOD_EM4H, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_DREGCALIB_LDREG_DUTYSCALE(Base_RM_Enum):
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
        super(RM_Enum_EMU_DREGCALIB_LDREG_DUTYSCALE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_RAM0FEATURE_SEQRAMEN(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.SEQRAM0 = 0x00000001
        zz_edict['SEQRAM0'] = self.SEQRAM0
        zz_desc['SEQRAM0'] = ""
        self.SEQRAM0TO1 = 0x00000003
        zz_edict['SEQRAM0TO1'] = self.SEQRAM0TO1
        zz_desc['SEQRAM0TO1'] = ""
        super(RM_Enum_EMU_RAM0FEATURE_SEQRAMEN, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_RAM0FEATURE_RAM0DIV(Base_RM_Enum):
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
        super(RM_Enum_EMU_RAM0FEATURE_RAM0DIV, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_RAM0FEATURE_RAMSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.RAM0 = 0x00000001
        zz_edict['RAM0'] = self.RAM0
        zz_desc['RAM0'] = ""
        self.RAM0TO1 = 0x00000003
        zz_edict['RAM0TO1'] = self.RAM0TO1
        zz_desc['RAM0TO1'] = ""
        self.RAM0TO2 = 0x00000007
        zz_edict['RAM0TO2'] = self.RAM0TO2
        zz_desc['RAM0TO2'] = ""
        self.RAM0TO3 = 0x0000000F
        zz_edict['RAM0TO3'] = self.RAM0TO3
        zz_desc['RAM0TO3'] = ""
        self.RAM0TO4 = 0x0000001F
        zz_edict['RAM0TO4'] = self.RAM0TO4
        zz_desc['RAM0TO4'] = ""
        super(RM_Enum_EMU_RAM0FEATURE_RAMSIZE, self).__init__(
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
        self.HDREGVREG = 0x00000019
        zz_edict['HDREGVREG'] = self.HDREGVREG
        zz_desc['HDREGVREG'] = ""
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
        self.PD01DIS = 0x0000001E
        zz_edict['PD01DIS'] = self.PD01DIS
        zz_desc['PD01DIS'] = ""
        self.PD02DIS = 0x0000001F
        zz_edict['PD02DIS'] = self.PD02DIS
        zz_desc['PD02DIS'] = ""
        self.DECBODRSTPTR = 0x00000020
        zz_edict['DECBODRSTPTR'] = self.DECBODRSTPTR
        zz_desc['DECBODRSTPTR'] = ""
        self.EMUOSC = 0x00000021
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
        self.HDREGVREG = 0x00000019
        zz_edict['HDREGVREG'] = self.HDREGVREG
        zz_desc['HDREGVREG'] = ""
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
        self.PD01DIS = 0x0000001E
        zz_edict['PD01DIS'] = self.PD01DIS
        zz_desc['PD01DIS'] = ""
        self.PD02DIS = 0x0000001F
        zz_edict['PD02DIS'] = self.PD02DIS
        zz_desc['PD02DIS'] = ""
        self.DECBODRSTPTR = 0x00000020
        zz_edict['DECBODRSTPTR'] = self.DECBODRSTPTR
        zz_desc['DECBODRSTPTR'] = ""
        self.EMUOSC = 0x00000021
        zz_edict['EMUOSC'] = self.EMUOSC
        zz_desc['EMUOSC'] = ""
        super(RM_Enum_EMU_TESTCTRL_CMCTRLPRSSEL1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_RAM1FEATURE_RAMSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.RAM0 = 0x00000001
        zz_edict['RAM0'] = self.RAM0
        zz_desc['RAM0'] = ""
        self.RAM0TO1 = 0x00000003
        zz_edict['RAM0TO1'] = self.RAM0TO1
        zz_desc['RAM0TO1'] = ""
        super(RM_Enum_EMU_RAM1FEATURE_RAMSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_RAM2FEATURE_RAMSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.RAM0 = 0x00000001
        zz_edict['RAM0'] = self.RAM0
        zz_desc['RAM0'] = ""
        super(RM_Enum_EMU_RAM2FEATURE_RAMSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_RAMBIASCONF_RAMBIASCTRL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.VSB100 = 0x00000001
        zz_edict['VSB100'] = self.VSB100
        zz_desc['VSB100'] = ""
        self.VSB200 = 0x00000002
        zz_edict['VSB200'] = self.VSB200
        zz_desc['VSB200'] = ""
        self.VSB300 = 0x00000004
        zz_edict['VSB300'] = self.VSB300
        zz_desc['VSB300'] = ""
        self.VSB400 = 0x00000008
        zz_edict['VSB400'] = self.VSB400
        zz_desc['VSB400'] = ""
        super(RM_Enum_EMU_RAMBIASCONF_RAMBIASCTRL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_TGTHFRCOCTRL_CLKDIV(Base_RM_Enum):
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
        super(RM_Enum_EMU_TGTHFRCOCTRL_CLKDIV, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_BCLFRCOCTRL_TIMEOUT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '2CYCLES' to 'E2CYCLES'")
        self.E2CYCLES = 0x00000000
        zz_edict['E2CYCLES'] = self.E2CYCLES
        zz_desc['E2CYCLES'] = ""
        #print("WARNING: Aliasing enum '16CYCLES' to 'E16CYCLES'")
        self.E16CYCLES = 0x00000001
        zz_edict['E16CYCLES'] = self.E16CYCLES
        zz_desc['E16CYCLES'] = ""
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000002
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        super(RM_Enum_EMU_BCLFRCOCTRL_TIMEOUT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_TESTBCLFRCOCTRL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '32KHZDUTY50' to 'E32KHZDUTY50'")
        self.E32KHZDUTY50 = 0x00000000
        zz_edict['E32KHZDUTY50'] = self.E32KHZDUTY50
        zz_desc['E32KHZDUTY50'] = ""
        #print("WARNING: Aliasing enum '64KHZDUTY5' to 'E64KHZDUTY5'")
        self.E64KHZDUTY5 = 0x00000001
        zz_edict['E64KHZDUTY5'] = self.E64KHZDUTY5
        zz_desc['E64KHZDUTY5'] = ""
        #print("WARNING: Aliasing enum '16KHZDUTY50' to 'E16KHZDUTY50'")
        self.E16KHZDUTY50 = 0x00000002
        zz_edict['E16KHZDUTY50'] = self.E16KHZDUTY50
        zz_desc['E16KHZDUTY50'] = ""
        #print("WARNING: Aliasing enum '32KHZDUTY5' to 'E32KHZDUTY5'")
        self.E32KHZDUTY5 = 0x00000003
        zz_edict['E32KHZDUTY5'] = self.E32KHZDUTY5
        zz_desc['E32KHZDUTY5'] = ""
        super(RM_Enum_EMU_TESTBCLFRCOCTRL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_TESTBCLFRCOCTRL_SELCLKDIV(Base_RM_Enum):
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
        super(RM_Enum_EMU_TESTBCLFRCOCTRL_SELCLKDIV, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_TESTBCLFRCOCTRL_VREFUPDATE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000000
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        #print("WARNING: Aliasing enum '64CYCLES' to 'E64CYCLES'")
        self.E64CYCLES = 0x00000001
        zz_edict['E64CYCLES'] = self.E64CYCLES
        zz_desc['E64CYCLES'] = ""
        #print("WARNING: Aliasing enum '128CYCLES' to 'E128CYCLES'")
        self.E128CYCLES = 0x00000002
        zz_edict['E128CYCLES'] = self.E128CYCLES
        zz_desc['E128CYCLES'] = ""
        #print("WARNING: Aliasing enum '256CYCLES' to 'E256CYCLES'")
        self.E256CYCLES = 0x00000003
        zz_edict['E256CYCLES'] = self.E256CYCLES
        zz_desc['E256CYCLES'] = ""
        super(RM_Enum_EMU_TESTBCLFRCOCTRL_VREFUPDATE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_TESTBCLFRCOCTRL_VREFPRECH(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '2CYCLES' to 'E2CYCLES'")
        self.E2CYCLES = 0x00000000
        zz_edict['E2CYCLES'] = self.E2CYCLES
        zz_desc['E2CYCLES'] = ""
        #print("WARNING: Aliasing enum '4CYCLES' to 'E4CYCLES'")
        self.E4CYCLES = 0x00000001
        zz_edict['E4CYCLES'] = self.E4CYCLES
        zz_desc['E4CYCLES'] = ""
        #print("WARNING: Aliasing enum '8CYCLES' to 'E8CYCLES'")
        self.E8CYCLES = 0x00000002
        zz_edict['E8CYCLES'] = self.E8CYCLES
        zz_desc['E8CYCLES'] = ""
        #print("WARNING: Aliasing enum '16CYCLES' to 'E16CYCLES'")
        self.E16CYCLES = 0x00000003
        zz_edict['E16CYCLES'] = self.E16CYCLES
        zz_desc['E16CYCLES'] = ""
        super(RM_Enum_EMU_TESTBCLFRCOCTRL_VREFPRECH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_FLASHVREFCALIB_FLASHVREF_DUTYSCALE(Base_RM_Enum):
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
        super(RM_Enum_EMU_FLASHVREFCALIB_FLASHVREF_DUTYSCALE, self).__init__(
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
        self.VREF = 0x0000001F
        zz_edict['VREF'] = self.VREF
        zz_desc['VREF'] = ""
        self.OPA0 = 0x00000023
        zz_edict['OPA0'] = self.OPA0
        zz_desc['OPA0'] = ""
        self.OPA1 = 0x00000024
        zz_edict['OPA1'] = self.OPA1
        zz_desc['OPA1'] = ""
        self.OPA2 = 0x00000025
        zz_edict['OPA2'] = self.OPA2
        zz_desc['OPA2'] = ""
        self.DAC0 = 0x00000027
        zz_edict['DAC0'] = self.DAC0
        zz_desc['DAC0'] = ""
        self.BCLFRCO = 0x00000028
        zz_edict['BCLFRCO'] = self.BCLFRCO
        zz_desc['BCLFRCO'] = ""
        self.RETREG = 0x00000029
        zz_edict['RETREG'] = self.RETREG
        zz_desc['RETREG'] = ""
        self.CSEN = 0x0000002A
        zz_edict['CSEN'] = self.CSEN
        zz_desc['CSEN'] = ""
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


class RM_Enum_EMU_EM2PERCTRL_EM2PERPWDN(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.BLK2 = 0x00000002
        zz_edict['BLK2'] = self.BLK2
        zz_desc['BLK2'] = ""
        self.BLK1TO2 = 0x00000003
        zz_edict['BLK1TO2'] = self.BLK1TO2
        zz_desc['BLK1TO2'] = ""
        super(RM_Enum_EMU_EM2PERCTRL_EM2PERPWDN, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_EMU_EM2PERCTRL_EM2PERPWUP(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.BLK2 = 0x00000002
        zz_edict['BLK2'] = self.BLK2
        zz_desc['BLK2'] = ""
        self.BLK1TO2 = 0x00000003
        zz_edict['BLK1TO2'] = self.BLK1TO2
        zz_desc['BLK1TO2'] = ""
        super(RM_Enum_EMU_EM2PERCTRL_EM2PERPWUP, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


