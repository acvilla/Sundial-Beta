
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_VDAC0_CTRL_REFSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '1V25LN' to 'E1V25LN'")
        self.E1V25LN = 0x00000000
        zz_edict['E1V25LN'] = self.E1V25LN
        zz_desc['E1V25LN'] = ""
        #print("WARNING: Aliasing enum '2V5LN' to 'E2V5LN'")
        self.E2V5LN = 0x00000001
        zz_edict['E2V5LN'] = self.E2V5LN
        zz_desc['E2V5LN'] = ""
        #print("WARNING: Aliasing enum '1V25' to 'E1V25'")
        self.E1V25 = 0x00000002
        zz_edict['E1V25'] = self.E1V25
        zz_desc['E1V25'] = ""
        #print("WARNING: Aliasing enum '2V5' to 'E2V5'")
        self.E2V5 = 0x00000003
        zz_edict['E2V5'] = self.E2V5
        zz_desc['E2V5'] = ""
        self.VDD = 0x00000004
        zz_edict['VDD'] = self.VDD
        zz_desc['VDD'] = ""
        self.VDDALT = 0x00000005
        zz_edict['VDDALT'] = self.VDDALT
        zz_desc['VDDALT'] = ""
        self.EXT = 0x00000006
        zz_edict['EXT'] = self.EXT
        zz_desc['EXT'] = ""
        super(RM_Enum_VDAC0_CTRL_REFSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_CTRL_PRESC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NODIVISION = 0x00000000
        zz_edict['NODIVISION'] = self.NODIVISION
        zz_desc['NODIVISION'] = ""
        super(RM_Enum_VDAC0_CTRL_PRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_CTRL_REFRESHPERIOD(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '8CYCLES' to 'E8CYCLES'")
        self.E8CYCLES = 0x00000000
        zz_edict['E8CYCLES'] = self.E8CYCLES
        zz_desc['E8CYCLES'] = ""
        #print("WARNING: Aliasing enum '16CYCLES' to 'E16CYCLES'")
        self.E16CYCLES = 0x00000001
        zz_edict['E16CYCLES'] = self.E16CYCLES
        zz_desc['E16CYCLES'] = ""
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000002
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        #print("WARNING: Aliasing enum '64CYCLES' to 'E64CYCLES'")
        self.E64CYCLES = 0x00000003
        zz_edict['E64CYCLES'] = self.E64CYCLES
        zz_desc['E64CYCLES'] = ""
        super(RM_Enum_VDAC0_CTRL_REFRESHPERIOD, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_CH0CTRL_TRIGMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.SW = 0x00000000
        zz_edict['SW'] = self.SW
        zz_desc['SW'] = ""
        self.PRS = 0x00000001
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.REFRESH = 0x00000002
        zz_edict['REFRESH'] = self.REFRESH
        zz_desc['REFRESH'] = ""
        self.SWPRS = 0x00000003
        zz_edict['SWPRS'] = self.SWPRS
        zz_desc['SWPRS'] = ""
        self.SWREFRESH = 0x00000004
        zz_edict['SWREFRESH'] = self.SWREFRESH
        zz_desc['SWREFRESH'] = ""
        self.LESENSE = 0x00000005
        zz_edict['LESENSE'] = self.LESENSE
        zz_desc['LESENSE'] = ""
        super(RM_Enum_VDAC0_CH0CTRL_TRIGMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_CH0CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_CH0CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_CH1CTRL_TRIGMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.SW = 0x00000000
        zz_edict['SW'] = self.SW
        zz_desc['SW'] = ""
        self.PRS = 0x00000001
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.REFRESH = 0x00000002
        zz_edict['REFRESH'] = self.REFRESH
        zz_desc['REFRESH'] = ""
        self.SWPRS = 0x00000003
        zz_edict['SWPRS'] = self.SWPRS
        zz_desc['SWPRS'] = ""
        self.SWREFRESH = 0x00000004
        zz_edict['SWREFRESH'] = self.SWREFRESH
        zz_desc['SWREFRESH'] = ""
        self.LESENSE = 0x00000005
        zz_edict['LESENSE'] = self.LESENSE
        zz_desc['LESENSE'] = ""
        super(RM_Enum_VDAC0_CH1CTRL_TRIGMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_CH1CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_CH1CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_DBGCTRL_REFRESHRATE(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_DBGCTRL_REFRESHRATE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA0_CTRL_DRIVESTRENGTH(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_OPA0_CTRL_DRIVESTRENGTH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA0_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_OPA0_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA0_MUX_RESINMUX(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.OPANEXT = 0x00000001
        zz_edict['OPANEXT'] = self.OPANEXT
        zz_desc['OPANEXT'] = ""
        self.NEGPAD = 0x00000002
        zz_edict['NEGPAD'] = self.NEGPAD
        zz_desc['NEGPAD'] = ""
        self.POSPAD = 0x00000003
        zz_edict['POSPAD'] = self.POSPAD
        zz_desc['POSPAD'] = ""
        self.COMPAD = 0x00000004
        zz_edict['COMPAD'] = self.COMPAD
        zz_desc['COMPAD'] = ""
        self.CENTER = 0x00000005
        zz_edict['CENTER'] = self.CENTER
        zz_desc['CENTER'] = ""
        self.VSS = 0x00000006
        zz_edict['VSS'] = self.VSS
        zz_desc['VSS'] = ""
        super(RM_Enum_VDAC0_OPA0_MUX_RESINMUX, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA0_MUX_RESSEL(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_OPA0_MUX_RESSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA0_OUT_ALTOUTPADEN(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.OUT0 = 0x00000001
        zz_edict['OUT0'] = self.OUT0
        zz_desc['OUT0'] = ""
        self.OUT1 = 0x00000002
        zz_edict['OUT1'] = self.OUT1
        zz_desc['OUT1'] = ""
        self.OUT2 = 0x00000004
        zz_edict['OUT2'] = self.OUT2
        zz_desc['OUT2'] = ""
        self.OUT3 = 0x00000008
        zz_edict['OUT3'] = self.OUT3
        zz_desc['OUT3'] = ""
        self.OUT4 = 0x00000010
        zz_edict['OUT4'] = self.OUT4
        zz_desc['OUT4'] = ""
        super(RM_Enum_VDAC0_OPA0_OUT_ALTOUTPADEN, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA1_CTRL_DRIVESTRENGTH(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_OPA1_CTRL_DRIVESTRENGTH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA1_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_OPA1_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA1_MUX_RESINMUX(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.OPANEXT = 0x00000001
        zz_edict['OPANEXT'] = self.OPANEXT
        zz_desc['OPANEXT'] = ""
        self.NEGPAD = 0x00000002
        zz_edict['NEGPAD'] = self.NEGPAD
        zz_desc['NEGPAD'] = ""
        self.POSPAD = 0x00000003
        zz_edict['POSPAD'] = self.POSPAD
        zz_desc['POSPAD'] = ""
        self.COMPAD = 0x00000004
        zz_edict['COMPAD'] = self.COMPAD
        zz_desc['COMPAD'] = ""
        self.CENTER = 0x00000005
        zz_edict['CENTER'] = self.CENTER
        zz_desc['CENTER'] = ""
        self.VSS = 0x00000006
        zz_edict['VSS'] = self.VSS
        zz_desc['VSS'] = ""
        super(RM_Enum_VDAC0_OPA1_MUX_RESINMUX, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA1_MUX_RESSEL(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_OPA1_MUX_RESSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA1_OUT_ALTOUTPADEN(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.OUT0 = 0x00000001
        zz_edict['OUT0'] = self.OUT0
        zz_desc['OUT0'] = ""
        self.OUT1 = 0x00000002
        zz_edict['OUT1'] = self.OUT1
        zz_desc['OUT1'] = ""
        self.OUT2 = 0x00000004
        zz_edict['OUT2'] = self.OUT2
        zz_desc['OUT2'] = ""
        self.OUT3 = 0x00000008
        zz_edict['OUT3'] = self.OUT3
        zz_desc['OUT3'] = ""
        self.OUT4 = 0x00000010
        zz_edict['OUT4'] = self.OUT4
        zz_desc['OUT4'] = ""
        super(RM_Enum_VDAC0_OPA1_OUT_ALTOUTPADEN, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA2_CTRL_DRIVESTRENGTH(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_OPA2_CTRL_DRIVESTRENGTH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA2_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_OPA2_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA2_MUX_RESINMUX(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.OPANEXT = 0x00000001
        zz_edict['OPANEXT'] = self.OPANEXT
        zz_desc['OPANEXT'] = ""
        self.NEGPAD = 0x00000002
        zz_edict['NEGPAD'] = self.NEGPAD
        zz_desc['NEGPAD'] = ""
        self.POSPAD = 0x00000003
        zz_edict['POSPAD'] = self.POSPAD
        zz_desc['POSPAD'] = ""
        self.COMPAD = 0x00000004
        zz_edict['COMPAD'] = self.COMPAD
        zz_desc['COMPAD'] = ""
        self.CENTER = 0x00000005
        zz_edict['CENTER'] = self.CENTER
        zz_desc['CENTER'] = ""
        self.VSS = 0x00000006
        zz_edict['VSS'] = self.VSS
        zz_desc['VSS'] = ""
        super(RM_Enum_VDAC0_OPA2_MUX_RESINMUX, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA2_MUX_RESSEL(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_OPA2_MUX_RESSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA2_OUT_ALTOUTPADEN(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.OUT0 = 0x00000001
        zz_edict['OUT0'] = self.OUT0
        zz_desc['OUT0'] = ""
        self.OUT1 = 0x00000002
        zz_edict['OUT1'] = self.OUT1
        zz_desc['OUT1'] = ""
        self.OUT2 = 0x00000004
        zz_edict['OUT2'] = self.OUT2
        zz_desc['OUT2'] = ""
        self.OUT3 = 0x00000008
        zz_edict['OUT3'] = self.OUT3
        zz_desc['OUT3'] = ""
        self.OUT4 = 0x00000010
        zz_edict['OUT4'] = self.OUT4
        zz_desc['OUT4'] = ""
        super(RM_Enum_VDAC0_OPA2_OUT_ALTOUTPADEN, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA3_CTRL_DRIVESTRENGTH(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_OPA3_CTRL_DRIVESTRENGTH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA3_CTRL_PRSSEL(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_OPA3_CTRL_PRSSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA3_MUX_RESINMUX(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000000
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.OPANEXT = 0x00000001
        zz_edict['OPANEXT'] = self.OPANEXT
        zz_desc['OPANEXT'] = ""
        self.NEGPAD = 0x00000002
        zz_edict['NEGPAD'] = self.NEGPAD
        zz_desc['NEGPAD'] = ""
        self.POSPAD = 0x00000003
        zz_edict['POSPAD'] = self.POSPAD
        zz_desc['POSPAD'] = ""
        self.COMPAD = 0x00000004
        zz_edict['COMPAD'] = self.COMPAD
        zz_desc['COMPAD'] = ""
        self.CENTER = 0x00000005
        zz_edict['CENTER'] = self.CENTER
        zz_desc['CENTER'] = ""
        self.VSS = 0x00000006
        zz_edict['VSS'] = self.VSS
        zz_desc['VSS'] = ""
        super(RM_Enum_VDAC0_OPA3_MUX_RESINMUX, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA3_MUX_RESSEL(Base_RM_Enum):
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
        super(RM_Enum_VDAC0_OPA3_MUX_RESSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_VDAC0_OPA3_OUT_ALTOUTPADEN(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.OUT0 = 0x00000001
        zz_edict['OUT0'] = self.OUT0
        zz_desc['OUT0'] = ""
        self.OUT1 = 0x00000002
        zz_edict['OUT1'] = self.OUT1
        zz_desc['OUT1'] = ""
        self.OUT2 = 0x00000004
        zz_edict['OUT2'] = self.OUT2
        zz_desc['OUT2'] = ""
        self.OUT3 = 0x00000008
        zz_edict['OUT3'] = self.OUT3
        zz_desc['OUT3'] = ""
        self.OUT4 = 0x00000010
        zz_edict['OUT4'] = self.OUT4
        zz_desc['OUT4'] = ""
        super(RM_Enum_VDAC0_OPA3_OUT_ALTOUTPADEN, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


