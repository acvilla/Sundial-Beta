
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_FRC_DFLCTRL_DFLMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.SINGLEBYTE = 0x00000001
        zz_edict['SINGLEBYTE'] = self.SINGLEBYTE
        zz_desc['SINGLEBYTE'] = ""
        self.SINGLEBYTEMSB = 0x00000002
        zz_edict['SINGLEBYTEMSB'] = self.SINGLEBYTEMSB
        zz_desc['SINGLEBYTEMSB'] = ""
        self.DUALBYTELSBFIRST = 0x00000003
        zz_edict['DUALBYTELSBFIRST'] = self.DUALBYTELSBFIRST
        zz_desc['DUALBYTELSBFIRST'] = ""
        self.DUALBYTEMSBFIRST = 0x00000004
        zz_edict['DUALBYTEMSBFIRST'] = self.DUALBYTEMSBFIRST
        zz_desc['DUALBYTEMSBFIRST'] = ""
        self.INFINITE = 0x00000005
        zz_edict['INFINITE'] = self.INFINITE
        zz_desc['INFINITE'] = ""
        self.BLOCKERROR = 0x00000006
        zz_edict['BLOCKERROR'] = self.BLOCKERROR
        zz_desc['BLOCKERROR'] = ""
        super(RM_Enum_FRC_DFLCTRL_DFLMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_WHITECTRL_FEEDBACKSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BIT0 = 0x00000000
        zz_edict['BIT0'] = self.BIT0
        zz_desc['BIT0'] = ""
        self.BIT1 = 0x00000001
        zz_edict['BIT1'] = self.BIT1
        zz_desc['BIT1'] = ""
        self.BIT2 = 0x00000002
        zz_edict['BIT2'] = self.BIT2
        zz_desc['BIT2'] = ""
        self.BIT3 = 0x00000003
        zz_edict['BIT3'] = self.BIT3
        zz_desc['BIT3'] = ""
        self.BIT4 = 0x00000004
        zz_edict['BIT4'] = self.BIT4
        zz_desc['BIT4'] = ""
        self.BIT5 = 0x00000005
        zz_edict['BIT5'] = self.BIT5
        zz_desc['BIT5'] = ""
        self.BIT6 = 0x00000006
        zz_edict['BIT6'] = self.BIT6
        zz_desc['BIT6'] = ""
        self.BIT7 = 0x00000007
        zz_edict['BIT7'] = self.BIT7
        zz_desc['BIT7'] = ""
        self.BIT8 = 0x00000008
        zz_edict['BIT8'] = self.BIT8
        zz_desc['BIT8'] = ""
        self.BIT9 = 0x00000009
        zz_edict['BIT9'] = self.BIT9
        zz_desc['BIT9'] = ""
        self.BIT10 = 0x0000000A
        zz_edict['BIT10'] = self.BIT10
        zz_desc['BIT10'] = ""
        self.BIT11 = 0x0000000B
        zz_edict['BIT11'] = self.BIT11
        zz_desc['BIT11'] = ""
        self.BIT12 = 0x0000000C
        zz_edict['BIT12'] = self.BIT12
        zz_desc['BIT12'] = ""
        self.BIT13 = 0x0000000D
        zz_edict['BIT13'] = self.BIT13
        zz_desc['BIT13'] = ""
        self.BIT14 = 0x0000000E
        zz_edict['BIT14'] = self.BIT14
        zz_desc['BIT14'] = ""
        self.BIT15 = 0x0000000F
        zz_edict['BIT15'] = self.BIT15
        zz_desc['BIT15'] = ""
        self.INPUT = 0x00000010
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.ZERO = 0x00000011
        zz_edict['ZERO'] = self.ZERO
        zz_desc['ZERO'] = ""
        self.ONE = 0x00000012
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TXLASTWORD = 0x00000013
        zz_edict['TXLASTWORD'] = self.TXLASTWORD
        zz_desc['TXLASTWORD'] = ""
        super(RM_Enum_FRC_WHITECTRL_FEEDBACKSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_WHITECTRL_XORFEEDBACK(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIRECT = 0x00000000
        zz_edict['DIRECT'] = self.DIRECT
        zz_desc['DIRECT'] = ""
        self.XOR = 0x00000001
        zz_edict['XOR'] = self.XOR
        zz_desc['XOR'] = ""
        self.ZERO = 0x00000002
        zz_edict['ZERO'] = self.ZERO
        zz_desc['ZERO'] = ""
        super(RM_Enum_FRC_WHITECTRL_XORFEEDBACK, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_FECCTRL_BLOCKWHITEMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIRECT = 0x00000000
        zz_edict['DIRECT'] = self.DIRECT
        zz_desc['DIRECT'] = ""
        self.WHITE = 0x00000001
        zz_edict['WHITE'] = self.WHITE
        zz_desc['WHITE'] = ""
        self.BYTEWHITE = 0x00000002
        zz_edict['BYTEWHITE'] = self.BYTEWHITE
        zz_desc['BYTEWHITE'] = ""
        self.INTERLEAVEDWHITE0 = 0x00000003
        zz_edict['INTERLEAVEDWHITE0'] = self.INTERLEAVEDWHITE0
        zz_desc['INTERLEAVEDWHITE0'] = ""
        self.INTERLEAVEDWHITE1 = 0x00000004
        zz_edict['INTERLEAVEDWHITE1'] = self.INTERLEAVEDWHITE1
        zz_desc['INTERLEAVEDWHITE1'] = ""
        self.BLOCKCODEINSERT = 0x00000005
        zz_edict['BLOCKCODEINSERT'] = self.BLOCKCODEINSERT
        zz_desc['BLOCKCODEINSERT'] = ""
        self.BLOCKCODEREPLACE = 0x00000006
        zz_edict['BLOCKCODEREPLACE'] = self.BLOCKCODEREPLACE
        zz_desc['BLOCKCODEREPLACE'] = ""
        self.BLOCKLOOKUP = 0x00000007
        zz_edict['BLOCKLOOKUP'] = self.BLOCKLOOKUP
        zz_desc['BLOCKLOOKUP'] = ""
        super(RM_Enum_FRC_FECCTRL_BLOCKWHITEMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_FECCTRL_CONVMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.CONVOLUTIONAL = 0x00000001
        zz_edict['CONVOLUTIONAL'] = self.CONVOLUTIONAL
        zz_desc['CONVOLUTIONAL'] = ""
        self.REPEAT = 0x00000002
        zz_edict['REPEAT'] = self.REPEAT
        zz_desc['REPEAT'] = ""
        super(RM_Enum_FRC_FECCTRL_CONVMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_FECCTRL_INTERLEAVEMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.ENABLE = 0x00000001
        zz_edict['ENABLE'] = self.ENABLE
        zz_desc['ENABLE'] = ""
        self.RXBUFFER = 0x00000002
        zz_edict['RXBUFFER'] = self.RXBUFFER
        zz_desc['RXBUFFER'] = ""
        self.RXTXBUFFER = 0x00000003
        zz_edict['RXTXBUFFER'] = self.RXTXBUFFER
        zz_desc['RXTXBUFFER'] = ""
        super(RM_Enum_FRC_FECCTRL_INTERLEAVEMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_CTRL_TXFCDMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.FCDMODE0 = 0x00000000
        zz_edict['FCDMODE0'] = self.FCDMODE0
        zz_desc['FCDMODE0'] = ""
        self.FCDMODE1 = 0x00000001
        zz_edict['FCDMODE1'] = self.FCDMODE1
        zz_desc['FCDMODE1'] = ""
        self.FCDMODE2 = 0x00000002
        zz_edict['FCDMODE2'] = self.FCDMODE2
        zz_desc['FCDMODE2'] = ""
        self.FCDMODE3 = 0x00000003
        zz_edict['FCDMODE3'] = self.FCDMODE3
        zz_desc['FCDMODE3'] = ""
        super(RM_Enum_FRC_CTRL_TXFCDMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_CTRL_RXFCDMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.FCDMODE0 = 0x00000000
        zz_edict['FCDMODE0'] = self.FCDMODE0
        zz_desc['FCDMODE0'] = ""
        self.FCDMODE1 = 0x00000001
        zz_edict['FCDMODE1'] = self.FCDMODE1
        zz_desc['FCDMODE1'] = ""
        self.FCDMODE2 = 0x00000002
        zz_edict['FCDMODE2'] = self.FCDMODE2
        zz_desc['FCDMODE2'] = ""
        self.FCDMODE3 = 0x00000003
        zz_edict['FCDMODE3'] = self.FCDMODE3
        zz_desc['FCDMODE3'] = ""
        super(RM_Enum_FRC_CTRL_RXFCDMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_BUFFERMODE_RXBUFFERMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BUFC = 0x00000000
        zz_edict['BUFC'] = self.BUFC
        zz_desc['BUFC'] = ""
        self.REGISTER = 0x00000001
        zz_edict['REGISTER'] = self.REGISTER
        zz_desc['REGISTER'] = ""
        self.DISABLE = 0x00000002
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        super(RM_Enum_FRC_BUFFERMODE_RXBUFFERMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_ROUTELOC0_DOUTLOC(Base_RM_Enum):
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
        super(RM_Enum_FRC_ROUTELOC0_DOUTLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_ROUTELOC0_DCLKLOC(Base_RM_Enum):
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
        super(RM_Enum_FRC_ROUTELOC0_DCLKLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_ROUTELOC0_DFRAMELOC(Base_RM_Enum):
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
        super(RM_Enum_FRC_ROUTELOC0_DFRAMELOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_SNIFFCTRL_SNIFFMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.OFF = 0x00000000
        zz_edict['OFF'] = self.OFF
        zz_desc['OFF'] = ""
        self.UART = 0x00000001
        zz_edict['UART'] = self.UART
        zz_desc['UART'] = ""
        self.SPI = 0x00000002
        zz_edict['SPI'] = self.SPI
        zz_desc['SPI'] = ""
        super(RM_Enum_FRC_SNIFFCTRL_SNIFFMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_RAWCTRL_TXRAWMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.SINGLEBUFFER = 0x00000001
        zz_edict['SINGLEBUFFER'] = self.SINGLEBUFFER
        zz_desc['SINGLEBUFFER'] = ""
        self.REPEATBUFFER = 0x00000002
        zz_edict['REPEATBUFFER'] = self.REPEATBUFFER
        zz_desc['REPEATBUFFER'] = ""
        super(RM_Enum_FRC_RAWCTRL_TXRAWMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_RAWCTRL_RXRAWMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.SINGLEITEM = 0x00000001
        zz_edict['SINGLEITEM'] = self.SINGLEITEM
        zz_desc['SINGLEITEM'] = ""
        self.SINGLEBUFFER = 0x00000002
        zz_edict['SINGLEBUFFER'] = self.SINGLEBUFFER
        zz_desc['SINGLEBUFFER'] = ""
        self.SINGLEBUFFERFRAME = 0x00000003
        zz_edict['SINGLEBUFFERFRAME'] = self.SINGLEBUFFERFRAME
        zz_desc['SINGLEBUFFERFRAME'] = ""
        self.REPEATBUFFER = 0x00000004
        zz_edict['REPEATBUFFER'] = self.REPEATBUFFER
        zz_desc['REPEATBUFFER'] = ""
        self.LVDS = 0x00000005
        zz_edict['LVDS'] = self.LVDS
        zz_desc['LVDS'] = ""
        super(RM_Enum_FRC_RAWCTRL_RXRAWMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_FRC_RAWCTRL_RXRAWPRSSEL(Base_RM_Enum):
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
        super(RM_Enum_FRC_RAWCTRL_RXRAWPRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


