
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_TIMER1_CTRL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.UP = 0x00000000
        zz_edict['UP'] = self.UP
        zz_desc['UP'] = ""
        self.DOWN = 0x00000001
        zz_edict['DOWN'] = self.DOWN
        zz_desc['DOWN'] = ""
        self.UPDOWN = 0x00000002
        zz_edict['UPDOWN'] = self.UPDOWN
        zz_desc['UPDOWN'] = ""
        self.QDEC = 0x00000003
        zz_edict['QDEC'] = self.QDEC
        zz_desc['QDEC'] = ""
        super(RM_Enum_TIMER1_CTRL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CTRL_RISEA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.START = 0x00000001
        zz_edict['START'] = self.START
        zz_desc['START'] = ""
        self.STOP = 0x00000002
        zz_edict['STOP'] = self.STOP
        zz_desc['STOP'] = ""
        self.RELOADSTART = 0x00000003
        zz_edict['RELOADSTART'] = self.RELOADSTART
        zz_desc['RELOADSTART'] = ""
        super(RM_Enum_TIMER1_CTRL_RISEA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CTRL_FALLA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.START = 0x00000001
        zz_edict['START'] = self.START
        zz_desc['START'] = ""
        self.STOP = 0x00000002
        zz_edict['STOP'] = self.STOP
        zz_desc['STOP'] = ""
        self.RELOADSTART = 0x00000003
        zz_edict['RELOADSTART'] = self.RELOADSTART
        zz_desc['RELOADSTART'] = ""
        super(RM_Enum_TIMER1_CTRL_FALLA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CTRL_CLKSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PRESCHFPERCLK = 0x00000000
        zz_edict['PRESCHFPERCLK'] = self.PRESCHFPERCLK
        zz_desc['PRESCHFPERCLK'] = ""
        self.CC1 = 0x00000001
        zz_edict['CC1'] = self.CC1
        zz_desc['CC1'] = ""
        self.TIMEROUF = 0x00000002
        zz_edict['TIMEROUF'] = self.TIMEROUF
        zz_desc['TIMEROUF'] = ""
        super(RM_Enum_TIMER1_CTRL_CLKSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CTRL_PRESC(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_CTRL_PRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_LOCK_TIMERLOCKKEY(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_LOCK_TIMERLOCKKEY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_ROUTELOC0_CC0LOC(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_ROUTELOC0_CC0LOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_ROUTELOC0_CC1LOC(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_ROUTELOC0_CC1LOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_ROUTELOC0_CC2LOC(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_ROUTELOC0_CC2LOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_ROUTELOC0_CC3LOC(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_ROUTELOC0_CC3LOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_ROUTELOC2_CDTI0LOC(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_ROUTELOC2_CDTI0LOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_ROUTELOC2_CDTI1LOC(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_ROUTELOC2_CDTI1LOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_ROUTELOC2_CDTI2LOC(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_ROUTELOC2_CDTI2LOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC0_CTRL_MODE(Base_RM_Enum):
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
        self.PWM = 0x00000003
        zz_edict['PWM'] = self.PWM
        zz_desc['PWM'] = ""
        super(RM_Enum_TIMER1_CC0_CTRL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC0_CTRL_CMOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_TIMER1_CC0_CTRL_CMOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC0_CTRL_COFOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_TIMER1_CC0_CTRL_COFOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC0_CTRL_CUFOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_TIMER1_CC0_CTRL_CUFOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC0_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_CC0_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC0_CTRL_ICEDGE(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_CC0_CTRL_ICEDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC0_CTRL_ICEVCTRL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.EVERYEDGE = 0x00000000
        zz_edict['EVERYEDGE'] = self.EVERYEDGE
        zz_desc['EVERYEDGE'] = ""
        self.EVERYSECONDEDGE = 0x00000001
        zz_edict['EVERYSECONDEDGE'] = self.EVERYSECONDEDGE
        zz_desc['EVERYSECONDEDGE'] = ""
        self.RISING = 0x00000002
        zz_edict['RISING'] = self.RISING
        zz_desc['RISING'] = ""
        self.FALLING = 0x00000003
        zz_edict['FALLING'] = self.FALLING
        zz_desc['FALLING'] = ""
        super(RM_Enum_TIMER1_CC0_CTRL_ICEVCTRL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC1_CTRL_MODE(Base_RM_Enum):
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
        self.PWM = 0x00000003
        zz_edict['PWM'] = self.PWM
        zz_desc['PWM'] = ""
        super(RM_Enum_TIMER1_CC1_CTRL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC1_CTRL_CMOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_TIMER1_CC1_CTRL_CMOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC1_CTRL_COFOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_TIMER1_CC1_CTRL_COFOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC1_CTRL_CUFOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_TIMER1_CC1_CTRL_CUFOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC1_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_CC1_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC1_CTRL_ICEDGE(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_CC1_CTRL_ICEDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC1_CTRL_ICEVCTRL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.EVERYEDGE = 0x00000000
        zz_edict['EVERYEDGE'] = self.EVERYEDGE
        zz_desc['EVERYEDGE'] = ""
        self.EVERYSECONDEDGE = 0x00000001
        zz_edict['EVERYSECONDEDGE'] = self.EVERYSECONDEDGE
        zz_desc['EVERYSECONDEDGE'] = ""
        self.RISING = 0x00000002
        zz_edict['RISING'] = self.RISING
        zz_desc['RISING'] = ""
        self.FALLING = 0x00000003
        zz_edict['FALLING'] = self.FALLING
        zz_desc['FALLING'] = ""
        super(RM_Enum_TIMER1_CC1_CTRL_ICEVCTRL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC2_CTRL_MODE(Base_RM_Enum):
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
        self.PWM = 0x00000003
        zz_edict['PWM'] = self.PWM
        zz_desc['PWM'] = ""
        super(RM_Enum_TIMER1_CC2_CTRL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC2_CTRL_CMOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_TIMER1_CC2_CTRL_CMOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC2_CTRL_COFOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_TIMER1_CC2_CTRL_COFOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC2_CTRL_CUFOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_TIMER1_CC2_CTRL_CUFOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC2_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_CC2_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC2_CTRL_ICEDGE(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_CC2_CTRL_ICEDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC2_CTRL_ICEVCTRL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.EVERYEDGE = 0x00000000
        zz_edict['EVERYEDGE'] = self.EVERYEDGE
        zz_desc['EVERYEDGE'] = ""
        self.EVERYSECONDEDGE = 0x00000001
        zz_edict['EVERYSECONDEDGE'] = self.EVERYSECONDEDGE
        zz_desc['EVERYSECONDEDGE'] = ""
        self.RISING = 0x00000002
        zz_edict['RISING'] = self.RISING
        zz_desc['RISING'] = ""
        self.FALLING = 0x00000003
        zz_edict['FALLING'] = self.FALLING
        zz_desc['FALLING'] = ""
        super(RM_Enum_TIMER1_CC2_CTRL_ICEVCTRL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC3_CTRL_MODE(Base_RM_Enum):
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
        self.PWM = 0x00000003
        zz_edict['PWM'] = self.PWM
        zz_desc['PWM'] = ""
        super(RM_Enum_TIMER1_CC3_CTRL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC3_CTRL_CMOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_TIMER1_CC3_CTRL_CMOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC3_CTRL_COFOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_TIMER1_CC3_CTRL_COFOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC3_CTRL_CUFOA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.TOGGLE = 0x00000001
        zz_edict['TOGGLE'] = self.TOGGLE
        zz_desc['TOGGLE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.SET = 0x00000003
        zz_edict['SET'] = self.SET
        zz_desc['SET'] = ""
        super(RM_Enum_TIMER1_CC3_CTRL_CUFOA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC3_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_CC3_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC3_CTRL_ICEDGE(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_CC3_CTRL_ICEDGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_CC3_CTRL_ICEVCTRL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.EVERYEDGE = 0x00000000
        zz_edict['EVERYEDGE'] = self.EVERYEDGE
        zz_desc['EVERYEDGE'] = ""
        self.EVERYSECONDEDGE = 0x00000001
        zz_edict['EVERYSECONDEDGE'] = self.EVERYSECONDEDGE
        zz_desc['EVERYSECONDEDGE'] = ""
        self.RISING = 0x00000002
        zz_edict['RISING'] = self.RISING
        zz_desc['RISING'] = ""
        self.FALLING = 0x00000003
        zz_edict['FALLING'] = self.FALLING
        zz_desc['FALLING'] = ""
        super(RM_Enum_TIMER1_CC3_CTRL_ICEVCTRL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_DTCTRL_DTPRSSEL(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_DTCTRL_DTPRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_DTTIME_DTPRESC(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_DTTIME_DTPRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_DTFC_DTPRS0FSEL(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_DTFC_DTPRS0FSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_DTFC_DTPRS1FSEL(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_DTFC_DTPRS1FSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_DTFC_DTFA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.INACTIVE = 0x00000001
        zz_edict['INACTIVE'] = self.INACTIVE
        zz_desc['INACTIVE'] = ""
        self.CLEAR = 0x00000002
        zz_edict['CLEAR'] = self.CLEAR
        zz_desc['CLEAR'] = ""
        self.TRISTATE = 0x00000003
        zz_edict['TRISTATE'] = self.TRISTATE
        zz_desc['TRISTATE'] = ""
        super(RM_Enum_TIMER1_DTFC_DTFA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_TIMER1_DTLOCK_LOCKKEY(Base_RM_Enum):
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
        super(RM_Enum_TIMER1_DTLOCK_LOCKKEY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


