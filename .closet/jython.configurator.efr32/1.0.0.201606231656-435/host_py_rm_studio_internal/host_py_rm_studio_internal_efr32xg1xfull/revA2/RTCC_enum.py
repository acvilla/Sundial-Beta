
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_RTCC_CTRL_CNTPRESC(Base_RM_Enum):
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
        self.DIV256 = 0x00000008
        zz_edict['DIV256'] = self.DIV256
        zz_desc['DIV256'] = ""
        self.DIV512 = 0x00000009
        zz_edict['DIV512'] = self.DIV512
        zz_desc['DIV512'] = ""
        self.DIV1024 = 0x0000000A
        zz_edict['DIV1024'] = self.DIV1024
        zz_desc['DIV1024'] = ""
        self.DIV2048 = 0x0000000B
        zz_edict['DIV2048'] = self.DIV2048
        zz_desc['DIV2048'] = ""
        self.DIV4096 = 0x0000000C
        zz_edict['DIV4096'] = self.DIV4096
        zz_desc['DIV4096'] = ""
        self.DIV8192 = 0x0000000D
        zz_edict['DIV8192'] = self.DIV8192
        zz_desc['DIV8192'] = ""
        self.DIV16384 = 0x0000000E
        zz_edict['DIV16384'] = self.DIV16384
        zz_desc['DIV16384'] = ""
        self.DIV32768 = 0x0000000F
        zz_edict['DIV32768'] = self.DIV32768
        zz_desc['DIV32768'] = ""
        super(RM_Enum_RTCC_CTRL_CNTPRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RTCC_LOCK_LOCKKEY(Base_RM_Enum):
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
        super(RM_Enum_RTCC_LOCK_LOCKKEY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RTCC_CC0_CTRL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.OFF = 0x00000000
        zz_edict['OFF'] = self.OFF
        zz_desc['OFF'] = ""
        self.INPUTCAPTURE = 0x00000001
        zz_edict['INPUTCAPTURE'] = self.INPUTCAPTURE
        zz_desc['INPUTCAPTURE'] = ""
        self.OUTPUTCOMPARE = 0x00000002
        zz_edict['OUTPUTCOMPARE'] = self.OUTPUTCOMPARE
        zz_desc['OUTPUTCOMPARE'] = ""
        super(RM_Enum_RTCC_CC0_CTRL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RTCC_CC0_CTRL_CMOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PULSE = 0x00000000
        zz_edict['PULSE'] = self.PULSE
        zz_desc['PULSE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_RTCC_CC0_CTRL_CMOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RTCC_CC0_CTRL_ICEDGE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.RISING = 0x00000000
        zz_edict['RISING'] = self.RISING
        zz_desc['RISING'] = ""
        self.FALLING = 0x00000001
        zz_edict['FALLING'] = self.FALLING
        zz_desc['FALLING'] = ""
        self.BOTH = 0x00000002
        zz_edict['BOTH'] = self.BOTH
        zz_desc['BOTH'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_RTCC_CC0_CTRL_ICEDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RTCC_CC0_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_RTCC_CC0_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RTCC_CC1_CTRL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.OFF = 0x00000000
        zz_edict['OFF'] = self.OFF
        zz_desc['OFF'] = ""
        self.INPUTCAPTURE = 0x00000001
        zz_edict['INPUTCAPTURE'] = self.INPUTCAPTURE
        zz_desc['INPUTCAPTURE'] = ""
        self.OUTPUTCOMPARE = 0x00000002
        zz_edict['OUTPUTCOMPARE'] = self.OUTPUTCOMPARE
        zz_desc['OUTPUTCOMPARE'] = ""
        super(RM_Enum_RTCC_CC1_CTRL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RTCC_CC1_CTRL_CMOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PULSE = 0x00000000
        zz_edict['PULSE'] = self.PULSE
        zz_desc['PULSE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_RTCC_CC1_CTRL_CMOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RTCC_CC1_CTRL_ICEDGE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.RISING = 0x00000000
        zz_edict['RISING'] = self.RISING
        zz_desc['RISING'] = ""
        self.FALLING = 0x00000001
        zz_edict['FALLING'] = self.FALLING
        zz_desc['FALLING'] = ""
        self.BOTH = 0x00000002
        zz_edict['BOTH'] = self.BOTH
        zz_desc['BOTH'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_RTCC_CC1_CTRL_ICEDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RTCC_CC1_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_RTCC_CC1_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RTCC_CC2_CTRL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.OFF = 0x00000000
        zz_edict['OFF'] = self.OFF
        zz_desc['OFF'] = ""
        self.INPUTCAPTURE = 0x00000001
        zz_edict['INPUTCAPTURE'] = self.INPUTCAPTURE
        zz_desc['INPUTCAPTURE'] = ""
        self.OUTPUTCOMPARE = 0x00000002
        zz_edict['OUTPUTCOMPARE'] = self.OUTPUTCOMPARE
        zz_desc['OUTPUTCOMPARE'] = ""
        super(RM_Enum_RTCC_CC2_CTRL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RTCC_CC2_CTRL_CMOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PULSE = 0x00000000
        zz_edict['PULSE'] = self.PULSE
        zz_desc['PULSE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_RTCC_CC2_CTRL_CMOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RTCC_CC2_CTRL_ICEDGE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.RISING = 0x00000000
        zz_edict['RISING'] = self.RISING
        zz_desc['RISING'] = ""
        self.FALLING = 0x00000001
        zz_edict['FALLING'] = self.FALLING
        zz_desc['FALLING'] = ""
        self.BOTH = 0x00000002
        zz_edict['BOTH'] = self.BOTH
        zz_desc['BOTH'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_RTCC_CC2_CTRL_ICEDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RTCC_CC2_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_RTCC_CC2_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


