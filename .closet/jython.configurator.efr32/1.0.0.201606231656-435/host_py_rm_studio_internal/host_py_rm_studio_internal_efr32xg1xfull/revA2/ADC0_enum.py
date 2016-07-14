
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


class RM_Enum_ADC0_CTRL_CHCONIDLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISCONNECT = 0x00000000
        zz_edict['DISCONNECT'] = self.DISCONNECT
        zz_desc['DISCONNECT'] = ""
        self.KEEPPREV = 0x00000001
        zz_edict['KEEPPREV'] = self.KEEPPREV
        zz_desc['KEEPPREV'] = ""
        self.PREFSINGLE = 0x00000002
        zz_edict['PREFSINGLE'] = self.PREFSINGLE
        zz_desc['PREFSINGLE'] = ""
        self.PREFSCAN = 0x00000003
        zz_edict['PREFSCAN'] = self.PREFSCAN
        zz_desc['PREFSCAN'] = ""
        super(RM_Enum_ADC0_CTRL_CHCONIDLE, self).__init__(
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
        #print("WARNING: Aliasing enum '5VDIFF' to 'E5VDIFF'")
        self.E5VDIFF = 0x00000003
        zz_edict['E5VDIFF'] = self.E5VDIFF
        zz_desc['E5VDIFF'] = ""
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


class RM_Enum_ADC0_SINGLECTRL_POSSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BUS0XCH0 = 0x00000000
        zz_edict['BUS0XCH0'] = self.BUS0XCH0
        zz_desc['BUS0XCH0'] = ""
        self.BUS0XCH1 = 0x00000001
        zz_edict['BUS0XCH1'] = self.BUS0XCH1
        zz_desc['BUS0XCH1'] = ""
        self.BUS0XCH2 = 0x00000002
        zz_edict['BUS0XCH2'] = self.BUS0XCH2
        zz_desc['BUS0XCH2'] = ""
        self.BUS0XCH3 = 0x00000003
        zz_edict['BUS0XCH3'] = self.BUS0XCH3
        zz_desc['BUS0XCH3'] = ""
        self.BUS0XCH4 = 0x00000004
        zz_edict['BUS0XCH4'] = self.BUS0XCH4
        zz_desc['BUS0XCH4'] = ""
        self.BUS0XCH5 = 0x00000005
        zz_edict['BUS0XCH5'] = self.BUS0XCH5
        zz_desc['BUS0XCH5'] = ""
        self.BUS0XCH6 = 0x00000006
        zz_edict['BUS0XCH6'] = self.BUS0XCH6
        zz_desc['BUS0XCH6'] = ""
        self.BUS0XCH7 = 0x00000007
        zz_edict['BUS0XCH7'] = self.BUS0XCH7
        zz_desc['BUS0XCH7'] = ""
        self.BUS0XCH8 = 0x00000008
        zz_edict['BUS0XCH8'] = self.BUS0XCH8
        zz_desc['BUS0XCH8'] = ""
        self.BUS0XCH9 = 0x00000009
        zz_edict['BUS0XCH9'] = self.BUS0XCH9
        zz_desc['BUS0XCH9'] = ""
        self.BUS0XCH10 = 0x0000000A
        zz_edict['BUS0XCH10'] = self.BUS0XCH10
        zz_desc['BUS0XCH10'] = ""
        self.BUS0XCH11 = 0x0000000B
        zz_edict['BUS0XCH11'] = self.BUS0XCH11
        zz_desc['BUS0XCH11'] = ""
        self.BUS0XCH12 = 0x0000000C
        zz_edict['BUS0XCH12'] = self.BUS0XCH12
        zz_desc['BUS0XCH12'] = ""
        self.BUS0XCH13 = 0x0000000D
        zz_edict['BUS0XCH13'] = self.BUS0XCH13
        zz_desc['BUS0XCH13'] = ""
        self.BUS0XCH14 = 0x0000000E
        zz_edict['BUS0XCH14'] = self.BUS0XCH14
        zz_desc['BUS0XCH14'] = ""
        self.BUS0XCH15 = 0x0000000F
        zz_edict['BUS0XCH15'] = self.BUS0XCH15
        zz_desc['BUS0XCH15'] = ""
        self.BUS0YCH0 = 0x00000010
        zz_edict['BUS0YCH0'] = self.BUS0YCH0
        zz_desc['BUS0YCH0'] = ""
        self.BUS0YCH1 = 0x00000011
        zz_edict['BUS0YCH1'] = self.BUS0YCH1
        zz_desc['BUS0YCH1'] = ""
        self.BUS0YCH2 = 0x00000012
        zz_edict['BUS0YCH2'] = self.BUS0YCH2
        zz_desc['BUS0YCH2'] = ""
        self.BUS0YCH3 = 0x00000013
        zz_edict['BUS0YCH3'] = self.BUS0YCH3
        zz_desc['BUS0YCH3'] = ""
        self.BUS0YCH4 = 0x00000014
        zz_edict['BUS0YCH4'] = self.BUS0YCH4
        zz_desc['BUS0YCH4'] = ""
        self.BUS0YCH5 = 0x00000015
        zz_edict['BUS0YCH5'] = self.BUS0YCH5
        zz_desc['BUS0YCH5'] = ""
        self.BUS0YCH6 = 0x00000016
        zz_edict['BUS0YCH6'] = self.BUS0YCH6
        zz_desc['BUS0YCH6'] = ""
        self.BUS0YCH7 = 0x00000017
        zz_edict['BUS0YCH7'] = self.BUS0YCH7
        zz_desc['BUS0YCH7'] = ""
        self.BUS0YCH8 = 0x00000018
        zz_edict['BUS0YCH8'] = self.BUS0YCH8
        zz_desc['BUS0YCH8'] = ""
        self.BUS0YCH9 = 0x00000019
        zz_edict['BUS0YCH9'] = self.BUS0YCH9
        zz_desc['BUS0YCH9'] = ""
        self.BUS0YCH10 = 0x0000001A
        zz_edict['BUS0YCH10'] = self.BUS0YCH10
        zz_desc['BUS0YCH10'] = ""
        self.BUS0YCH11 = 0x0000001B
        zz_edict['BUS0YCH11'] = self.BUS0YCH11
        zz_desc['BUS0YCH11'] = ""
        self.BUS0YCH12 = 0x0000001C
        zz_edict['BUS0YCH12'] = self.BUS0YCH12
        zz_desc['BUS0YCH12'] = ""
        self.BUS0YCH13 = 0x0000001D
        zz_edict['BUS0YCH13'] = self.BUS0YCH13
        zz_desc['BUS0YCH13'] = ""
        self.BUS0YCH14 = 0x0000001E
        zz_edict['BUS0YCH14'] = self.BUS0YCH14
        zz_desc['BUS0YCH14'] = ""
        self.BUS0YCH15 = 0x0000001F
        zz_edict['BUS0YCH15'] = self.BUS0YCH15
        zz_desc['BUS0YCH15'] = ""
        self.BUS1XCH0 = 0x00000020
        zz_edict['BUS1XCH0'] = self.BUS1XCH0
        zz_desc['BUS1XCH0'] = ""
        self.BUS1YCH1 = 0x00000021
        zz_edict['BUS1YCH1'] = self.BUS1YCH1
        zz_desc['BUS1YCH1'] = ""
        self.BUS1XCH2 = 0x00000022
        zz_edict['BUS1XCH2'] = self.BUS1XCH2
        zz_desc['BUS1XCH2'] = ""
        self.BUS1YCH3 = 0x00000023
        zz_edict['BUS1YCH3'] = self.BUS1YCH3
        zz_desc['BUS1YCH3'] = ""
        self.BUS1XCH4 = 0x00000024
        zz_edict['BUS1XCH4'] = self.BUS1XCH4
        zz_desc['BUS1XCH4'] = ""
        self.BUS1YCH5 = 0x00000025
        zz_edict['BUS1YCH5'] = self.BUS1YCH5
        zz_desc['BUS1YCH5'] = ""
        self.BUS1XCH6 = 0x00000026
        zz_edict['BUS1XCH6'] = self.BUS1XCH6
        zz_desc['BUS1XCH6'] = ""
        self.BUS1YCH7 = 0x00000027
        zz_edict['BUS1YCH7'] = self.BUS1YCH7
        zz_desc['BUS1YCH7'] = ""
        self.BUS1XCH8 = 0x00000028
        zz_edict['BUS1XCH8'] = self.BUS1XCH8
        zz_desc['BUS1XCH8'] = ""
        self.BUS1YCH9 = 0x00000029
        zz_edict['BUS1YCH9'] = self.BUS1YCH9
        zz_desc['BUS1YCH9'] = ""
        self.BUS1XCH10 = 0x0000002A
        zz_edict['BUS1XCH10'] = self.BUS1XCH10
        zz_desc['BUS1XCH10'] = ""
        self.BUS1YCH11 = 0x0000002B
        zz_edict['BUS1YCH11'] = self.BUS1YCH11
        zz_desc['BUS1YCH11'] = ""
        self.BUS1XCH12 = 0x0000002C
        zz_edict['BUS1XCH12'] = self.BUS1XCH12
        zz_desc['BUS1XCH12'] = ""
        self.BUS1YCH13 = 0x0000002D
        zz_edict['BUS1YCH13'] = self.BUS1YCH13
        zz_desc['BUS1YCH13'] = ""
        self.BUS1XCH14 = 0x0000002E
        zz_edict['BUS1XCH14'] = self.BUS1XCH14
        zz_desc['BUS1XCH14'] = ""
        self.BUS1YCH15 = 0x0000002F
        zz_edict['BUS1YCH15'] = self.BUS1YCH15
        zz_desc['BUS1YCH15'] = ""
        self.BUS1XCH16 = 0x00000030
        zz_edict['BUS1XCH16'] = self.BUS1XCH16
        zz_desc['BUS1XCH16'] = ""
        self.BUS1YCH17 = 0x00000031
        zz_edict['BUS1YCH17'] = self.BUS1YCH17
        zz_desc['BUS1YCH17'] = ""
        self.BUS1XCH18 = 0x00000032
        zz_edict['BUS1XCH18'] = self.BUS1XCH18
        zz_desc['BUS1XCH18'] = ""
        self.BUS1YCH19 = 0x00000033
        zz_edict['BUS1YCH19'] = self.BUS1YCH19
        zz_desc['BUS1YCH19'] = ""
        self.BUS1XCH20 = 0x00000034
        zz_edict['BUS1XCH20'] = self.BUS1XCH20
        zz_desc['BUS1XCH20'] = ""
        self.BUS1YCH21 = 0x00000035
        zz_edict['BUS1YCH21'] = self.BUS1YCH21
        zz_desc['BUS1YCH21'] = ""
        self.BUS1XCH22 = 0x00000036
        zz_edict['BUS1XCH22'] = self.BUS1XCH22
        zz_desc['BUS1XCH22'] = ""
        self.BUS1YCH23 = 0x00000037
        zz_edict['BUS1YCH23'] = self.BUS1YCH23
        zz_desc['BUS1YCH23'] = ""
        self.BUS1XCH24 = 0x00000038
        zz_edict['BUS1XCH24'] = self.BUS1XCH24
        zz_desc['BUS1XCH24'] = ""
        self.BUS1YCH25 = 0x00000039
        zz_edict['BUS1YCH25'] = self.BUS1YCH25
        zz_desc['BUS1YCH25'] = ""
        self.BUS1XCH26 = 0x0000003A
        zz_edict['BUS1XCH26'] = self.BUS1XCH26
        zz_desc['BUS1XCH26'] = ""
        self.BUS1YCH27 = 0x0000003B
        zz_edict['BUS1YCH27'] = self.BUS1YCH27
        zz_desc['BUS1YCH27'] = ""
        self.BUS1XCH28 = 0x0000003C
        zz_edict['BUS1XCH28'] = self.BUS1XCH28
        zz_desc['BUS1XCH28'] = ""
        self.BUS1YCH29 = 0x0000003D
        zz_edict['BUS1YCH29'] = self.BUS1YCH29
        zz_desc['BUS1YCH29'] = ""
        self.BUS1XCH30 = 0x0000003E
        zz_edict['BUS1XCH30'] = self.BUS1XCH30
        zz_desc['BUS1XCH30'] = ""
        self.BUS1YCH31 = 0x0000003F
        zz_edict['BUS1YCH31'] = self.BUS1YCH31
        zz_desc['BUS1YCH31'] = ""
        self.BUS2YCH0 = 0x00000040
        zz_edict['BUS2YCH0'] = self.BUS2YCH0
        zz_desc['BUS2YCH0'] = ""
        self.BUS2XCH1 = 0x00000041
        zz_edict['BUS2XCH1'] = self.BUS2XCH1
        zz_desc['BUS2XCH1'] = ""
        self.BUS2YCH2 = 0x00000042
        zz_edict['BUS2YCH2'] = self.BUS2YCH2
        zz_desc['BUS2YCH2'] = ""
        self.BUS2XCH3 = 0x00000043
        zz_edict['BUS2XCH3'] = self.BUS2XCH3
        zz_desc['BUS2XCH3'] = ""
        self.BUS2YCH4 = 0x00000044
        zz_edict['BUS2YCH4'] = self.BUS2YCH4
        zz_desc['BUS2YCH4'] = ""
        self.BUS2XCH5 = 0x00000045
        zz_edict['BUS2XCH5'] = self.BUS2XCH5
        zz_desc['BUS2XCH5'] = ""
        self.BUS2YCH6 = 0x00000046
        zz_edict['BUS2YCH6'] = self.BUS2YCH6
        zz_desc['BUS2YCH6'] = ""
        self.BUS2XCH7 = 0x00000047
        zz_edict['BUS2XCH7'] = self.BUS2XCH7
        zz_desc['BUS2XCH7'] = ""
        self.BUS2YCH8 = 0x00000048
        zz_edict['BUS2YCH8'] = self.BUS2YCH8
        zz_desc['BUS2YCH8'] = ""
        self.BUS2XCH9 = 0x00000049
        zz_edict['BUS2XCH9'] = self.BUS2XCH9
        zz_desc['BUS2XCH9'] = ""
        self.BUS2YCH10 = 0x0000004A
        zz_edict['BUS2YCH10'] = self.BUS2YCH10
        zz_desc['BUS2YCH10'] = ""
        self.BUS2XCH11 = 0x0000004B
        zz_edict['BUS2XCH11'] = self.BUS2XCH11
        zz_desc['BUS2XCH11'] = ""
        self.BUS2YCH12 = 0x0000004C
        zz_edict['BUS2YCH12'] = self.BUS2YCH12
        zz_desc['BUS2YCH12'] = ""
        self.BUS2XCH13 = 0x0000004D
        zz_edict['BUS2XCH13'] = self.BUS2XCH13
        zz_desc['BUS2XCH13'] = ""
        self.BUS2YCH14 = 0x0000004E
        zz_edict['BUS2YCH14'] = self.BUS2YCH14
        zz_desc['BUS2YCH14'] = ""
        self.BUS2XCH15 = 0x0000004F
        zz_edict['BUS2XCH15'] = self.BUS2XCH15
        zz_desc['BUS2XCH15'] = ""
        self.BUS2YCH16 = 0x00000050
        zz_edict['BUS2YCH16'] = self.BUS2YCH16
        zz_desc['BUS2YCH16'] = ""
        self.BUS2XCH17 = 0x00000051
        zz_edict['BUS2XCH17'] = self.BUS2XCH17
        zz_desc['BUS2XCH17'] = ""
        self.BUS2YCH18 = 0x00000052
        zz_edict['BUS2YCH18'] = self.BUS2YCH18
        zz_desc['BUS2YCH18'] = ""
        self.BUS2XCH19 = 0x00000053
        zz_edict['BUS2XCH19'] = self.BUS2XCH19
        zz_desc['BUS2XCH19'] = ""
        self.BUS2YCH20 = 0x00000054
        zz_edict['BUS2YCH20'] = self.BUS2YCH20
        zz_desc['BUS2YCH20'] = ""
        self.BUS2XCH21 = 0x00000055
        zz_edict['BUS2XCH21'] = self.BUS2XCH21
        zz_desc['BUS2XCH21'] = ""
        self.BUS2YCH22 = 0x00000056
        zz_edict['BUS2YCH22'] = self.BUS2YCH22
        zz_desc['BUS2YCH22'] = ""
        self.BUS2XCH23 = 0x00000057
        zz_edict['BUS2XCH23'] = self.BUS2XCH23
        zz_desc['BUS2XCH23'] = ""
        self.BUS2YCH24 = 0x00000058
        zz_edict['BUS2YCH24'] = self.BUS2YCH24
        zz_desc['BUS2YCH24'] = ""
        self.BUS2XCH25 = 0x00000059
        zz_edict['BUS2XCH25'] = self.BUS2XCH25
        zz_desc['BUS2XCH25'] = ""
        self.BUS2YCH26 = 0x0000005A
        zz_edict['BUS2YCH26'] = self.BUS2YCH26
        zz_desc['BUS2YCH26'] = ""
        self.BUS2XCH27 = 0x0000005B
        zz_edict['BUS2XCH27'] = self.BUS2XCH27
        zz_desc['BUS2XCH27'] = ""
        self.BUS2YCH28 = 0x0000005C
        zz_edict['BUS2YCH28'] = self.BUS2YCH28
        zz_desc['BUS2YCH28'] = ""
        self.BUS2XCH29 = 0x0000005D
        zz_edict['BUS2XCH29'] = self.BUS2XCH29
        zz_desc['BUS2XCH29'] = ""
        self.BUS2YCH30 = 0x0000005E
        zz_edict['BUS2YCH30'] = self.BUS2YCH30
        zz_desc['BUS2YCH30'] = ""
        self.BUS2XCH31 = 0x0000005F
        zz_edict['BUS2XCH31'] = self.BUS2XCH31
        zz_desc['BUS2XCH31'] = ""
        self.BUS3XCH0 = 0x00000060
        zz_edict['BUS3XCH0'] = self.BUS3XCH0
        zz_desc['BUS3XCH0'] = ""
        self.BUS3YCH1 = 0x00000061
        zz_edict['BUS3YCH1'] = self.BUS3YCH1
        zz_desc['BUS3YCH1'] = ""
        self.BUS3XCH2 = 0x00000062
        zz_edict['BUS3XCH2'] = self.BUS3XCH2
        zz_desc['BUS3XCH2'] = ""
        self.BUS3YCH3 = 0x00000063
        zz_edict['BUS3YCH3'] = self.BUS3YCH3
        zz_desc['BUS3YCH3'] = ""
        self.BUS3XCH4 = 0x00000064
        zz_edict['BUS3XCH4'] = self.BUS3XCH4
        zz_desc['BUS3XCH4'] = ""
        self.BUS3YCH5 = 0x00000065
        zz_edict['BUS3YCH5'] = self.BUS3YCH5
        zz_desc['BUS3YCH5'] = ""
        self.BUS3XCH6 = 0x00000066
        zz_edict['BUS3XCH6'] = self.BUS3XCH6
        zz_desc['BUS3XCH6'] = ""
        self.BUS3YCH7 = 0x00000067
        zz_edict['BUS3YCH7'] = self.BUS3YCH7
        zz_desc['BUS3YCH7'] = ""
        self.BUS3XCH8 = 0x00000068
        zz_edict['BUS3XCH8'] = self.BUS3XCH8
        zz_desc['BUS3XCH8'] = ""
        self.BUS3YCH9 = 0x00000069
        zz_edict['BUS3YCH9'] = self.BUS3YCH9
        zz_desc['BUS3YCH9'] = ""
        self.BUS3XCH10 = 0x0000006A
        zz_edict['BUS3XCH10'] = self.BUS3XCH10
        zz_desc['BUS3XCH10'] = ""
        self.BUS3YCH11 = 0x0000006B
        zz_edict['BUS3YCH11'] = self.BUS3YCH11
        zz_desc['BUS3YCH11'] = ""
        self.BUS3XCH12 = 0x0000006C
        zz_edict['BUS3XCH12'] = self.BUS3XCH12
        zz_desc['BUS3XCH12'] = ""
        self.BUS3YCH13 = 0x0000006D
        zz_edict['BUS3YCH13'] = self.BUS3YCH13
        zz_desc['BUS3YCH13'] = ""
        self.BUS3XCH14 = 0x0000006E
        zz_edict['BUS3XCH14'] = self.BUS3XCH14
        zz_desc['BUS3XCH14'] = ""
        self.BUS3YCH15 = 0x0000006F
        zz_edict['BUS3YCH15'] = self.BUS3YCH15
        zz_desc['BUS3YCH15'] = ""
        self.BUS3XCH16 = 0x00000070
        zz_edict['BUS3XCH16'] = self.BUS3XCH16
        zz_desc['BUS3XCH16'] = ""
        self.BUS3YCH17 = 0x00000071
        zz_edict['BUS3YCH17'] = self.BUS3YCH17
        zz_desc['BUS3YCH17'] = ""
        self.BUS3XCH18 = 0x00000072
        zz_edict['BUS3XCH18'] = self.BUS3XCH18
        zz_desc['BUS3XCH18'] = ""
        self.BUS3YCH19 = 0x00000073
        zz_edict['BUS3YCH19'] = self.BUS3YCH19
        zz_desc['BUS3YCH19'] = ""
        self.BUS3XCH20 = 0x00000074
        zz_edict['BUS3XCH20'] = self.BUS3XCH20
        zz_desc['BUS3XCH20'] = ""
        self.BUS3YCH21 = 0x00000075
        zz_edict['BUS3YCH21'] = self.BUS3YCH21
        zz_desc['BUS3YCH21'] = ""
        self.BUS3XCH22 = 0x00000076
        zz_edict['BUS3XCH22'] = self.BUS3XCH22
        zz_desc['BUS3XCH22'] = ""
        self.BUS3YCH23 = 0x00000077
        zz_edict['BUS3YCH23'] = self.BUS3YCH23
        zz_desc['BUS3YCH23'] = ""
        self.BUS3XCH24 = 0x00000078
        zz_edict['BUS3XCH24'] = self.BUS3XCH24
        zz_desc['BUS3XCH24'] = ""
        self.BUS3YCH25 = 0x00000079
        zz_edict['BUS3YCH25'] = self.BUS3YCH25
        zz_desc['BUS3YCH25'] = ""
        self.BUS3XCH26 = 0x0000007A
        zz_edict['BUS3XCH26'] = self.BUS3XCH26
        zz_desc['BUS3XCH26'] = ""
        self.BUS3YCH27 = 0x0000007B
        zz_edict['BUS3YCH27'] = self.BUS3YCH27
        zz_desc['BUS3YCH27'] = ""
        self.BUS3XCH28 = 0x0000007C
        zz_edict['BUS3XCH28'] = self.BUS3XCH28
        zz_desc['BUS3XCH28'] = ""
        self.BUS3YCH29 = 0x0000007D
        zz_edict['BUS3YCH29'] = self.BUS3YCH29
        zz_desc['BUS3YCH29'] = ""
        self.BUS3XCH30 = 0x0000007E
        zz_edict['BUS3XCH30'] = self.BUS3XCH30
        zz_desc['BUS3XCH30'] = ""
        self.BUS3YCH31 = 0x0000007F
        zz_edict['BUS3YCH31'] = self.BUS3YCH31
        zz_desc['BUS3YCH31'] = ""
        self.BUS4YCH0 = 0x00000080
        zz_edict['BUS4YCH0'] = self.BUS4YCH0
        zz_desc['BUS4YCH0'] = ""
        self.BUS4XCH1 = 0x00000081
        zz_edict['BUS4XCH1'] = self.BUS4XCH1
        zz_desc['BUS4XCH1'] = ""
        self.BUS4YCH2 = 0x00000082
        zz_edict['BUS4YCH2'] = self.BUS4YCH2
        zz_desc['BUS4YCH2'] = ""
        self.BUS4XCH3 = 0x00000083
        zz_edict['BUS4XCH3'] = self.BUS4XCH3
        zz_desc['BUS4XCH3'] = ""
        self.BUS4YCH4 = 0x00000084
        zz_edict['BUS4YCH4'] = self.BUS4YCH4
        zz_desc['BUS4YCH4'] = ""
        self.BUS4XCH5 = 0x00000085
        zz_edict['BUS4XCH5'] = self.BUS4XCH5
        zz_desc['BUS4XCH5'] = ""
        self.BUS4YCH6 = 0x00000086
        zz_edict['BUS4YCH6'] = self.BUS4YCH6
        zz_desc['BUS4YCH6'] = ""
        self.BUS4XCH7 = 0x00000087
        zz_edict['BUS4XCH7'] = self.BUS4XCH7
        zz_desc['BUS4XCH7'] = ""
        self.BUS4YCH8 = 0x00000088
        zz_edict['BUS4YCH8'] = self.BUS4YCH8
        zz_desc['BUS4YCH8'] = ""
        self.BUS4XCH9 = 0x00000089
        zz_edict['BUS4XCH9'] = self.BUS4XCH9
        zz_desc['BUS4XCH9'] = ""
        self.BUS4YCH10 = 0x0000008A
        zz_edict['BUS4YCH10'] = self.BUS4YCH10
        zz_desc['BUS4YCH10'] = ""
        self.BUS4XCH11 = 0x0000008B
        zz_edict['BUS4XCH11'] = self.BUS4XCH11
        zz_desc['BUS4XCH11'] = ""
        self.BUS4YCH12 = 0x0000008C
        zz_edict['BUS4YCH12'] = self.BUS4YCH12
        zz_desc['BUS4YCH12'] = ""
        self.BUS4XCH13 = 0x0000008D
        zz_edict['BUS4XCH13'] = self.BUS4XCH13
        zz_desc['BUS4XCH13'] = ""
        self.BUS4YCH14 = 0x0000008E
        zz_edict['BUS4YCH14'] = self.BUS4YCH14
        zz_desc['BUS4YCH14'] = ""
        self.BUS4XCH15 = 0x0000008F
        zz_edict['BUS4XCH15'] = self.BUS4XCH15
        zz_desc['BUS4XCH15'] = ""
        self.BUS4YCH16 = 0x00000090
        zz_edict['BUS4YCH16'] = self.BUS4YCH16
        zz_desc['BUS4YCH16'] = ""
        self.BUS4XCH17 = 0x00000091
        zz_edict['BUS4XCH17'] = self.BUS4XCH17
        zz_desc['BUS4XCH17'] = ""
        self.BUS4YCH18 = 0x00000092
        zz_edict['BUS4YCH18'] = self.BUS4YCH18
        zz_desc['BUS4YCH18'] = ""
        self.BUS4XCH19 = 0x00000093
        zz_edict['BUS4XCH19'] = self.BUS4XCH19
        zz_desc['BUS4XCH19'] = ""
        self.BUS4YCH20 = 0x00000094
        zz_edict['BUS4YCH20'] = self.BUS4YCH20
        zz_desc['BUS4YCH20'] = ""
        self.BUS4XCH21 = 0x00000095
        zz_edict['BUS4XCH21'] = self.BUS4XCH21
        zz_desc['BUS4XCH21'] = ""
        self.BUS4YCH22 = 0x00000096
        zz_edict['BUS4YCH22'] = self.BUS4YCH22
        zz_desc['BUS4YCH22'] = ""
        self.BUS4XCH23 = 0x00000097
        zz_edict['BUS4XCH23'] = self.BUS4XCH23
        zz_desc['BUS4XCH23'] = ""
        self.BUS4YCH24 = 0x00000098
        zz_edict['BUS4YCH24'] = self.BUS4YCH24
        zz_desc['BUS4YCH24'] = ""
        self.BUS4XCH25 = 0x00000099
        zz_edict['BUS4XCH25'] = self.BUS4XCH25
        zz_desc['BUS4XCH25'] = ""
        self.BUS4YCH26 = 0x0000009A
        zz_edict['BUS4YCH26'] = self.BUS4YCH26
        zz_desc['BUS4YCH26'] = ""
        self.BUS4XCH27 = 0x0000009B
        zz_edict['BUS4XCH27'] = self.BUS4XCH27
        zz_desc['BUS4XCH27'] = ""
        self.BUS4YCH28 = 0x0000009C
        zz_edict['BUS4YCH28'] = self.BUS4YCH28
        zz_desc['BUS4YCH28'] = ""
        self.BUS4XCH29 = 0x0000009D
        zz_edict['BUS4XCH29'] = self.BUS4XCH29
        zz_desc['BUS4XCH29'] = ""
        self.BUS4YCH30 = 0x0000009E
        zz_edict['BUS4YCH30'] = self.BUS4YCH30
        zz_desc['BUS4YCH30'] = ""
        self.BUS4XCH31 = 0x0000009F
        zz_edict['BUS4XCH31'] = self.BUS4XCH31
        zz_desc['BUS4XCH31'] = ""
        self.AVDD = 0x000000E0
        zz_edict['AVDD'] = self.AVDD
        zz_desc['AVDD'] = ""
        self.BU = 0x000000E1
        zz_edict['BU'] = self.BU
        zz_desc['BU'] = ""
        self.AREG = 0x000000E2
        zz_edict['AREG'] = self.AREG
        zz_desc['AREG'] = ""
        self.VREGOUTPA = 0x000000E3
        zz_edict['VREGOUTPA'] = self.VREGOUTPA
        zz_desc['VREGOUTPA'] = ""
        self.PDBU = 0x000000E4
        zz_edict['PDBU'] = self.PDBU
        zz_desc['PDBU'] = ""
        self.IO0 = 0x000000E5
        zz_edict['IO0'] = self.IO0
        zz_desc['IO0'] = ""
        self.IO1 = 0x000000E6
        zz_edict['IO1'] = self.IO1
        zz_desc['IO1'] = ""
        self.VSP = 0x000000E7
        zz_edict['VSP'] = self.VSP
        zz_desc['VSP'] = ""
        self.SP0 = 0x000000F2
        zz_edict['SP0'] = self.SP0
        zz_desc['SP0'] = ""
        self.TEMP = 0x000000F3
        zz_edict['TEMP'] = self.TEMP
        zz_desc['TEMP'] = ""
        self.DAC0OUT0 = 0x000000F4
        zz_edict['DAC0OUT0'] = self.DAC0OUT0
        zz_desc['DAC0OUT0'] = ""
        self.TESTP = 0x000000F5
        zz_edict['TESTP'] = self.TESTP
        zz_desc['TESTP'] = ""
        self.SP1 = 0x000000F6
        zz_edict['SP1'] = self.SP1
        zz_desc['SP1'] = ""
        self.SP2 = 0x000000F7
        zz_edict['SP2'] = self.SP2
        zz_desc['SP2'] = ""
        self.DAC0OUT1 = 0x000000F8
        zz_edict['DAC0OUT1'] = self.DAC0OUT1
        zz_desc['DAC0OUT1'] = ""
        self.SUBLSB = 0x000000F9
        zz_edict['SUBLSB'] = self.SUBLSB
        zz_desc['SUBLSB'] = ""
        self.VSS = 0x000000FF
        zz_edict['VSS'] = self.VSS
        zz_desc['VSS'] = ""
        super(RM_Enum_ADC0_SINGLECTRL_POSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SINGLECTRL_NEGSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BUS0XCH0 = 0x00000000
        zz_edict['BUS0XCH0'] = self.BUS0XCH0
        zz_desc['BUS0XCH0'] = ""
        self.BUS0XCH1 = 0x00000001
        zz_edict['BUS0XCH1'] = self.BUS0XCH1
        zz_desc['BUS0XCH1'] = ""
        self.BUS0XCH2 = 0x00000002
        zz_edict['BUS0XCH2'] = self.BUS0XCH2
        zz_desc['BUS0XCH2'] = ""
        self.BUS0XCH3 = 0x00000003
        zz_edict['BUS0XCH3'] = self.BUS0XCH3
        zz_desc['BUS0XCH3'] = ""
        self.BUS0XCH4 = 0x00000004
        zz_edict['BUS0XCH4'] = self.BUS0XCH4
        zz_desc['BUS0XCH4'] = ""
        self.BUS0XCH5 = 0x00000005
        zz_edict['BUS0XCH5'] = self.BUS0XCH5
        zz_desc['BUS0XCH5'] = ""
        self.BUS0XCH6 = 0x00000006
        zz_edict['BUS0XCH6'] = self.BUS0XCH6
        zz_desc['BUS0XCH6'] = ""
        self.BUS0XCH7 = 0x00000007
        zz_edict['BUS0XCH7'] = self.BUS0XCH7
        zz_desc['BUS0XCH7'] = ""
        self.BUS0XCH8 = 0x00000008
        zz_edict['BUS0XCH8'] = self.BUS0XCH8
        zz_desc['BUS0XCH8'] = ""
        self.BUS0XCH9 = 0x00000009
        zz_edict['BUS0XCH9'] = self.BUS0XCH9
        zz_desc['BUS0XCH9'] = ""
        self.BUS0XCH10 = 0x0000000A
        zz_edict['BUS0XCH10'] = self.BUS0XCH10
        zz_desc['BUS0XCH10'] = ""
        self.BUS0XCH11 = 0x0000000B
        zz_edict['BUS0XCH11'] = self.BUS0XCH11
        zz_desc['BUS0XCH11'] = ""
        self.BUS0XCH12 = 0x0000000C
        zz_edict['BUS0XCH12'] = self.BUS0XCH12
        zz_desc['BUS0XCH12'] = ""
        self.BUS0XCH13 = 0x0000000D
        zz_edict['BUS0XCH13'] = self.BUS0XCH13
        zz_desc['BUS0XCH13'] = ""
        self.BUS0XCH14 = 0x0000000E
        zz_edict['BUS0XCH14'] = self.BUS0XCH14
        zz_desc['BUS0XCH14'] = ""
        self.BUS0XCH15 = 0x0000000F
        zz_edict['BUS0XCH15'] = self.BUS0XCH15
        zz_desc['BUS0XCH15'] = ""
        self.BUS0YCH0 = 0x00000010
        zz_edict['BUS0YCH0'] = self.BUS0YCH0
        zz_desc['BUS0YCH0'] = ""
        self.BUS0YCH1 = 0x00000011
        zz_edict['BUS0YCH1'] = self.BUS0YCH1
        zz_desc['BUS0YCH1'] = ""
        self.BUS0YCH2 = 0x00000012
        zz_edict['BUS0YCH2'] = self.BUS0YCH2
        zz_desc['BUS0YCH2'] = ""
        self.BUS0YCH3 = 0x00000013
        zz_edict['BUS0YCH3'] = self.BUS0YCH3
        zz_desc['BUS0YCH3'] = ""
        self.BUS0YCH4 = 0x00000014
        zz_edict['BUS0YCH4'] = self.BUS0YCH4
        zz_desc['BUS0YCH4'] = ""
        self.BUS0YCH5 = 0x00000015
        zz_edict['BUS0YCH5'] = self.BUS0YCH5
        zz_desc['BUS0YCH5'] = ""
        self.BUS0YCH6 = 0x00000016
        zz_edict['BUS0YCH6'] = self.BUS0YCH6
        zz_desc['BUS0YCH6'] = ""
        self.BUS0YCH7 = 0x00000017
        zz_edict['BUS0YCH7'] = self.BUS0YCH7
        zz_desc['BUS0YCH7'] = ""
        self.BUS0YCH8 = 0x00000018
        zz_edict['BUS0YCH8'] = self.BUS0YCH8
        zz_desc['BUS0YCH8'] = ""
        self.BUS0YCH9 = 0x00000019
        zz_edict['BUS0YCH9'] = self.BUS0YCH9
        zz_desc['BUS0YCH9'] = ""
        self.BUS0YCH10 = 0x0000001A
        zz_edict['BUS0YCH10'] = self.BUS0YCH10
        zz_desc['BUS0YCH10'] = ""
        self.BUS0YCH11 = 0x0000001B
        zz_edict['BUS0YCH11'] = self.BUS0YCH11
        zz_desc['BUS0YCH11'] = ""
        self.BUS0YCH12 = 0x0000001C
        zz_edict['BUS0YCH12'] = self.BUS0YCH12
        zz_desc['BUS0YCH12'] = ""
        self.BUS0YCH13 = 0x0000001D
        zz_edict['BUS0YCH13'] = self.BUS0YCH13
        zz_desc['BUS0YCH13'] = ""
        self.BUS0YCH14 = 0x0000001E
        zz_edict['BUS0YCH14'] = self.BUS0YCH14
        zz_desc['BUS0YCH14'] = ""
        self.BUS0YCH15 = 0x0000001F
        zz_edict['BUS0YCH15'] = self.BUS0YCH15
        zz_desc['BUS0YCH15'] = ""
        self.BUS1XCH0 = 0x00000020
        zz_edict['BUS1XCH0'] = self.BUS1XCH0
        zz_desc['BUS1XCH0'] = ""
        self.BUS1YCH1 = 0x00000021
        zz_edict['BUS1YCH1'] = self.BUS1YCH1
        zz_desc['BUS1YCH1'] = ""
        self.BUS1XCH2 = 0x00000022
        zz_edict['BUS1XCH2'] = self.BUS1XCH2
        zz_desc['BUS1XCH2'] = ""
        self.BUS1YCH3 = 0x00000023
        zz_edict['BUS1YCH3'] = self.BUS1YCH3
        zz_desc['BUS1YCH3'] = ""
        self.BUS1XCH4 = 0x00000024
        zz_edict['BUS1XCH4'] = self.BUS1XCH4
        zz_desc['BUS1XCH4'] = ""
        self.BUS1YCH5 = 0x00000025
        zz_edict['BUS1YCH5'] = self.BUS1YCH5
        zz_desc['BUS1YCH5'] = ""
        self.BUS1XCH6 = 0x00000026
        zz_edict['BUS1XCH6'] = self.BUS1XCH6
        zz_desc['BUS1XCH6'] = ""
        self.BUS1YCH7 = 0x00000027
        zz_edict['BUS1YCH7'] = self.BUS1YCH7
        zz_desc['BUS1YCH7'] = ""
        self.BUS1XCH8 = 0x00000028
        zz_edict['BUS1XCH8'] = self.BUS1XCH8
        zz_desc['BUS1XCH8'] = ""
        self.BUS1YCH9 = 0x00000029
        zz_edict['BUS1YCH9'] = self.BUS1YCH9
        zz_desc['BUS1YCH9'] = ""
        self.BUS1XCH10 = 0x0000002A
        zz_edict['BUS1XCH10'] = self.BUS1XCH10
        zz_desc['BUS1XCH10'] = ""
        self.BUS1YCH11 = 0x0000002B
        zz_edict['BUS1YCH11'] = self.BUS1YCH11
        zz_desc['BUS1YCH11'] = ""
        self.BUS1XCH12 = 0x0000002C
        zz_edict['BUS1XCH12'] = self.BUS1XCH12
        zz_desc['BUS1XCH12'] = ""
        self.BUS1YCH13 = 0x0000002D
        zz_edict['BUS1YCH13'] = self.BUS1YCH13
        zz_desc['BUS1YCH13'] = ""
        self.BUS1XCH14 = 0x0000002E
        zz_edict['BUS1XCH14'] = self.BUS1XCH14
        zz_desc['BUS1XCH14'] = ""
        self.BUS1YCH15 = 0x0000002F
        zz_edict['BUS1YCH15'] = self.BUS1YCH15
        zz_desc['BUS1YCH15'] = ""
        self.BUS1XCH16 = 0x00000030
        zz_edict['BUS1XCH16'] = self.BUS1XCH16
        zz_desc['BUS1XCH16'] = ""
        self.BUS1YCH17 = 0x00000031
        zz_edict['BUS1YCH17'] = self.BUS1YCH17
        zz_desc['BUS1YCH17'] = ""
        self.BUS1XCH18 = 0x00000032
        zz_edict['BUS1XCH18'] = self.BUS1XCH18
        zz_desc['BUS1XCH18'] = ""
        self.BUS1YCH19 = 0x00000033
        zz_edict['BUS1YCH19'] = self.BUS1YCH19
        zz_desc['BUS1YCH19'] = ""
        self.BUS1XCH20 = 0x00000034
        zz_edict['BUS1XCH20'] = self.BUS1XCH20
        zz_desc['BUS1XCH20'] = ""
        self.BUS1YCH21 = 0x00000035
        zz_edict['BUS1YCH21'] = self.BUS1YCH21
        zz_desc['BUS1YCH21'] = ""
        self.BUS1XCH22 = 0x00000036
        zz_edict['BUS1XCH22'] = self.BUS1XCH22
        zz_desc['BUS1XCH22'] = ""
        self.BUS1YCH23 = 0x00000037
        zz_edict['BUS1YCH23'] = self.BUS1YCH23
        zz_desc['BUS1YCH23'] = ""
        self.BUS1XCH24 = 0x00000038
        zz_edict['BUS1XCH24'] = self.BUS1XCH24
        zz_desc['BUS1XCH24'] = ""
        self.BUS1YCH25 = 0x00000039
        zz_edict['BUS1YCH25'] = self.BUS1YCH25
        zz_desc['BUS1YCH25'] = ""
        self.BUS1XCH26 = 0x0000003A
        zz_edict['BUS1XCH26'] = self.BUS1XCH26
        zz_desc['BUS1XCH26'] = ""
        self.BUS1YCH27 = 0x0000003B
        zz_edict['BUS1YCH27'] = self.BUS1YCH27
        zz_desc['BUS1YCH27'] = ""
        self.BUS1XCH28 = 0x0000003C
        zz_edict['BUS1XCH28'] = self.BUS1XCH28
        zz_desc['BUS1XCH28'] = ""
        self.BUS1YCH29 = 0x0000003D
        zz_edict['BUS1YCH29'] = self.BUS1YCH29
        zz_desc['BUS1YCH29'] = ""
        self.BUS1XCH30 = 0x0000003E
        zz_edict['BUS1XCH30'] = self.BUS1XCH30
        zz_desc['BUS1XCH30'] = ""
        self.BUS1YCH31 = 0x0000003F
        zz_edict['BUS1YCH31'] = self.BUS1YCH31
        zz_desc['BUS1YCH31'] = ""
        self.BUS2YCH0 = 0x00000040
        zz_edict['BUS2YCH0'] = self.BUS2YCH0
        zz_desc['BUS2YCH0'] = ""
        self.BUS2XCH1 = 0x00000041
        zz_edict['BUS2XCH1'] = self.BUS2XCH1
        zz_desc['BUS2XCH1'] = ""
        self.BUS2YCH2 = 0x00000042
        zz_edict['BUS2YCH2'] = self.BUS2YCH2
        zz_desc['BUS2YCH2'] = ""
        self.BUS2XCH3 = 0x00000043
        zz_edict['BUS2XCH3'] = self.BUS2XCH3
        zz_desc['BUS2XCH3'] = ""
        self.BUS2YCH4 = 0x00000044
        zz_edict['BUS2YCH4'] = self.BUS2YCH4
        zz_desc['BUS2YCH4'] = ""
        self.BUS2XCH5 = 0x00000045
        zz_edict['BUS2XCH5'] = self.BUS2XCH5
        zz_desc['BUS2XCH5'] = ""
        self.BUS2YCH6 = 0x00000046
        zz_edict['BUS2YCH6'] = self.BUS2YCH6
        zz_desc['BUS2YCH6'] = ""
        self.BUS2XCH7 = 0x00000047
        zz_edict['BUS2XCH7'] = self.BUS2XCH7
        zz_desc['BUS2XCH7'] = ""
        self.BUS2YCH8 = 0x00000048
        zz_edict['BUS2YCH8'] = self.BUS2YCH8
        zz_desc['BUS2YCH8'] = ""
        self.BUS2XCH9 = 0x00000049
        zz_edict['BUS2XCH9'] = self.BUS2XCH9
        zz_desc['BUS2XCH9'] = ""
        self.BUS2YCH10 = 0x0000004A
        zz_edict['BUS2YCH10'] = self.BUS2YCH10
        zz_desc['BUS2YCH10'] = ""
        self.BUS2XCH11 = 0x0000004B
        zz_edict['BUS2XCH11'] = self.BUS2XCH11
        zz_desc['BUS2XCH11'] = ""
        self.BUS2YCH12 = 0x0000004C
        zz_edict['BUS2YCH12'] = self.BUS2YCH12
        zz_desc['BUS2YCH12'] = ""
        self.BUS2XCH13 = 0x0000004D
        zz_edict['BUS2XCH13'] = self.BUS2XCH13
        zz_desc['BUS2XCH13'] = ""
        self.BUS2YCH14 = 0x0000004E
        zz_edict['BUS2YCH14'] = self.BUS2YCH14
        zz_desc['BUS2YCH14'] = ""
        self.BUS2XCH15 = 0x0000004F
        zz_edict['BUS2XCH15'] = self.BUS2XCH15
        zz_desc['BUS2XCH15'] = ""
        self.BUS2YCH16 = 0x00000050
        zz_edict['BUS2YCH16'] = self.BUS2YCH16
        zz_desc['BUS2YCH16'] = ""
        self.BUS2XCH17 = 0x00000051
        zz_edict['BUS2XCH17'] = self.BUS2XCH17
        zz_desc['BUS2XCH17'] = ""
        self.BUS2YCH18 = 0x00000052
        zz_edict['BUS2YCH18'] = self.BUS2YCH18
        zz_desc['BUS2YCH18'] = ""
        self.BUS2XCH19 = 0x00000053
        zz_edict['BUS2XCH19'] = self.BUS2XCH19
        zz_desc['BUS2XCH19'] = ""
        self.BUS2YCH20 = 0x00000054
        zz_edict['BUS2YCH20'] = self.BUS2YCH20
        zz_desc['BUS2YCH20'] = ""
        self.BUS2XCH21 = 0x00000055
        zz_edict['BUS2XCH21'] = self.BUS2XCH21
        zz_desc['BUS2XCH21'] = ""
        self.BUS2YCH22 = 0x00000056
        zz_edict['BUS2YCH22'] = self.BUS2YCH22
        zz_desc['BUS2YCH22'] = ""
        self.BUS2XCH23 = 0x00000057
        zz_edict['BUS2XCH23'] = self.BUS2XCH23
        zz_desc['BUS2XCH23'] = ""
        self.BUS2YCH24 = 0x00000058
        zz_edict['BUS2YCH24'] = self.BUS2YCH24
        zz_desc['BUS2YCH24'] = ""
        self.BUS2XCH25 = 0x00000059
        zz_edict['BUS2XCH25'] = self.BUS2XCH25
        zz_desc['BUS2XCH25'] = ""
        self.BUS2YCH26 = 0x0000005A
        zz_edict['BUS2YCH26'] = self.BUS2YCH26
        zz_desc['BUS2YCH26'] = ""
        self.BUS2XCH27 = 0x0000005B
        zz_edict['BUS2XCH27'] = self.BUS2XCH27
        zz_desc['BUS2XCH27'] = ""
        self.BUS2YCH28 = 0x0000005C
        zz_edict['BUS2YCH28'] = self.BUS2YCH28
        zz_desc['BUS2YCH28'] = ""
        self.BUS2XCH29 = 0x0000005D
        zz_edict['BUS2XCH29'] = self.BUS2XCH29
        zz_desc['BUS2XCH29'] = ""
        self.BUS2YCH30 = 0x0000005E
        zz_edict['BUS2YCH30'] = self.BUS2YCH30
        zz_desc['BUS2YCH30'] = ""
        self.BUS2XCH31 = 0x0000005F
        zz_edict['BUS2XCH31'] = self.BUS2XCH31
        zz_desc['BUS2XCH31'] = ""
        self.BUS3XCH0 = 0x00000060
        zz_edict['BUS3XCH0'] = self.BUS3XCH0
        zz_desc['BUS3XCH0'] = ""
        self.BUS3YCH1 = 0x00000061
        zz_edict['BUS3YCH1'] = self.BUS3YCH1
        zz_desc['BUS3YCH1'] = ""
        self.BUS3XCH2 = 0x00000062
        zz_edict['BUS3XCH2'] = self.BUS3XCH2
        zz_desc['BUS3XCH2'] = ""
        self.BUS3YCH3 = 0x00000063
        zz_edict['BUS3YCH3'] = self.BUS3YCH3
        zz_desc['BUS3YCH3'] = ""
        self.BUS3XCH4 = 0x00000064
        zz_edict['BUS3XCH4'] = self.BUS3XCH4
        zz_desc['BUS3XCH4'] = ""
        self.BUS3YCH5 = 0x00000065
        zz_edict['BUS3YCH5'] = self.BUS3YCH5
        zz_desc['BUS3YCH5'] = ""
        self.BUS3XCH6 = 0x00000066
        zz_edict['BUS3XCH6'] = self.BUS3XCH6
        zz_desc['BUS3XCH6'] = ""
        self.BUS3YCH7 = 0x00000067
        zz_edict['BUS3YCH7'] = self.BUS3YCH7
        zz_desc['BUS3YCH7'] = ""
        self.BUS3XCH8 = 0x00000068
        zz_edict['BUS3XCH8'] = self.BUS3XCH8
        zz_desc['BUS3XCH8'] = ""
        self.BUS3YCH9 = 0x00000069
        zz_edict['BUS3YCH9'] = self.BUS3YCH9
        zz_desc['BUS3YCH9'] = ""
        self.BUS3XCH10 = 0x0000006A
        zz_edict['BUS3XCH10'] = self.BUS3XCH10
        zz_desc['BUS3XCH10'] = ""
        self.BUS3YCH11 = 0x0000006B
        zz_edict['BUS3YCH11'] = self.BUS3YCH11
        zz_desc['BUS3YCH11'] = ""
        self.BUS3XCH12 = 0x0000006C
        zz_edict['BUS3XCH12'] = self.BUS3XCH12
        zz_desc['BUS3XCH12'] = ""
        self.BUS3YCH13 = 0x0000006D
        zz_edict['BUS3YCH13'] = self.BUS3YCH13
        zz_desc['BUS3YCH13'] = ""
        self.BUS3XCH14 = 0x0000006E
        zz_edict['BUS3XCH14'] = self.BUS3XCH14
        zz_desc['BUS3XCH14'] = ""
        self.BUS3YCH15 = 0x0000006F
        zz_edict['BUS3YCH15'] = self.BUS3YCH15
        zz_desc['BUS3YCH15'] = ""
        self.BUS3XCH16 = 0x00000070
        zz_edict['BUS3XCH16'] = self.BUS3XCH16
        zz_desc['BUS3XCH16'] = ""
        self.BUS3YCH17 = 0x00000071
        zz_edict['BUS3YCH17'] = self.BUS3YCH17
        zz_desc['BUS3YCH17'] = ""
        self.BUS3XCH18 = 0x00000072
        zz_edict['BUS3XCH18'] = self.BUS3XCH18
        zz_desc['BUS3XCH18'] = ""
        self.BUS3YCH19 = 0x00000073
        zz_edict['BUS3YCH19'] = self.BUS3YCH19
        zz_desc['BUS3YCH19'] = ""
        self.BUS3XCH20 = 0x00000074
        zz_edict['BUS3XCH20'] = self.BUS3XCH20
        zz_desc['BUS3XCH20'] = ""
        self.BUS3YCH21 = 0x00000075
        zz_edict['BUS3YCH21'] = self.BUS3YCH21
        zz_desc['BUS3YCH21'] = ""
        self.BUS3XCH22 = 0x00000076
        zz_edict['BUS3XCH22'] = self.BUS3XCH22
        zz_desc['BUS3XCH22'] = ""
        self.BUS3YCH23 = 0x00000077
        zz_edict['BUS3YCH23'] = self.BUS3YCH23
        zz_desc['BUS3YCH23'] = ""
        self.BUS3XCH24 = 0x00000078
        zz_edict['BUS3XCH24'] = self.BUS3XCH24
        zz_desc['BUS3XCH24'] = ""
        self.BUS3YCH25 = 0x00000079
        zz_edict['BUS3YCH25'] = self.BUS3YCH25
        zz_desc['BUS3YCH25'] = ""
        self.BUS3XCH26 = 0x0000007A
        zz_edict['BUS3XCH26'] = self.BUS3XCH26
        zz_desc['BUS3XCH26'] = ""
        self.BUS3YCH27 = 0x0000007B
        zz_edict['BUS3YCH27'] = self.BUS3YCH27
        zz_desc['BUS3YCH27'] = ""
        self.BUS3XCH28 = 0x0000007C
        zz_edict['BUS3XCH28'] = self.BUS3XCH28
        zz_desc['BUS3XCH28'] = ""
        self.BUS3YCH29 = 0x0000007D
        zz_edict['BUS3YCH29'] = self.BUS3YCH29
        zz_desc['BUS3YCH29'] = ""
        self.BUS3XCH30 = 0x0000007E
        zz_edict['BUS3XCH30'] = self.BUS3XCH30
        zz_desc['BUS3XCH30'] = ""
        self.BUS3YCH31 = 0x0000007F
        zz_edict['BUS3YCH31'] = self.BUS3YCH31
        zz_desc['BUS3YCH31'] = ""
        self.BUS4YCH0 = 0x00000080
        zz_edict['BUS4YCH0'] = self.BUS4YCH0
        zz_desc['BUS4YCH0'] = ""
        self.BUS4XCH1 = 0x00000081
        zz_edict['BUS4XCH1'] = self.BUS4XCH1
        zz_desc['BUS4XCH1'] = ""
        self.BUS4YCH2 = 0x00000082
        zz_edict['BUS4YCH2'] = self.BUS4YCH2
        zz_desc['BUS4YCH2'] = ""
        self.BUS4XCH3 = 0x00000083
        zz_edict['BUS4XCH3'] = self.BUS4XCH3
        zz_desc['BUS4XCH3'] = ""
        self.BUS4YCH4 = 0x00000084
        zz_edict['BUS4YCH4'] = self.BUS4YCH4
        zz_desc['BUS4YCH4'] = ""
        self.BUS4XCH5 = 0x00000085
        zz_edict['BUS4XCH5'] = self.BUS4XCH5
        zz_desc['BUS4XCH5'] = ""
        self.BUS4YCH6 = 0x00000086
        zz_edict['BUS4YCH6'] = self.BUS4YCH6
        zz_desc['BUS4YCH6'] = ""
        self.BUS4XCH7 = 0x00000087
        zz_edict['BUS4XCH7'] = self.BUS4XCH7
        zz_desc['BUS4XCH7'] = ""
        self.BUS4YCH8 = 0x00000088
        zz_edict['BUS4YCH8'] = self.BUS4YCH8
        zz_desc['BUS4YCH8'] = ""
        self.BUS4XCH9 = 0x00000089
        zz_edict['BUS4XCH9'] = self.BUS4XCH9
        zz_desc['BUS4XCH9'] = ""
        self.BUS4YCH10 = 0x0000008A
        zz_edict['BUS4YCH10'] = self.BUS4YCH10
        zz_desc['BUS4YCH10'] = ""
        self.BUS4XCH11 = 0x0000008B
        zz_edict['BUS4XCH11'] = self.BUS4XCH11
        zz_desc['BUS4XCH11'] = ""
        self.BUS4YCH12 = 0x0000008C
        zz_edict['BUS4YCH12'] = self.BUS4YCH12
        zz_desc['BUS4YCH12'] = ""
        self.BUS4XCH13 = 0x0000008D
        zz_edict['BUS4XCH13'] = self.BUS4XCH13
        zz_desc['BUS4XCH13'] = ""
        self.BUS4YCH14 = 0x0000008E
        zz_edict['BUS4YCH14'] = self.BUS4YCH14
        zz_desc['BUS4YCH14'] = ""
        self.BUS4XCH15 = 0x0000008F
        zz_edict['BUS4XCH15'] = self.BUS4XCH15
        zz_desc['BUS4XCH15'] = ""
        self.BUS4YCH16 = 0x00000090
        zz_edict['BUS4YCH16'] = self.BUS4YCH16
        zz_desc['BUS4YCH16'] = ""
        self.BUS4XCH17 = 0x00000091
        zz_edict['BUS4XCH17'] = self.BUS4XCH17
        zz_desc['BUS4XCH17'] = ""
        self.BUS4YCH18 = 0x00000092
        zz_edict['BUS4YCH18'] = self.BUS4YCH18
        zz_desc['BUS4YCH18'] = ""
        self.BUS4XCH19 = 0x00000093
        zz_edict['BUS4XCH19'] = self.BUS4XCH19
        zz_desc['BUS4XCH19'] = ""
        self.BUS4YCH20 = 0x00000094
        zz_edict['BUS4YCH20'] = self.BUS4YCH20
        zz_desc['BUS4YCH20'] = ""
        self.BUS4XCH21 = 0x00000095
        zz_edict['BUS4XCH21'] = self.BUS4XCH21
        zz_desc['BUS4XCH21'] = ""
        self.BUS4YCH22 = 0x00000096
        zz_edict['BUS4YCH22'] = self.BUS4YCH22
        zz_desc['BUS4YCH22'] = ""
        self.BUS4XCH23 = 0x00000097
        zz_edict['BUS4XCH23'] = self.BUS4XCH23
        zz_desc['BUS4XCH23'] = ""
        self.BUS4YCH24 = 0x00000098
        zz_edict['BUS4YCH24'] = self.BUS4YCH24
        zz_desc['BUS4YCH24'] = ""
        self.BUS4XCH25 = 0x00000099
        zz_edict['BUS4XCH25'] = self.BUS4XCH25
        zz_desc['BUS4XCH25'] = ""
        self.BUS4YCH26 = 0x0000009A
        zz_edict['BUS4YCH26'] = self.BUS4YCH26
        zz_desc['BUS4YCH26'] = ""
        self.BUS4XCH27 = 0x0000009B
        zz_edict['BUS4XCH27'] = self.BUS4XCH27
        zz_desc['BUS4XCH27'] = ""
        self.BUS4YCH28 = 0x0000009C
        zz_edict['BUS4YCH28'] = self.BUS4YCH28
        zz_desc['BUS4YCH28'] = ""
        self.BUS4XCH29 = 0x0000009D
        zz_edict['BUS4XCH29'] = self.BUS4XCH29
        zz_desc['BUS4XCH29'] = ""
        self.BUS4YCH30 = 0x0000009E
        zz_edict['BUS4YCH30'] = self.BUS4YCH30
        zz_desc['BUS4YCH30'] = ""
        self.BUS4XCH31 = 0x0000009F
        zz_edict['BUS4XCH31'] = self.BUS4XCH31
        zz_desc['BUS4XCH31'] = ""
        self.TESTN = 0x000000F5
        zz_edict['TESTN'] = self.TESTN
        zz_desc['TESTN'] = ""
        self.VSS = 0x000000FF
        zz_edict['VSS'] = self.VSS
        zz_desc['VSS'] = ""
        super(RM_Enum_ADC0_SINGLECTRL_NEGSEL, self).__init__(
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
        #print("WARNING: Aliasing enum '5VDIFF' to 'E5VDIFF'")
        self.E5VDIFF = 0x00000003
        zz_edict['E5VDIFF'] = self.E5VDIFF
        zz_desc['E5VDIFF'] = ""
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


class RM_Enum_ADC0_SCANMASK_SCANMASK(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CH0CH0NSEL = 0x00000001
        zz_edict['CH0CH0NSEL'] = self.CH0CH0NSEL
        zz_desc['CH0CH0NSEL'] = ""
        self.CH0 = 0x00000001
        zz_edict['CH0'] = self.CH0
        zz_desc['CH0'] = ""
        self.CH1CH2 = 0x00000002
        zz_edict['CH1CH2'] = self.CH1CH2
        zz_desc['CH1CH2'] = ""
        self.CH1 = 0x00000002
        zz_edict['CH1'] = self.CH1
        zz_desc['CH1'] = ""
        self.CH2 = 0x00000004
        zz_edict['CH2'] = self.CH2
        zz_desc['CH2'] = ""
        self.CH2CH2NSEL = 0x00000004
        zz_edict['CH2CH2NSEL'] = self.CH2CH2NSEL
        zz_desc['CH2CH2NSEL'] = ""
        self.CH3 = 0x00000008
        zz_edict['CH3'] = self.CH3
        zz_desc['CH3'] = ""
        self.CH3CH4 = 0x00000008
        zz_edict['CH3CH4'] = self.CH3CH4
        zz_desc['CH3CH4'] = ""
        self.CH4 = 0x00000010
        zz_edict['CH4'] = self.CH4
        zz_desc['CH4'] = ""
        self.CH4CH4NSEL = 0x00000010
        zz_edict['CH4CH4NSEL'] = self.CH4CH4NSEL
        zz_desc['CH4CH4NSEL'] = ""
        self.CH5CH6 = 0x00000020
        zz_edict['CH5CH6'] = self.CH5CH6
        zz_desc['CH5CH6'] = ""
        self.CH5 = 0x00000020
        zz_edict['CH5'] = self.CH5
        zz_desc['CH5'] = ""
        self.CH6 = 0x00000040
        zz_edict['CH6'] = self.CH6
        zz_desc['CH6'] = ""
        self.CH6CH6NSEL = 0x00000040
        zz_edict['CH6CH6NSEL'] = self.CH6CH6NSEL
        zz_desc['CH6CH6NSEL'] = ""
        self.CH7 = 0x00000080
        zz_edict['CH7'] = self.CH7
        zz_desc['CH7'] = ""
        self.CH7CH0 = 0x00000080
        zz_edict['CH7CH0'] = self.CH7CH0
        zz_desc['CH7CH0'] = ""
        self.CH8 = 0x00000100
        zz_edict['CH8'] = self.CH8
        zz_desc['CH8'] = ""
        self.CH8CH9 = 0x00000100
        zz_edict['CH8CH9'] = self.CH8CH9
        zz_desc['CH8CH9'] = ""
        self.CH9 = 0x00000200
        zz_edict['CH9'] = self.CH9
        zz_desc['CH9'] = ""
        self.CH9CH9NSEL = 0x00000200
        zz_edict['CH9CH9NSEL'] = self.CH9CH9NSEL
        zz_desc['CH9CH9NSEL'] = ""
        self.CH10 = 0x00000400
        zz_edict['CH10'] = self.CH10
        zz_desc['CH10'] = ""
        self.CH10CH11 = 0x00000400
        zz_edict['CH10CH11'] = self.CH10CH11
        zz_desc['CH10CH11'] = ""
        self.CH11 = 0x00000800
        zz_edict['CH11'] = self.CH11
        zz_desc['CH11'] = ""
        self.CH11CH11NSEL = 0x00000800
        zz_edict['CH11CH11NSEL'] = self.CH11CH11NSEL
        zz_desc['CH11CH11NSEL'] = ""
        self.CH12CH13 = 0x00001000
        zz_edict['CH12CH13'] = self.CH12CH13
        zz_desc['CH12CH13'] = ""
        self.CH12 = 0x00001000
        zz_edict['CH12'] = self.CH12
        zz_desc['CH12'] = ""
        self.CH13 = 0x00002000
        zz_edict['CH13'] = self.CH13
        zz_desc['CH13'] = ""
        self.CH13CH13NSEL = 0x00002000
        zz_edict['CH13CH13NSEL'] = self.CH13CH13NSEL
        zz_desc['CH13CH13NSEL'] = ""
        self.CH14CH15 = 0x00004000
        zz_edict['CH14CH15'] = self.CH14CH15
        zz_desc['CH14CH15'] = ""
        self.CH14 = 0x00004000
        zz_edict['CH14'] = self.CH14
        zz_desc['CH14'] = ""
        self.CH15 = 0x00008000
        zz_edict['CH15'] = self.CH15
        zz_desc['CH15'] = ""
        self.CH15CH15NSEL = 0x00008000
        zz_edict['CH15CH15NSEL'] = self.CH15CH15NSEL
        zz_desc['CH15CH15NSEL'] = ""
        self.CH16 = 0x00010000
        zz_edict['CH16'] = self.CH16
        zz_desc['CH16'] = ""
        self.CH16CH17 = 0x00010000
        zz_edict['CH16CH17'] = self.CH16CH17
        zz_desc['CH16CH17'] = ""
        self.CH17CH18 = 0x00020000
        zz_edict['CH17CH18'] = self.CH17CH18
        zz_desc['CH17CH18'] = ""
        self.CH17 = 0x00020000
        zz_edict['CH17'] = self.CH17
        zz_desc['CH17'] = ""
        self.CH18 = 0x00040000
        zz_edict['CH18'] = self.CH18
        zz_desc['CH18'] = ""
        self.CH18CH19 = 0x00040000
        zz_edict['CH18CH19'] = self.CH18CH19
        zz_desc['CH18CH19'] = ""
        self.CH19CH20 = 0x00080000
        zz_edict['CH19CH20'] = self.CH19CH20
        zz_desc['CH19CH20'] = ""
        self.CH19 = 0x00080000
        zz_edict['CH19'] = self.CH19
        zz_desc['CH19'] = ""
        self.CH20 = 0x00100000
        zz_edict['CH20'] = self.CH20
        zz_desc['CH20'] = ""
        self.CH20CH21 = 0x00100000
        zz_edict['CH20CH21'] = self.CH20CH21
        zz_desc['CH20CH21'] = ""
        self.CH21 = 0x00200000
        zz_edict['CH21'] = self.CH21
        zz_desc['CH21'] = ""
        self.CH21CH22 = 0x00200000
        zz_edict['CH21CH22'] = self.CH21CH22
        zz_desc['CH21CH22'] = ""
        self.CH22 = 0x00400000
        zz_edict['CH22'] = self.CH22
        zz_desc['CH22'] = ""
        self.CH22CH23 = 0x00400000
        zz_edict['CH22CH23'] = self.CH22CH23
        zz_desc['CH22CH23'] = ""
        self.CH23 = 0x00800000
        zz_edict['CH23'] = self.CH23
        zz_desc['CH23'] = ""
        self.CH23CH16 = 0x00800000
        zz_edict['CH23CH16'] = self.CH23CH16
        zz_desc['CH23CH16'] = ""
        self.CH24 = 0x01000000
        zz_edict['CH24'] = self.CH24
        zz_desc['CH24'] = ""
        self.CH24CH25 = 0x01000000
        zz_edict['CH24CH25'] = self.CH24CH25
        zz_desc['CH24CH25'] = ""
        self.CH25 = 0x02000000
        zz_edict['CH25'] = self.CH25
        zz_desc['CH25'] = ""
        self.CH25CH26 = 0x02000000
        zz_edict['CH25CH26'] = self.CH25CH26
        zz_desc['CH25CH26'] = ""
        self.CH26 = 0x04000000
        zz_edict['CH26'] = self.CH26
        zz_desc['CH26'] = ""
        self.CH26CH27 = 0x04000000
        zz_edict['CH26CH27'] = self.CH26CH27
        zz_desc['CH26CH27'] = ""
        self.CH27 = 0x08000000
        zz_edict['CH27'] = self.CH27
        zz_desc['CH27'] = ""
        self.CH27CH28 = 0x08000000
        zz_edict['CH27CH28'] = self.CH27CH28
        zz_desc['CH27CH28'] = ""
        self.CH28 = 0x10000000
        zz_edict['CH28'] = self.CH28
        zz_desc['CH28'] = ""
        self.CH28CH29 = 0x10000000
        zz_edict['CH28CH29'] = self.CH28CH29
        zz_desc['CH28CH29'] = ""
        self.CH29CH30 = 0x20000000
        zz_edict['CH29CH30'] = self.CH29CH30
        zz_desc['CH29CH30'] = ""
        self.CH29 = 0x20000000
        zz_edict['CH29'] = self.CH29
        zz_desc['CH29'] = ""
        self.CH30 = 0x40000000
        zz_edict['CH30'] = self.CH30
        zz_desc['CH30'] = ""
        self.CH30CH31 = 0x40000000
        zz_edict['CH30CH31'] = self.CH30CH31
        zz_desc['CH30CH31'] = ""
        self.CH31CH24 = 0x80000000
        zz_edict['CH31CH24'] = self.CH31CH24
        zz_desc['CH31CH24'] = ""
        self.CH31 = 0x80000000
        zz_edict['CH31'] = self.CH31
        zz_desc['CH31'] = ""
        super(RM_Enum_ADC0_SCANMASK_SCANMASK, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANCHCONF_CH0TO7SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BUS0CH0TO7 = 0x00000000
        zz_edict['BUS0CH0TO7'] = self.BUS0CH0TO7
        zz_desc['BUS0CH0TO7'] = ""
        self.BUS0CH8TO15 = 0x00000001
        zz_edict['BUS0CH8TO15'] = self.BUS0CH8TO15
        zz_desc['BUS0CH8TO15'] = ""
        self.BUS1CH0TO7 = 0x00000004
        zz_edict['BUS1CH0TO7'] = self.BUS1CH0TO7
        zz_desc['BUS1CH0TO7'] = ""
        self.BUS1CH8TO15 = 0x00000005
        zz_edict['BUS1CH8TO15'] = self.BUS1CH8TO15
        zz_desc['BUS1CH8TO15'] = ""
        self.BUS1CH16TO23 = 0x00000006
        zz_edict['BUS1CH16TO23'] = self.BUS1CH16TO23
        zz_desc['BUS1CH16TO23'] = ""
        self.BUS1CH24TO31 = 0x00000007
        zz_edict['BUS1CH24TO31'] = self.BUS1CH24TO31
        zz_desc['BUS1CH24TO31'] = ""
        self.BUS2CH0TO7 = 0x00000008
        zz_edict['BUS2CH0TO7'] = self.BUS2CH0TO7
        zz_desc['BUS2CH0TO7'] = ""
        self.BUS2CH8TO15 = 0x00000009
        zz_edict['BUS2CH8TO15'] = self.BUS2CH8TO15
        zz_desc['BUS2CH8TO15'] = ""
        self.BUS2CH16TO23 = 0x0000000A
        zz_edict['BUS2CH16TO23'] = self.BUS2CH16TO23
        zz_desc['BUS2CH16TO23'] = ""
        self.BUS2CH24TO31 = 0x0000000B
        zz_edict['BUS2CH24TO31'] = self.BUS2CH24TO31
        zz_desc['BUS2CH24TO31'] = ""
        self.BUS3CH0TO7 = 0x0000000C
        zz_edict['BUS3CH0TO7'] = self.BUS3CH0TO7
        zz_desc['BUS3CH0TO7'] = ""
        self.BUS3CH8TO15 = 0x0000000D
        zz_edict['BUS3CH8TO15'] = self.BUS3CH8TO15
        zz_desc['BUS3CH8TO15'] = ""
        self.BUS3CH16TO23 = 0x0000000E
        zz_edict['BUS3CH16TO23'] = self.BUS3CH16TO23
        zz_desc['BUS3CH16TO23'] = ""
        self.BUS3CH24TO31 = 0x0000000F
        zz_edict['BUS3CH24TO31'] = self.BUS3CH24TO31
        zz_desc['BUS3CH24TO31'] = ""
        self.BUS4CH0TO7 = 0x00000010
        zz_edict['BUS4CH0TO7'] = self.BUS4CH0TO7
        zz_desc['BUS4CH0TO7'] = ""
        self.BUS4CH8TO15 = 0x00000011
        zz_edict['BUS4CH8TO15'] = self.BUS4CH8TO15
        zz_desc['BUS4CH8TO15'] = ""
        self.BUS4CH16TO23 = 0x00000012
        zz_edict['BUS4CH16TO23'] = self.BUS4CH16TO23
        zz_desc['BUS4CH16TO23'] = ""
        self.BUS4CH24TO31 = 0x00000013
        zz_edict['BUS4CH24TO31'] = self.BUS4CH24TO31
        zz_desc['BUS4CH24TO31'] = ""
        super(RM_Enum_ADC0_SCANCHCONF_CH0TO7SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANCHCONF_CH8TO15SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BUS0CH0TO7 = 0x00000000
        zz_edict['BUS0CH0TO7'] = self.BUS0CH0TO7
        zz_desc['BUS0CH0TO7'] = ""
        self.BUS0CH8TO15 = 0x00000001
        zz_edict['BUS0CH8TO15'] = self.BUS0CH8TO15
        zz_desc['BUS0CH8TO15'] = ""
        self.BUS1CH0TO7 = 0x00000004
        zz_edict['BUS1CH0TO7'] = self.BUS1CH0TO7
        zz_desc['BUS1CH0TO7'] = ""
        self.BUS1CH8TO15 = 0x00000005
        zz_edict['BUS1CH8TO15'] = self.BUS1CH8TO15
        zz_desc['BUS1CH8TO15'] = ""
        self.BUS1CH16TO23 = 0x00000006
        zz_edict['BUS1CH16TO23'] = self.BUS1CH16TO23
        zz_desc['BUS1CH16TO23'] = ""
        self.BUS1CH24TO31 = 0x00000007
        zz_edict['BUS1CH24TO31'] = self.BUS1CH24TO31
        zz_desc['BUS1CH24TO31'] = ""
        self.BUS2CH0TO7 = 0x00000008
        zz_edict['BUS2CH0TO7'] = self.BUS2CH0TO7
        zz_desc['BUS2CH0TO7'] = ""
        self.BUS2CH8TO15 = 0x00000009
        zz_edict['BUS2CH8TO15'] = self.BUS2CH8TO15
        zz_desc['BUS2CH8TO15'] = ""
        self.BUS2CH16TO23 = 0x0000000A
        zz_edict['BUS2CH16TO23'] = self.BUS2CH16TO23
        zz_desc['BUS2CH16TO23'] = ""
        self.BUS2CH24TO31 = 0x0000000B
        zz_edict['BUS2CH24TO31'] = self.BUS2CH24TO31
        zz_desc['BUS2CH24TO31'] = ""
        self.BUS3CH0TO7 = 0x0000000C
        zz_edict['BUS3CH0TO7'] = self.BUS3CH0TO7
        zz_desc['BUS3CH0TO7'] = ""
        self.BUS3CH8TO15 = 0x0000000D
        zz_edict['BUS3CH8TO15'] = self.BUS3CH8TO15
        zz_desc['BUS3CH8TO15'] = ""
        self.BUS3CH16TO23 = 0x0000000E
        zz_edict['BUS3CH16TO23'] = self.BUS3CH16TO23
        zz_desc['BUS3CH16TO23'] = ""
        self.BUS3CH24TO31 = 0x0000000F
        zz_edict['BUS3CH24TO31'] = self.BUS3CH24TO31
        zz_desc['BUS3CH24TO31'] = ""
        self.BUS4CH0TO7 = 0x00000010
        zz_edict['BUS4CH0TO7'] = self.BUS4CH0TO7
        zz_desc['BUS4CH0TO7'] = ""
        self.BUS4CH8TO15 = 0x00000011
        zz_edict['BUS4CH8TO15'] = self.BUS4CH8TO15
        zz_desc['BUS4CH8TO15'] = ""
        self.BUS4CH16TO23 = 0x00000012
        zz_edict['BUS4CH16TO23'] = self.BUS4CH16TO23
        zz_desc['BUS4CH16TO23'] = ""
        self.BUS4CH24TO31 = 0x00000013
        zz_edict['BUS4CH24TO31'] = self.BUS4CH24TO31
        zz_desc['BUS4CH24TO31'] = ""
        super(RM_Enum_ADC0_SCANCHCONF_CH8TO15SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANCHCONF_CH16TO23SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BUS0CH0TO7 = 0x00000000
        zz_edict['BUS0CH0TO7'] = self.BUS0CH0TO7
        zz_desc['BUS0CH0TO7'] = ""
        self.BUS0CH8TO15 = 0x00000001
        zz_edict['BUS0CH8TO15'] = self.BUS0CH8TO15
        zz_desc['BUS0CH8TO15'] = ""
        self.BUS1CH0TO7 = 0x00000004
        zz_edict['BUS1CH0TO7'] = self.BUS1CH0TO7
        zz_desc['BUS1CH0TO7'] = ""
        self.BUS1CH8TO15 = 0x00000005
        zz_edict['BUS1CH8TO15'] = self.BUS1CH8TO15
        zz_desc['BUS1CH8TO15'] = ""
        self.BUS1CH16TO23 = 0x00000006
        zz_edict['BUS1CH16TO23'] = self.BUS1CH16TO23
        zz_desc['BUS1CH16TO23'] = ""
        self.BUS1CH24TO31 = 0x00000007
        zz_edict['BUS1CH24TO31'] = self.BUS1CH24TO31
        zz_desc['BUS1CH24TO31'] = ""
        self.BUS2CH0TO7 = 0x00000008
        zz_edict['BUS2CH0TO7'] = self.BUS2CH0TO7
        zz_desc['BUS2CH0TO7'] = ""
        self.BUS2CH8TO15 = 0x00000009
        zz_edict['BUS2CH8TO15'] = self.BUS2CH8TO15
        zz_desc['BUS2CH8TO15'] = ""
        self.BUS2CH16TO23 = 0x0000000A
        zz_edict['BUS2CH16TO23'] = self.BUS2CH16TO23
        zz_desc['BUS2CH16TO23'] = ""
        self.BUS2CH24TO31 = 0x0000000B
        zz_edict['BUS2CH24TO31'] = self.BUS2CH24TO31
        zz_desc['BUS2CH24TO31'] = ""
        self.BUS3CH0TO7 = 0x0000000C
        zz_edict['BUS3CH0TO7'] = self.BUS3CH0TO7
        zz_desc['BUS3CH0TO7'] = ""
        self.BUS3CH8TO15 = 0x0000000D
        zz_edict['BUS3CH8TO15'] = self.BUS3CH8TO15
        zz_desc['BUS3CH8TO15'] = ""
        self.BUS3CH16TO23 = 0x0000000E
        zz_edict['BUS3CH16TO23'] = self.BUS3CH16TO23
        zz_desc['BUS3CH16TO23'] = ""
        self.BUS3CH24TO31 = 0x0000000F
        zz_edict['BUS3CH24TO31'] = self.BUS3CH24TO31
        zz_desc['BUS3CH24TO31'] = ""
        self.BUS4CH0TO7 = 0x00000010
        zz_edict['BUS4CH0TO7'] = self.BUS4CH0TO7
        zz_desc['BUS4CH0TO7'] = ""
        self.BUS4CH8TO15 = 0x00000011
        zz_edict['BUS4CH8TO15'] = self.BUS4CH8TO15
        zz_desc['BUS4CH8TO15'] = ""
        self.BUS4CH16TO23 = 0x00000012
        zz_edict['BUS4CH16TO23'] = self.BUS4CH16TO23
        zz_desc['BUS4CH16TO23'] = ""
        self.BUS4CH24TO31 = 0x00000013
        zz_edict['BUS4CH24TO31'] = self.BUS4CH24TO31
        zz_desc['BUS4CH24TO31'] = ""
        super(RM_Enum_ADC0_SCANCHCONF_CH16TO23SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANCHCONF_CH24TO31SEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BUS0CH0TO7 = 0x00000000
        zz_edict['BUS0CH0TO7'] = self.BUS0CH0TO7
        zz_desc['BUS0CH0TO7'] = ""
        self.BUS0CH8TO15 = 0x00000001
        zz_edict['BUS0CH8TO15'] = self.BUS0CH8TO15
        zz_desc['BUS0CH8TO15'] = ""
        self.BUS1CH0TO7 = 0x00000004
        zz_edict['BUS1CH0TO7'] = self.BUS1CH0TO7
        zz_desc['BUS1CH0TO7'] = ""
        self.BUS1CH8TO15 = 0x00000005
        zz_edict['BUS1CH8TO15'] = self.BUS1CH8TO15
        zz_desc['BUS1CH8TO15'] = ""
        self.BUS1CH16TO23 = 0x00000006
        zz_edict['BUS1CH16TO23'] = self.BUS1CH16TO23
        zz_desc['BUS1CH16TO23'] = ""
        self.BUS1CH24TO31 = 0x00000007
        zz_edict['BUS1CH24TO31'] = self.BUS1CH24TO31
        zz_desc['BUS1CH24TO31'] = ""
        self.BUS2CH0TO7 = 0x00000008
        zz_edict['BUS2CH0TO7'] = self.BUS2CH0TO7
        zz_desc['BUS2CH0TO7'] = ""
        self.BUS2CH8TO15 = 0x00000009
        zz_edict['BUS2CH8TO15'] = self.BUS2CH8TO15
        zz_desc['BUS2CH8TO15'] = ""
        self.BUS2CH16TO23 = 0x0000000A
        zz_edict['BUS2CH16TO23'] = self.BUS2CH16TO23
        zz_desc['BUS2CH16TO23'] = ""
        self.BUS2CH24TO31 = 0x0000000B
        zz_edict['BUS2CH24TO31'] = self.BUS2CH24TO31
        zz_desc['BUS2CH24TO31'] = ""
        self.BUS3CH0TO7 = 0x0000000C
        zz_edict['BUS3CH0TO7'] = self.BUS3CH0TO7
        zz_desc['BUS3CH0TO7'] = ""
        self.BUS3CH8TO15 = 0x0000000D
        zz_edict['BUS3CH8TO15'] = self.BUS3CH8TO15
        zz_desc['BUS3CH8TO15'] = ""
        self.BUS3CH16TO23 = 0x0000000E
        zz_edict['BUS3CH16TO23'] = self.BUS3CH16TO23
        zz_desc['BUS3CH16TO23'] = ""
        self.BUS3CH24TO31 = 0x0000000F
        zz_edict['BUS3CH24TO31'] = self.BUS3CH24TO31
        zz_desc['BUS3CH24TO31'] = ""
        self.BUS4CH0TO7 = 0x00000010
        zz_edict['BUS4CH0TO7'] = self.BUS4CH0TO7
        zz_desc['BUS4CH0TO7'] = ""
        self.BUS4CH8TO15 = 0x00000011
        zz_edict['BUS4CH8TO15'] = self.BUS4CH8TO15
        zz_desc['BUS4CH8TO15'] = ""
        self.BUS4CH16TO23 = 0x00000012
        zz_edict['BUS4CH16TO23'] = self.BUS4CH16TO23
        zz_desc['BUS4CH16TO23'] = ""
        self.BUS4CH24TO31 = 0x00000013
        zz_edict['BUS4CH24TO31'] = self.BUS4CH24TO31
        zz_desc['BUS4CH24TO31'] = ""
        super(RM_Enum_ADC0_SCANCHCONF_CH24TO31SEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNSEL_CH0NSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CH1 = 0x00000000
        zz_edict['CH1'] = self.CH1
        zz_desc['CH1'] = ""
        self.CH3 = 0x00000001
        zz_edict['CH3'] = self.CH3
        zz_desc['CH3'] = ""
        self.CH5 = 0x00000002
        zz_edict['CH5'] = self.CH5
        zz_desc['CH5'] = ""
        self.CH7 = 0x00000003
        zz_edict['CH7'] = self.CH7
        zz_desc['CH7'] = ""
        super(RM_Enum_ADC0_SCANNSEL_CH0NSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNSEL_CH2NSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CH1 = 0x00000000
        zz_edict['CH1'] = self.CH1
        zz_desc['CH1'] = ""
        self.CH3 = 0x00000001
        zz_edict['CH3'] = self.CH3
        zz_desc['CH3'] = ""
        self.CH5 = 0x00000002
        zz_edict['CH5'] = self.CH5
        zz_desc['CH5'] = ""
        self.CH7 = 0x00000003
        zz_edict['CH7'] = self.CH7
        zz_desc['CH7'] = ""
        super(RM_Enum_ADC0_SCANNSEL_CH2NSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNSEL_CH4NSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CH1 = 0x00000000
        zz_edict['CH1'] = self.CH1
        zz_desc['CH1'] = ""
        self.CH3 = 0x00000001
        zz_edict['CH3'] = self.CH3
        zz_desc['CH3'] = ""
        self.CH5 = 0x00000002
        zz_edict['CH5'] = self.CH5
        zz_desc['CH5'] = ""
        self.CH7 = 0x00000003
        zz_edict['CH7'] = self.CH7
        zz_desc['CH7'] = ""
        super(RM_Enum_ADC0_SCANNSEL_CH4NSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNSEL_CH6NSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CH1 = 0x00000000
        zz_edict['CH1'] = self.CH1
        zz_desc['CH1'] = ""
        self.CH3 = 0x00000001
        zz_edict['CH3'] = self.CH3
        zz_desc['CH3'] = ""
        self.CH5 = 0x00000002
        zz_edict['CH5'] = self.CH5
        zz_desc['CH5'] = ""
        self.CH7 = 0x00000003
        zz_edict['CH7'] = self.CH7
        zz_desc['CH7'] = ""
        super(RM_Enum_ADC0_SCANNSEL_CH6NSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNSEL_CH9NSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CH8 = 0x00000000
        zz_edict['CH8'] = self.CH8
        zz_desc['CH8'] = ""
        self.CH10 = 0x00000001
        zz_edict['CH10'] = self.CH10
        zz_desc['CH10'] = ""
        self.CH12 = 0x00000002
        zz_edict['CH12'] = self.CH12
        zz_desc['CH12'] = ""
        self.CH14 = 0x00000003
        zz_edict['CH14'] = self.CH14
        zz_desc['CH14'] = ""
        super(RM_Enum_ADC0_SCANNSEL_CH9NSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNSEL_CH11NSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CH8 = 0x00000000
        zz_edict['CH8'] = self.CH8
        zz_desc['CH8'] = ""
        self.CH10 = 0x00000001
        zz_edict['CH10'] = self.CH10
        zz_desc['CH10'] = ""
        self.CH12 = 0x00000002
        zz_edict['CH12'] = self.CH12
        zz_desc['CH12'] = ""
        self.CH14 = 0x00000003
        zz_edict['CH14'] = self.CH14
        zz_desc['CH14'] = ""
        super(RM_Enum_ADC0_SCANNSEL_CH11NSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNSEL_CH13NSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CH8 = 0x00000000
        zz_edict['CH8'] = self.CH8
        zz_desc['CH8'] = ""
        self.CH10 = 0x00000001
        zz_edict['CH10'] = self.CH10
        zz_desc['CH10'] = ""
        self.CH12 = 0x00000002
        zz_edict['CH12'] = self.CH12
        zz_desc['CH12'] = ""
        self.CH14 = 0x00000003
        zz_edict['CH14'] = self.CH14
        zz_desc['CH14'] = ""
        super(RM_Enum_ADC0_SCANNSEL_CH13NSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ADC0_SCANNSEL_CH15NSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CH8 = 0x00000000
        zz_edict['CH8'] = self.CH8
        zz_desc['CH8'] = ""
        self.CH10 = 0x00000001
        zz_edict['CH10'] = self.CH10
        zz_desc['CH10'] = ""
        self.CH12 = 0x00000002
        zz_edict['CH12'] = self.CH12
        zz_desc['CH12'] = ""
        self.CH14 = 0x00000003
        zz_edict['CH14'] = self.CH14
        zz_desc['CH14'] = ""
        super(RM_Enum_ADC0_SCANNSEL_CH15NSEL, self).__init__(
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


