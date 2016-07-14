
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_PROTIMER_CTRL_PRECNTSRC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.CLOCK = 0x00000001
        zz_edict['CLOCK'] = self.CLOCK
        zz_desc['CLOCK'] = ""
        self.UNUSED = 0x00000003
        zz_edict['UNUSED'] = self.UNUSED
        zz_desc['UNUSED'] = ""
        super(RM_Enum_PROTIMER_CTRL_PRECNTSRC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CTRL_BASECNTSRC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.PRECNTOF = 0x00000001
        zz_edict['PRECNTOF'] = self.PRECNTOF
        zz_desc['PRECNTOF'] = ""
        self.UNUSED = 0x00000003
        zz_edict['UNUSED'] = self.UNUSED
        zz_desc['UNUSED'] = ""
        super(RM_Enum_PROTIMER_CTRL_BASECNTSRC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CTRL_WRAPCNTSRC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.PRECNTOF = 0x00000001
        zz_edict['PRECNTOF'] = self.PRECNTOF
        zz_desc['PRECNTOF'] = ""
        self.BASECNTOF = 0x00000002
        zz_edict['BASECNTOF'] = self.BASECNTOF
        zz_desc['BASECNTOF'] = ""
        self.UNUSED = 0x00000003
        zz_edict['UNUSED'] = self.UNUSED
        zz_desc['UNUSED'] = ""
        super(RM_Enum_PROTIMER_CTRL_WRAPCNTSRC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CTRL_TOUT0SRC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.PRECNTOF = 0x00000001
        zz_edict['PRECNTOF'] = self.PRECNTOF
        zz_desc['PRECNTOF'] = ""
        self.BASECNTOF = 0x00000002
        zz_edict['BASECNTOF'] = self.BASECNTOF
        zz_desc['BASECNTOF'] = ""
        self.WRAPCNTOF = 0x00000003
        zz_edict['WRAPCNTOF'] = self.WRAPCNTOF
        zz_desc['WRAPCNTOF'] = ""
        super(RM_Enum_PROTIMER_CTRL_TOUT0SRC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CTRL_TOUT0SYNCSRC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.PRECNTOF = 0x00000001
        zz_edict['PRECNTOF'] = self.PRECNTOF
        zz_desc['PRECNTOF'] = ""
        self.BASECNTOF = 0x00000002
        zz_edict['BASECNTOF'] = self.BASECNTOF
        zz_desc['BASECNTOF'] = ""
        self.WRAPCNTOF = 0x00000003
        zz_edict['WRAPCNTOF'] = self.WRAPCNTOF
        zz_desc['WRAPCNTOF'] = ""
        super(RM_Enum_PROTIMER_CTRL_TOUT0SYNCSRC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CTRL_TOUT1SRC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.PRECNTOF = 0x00000001
        zz_edict['PRECNTOF'] = self.PRECNTOF
        zz_desc['PRECNTOF'] = ""
        self.BASECNTOF = 0x00000002
        zz_edict['BASECNTOF'] = self.BASECNTOF
        zz_desc['BASECNTOF'] = ""
        self.WRAPCNTOF = 0x00000003
        zz_edict['WRAPCNTOF'] = self.WRAPCNTOF
        zz_desc['WRAPCNTOF'] = ""
        super(RM_Enum_PROTIMER_CTRL_TOUT1SRC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CTRL_TOUT1SYNCSRC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.PRECNTOF = 0x00000001
        zz_edict['PRECNTOF'] = self.PRECNTOF
        zz_desc['PRECNTOF'] = ""
        self.BASECNTOF = 0x00000002
        zz_edict['BASECNTOF'] = self.BASECNTOF
        zz_desc['BASECNTOF'] = ""
        self.WRAPCNTOF = 0x00000003
        zz_edict['WRAPCNTOF'] = self.WRAPCNTOF
        zz_desc['WRAPCNTOF'] = ""
        super(RM_Enum_PROTIMER_CTRL_TOUT1SYNCSRC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_PRSCTRL_STARTEDGE(Base_RM_Enum):
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
        self.DISABLED = 0x00000003
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        super(RM_Enum_PROTIMER_PRSCTRL_STARTEDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_PRSCTRL_STARTPRSSEL(Base_RM_Enum):
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
        super(RM_Enum_PROTIMER_PRSCTRL_STARTPRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_PRSCTRL_STOPEDGE(Base_RM_Enum):
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
        self.DISABLED = 0x00000003
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        super(RM_Enum_PROTIMER_PRSCTRL_STOPEDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_PRSCTRL_STOPPRSSEL(Base_RM_Enum):
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
        super(RM_Enum_PROTIMER_PRSCTRL_STOPPRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_PRSCTRL_RTCCTRIGGEREDGE(Base_RM_Enum):
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
        self.DISABLED = 0x00000003
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        super(RM_Enum_PROTIMER_PRSCTRL_RTCCTRIGGEREDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_PRSCTRL_RTCCTRIGGERPRSSEL(Base_RM_Enum):
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
        super(RM_Enum_PROTIMER_PRSCTRL_RTCCTRIGGERPRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_LBTCTRL_STARTEXP(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.EXP0 = 0x00000000
        zz_edict['EXP0'] = self.EXP0
        zz_desc['EXP0'] = ""
        self.EXP1 = 0x00000001
        zz_edict['EXP1'] = self.EXP1
        zz_desc['EXP1'] = ""
        self.EXP2 = 0x00000002
        zz_edict['EXP2'] = self.EXP2
        zz_desc['EXP2'] = ""
        self.EXP3 = 0x00000003
        zz_edict['EXP3'] = self.EXP3
        zz_desc['EXP3'] = ""
        self.EXP4 = 0x00000004
        zz_edict['EXP4'] = self.EXP4
        zz_desc['EXP4'] = ""
        self.EXP5 = 0x00000005
        zz_edict['EXP5'] = self.EXP5
        zz_desc['EXP5'] = ""
        self.EXP6 = 0x00000006
        zz_edict['EXP6'] = self.EXP6
        zz_desc['EXP6'] = ""
        self.EXP7 = 0x00000007
        zz_edict['EXP7'] = self.EXP7
        zz_desc['EXP7'] = ""
        self.EXP8 = 0x00000008
        zz_edict['EXP8'] = self.EXP8
        zz_desc['EXP8'] = ""
        super(RM_Enum_PROTIMER_LBTCTRL_STARTEXP, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_LBTCTRL_MAXEXP(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.EXP0 = 0x00000000
        zz_edict['EXP0'] = self.EXP0
        zz_desc['EXP0'] = ""
        self.EXP1 = 0x00000001
        zz_edict['EXP1'] = self.EXP1
        zz_desc['EXP1'] = ""
        self.EXP2 = 0x00000002
        zz_edict['EXP2'] = self.EXP2
        zz_desc['EXP2'] = ""
        self.EXP3 = 0x00000003
        zz_edict['EXP3'] = self.EXP3
        zz_desc['EXP3'] = ""
        self.EXP4 = 0x00000004
        zz_edict['EXP4'] = self.EXP4
        zz_desc['EXP4'] = ""
        self.EXP5 = 0x00000005
        zz_edict['EXP5'] = self.EXP5
        zz_desc['EXP5'] = ""
        self.EXP6 = 0x00000006
        zz_edict['EXP6'] = self.EXP6
        zz_desc['EXP6'] = ""
        self.EXP7 = 0x00000007
        zz_edict['EXP7'] = self.EXP7
        zz_desc['EXP7'] = ""
        self.EXP8 = 0x00000008
        zz_edict['EXP8'] = self.EXP8
        zz_desc['EXP8'] = ""
        super(RM_Enum_PROTIMER_LBTCTRL_MAXEXP, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_LBTPRSCTRL_LBTSTARTPRSSEL(Base_RM_Enum):
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
        super(RM_Enum_PROTIMER_LBTPRSCTRL_LBTSTARTPRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_LBTPRSCTRL_LBTPAUSEPRSSEL(Base_RM_Enum):
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
        super(RM_Enum_PROTIMER_LBTPRSCTRL_LBTPAUSEPRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_LBTPRSCTRL_LBTSTOPPRSSEL(Base_RM_Enum):
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
        super(RM_Enum_PROTIMER_LBTPRSCTRL_LBTSTOPPRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_RXCTRL_RXSETEVENT1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.ALWAYS = 0x00000001
        zz_edict['ALWAYS'] = self.ALWAYS
        zz_desc['ALWAYS'] = ""
        self.PRECNTOF = 0x00000002
        zz_edict['PRECNTOF'] = self.PRECNTOF
        zz_desc['PRECNTOF'] = ""
        self.BASECNTOF = 0x00000003
        zz_edict['BASECNTOF'] = self.BASECNTOF
        zz_desc['BASECNTOF'] = ""
        self.WRAPCNTOF = 0x00000004
        zz_edict['WRAPCNTOF'] = self.WRAPCNTOF
        zz_desc['WRAPCNTOF'] = ""
        self.TOUT0UF = 0x00000005
        zz_edict['TOUT0UF'] = self.TOUT0UF
        zz_desc['TOUT0UF'] = ""
        self.TOUT1UF = 0x00000006
        zz_edict['TOUT1UF'] = self.TOUT1UF
        zz_desc['TOUT1UF'] = ""
        self.TOUT0MATCH = 0x00000007
        zz_edict['TOUT0MATCH'] = self.TOUT0MATCH
        zz_desc['TOUT0MATCH'] = ""
        self.TOUT1MATCH = 0x00000008
        zz_edict['TOUT1MATCH'] = self.TOUT1MATCH
        zz_desc['TOUT1MATCH'] = ""
        self.CC0 = 0x00000009
        zz_edict['CC0'] = self.CC0
        zz_desc['CC0'] = ""
        self.CC1 = 0x0000000A
        zz_edict['CC1'] = self.CC1
        zz_desc['CC1'] = ""
        self.CC2 = 0x0000000B
        zz_edict['CC2'] = self.CC2
        zz_desc['CC2'] = ""
        self.CC3 = 0x0000000C
        zz_edict['CC3'] = self.CC3
        zz_desc['CC3'] = ""
        self.CC4 = 0x0000000D
        zz_edict['CC4'] = self.CC4
        zz_desc['CC4'] = ""
        self.TXDONE = 0x0000000E
        zz_edict['TXDONE'] = self.TXDONE
        zz_desc['TXDONE'] = ""
        self.RXDONE = 0x0000000F
        zz_edict['RXDONE'] = self.RXDONE
        zz_desc['RXDONE'] = ""
        self.TXORRXDONE = 0x00000010
        zz_edict['TXORRXDONE'] = self.TXORRXDONE
        zz_desc['TXORRXDONE'] = ""
        self.FDET0 = 0x00000011
        zz_edict['FDET0'] = self.FDET0
        zz_desc['FDET0'] = ""
        self.FDET1 = 0x00000012
        zz_edict['FDET1'] = self.FDET1
        zz_desc['FDET1'] = ""
        self.FDET0OR1 = 0x00000013
        zz_edict['FDET0OR1'] = self.FDET0OR1
        zz_desc['FDET0OR1'] = ""
        self.LBTSUCCESS = 0x00000014
        zz_edict['LBTSUCCESS'] = self.LBTSUCCESS
        zz_desc['LBTSUCCESS'] = ""
        self.LBTRETRY = 0x00000015
        zz_edict['LBTRETRY'] = self.LBTRETRY
        zz_desc['LBTRETRY'] = ""
        self.LBTFAILURE = 0x00000016
        zz_edict['LBTFAILURE'] = self.LBTFAILURE
        zz_desc['LBTFAILURE'] = ""
        self.ANYLBT = 0x00000017
        zz_edict['ANYLBT'] = self.ANYLBT
        zz_desc['ANYLBT'] = ""
        self.CCAACK = 0x00000018
        zz_edict['CCAACK'] = self.CCAACK
        zz_desc['CCAACK'] = ""
        self.CCA = 0x00000019
        zz_edict['CCA'] = self.CCA
        zz_desc['CCA'] = ""
        self.NOTCCA = 0x0000001A
        zz_edict['NOTCCA'] = self.NOTCCA
        zz_desc['NOTCCA'] = ""
        self.TOUT0MATCHLBT = 0x0000001B
        zz_edict['TOUT0MATCHLBT'] = self.TOUT0MATCHLBT
        zz_desc['TOUT0MATCHLBT'] = ""
        super(RM_Enum_PROTIMER_RXCTRL_RXSETEVENT1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_TXCTRL_TXSETEVENT1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.ALWAYS = 0x00000001
        zz_edict['ALWAYS'] = self.ALWAYS
        zz_desc['ALWAYS'] = ""
        self.PRECNTOF = 0x00000002
        zz_edict['PRECNTOF'] = self.PRECNTOF
        zz_desc['PRECNTOF'] = ""
        self.BASECNTOF = 0x00000003
        zz_edict['BASECNTOF'] = self.BASECNTOF
        zz_desc['BASECNTOF'] = ""
        self.WRAPCNTOF = 0x00000004
        zz_edict['WRAPCNTOF'] = self.WRAPCNTOF
        zz_desc['WRAPCNTOF'] = ""
        self.TOUT0UF = 0x00000005
        zz_edict['TOUT0UF'] = self.TOUT0UF
        zz_desc['TOUT0UF'] = ""
        self.TOUT1UF = 0x00000006
        zz_edict['TOUT1UF'] = self.TOUT1UF
        zz_desc['TOUT1UF'] = ""
        self.TOUT0MATCH = 0x00000007
        zz_edict['TOUT0MATCH'] = self.TOUT0MATCH
        zz_desc['TOUT0MATCH'] = ""
        self.TOUT1MATCH = 0x00000008
        zz_edict['TOUT1MATCH'] = self.TOUT1MATCH
        zz_desc['TOUT1MATCH'] = ""
        self.CC0 = 0x00000009
        zz_edict['CC0'] = self.CC0
        zz_desc['CC0'] = ""
        self.CC1 = 0x0000000A
        zz_edict['CC1'] = self.CC1
        zz_desc['CC1'] = ""
        self.CC2 = 0x0000000B
        zz_edict['CC2'] = self.CC2
        zz_desc['CC2'] = ""
        self.CC3 = 0x0000000C
        zz_edict['CC3'] = self.CC3
        zz_desc['CC3'] = ""
        self.CC4 = 0x0000000D
        zz_edict['CC4'] = self.CC4
        zz_desc['CC4'] = ""
        self.TXDONE = 0x0000000E
        zz_edict['TXDONE'] = self.TXDONE
        zz_desc['TXDONE'] = ""
        self.RXDONE = 0x0000000F
        zz_edict['RXDONE'] = self.RXDONE
        zz_desc['RXDONE'] = ""
        self.TXORRXDONE = 0x00000010
        zz_edict['TXORRXDONE'] = self.TXORRXDONE
        zz_desc['TXORRXDONE'] = ""
        self.FDET0 = 0x00000011
        zz_edict['FDET0'] = self.FDET0
        zz_desc['FDET0'] = ""
        self.FDET1 = 0x00000012
        zz_edict['FDET1'] = self.FDET1
        zz_desc['FDET1'] = ""
        self.FDET0OR1 = 0x00000013
        zz_edict['FDET0OR1'] = self.FDET0OR1
        zz_desc['FDET0OR1'] = ""
        self.LBTSUCCESS = 0x00000014
        zz_edict['LBTSUCCESS'] = self.LBTSUCCESS
        zz_desc['LBTSUCCESS'] = ""
        self.LBTRETRY = 0x00000015
        zz_edict['LBTRETRY'] = self.LBTRETRY
        zz_desc['LBTRETRY'] = ""
        self.LBTFAILURE = 0x00000016
        zz_edict['LBTFAILURE'] = self.LBTFAILURE
        zz_desc['LBTFAILURE'] = ""
        self.ANYLBT = 0x00000017
        zz_edict['ANYLBT'] = self.ANYLBT
        zz_desc['ANYLBT'] = ""
        self.CCAACK = 0x00000018
        zz_edict['CCAACK'] = self.CCAACK
        zz_desc['CCAACK'] = ""
        self.CCA = 0x00000019
        zz_edict['CCA'] = self.CCA
        zz_desc['CCA'] = ""
        self.NOTCCA = 0x0000001A
        zz_edict['NOTCCA'] = self.NOTCCA
        zz_desc['NOTCCA'] = ""
        self.TOUT0MATCHLBT = 0x0000001B
        zz_edict['TOUT0MATCHLBT'] = self.TOUT0MATCHLBT
        zz_desc['TOUT0MATCHLBT'] = ""
        super(RM_Enum_PROTIMER_TXCTRL_TXSETEVENT1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC0_CTRL_MOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_PROTIMER_CC0_CTRL_MOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC0_CTRL_OFOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_PROTIMER_CC0_CTRL_OFOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC0_CTRL_OFSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PRECNT = 0x00000000
        zz_edict['PRECNT'] = self.PRECNT
        zz_desc['PRECNT'] = ""
        self.BASECNT = 0x00000001
        zz_edict['BASECNT'] = self.BASECNT
        zz_desc['BASECNT'] = ""
        self.WRAPCNT = 0x00000002
        zz_edict['WRAPCNT'] = self.WRAPCNT
        zz_desc['WRAPCNT'] = ""
        self.DISABLED = 0x00000003
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        super(RM_Enum_PROTIMER_CC0_CTRL_OFSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC0_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_PROTIMER_CC0_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC0_CTRL_INSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PRS = 0x00000000
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.TXDONE = 0x00000001
        zz_edict['TXDONE'] = self.TXDONE
        zz_desc['TXDONE'] = ""
        self.RXDONE = 0x00000002
        zz_edict['RXDONE'] = self.RXDONE
        zz_desc['RXDONE'] = ""
        self.TXORRXDONE = 0x00000003
        zz_edict['TXORRXDONE'] = self.TXORRXDONE
        zz_desc['TXORRXDONE'] = ""
        self.FRAMEDET0 = 0x00000004
        zz_edict['FRAMEDET0'] = self.FRAMEDET0
        zz_desc['FRAMEDET0'] = ""
        self.FRAMEDET1 = 0x00000005
        zz_edict['FRAMEDET1'] = self.FRAMEDET1
        zz_desc['FRAMEDET1'] = ""
        self.FDET0OR1 = 0x00000006
        zz_edict['FDET0OR1'] = self.FDET0OR1
        zz_desc['FDET0OR1'] = ""
        super(RM_Enum_PROTIMER_CC0_CTRL_INSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC0_CTRL_ICEDGE(Base_RM_Enum):
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
        self.DISABLED = 0x00000003
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        super(RM_Enum_PROTIMER_CC0_CTRL_ICEDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC1_CTRL_MOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_PROTIMER_CC1_CTRL_MOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC1_CTRL_OFOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_PROTIMER_CC1_CTRL_OFOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC1_CTRL_OFSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PRECNT = 0x00000000
        zz_edict['PRECNT'] = self.PRECNT
        zz_desc['PRECNT'] = ""
        self.BASECNT = 0x00000001
        zz_edict['BASECNT'] = self.BASECNT
        zz_desc['BASECNT'] = ""
        self.WRAPCNT = 0x00000002
        zz_edict['WRAPCNT'] = self.WRAPCNT
        zz_desc['WRAPCNT'] = ""
        self.DISABLED = 0x00000003
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        super(RM_Enum_PROTIMER_CC1_CTRL_OFSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC1_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_PROTIMER_CC1_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC1_CTRL_INSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PRS = 0x00000000
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.TXDONE = 0x00000001
        zz_edict['TXDONE'] = self.TXDONE
        zz_desc['TXDONE'] = ""
        self.RXDONE = 0x00000002
        zz_edict['RXDONE'] = self.RXDONE
        zz_desc['RXDONE'] = ""
        self.TXORRXDONE = 0x00000003
        zz_edict['TXORRXDONE'] = self.TXORRXDONE
        zz_desc['TXORRXDONE'] = ""
        self.FRAMEDET0 = 0x00000004
        zz_edict['FRAMEDET0'] = self.FRAMEDET0
        zz_desc['FRAMEDET0'] = ""
        self.FRAMEDET1 = 0x00000005
        zz_edict['FRAMEDET1'] = self.FRAMEDET1
        zz_desc['FRAMEDET1'] = ""
        self.FDET0OR1 = 0x00000006
        zz_edict['FDET0OR1'] = self.FDET0OR1
        zz_desc['FDET0OR1'] = ""
        super(RM_Enum_PROTIMER_CC1_CTRL_INSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC1_CTRL_ICEDGE(Base_RM_Enum):
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
        self.DISABLED = 0x00000003
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        super(RM_Enum_PROTIMER_CC1_CTRL_ICEDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC2_CTRL_MOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_PROTIMER_CC2_CTRL_MOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC2_CTRL_OFOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_PROTIMER_CC2_CTRL_OFOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC2_CTRL_OFSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PRECNT = 0x00000000
        zz_edict['PRECNT'] = self.PRECNT
        zz_desc['PRECNT'] = ""
        self.BASECNT = 0x00000001
        zz_edict['BASECNT'] = self.BASECNT
        zz_desc['BASECNT'] = ""
        self.WRAPCNT = 0x00000002
        zz_edict['WRAPCNT'] = self.WRAPCNT
        zz_desc['WRAPCNT'] = ""
        self.DISABLED = 0x00000003
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        super(RM_Enum_PROTIMER_CC2_CTRL_OFSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC2_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_PROTIMER_CC2_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC2_CTRL_INSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PRS = 0x00000000
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.TXDONE = 0x00000001
        zz_edict['TXDONE'] = self.TXDONE
        zz_desc['TXDONE'] = ""
        self.RXDONE = 0x00000002
        zz_edict['RXDONE'] = self.RXDONE
        zz_desc['RXDONE'] = ""
        self.TXORRXDONE = 0x00000003
        zz_edict['TXORRXDONE'] = self.TXORRXDONE
        zz_desc['TXORRXDONE'] = ""
        self.FRAMEDET0 = 0x00000004
        zz_edict['FRAMEDET0'] = self.FRAMEDET0
        zz_desc['FRAMEDET0'] = ""
        self.FRAMEDET1 = 0x00000005
        zz_edict['FRAMEDET1'] = self.FRAMEDET1
        zz_desc['FRAMEDET1'] = ""
        self.FDET0OR1 = 0x00000006
        zz_edict['FDET0OR1'] = self.FDET0OR1
        zz_desc['FDET0OR1'] = ""
        super(RM_Enum_PROTIMER_CC2_CTRL_INSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC2_CTRL_ICEDGE(Base_RM_Enum):
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
        self.DISABLED = 0x00000003
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        super(RM_Enum_PROTIMER_CC2_CTRL_ICEDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC3_CTRL_MOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_PROTIMER_CC3_CTRL_MOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC3_CTRL_OFOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_PROTIMER_CC3_CTRL_OFOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC3_CTRL_OFSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PRECNT = 0x00000000
        zz_edict['PRECNT'] = self.PRECNT
        zz_desc['PRECNT'] = ""
        self.BASECNT = 0x00000001
        zz_edict['BASECNT'] = self.BASECNT
        zz_desc['BASECNT'] = ""
        self.WRAPCNT = 0x00000002
        zz_edict['WRAPCNT'] = self.WRAPCNT
        zz_desc['WRAPCNT'] = ""
        self.DISABLED = 0x00000003
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        super(RM_Enum_PROTIMER_CC3_CTRL_OFSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC3_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_PROTIMER_CC3_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC3_CTRL_INSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PRS = 0x00000000
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.TXDONE = 0x00000001
        zz_edict['TXDONE'] = self.TXDONE
        zz_desc['TXDONE'] = ""
        self.RXDONE = 0x00000002
        zz_edict['RXDONE'] = self.RXDONE
        zz_desc['RXDONE'] = ""
        self.TXORRXDONE = 0x00000003
        zz_edict['TXORRXDONE'] = self.TXORRXDONE
        zz_desc['TXORRXDONE'] = ""
        self.FRAMEDET0 = 0x00000004
        zz_edict['FRAMEDET0'] = self.FRAMEDET0
        zz_desc['FRAMEDET0'] = ""
        self.FRAMEDET1 = 0x00000005
        zz_edict['FRAMEDET1'] = self.FRAMEDET1
        zz_desc['FRAMEDET1'] = ""
        self.FDET0OR1 = 0x00000006
        zz_edict['FDET0OR1'] = self.FDET0OR1
        zz_desc['FDET0OR1'] = ""
        super(RM_Enum_PROTIMER_CC3_CTRL_INSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC3_CTRL_ICEDGE(Base_RM_Enum):
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
        self.DISABLED = 0x00000003
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        super(RM_Enum_PROTIMER_CC3_CTRL_ICEDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC4_CTRL_MOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_PROTIMER_CC4_CTRL_MOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC4_CTRL_OFOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_PROTIMER_CC4_CTRL_OFOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC4_CTRL_OFSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PRECNT = 0x00000000
        zz_edict['PRECNT'] = self.PRECNT
        zz_desc['PRECNT'] = ""
        self.BASECNT = 0x00000001
        zz_edict['BASECNT'] = self.BASECNT
        zz_desc['BASECNT'] = ""
        self.WRAPCNT = 0x00000002
        zz_edict['WRAPCNT'] = self.WRAPCNT
        zz_desc['WRAPCNT'] = ""
        self.DISABLED = 0x00000003
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        super(RM_Enum_PROTIMER_CC4_CTRL_OFSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC4_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_PROTIMER_CC4_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC4_CTRL_INSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PRS = 0x00000000
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.TXDONE = 0x00000001
        zz_edict['TXDONE'] = self.TXDONE
        zz_desc['TXDONE'] = ""
        self.RXDONE = 0x00000002
        zz_edict['RXDONE'] = self.RXDONE
        zz_desc['RXDONE'] = ""
        self.TXORRXDONE = 0x00000003
        zz_edict['TXORRXDONE'] = self.TXORRXDONE
        zz_desc['TXORRXDONE'] = ""
        self.FRAMEDET0 = 0x00000004
        zz_edict['FRAMEDET0'] = self.FRAMEDET0
        zz_desc['FRAMEDET0'] = ""
        self.FRAMEDET1 = 0x00000005
        zz_edict['FRAMEDET1'] = self.FRAMEDET1
        zz_desc['FRAMEDET1'] = ""
        self.FDET0OR1 = 0x00000006
        zz_edict['FDET0OR1'] = self.FDET0OR1
        zz_desc['FDET0OR1'] = ""
        super(RM_Enum_PROTIMER_CC4_CTRL_INSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_PROTIMER_CC4_CTRL_ICEDGE(Base_RM_Enum):
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
        self.DISABLED = 0x00000003
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        super(RM_Enum_PROTIMER_CC4_CTRL_ICEDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


