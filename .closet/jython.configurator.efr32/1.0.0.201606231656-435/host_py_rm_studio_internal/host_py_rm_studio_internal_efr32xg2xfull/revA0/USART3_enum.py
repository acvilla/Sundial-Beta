
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_USART3_CTRL_OVS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.X16 = 0x00000000
        zz_edict['X16'] = self.X16
        zz_desc['X16'] = ""
        self.X8 = 0x00000001
        zz_edict['X8'] = self.X8
        zz_desc['X8'] = ""
        self.X6 = 0x00000002
        zz_edict['X6'] = self.X6
        zz_desc['X6'] = ""
        self.X4 = 0x00000003
        zz_edict['X4'] = self.X4
        zz_desc['X4'] = ""
        super(RM_Enum_USART3_CTRL_OVS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_FRAME_DATABITS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.FOUR = 0x00000001
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.FIVE = 0x00000002
        zz_edict['FIVE'] = self.FIVE
        zz_desc['FIVE'] = ""
        self.SIX = 0x00000003
        zz_edict['SIX'] = self.SIX
        zz_desc['SIX'] = ""
        self.SEVEN = 0x00000004
        zz_edict['SEVEN'] = self.SEVEN
        zz_desc['SEVEN'] = ""
        self.EIGHT = 0x00000005
        zz_edict['EIGHT'] = self.EIGHT
        zz_desc['EIGHT'] = ""
        self.NINE = 0x00000006
        zz_edict['NINE'] = self.NINE
        zz_desc['NINE'] = ""
        self.TEN = 0x00000007
        zz_edict['TEN'] = self.TEN
        zz_desc['TEN'] = ""
        self.ELEVEN = 0x00000008
        zz_edict['ELEVEN'] = self.ELEVEN
        zz_desc['ELEVEN'] = ""
        self.TWELVE = 0x00000009
        zz_edict['TWELVE'] = self.TWELVE
        zz_desc['TWELVE'] = ""
        self.THIRTEEN = 0x0000000A
        zz_edict['THIRTEEN'] = self.THIRTEEN
        zz_desc['THIRTEEN'] = ""
        self.FOURTEEN = 0x0000000B
        zz_edict['FOURTEEN'] = self.FOURTEEN
        zz_desc['FOURTEEN'] = ""
        self.FIFTEEN = 0x0000000C
        zz_edict['FIFTEEN'] = self.FIFTEEN
        zz_desc['FIFTEEN'] = ""
        self.SIXTEEN = 0x0000000D
        zz_edict['SIXTEEN'] = self.SIXTEEN
        zz_desc['SIXTEEN'] = ""
        super(RM_Enum_USART3_FRAME_DATABITS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_FRAME_PARITY(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.EVEN = 0x00000002
        zz_edict['EVEN'] = self.EVEN
        zz_desc['EVEN'] = ""
        self.ODD = 0x00000003
        zz_edict['ODD'] = self.ODD
        zz_desc['ODD'] = ""
        super(RM_Enum_USART3_FRAME_PARITY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_FRAME_STOPBITS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.HALF = 0x00000000
        zz_edict['HALF'] = self.HALF
        zz_desc['HALF'] = ""
        self.ONE = 0x00000001
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.ONEANDAHALF = 0x00000002
        zz_edict['ONEANDAHALF'] = self.ONEANDAHALF
        zz_desc['ONEANDAHALF'] = ""
        self.TWO = 0x00000003
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        super(RM_Enum_USART3_FRAME_STOPBITS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_TRIGCTRL_TSEL(Base_RM_Enum):
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
        super(RM_Enum_USART3_TRIGCTRL_TSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_IRCTRL_IRPW(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.THREE = 0x00000002
        zz_edict['THREE'] = self.THREE
        zz_desc['THREE'] = ""
        self.FOUR = 0x00000003
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        super(RM_Enum_USART3_IRCTRL_IRPW, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_IRCTRL_IRPRSSEL(Base_RM_Enum):
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
        super(RM_Enum_USART3_IRCTRL_IRPRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_INPUT_RXPRSSEL(Base_RM_Enum):
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
        super(RM_Enum_USART3_INPUT_RXPRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_INPUT_CLKPRSSEL(Base_RM_Enum):
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
        super(RM_Enum_USART3_INPUT_CLKPRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_I2SCTRL_FORMAT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.W32D32 = 0x00000000
        zz_edict['W32D32'] = self.W32D32
        zz_desc['W32D32'] = ""
        self.W32D24M = 0x00000001
        zz_edict['W32D24M'] = self.W32D24M
        zz_desc['W32D24M'] = ""
        self.W32D24 = 0x00000002
        zz_edict['W32D24'] = self.W32D24
        zz_desc['W32D24'] = ""
        self.W32D16 = 0x00000003
        zz_edict['W32D16'] = self.W32D16
        zz_desc['W32D16'] = ""
        self.W32D8 = 0x00000004
        zz_edict['W32D8'] = self.W32D8
        zz_desc['W32D8'] = ""
        self.W16D16 = 0x00000005
        zz_edict['W16D16'] = self.W16D16
        zz_desc['W16D16'] = ""
        self.W16D8 = 0x00000006
        zz_edict['W16D8'] = self.W16D8
        zz_desc['W16D8'] = ""
        self.W8D8 = 0x00000007
        zz_edict['W8D8'] = self.W8D8
        zz_desc['W8D8'] = ""
        super(RM_Enum_USART3_I2SCTRL_FORMAT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_TIMING_TXDELAY(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.ONE = 0x00000001
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000002
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.THREE = 0x00000003
        zz_edict['THREE'] = self.THREE
        zz_desc['THREE'] = ""
        self.SEVEN = 0x00000004
        zz_edict['SEVEN'] = self.SEVEN
        zz_desc['SEVEN'] = ""
        self.TCMP0 = 0x00000005
        zz_edict['TCMP0'] = self.TCMP0
        zz_desc['TCMP0'] = ""
        self.TCMP1 = 0x00000006
        zz_edict['TCMP1'] = self.TCMP1
        zz_desc['TCMP1'] = ""
        self.TCMP2 = 0x00000007
        zz_edict['TCMP2'] = self.TCMP2
        zz_desc['TCMP2'] = ""
        super(RM_Enum_USART3_TIMING_TXDELAY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_TIMING_CSSETUP(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ZERO = 0x00000000
        zz_edict['ZERO'] = self.ZERO
        zz_desc['ZERO'] = ""
        self.ONE = 0x00000001
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000002
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.THREE = 0x00000003
        zz_edict['THREE'] = self.THREE
        zz_desc['THREE'] = ""
        self.SEVEN = 0x00000004
        zz_edict['SEVEN'] = self.SEVEN
        zz_desc['SEVEN'] = ""
        self.TCMP0 = 0x00000005
        zz_edict['TCMP0'] = self.TCMP0
        zz_desc['TCMP0'] = ""
        self.TCMP1 = 0x00000006
        zz_edict['TCMP1'] = self.TCMP1
        zz_desc['TCMP1'] = ""
        self.TCMP2 = 0x00000007
        zz_edict['TCMP2'] = self.TCMP2
        zz_desc['TCMP2'] = ""
        super(RM_Enum_USART3_TIMING_CSSETUP, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_TIMING_ICS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ZERO = 0x00000000
        zz_edict['ZERO'] = self.ZERO
        zz_desc['ZERO'] = ""
        self.ONE = 0x00000001
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000002
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.THREE = 0x00000003
        zz_edict['THREE'] = self.THREE
        zz_desc['THREE'] = ""
        self.SEVEN = 0x00000004
        zz_edict['SEVEN'] = self.SEVEN
        zz_desc['SEVEN'] = ""
        self.TCMP0 = 0x00000005
        zz_edict['TCMP0'] = self.TCMP0
        zz_desc['TCMP0'] = ""
        self.TCMP1 = 0x00000006
        zz_edict['TCMP1'] = self.TCMP1
        zz_desc['TCMP1'] = ""
        self.TCMP2 = 0x00000007
        zz_edict['TCMP2'] = self.TCMP2
        zz_desc['TCMP2'] = ""
        super(RM_Enum_USART3_TIMING_ICS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_TIMING_CSHOLD(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ZERO = 0x00000000
        zz_edict['ZERO'] = self.ZERO
        zz_desc['ZERO'] = ""
        self.ONE = 0x00000001
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000002
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.THREE = 0x00000003
        zz_edict['THREE'] = self.THREE
        zz_desc['THREE'] = ""
        self.SEVEN = 0x00000004
        zz_edict['SEVEN'] = self.SEVEN
        zz_desc['SEVEN'] = ""
        self.TCMP0 = 0x00000005
        zz_edict['TCMP0'] = self.TCMP0
        zz_desc['TCMP0'] = ""
        self.TCMP1 = 0x00000006
        zz_edict['TCMP1'] = self.TCMP1
        zz_desc['TCMP1'] = ""
        self.TCMP2 = 0x00000007
        zz_edict['TCMP2'] = self.TCMP2
        zz_desc['TCMP2'] = ""
        super(RM_Enum_USART3_TIMING_CSHOLD, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_TIMECMP0_TSTART(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.TXEOF = 0x00000001
        zz_edict['TXEOF'] = self.TXEOF
        zz_desc['TXEOF'] = ""
        self.TXC = 0x00000002
        zz_edict['TXC'] = self.TXC
        zz_desc['TXC'] = ""
        self.RXACT = 0x00000003
        zz_edict['RXACT'] = self.RXACT
        zz_desc['RXACT'] = ""
        self.RXEOF = 0x00000004
        zz_edict['RXEOF'] = self.RXEOF
        zz_desc['RXEOF'] = ""
        super(RM_Enum_USART3_TIMECMP0_TSTART, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_TIMECMP0_TSTOP(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.TCMP0 = 0x00000000
        zz_edict['TCMP0'] = self.TCMP0
        zz_desc['TCMP0'] = ""
        self.TXST = 0x00000001
        zz_edict['TXST'] = self.TXST
        zz_desc['TXST'] = ""
        self.RXACT = 0x00000002
        zz_edict['RXACT'] = self.RXACT
        zz_desc['RXACT'] = ""
        self.RXACTN = 0x00000003
        zz_edict['RXACTN'] = self.RXACTN
        zz_desc['RXACTN'] = ""
        super(RM_Enum_USART3_TIMECMP0_TSTOP, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_TIMECMP1_TSTART(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.TXEOF = 0x00000001
        zz_edict['TXEOF'] = self.TXEOF
        zz_desc['TXEOF'] = ""
        self.TXC = 0x00000002
        zz_edict['TXC'] = self.TXC
        zz_desc['TXC'] = ""
        self.RXACT = 0x00000003
        zz_edict['RXACT'] = self.RXACT
        zz_desc['RXACT'] = ""
        self.RXEOF = 0x00000004
        zz_edict['RXEOF'] = self.RXEOF
        zz_desc['RXEOF'] = ""
        super(RM_Enum_USART3_TIMECMP1_TSTART, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_TIMECMP1_TSTOP(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.TCMP1 = 0x00000000
        zz_edict['TCMP1'] = self.TCMP1
        zz_desc['TCMP1'] = ""
        self.TXST = 0x00000001
        zz_edict['TXST'] = self.TXST
        zz_desc['TXST'] = ""
        self.RXACT = 0x00000002
        zz_edict['RXACT'] = self.RXACT
        zz_desc['RXACT'] = ""
        self.RXACTN = 0x00000003
        zz_edict['RXACTN'] = self.RXACTN
        zz_desc['RXACTN'] = ""
        super(RM_Enum_USART3_TIMECMP1_TSTOP, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_TIMECMP2_TSTART(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.TXEOF = 0x00000001
        zz_edict['TXEOF'] = self.TXEOF
        zz_desc['TXEOF'] = ""
        self.TXC = 0x00000002
        zz_edict['TXC'] = self.TXC
        zz_desc['TXC'] = ""
        self.RXACT = 0x00000003
        zz_edict['RXACT'] = self.RXACT
        zz_desc['RXACT'] = ""
        self.RXEOF = 0x00000004
        zz_edict['RXEOF'] = self.RXEOF
        zz_desc['RXEOF'] = ""
        super(RM_Enum_USART3_TIMECMP2_TSTART, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_TIMECMP2_TSTOP(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.TCMP2 = 0x00000000
        zz_edict['TCMP2'] = self.TCMP2
        zz_desc['TCMP2'] = ""
        self.TXST = 0x00000001
        zz_edict['TXST'] = self.TXST
        zz_desc['TXST'] = ""
        self.RXACT = 0x00000002
        zz_edict['RXACT'] = self.RXACT
        zz_desc['RXACT'] = ""
        self.RXACTN = 0x00000003
        zz_edict['RXACTN'] = self.RXACTN
        zz_desc['RXACTN'] = ""
        super(RM_Enum_USART3_TIMECMP2_TSTOP, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_ROUTELOC0_RXLOC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOC0 = 0x00000000
        zz_edict['LOC0'] = self.LOC0
        zz_desc['LOC0'] = ""
        self.LOC1 = 0x00000001
        zz_edict['LOC1'] = self.LOC1
        zz_desc['LOC1'] = ""
        self.LOC2 = 0x00000002
        zz_edict['LOC2'] = self.LOC2
        zz_desc['LOC2'] = ""
        self.LOC3 = 0x00000003
        zz_edict['LOC3'] = self.LOC3
        zz_desc['LOC3'] = ""
        self.LOC4 = 0x00000004
        zz_edict['LOC4'] = self.LOC4
        zz_desc['LOC4'] = ""
        self.LOC5 = 0x00000005
        zz_edict['LOC5'] = self.LOC5
        zz_desc['LOC5'] = ""
        self.LOC6 = 0x00000006
        zz_edict['LOC6'] = self.LOC6
        zz_desc['LOC6'] = ""
        self.LOC7 = 0x00000007
        zz_edict['LOC7'] = self.LOC7
        zz_desc['LOC7'] = ""
        self.LOC8 = 0x00000008
        zz_edict['LOC8'] = self.LOC8
        zz_desc['LOC8'] = ""
        self.LOC9 = 0x00000009
        zz_edict['LOC9'] = self.LOC9
        zz_desc['LOC9'] = ""
        self.LOC10 = 0x0000000A
        zz_edict['LOC10'] = self.LOC10
        zz_desc['LOC10'] = ""
        self.LOC11 = 0x0000000B
        zz_edict['LOC11'] = self.LOC11
        zz_desc['LOC11'] = ""
        self.LOC12 = 0x0000000C
        zz_edict['LOC12'] = self.LOC12
        zz_desc['LOC12'] = ""
        self.LOC13 = 0x0000000D
        zz_edict['LOC13'] = self.LOC13
        zz_desc['LOC13'] = ""
        self.LOC14 = 0x0000000E
        zz_edict['LOC14'] = self.LOC14
        zz_desc['LOC14'] = ""
        self.LOC15 = 0x0000000F
        zz_edict['LOC15'] = self.LOC15
        zz_desc['LOC15'] = ""
        self.LOC16 = 0x00000010
        zz_edict['LOC16'] = self.LOC16
        zz_desc['LOC16'] = ""
        self.LOC17 = 0x00000011
        zz_edict['LOC17'] = self.LOC17
        zz_desc['LOC17'] = ""
        self.LOC18 = 0x00000012
        zz_edict['LOC18'] = self.LOC18
        zz_desc['LOC18'] = ""
        self.LOC19 = 0x00000013
        zz_edict['LOC19'] = self.LOC19
        zz_desc['LOC19'] = ""
        self.LOC20 = 0x00000014
        zz_edict['LOC20'] = self.LOC20
        zz_desc['LOC20'] = ""
        self.LOC21 = 0x00000015
        zz_edict['LOC21'] = self.LOC21
        zz_desc['LOC21'] = ""
        self.LOC22 = 0x00000016
        zz_edict['LOC22'] = self.LOC22
        zz_desc['LOC22'] = ""
        self.LOC23 = 0x00000017
        zz_edict['LOC23'] = self.LOC23
        zz_desc['LOC23'] = ""
        self.LOC24 = 0x00000018
        zz_edict['LOC24'] = self.LOC24
        zz_desc['LOC24'] = ""
        self.LOC25 = 0x00000019
        zz_edict['LOC25'] = self.LOC25
        zz_desc['LOC25'] = ""
        self.LOC26 = 0x0000001A
        zz_edict['LOC26'] = self.LOC26
        zz_desc['LOC26'] = ""
        self.LOC27 = 0x0000001B
        zz_edict['LOC27'] = self.LOC27
        zz_desc['LOC27'] = ""
        self.LOC28 = 0x0000001C
        zz_edict['LOC28'] = self.LOC28
        zz_desc['LOC28'] = ""
        self.LOC29 = 0x0000001D
        zz_edict['LOC29'] = self.LOC29
        zz_desc['LOC29'] = ""
        self.LOC30 = 0x0000001E
        zz_edict['LOC30'] = self.LOC30
        zz_desc['LOC30'] = ""
        self.LOC31 = 0x0000001F
        zz_edict['LOC31'] = self.LOC31
        zz_desc['LOC31'] = ""
        super(RM_Enum_USART3_ROUTELOC0_RXLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_ROUTELOC0_TXLOC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOC0 = 0x00000000
        zz_edict['LOC0'] = self.LOC0
        zz_desc['LOC0'] = ""
        self.LOC1 = 0x00000001
        zz_edict['LOC1'] = self.LOC1
        zz_desc['LOC1'] = ""
        self.LOC2 = 0x00000002
        zz_edict['LOC2'] = self.LOC2
        zz_desc['LOC2'] = ""
        self.LOC3 = 0x00000003
        zz_edict['LOC3'] = self.LOC3
        zz_desc['LOC3'] = ""
        self.LOC4 = 0x00000004
        zz_edict['LOC4'] = self.LOC4
        zz_desc['LOC4'] = ""
        self.LOC5 = 0x00000005
        zz_edict['LOC5'] = self.LOC5
        zz_desc['LOC5'] = ""
        self.LOC6 = 0x00000006
        zz_edict['LOC6'] = self.LOC6
        zz_desc['LOC6'] = ""
        self.LOC7 = 0x00000007
        zz_edict['LOC7'] = self.LOC7
        zz_desc['LOC7'] = ""
        self.LOC8 = 0x00000008
        zz_edict['LOC8'] = self.LOC8
        zz_desc['LOC8'] = ""
        self.LOC9 = 0x00000009
        zz_edict['LOC9'] = self.LOC9
        zz_desc['LOC9'] = ""
        self.LOC10 = 0x0000000A
        zz_edict['LOC10'] = self.LOC10
        zz_desc['LOC10'] = ""
        self.LOC11 = 0x0000000B
        zz_edict['LOC11'] = self.LOC11
        zz_desc['LOC11'] = ""
        self.LOC12 = 0x0000000C
        zz_edict['LOC12'] = self.LOC12
        zz_desc['LOC12'] = ""
        self.LOC13 = 0x0000000D
        zz_edict['LOC13'] = self.LOC13
        zz_desc['LOC13'] = ""
        self.LOC14 = 0x0000000E
        zz_edict['LOC14'] = self.LOC14
        zz_desc['LOC14'] = ""
        self.LOC15 = 0x0000000F
        zz_edict['LOC15'] = self.LOC15
        zz_desc['LOC15'] = ""
        self.LOC16 = 0x00000010
        zz_edict['LOC16'] = self.LOC16
        zz_desc['LOC16'] = ""
        self.LOC17 = 0x00000011
        zz_edict['LOC17'] = self.LOC17
        zz_desc['LOC17'] = ""
        self.LOC18 = 0x00000012
        zz_edict['LOC18'] = self.LOC18
        zz_desc['LOC18'] = ""
        self.LOC19 = 0x00000013
        zz_edict['LOC19'] = self.LOC19
        zz_desc['LOC19'] = ""
        self.LOC20 = 0x00000014
        zz_edict['LOC20'] = self.LOC20
        zz_desc['LOC20'] = ""
        self.LOC21 = 0x00000015
        zz_edict['LOC21'] = self.LOC21
        zz_desc['LOC21'] = ""
        self.LOC22 = 0x00000016
        zz_edict['LOC22'] = self.LOC22
        zz_desc['LOC22'] = ""
        self.LOC23 = 0x00000017
        zz_edict['LOC23'] = self.LOC23
        zz_desc['LOC23'] = ""
        self.LOC24 = 0x00000018
        zz_edict['LOC24'] = self.LOC24
        zz_desc['LOC24'] = ""
        self.LOC25 = 0x00000019
        zz_edict['LOC25'] = self.LOC25
        zz_desc['LOC25'] = ""
        self.LOC26 = 0x0000001A
        zz_edict['LOC26'] = self.LOC26
        zz_desc['LOC26'] = ""
        self.LOC27 = 0x0000001B
        zz_edict['LOC27'] = self.LOC27
        zz_desc['LOC27'] = ""
        self.LOC28 = 0x0000001C
        zz_edict['LOC28'] = self.LOC28
        zz_desc['LOC28'] = ""
        self.LOC29 = 0x0000001D
        zz_edict['LOC29'] = self.LOC29
        zz_desc['LOC29'] = ""
        self.LOC30 = 0x0000001E
        zz_edict['LOC30'] = self.LOC30
        zz_desc['LOC30'] = ""
        self.LOC31 = 0x0000001F
        zz_edict['LOC31'] = self.LOC31
        zz_desc['LOC31'] = ""
        super(RM_Enum_USART3_ROUTELOC0_TXLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_ROUTELOC0_CSLOC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOC0 = 0x00000000
        zz_edict['LOC0'] = self.LOC0
        zz_desc['LOC0'] = ""
        self.LOC1 = 0x00000001
        zz_edict['LOC1'] = self.LOC1
        zz_desc['LOC1'] = ""
        self.LOC2 = 0x00000002
        zz_edict['LOC2'] = self.LOC2
        zz_desc['LOC2'] = ""
        self.LOC3 = 0x00000003
        zz_edict['LOC3'] = self.LOC3
        zz_desc['LOC3'] = ""
        self.LOC4 = 0x00000004
        zz_edict['LOC4'] = self.LOC4
        zz_desc['LOC4'] = ""
        self.LOC5 = 0x00000005
        zz_edict['LOC5'] = self.LOC5
        zz_desc['LOC5'] = ""
        self.LOC6 = 0x00000006
        zz_edict['LOC6'] = self.LOC6
        zz_desc['LOC6'] = ""
        self.LOC7 = 0x00000007
        zz_edict['LOC7'] = self.LOC7
        zz_desc['LOC7'] = ""
        self.LOC8 = 0x00000008
        zz_edict['LOC8'] = self.LOC8
        zz_desc['LOC8'] = ""
        self.LOC9 = 0x00000009
        zz_edict['LOC9'] = self.LOC9
        zz_desc['LOC9'] = ""
        self.LOC10 = 0x0000000A
        zz_edict['LOC10'] = self.LOC10
        zz_desc['LOC10'] = ""
        self.LOC11 = 0x0000000B
        zz_edict['LOC11'] = self.LOC11
        zz_desc['LOC11'] = ""
        self.LOC12 = 0x0000000C
        zz_edict['LOC12'] = self.LOC12
        zz_desc['LOC12'] = ""
        self.LOC13 = 0x0000000D
        zz_edict['LOC13'] = self.LOC13
        zz_desc['LOC13'] = ""
        self.LOC14 = 0x0000000E
        zz_edict['LOC14'] = self.LOC14
        zz_desc['LOC14'] = ""
        self.LOC15 = 0x0000000F
        zz_edict['LOC15'] = self.LOC15
        zz_desc['LOC15'] = ""
        self.LOC16 = 0x00000010
        zz_edict['LOC16'] = self.LOC16
        zz_desc['LOC16'] = ""
        self.LOC17 = 0x00000011
        zz_edict['LOC17'] = self.LOC17
        zz_desc['LOC17'] = ""
        self.LOC18 = 0x00000012
        zz_edict['LOC18'] = self.LOC18
        zz_desc['LOC18'] = ""
        self.LOC19 = 0x00000013
        zz_edict['LOC19'] = self.LOC19
        zz_desc['LOC19'] = ""
        self.LOC20 = 0x00000014
        zz_edict['LOC20'] = self.LOC20
        zz_desc['LOC20'] = ""
        self.LOC21 = 0x00000015
        zz_edict['LOC21'] = self.LOC21
        zz_desc['LOC21'] = ""
        self.LOC22 = 0x00000016
        zz_edict['LOC22'] = self.LOC22
        zz_desc['LOC22'] = ""
        self.LOC23 = 0x00000017
        zz_edict['LOC23'] = self.LOC23
        zz_desc['LOC23'] = ""
        self.LOC24 = 0x00000018
        zz_edict['LOC24'] = self.LOC24
        zz_desc['LOC24'] = ""
        self.LOC25 = 0x00000019
        zz_edict['LOC25'] = self.LOC25
        zz_desc['LOC25'] = ""
        self.LOC26 = 0x0000001A
        zz_edict['LOC26'] = self.LOC26
        zz_desc['LOC26'] = ""
        self.LOC27 = 0x0000001B
        zz_edict['LOC27'] = self.LOC27
        zz_desc['LOC27'] = ""
        self.LOC28 = 0x0000001C
        zz_edict['LOC28'] = self.LOC28
        zz_desc['LOC28'] = ""
        self.LOC29 = 0x0000001D
        zz_edict['LOC29'] = self.LOC29
        zz_desc['LOC29'] = ""
        self.LOC30 = 0x0000001E
        zz_edict['LOC30'] = self.LOC30
        zz_desc['LOC30'] = ""
        self.LOC31 = 0x0000001F
        zz_edict['LOC31'] = self.LOC31
        zz_desc['LOC31'] = ""
        super(RM_Enum_USART3_ROUTELOC0_CSLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_ROUTELOC0_CLKLOC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOC0 = 0x00000000
        zz_edict['LOC0'] = self.LOC0
        zz_desc['LOC0'] = ""
        self.LOC1 = 0x00000001
        zz_edict['LOC1'] = self.LOC1
        zz_desc['LOC1'] = ""
        self.LOC2 = 0x00000002
        zz_edict['LOC2'] = self.LOC2
        zz_desc['LOC2'] = ""
        self.LOC3 = 0x00000003
        zz_edict['LOC3'] = self.LOC3
        zz_desc['LOC3'] = ""
        self.LOC4 = 0x00000004
        zz_edict['LOC4'] = self.LOC4
        zz_desc['LOC4'] = ""
        self.LOC5 = 0x00000005
        zz_edict['LOC5'] = self.LOC5
        zz_desc['LOC5'] = ""
        self.LOC6 = 0x00000006
        zz_edict['LOC6'] = self.LOC6
        zz_desc['LOC6'] = ""
        self.LOC7 = 0x00000007
        zz_edict['LOC7'] = self.LOC7
        zz_desc['LOC7'] = ""
        self.LOC8 = 0x00000008
        zz_edict['LOC8'] = self.LOC8
        zz_desc['LOC8'] = ""
        self.LOC9 = 0x00000009
        zz_edict['LOC9'] = self.LOC9
        zz_desc['LOC9'] = ""
        self.LOC10 = 0x0000000A
        zz_edict['LOC10'] = self.LOC10
        zz_desc['LOC10'] = ""
        self.LOC11 = 0x0000000B
        zz_edict['LOC11'] = self.LOC11
        zz_desc['LOC11'] = ""
        self.LOC12 = 0x0000000C
        zz_edict['LOC12'] = self.LOC12
        zz_desc['LOC12'] = ""
        self.LOC13 = 0x0000000D
        zz_edict['LOC13'] = self.LOC13
        zz_desc['LOC13'] = ""
        self.LOC14 = 0x0000000E
        zz_edict['LOC14'] = self.LOC14
        zz_desc['LOC14'] = ""
        self.LOC15 = 0x0000000F
        zz_edict['LOC15'] = self.LOC15
        zz_desc['LOC15'] = ""
        self.LOC16 = 0x00000010
        zz_edict['LOC16'] = self.LOC16
        zz_desc['LOC16'] = ""
        self.LOC17 = 0x00000011
        zz_edict['LOC17'] = self.LOC17
        zz_desc['LOC17'] = ""
        self.LOC18 = 0x00000012
        zz_edict['LOC18'] = self.LOC18
        zz_desc['LOC18'] = ""
        self.LOC19 = 0x00000013
        zz_edict['LOC19'] = self.LOC19
        zz_desc['LOC19'] = ""
        self.LOC20 = 0x00000014
        zz_edict['LOC20'] = self.LOC20
        zz_desc['LOC20'] = ""
        self.LOC21 = 0x00000015
        zz_edict['LOC21'] = self.LOC21
        zz_desc['LOC21'] = ""
        self.LOC22 = 0x00000016
        zz_edict['LOC22'] = self.LOC22
        zz_desc['LOC22'] = ""
        self.LOC23 = 0x00000017
        zz_edict['LOC23'] = self.LOC23
        zz_desc['LOC23'] = ""
        self.LOC24 = 0x00000018
        zz_edict['LOC24'] = self.LOC24
        zz_desc['LOC24'] = ""
        self.LOC25 = 0x00000019
        zz_edict['LOC25'] = self.LOC25
        zz_desc['LOC25'] = ""
        self.LOC26 = 0x0000001A
        zz_edict['LOC26'] = self.LOC26
        zz_desc['LOC26'] = ""
        self.LOC27 = 0x0000001B
        zz_edict['LOC27'] = self.LOC27
        zz_desc['LOC27'] = ""
        self.LOC28 = 0x0000001C
        zz_edict['LOC28'] = self.LOC28
        zz_desc['LOC28'] = ""
        self.LOC29 = 0x0000001D
        zz_edict['LOC29'] = self.LOC29
        zz_desc['LOC29'] = ""
        self.LOC30 = 0x0000001E
        zz_edict['LOC30'] = self.LOC30
        zz_desc['LOC30'] = ""
        self.LOC31 = 0x0000001F
        zz_edict['LOC31'] = self.LOC31
        zz_desc['LOC31'] = ""
        super(RM_Enum_USART3_ROUTELOC0_CLKLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_ROUTELOC1_CTSLOC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOC0 = 0x00000000
        zz_edict['LOC0'] = self.LOC0
        zz_desc['LOC0'] = ""
        self.LOC1 = 0x00000001
        zz_edict['LOC1'] = self.LOC1
        zz_desc['LOC1'] = ""
        self.LOC2 = 0x00000002
        zz_edict['LOC2'] = self.LOC2
        zz_desc['LOC2'] = ""
        self.LOC3 = 0x00000003
        zz_edict['LOC3'] = self.LOC3
        zz_desc['LOC3'] = ""
        self.LOC4 = 0x00000004
        zz_edict['LOC4'] = self.LOC4
        zz_desc['LOC4'] = ""
        self.LOC5 = 0x00000005
        zz_edict['LOC5'] = self.LOC5
        zz_desc['LOC5'] = ""
        self.LOC6 = 0x00000006
        zz_edict['LOC6'] = self.LOC6
        zz_desc['LOC6'] = ""
        self.LOC7 = 0x00000007
        zz_edict['LOC7'] = self.LOC7
        zz_desc['LOC7'] = ""
        self.LOC8 = 0x00000008
        zz_edict['LOC8'] = self.LOC8
        zz_desc['LOC8'] = ""
        self.LOC9 = 0x00000009
        zz_edict['LOC9'] = self.LOC9
        zz_desc['LOC9'] = ""
        self.LOC10 = 0x0000000A
        zz_edict['LOC10'] = self.LOC10
        zz_desc['LOC10'] = ""
        self.LOC11 = 0x0000000B
        zz_edict['LOC11'] = self.LOC11
        zz_desc['LOC11'] = ""
        self.LOC12 = 0x0000000C
        zz_edict['LOC12'] = self.LOC12
        zz_desc['LOC12'] = ""
        self.LOC13 = 0x0000000D
        zz_edict['LOC13'] = self.LOC13
        zz_desc['LOC13'] = ""
        self.LOC14 = 0x0000000E
        zz_edict['LOC14'] = self.LOC14
        zz_desc['LOC14'] = ""
        self.LOC15 = 0x0000000F
        zz_edict['LOC15'] = self.LOC15
        zz_desc['LOC15'] = ""
        self.LOC16 = 0x00000010
        zz_edict['LOC16'] = self.LOC16
        zz_desc['LOC16'] = ""
        self.LOC17 = 0x00000011
        zz_edict['LOC17'] = self.LOC17
        zz_desc['LOC17'] = ""
        self.LOC18 = 0x00000012
        zz_edict['LOC18'] = self.LOC18
        zz_desc['LOC18'] = ""
        self.LOC19 = 0x00000013
        zz_edict['LOC19'] = self.LOC19
        zz_desc['LOC19'] = ""
        self.LOC20 = 0x00000014
        zz_edict['LOC20'] = self.LOC20
        zz_desc['LOC20'] = ""
        self.LOC21 = 0x00000015
        zz_edict['LOC21'] = self.LOC21
        zz_desc['LOC21'] = ""
        self.LOC22 = 0x00000016
        zz_edict['LOC22'] = self.LOC22
        zz_desc['LOC22'] = ""
        self.LOC23 = 0x00000017
        zz_edict['LOC23'] = self.LOC23
        zz_desc['LOC23'] = ""
        self.LOC24 = 0x00000018
        zz_edict['LOC24'] = self.LOC24
        zz_desc['LOC24'] = ""
        self.LOC25 = 0x00000019
        zz_edict['LOC25'] = self.LOC25
        zz_desc['LOC25'] = ""
        self.LOC26 = 0x0000001A
        zz_edict['LOC26'] = self.LOC26
        zz_desc['LOC26'] = ""
        self.LOC27 = 0x0000001B
        zz_edict['LOC27'] = self.LOC27
        zz_desc['LOC27'] = ""
        self.LOC28 = 0x0000001C
        zz_edict['LOC28'] = self.LOC28
        zz_desc['LOC28'] = ""
        self.LOC29 = 0x0000001D
        zz_edict['LOC29'] = self.LOC29
        zz_desc['LOC29'] = ""
        self.LOC30 = 0x0000001E
        zz_edict['LOC30'] = self.LOC30
        zz_desc['LOC30'] = ""
        self.LOC31 = 0x0000001F
        zz_edict['LOC31'] = self.LOC31
        zz_desc['LOC31'] = ""
        super(RM_Enum_USART3_ROUTELOC1_CTSLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_USART3_ROUTELOC1_RTSLOC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOC0 = 0x00000000
        zz_edict['LOC0'] = self.LOC0
        zz_desc['LOC0'] = ""
        self.LOC1 = 0x00000001
        zz_edict['LOC1'] = self.LOC1
        zz_desc['LOC1'] = ""
        self.LOC2 = 0x00000002
        zz_edict['LOC2'] = self.LOC2
        zz_desc['LOC2'] = ""
        self.LOC3 = 0x00000003
        zz_edict['LOC3'] = self.LOC3
        zz_desc['LOC3'] = ""
        self.LOC4 = 0x00000004
        zz_edict['LOC4'] = self.LOC4
        zz_desc['LOC4'] = ""
        self.LOC5 = 0x00000005
        zz_edict['LOC5'] = self.LOC5
        zz_desc['LOC5'] = ""
        self.LOC6 = 0x00000006
        zz_edict['LOC6'] = self.LOC6
        zz_desc['LOC6'] = ""
        self.LOC7 = 0x00000007
        zz_edict['LOC7'] = self.LOC7
        zz_desc['LOC7'] = ""
        self.LOC8 = 0x00000008
        zz_edict['LOC8'] = self.LOC8
        zz_desc['LOC8'] = ""
        self.LOC9 = 0x00000009
        zz_edict['LOC9'] = self.LOC9
        zz_desc['LOC9'] = ""
        self.LOC10 = 0x0000000A
        zz_edict['LOC10'] = self.LOC10
        zz_desc['LOC10'] = ""
        self.LOC11 = 0x0000000B
        zz_edict['LOC11'] = self.LOC11
        zz_desc['LOC11'] = ""
        self.LOC12 = 0x0000000C
        zz_edict['LOC12'] = self.LOC12
        zz_desc['LOC12'] = ""
        self.LOC13 = 0x0000000D
        zz_edict['LOC13'] = self.LOC13
        zz_desc['LOC13'] = ""
        self.LOC14 = 0x0000000E
        zz_edict['LOC14'] = self.LOC14
        zz_desc['LOC14'] = ""
        self.LOC15 = 0x0000000F
        zz_edict['LOC15'] = self.LOC15
        zz_desc['LOC15'] = ""
        self.LOC16 = 0x00000010
        zz_edict['LOC16'] = self.LOC16
        zz_desc['LOC16'] = ""
        self.LOC17 = 0x00000011
        zz_edict['LOC17'] = self.LOC17
        zz_desc['LOC17'] = ""
        self.LOC18 = 0x00000012
        zz_edict['LOC18'] = self.LOC18
        zz_desc['LOC18'] = ""
        self.LOC19 = 0x00000013
        zz_edict['LOC19'] = self.LOC19
        zz_desc['LOC19'] = ""
        self.LOC20 = 0x00000014
        zz_edict['LOC20'] = self.LOC20
        zz_desc['LOC20'] = ""
        self.LOC21 = 0x00000015
        zz_edict['LOC21'] = self.LOC21
        zz_desc['LOC21'] = ""
        self.LOC22 = 0x00000016
        zz_edict['LOC22'] = self.LOC22
        zz_desc['LOC22'] = ""
        self.LOC23 = 0x00000017
        zz_edict['LOC23'] = self.LOC23
        zz_desc['LOC23'] = ""
        self.LOC24 = 0x00000018
        zz_edict['LOC24'] = self.LOC24
        zz_desc['LOC24'] = ""
        self.LOC25 = 0x00000019
        zz_edict['LOC25'] = self.LOC25
        zz_desc['LOC25'] = ""
        self.LOC26 = 0x0000001A
        zz_edict['LOC26'] = self.LOC26
        zz_desc['LOC26'] = ""
        self.LOC27 = 0x0000001B
        zz_edict['LOC27'] = self.LOC27
        zz_desc['LOC27'] = ""
        self.LOC28 = 0x0000001C
        zz_edict['LOC28'] = self.LOC28
        zz_desc['LOC28'] = ""
        self.LOC29 = 0x0000001D
        zz_edict['LOC29'] = self.LOC29
        zz_desc['LOC29'] = ""
        self.LOC30 = 0x0000001E
        zz_edict['LOC30'] = self.LOC30
        zz_desc['LOC30'] = ""
        self.LOC31 = 0x0000001F
        zz_edict['LOC31'] = self.LOC31
        zz_desc['LOC31'] = ""
        super(RM_Enum_USART3_ROUTELOC1_RTSLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


