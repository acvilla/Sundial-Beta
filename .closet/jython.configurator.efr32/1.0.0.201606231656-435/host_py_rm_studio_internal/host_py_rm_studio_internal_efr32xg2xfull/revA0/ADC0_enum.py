
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_ADC0_CTRL_WARMUPMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NORMAL = 0x00000000
        zz_edict['NORMAL'] = self.NORMAL
        zz_desc['NORMAL'] = ""
        self.KEEPINSTANDBY = 0x00000001
        zz_edict['KEEPINSTANDBY'] = self.KEEPINSTANDBY
        zz_desc['KEEPINSTANDBY'] = ""
        self.KEEPINSLOWACC = 0x00000002
        zz_edict['KEEPINSLOWACC'] = self.KEEPINSLOWACC
        zz_desc['KEEPINSLOWACC'] = ""
        self.KEEPADCWARM = 0x00000003
        zz_edict['KEEPADCWARM'] = self.KEEPADCWARM
        zz_desc['KEEPADCWARM'] = ""
        super(RM_Enum_ADC0_CTRL_WARMUPMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_CTRL_PRESC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NODIVISION = 0x00000000
        zz_edict['NODIVISION'] = self.NODIVISION
        zz_desc['NODIVISION'] = ""
        super(RM_Enum_ADC0_CTRL_PRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_CTRL_OVSRSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.X2 = 0x00000000
        zz_edict['X2'] = self.X2
        zz_desc['X2'] = ""
        self.X4 = 0x00000001
        zz_edict['X4'] = self.X4
        zz_desc['X4'] = ""
        self.X8 = 0x00000002
        zz_edict['X8'] = self.X8
        zz_desc['X8'] = ""
        self.X16 = 0x00000003
        zz_edict['X16'] = self.X16
        zz_desc['X16'] = ""
        self.X32 = 0x00000004
        zz_edict['X32'] = self.X32
        zz_desc['X32'] = ""
        self.X64 = 0x00000005
        zz_edict['X64'] = self.X64
        zz_desc['X64'] = ""
        self.X128 = 0x00000006
        zz_edict['X128'] = self.X128
        zz_desc['X128'] = ""
        self.X256 = 0x00000007
        zz_edict['X256'] = self.X256
        zz_desc['X256'] = ""
        self.X512 = 0x00000008
        zz_edict['X512'] = self.X512
        zz_desc['X512'] = ""
        self.X1024 = 0x00000009
        zz_edict['X1024'] = self.X1024
        zz_desc['X1024'] = ""
        self.X2048 = 0x0000000A
        zz_edict['X2048'] = self.X2048
        zz_desc['X2048'] = ""
        self.X4096 = 0x0000000B
        zz_edict['X4096'] = self.X4096
        zz_desc['X4096'] = ""
        super(RM_Enum_ADC0_CTRL_OVSRSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_CTRL_CHCONREFWARMIDLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PREFSCAN = 0x00000000
        zz_edict['PREFSCAN'] = self.PREFSCAN
        zz_desc['PREFSCAN'] = ""
        self.PREFSINGLE = 0x00000001
        zz_edict['PREFSINGLE'] = self.PREFSINGLE
        zz_desc['PREFSINGLE'] = ""
        self.KEEPPREV = 0x00000002
        zz_edict['KEEPPREV'] = self.KEEPPREV
        zz_desc['KEEPPREV'] = ""
        super(RM_Enum_ADC0_CTRL_CHCONREFWARMIDLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_STATUS_PROGERR(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BUSCONF = 0x00000001
        zz_edict['BUSCONF'] = self.BUSCONF
        zz_desc['BUSCONF'] = ""
        self.NEGSELCONF = 0x00000002
        zz_edict['NEGSELCONF'] = self.NEGSELCONF
        zz_desc['NEGSELCONF'] = ""
        super(RM_Enum_ADC0_STATUS_PROGERR, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SINGLECTRL_RES(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '12BIT' to 'E12BIT'")
        self.E12BIT = 0x00000000
        zz_edict['E12BIT'] = self.E12BIT
        zz_desc['E12BIT'] = ""
        #print("WARNING: Aliasing enum '8BIT' to 'E8BIT'")
        self.E8BIT = 0x00000001
        zz_edict['E8BIT'] = self.E8BIT
        zz_desc['E8BIT'] = ""
        #print("WARNING: Aliasing enum '6BIT' to 'E6BIT'")
        self.E6BIT = 0x00000002
        zz_edict['E6BIT'] = self.E6BIT
        zz_desc['E6BIT'] = ""
        self.OVS = 0x00000003
        zz_edict['OVS'] = self.OVS
        zz_desc['OVS'] = ""
        super(RM_Enum_ADC0_SINGLECTRL_RES, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SINGLECTRL_REF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '1V25' to 'E1V25'")
        self.E1V25 = 0x00000000
        zz_edict['E1V25'] = self.E1V25
        zz_desc['E1V25'] = ""
        #print("WARNING: Aliasing enum '2V5' to 'E2V5'")
        self.E2V5 = 0x00000001
        zz_edict['E2V5'] = self.E2V5
        zz_desc['E2V5'] = ""
        self.VDD = 0x00000002
        zz_edict['VDD'] = self.VDD
        zz_desc['VDD'] = ""
        #print("WARNING: Aliasing enum '5V' to 'E5V'")
        self.E5V = 0x00000003
        zz_edict['E5V'] = self.E5V
        zz_desc['E5V'] = ""
        self.EXTSINGLE = 0x00000004
        zz_edict['EXTSINGLE'] = self.EXTSINGLE
        zz_desc['EXTSINGLE'] = ""
        #print("WARNING: Aliasing enum '2XEXTDIFF' to 'E2XEXTDIFF'")
        self.E2XEXTDIFF = 0x00000005
        zz_edict['E2XEXTDIFF'] = self.E2XEXTDIFF
        zz_desc['E2XEXTDIFF'] = ""
        #print("WARNING: Aliasing enum '2XVDD' to 'E2XVDD'")
        self.E2XVDD = 0x00000006
        zz_edict['E2XVDD'] = self.E2XVDD
        zz_desc['E2XVDD'] = ""
        self.CONF = 0x00000007
        zz_edict['CONF'] = self.CONF
        zz_desc['CONF'] = ""
        super(RM_Enum_ADC0_SINGLECTRL_REF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SINGLECTRL_AT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '1CYCLE' to 'E1CYCLE'")
        self.E1CYCLE = 0x00000000
        zz_edict['E1CYCLE'] = self.E1CYCLE
        zz_desc['E1CYCLE'] = ""
        #print("WARNING: Aliasing enum '2CYCLES' to 'E2CYCLES'")
        self.E2CYCLES = 0x00000001
        zz_edict['E2CYCLES'] = self.E2CYCLES
        zz_desc['E2CYCLES'] = ""
        #print("WARNING: Aliasing enum '3CYCLES' to 'E3CYCLES'")
        self.E3CYCLES = 0x00000002
        zz_edict['E3CYCLES'] = self.E3CYCLES
        zz_desc['E3CYCLES'] = ""
        #print("WARNING: Aliasing enum '4CYCLES' to 'E4CYCLES'")
        self.E4CYCLES = 0x00000003
        zz_edict['E4CYCLES'] = self.E4CYCLES
        zz_desc['E4CYCLES'] = ""
        #print("WARNING: Aliasing enum '8CYCLES' to 'E8CYCLES'")
        self.E8CYCLES = 0x00000004
        zz_edict['E8CYCLES'] = self.E8CYCLES
        zz_desc['E8CYCLES'] = ""
        #print("WARNING: Aliasing enum '16CYCLES' to 'E16CYCLES'")
        self.E16CYCLES = 0x00000005
        zz_edict['E16CYCLES'] = self.E16CYCLES
        zz_desc['E16CYCLES'] = ""
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000006
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        #print("WARNING: Aliasing enum '64CYCLES' to 'E64CYCLES'")
        self.E64CYCLES = 0x00000007
        zz_edict['E64CYCLES'] = self.E64CYCLES
        zz_desc['E64CYCLES'] = ""
        #print("WARNING: Aliasing enum '128CYCLES' to 'E128CYCLES'")
        self.E128CYCLES = 0x00000008
        zz_edict['E128CYCLES'] = self.E128CYCLES
        zz_desc['E128CYCLES'] = ""
        #print("WARNING: Aliasing enum '256CYCLES' to 'E256CYCLES'")
        self.E256CYCLES = 0x00000009
        zz_edict['E256CYCLES'] = self.E256CYCLES
        zz_desc['E256CYCLES'] = ""
        super(RM_Enum_ADC0_SINGLECTRL_AT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SINGLECTRLX_VREFSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.VBGR = 0x00000000
        zz_edict['VBGR'] = self.VBGR
        zz_desc['VBGR'] = ""
        self.VDDXWATT = 0x00000001
        zz_edict['VDDXWATT'] = self.VDDXWATT
        zz_desc['VDDXWATT'] = ""
        self.VREFPWATT = 0x00000002
        zz_edict['VREFPWATT'] = self.VREFPWATT
        zz_desc['VREFPWATT'] = ""
        self.VREFP = 0x00000003
        zz_edict['VREFP'] = self.VREFP
        zz_desc['VREFP'] = ""
        self.VENTROPY = 0x00000004
        zz_edict['VENTROPY'] = self.VENTROPY
        zz_desc['VENTROPY'] = ""
        self.VREFPNWATT = 0x00000005
        zz_edict['VREFPNWATT'] = self.VREFPNWATT
        zz_desc['VREFPNWATT'] = ""
        self.VREFPN = 0x00000006
        zz_edict['VREFPN'] = self.VREFPN
        zz_desc['VREFPN'] = ""
        self.VBGRLOW = 0x00000007
        zz_edict['VBGRLOW'] = self.VBGRLOW
        zz_desc['VBGRLOW'] = ""
        super(RM_Enum_ADC0_SINGLECTRLX_VREFSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SINGLECTRLX_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_ADC0_SINGLECTRLX_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SINGLECTRLX_REPDELAY(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NODELAY = 0x00000000
        zz_edict['NODELAY'] = self.NODELAY
        zz_desc['NODELAY'] = ""
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
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000004
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        #print("WARNING: Aliasing enum '64CYCLES' to 'E64CYCLES'")
        self.E64CYCLES = 0x00000005
        zz_edict['E64CYCLES'] = self.E64CYCLES
        zz_desc['E64CYCLES'] = ""
        #print("WARNING: Aliasing enum '128CYCLES' to 'E128CYCLES'")
        self.E128CYCLES = 0x00000006
        zz_edict['E128CYCLES'] = self.E128CYCLES
        zz_desc['E128CYCLES'] = ""
        #print("WARNING: Aliasing enum '256CYCLES' to 'E256CYCLES'")
        self.E256CYCLES = 0x00000007
        zz_edict['E256CYCLES'] = self.E256CYCLES
        zz_desc['E256CYCLES'] = ""
        super(RM_Enum_ADC0_SINGLECTRLX_REPDELAY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANCTRL_RES(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '12BIT' to 'E12BIT'")
        self.E12BIT = 0x00000000
        zz_edict['E12BIT'] = self.E12BIT
        zz_desc['E12BIT'] = ""
        #print("WARNING: Aliasing enum '8BIT' to 'E8BIT'")
        self.E8BIT = 0x00000001
        zz_edict['E8BIT'] = self.E8BIT
        zz_desc['E8BIT'] = ""
        #print("WARNING: Aliasing enum '6BIT' to 'E6BIT'")
        self.E6BIT = 0x00000002
        zz_edict['E6BIT'] = self.E6BIT
        zz_desc['E6BIT'] = ""
        self.OVS = 0x00000003
        zz_edict['OVS'] = self.OVS
        zz_desc['OVS'] = ""
        super(RM_Enum_ADC0_SCANCTRL_RES, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANCTRL_REF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '1V25' to 'E1V25'")
        self.E1V25 = 0x00000000
        zz_edict['E1V25'] = self.E1V25
        zz_desc['E1V25'] = ""
        #print("WARNING: Aliasing enum '2V5' to 'E2V5'")
        self.E2V5 = 0x00000001
        zz_edict['E2V5'] = self.E2V5
        zz_desc['E2V5'] = ""
        self.VDD = 0x00000002
        zz_edict['VDD'] = self.VDD
        zz_desc['VDD'] = ""
        #print("WARNING: Aliasing enum '5V' to 'E5V'")
        self.E5V = 0x00000003
        zz_edict['E5V'] = self.E5V
        zz_desc['E5V'] = ""
        self.EXTSINGLE = 0x00000004
        zz_edict['EXTSINGLE'] = self.EXTSINGLE
        zz_desc['EXTSINGLE'] = ""
        #print("WARNING: Aliasing enum '2XEXTDIFF' to 'E2XEXTDIFF'")
        self.E2XEXTDIFF = 0x00000005
        zz_edict['E2XEXTDIFF'] = self.E2XEXTDIFF
        zz_desc['E2XEXTDIFF'] = ""
        #print("WARNING: Aliasing enum '2XVDD' to 'E2XVDD'")
        self.E2XVDD = 0x00000006
        zz_edict['E2XVDD'] = self.E2XVDD
        zz_desc['E2XVDD'] = ""
        self.CONF = 0x00000007
        zz_edict['CONF'] = self.CONF
        zz_desc['CONF'] = ""
        super(RM_Enum_ADC0_SCANCTRL_REF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANCTRL_AT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '1CYCLE' to 'E1CYCLE'")
        self.E1CYCLE = 0x00000000
        zz_edict['E1CYCLE'] = self.E1CYCLE
        zz_desc['E1CYCLE'] = ""
        #print("WARNING: Aliasing enum '2CYCLES' to 'E2CYCLES'")
        self.E2CYCLES = 0x00000001
        zz_edict['E2CYCLES'] = self.E2CYCLES
        zz_desc['E2CYCLES'] = ""
        #print("WARNING: Aliasing enum '3CYCLES' to 'E3CYCLES'")
        self.E3CYCLES = 0x00000002
        zz_edict['E3CYCLES'] = self.E3CYCLES
        zz_desc['E3CYCLES'] = ""
        #print("WARNING: Aliasing enum '4CYCLES' to 'E4CYCLES'")
        self.E4CYCLES = 0x00000003
        zz_edict['E4CYCLES'] = self.E4CYCLES
        zz_desc['E4CYCLES'] = ""
        #print("WARNING: Aliasing enum '8CYCLES' to 'E8CYCLES'")
        self.E8CYCLES = 0x00000004
        zz_edict['E8CYCLES'] = self.E8CYCLES
        zz_desc['E8CYCLES'] = ""
        #print("WARNING: Aliasing enum '16CYCLES' to 'E16CYCLES'")
        self.E16CYCLES = 0x00000005
        zz_edict['E16CYCLES'] = self.E16CYCLES
        zz_desc['E16CYCLES'] = ""
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000006
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        #print("WARNING: Aliasing enum '64CYCLES' to 'E64CYCLES'")
        self.E64CYCLES = 0x00000007
        zz_edict['E64CYCLES'] = self.E64CYCLES
        zz_desc['E64CYCLES'] = ""
        #print("WARNING: Aliasing enum '128CYCLES' to 'E128CYCLES'")
        self.E128CYCLES = 0x00000008
        zz_edict['E128CYCLES'] = self.E128CYCLES
        zz_desc['E128CYCLES'] = ""
        #print("WARNING: Aliasing enum '256CYCLES' to 'E256CYCLES'")
        self.E256CYCLES = 0x00000009
        zz_edict['E256CYCLES'] = self.E256CYCLES
        zz_desc['E256CYCLES'] = ""
        super(RM_Enum_ADC0_SCANCTRL_AT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANCTRLX_VREFSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.VBGR = 0x00000000
        zz_edict['VBGR'] = self.VBGR
        zz_desc['VBGR'] = ""
        self.VDDXWATT = 0x00000001
        zz_edict['VDDXWATT'] = self.VDDXWATT
        zz_desc['VDDXWATT'] = ""
        self.VREFPWATT = 0x00000002
        zz_edict['VREFPWATT'] = self.VREFPWATT
        zz_desc['VREFPWATT'] = ""
        self.VREFP = 0x00000003
        zz_edict['VREFP'] = self.VREFP
        zz_desc['VREFP'] = ""
        self.VREFPNWATT = 0x00000005
        zz_edict['VREFPNWATT'] = self.VREFPNWATT
        zz_desc['VREFPNWATT'] = ""
        self.VREFPN = 0x00000006
        zz_edict['VREFPN'] = self.VREFPN
        zz_desc['VREFPN'] = ""
        self.VBGRLOW = 0x00000007
        zz_edict['VBGRLOW'] = self.VBGRLOW
        zz_desc['VBGRLOW'] = ""
        super(RM_Enum_ADC0_SCANCTRLX_VREFSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANCTRLX_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_ADC0_SCANCTRLX_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANCTRLX_REPDELAY(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NODELAY = 0x00000000
        zz_edict['NODELAY'] = self.NODELAY
        zz_desc['NODELAY'] = ""
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
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000004
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        #print("WARNING: Aliasing enum '64CYCLES' to 'E64CYCLES'")
        self.E64CYCLES = 0x00000005
        zz_edict['E64CYCLES'] = self.E64CYCLES
        zz_desc['E64CYCLES'] = ""
        #print("WARNING: Aliasing enum '128CYCLES' to 'E128CYCLES'")
        self.E128CYCLES = 0x00000006
        zz_edict['E128CYCLES'] = self.E128CYCLES
        zz_desc['E128CYCLES'] = ""
        #print("WARNING: Aliasing enum '256CYCLES' to 'E256CYCLES'")
        self.E256CYCLES = 0x00000007
        zz_edict['E256CYCLES'] = self.E256CYCLES
        zz_desc['E256CYCLES'] = ""
        super(RM_Enum_ADC0_SCANCTRLX_REPDELAY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANMASK_SCANINPUTEN(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.INPUT0INPUT0NEGSEL = 0x00000001
        zz_edict['INPUT0INPUT0NEGSEL'] = self.INPUT0INPUT0NEGSEL
        zz_desc['INPUT0INPUT0NEGSEL'] = ""
        self.INPUT0 = 0x00000001
        zz_edict['INPUT0'] = self.INPUT0
        zz_desc['INPUT0'] = ""
        self.INPUT1 = 0x00000002
        zz_edict['INPUT1'] = self.INPUT1
        zz_desc['INPUT1'] = ""
        self.INPUT1INPUT2 = 0x00000002
        zz_edict['INPUT1INPUT2'] = self.INPUT1INPUT2
        zz_desc['INPUT1INPUT2'] = ""
        self.INPUT2 = 0x00000004
        zz_edict['INPUT2'] = self.INPUT2
        zz_desc['INPUT2'] = ""
        self.INPUT2INPUT2NEGSEL = 0x00000004
        zz_edict['INPUT2INPUT2NEGSEL'] = self.INPUT2INPUT2NEGSEL
        zz_desc['INPUT2INPUT2NEGSEL'] = ""
        self.INPUT3 = 0x00000008
        zz_edict['INPUT3'] = self.INPUT3
        zz_desc['INPUT3'] = ""
        self.INPUT3INPUT4 = 0x00000008
        zz_edict['INPUT3INPUT4'] = self.INPUT3INPUT4
        zz_desc['INPUT3INPUT4'] = ""
        self.INPUT4 = 0x00000010
        zz_edict['INPUT4'] = self.INPUT4
        zz_desc['INPUT4'] = ""
        self.INPUT4INPUT4NEGSEL = 0x00000010
        zz_edict['INPUT4INPUT4NEGSEL'] = self.INPUT4INPUT4NEGSEL
        zz_desc['INPUT4INPUT4NEGSEL'] = ""
        self.INPUT5INPUT6 = 0x00000020
        zz_edict['INPUT5INPUT6'] = self.INPUT5INPUT6
        zz_desc['INPUT5INPUT6'] = ""
        self.INPUT5 = 0x00000020
        zz_edict['INPUT5'] = self.INPUT5
        zz_desc['INPUT5'] = ""
        self.INPUT6INPUT6NEGSEL = 0x00000040
        zz_edict['INPUT6INPUT6NEGSEL'] = self.INPUT6INPUT6NEGSEL
        zz_desc['INPUT6INPUT6NEGSEL'] = ""
        self.INPUT6 = 0x00000040
        zz_edict['INPUT6'] = self.INPUT6
        zz_desc['INPUT6'] = ""
        self.INPUT7 = 0x00000080
        zz_edict['INPUT7'] = self.INPUT7
        zz_desc['INPUT7'] = ""
        self.INPUT7INPUT0 = 0x00000080
        zz_edict['INPUT7INPUT0'] = self.INPUT7INPUT0
        zz_desc['INPUT7INPUT0'] = ""
        self.INPUT8INPUT9 = 0x00000100
        zz_edict['INPUT8INPUT9'] = self.INPUT8INPUT9
        zz_desc['INPUT8INPUT9'] = ""
        self.INPUT8 = 0x00000100
        zz_edict['INPUT8'] = self.INPUT8
        zz_desc['INPUT8'] = ""
        self.INPUT9 = 0x00000200
        zz_edict['INPUT9'] = self.INPUT9
        zz_desc['INPUT9'] = ""
        self.INPUT9INPUT9NEGSEL = 0x00000200
        zz_edict['INPUT9INPUT9NEGSEL'] = self.INPUT9INPUT9NEGSEL
        zz_desc['INPUT9INPUT9NEGSEL'] = ""
        self.INPUT10INPUT11 = 0x00000400
        zz_edict['INPUT10INPUT11'] = self.INPUT10INPUT11
        zz_desc['INPUT10INPUT11'] = ""
        self.INPUT10 = 0x00000400
        zz_edict['INPUT10'] = self.INPUT10
        zz_desc['INPUT10'] = ""
        self.INPUT11INPUT11NEGSEL = 0x00000800
        zz_edict['INPUT11INPUT11NEGSEL'] = self.INPUT11INPUT11NEGSEL
        zz_desc['INPUT11INPUT11NEGSEL'] = ""
        self.INPUT11 = 0x00000800
        zz_edict['INPUT11'] = self.INPUT11
        zz_desc['INPUT11'] = ""
        self.INPUT12INPUT13 = 0x00001000
        zz_edict['INPUT12INPUT13'] = self.INPUT12INPUT13
        zz_desc['INPUT12INPUT13'] = ""
        self.INPUT12 = 0x00001000
        zz_edict['INPUT12'] = self.INPUT12
        zz_desc['INPUT12'] = ""
        self.INPUT13INPUT13NEGSEL = 0x00002000
        zz_edict['INPUT13INPUT13NEGSEL'] = self.INPUT13INPUT13NEGSEL
        zz_desc['INPUT13INPUT13NEGSEL'] = ""
        self.INPUT13 = 0x00002000
        zz_edict['INPUT13'] = self.INPUT13
        zz_desc['INPUT13'] = ""
        self.INPUT14INPUT15 = 0x00004000
        zz_edict['INPUT14INPUT15'] = self.INPUT14INPUT15
        zz_desc['INPUT14INPUT15'] = ""
        self.INPUT14 = 0x00004000
        zz_edict['INPUT14'] = self.INPUT14
        zz_desc['INPUT14'] = ""
        self.INPUT15INPUT15NEGSEL = 0x00008000
        zz_edict['INPUT15INPUT15NEGSEL'] = self.INPUT15INPUT15NEGSEL
        zz_desc['INPUT15INPUT15NEGSEL'] = ""
        self.INPUT15 = 0x00008000
        zz_edict['INPUT15'] = self.INPUT15
        zz_desc['INPUT15'] = ""
        self.INPUT16INPUT17 = 0x00010000
        zz_edict['INPUT16INPUT17'] = self.INPUT16INPUT17
        zz_desc['INPUT16INPUT17'] = ""
        self.INPUT16 = 0x00010000
        zz_edict['INPUT16'] = self.INPUT16
        zz_desc['INPUT16'] = ""
        self.INPUT17INPUT18 = 0x00020000
        zz_edict['INPUT17INPUT18'] = self.INPUT17INPUT18
        zz_desc['INPUT17INPUT18'] = ""
        self.INPUT17 = 0x00020000
        zz_edict['INPUT17'] = self.INPUT17
        zz_desc['INPUT17'] = ""
        self.INPUT18INPUT19 = 0x00040000
        zz_edict['INPUT18INPUT19'] = self.INPUT18INPUT19
        zz_desc['INPUT18INPUT19'] = ""
        self.INPUT18 = 0x00040000
        zz_edict['INPUT18'] = self.INPUT18
        zz_desc['INPUT18'] = ""
        self.INPUT19 = 0x00080000
        zz_edict['INPUT19'] = self.INPUT19
        zz_desc['INPUT19'] = ""
        self.INPUT19INPUT20 = 0x00080000
        zz_edict['INPUT19INPUT20'] = self.INPUT19INPUT20
        zz_desc['INPUT19INPUT20'] = ""
        self.INPUT20INPUT21 = 0x00100000
        zz_edict['INPUT20INPUT21'] = self.INPUT20INPUT21
        zz_desc['INPUT20INPUT21'] = ""
        self.INPUT20 = 0x00100000
        zz_edict['INPUT20'] = self.INPUT20
        zz_desc['INPUT20'] = ""
        self.INPUT21 = 0x00200000
        zz_edict['INPUT21'] = self.INPUT21
        zz_desc['INPUT21'] = ""
        self.INPUT21INPUT22 = 0x00200000
        zz_edict['INPUT21INPUT22'] = self.INPUT21INPUT22
        zz_desc['INPUT21INPUT22'] = ""
        self.INPUT22INPUT23 = 0x00400000
        zz_edict['INPUT22INPUT23'] = self.INPUT22INPUT23
        zz_desc['INPUT22INPUT23'] = ""
        self.INPUT22 = 0x00400000
        zz_edict['INPUT22'] = self.INPUT22
        zz_desc['INPUT22'] = ""
        self.INPUT23INPUT16 = 0x00800000
        zz_edict['INPUT23INPUT16'] = self.INPUT23INPUT16
        zz_desc['INPUT23INPUT16'] = ""
        self.INPUT23 = 0x00800000
        zz_edict['INPUT23'] = self.INPUT23
        zz_desc['INPUT23'] = ""
        self.INPUT24 = 0x01000000
        zz_edict['INPUT24'] = self.INPUT24
        zz_desc['INPUT24'] = ""
        self.INPUT24INPUT25 = 0x01000000
        zz_edict['INPUT24INPUT25'] = self.INPUT24INPUT25
        zz_desc['INPUT24INPUT25'] = ""
        self.INPUT25INPUT26 = 0x02000000
        zz_edict['INPUT25INPUT26'] = self.INPUT25INPUT26
        zz_desc['INPUT25INPUT26'] = ""
        self.INPUT25 = 0x02000000
        zz_edict['INPUT25'] = self.INPUT25
        zz_desc['INPUT25'] = ""
        self.INPUT26 = 0x04000000
        zz_edict['INPUT26'] = self.INPUT26
        zz_desc['INPUT26'] = ""
        self.INPUT26INPUT27 = 0x04000000
        zz_edict['INPUT26INPUT27'] = self.INPUT26INPUT27
        zz_desc['INPUT26INPUT27'] = ""
        self.INPUT27INPUT28 = 0x08000000
        zz_edict['INPUT27INPUT28'] = self.INPUT27INPUT28
        zz_desc['INPUT27INPUT28'] = ""
        self.INPUT27 = 0x08000000
        zz_edict['INPUT27'] = self.INPUT27
        zz_desc['INPUT27'] = ""
        self.INPUT28INPUT29 = 0x10000000
        zz_edict['INPUT28INPUT29'] = self.INPUT28INPUT29
        zz_desc['INPUT28INPUT29'] = ""
        self.INPUT28 = 0x10000000
        zz_edict['INPUT28'] = self.INPUT28
        zz_desc['INPUT28'] = ""
        self.INPUT29 = 0x20000000
        zz_edict['INPUT29'] = self.INPUT29
        zz_desc['INPUT29'] = ""
        self.INPUT29INPUT30 = 0x20000000
        zz_edict['INPUT29INPUT30'] = self.INPUT29INPUT30
        zz_desc['INPUT29INPUT30'] = ""
        self.INPUT30 = 0x40000000
        zz_edict['INPUT30'] = self.INPUT30
        zz_desc['INPUT30'] = ""
        self.INPUT30INPUT31 = 0x40000000
        zz_edict['INPUT30INPUT31'] = self.INPUT30INPUT31
        zz_desc['INPUT30INPUT31'] = ""
        self.INPUT31INPUT24 = 0x80000000
        zz_edict['INPUT31INPUT24'] = self.INPUT31INPUT24
        zz_desc['INPUT31INPUT24'] = ""
        self.INPUT31 = 0x80000000
        zz_edict['INPUT31'] = self.INPUT31
        zz_desc['INPUT31'] = ""
        super(RM_Enum_ADC0_SCANMASK_SCANINPUTEN, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANINPUTSEL_INPUT0TO7SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.APORT0CH0TO7 = 0x00000000
        zz_edict['APORT0CH0TO7'] = self.APORT0CH0TO7
        zz_desc['APORT0CH0TO7'] = ""
        self.APORT0CH8TO15 = 0x00000001
        zz_edict['APORT0CH8TO15'] = self.APORT0CH8TO15
        zz_desc['APORT0CH8TO15'] = ""
        self.APORT1CH0TO7 = 0x00000004
        zz_edict['APORT1CH0TO7'] = self.APORT1CH0TO7
        zz_desc['APORT1CH0TO7'] = ""
        self.APORT1CH8TO15 = 0x00000005
        zz_edict['APORT1CH8TO15'] = self.APORT1CH8TO15
        zz_desc['APORT1CH8TO15'] = ""
        self.APORT1CH16TO23 = 0x00000006
        zz_edict['APORT1CH16TO23'] = self.APORT1CH16TO23
        zz_desc['APORT1CH16TO23'] = ""
        self.APORT1CH24TO31 = 0x00000007
        zz_edict['APORT1CH24TO31'] = self.APORT1CH24TO31
        zz_desc['APORT1CH24TO31'] = ""
        self.APORT2CH0TO7 = 0x00000008
        zz_edict['APORT2CH0TO7'] = self.APORT2CH0TO7
        zz_desc['APORT2CH0TO7'] = ""
        self.APORT2CH8TO15 = 0x00000009
        zz_edict['APORT2CH8TO15'] = self.APORT2CH8TO15
        zz_desc['APORT2CH8TO15'] = ""
        self.APORT2CH16TO23 = 0x0000000A
        zz_edict['APORT2CH16TO23'] = self.APORT2CH16TO23
        zz_desc['APORT2CH16TO23'] = ""
        self.APORT2CH24TO31 = 0x0000000B
        zz_edict['APORT2CH24TO31'] = self.APORT2CH24TO31
        zz_desc['APORT2CH24TO31'] = ""
        self.APORT3CH0TO7 = 0x0000000C
        zz_edict['APORT3CH0TO7'] = self.APORT3CH0TO7
        zz_desc['APORT3CH0TO7'] = ""
        self.APORT3CH8TO15 = 0x0000000D
        zz_edict['APORT3CH8TO15'] = self.APORT3CH8TO15
        zz_desc['APORT3CH8TO15'] = ""
        self.APORT3CH16TO23 = 0x0000000E
        zz_edict['APORT3CH16TO23'] = self.APORT3CH16TO23
        zz_desc['APORT3CH16TO23'] = ""
        self.APORT3CH24TO31 = 0x0000000F
        zz_edict['APORT3CH24TO31'] = self.APORT3CH24TO31
        zz_desc['APORT3CH24TO31'] = ""
        self.APORT4CH0TO7 = 0x00000010
        zz_edict['APORT4CH0TO7'] = self.APORT4CH0TO7
        zz_desc['APORT4CH0TO7'] = ""
        self.APORT4CH8TO15 = 0x00000011
        zz_edict['APORT4CH8TO15'] = self.APORT4CH8TO15
        zz_desc['APORT4CH8TO15'] = ""
        self.APORT4CH16TO23 = 0x00000012
        zz_edict['APORT4CH16TO23'] = self.APORT4CH16TO23
        zz_desc['APORT4CH16TO23'] = ""
        self.APORT4CH24TO31 = 0x00000013
        zz_edict['APORT4CH24TO31'] = self.APORT4CH24TO31
        zz_desc['APORT4CH24TO31'] = ""
        super(RM_Enum_ADC0_SCANINPUTSEL_INPUT0TO7SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANINPUTSEL_INPUT8TO15SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.APORT0CH0TO7 = 0x00000000
        zz_edict['APORT0CH0TO7'] = self.APORT0CH0TO7
        zz_desc['APORT0CH0TO7'] = ""
        self.APORT0CH8TO15 = 0x00000001
        zz_edict['APORT0CH8TO15'] = self.APORT0CH8TO15
        zz_desc['APORT0CH8TO15'] = ""
        self.APORT1CH0TO7 = 0x00000004
        zz_edict['APORT1CH0TO7'] = self.APORT1CH0TO7
        zz_desc['APORT1CH0TO7'] = ""
        self.APORT1CH8TO15 = 0x00000005
        zz_edict['APORT1CH8TO15'] = self.APORT1CH8TO15
        zz_desc['APORT1CH8TO15'] = ""
        self.APORT1CH16TO23 = 0x00000006
        zz_edict['APORT1CH16TO23'] = self.APORT1CH16TO23
        zz_desc['APORT1CH16TO23'] = ""
        self.APORT1CH24TO31 = 0x00000007
        zz_edict['APORT1CH24TO31'] = self.APORT1CH24TO31
        zz_desc['APORT1CH24TO31'] = ""
        self.APORT2CH0TO7 = 0x00000008
        zz_edict['APORT2CH0TO7'] = self.APORT2CH0TO7
        zz_desc['APORT2CH0TO7'] = ""
        self.APORT2CH8TO15 = 0x00000009
        zz_edict['APORT2CH8TO15'] = self.APORT2CH8TO15
        zz_desc['APORT2CH8TO15'] = ""
        self.APORT2CH16TO23 = 0x0000000A
        zz_edict['APORT2CH16TO23'] = self.APORT2CH16TO23
        zz_desc['APORT2CH16TO23'] = ""
        self.APORT2CH24TO31 = 0x0000000B
        zz_edict['APORT2CH24TO31'] = self.APORT2CH24TO31
        zz_desc['APORT2CH24TO31'] = ""
        self.APORT3CH0TO7 = 0x0000000C
        zz_edict['APORT3CH0TO7'] = self.APORT3CH0TO7
        zz_desc['APORT3CH0TO7'] = ""
        self.APORT3CH8TO15 = 0x0000000D
        zz_edict['APORT3CH8TO15'] = self.APORT3CH8TO15
        zz_desc['APORT3CH8TO15'] = ""
        self.APORT3CH16TO23 = 0x0000000E
        zz_edict['APORT3CH16TO23'] = self.APORT3CH16TO23
        zz_desc['APORT3CH16TO23'] = ""
        self.APORT3CH24TO31 = 0x0000000F
        zz_edict['APORT3CH24TO31'] = self.APORT3CH24TO31
        zz_desc['APORT3CH24TO31'] = ""
        self.APORT4CH0TO7 = 0x00000010
        zz_edict['APORT4CH0TO7'] = self.APORT4CH0TO7
        zz_desc['APORT4CH0TO7'] = ""
        self.APORT4CH8TO15 = 0x00000011
        zz_edict['APORT4CH8TO15'] = self.APORT4CH8TO15
        zz_desc['APORT4CH8TO15'] = ""
        self.APORT4CH16TO23 = 0x00000012
        zz_edict['APORT4CH16TO23'] = self.APORT4CH16TO23
        zz_desc['APORT4CH16TO23'] = ""
        self.APORT4CH24TO31 = 0x00000013
        zz_edict['APORT4CH24TO31'] = self.APORT4CH24TO31
        zz_desc['APORT4CH24TO31'] = ""
        super(RM_Enum_ADC0_SCANINPUTSEL_INPUT8TO15SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANINPUTSEL_INPUT16TO23SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.APORT0CH0TO7 = 0x00000000
        zz_edict['APORT0CH0TO7'] = self.APORT0CH0TO7
        zz_desc['APORT0CH0TO7'] = ""
        self.APORT0CH8TO15 = 0x00000001
        zz_edict['APORT0CH8TO15'] = self.APORT0CH8TO15
        zz_desc['APORT0CH8TO15'] = ""
        self.APORT1CH0TO7 = 0x00000004
        zz_edict['APORT1CH0TO7'] = self.APORT1CH0TO7
        zz_desc['APORT1CH0TO7'] = ""
        self.APORT1CH8TO15 = 0x00000005
        zz_edict['APORT1CH8TO15'] = self.APORT1CH8TO15
        zz_desc['APORT1CH8TO15'] = ""
        self.APORT1CH16TO23 = 0x00000006
        zz_edict['APORT1CH16TO23'] = self.APORT1CH16TO23
        zz_desc['APORT1CH16TO23'] = ""
        self.APORT1CH24TO31 = 0x00000007
        zz_edict['APORT1CH24TO31'] = self.APORT1CH24TO31
        zz_desc['APORT1CH24TO31'] = ""
        self.APORT2CH0TO7 = 0x00000008
        zz_edict['APORT2CH0TO7'] = self.APORT2CH0TO7
        zz_desc['APORT2CH0TO7'] = ""
        self.APORT2CH8TO15 = 0x00000009
        zz_edict['APORT2CH8TO15'] = self.APORT2CH8TO15
        zz_desc['APORT2CH8TO15'] = ""
        self.APORT2CH16TO23 = 0x0000000A
        zz_edict['APORT2CH16TO23'] = self.APORT2CH16TO23
        zz_desc['APORT2CH16TO23'] = ""
        self.APORT2CH24TO31 = 0x0000000B
        zz_edict['APORT2CH24TO31'] = self.APORT2CH24TO31
        zz_desc['APORT2CH24TO31'] = ""
        self.APORT3CH0TO7 = 0x0000000C
        zz_edict['APORT3CH0TO7'] = self.APORT3CH0TO7
        zz_desc['APORT3CH0TO7'] = ""
        self.APORT3CH8TO15 = 0x0000000D
        zz_edict['APORT3CH8TO15'] = self.APORT3CH8TO15
        zz_desc['APORT3CH8TO15'] = ""
        self.APORT3CH16TO23 = 0x0000000E
        zz_edict['APORT3CH16TO23'] = self.APORT3CH16TO23
        zz_desc['APORT3CH16TO23'] = ""
        self.APORT3CH24TO31 = 0x0000000F
        zz_edict['APORT3CH24TO31'] = self.APORT3CH24TO31
        zz_desc['APORT3CH24TO31'] = ""
        self.APORT4CH0TO7 = 0x00000010
        zz_edict['APORT4CH0TO7'] = self.APORT4CH0TO7
        zz_desc['APORT4CH0TO7'] = ""
        self.APORT4CH8TO15 = 0x00000011
        zz_edict['APORT4CH8TO15'] = self.APORT4CH8TO15
        zz_desc['APORT4CH8TO15'] = ""
        self.APORT4CH16TO23 = 0x00000012
        zz_edict['APORT4CH16TO23'] = self.APORT4CH16TO23
        zz_desc['APORT4CH16TO23'] = ""
        self.APORT4CH24TO31 = 0x00000013
        zz_edict['APORT4CH24TO31'] = self.APORT4CH24TO31
        zz_desc['APORT4CH24TO31'] = ""
        super(RM_Enum_ADC0_SCANINPUTSEL_INPUT16TO23SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANINPUTSEL_INPUT24TO31SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.APORT0CH0TO7 = 0x00000000
        zz_edict['APORT0CH0TO7'] = self.APORT0CH0TO7
        zz_desc['APORT0CH0TO7'] = ""
        self.APORT0CH8TO15 = 0x00000001
        zz_edict['APORT0CH8TO15'] = self.APORT0CH8TO15
        zz_desc['APORT0CH8TO15'] = ""
        self.APORT1CH0TO7 = 0x00000004
        zz_edict['APORT1CH0TO7'] = self.APORT1CH0TO7
        zz_desc['APORT1CH0TO7'] = ""
        self.APORT1CH8TO15 = 0x00000005
        zz_edict['APORT1CH8TO15'] = self.APORT1CH8TO15
        zz_desc['APORT1CH8TO15'] = ""
        self.APORT1CH16TO23 = 0x00000006
        zz_edict['APORT1CH16TO23'] = self.APORT1CH16TO23
        zz_desc['APORT1CH16TO23'] = ""
        self.APORT1CH24TO31 = 0x00000007
        zz_edict['APORT1CH24TO31'] = self.APORT1CH24TO31
        zz_desc['APORT1CH24TO31'] = ""
        self.APORT2CH0TO7 = 0x00000008
        zz_edict['APORT2CH0TO7'] = self.APORT2CH0TO7
        zz_desc['APORT2CH0TO7'] = ""
        self.APORT2CH8TO15 = 0x00000009
        zz_edict['APORT2CH8TO15'] = self.APORT2CH8TO15
        zz_desc['APORT2CH8TO15'] = ""
        self.APORT2CH16TO23 = 0x0000000A
        zz_edict['APORT2CH16TO23'] = self.APORT2CH16TO23
        zz_desc['APORT2CH16TO23'] = ""
        self.APORT2CH24TO31 = 0x0000000B
        zz_edict['APORT2CH24TO31'] = self.APORT2CH24TO31
        zz_desc['APORT2CH24TO31'] = ""
        self.APORT3CH0TO7 = 0x0000000C
        zz_edict['APORT3CH0TO7'] = self.APORT3CH0TO7
        zz_desc['APORT3CH0TO7'] = ""
        self.APORT3CH8TO15 = 0x0000000D
        zz_edict['APORT3CH8TO15'] = self.APORT3CH8TO15
        zz_desc['APORT3CH8TO15'] = ""
        self.APORT3CH16TO23 = 0x0000000E
        zz_edict['APORT3CH16TO23'] = self.APORT3CH16TO23
        zz_desc['APORT3CH16TO23'] = ""
        self.APORT3CH24TO31 = 0x0000000F
        zz_edict['APORT3CH24TO31'] = self.APORT3CH24TO31
        zz_desc['APORT3CH24TO31'] = ""
        self.APORT4CH0TO7 = 0x00000010
        zz_edict['APORT4CH0TO7'] = self.APORT4CH0TO7
        zz_desc['APORT4CH0TO7'] = ""
        self.APORT4CH8TO15 = 0x00000011
        zz_edict['APORT4CH8TO15'] = self.APORT4CH8TO15
        zz_desc['APORT4CH8TO15'] = ""
        self.APORT4CH16TO23 = 0x00000012
        zz_edict['APORT4CH16TO23'] = self.APORT4CH16TO23
        zz_desc['APORT4CH16TO23'] = ""
        self.APORT4CH24TO31 = 0x00000013
        zz_edict['APORT4CH24TO31'] = self.APORT4CH24TO31
        zz_desc['APORT4CH24TO31'] = ""
        super(RM_Enum_ADC0_SCANINPUTSEL_INPUT24TO31SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNEGSEL_INPUT0NEGSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.INPUT1 = 0x00000000
        zz_edict['INPUT1'] = self.INPUT1
        zz_desc['INPUT1'] = ""
        self.INPUT3 = 0x00000001
        zz_edict['INPUT3'] = self.INPUT3
        zz_desc['INPUT3'] = ""
        self.INPUT5 = 0x00000002
        zz_edict['INPUT5'] = self.INPUT5
        zz_desc['INPUT5'] = ""
        self.INPUT7 = 0x00000003
        zz_edict['INPUT7'] = self.INPUT7
        zz_desc['INPUT7'] = ""
        super(RM_Enum_ADC0_SCANNEGSEL_INPUT0NEGSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNEGSEL_INPUT2NEGSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.INPUT1 = 0x00000000
        zz_edict['INPUT1'] = self.INPUT1
        zz_desc['INPUT1'] = ""
        self.INPUT3 = 0x00000001
        zz_edict['INPUT3'] = self.INPUT3
        zz_desc['INPUT3'] = ""
        self.INPUT5 = 0x00000002
        zz_edict['INPUT5'] = self.INPUT5
        zz_desc['INPUT5'] = ""
        self.INPUT7 = 0x00000003
        zz_edict['INPUT7'] = self.INPUT7
        zz_desc['INPUT7'] = ""
        super(RM_Enum_ADC0_SCANNEGSEL_INPUT2NEGSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNEGSEL_INPUT4NEGSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.INPUT1 = 0x00000000
        zz_edict['INPUT1'] = self.INPUT1
        zz_desc['INPUT1'] = ""
        self.INPUT3 = 0x00000001
        zz_edict['INPUT3'] = self.INPUT3
        zz_desc['INPUT3'] = ""
        self.INPUT5 = 0x00000002
        zz_edict['INPUT5'] = self.INPUT5
        zz_desc['INPUT5'] = ""
        self.INPUT7 = 0x00000003
        zz_edict['INPUT7'] = self.INPUT7
        zz_desc['INPUT7'] = ""
        super(RM_Enum_ADC0_SCANNEGSEL_INPUT4NEGSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNEGSEL_INPUT6NEGSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.INPUT1 = 0x00000000
        zz_edict['INPUT1'] = self.INPUT1
        zz_desc['INPUT1'] = ""
        self.INPUT3 = 0x00000001
        zz_edict['INPUT3'] = self.INPUT3
        zz_desc['INPUT3'] = ""
        self.INPUT5 = 0x00000002
        zz_edict['INPUT5'] = self.INPUT5
        zz_desc['INPUT5'] = ""
        self.INPUT7 = 0x00000003
        zz_edict['INPUT7'] = self.INPUT7
        zz_desc['INPUT7'] = ""
        super(RM_Enum_ADC0_SCANNEGSEL_INPUT6NEGSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNEGSEL_INPUT9NEGSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.INPUT8 = 0x00000000
        zz_edict['INPUT8'] = self.INPUT8
        zz_desc['INPUT8'] = ""
        self.INPUT10 = 0x00000001
        zz_edict['INPUT10'] = self.INPUT10
        zz_desc['INPUT10'] = ""
        self.INPUT12 = 0x00000002
        zz_edict['INPUT12'] = self.INPUT12
        zz_desc['INPUT12'] = ""
        self.INPUT14 = 0x00000003
        zz_edict['INPUT14'] = self.INPUT14
        zz_desc['INPUT14'] = ""
        super(RM_Enum_ADC0_SCANNEGSEL_INPUT9NEGSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNEGSEL_INPUT11NEGSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.INPUT8 = 0x00000000
        zz_edict['INPUT8'] = self.INPUT8
        zz_desc['INPUT8'] = ""
        self.INPUT10 = 0x00000001
        zz_edict['INPUT10'] = self.INPUT10
        zz_desc['INPUT10'] = ""
        self.INPUT12 = 0x00000002
        zz_edict['INPUT12'] = self.INPUT12
        zz_desc['INPUT12'] = ""
        self.INPUT14 = 0x00000003
        zz_edict['INPUT14'] = self.INPUT14
        zz_desc['INPUT14'] = ""
        super(RM_Enum_ADC0_SCANNEGSEL_INPUT11NEGSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNEGSEL_INPUT13NEGSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.INPUT8 = 0x00000000
        zz_edict['INPUT8'] = self.INPUT8
        zz_desc['INPUT8'] = ""
        self.INPUT10 = 0x00000001
        zz_edict['INPUT10'] = self.INPUT10
        zz_desc['INPUT10'] = ""
        self.INPUT12 = 0x00000002
        zz_edict['INPUT12'] = self.INPUT12
        zz_desc['INPUT12'] = ""
        self.INPUT14 = 0x00000003
        zz_edict['INPUT14'] = self.INPUT14
        zz_desc['INPUT14'] = ""
        super(RM_Enum_ADC0_SCANNEGSEL_INPUT13NEGSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNEGSEL_INPUT15NEGSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.INPUT8 = 0x00000000
        zz_edict['INPUT8'] = self.INPUT8
        zz_desc['INPUT8'] = ""
        self.INPUT10 = 0x00000001
        zz_edict['INPUT10'] = self.INPUT10
        zz_desc['INPUT10'] = ""
        self.INPUT12 = 0x00000002
        zz_edict['INPUT12'] = self.INPUT12
        zz_desc['INPUT12'] = ""
        self.INPUT14 = 0x00000003
        zz_edict['INPUT14'] = self.INPUT14
        zz_desc['INPUT14'] = ""
        super(RM_Enum_ADC0_SCANNEGSEL_INPUT15NEGSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_BIASPROG_ADCBIASPROG(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NORMAL = 0x00000000
        zz_edict['NORMAL'] = self.NORMAL
        zz_desc['NORMAL'] = ""
        self.SCALE2 = 0x00000004
        zz_edict['SCALE2'] = self.SCALE2
        zz_desc['SCALE2'] = ""
        self.SCALE4 = 0x00000008
        zz_edict['SCALE4'] = self.SCALE4
        zz_desc['SCALE4'] = ""
        self.SCALE8 = 0x0000000C
        zz_edict['SCALE8'] = self.SCALE8
        zz_desc['SCALE8'] = ""
        self.SCALE16 = 0x0000000E
        zz_edict['SCALE16'] = self.SCALE16
        zz_desc['SCALE16'] = ""
        self.SCALE32 = 0x0000000F
        zz_edict['SCALE32'] = self.SCALE32
        zz_desc['SCALE32'] = ""
        super(RM_Enum_ADC0_BIASPROG_ADCBIASPROG, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_BIASPROG_CONVSPEED(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.X2 = 0x00000000
        zz_edict['X2'] = self.X2
        zz_desc['X2'] = ""
        self.X1 = 0x00000001
        zz_edict['X1'] = self.X1
        zz_desc['X1'] = ""
        self.X1DIV2 = 0x00000002
        zz_edict['X1DIV2'] = self.X1DIV2
        zz_desc['X1DIV2'] = ""
        self.X1DIV3 = 0x00000003
        zz_edict['X1DIV3'] = self.X1DIV3
        zz_desc['X1DIV3'] = ""
        super(RM_Enum_ADC0_BIASPROG_CONVSPEED, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_TEST_VREGSTEP(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '1P30V' to 'E1P30V'")
        self.E1P30V = 0x00000000
        zz_edict['E1P30V'] = self.E1P30V
        zz_desc['E1P30V'] = ""
        #print("WARNING: Aliasing enum '1P34V' to 'E1P34V'")
        self.E1P34V = 0x00000001
        zz_edict['E1P34V'] = self.E1P34V
        zz_desc['E1P34V'] = ""
        #print("WARNING: Aliasing enum '1P23V' to 'E1P23V'")
        self.E1P23V = 0x00000002
        zz_edict['E1P23V'] = self.E1P23V
        zz_desc['E1P23V'] = ""
        #print("WARNING: Aliasing enum '1P26V' to 'E1P26V'")
        self.E1P26V = 0x00000003
        zz_edict['E1P26V'] = self.E1P26V
        zz_desc['E1P26V'] = ""
        super(RM_Enum_ADC0_TEST_VREGSTEP, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_TEST_VCMSTEP(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0P70V' to 'E0P70V'")
        self.E0P70V = 0x00000000
        zz_edict['E0P70V'] = self.E0P70V
        zz_desc['E0P70V'] = ""
        #print("WARNING: Aliasing enum '0P74V' to 'E0P74V'")
        self.E0P74V = 0x00000001
        zz_edict['E0P74V'] = self.E0P74V
        zz_desc['E0P74V'] = ""
        #print("WARNING: Aliasing enum '0P62V' to 'E0P62V'")
        self.E0P62V = 0x00000002
        zz_edict['E0P62V'] = self.E0P62V
        zz_desc['E0P62V'] = ""
        #print("WARNING: Aliasing enum '0P66V' to 'E0P66V'")
        self.E0P66V = 0x00000003
        zz_edict['E0P66V'] = self.E0P66V
        zz_desc['E0P66V'] = ""
        super(RM_Enum_ADC0_TEST_VCMSTEP, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


