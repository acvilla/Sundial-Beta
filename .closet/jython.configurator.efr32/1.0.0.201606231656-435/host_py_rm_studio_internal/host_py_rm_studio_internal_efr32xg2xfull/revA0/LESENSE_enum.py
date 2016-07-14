
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_LESENSE_CTRL_SCANMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PERIODIC = 0x00000000
        zz_edict['PERIODIC'] = self.PERIODIC
        zz_desc['PERIODIC'] = ""
        self.ONESHOT = 0x00000001
        zz_edict['ONESHOT'] = self.ONESHOT
        zz_desc['ONESHOT'] = ""
        self.PRS = 0x00000002
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        super(RM_Enum_LESENSE_CTRL_SCANMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_LESENSE_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CTRL_SCANCONF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIRMAP = 0x00000000
        zz_edict['DIRMAP'] = self.DIRMAP
        zz_desc['DIRMAP'] = ""
        self.INVMAP = 0x00000001
        zz_edict['INVMAP'] = self.INVMAP
        zz_desc['INVMAP'] = ""
        self.TOGGLE = 0x00000002
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.DECDEF = 0x00000003
        zz_edict['DECDEF'] = self.DECDEF
        zz_desc['DECDEF'] = ""
        super(RM_Enum_LESENSE_CTRL_SCANCONF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CTRL_DMAWU(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.BUFDATAV = 0x00000001
        zz_edict['BUFDATAV'] = self.BUFDATAV
        zz_desc['BUFDATAV'] = ""
        self.BUFLEVEL = 0x00000002
        zz_edict['BUFLEVEL'] = self.BUFLEVEL
        zz_desc['BUFLEVEL'] = ""
        super(RM_Enum_LESENSE_CTRL_DMAWU, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_TIMCTRL_AUXPRESC(Base_RM_Enum):
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
        super(RM_Enum_LESENSE_TIMCTRL_AUXPRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_TIMCTRL_LFPRESC(Base_RM_Enum):
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
        self.DIV16 = 0x00000004
        zz_edict['DIV16'] = self.DIV16
        zz_desc['DIV16'] = ""
        self.DIV32 = 0x00000005
        zz_edict['DIV32'] = self.DIV32
        zz_desc['DIV32'] = ""
        self.DIV64 = 0x00000006
        zz_edict['DIV64'] = self.DIV64
        zz_desc['DIV64'] = ""
        self.DIV128 = 0x00000007
        zz_edict['DIV128'] = self.DIV128
        zz_desc['DIV128'] = ""
        super(RM_Enum_LESENSE_TIMCTRL_LFPRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_TIMCTRL_PCPRESC(Base_RM_Enum):
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
        self.DIV16 = 0x00000004
        zz_edict['DIV16'] = self.DIV16
        zz_desc['DIV16'] = ""
        self.DIV32 = 0x00000005
        zz_edict['DIV32'] = self.DIV32
        zz_desc['DIV32'] = ""
        self.DIV64 = 0x00000006
        zz_edict['DIV64'] = self.DIV64
        zz_desc['DIV64'] = ""
        self.DIV128 = 0x00000007
        zz_edict['DIV128'] = self.DIV128
        zz_desc['DIV128'] = ""
        super(RM_Enum_LESENSE_TIMCTRL_PCPRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_PERCTRL_ACMP0MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.MUX = 0x00000001
        zz_edict['MUX'] = self.MUX
        zz_desc['MUX'] = ""
        self.MUXTHRES = 0x00000002
        zz_edict['MUXTHRES'] = self.MUXTHRES
        zz_desc['MUXTHRES'] = ""
        super(RM_Enum_LESENSE_PERCTRL_ACMP0MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_PERCTRL_ACMP1MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.MUX = 0x00000001
        zz_edict['MUX'] = self.MUX
        zz_desc['MUX'] = ""
        self.MUXTHRES = 0x00000002
        zz_edict['MUXTHRES'] = self.MUXTHRES
        zz_desc['MUXTHRES'] = ""
        super(RM_Enum_LESENSE_PERCTRL_ACMP1MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_PERCTRL_WARMUPMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NORMAL = 0x00000000
        zz_edict['NORMAL'] = self.NORMAL
        zz_desc['NORMAL'] = ""
        self.KEEPACMPWARM = 0x00000001
        zz_edict['KEEPACMPWARM'] = self.KEEPACMPWARM
        zz_desc['KEEPACMPWARM'] = ""
        self.KEEPDACWARM = 0x00000002
        zz_edict['KEEPDACWARM'] = self.KEEPDACWARM
        zz_desc['KEEPDACWARM'] = ""
        self.KEEPACMPDACWARM = 0x00000003
        zz_edict['KEEPACMPDACWARM'] = self.KEEPACMPDACWARM
        zz_desc['KEEPACMPDACWARM'] = ""
        super(RM_Enum_LESENSE_PERCTRL_WARMUPMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_DECCTRL_PRSSEL0(Base_RM_Enum):
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
        super(RM_Enum_LESENSE_DECCTRL_PRSSEL0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_DECCTRL_PRSSEL1(Base_RM_Enum):
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
        super(RM_Enum_LESENSE_DECCTRL_PRSSEL1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_DECCTRL_PRSSEL2(Base_RM_Enum):
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
        super(RM_Enum_LESENSE_DECCTRL_PRSSEL2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_DECCTRL_PRSSEL3(Base_RM_Enum):
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
        super(RM_Enum_LESENSE_DECCTRL_PRSSEL3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_BIASCTRL_BIASMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DONTTOUCH = 0x00000000
        zz_edict['DONTTOUCH'] = self.DONTTOUCH
        zz_desc['DONTTOUCH'] = ""
        self.DUTYCYCLE = 0x00000001
        zz_edict['DUTYCYCLE'] = self.DUTYCYCLE
        zz_desc['DUTYCYCLE'] = ""
        self.HIGHACC = 0x00000002
        zz_edict['HIGHACC'] = self.HIGHACC
        zz_desc['HIGHACC'] = ""
        super(RM_Enum_LESENSE_BIASCTRL_BIASMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_IDLECONF_CH15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DAC = 0x00000003
        zz_edict['DAC'] = self.DAC
        zz_desc['DAC'] = ""
        super(RM_Enum_LESENSE_IDLECONF_CH15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_ALTEXCONF_IDLECONF0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        super(RM_Enum_LESENSE_ALTEXCONF_IDLECONF0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_ALTEXCONF_IDLECONF1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        super(RM_Enum_LESENSE_ALTEXCONF_IDLECONF1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_ALTEXCONF_IDLECONF2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        super(RM_Enum_LESENSE_ALTEXCONF_IDLECONF2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_ALTEXCONF_IDLECONF3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        super(RM_Enum_LESENSE_ALTEXCONF_IDLECONF3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_ALTEXCONF_IDLECONF4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        super(RM_Enum_LESENSE_ALTEXCONF_IDLECONF4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_ALTEXCONF_IDLECONF5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        super(RM_Enum_LESENSE_ALTEXCONF_IDLECONF5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_ALTEXCONF_IDLECONF6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        super(RM_Enum_LESENSE_ALTEXCONF_IDLECONF6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_ALTEXCONF_IDLECONF7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        super(RM_Enum_LESENSE_ALTEXCONF_IDLECONF7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH0_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH0_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH0_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH0_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH0_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH0_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH0_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH0_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH0_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH0_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH1_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH1_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH1_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH1_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH1_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH1_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH1_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH1_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH1_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH1_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH2_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH2_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH2_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH2_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH2_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH2_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH2_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH2_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH2_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH2_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH3_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH3_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH3_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH3_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH3_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH3_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH3_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH3_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH3_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH3_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH4_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH4_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH4_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH4_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH4_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH4_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH4_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH4_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH4_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH4_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH5_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH5_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH5_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH5_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH5_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH5_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH5_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH5_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH5_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH5_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH6_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH6_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH6_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH6_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH6_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH6_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH6_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH6_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH6_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH6_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH7_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH7_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH7_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH7_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH7_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH7_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH7_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH7_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH7_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH7_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH8_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH8_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH8_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH8_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH8_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH8_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH8_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH8_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH8_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH8_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH9_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH9_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH9_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH9_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH9_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH9_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH9_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH9_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH9_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH9_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH10_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH10_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH10_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH10_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH10_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH10_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH10_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH10_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH10_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH10_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH11_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH11_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH11_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH11_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH11_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH11_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH11_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH11_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH11_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH11_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH12_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH12_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH12_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH12_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH12_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH12_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH12_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH12_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH12_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH12_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH13_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH13_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH13_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH13_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH13_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH13_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH13_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH13_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH13_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH13_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH14_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH14_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH14_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH14_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH14_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH14_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH14_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH14_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH14_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH14_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH15_INTERACT_SAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACMPCOUNT = 0x00000000
        zz_edict['ACMPCOUNT'] = self.ACMPCOUNT
        zz_desc['ACMPCOUNT'] = ""
        self.ACMP = 0x00000001
        zz_edict['ACMP'] = self.ACMP
        zz_desc['ACMP'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.ADCDIFF = 0x00000003
        zz_edict['ADCDIFF'] = self.ADCDIFF
        zz_desc['ADCDIFF'] = ""
        super(RM_Enum_LESENSE_CH15_INTERACT_SAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH15_INTERACT_SETIF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.LEVEL = 0x00000001
        zz_edict['LEVEL'] = self.LEVEL
        zz_desc['LEVEL'] = ""
        self.POSEDGE = 0x00000002
        zz_edict['POSEDGE'] = self.POSEDGE
        zz_desc['POSEDGE'] = ""
        self.NEGEDGE = 0x00000003
        zz_edict['NEGEDGE'] = self.NEGEDGE
        zz_desc['NEGEDGE'] = ""
        self.BOTHEDGES = 0x00000004
        zz_edict['BOTHEDGES'] = self.BOTHEDGES
        zz_desc['BOTHEDGES'] = ""
        super(RM_Enum_LESENSE_CH15_INTERACT_SETIF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH15_INTERACT_EXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        self.LOW = 0x00000002
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.DACOUT = 0x00000003
        zz_edict['DACOUT'] = self.DACOUT
        zz_desc['DACOUT'] = ""
        super(RM_Enum_LESENSE_CH15_INTERACT_EXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH15_EVAL_STRSAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.DATA = 0x00000001
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATASRC = 0x00000002
        zz_edict['DATASRC'] = self.DATASRC
        zz_desc['DATASRC'] = ""
        super(RM_Enum_LESENSE_CH15_EVAL_STRSAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LESENSE_CH15_EVAL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.THRES = 0x00000000
        zz_edict['THRES'] = self.THRES
        zz_desc['THRES'] = ""
        self.SLIDINGWIN = 0x00000001
        zz_edict['SLIDINGWIN'] = self.SLIDINGWIN
        zz_desc['SLIDINGWIN'] = ""
        self.STEPDET = 0x00000002
        zz_edict['STEPDET'] = self.STEPDET
        zz_desc['STEPDET'] = ""
        super(RM_Enum_LESENSE_CH15_EVAL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


