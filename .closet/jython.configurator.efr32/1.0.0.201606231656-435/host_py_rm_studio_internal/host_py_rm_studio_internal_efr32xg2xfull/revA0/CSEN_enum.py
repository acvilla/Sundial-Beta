
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_CSEN_CTRL_CM(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.SGL = 0x00000000
        zz_edict['SGL'] = self.SGL
        zz_desc['SGL'] = ""
        self.SCAN = 0x00000001
        zz_edict['SCAN'] = self.SCAN
        zz_desc['SCAN'] = ""
        self.CONTSGL = 0x00000002
        zz_edict['CONTSGL'] = self.CONTSGL
        zz_desc['CONTSGL'] = ""
        self.CONTSCAN = 0x00000003
        zz_edict['CONTSCAN'] = self.CONTSCAN
        zz_desc['CONTSCAN'] = ""
        super(RM_Enum_CSEN_CTRL_CM, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_CTRL_SARCR(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CLK10 = 0x00000000
        zz_edict['CLK10'] = self.CLK10
        zz_desc['CLK10'] = ""
        self.CLK12 = 0x00000001
        zz_edict['CLK12'] = self.CLK12
        zz_desc['CLK12'] = ""
        self.CLK14 = 0x00000002
        zz_edict['CLK14'] = self.CLK14
        zz_desc['CLK14'] = ""
        self.CLK16 = 0x00000003
        zz_edict['CLK16'] = self.CLK16
        zz_desc['CLK16'] = ""
        super(RM_Enum_CSEN_CTRL_SARCR, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_CTRL_ACU(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ACC1 = 0x00000000
        zz_edict['ACC1'] = self.ACC1
        zz_desc['ACC1'] = ""
        self.ACC2 = 0x00000001
        zz_edict['ACC2'] = self.ACC2
        zz_desc['ACC2'] = ""
        self.ACC4 = 0x00000002
        zz_edict['ACC4'] = self.ACC4
        zz_desc['ACC4'] = ""
        self.ACC8 = 0x00000003
        zz_edict['ACC8'] = self.ACC8
        zz_desc['ACC8'] = ""
        self.ACC16 = 0x00000004
        zz_edict['ACC16'] = self.ACC16
        zz_desc['ACC16'] = ""
        self.ACC32 = 0x00000005
        zz_edict['ACC32'] = self.ACC32
        zz_desc['ACC32'] = ""
        self.ACC64 = 0x00000006
        zz_edict['ACC64'] = self.ACC64
        zz_desc['ACC64'] = ""
        super(RM_Enum_CSEN_CTRL_ACU, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_CTRL_STM(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PRS = 0x00000000
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.TIMER = 0x00000001
        zz_edict['TIMER'] = self.TIMER
        zz_desc['TIMER'] = ""
        self.START = 0x00000002
        zz_edict['START'] = self.START
        zz_desc['START'] = ""
        super(RM_Enum_CSEN_CTRL_STM, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_TIMCTRL_PCPRESC(Base_RM_Enum):
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
        super(RM_Enum_CSEN_TIMCTRL_PCPRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_PRSSEL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_CSEN_PRSSEL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_SCANINPUTSEL0_INPUT0TO7SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
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
        super(RM_Enum_CSEN_SCANINPUTSEL0_INPUT0TO7SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_SCANINPUTSEL0_INPUT8TO15SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
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
        super(RM_Enum_CSEN_SCANINPUTSEL0_INPUT8TO15SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_SCANINPUTSEL0_INPUT16TO23SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
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
        super(RM_Enum_CSEN_SCANINPUTSEL0_INPUT16TO23SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_SCANINPUTSEL0_INPUT24TO31SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
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
        super(RM_Enum_CSEN_SCANINPUTSEL0_INPUT24TO31SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_SCANINPUTSEL1_INPUT32TO39SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
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
        super(RM_Enum_CSEN_SCANINPUTSEL1_INPUT32TO39SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_SCANINPUTSEL1_INPUT40TO47SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
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
        super(RM_Enum_CSEN_SCANINPUTSEL1_INPUT40TO47SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_SCANINPUTSEL1_INPUT48TO55SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
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
        super(RM_Enum_CSEN_SCANINPUTSEL1_INPUT48TO55SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_SCANINPUTSEL1_INPUT56TO63SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
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
        super(RM_Enum_CSEN_SCANINPUTSEL1_INPUT56TO63SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_EMACTRL_EMASAMPLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.W1 = 0x00000000
        zz_edict['W1'] = self.W1
        zz_desc['W1'] = ""
        self.W2 = 0x00000001
        zz_edict['W2'] = self.W2
        zz_desc['W2'] = ""
        self.W4 = 0x00000002
        zz_edict['W4'] = self.W4
        zz_desc['W4'] = ""
        self.W8 = 0x00000003
        zz_edict['W8'] = self.W8
        zz_desc['W8'] = ""
        self.W16 = 0x00000004
        zz_edict['W16'] = self.W16
        zz_desc['W16'] = ""
        self.W32 = 0x00000005
        zz_edict['W32'] = self.W32
        zz_desc['W32'] = ""
        self.W64 = 0x00000006
        zz_edict['W64'] = self.W64
        zz_desc['W64'] = ""
        super(RM_Enum_CSEN_EMACTRL_EMASAMPLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_SINGLECTRL_SINGLESEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.APORT1XCH0 = 0x00000020
        zz_edict['APORT1XCH0'] = self.APORT1XCH0
        zz_desc['APORT1XCH0'] = ""
        self.APORT1YCH1 = 0x00000021
        zz_edict['APORT1YCH1'] = self.APORT1YCH1
        zz_desc['APORT1YCH1'] = ""
        self.APORT1XCH2 = 0x00000022
        zz_edict['APORT1XCH2'] = self.APORT1XCH2
        zz_desc['APORT1XCH2'] = ""
        self.APORT1YCH3 = 0x00000023
        zz_edict['APORT1YCH3'] = self.APORT1YCH3
        zz_desc['APORT1YCH3'] = ""
        self.APORT1XCH4 = 0x00000024
        zz_edict['APORT1XCH4'] = self.APORT1XCH4
        zz_desc['APORT1XCH4'] = ""
        self.APORT1YCH5 = 0x00000025
        zz_edict['APORT1YCH5'] = self.APORT1YCH5
        zz_desc['APORT1YCH5'] = ""
        self.APORT1XCH6 = 0x00000026
        zz_edict['APORT1XCH6'] = self.APORT1XCH6
        zz_desc['APORT1XCH6'] = ""
        self.APORT1YCH7 = 0x00000027
        zz_edict['APORT1YCH7'] = self.APORT1YCH7
        zz_desc['APORT1YCH7'] = ""
        self.APORT1XCH8 = 0x00000028
        zz_edict['APORT1XCH8'] = self.APORT1XCH8
        zz_desc['APORT1XCH8'] = ""
        self.APORT1YCH9 = 0x00000029
        zz_edict['APORT1YCH9'] = self.APORT1YCH9
        zz_desc['APORT1YCH9'] = ""
        self.APORT1XCH10 = 0x0000002A
        zz_edict['APORT1XCH10'] = self.APORT1XCH10
        zz_desc['APORT1XCH10'] = ""
        self.APORT1YCH11 = 0x0000002B
        zz_edict['APORT1YCH11'] = self.APORT1YCH11
        zz_desc['APORT1YCH11'] = ""
        self.APORT1XCH12 = 0x0000002C
        zz_edict['APORT1XCH12'] = self.APORT1XCH12
        zz_desc['APORT1XCH12'] = ""
        self.APORT1YCH13 = 0x0000002D
        zz_edict['APORT1YCH13'] = self.APORT1YCH13
        zz_desc['APORT1YCH13'] = ""
        self.APORT1XCH14 = 0x0000002E
        zz_edict['APORT1XCH14'] = self.APORT1XCH14
        zz_desc['APORT1XCH14'] = ""
        self.APORT1YCH15 = 0x0000002F
        zz_edict['APORT1YCH15'] = self.APORT1YCH15
        zz_desc['APORT1YCH15'] = ""
        self.APORT1XCH16 = 0x00000030
        zz_edict['APORT1XCH16'] = self.APORT1XCH16
        zz_desc['APORT1XCH16'] = ""
        self.APORT1YCH17 = 0x00000031
        zz_edict['APORT1YCH17'] = self.APORT1YCH17
        zz_desc['APORT1YCH17'] = ""
        self.APORT1XCH18 = 0x00000032
        zz_edict['APORT1XCH18'] = self.APORT1XCH18
        zz_desc['APORT1XCH18'] = ""
        self.APORT1YCH19 = 0x00000033
        zz_edict['APORT1YCH19'] = self.APORT1YCH19
        zz_desc['APORT1YCH19'] = ""
        self.APORT1XCH20 = 0x00000034
        zz_edict['APORT1XCH20'] = self.APORT1XCH20
        zz_desc['APORT1XCH20'] = ""
        self.APORT1YCH21 = 0x00000035
        zz_edict['APORT1YCH21'] = self.APORT1YCH21
        zz_desc['APORT1YCH21'] = ""
        self.APORT1XCH22 = 0x00000036
        zz_edict['APORT1XCH22'] = self.APORT1XCH22
        zz_desc['APORT1XCH22'] = ""
        self.APORT1YCH23 = 0x00000037
        zz_edict['APORT1YCH23'] = self.APORT1YCH23
        zz_desc['APORT1YCH23'] = ""
        self.APORT1XCH24 = 0x00000038
        zz_edict['APORT1XCH24'] = self.APORT1XCH24
        zz_desc['APORT1XCH24'] = ""
        self.APORT1YCH25 = 0x00000039
        zz_edict['APORT1YCH25'] = self.APORT1YCH25
        zz_desc['APORT1YCH25'] = ""
        self.APORT1XCH26 = 0x0000003A
        zz_edict['APORT1XCH26'] = self.APORT1XCH26
        zz_desc['APORT1XCH26'] = ""
        self.APORT1YCH27 = 0x0000003B
        zz_edict['APORT1YCH27'] = self.APORT1YCH27
        zz_desc['APORT1YCH27'] = ""
        self.APORT1XCH28 = 0x0000003C
        zz_edict['APORT1XCH28'] = self.APORT1XCH28
        zz_desc['APORT1XCH28'] = ""
        self.APORT1YCH29 = 0x0000003D
        zz_edict['APORT1YCH29'] = self.APORT1YCH29
        zz_desc['APORT1YCH29'] = ""
        self.APORT1XCH30 = 0x0000003E
        zz_edict['APORT1XCH30'] = self.APORT1XCH30
        zz_desc['APORT1XCH30'] = ""
        self.APORT1YCH31 = 0x0000003F
        zz_edict['APORT1YCH31'] = self.APORT1YCH31
        zz_desc['APORT1YCH31'] = ""
        self.APORT3XCH0 = 0x00000060
        zz_edict['APORT3XCH0'] = self.APORT3XCH0
        zz_desc['APORT3XCH0'] = ""
        self.APORT3YCH1 = 0x00000061
        zz_edict['APORT3YCH1'] = self.APORT3YCH1
        zz_desc['APORT3YCH1'] = ""
        self.APORT3XCH2 = 0x00000062
        zz_edict['APORT3XCH2'] = self.APORT3XCH2
        zz_desc['APORT3XCH2'] = ""
        self.APORT3YCH3 = 0x00000063
        zz_edict['APORT3YCH3'] = self.APORT3YCH3
        zz_desc['APORT3YCH3'] = ""
        self.APORT3XCH4 = 0x00000064
        zz_edict['APORT3XCH4'] = self.APORT3XCH4
        zz_desc['APORT3XCH4'] = ""
        self.APORT3YCH5 = 0x00000065
        zz_edict['APORT3YCH5'] = self.APORT3YCH5
        zz_desc['APORT3YCH5'] = ""
        self.APORT3XCH6 = 0x00000066
        zz_edict['APORT3XCH6'] = self.APORT3XCH6
        zz_desc['APORT3XCH6'] = ""
        self.APORT3YCH7 = 0x00000067
        zz_edict['APORT3YCH7'] = self.APORT3YCH7
        zz_desc['APORT3YCH7'] = ""
        self.APORT3XCH8 = 0x00000068
        zz_edict['APORT3XCH8'] = self.APORT3XCH8
        zz_desc['APORT3XCH8'] = ""
        self.APORT3YCH9 = 0x00000069
        zz_edict['APORT3YCH9'] = self.APORT3YCH9
        zz_desc['APORT3YCH9'] = ""
        self.APORT3XCH10 = 0x0000006A
        zz_edict['APORT3XCH10'] = self.APORT3XCH10
        zz_desc['APORT3XCH10'] = ""
        self.APORT3YCH11 = 0x0000006B
        zz_edict['APORT3YCH11'] = self.APORT3YCH11
        zz_desc['APORT3YCH11'] = ""
        self.APORT3XCH12 = 0x0000006C
        zz_edict['APORT3XCH12'] = self.APORT3XCH12
        zz_desc['APORT3XCH12'] = ""
        self.APORT3YCH13 = 0x0000006D
        zz_edict['APORT3YCH13'] = self.APORT3YCH13
        zz_desc['APORT3YCH13'] = ""
        self.APORT3XCH14 = 0x0000006E
        zz_edict['APORT3XCH14'] = self.APORT3XCH14
        zz_desc['APORT3XCH14'] = ""
        self.APORT3YCH15 = 0x0000006F
        zz_edict['APORT3YCH15'] = self.APORT3YCH15
        zz_desc['APORT3YCH15'] = ""
        self.APORT3XCH16 = 0x00000070
        zz_edict['APORT3XCH16'] = self.APORT3XCH16
        zz_desc['APORT3XCH16'] = ""
        self.APORT3YCH17 = 0x00000071
        zz_edict['APORT3YCH17'] = self.APORT3YCH17
        zz_desc['APORT3YCH17'] = ""
        self.APORT3XCH18 = 0x00000072
        zz_edict['APORT3XCH18'] = self.APORT3XCH18
        zz_desc['APORT3XCH18'] = ""
        self.APORT3YCH19 = 0x00000073
        zz_edict['APORT3YCH19'] = self.APORT3YCH19
        zz_desc['APORT3YCH19'] = ""
        self.APORT3XCH20 = 0x00000074
        zz_edict['APORT3XCH20'] = self.APORT3XCH20
        zz_desc['APORT3XCH20'] = ""
        self.APORT3YCH21 = 0x00000075
        zz_edict['APORT3YCH21'] = self.APORT3YCH21
        zz_desc['APORT3YCH21'] = ""
        self.APORT3XCH22 = 0x00000076
        zz_edict['APORT3XCH22'] = self.APORT3XCH22
        zz_desc['APORT3XCH22'] = ""
        self.APORT3YCH23 = 0x00000077
        zz_edict['APORT3YCH23'] = self.APORT3YCH23
        zz_desc['APORT3YCH23'] = ""
        self.APORT3XCH24 = 0x00000078
        zz_edict['APORT3XCH24'] = self.APORT3XCH24
        zz_desc['APORT3XCH24'] = ""
        self.APORT3YCH25 = 0x00000079
        zz_edict['APORT3YCH25'] = self.APORT3YCH25
        zz_desc['APORT3YCH25'] = ""
        self.APORT3XCH26 = 0x0000007A
        zz_edict['APORT3XCH26'] = self.APORT3XCH26
        zz_desc['APORT3XCH26'] = ""
        self.APORT3YCH27 = 0x0000007B
        zz_edict['APORT3YCH27'] = self.APORT3YCH27
        zz_desc['APORT3YCH27'] = ""
        self.APORT3XCH28 = 0x0000007C
        zz_edict['APORT3XCH28'] = self.APORT3XCH28
        zz_desc['APORT3XCH28'] = ""
        self.APORT3YCH29 = 0x0000007D
        zz_edict['APORT3YCH29'] = self.APORT3YCH29
        zz_desc['APORT3YCH29'] = ""
        self.APORT3XCH30 = 0x0000007E
        zz_edict['APORT3XCH30'] = self.APORT3XCH30
        zz_desc['APORT3XCH30'] = ""
        self.APORT3YCH31 = 0x0000007F
        zz_edict['APORT3YCH31'] = self.APORT3YCH31
        zz_desc['APORT3YCH31'] = ""
        super(RM_Enum_CSEN_SINGLECTRL_SINGLESEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_DMCFG_CRMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DM10 = 0x00000000
        zz_edict['DM10'] = self.DM10
        zz_desc['DM10'] = ""
        self.DM12 = 0x00000001
        zz_edict['DM12'] = self.DM12
        zz_desc['DM12'] = ""
        self.DM14 = 0x00000002
        zz_edict['DM14'] = self.DM14
        zz_desc['DM14'] = ""
        self.DM16 = 0x00000003
        zz_edict['DM16'] = self.DM16
        zz_desc['DM16'] = ""
        super(RM_Enum_CSEN_DMCFG_CRMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_ANACTRL_DUTYSCALE(Base_RM_Enum):
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
        super(RM_Enum_CSEN_ANACTRL_DUTYSCALE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_ANACTRL_BIASPROG(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONEX = 0x00000000
        zz_edict['ONEX'] = self.ONEX
        zz_desc['ONEX'] = ""
        self.TWOX = 0x00000001
        zz_edict['TWOX'] = self.TWOX
        zz_desc['TWOX'] = ""
        self.ONETENTH = 0x00000002
        zz_edict['ONETENTH'] = self.ONETENTH
        zz_desc['ONETENTH'] = ""
        self.HALF = 0x00000003
        zz_edict['HALF'] = self.HALF
        zz_desc['HALF'] = ""
        super(RM_Enum_CSEN_ANACTRL_BIASPROG, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CSEN_TESTCFG_VRAMP(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.RAMP0 = 0x00000000
        zz_edict['RAMP0'] = self.RAMP0
        zz_desc['RAMP0'] = ""
        self.RAMP1 = 0x00000001
        zz_edict['RAMP1'] = self.RAMP1
        zz_desc['RAMP1'] = ""
        self.RAMP2 = 0x00000002
        zz_edict['RAMP2'] = self.RAMP2
        zz_desc['RAMP2'] = ""
        self.RAMP3 = 0x00000003
        zz_edict['RAMP3'] = self.RAMP3
        zz_desc['RAMP3'] = ""
        super(RM_Enum_CSEN_TESTCFG_VRAMP, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


