
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_ACMP1_CTRL_REFRESHRATE(Base_RM_Enum):
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
        super(RM_Enum_ACMP1_CTRL_REFRESHRATE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ACMP1_CTRL_PWRSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.AVDD = 0x00000000
        zz_edict['AVDD'] = self.AVDD
        zz_desc['AVDD'] = ""
        self.VREGVDD = 0x00000001
        zz_edict['VREGVDD'] = self.VREGVDD
        zz_desc['VREGVDD'] = ""
        self.IOVDD0 = 0x00000002
        zz_edict['IOVDD0'] = self.IOVDD0
        zz_desc['IOVDD0'] = ""
        self.IOVDD1 = 0x00000004
        zz_edict['IOVDD1'] = self.IOVDD1
        zz_desc['IOVDD1'] = ""
        super(RM_Enum_ACMP1_CTRL_PWRSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ACMP1_CTRL_INPUTRANGE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.FULL = 0x00000000
        zz_edict['FULL'] = self.FULL
        zz_desc['FULL'] = ""
        self.GTVDDDIV2 = 0x00000001
        zz_edict['GTVDDDIV2'] = self.GTVDDDIV2
        zz_desc['GTVDDDIV2'] = ""
        self.LTVDDDIV2 = 0x00000002
        zz_edict['LTVDDDIV2'] = self.LTVDDDIV2
        zz_desc['LTVDDDIV2'] = ""
        super(RM_Enum_ACMP1_CTRL_INPUTRANGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ACMP1_INPUTSEL_VASEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.VDD = 0x00000000
        zz_edict['VDD'] = self.VDD
        zz_desc['VDD'] = ""
        self.APORT2YCH0 = 0x00000001
        zz_edict['APORT2YCH0'] = self.APORT2YCH0
        zz_desc['APORT2YCH0'] = ""
        self.APORT2YCH2 = 0x00000003
        zz_edict['APORT2YCH2'] = self.APORT2YCH2
        zz_desc['APORT2YCH2'] = ""
        self.APORT2YCH4 = 0x00000005
        zz_edict['APORT2YCH4'] = self.APORT2YCH4
        zz_desc['APORT2YCH4'] = ""
        self.APORT2YCH6 = 0x00000007
        zz_edict['APORT2YCH6'] = self.APORT2YCH6
        zz_desc['APORT2YCH6'] = ""
        self.APORT2YCH8 = 0x00000009
        zz_edict['APORT2YCH8'] = self.APORT2YCH8
        zz_desc['APORT2YCH8'] = ""
        self.APORT2YCH10 = 0x0000000B
        zz_edict['APORT2YCH10'] = self.APORT2YCH10
        zz_desc['APORT2YCH10'] = ""
        self.APORT2YCH12 = 0x0000000D
        zz_edict['APORT2YCH12'] = self.APORT2YCH12
        zz_desc['APORT2YCH12'] = ""
        self.APORT2YCH14 = 0x0000000F
        zz_edict['APORT2YCH14'] = self.APORT2YCH14
        zz_desc['APORT2YCH14'] = ""
        self.APORT2YCH16 = 0x00000011
        zz_edict['APORT2YCH16'] = self.APORT2YCH16
        zz_desc['APORT2YCH16'] = ""
        self.APORT2YCH18 = 0x00000013
        zz_edict['APORT2YCH18'] = self.APORT2YCH18
        zz_desc['APORT2YCH18'] = ""
        self.APORT2YCH20 = 0x00000015
        zz_edict['APORT2YCH20'] = self.APORT2YCH20
        zz_desc['APORT2YCH20'] = ""
        self.APORT2YCH22 = 0x00000017
        zz_edict['APORT2YCH22'] = self.APORT2YCH22
        zz_desc['APORT2YCH22'] = ""
        self.APORT2YCH24 = 0x00000019
        zz_edict['APORT2YCH24'] = self.APORT2YCH24
        zz_desc['APORT2YCH24'] = ""
        self.APORT2YCH26 = 0x0000001B
        zz_edict['APORT2YCH26'] = self.APORT2YCH26
        zz_desc['APORT2YCH26'] = ""
        self.APORT2YCH28 = 0x0000001D
        zz_edict['APORT2YCH28'] = self.APORT2YCH28
        zz_desc['APORT2YCH28'] = ""
        self.APORT2YCH30 = 0x0000001F
        zz_edict['APORT2YCH30'] = self.APORT2YCH30
        zz_desc['APORT2YCH30'] = ""
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
        super(RM_Enum_ACMP1_INPUTSEL_VASEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ACMP1_INPUTSEL_CSRESSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.RES0 = 0x00000000
        zz_edict['RES0'] = self.RES0
        zz_desc['RES0'] = ""
        self.RES1 = 0x00000001
        zz_edict['RES1'] = self.RES1
        zz_desc['RES1'] = ""
        self.RES2 = 0x00000002
        zz_edict['RES2'] = self.RES2
        zz_desc['RES2'] = ""
        self.RES3 = 0x00000003
        zz_edict['RES3'] = self.RES3
        zz_desc['RES3'] = ""
        self.RES4 = 0x00000004
        zz_edict['RES4'] = self.RES4
        zz_desc['RES4'] = ""
        self.RES5 = 0x00000005
        zz_edict['RES5'] = self.RES5
        zz_desc['RES5'] = ""
        self.RES6 = 0x00000006
        zz_edict['RES6'] = self.RES6
        zz_desc['RES6'] = ""
        self.RES7 = 0x00000007
        zz_edict['RES7'] = self.RES7
        zz_desc['RES7'] = ""
        super(RM_Enum_ACMP1_INPUTSEL_CSRESSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ACMP1_HYSTERESIS0_HYST(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.HYST0 = 0x00000000
        zz_edict['HYST0'] = self.HYST0
        zz_desc['HYST0'] = ""
        self.HYST1 = 0x00000001
        zz_edict['HYST1'] = self.HYST1
        zz_desc['HYST1'] = ""
        self.HYST2 = 0x00000002
        zz_edict['HYST2'] = self.HYST2
        zz_desc['HYST2'] = ""
        self.HYST3 = 0x00000003
        zz_edict['HYST3'] = self.HYST3
        zz_desc['HYST3'] = ""
        self.HYST4 = 0x00000004
        zz_edict['HYST4'] = self.HYST4
        zz_desc['HYST4'] = ""
        self.HYST5 = 0x00000005
        zz_edict['HYST5'] = self.HYST5
        zz_desc['HYST5'] = ""
        self.HYST6 = 0x00000006
        zz_edict['HYST6'] = self.HYST6
        zz_desc['HYST6'] = ""
        self.HYST7 = 0x00000007
        zz_edict['HYST7'] = self.HYST7
        zz_desc['HYST7'] = ""
        self.HYST8 = 0x00000008
        zz_edict['HYST8'] = self.HYST8
        zz_desc['HYST8'] = ""
        self.HYST9 = 0x00000009
        zz_edict['HYST9'] = self.HYST9
        zz_desc['HYST9'] = ""
        self.HYST10 = 0x0000000A
        zz_edict['HYST10'] = self.HYST10
        zz_desc['HYST10'] = ""
        self.HYST11 = 0x0000000B
        zz_edict['HYST11'] = self.HYST11
        zz_desc['HYST11'] = ""
        self.HYST12 = 0x0000000C
        zz_edict['HYST12'] = self.HYST12
        zz_desc['HYST12'] = ""
        self.HYST13 = 0x0000000D
        zz_edict['HYST13'] = self.HYST13
        zz_desc['HYST13'] = ""
        self.HYST14 = 0x0000000E
        zz_edict['HYST14'] = self.HYST14
        zz_desc['HYST14'] = ""
        self.HYST15 = 0x0000000F
        zz_edict['HYST15'] = self.HYST15
        zz_desc['HYST15'] = ""
        super(RM_Enum_ACMP1_HYSTERESIS0_HYST, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ACMP1_HYSTERESIS1_HYST(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.HYST0 = 0x00000000
        zz_edict['HYST0'] = self.HYST0
        zz_desc['HYST0'] = ""
        self.HYST1 = 0x00000001
        zz_edict['HYST1'] = self.HYST1
        zz_desc['HYST1'] = ""
        self.HYST2 = 0x00000002
        zz_edict['HYST2'] = self.HYST2
        zz_desc['HYST2'] = ""
        self.HYST3 = 0x00000003
        zz_edict['HYST3'] = self.HYST3
        zz_desc['HYST3'] = ""
        self.HYST4 = 0x00000004
        zz_edict['HYST4'] = self.HYST4
        zz_desc['HYST4'] = ""
        self.HYST5 = 0x00000005
        zz_edict['HYST5'] = self.HYST5
        zz_desc['HYST5'] = ""
        self.HYST6 = 0x00000006
        zz_edict['HYST6'] = self.HYST6
        zz_desc['HYST6'] = ""
        self.HYST7 = 0x00000007
        zz_edict['HYST7'] = self.HYST7
        zz_desc['HYST7'] = ""
        self.HYST8 = 0x00000008
        zz_edict['HYST8'] = self.HYST8
        zz_desc['HYST8'] = ""
        self.HYST9 = 0x00000009
        zz_edict['HYST9'] = self.HYST9
        zz_desc['HYST9'] = ""
        self.HYST10 = 0x0000000A
        zz_edict['HYST10'] = self.HYST10
        zz_desc['HYST10'] = ""
        self.HYST11 = 0x0000000B
        zz_edict['HYST11'] = self.HYST11
        zz_desc['HYST11'] = ""
        self.HYST12 = 0x0000000C
        zz_edict['HYST12'] = self.HYST12
        zz_desc['HYST12'] = ""
        self.HYST13 = 0x0000000D
        zz_edict['HYST13'] = self.HYST13
        zz_desc['HYST13'] = ""
        self.HYST14 = 0x0000000E
        zz_edict['HYST14'] = self.HYST14
        zz_desc['HYST14'] = ""
        self.HYST15 = 0x0000000F
        zz_edict['HYST15'] = self.HYST15
        zz_desc['HYST15'] = ""
        super(RM_Enum_ACMP1_HYSTERESIS1_HYST, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ACMP1_ROUTELOC0_OUTLOC(Base_RM_Enum):
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
        super(RM_Enum_ACMP1_ROUTELOC0_OUTLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ACMP1_EXTIFCTRL_APORTSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.APORT0X = 0x00000000
        zz_edict['APORT0X'] = self.APORT0X
        zz_desc['APORT0X'] = ""
        self.APORT0Y = 0x00000001
        zz_edict['APORT0Y'] = self.APORT0Y
        zz_desc['APORT0Y'] = ""
        self.APORT1X = 0x00000002
        zz_edict['APORT1X'] = self.APORT1X
        zz_desc['APORT1X'] = ""
        self.APORT1Y = 0x00000003
        zz_edict['APORT1Y'] = self.APORT1Y
        zz_desc['APORT1Y'] = ""
        self.APORT1XY = 0x00000004
        zz_edict['APORT1XY'] = self.APORT1XY
        zz_desc['APORT1XY'] = ""
        self.APORT2X = 0x00000005
        zz_edict['APORT2X'] = self.APORT2X
        zz_desc['APORT2X'] = ""
        self.APORT2Y = 0x00000006
        zz_edict['APORT2Y'] = self.APORT2Y
        zz_desc['APORT2Y'] = ""
        self.APORT2YX = 0x00000007
        zz_edict['APORT2YX'] = self.APORT2YX
        zz_desc['APORT2YX'] = ""
        self.APORT3X = 0x00000008
        zz_edict['APORT3X'] = self.APORT3X
        zz_desc['APORT3X'] = ""
        self.APORT3Y = 0x00000009
        zz_edict['APORT3Y'] = self.APORT3Y
        zz_desc['APORT3Y'] = ""
        self.APORT3XY = 0x0000000A
        zz_edict['APORT3XY'] = self.APORT3XY
        zz_desc['APORT3XY'] = ""
        self.APORT4X = 0x0000000B
        zz_edict['APORT4X'] = self.APORT4X
        zz_desc['APORT4X'] = ""
        self.APORT4Y = 0x0000000C
        zz_edict['APORT4Y'] = self.APORT4Y
        zz_desc['APORT4Y'] = ""
        self.APORT4YX = 0x0000000D
        zz_edict['APORT4YX'] = self.APORT4YX
        zz_desc['APORT4YX'] = ""
        super(RM_Enum_ACMP1_EXTIFCTRL_APORTSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


