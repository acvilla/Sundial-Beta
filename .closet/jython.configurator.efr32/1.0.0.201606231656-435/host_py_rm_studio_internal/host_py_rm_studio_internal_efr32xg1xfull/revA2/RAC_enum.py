
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_RAC_RXENSRCEN_PRSRXENSEL(Base_RM_Enum):
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
        super(RM_Enum_RAC_RXENSRCEN_PRSRXENSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_STATUS_STATE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.OFF = 0x00000000
        zz_edict['OFF'] = self.OFF
        zz_desc['OFF'] = ""
        self.RXWARM = 0x00000001
        zz_edict['RXWARM'] = self.RXWARM
        zz_desc['RXWARM'] = ""
        self.RXSEARCH = 0x00000002
        zz_edict['RXSEARCH'] = self.RXSEARCH
        zz_desc['RXSEARCH'] = ""
        self.RXFRAME = 0x00000003
        zz_edict['RXFRAME'] = self.RXFRAME
        zz_desc['RXFRAME'] = ""
        self.RXPD = 0x00000004
        zz_edict['RXPD'] = self.RXPD
        zz_desc['RXPD'] = ""
        self.RX2RX = 0x00000005
        zz_edict['RX2RX'] = self.RX2RX
        zz_desc['RX2RX'] = ""
        self.RXOVERFLOW = 0x00000006
        zz_edict['RXOVERFLOW'] = self.RXOVERFLOW
        zz_desc['RXOVERFLOW'] = ""
        self.RX2TX = 0x00000007
        zz_edict['RX2TX'] = self.RX2TX
        zz_desc['RX2TX'] = ""
        self.TXWARM = 0x00000008
        zz_edict['TXWARM'] = self.TXWARM
        zz_desc['TXWARM'] = ""
        self.TX = 0x00000009
        zz_edict['TX'] = self.TX
        zz_desc['TX'] = ""
        self.TXPD = 0x0000000A
        zz_edict['TXPD'] = self.TXPD
        zz_desc['TXPD'] = ""
        self.TX2RX = 0x0000000B
        zz_edict['TX2RX'] = self.TX2RX
        zz_desc['TX2RX'] = ""
        self.TX2TX = 0x0000000C
        zz_edict['TX2TX'] = self.TX2TX
        zz_desc['TX2TX'] = ""
        self.SHUTDOWN = 0x0000000D
        zz_edict['SHUTDOWN'] = self.SHUTDOWN
        zz_desc['SHUTDOWN'] = ""
        super(RM_Enum_RAC_STATUS_STATE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_CTRL_PRSRXDISSEL(Base_RM_Enum):
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
        super(RM_Enum_RAC_CTRL_PRSRXDISSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_CTRL_PRSFORCETXSEL(Base_RM_Enum):
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
        super(RM_Enum_RAC_CTRL_PRSFORCETXSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_CTRL_PRSTXENSEL(Base_RM_Enum):
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
        super(RM_Enum_RAC_CTRL_PRSTXENSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_CTRL_PRSCLRSEL(Base_RM_Enum):
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
        super(RM_Enum_RAC_CTRL_PRSCLRSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_LVDSCTRL_LVDSCURR(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_LVDSCTRL_LVDSCURR, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_LVDSCTRL_LVDSCMCONFIG(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_LVDSCTRL_LVDSCMCONFIG, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SEQCTRL_COMPINVALMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NEVER = 0x00000000
        zz_edict['NEVER'] = self.NEVER
        zz_desc['NEVER'] = ""
        self.STATECHANGE = 0x00000001
        zz_edict['STATECHANGE'] = self.STATECHANGE
        zz_desc['STATECHANGE'] = ""
        self.COMPEVENT = 0x00000002
        zz_edict['COMPEVENT'] = self.COMPEVENT
        zz_desc['COMPEVENT'] = ""
        self.STATECOMP = 0x00000003
        zz_edict['STATECOMP'] = self.STATECOMP
        zz_desc['STATECOMP'] = ""
        super(RM_Enum_RAC_SEQCTRL_COMPINVALMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SEQCTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_RAC_SEQCTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_LPFCTRL_LPFBW(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        #print("WARNING: Aliasing enum '8' to 'E8'")
        self.E8 = 0x00000008
        zz_edict['E8'] = self.E8
        zz_desc['E8'] = ""
        #print("WARNING: Aliasing enum '9' to 'E9'")
        self.E9 = 0x00000009
        zz_edict['E9'] = self.E9
        zz_desc['E9'] = ""
        #print("WARNING: Aliasing enum '10' to 'E10'")
        self.E10 = 0x0000000A
        zz_edict['E10'] = self.E10
        zz_desc['E10'] = ""
        #print("WARNING: Aliasing enum '11' to 'E11'")
        self.E11 = 0x0000000B
        zz_edict['E11'] = self.E11
        zz_desc['E11'] = ""
        #print("WARNING: Aliasing enum '12' to 'E12'")
        self.E12 = 0x0000000C
        zz_edict['E12'] = self.E12
        zz_desc['E12'] = ""
        #print("WARNING: Aliasing enum '13' to 'E13'")
        self.E13 = 0x0000000D
        zz_edict['E13'] = self.E13
        zz_desc['E13'] = ""
        #print("WARNING: Aliasing enum '14' to 'E14'")
        self.E14 = 0x0000000E
        zz_edict['E14'] = self.E14
        zz_desc['E14'] = ""
        #print("WARNING: Aliasing enum '15' to 'E15'")
        self.E15 = 0x0000000F
        zz_edict['E15'] = self.E15
        zz_desc['E15'] = ""
        super(RM_Enum_RAC_LPFCTRL_LPFBW, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_AUXCTRL_LODIVSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.RX = 0x00000001
        zz_edict['RX'] = self.RX
        zz_desc['RX'] = ""
        self.SGRX = 0x00000002
        zz_edict['SGRX'] = self.SGRX
        zz_desc['SGRX'] = ""
        self.TX = 0x00000003
        zz_edict['TX'] = self.TX
        zz_desc['TX'] = ""
        self.LVDS = 0x00000004
        zz_edict['LVDS'] = self.LVDS
        zz_desc['LVDS'] = ""
        super(RM_Enum_RAC_AUXCTRL_LODIVSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PACTRL0_CASCODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.EN1SLICE = 0x00000001
        zz_edict['EN1SLICE'] = self.EN1SLICE
        zz_desc['EN1SLICE'] = ""
        self.EN2SLICES = 0x00000003
        zz_edict['EN2SLICES'] = self.EN2SLICES
        zz_desc['EN2SLICES'] = ""
        self.EN3SLICES = 0x00000007
        zz_edict['EN3SLICES'] = self.EN3SLICES
        zz_desc['EN3SLICES'] = ""
        self.EN4SLICES = 0x0000000F
        zz_edict['EN4SLICES'] = self.EN4SLICES
        zz_desc['EN4SLICES'] = ""
        self.EN5SLICES = 0x0000001F
        zz_edict['EN5SLICES'] = self.EN5SLICES
        zz_desc['EN5SLICES'] = ""
        self.EN6SLICES = 0x0000003F
        zz_edict['EN6SLICES'] = self.EN6SLICES
        zz_desc['EN6SLICES'] = ""
        self.EN7SLICES = 0x0000007F
        zz_edict['EN7SLICES'] = self.EN7SLICES
        zz_desc['EN7SLICES'] = ""
        self.EN8SLICES = 0x000000FF
        zz_edict['EN8SLICES'] = self.EN8SLICES
        zz_desc['EN8SLICES'] = ""
        super(RM_Enum_RAC_PACTRL0_CASCODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PACTRL0_SLICE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.EN1SLICE = 0x00000001
        zz_edict['EN1SLICE'] = self.EN1SLICE
        zz_desc['EN1SLICE'] = ""
        self.EN2SLICES = 0x00000003
        zz_edict['EN2SLICES'] = self.EN2SLICES
        zz_desc['EN2SLICES'] = ""
        self.EN3SLICES = 0x00000007
        zz_edict['EN3SLICES'] = self.EN3SLICES
        zz_desc['EN3SLICES'] = ""
        self.EN4SLICES = 0x0000000F
        zz_edict['EN4SLICES'] = self.EN4SLICES
        zz_desc['EN4SLICES'] = ""
        self.EN5SLICES = 0x0000001F
        zz_edict['EN5SLICES'] = self.EN5SLICES
        zz_desc['EN5SLICES'] = ""
        self.EN6SLICES = 0x0000003F
        zz_edict['EN6SLICES'] = self.EN6SLICES
        zz_desc['EN6SLICES'] = ""
        self.EN7SLICES = 0x0000007F
        zz_edict['EN7SLICES'] = self.EN7SLICES
        zz_desc['EN7SLICES'] = ""
        self.EN8SLICES = 0x000000FF
        zz_edict['EN8SLICES'] = self.EN8SLICES
        zz_desc['EN8SLICES'] = ""
        super(RM_Enum_RAC_PACTRL0_SLICE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PACTRL0_STRIPE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.EN1STRIPE = 0x00000001
        zz_edict['EN1STRIPE'] = self.EN1STRIPE
        zz_desc['EN1STRIPE'] = ""
        self.EN2STRIPES = 0x00000002
        zz_edict['EN2STRIPES'] = self.EN2STRIPES
        zz_desc['EN2STRIPES'] = ""
        self.EN3STRIPES = 0x00000003
        zz_edict['EN3STRIPES'] = self.EN3STRIPES
        zz_desc['EN3STRIPES'] = ""
        self.EN4STRIPES = 0x00000004
        zz_edict['EN4STRIPES'] = self.EN4STRIPES
        zz_desc['EN4STRIPES'] = ""
        self.EN31STRIPES = 0x0000001F
        zz_edict['EN31STRIPES'] = self.EN31STRIPES
        zz_desc['EN31STRIPES'] = ""
        super(RM_Enum_RAC_PACTRL0_STRIPE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PAPKDCTRL_VTLSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        #print("WARNING: Aliasing enum '8' to 'E8'")
        self.E8 = 0x00000008
        zz_edict['E8'] = self.E8
        zz_desc['E8'] = ""
        #print("WARNING: Aliasing enum '9' to 'E9'")
        self.E9 = 0x00000009
        zz_edict['E9'] = self.E9
        zz_desc['E9'] = ""
        #print("WARNING: Aliasing enum '10' to 'E10'")
        self.E10 = 0x0000000A
        zz_edict['E10'] = self.E10
        zz_desc['E10'] = ""
        #print("WARNING: Aliasing enum '11' to 'E11'")
        self.E11 = 0x0000000B
        zz_edict['E11'] = self.E11
        zz_desc['E11'] = ""
        #print("WARNING: Aliasing enum '12' to 'E12'")
        self.E12 = 0x0000000C
        zz_edict['E12'] = self.E12
        zz_desc['E12'] = ""
        #print("WARNING: Aliasing enum '13' to 'E13'")
        self.E13 = 0x0000000D
        zz_edict['E13'] = self.E13
        zz_desc['E13'] = ""
        #print("WARNING: Aliasing enum '14' to 'E14'")
        self.E14 = 0x0000000E
        zz_edict['E14'] = self.E14
        zz_desc['E14'] = ""
        #print("WARNING: Aliasing enum '15' to 'E15'")
        self.E15 = 0x0000000F
        zz_edict['E15'] = self.E15
        zz_desc['E15'] = ""
        #print("WARNING: Aliasing enum '16' to 'E16'")
        self.E16 = 0x00000010
        zz_edict['E16'] = self.E16
        zz_desc['E16'] = ""
        #print("WARNING: Aliasing enum '17' to 'E17'")
        self.E17 = 0x00000011
        zz_edict['E17'] = self.E17
        zz_desc['E17'] = ""
        #print("WARNING: Aliasing enum '18' to 'E18'")
        self.E18 = 0x00000012
        zz_edict['E18'] = self.E18
        zz_desc['E18'] = ""
        #print("WARNING: Aliasing enum '19' to 'E19'")
        self.E19 = 0x00000013
        zz_edict['E19'] = self.E19
        zz_desc['E19'] = ""
        #print("WARNING: Aliasing enum '20' to 'E20'")
        self.E20 = 0x00000014
        zz_edict['E20'] = self.E20
        zz_desc['E20'] = ""
        #print("WARNING: Aliasing enum '21' to 'E21'")
        self.E21 = 0x00000015
        zz_edict['E21'] = self.E21
        zz_desc['E21'] = ""
        #print("WARNING: Aliasing enum '22' to 'E22'")
        self.E22 = 0x00000016
        zz_edict['E22'] = self.E22
        zz_desc['E22'] = ""
        #print("WARNING: Aliasing enum '23' to 'E23'")
        self.E23 = 0x00000017
        zz_edict['E23'] = self.E23
        zz_desc['E23'] = ""
        super(RM_Enum_RAC_PAPKDCTRL_VTLSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PAPKDCTRL_VTHSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        #print("WARNING: Aliasing enum '8' to 'E8'")
        self.E8 = 0x00000008
        zz_edict['E8'] = self.E8
        zz_desc['E8'] = ""
        #print("WARNING: Aliasing enum '9' to 'E9'")
        self.E9 = 0x00000009
        zz_edict['E9'] = self.E9
        zz_desc['E9'] = ""
        #print("WARNING: Aliasing enum '10' to 'E10'")
        self.E10 = 0x0000000A
        zz_edict['E10'] = self.E10
        zz_desc['E10'] = ""
        #print("WARNING: Aliasing enum '11' to 'E11'")
        self.E11 = 0x0000000B
        zz_edict['E11'] = self.E11
        zz_desc['E11'] = ""
        #print("WARNING: Aliasing enum '12' to 'E12'")
        self.E12 = 0x0000000C
        zz_edict['E12'] = self.E12
        zz_desc['E12'] = ""
        #print("WARNING: Aliasing enum '13' to 'E13'")
        self.E13 = 0x0000000D
        zz_edict['E13'] = self.E13
        zz_desc['E13'] = ""
        #print("WARNING: Aliasing enum '14' to 'E14'")
        self.E14 = 0x0000000E
        zz_edict['E14'] = self.E14
        zz_desc['E14'] = ""
        #print("WARNING: Aliasing enum '15' to 'E15'")
        self.E15 = 0x0000000F
        zz_edict['E15'] = self.E15
        zz_desc['E15'] = ""
        #print("WARNING: Aliasing enum '16' to 'E16'")
        self.E16 = 0x00000010
        zz_edict['E16'] = self.E16
        zz_desc['E16'] = ""
        #print("WARNING: Aliasing enum '17' to 'E17'")
        self.E17 = 0x00000011
        zz_edict['E17'] = self.E17
        zz_desc['E17'] = ""
        #print("WARNING: Aliasing enum '18' to 'E18'")
        self.E18 = 0x00000012
        zz_edict['E18'] = self.E18
        zz_desc['E18'] = ""
        #print("WARNING: Aliasing enum '19' to 'E19'")
        self.E19 = 0x00000013
        zz_edict['E19'] = self.E19
        zz_desc['E19'] = ""
        #print("WARNING: Aliasing enum '20' to 'E20'")
        self.E20 = 0x00000014
        zz_edict['E20'] = self.E20
        zz_desc['E20'] = ""
        #print("WARNING: Aliasing enum '21' to 'E21'")
        self.E21 = 0x00000015
        zz_edict['E21'] = self.E21
        zz_desc['E21'] = ""
        #print("WARNING: Aliasing enum '22' to 'E22'")
        self.E22 = 0x00000016
        zz_edict['E22'] = self.E22
        zz_desc['E22'] = ""
        #print("WARNING: Aliasing enum '23' to 'E23'")
        self.E23 = 0x00000017
        zz_edict['E23'] = self.E23
        zz_desc['E23'] = ""
        super(RM_Enum_RAC_PAPKDCTRL_VTHSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PAPKDCTRL_CAPSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_PAPKDCTRL_CAPSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PAPKDCTRL_I2VCM(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_PAPKDCTRL_I2VCM, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PAPKDCTRL_PKDBIASTH(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        super(RM_Enum_RAC_PAPKDCTRL_PKDBIASTH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PABIASCTRL0_PABIAS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_PABIASCTRL0_PABIAS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PABIASCTRL0_BUF0BIAS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_PABIASCTRL0_BUF0BIAS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PABIASCTRL0_BUF12BIAS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_PABIASCTRL0_BUF12BIAS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PABIASCTRL1_VLDO(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        super(RM_Enum_RAC_PABIASCTRL1_VLDO, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PABIASCTRL1_VLDOFB(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_PABIASCTRL1_VLDOFB, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PABIASCTRL1_VCASCODEHV(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        super(RM_Enum_RAC_PABIASCTRL1_VCASCODEHV, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PABIASCTRL1_VCASCODELV(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        super(RM_Enum_RAC_PABIASCTRL1_VCASCODELV, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PABIASCTRL1_2P4VDDPATHRESHOLD(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_PABIASCTRL1_2P4VDDPATHRESHOLD, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPACTRL0_CASCODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.EN1SLICE = 0x00000001
        zz_edict['EN1SLICE'] = self.EN1SLICE
        zz_desc['EN1SLICE'] = ""
        self.EN2SLICES = 0x00000003
        zz_edict['EN2SLICES'] = self.EN2SLICES
        zz_desc['EN2SLICES'] = ""
        self.EN3SLICES = 0x00000007
        zz_edict['EN3SLICES'] = self.EN3SLICES
        zz_desc['EN3SLICES'] = ""
        self.EN4SLICES = 0x0000000F
        zz_edict['EN4SLICES'] = self.EN4SLICES
        zz_desc['EN4SLICES'] = ""
        self.EN5SLICES = 0x0000001F
        zz_edict['EN5SLICES'] = self.EN5SLICES
        zz_desc['EN5SLICES'] = ""
        self.EN6SLICES = 0x0000003F
        zz_edict['EN6SLICES'] = self.EN6SLICES
        zz_desc['EN6SLICES'] = ""
        self.EN7SLICES = 0x0000007F
        zz_edict['EN7SLICES'] = self.EN7SLICES
        zz_desc['EN7SLICES'] = ""
        self.EN8SLICES = 0x000000FF
        zz_edict['EN8SLICES'] = self.EN8SLICES
        zz_desc['EN8SLICES'] = ""
        super(RM_Enum_RAC_SGPACTRL0_CASCODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPACTRL0_SLICE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.EN1SLICE = 0x00000001
        zz_edict['EN1SLICE'] = self.EN1SLICE
        zz_desc['EN1SLICE'] = ""
        self.EN2SLICES = 0x00000003
        zz_edict['EN2SLICES'] = self.EN2SLICES
        zz_desc['EN2SLICES'] = ""
        self.EN3SLICES = 0x00000007
        zz_edict['EN3SLICES'] = self.EN3SLICES
        zz_desc['EN3SLICES'] = ""
        self.EN4SLICES = 0x0000000F
        zz_edict['EN4SLICES'] = self.EN4SLICES
        zz_desc['EN4SLICES'] = ""
        self.EN5SLICES = 0x0000001F
        zz_edict['EN5SLICES'] = self.EN5SLICES
        zz_desc['EN5SLICES'] = ""
        self.EN6SLICES = 0x0000003F
        zz_edict['EN6SLICES'] = self.EN6SLICES
        zz_desc['EN6SLICES'] = ""
        self.EN7SLICES = 0x0000007F
        zz_edict['EN7SLICES'] = self.EN7SLICES
        zz_desc['EN7SLICES'] = ""
        self.EN8SLICES = 0x000000FF
        zz_edict['EN8SLICES'] = self.EN8SLICES
        zz_desc['EN8SLICES'] = ""
        super(RM_Enum_RAC_SGPACTRL0_SLICE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPACTRL0_STRIPE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.EN1STRIPE = 0x00000001
        zz_edict['EN1STRIPE'] = self.EN1STRIPE
        zz_desc['EN1STRIPE'] = ""
        self.EN2STRIPES = 0x00000002
        zz_edict['EN2STRIPES'] = self.EN2STRIPES
        zz_desc['EN2STRIPES'] = ""
        self.EN3STRIPES = 0x00000003
        zz_edict['EN3STRIPES'] = self.EN3STRIPES
        zz_desc['EN3STRIPES'] = ""
        self.EN4STRIPES = 0x00000004
        zz_edict['EN4STRIPES'] = self.EN4STRIPES
        zz_desc['EN4STRIPES'] = ""
        self.EN31STRIPES = 0x0000001F
        zz_edict['EN31STRIPES'] = self.EN31STRIPES
        zz_desc['EN31STRIPES'] = ""
        super(RM_Enum_RAC_SGPACTRL0_STRIPE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPAPKDCTRL_VTLSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        #print("WARNING: Aliasing enum '8' to 'E8'")
        self.E8 = 0x00000008
        zz_edict['E8'] = self.E8
        zz_desc['E8'] = ""
        #print("WARNING: Aliasing enum '9' to 'E9'")
        self.E9 = 0x00000009
        zz_edict['E9'] = self.E9
        zz_desc['E9'] = ""
        #print("WARNING: Aliasing enum '10' to 'E10'")
        self.E10 = 0x0000000A
        zz_edict['E10'] = self.E10
        zz_desc['E10'] = ""
        #print("WARNING: Aliasing enum '11' to 'E11'")
        self.E11 = 0x0000000B
        zz_edict['E11'] = self.E11
        zz_desc['E11'] = ""
        #print("WARNING: Aliasing enum '12' to 'E12'")
        self.E12 = 0x0000000C
        zz_edict['E12'] = self.E12
        zz_desc['E12'] = ""
        #print("WARNING: Aliasing enum '13' to 'E13'")
        self.E13 = 0x0000000D
        zz_edict['E13'] = self.E13
        zz_desc['E13'] = ""
        #print("WARNING: Aliasing enum '14' to 'E14'")
        self.E14 = 0x0000000E
        zz_edict['E14'] = self.E14
        zz_desc['E14'] = ""
        #print("WARNING: Aliasing enum '15' to 'E15'")
        self.E15 = 0x0000000F
        zz_edict['E15'] = self.E15
        zz_desc['E15'] = ""
        #print("WARNING: Aliasing enum '16' to 'E16'")
        self.E16 = 0x00000010
        zz_edict['E16'] = self.E16
        zz_desc['E16'] = ""
        #print("WARNING: Aliasing enum '17' to 'E17'")
        self.E17 = 0x00000011
        zz_edict['E17'] = self.E17
        zz_desc['E17'] = ""
        #print("WARNING: Aliasing enum '18' to 'E18'")
        self.E18 = 0x00000012
        zz_edict['E18'] = self.E18
        zz_desc['E18'] = ""
        #print("WARNING: Aliasing enum '19' to 'E19'")
        self.E19 = 0x00000013
        zz_edict['E19'] = self.E19
        zz_desc['E19'] = ""
        #print("WARNING: Aliasing enum '20' to 'E20'")
        self.E20 = 0x00000014
        zz_edict['E20'] = self.E20
        zz_desc['E20'] = ""
        #print("WARNING: Aliasing enum '21' to 'E21'")
        self.E21 = 0x00000015
        zz_edict['E21'] = self.E21
        zz_desc['E21'] = ""
        #print("WARNING: Aliasing enum '22' to 'E22'")
        self.E22 = 0x00000016
        zz_edict['E22'] = self.E22
        zz_desc['E22'] = ""
        #print("WARNING: Aliasing enum '23' to 'E23'")
        self.E23 = 0x00000017
        zz_edict['E23'] = self.E23
        zz_desc['E23'] = ""
        super(RM_Enum_RAC_SGPAPKDCTRL_VTLSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPAPKDCTRL_VTHSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        #print("WARNING: Aliasing enum '8' to 'E8'")
        self.E8 = 0x00000008
        zz_edict['E8'] = self.E8
        zz_desc['E8'] = ""
        #print("WARNING: Aliasing enum '9' to 'E9'")
        self.E9 = 0x00000009
        zz_edict['E9'] = self.E9
        zz_desc['E9'] = ""
        #print("WARNING: Aliasing enum '10' to 'E10'")
        self.E10 = 0x0000000A
        zz_edict['E10'] = self.E10
        zz_desc['E10'] = ""
        #print("WARNING: Aliasing enum '11' to 'E11'")
        self.E11 = 0x0000000B
        zz_edict['E11'] = self.E11
        zz_desc['E11'] = ""
        #print("WARNING: Aliasing enum '12' to 'E12'")
        self.E12 = 0x0000000C
        zz_edict['E12'] = self.E12
        zz_desc['E12'] = ""
        #print("WARNING: Aliasing enum '13' to 'E13'")
        self.E13 = 0x0000000D
        zz_edict['E13'] = self.E13
        zz_desc['E13'] = ""
        #print("WARNING: Aliasing enum '14' to 'E14'")
        self.E14 = 0x0000000E
        zz_edict['E14'] = self.E14
        zz_desc['E14'] = ""
        #print("WARNING: Aliasing enum '15' to 'E15'")
        self.E15 = 0x0000000F
        zz_edict['E15'] = self.E15
        zz_desc['E15'] = ""
        #print("WARNING: Aliasing enum '16' to 'E16'")
        self.E16 = 0x00000010
        zz_edict['E16'] = self.E16
        zz_desc['E16'] = ""
        #print("WARNING: Aliasing enum '17' to 'E17'")
        self.E17 = 0x00000011
        zz_edict['E17'] = self.E17
        zz_desc['E17'] = ""
        #print("WARNING: Aliasing enum '18' to 'E18'")
        self.E18 = 0x00000012
        zz_edict['E18'] = self.E18
        zz_desc['E18'] = ""
        #print("WARNING: Aliasing enum '19' to 'E19'")
        self.E19 = 0x00000013
        zz_edict['E19'] = self.E19
        zz_desc['E19'] = ""
        #print("WARNING: Aliasing enum '20' to 'E20'")
        self.E20 = 0x00000014
        zz_edict['E20'] = self.E20
        zz_desc['E20'] = ""
        #print("WARNING: Aliasing enum '21' to 'E21'")
        self.E21 = 0x00000015
        zz_edict['E21'] = self.E21
        zz_desc['E21'] = ""
        #print("WARNING: Aliasing enum '22' to 'E22'")
        self.E22 = 0x00000016
        zz_edict['E22'] = self.E22
        zz_desc['E22'] = ""
        #print("WARNING: Aliasing enum '23' to 'E23'")
        self.E23 = 0x00000017
        zz_edict['E23'] = self.E23
        zz_desc['E23'] = ""
        super(RM_Enum_RAC_SGPAPKDCTRL_VTHSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPAPKDCTRL_CAPSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_SGPAPKDCTRL_CAPSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPAPKDCTRL_I2VCM(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_SGPAPKDCTRL_I2VCM, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPAPKDCTRL_PKDBIASTH(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        super(RM_Enum_RAC_SGPAPKDCTRL_PKDBIASTH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPABIASCTRL0_PABIAS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_SGPABIASCTRL0_PABIAS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPABIASCTRL0_BUF0BIAS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_SGPABIASCTRL0_BUF0BIAS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPABIASCTRL0_BUF12BIAS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_SGPABIASCTRL0_BUF12BIAS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPABIASCTRL0_SGDACFILTBANDWIDTH(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        super(RM_Enum_RAC_SGPABIASCTRL0_SGDACFILTBANDWIDTH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPABIASCTRL1_VLDO(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        super(RM_Enum_RAC_SGPABIASCTRL1_VLDO, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPABIASCTRL1_VLDOFB(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_SGPABIASCTRL1_VLDOFB, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPABIASCTRL1_VCASCODEHV(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        super(RM_Enum_RAC_SGPABIASCTRL1_VCASCODEHV, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPABIASCTRL1_VCASCODELV(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        super(RM_Enum_RAC_SGPABIASCTRL1_VCASCODELV, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_SGPABIASCTRL1_SGVBATDETTHRESHOLD(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_SGPABIASCTRL1_SGVBATDETTHRESHOLD, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_IFPGACTRL_VLDO(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        super(RM_Enum_RAC_IFPGACTRL_VLDO, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_IFADCCTRL_VLDOSERIES(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        super(RM_Enum_RAC_IFADCCTRL_VLDOSERIES, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_IFADCCTRL_VLDOSHUNT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_IFADCCTRL_VLDOSHUNT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_IFADCCTRL_VLDOCLKGEN(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_IFADCCTRL_VLDOCLKGEN, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_IFADCCTRL_VCM(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        super(RM_Enum_RAC_IFADCCTRL_VCM, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_IFADCCTRL_OTA1CURRENT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_IFADCCTRL_OTA1CURRENT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_IFADCCTRL_OTA2CURRENT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_IFADCCTRL_OTA2CURRENT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_IFADCCTRL_OTA3CURRENT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        super(RM_Enum_RAC_IFADCCTRL_OTA3CURRENT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RAC_PACTUNECTRL_PACTUNE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0' to 'E0'")
        self.E0 = 0x00000000
        zz_edict['E0'] = self.E0
        zz_desc['E0'] = ""
        #print("WARNING: Aliasing enum '1' to 'E1'")
        self.E1 = 0x00000001
        zz_edict['E1'] = self.E1
        zz_desc['E1'] = ""
        #print("WARNING: Aliasing enum '2' to 'E2'")
        self.E2 = 0x00000002
        zz_edict['E2'] = self.E2
        zz_desc['E2'] = ""
        #print("WARNING: Aliasing enum '3' to 'E3'")
        self.E3 = 0x00000003
        zz_edict['E3'] = self.E3
        zz_desc['E3'] = ""
        #print("WARNING: Aliasing enum '4' to 'E4'")
        self.E4 = 0x00000004
        zz_edict['E4'] = self.E4
        zz_desc['E4'] = ""
        #print("WARNING: Aliasing enum '5' to 'E5'")
        self.E5 = 0x00000005
        zz_edict['E5'] = self.E5
        zz_desc['E5'] = ""
        #print("WARNING: Aliasing enum '6' to 'E6'")
        self.E6 = 0x00000006
        zz_edict['E6'] = self.E6
        zz_desc['E6'] = ""
        #print("WARNING: Aliasing enum '7' to 'E7'")
        self.E7 = 0x00000007
        zz_edict['E7'] = self.E7
        zz_desc['E7'] = ""
        super(RM_Enum_RAC_PACTUNECTRL_PACTUNE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


