
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_CMU_CTRL_CLKOUTSEL0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.ULFRCO = 0x00000001
        zz_edict['ULFRCO'] = self.ULFRCO
        zz_desc['ULFRCO'] = ""
        self.LFRCO = 0x00000002
        zz_edict['LFRCO'] = self.LFRCO
        zz_desc['LFRCO'] = ""
        self.LFXO = 0x00000003
        zz_edict['LFXO'] = self.LFXO
        zz_desc['LFXO'] = ""
        self.HFXO = 0x00000006
        zz_edict['HFXO'] = self.HFXO
        zz_desc['HFXO'] = ""
        self.HFEXPCLK = 0x00000007
        zz_edict['HFEXPCLK'] = self.HFEXPCLK
        zz_desc['HFEXPCLK'] = ""
        self.ULFRCOQ = 0x00000009
        zz_edict['ULFRCOQ'] = self.ULFRCOQ
        zz_desc['ULFRCOQ'] = ""
        self.LFRCOQ = 0x0000000A
        zz_edict['LFRCOQ'] = self.LFRCOQ
        zz_desc['LFRCOQ'] = ""
        self.LFXOQ = 0x0000000B
        zz_edict['LFXOQ'] = self.LFXOQ
        zz_desc['LFXOQ'] = ""
        self.HFRCOQ = 0x0000000C
        zz_edict['HFRCOQ'] = self.HFRCOQ
        zz_desc['HFRCOQ'] = ""
        self.AUXHFRCOQ = 0x0000000D
        zz_edict['AUXHFRCOQ'] = self.AUXHFRCOQ
        zz_desc['AUXHFRCOQ'] = ""
        self.HFXOQ = 0x0000000E
        zz_edict['HFXOQ'] = self.HFXOQ
        zz_desc['HFXOQ'] = ""
        self.HFSRCCLK = 0x0000000F
        zz_edict['HFSRCCLK'] = self.HFSRCCLK
        zz_desc['HFSRCCLK'] = ""
        super(RM_Enum_CMU_CTRL_CLKOUTSEL0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_CTRL_CLKOUTSEL1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.ULFRCO = 0x00000001
        zz_edict['ULFRCO'] = self.ULFRCO
        zz_desc['ULFRCO'] = ""
        self.LFRCO = 0x00000002
        zz_edict['LFRCO'] = self.LFRCO
        zz_desc['LFRCO'] = ""
        self.LFXO = 0x00000003
        zz_edict['LFXO'] = self.LFXO
        zz_desc['LFXO'] = ""
        self.HFXO = 0x00000006
        zz_edict['HFXO'] = self.HFXO
        zz_desc['HFXO'] = ""
        self.HFEXPCLK = 0x00000007
        zz_edict['HFEXPCLK'] = self.HFEXPCLK
        zz_desc['HFEXPCLK'] = ""
        self.ULFRCOQ = 0x00000009
        zz_edict['ULFRCOQ'] = self.ULFRCOQ
        zz_desc['ULFRCOQ'] = ""
        self.LFRCOQ = 0x0000000A
        zz_edict['LFRCOQ'] = self.LFRCOQ
        zz_desc['LFRCOQ'] = ""
        self.LFXOQ = 0x0000000B
        zz_edict['LFXOQ'] = self.LFXOQ
        zz_desc['LFXOQ'] = ""
        self.HFRCOQ = 0x0000000C
        zz_edict['HFRCOQ'] = self.HFRCOQ
        zz_desc['HFRCOQ'] = ""
        self.AUXHFRCOQ = 0x0000000D
        zz_edict['AUXHFRCOQ'] = self.AUXHFRCOQ
        zz_desc['AUXHFRCOQ'] = ""
        self.HFXOQ = 0x0000000E
        zz_edict['HFXOQ'] = self.HFXOQ
        zz_desc['HFXOQ'] = ""
        self.HFSRCCLK = 0x0000000F
        zz_edict['HFSRCCLK'] = self.HFSRCCLK
        zz_desc['HFSRCCLK'] = ""
        super(RM_Enum_CMU_CTRL_CLKOUTSEL1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFRCOCTRL_CLKDIV(Base_RM_Enum):
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
        super(RM_Enum_CMU_HFRCOCTRL_CLKDIV, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_AUXHFRCOCTRL_CLKDIV(Base_RM_Enum):
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
        super(RM_Enum_CMU_AUXHFRCOCTRL_CLKDIV, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_LFRCOCTRL_TIMEOUT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '2CYCLES' to 'E2CYCLES'")
        self.E2CYCLES = 0x00000000
        zz_edict['E2CYCLES'] = self.E2CYCLES
        zz_desc['E2CYCLES'] = ""
        #print("WARNING: Aliasing enum '16CYCLES' to 'E16CYCLES'")
        self.E16CYCLES = 0x00000001
        zz_edict['E16CYCLES'] = self.E16CYCLES
        zz_desc['E16CYCLES'] = ""
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000002
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        super(RM_Enum_CMU_LFRCOCTRL_TIMEOUT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFXOCTRL_PEAKDETSHUNTOPTMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.AUTOCMD = 0x00000000
        zz_edict['AUTOCMD'] = self.AUTOCMD
        zz_desc['AUTOCMD'] = ""
        self.CMD = 0x00000001
        zz_edict['CMD'] = self.CMD
        zz_desc['CMD'] = ""
        self.MANUAL = 0x00000002
        zz_edict['MANUAL'] = self.MANUAL
        zz_desc['MANUAL'] = ""
        super(RM_Enum_CMU_HFXOCTRL_PEAKDETSHUNTOPTMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFXOCTRL_LFTIMEOUT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '0CYCLES' to 'E0CYCLES'")
        self.E0CYCLES = 0x00000000
        zz_edict['E0CYCLES'] = self.E0CYCLES
        zz_desc['E0CYCLES'] = ""
        #print("WARNING: Aliasing enum '2CYCLES' to 'E2CYCLES'")
        self.E2CYCLES = 0x00000001
        zz_edict['E2CYCLES'] = self.E2CYCLES
        zz_desc['E2CYCLES'] = ""
        #print("WARNING: Aliasing enum '4CYCLES' to 'E4CYCLES'")
        self.E4CYCLES = 0x00000002
        zz_edict['E4CYCLES'] = self.E4CYCLES
        zz_desc['E4CYCLES'] = ""
        #print("WARNING: Aliasing enum '16CYCLES' to 'E16CYCLES'")
        self.E16CYCLES = 0x00000003
        zz_edict['E16CYCLES'] = self.E16CYCLES
        zz_desc['E16CYCLES'] = ""
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000004
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        #print("WARNING: Aliasing enum '64CYCLES' to 'E64CYCLES'")
        self.E64CYCLES = 0x00000005
        zz_edict['E64CYCLES'] = self.E64CYCLES
        zz_desc['E64CYCLES'] = ""
        #print("WARNING: Aliasing enum '1KCYCLES' to 'E1KCYCLES'")
        self.E1KCYCLES = 0x00000006
        zz_edict['E1KCYCLES'] = self.E1KCYCLES
        zz_desc['E1KCYCLES'] = ""
        #print("WARNING: Aliasing enum '4KCYCLES' to 'E4KCYCLES'")
        self.E4KCYCLES = 0x00000007
        zz_edict['E4KCYCLES'] = self.E4KCYCLES
        zz_desc['E4KCYCLES'] = ""
        super(RM_Enum_CMU_HFXOCTRL_LFTIMEOUT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFXOTIMEOUTCTRL_STARTUPTIMEOUT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '2CYCLES' to 'E2CYCLES'")
        self.E2CYCLES = 0x00000000
        zz_edict['E2CYCLES'] = self.E2CYCLES
        zz_desc['E2CYCLES'] = ""
        #print("WARNING: Aliasing enum '4CYCLES' to 'E4CYCLES'")
        self.E4CYCLES = 0x00000001
        zz_edict['E4CYCLES'] = self.E4CYCLES
        zz_desc['E4CYCLES'] = ""
        #print("WARNING: Aliasing enum '16CYCLES' to 'E16CYCLES'")
        self.E16CYCLES = 0x00000002
        zz_edict['E16CYCLES'] = self.E16CYCLES
        zz_desc['E16CYCLES'] = ""
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000003
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        #print("WARNING: Aliasing enum '256CYCLES' to 'E256CYCLES'")
        self.E256CYCLES = 0x00000004
        zz_edict['E256CYCLES'] = self.E256CYCLES
        zz_desc['E256CYCLES'] = ""
        #print("WARNING: Aliasing enum '1KCYCLES' to 'E1KCYCLES'")
        self.E1KCYCLES = 0x00000005
        zz_edict['E1KCYCLES'] = self.E1KCYCLES
        zz_desc['E1KCYCLES'] = ""
        #print("WARNING: Aliasing enum '2KCYCLES' to 'E2KCYCLES'")
        self.E2KCYCLES = 0x00000006
        zz_edict['E2KCYCLES'] = self.E2KCYCLES
        zz_desc['E2KCYCLES'] = ""
        #print("WARNING: Aliasing enum '4KCYCLES' to 'E4KCYCLES'")
        self.E4KCYCLES = 0x00000007
        zz_edict['E4KCYCLES'] = self.E4KCYCLES
        zz_desc['E4KCYCLES'] = ""
        #print("WARNING: Aliasing enum '8KCYCLES' to 'E8KCYCLES'")
        self.E8KCYCLES = 0x00000008
        zz_edict['E8KCYCLES'] = self.E8KCYCLES
        zz_desc['E8KCYCLES'] = ""
        #print("WARNING: Aliasing enum '16KCYCLES' to 'E16KCYCLES'")
        self.E16KCYCLES = 0x00000009
        zz_edict['E16KCYCLES'] = self.E16KCYCLES
        zz_desc['E16KCYCLES'] = ""
        #print("WARNING: Aliasing enum '32KCYCLES' to 'E32KCYCLES'")
        self.E32KCYCLES = 0x0000000A
        zz_edict['E32KCYCLES'] = self.E32KCYCLES
        zz_desc['E32KCYCLES'] = ""
        super(RM_Enum_CMU_HFXOTIMEOUTCTRL_STARTUPTIMEOUT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFXOTIMEOUTCTRL_STEADYTIMEOUT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '2CYCLES' to 'E2CYCLES'")
        self.E2CYCLES = 0x00000000
        zz_edict['E2CYCLES'] = self.E2CYCLES
        zz_desc['E2CYCLES'] = ""
        #print("WARNING: Aliasing enum '4CYCLES' to 'E4CYCLES'")
        self.E4CYCLES = 0x00000001
        zz_edict['E4CYCLES'] = self.E4CYCLES
        zz_desc['E4CYCLES'] = ""
        #print("WARNING: Aliasing enum '16CYCLES' to 'E16CYCLES'")
        self.E16CYCLES = 0x00000002
        zz_edict['E16CYCLES'] = self.E16CYCLES
        zz_desc['E16CYCLES'] = ""
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000003
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        #print("WARNING: Aliasing enum '256CYCLES' to 'E256CYCLES'")
        self.E256CYCLES = 0x00000004
        zz_edict['E256CYCLES'] = self.E256CYCLES
        zz_desc['E256CYCLES'] = ""
        #print("WARNING: Aliasing enum '1KCYCLES' to 'E1KCYCLES'")
        self.E1KCYCLES = 0x00000005
        zz_edict['E1KCYCLES'] = self.E1KCYCLES
        zz_desc['E1KCYCLES'] = ""
        #print("WARNING: Aliasing enum '2KCYCLES' to 'E2KCYCLES'")
        self.E2KCYCLES = 0x00000006
        zz_edict['E2KCYCLES'] = self.E2KCYCLES
        zz_desc['E2KCYCLES'] = ""
        #print("WARNING: Aliasing enum '4KCYCLES' to 'E4KCYCLES'")
        self.E4KCYCLES = 0x00000007
        zz_edict['E4KCYCLES'] = self.E4KCYCLES
        zz_desc['E4KCYCLES'] = ""
        #print("WARNING: Aliasing enum '8KCYCLES' to 'E8KCYCLES'")
        self.E8KCYCLES = 0x00000008
        zz_edict['E8KCYCLES'] = self.E8KCYCLES
        zz_desc['E8KCYCLES'] = ""
        #print("WARNING: Aliasing enum '16KCYCLES' to 'E16KCYCLES'")
        self.E16KCYCLES = 0x00000009
        zz_edict['E16KCYCLES'] = self.E16KCYCLES
        zz_desc['E16KCYCLES'] = ""
        #print("WARNING: Aliasing enum '32KCYCLES' to 'E32KCYCLES'")
        self.E32KCYCLES = 0x0000000A
        zz_edict['E32KCYCLES'] = self.E32KCYCLES
        zz_desc['E32KCYCLES'] = ""
        super(RM_Enum_CMU_HFXOTIMEOUTCTRL_STEADYTIMEOUT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFXOTIMEOUTCTRL_WARMSTEADYTIMEOUT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '2CYCLES' to 'E2CYCLES'")
        self.E2CYCLES = 0x00000000
        zz_edict['E2CYCLES'] = self.E2CYCLES
        zz_desc['E2CYCLES'] = ""
        #print("WARNING: Aliasing enum '4CYCLES' to 'E4CYCLES'")
        self.E4CYCLES = 0x00000001
        zz_edict['E4CYCLES'] = self.E4CYCLES
        zz_desc['E4CYCLES'] = ""
        #print("WARNING: Aliasing enum '16CYCLES' to 'E16CYCLES'")
        self.E16CYCLES = 0x00000002
        zz_edict['E16CYCLES'] = self.E16CYCLES
        zz_desc['E16CYCLES'] = ""
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000003
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        #print("WARNING: Aliasing enum '256CYCLES' to 'E256CYCLES'")
        self.E256CYCLES = 0x00000004
        zz_edict['E256CYCLES'] = self.E256CYCLES
        zz_desc['E256CYCLES'] = ""
        #print("WARNING: Aliasing enum '1KCYCLES' to 'E1KCYCLES'")
        self.E1KCYCLES = 0x00000005
        zz_edict['E1KCYCLES'] = self.E1KCYCLES
        zz_desc['E1KCYCLES'] = ""
        #print("WARNING: Aliasing enum '2KCYCLES' to 'E2KCYCLES'")
        self.E2KCYCLES = 0x00000006
        zz_edict['E2KCYCLES'] = self.E2KCYCLES
        zz_desc['E2KCYCLES'] = ""
        #print("WARNING: Aliasing enum '4KCYCLES' to 'E4KCYCLES'")
        self.E4KCYCLES = 0x00000007
        zz_edict['E4KCYCLES'] = self.E4KCYCLES
        zz_desc['E4KCYCLES'] = ""
        #print("WARNING: Aliasing enum '8KCYCLES' to 'E8KCYCLES'")
        self.E8KCYCLES = 0x00000008
        zz_edict['E8KCYCLES'] = self.E8KCYCLES
        zz_desc['E8KCYCLES'] = ""
        #print("WARNING: Aliasing enum '16KCYCLES' to 'E16KCYCLES'")
        self.E16KCYCLES = 0x00000009
        zz_edict['E16KCYCLES'] = self.E16KCYCLES
        zz_desc['E16KCYCLES'] = ""
        #print("WARNING: Aliasing enum '32KCYCLES' to 'E32KCYCLES'")
        self.E32KCYCLES = 0x0000000A
        zz_edict['E32KCYCLES'] = self.E32KCYCLES
        zz_desc['E32KCYCLES'] = ""
        super(RM_Enum_CMU_HFXOTIMEOUTCTRL_WARMSTEADYTIMEOUT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFXOTIMEOUTCTRL_PEAKDETTIMEOUT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '2CYCLES' to 'E2CYCLES'")
        self.E2CYCLES = 0x00000000
        zz_edict['E2CYCLES'] = self.E2CYCLES
        zz_desc['E2CYCLES'] = ""
        #print("WARNING: Aliasing enum '4CYCLES' to 'E4CYCLES'")
        self.E4CYCLES = 0x00000001
        zz_edict['E4CYCLES'] = self.E4CYCLES
        zz_desc['E4CYCLES'] = ""
        #print("WARNING: Aliasing enum '16CYCLES' to 'E16CYCLES'")
        self.E16CYCLES = 0x00000002
        zz_edict['E16CYCLES'] = self.E16CYCLES
        zz_desc['E16CYCLES'] = ""
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000003
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        #print("WARNING: Aliasing enum '256CYCLES' to 'E256CYCLES'")
        self.E256CYCLES = 0x00000004
        zz_edict['E256CYCLES'] = self.E256CYCLES
        zz_desc['E256CYCLES'] = ""
        #print("WARNING: Aliasing enum '1KCYCLES' to 'E1KCYCLES'")
        self.E1KCYCLES = 0x00000005
        zz_edict['E1KCYCLES'] = self.E1KCYCLES
        zz_desc['E1KCYCLES'] = ""
        #print("WARNING: Aliasing enum '2KCYCLES' to 'E2KCYCLES'")
        self.E2KCYCLES = 0x00000006
        zz_edict['E2KCYCLES'] = self.E2KCYCLES
        zz_desc['E2KCYCLES'] = ""
        #print("WARNING: Aliasing enum '4KCYCLES' to 'E4KCYCLES'")
        self.E4KCYCLES = 0x00000007
        zz_edict['E4KCYCLES'] = self.E4KCYCLES
        zz_desc['E4KCYCLES'] = ""
        #print("WARNING: Aliasing enum '8KCYCLES' to 'E8KCYCLES'")
        self.E8KCYCLES = 0x00000008
        zz_edict['E8KCYCLES'] = self.E8KCYCLES
        zz_desc['E8KCYCLES'] = ""
        #print("WARNING: Aliasing enum '16KCYCLES' to 'E16KCYCLES'")
        self.E16KCYCLES = 0x00000009
        zz_edict['E16KCYCLES'] = self.E16KCYCLES
        zz_desc['E16KCYCLES'] = ""
        #print("WARNING: Aliasing enum '32KCYCLES' to 'E32KCYCLES'")
        self.E32KCYCLES = 0x0000000A
        zz_edict['E32KCYCLES'] = self.E32KCYCLES
        zz_desc['E32KCYCLES'] = ""
        super(RM_Enum_CMU_HFXOTIMEOUTCTRL_PEAKDETTIMEOUT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFXOTIMEOUTCTRL_SHUNTOPTTIMEOUT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '2CYCLES' to 'E2CYCLES'")
        self.E2CYCLES = 0x00000000
        zz_edict['E2CYCLES'] = self.E2CYCLES
        zz_desc['E2CYCLES'] = ""
        #print("WARNING: Aliasing enum '4CYCLES' to 'E4CYCLES'")
        self.E4CYCLES = 0x00000001
        zz_edict['E4CYCLES'] = self.E4CYCLES
        zz_desc['E4CYCLES'] = ""
        #print("WARNING: Aliasing enum '16CYCLES' to 'E16CYCLES'")
        self.E16CYCLES = 0x00000002
        zz_edict['E16CYCLES'] = self.E16CYCLES
        zz_desc['E16CYCLES'] = ""
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000003
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        #print("WARNING: Aliasing enum '256CYCLES' to 'E256CYCLES'")
        self.E256CYCLES = 0x00000004
        zz_edict['E256CYCLES'] = self.E256CYCLES
        zz_desc['E256CYCLES'] = ""
        #print("WARNING: Aliasing enum '1KCYCLES' to 'E1KCYCLES'")
        self.E1KCYCLES = 0x00000005
        zz_edict['E1KCYCLES'] = self.E1KCYCLES
        zz_desc['E1KCYCLES'] = ""
        #print("WARNING: Aliasing enum '2KCYCLES' to 'E2KCYCLES'")
        self.E2KCYCLES = 0x00000006
        zz_edict['E2KCYCLES'] = self.E2KCYCLES
        zz_desc['E2KCYCLES'] = ""
        #print("WARNING: Aliasing enum '4KCYCLES' to 'E4KCYCLES'")
        self.E4KCYCLES = 0x00000007
        zz_edict['E4KCYCLES'] = self.E4KCYCLES
        zz_desc['E4KCYCLES'] = ""
        #print("WARNING: Aliasing enum '8KCYCLES' to 'E8KCYCLES'")
        self.E8KCYCLES = 0x00000008
        zz_edict['E8KCYCLES'] = self.E8KCYCLES
        zz_desc['E8KCYCLES'] = ""
        #print("WARNING: Aliasing enum '16KCYCLES' to 'E16KCYCLES'")
        self.E16KCYCLES = 0x00000009
        zz_edict['E16KCYCLES'] = self.E16KCYCLES
        zz_desc['E16KCYCLES'] = ""
        #print("WARNING: Aliasing enum '32KCYCLES' to 'E32KCYCLES'")
        self.E32KCYCLES = 0x0000000A
        zz_edict['E32KCYCLES'] = self.E32KCYCLES
        zz_desc['E32KCYCLES'] = ""
        super(RM_Enum_CMU_HFXOTIMEOUTCTRL_SHUNTOPTTIMEOUT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_LFXOCTRL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.XTAL = 0x00000000
        zz_edict['XTAL'] = self.XTAL
        zz_desc['XTAL'] = ""
        self.BUFEXTCLK = 0x00000001
        zz_edict['BUFEXTCLK'] = self.BUFEXTCLK
        zz_desc['BUFEXTCLK'] = ""
        self.DIGEXTCLK = 0x00000002
        zz_edict['DIGEXTCLK'] = self.DIGEXTCLK
        zz_desc['DIGEXTCLK'] = ""
        super(RM_Enum_CMU_LFXOCTRL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_LFXOCTRL_TIMEOUT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '2CYCLES' to 'E2CYCLES'")
        self.E2CYCLES = 0x00000000
        zz_edict['E2CYCLES'] = self.E2CYCLES
        zz_desc['E2CYCLES'] = ""
        #print("WARNING: Aliasing enum '256CYCLES' to 'E256CYCLES'")
        self.E256CYCLES = 0x00000001
        zz_edict['E256CYCLES'] = self.E256CYCLES
        zz_desc['E256CYCLES'] = ""
        #print("WARNING: Aliasing enum '1KCYCLES' to 'E1KCYCLES'")
        self.E1KCYCLES = 0x00000002
        zz_edict['E1KCYCLES'] = self.E1KCYCLES
        zz_desc['E1KCYCLES'] = ""
        #print("WARNING: Aliasing enum '2KCYCLES' to 'E2KCYCLES'")
        self.E2KCYCLES = 0x00000003
        zz_edict['E2KCYCLES'] = self.E2KCYCLES
        zz_desc['E2KCYCLES'] = ""
        #print("WARNING: Aliasing enum '4KCYCLES' to 'E4KCYCLES'")
        self.E4KCYCLES = 0x00000004
        zz_edict['E4KCYCLES'] = self.E4KCYCLES
        zz_desc['E4KCYCLES'] = ""
        #print("WARNING: Aliasing enum '8KCYCLES' to 'E8KCYCLES'")
        self.E8KCYCLES = 0x00000005
        zz_edict['E8KCYCLES'] = self.E8KCYCLES
        zz_desc['E8KCYCLES'] = ""
        #print("WARNING: Aliasing enum '16KCYCLES' to 'E16KCYCLES'")
        self.E16KCYCLES = 0x00000006
        zz_edict['E16KCYCLES'] = self.E16KCYCLES
        zz_desc['E16KCYCLES'] = ""
        #print("WARNING: Aliasing enum '32KCYCLES' to 'E32KCYCLES'")
        self.E32KCYCLES = 0x00000007
        zz_edict['E32KCYCLES'] = self.E32KCYCLES
        zz_desc['E32KCYCLES'] = ""
        super(RM_Enum_CMU_LFXOCTRL_TIMEOUT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_ULFRCOCTRL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '1KHZ' to 'E1KHZ'")
        self.E1KHZ = 0x00000000
        zz_edict['E1KHZ'] = self.E1KHZ
        zz_desc['E1KHZ'] = ""
        #print("WARNING: Aliasing enum '2KHZ' to 'E2KHZ'")
        self.E2KHZ = 0x00000001
        zz_edict['E2KHZ'] = self.E2KHZ
        zz_desc['E2KHZ'] = ""
        #print("WARNING: Aliasing enum '4KHZ' to 'E4KHZ'")
        self.E4KHZ = 0x00000002
        zz_edict['E4KHZ'] = self.E4KHZ
        zz_desc['E4KHZ'] = ""
        #print("WARNING: Aliasing enum '32KHZ' to 'E32KHZ'")
        self.E32KHZ = 0x00000003
        zz_edict['E32KHZ'] = self.E32KHZ
        zz_desc['E32KHZ'] = ""
        super(RM_Enum_CMU_ULFRCOCTRL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_CALCTRL_UPSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.HFXO = 0x00000000
        zz_edict['HFXO'] = self.HFXO
        zz_desc['HFXO'] = ""
        self.LFXO = 0x00000001
        zz_edict['LFXO'] = self.LFXO
        zz_desc['LFXO'] = ""
        self.HFRCO = 0x00000002
        zz_edict['HFRCO'] = self.HFRCO
        zz_desc['HFRCO'] = ""
        self.LFRCO = 0x00000003
        zz_edict['LFRCO'] = self.LFRCO
        zz_desc['LFRCO'] = ""
        self.AUXHFRCO = 0x00000004
        zz_edict['AUXHFRCO'] = self.AUXHFRCO
        zz_desc['AUXHFRCO'] = ""
        self.PRS = 0x00000005
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        super(RM_Enum_CMU_CALCTRL_UPSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_CALCTRL_DOWNSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.HFCLK = 0x00000000
        zz_edict['HFCLK'] = self.HFCLK
        zz_desc['HFCLK'] = ""
        self.HFXO = 0x00000001
        zz_edict['HFXO'] = self.HFXO
        zz_desc['HFXO'] = ""
        self.LFXO = 0x00000002
        zz_edict['LFXO'] = self.LFXO
        zz_desc['LFXO'] = ""
        self.HFRCO = 0x00000003
        zz_edict['HFRCO'] = self.HFRCO
        zz_desc['HFRCO'] = ""
        self.LFRCO = 0x00000004
        zz_edict['LFRCO'] = self.LFRCO
        zz_desc['LFRCO'] = ""
        self.AUXHFRCO = 0x00000005
        zz_edict['AUXHFRCO'] = self.AUXHFRCO
        zz_desc['AUXHFRCO'] = ""
        self.PRS = 0x00000006
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        super(RM_Enum_CMU_CALCTRL_DOWNSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_CALCTRL_PRSUPSEL(Base_RM_Enum):
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
        super(RM_Enum_CMU_CALCTRL_PRSUPSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_CALCTRL_PRSDOWNSEL(Base_RM_Enum):
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
        super(RM_Enum_CMU_CALCTRL_PRSDOWNSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFCLKSEL_HF(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.HFRCO = 0x00000001
        zz_edict['HFRCO'] = self.HFRCO
        zz_desc['HFRCO'] = ""
        self.HFXO = 0x00000002
        zz_edict['HFXO'] = self.HFXO
        zz_desc['HFXO'] = ""
        self.LFRCO = 0x00000003
        zz_edict['LFRCO'] = self.LFRCO
        zz_desc['LFRCO'] = ""
        self.LFXO = 0x00000004
        zz_edict['LFXO'] = self.LFXO
        zz_desc['LFXO'] = ""
        super(RM_Enum_CMU_HFCLKSEL_HF, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_LFACLKSEL_LFA(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.LFRCO = 0x00000001
        zz_edict['LFRCO'] = self.LFRCO
        zz_desc['LFRCO'] = ""
        self.LFXO = 0x00000002
        zz_edict['LFXO'] = self.LFXO
        zz_desc['LFXO'] = ""
        self.HFCLKLE = 0x00000003
        zz_edict['HFCLKLE'] = self.HFCLKLE
        zz_desc['HFCLKLE'] = ""
        self.ULFRCO = 0x00000004
        zz_edict['ULFRCO'] = self.ULFRCO
        zz_desc['ULFRCO'] = ""
        super(RM_Enum_CMU_LFACLKSEL_LFA, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_LFBCLKSEL_LFB(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.LFRCO = 0x00000001
        zz_edict['LFRCO'] = self.LFRCO
        zz_desc['LFRCO'] = ""
        self.LFXO = 0x00000002
        zz_edict['LFXO'] = self.LFXO
        zz_desc['LFXO'] = ""
        self.HFCLKLE = 0x00000003
        zz_edict['HFCLKLE'] = self.HFCLKLE
        zz_desc['HFCLKLE'] = ""
        self.ULFRCO = 0x00000004
        zz_edict['ULFRCO'] = self.ULFRCO
        zz_desc['ULFRCO'] = ""
        super(RM_Enum_CMU_LFBCLKSEL_LFB, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_LFECLKSEL_LFE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.LFRCO = 0x00000001
        zz_edict['LFRCO'] = self.LFRCO
        zz_desc['LFRCO'] = ""
        self.LFXO = 0x00000002
        zz_edict['LFXO'] = self.LFXO
        zz_desc['LFXO'] = ""
        self.HFCLKLE = 0x00000003
        zz_edict['HFCLKLE'] = self.HFCLKLE
        zz_desc['HFCLKLE'] = ""
        self.ULFRCO = 0x00000004
        zz_edict['ULFRCO'] = self.ULFRCO
        zz_desc['ULFRCO'] = ""
        super(RM_Enum_CMU_LFECLKSEL_LFE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFCLKSTATUS_SELECTED(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.HFRCO = 0x00000001
        zz_edict['HFRCO'] = self.HFRCO
        zz_desc['HFRCO'] = ""
        self.HFXO = 0x00000002
        zz_edict['HFXO'] = self.HFXO
        zz_desc['HFXO'] = ""
        self.LFRCO = 0x00000003
        zz_edict['LFRCO'] = self.LFRCO
        zz_desc['LFRCO'] = ""
        self.LFXO = 0x00000004
        zz_edict['LFXO'] = self.LFXO
        zz_desc['LFXO'] = ""
        super(RM_Enum_CMU_HFCLKSTATUS_SELECTED, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFPRESC_PRESC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NODIVISION = 0x00000000
        zz_edict['NODIVISION'] = self.NODIVISION
        zz_desc['NODIVISION'] = ""
        super(RM_Enum_CMU_HFPRESC_PRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFCOREPRESC_PRESC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NODIVISION = 0x00000000
        zz_edict['NODIVISION'] = self.NODIVISION
        zz_desc['NODIVISION'] = ""
        super(RM_Enum_CMU_HFCOREPRESC_PRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFPERPRESC_PRESC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NODIVISION = 0x00000000
        zz_edict['NODIVISION'] = self.NODIVISION
        zz_desc['NODIVISION'] = ""
        super(RM_Enum_CMU_HFPERPRESC_PRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFRADIOPRESC_PRESC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NODIVISION = 0x00000000
        zz_edict['NODIVISION'] = self.NODIVISION
        zz_desc['NODIVISION'] = ""
        super(RM_Enum_CMU_HFRADIOPRESC_PRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_HFEXPPRESC_PRESC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NODIVISION = 0x00000000
        zz_edict['NODIVISION'] = self.NODIVISION
        zz_desc['NODIVISION'] = ""
        super(RM_Enum_CMU_HFEXPPRESC_PRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_LFAPRESC0_LETIMER0(Base_RM_Enum):
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
        super(RM_Enum_CMU_LFAPRESC0_LETIMER0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_LFBPRESC0_LEUART0(Base_RM_Enum):
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
        super(RM_Enum_CMU_LFBPRESC0_LEUART0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_LFEPRESC0_RTCC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIV1 = 0x00000000
        zz_edict['DIV1'] = self.DIV1
        zz_desc['DIV1'] = ""
        super(RM_Enum_CMU_LFEPRESC0_RTCC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_LCDCTRL_VBFDIV(Base_RM_Enum):
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
        super(RM_Enum_CMU_LCDCTRL_VBFDIV, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_LVDSCTRL_CLKSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.HFCLK = 0x00000001
        zz_edict['HFCLK'] = self.HFCLK
        zz_desc['HFCLK'] = ""
        self.AUXSYNTHCLK = 0x00000002
        zz_edict['AUXSYNTHCLK'] = self.AUXSYNTHCLK
        zz_desc['AUXSYNTHCLK'] = ""
        super(RM_Enum_CMU_LVDSCTRL_CLKSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_ADCCTRL_CLKSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.AUXHFRCO = 0x00000001
        zz_edict['AUXHFRCO'] = self.AUXHFRCO
        zz_desc['AUXHFRCO'] = ""
        self.HFXO = 0x00000002
        zz_edict['HFXO'] = self.HFXO
        zz_desc['HFXO'] = ""
        self.HFSRCCLK = 0x00000003
        zz_edict['HFSRCCLK'] = self.HFSRCCLK
        zz_desc['HFSRCCLK'] = ""
        super(RM_Enum_CMU_ADCCTRL_CLKSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_ROUTELOC0_CLKOUT0LOC(Base_RM_Enum):
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
        super(RM_Enum_CMU_ROUTELOC0_CLKOUT0LOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_ROUTELOC0_CLKOUT1LOC(Base_RM_Enum):
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
        super(RM_Enum_CMU_ROUTELOC0_CLKOUT1LOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_LOCK_LOCKKEY(Base_RM_Enum):
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
        super(RM_Enum_CMU_LOCK_LOCKKEY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_RFLOCK0_SYNTHLODIVFREQCTRL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIV2 = 0x00000001
        zz_edict['DIV2'] = self.DIV2
        zz_desc['DIV2'] = ""
        self.DIV3 = 0x00000002
        zz_edict['DIV3'] = self.DIV3
        zz_desc['DIV3'] = ""
        self.DIV4 = 0x00000004
        zz_edict['DIV4'] = self.DIV4
        zz_desc['DIV4'] = ""
        self.DIV5 = 0x00000008
        zz_edict['DIV5'] = self.DIV5
        zz_desc['DIV5'] = ""
        self.DIV6 = 0x00000010
        zz_edict['DIV6'] = self.DIV6
        zz_desc['DIV6'] = ""
        self.DIV8 = 0x00000020
        zz_edict['DIV8'] = self.DIV8
        zz_desc['DIV8'] = ""
        self.DIV9AND10AND12 = 0x00000040
        zz_edict['DIV9AND10AND12'] = self.DIV9AND10AND12
        zz_desc['DIV9AND10AND12'] = ""
        self.DIV15AND16 = 0x00000080
        zz_edict['DIV15AND16'] = self.DIV15AND16
        zz_desc['DIV15AND16'] = ""
        self.DIVOTHER = 0x00000100
        zz_edict['DIVOTHER'] = self.DIVOTHER
        zz_desc['DIVOTHER'] = ""
        super(RM_Enum_CMU_RFLOCK0_SYNTHLODIVFREQCTRL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_TEST_CLKOUTHIDDENSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.ULFRCO = 0x00000001
        zz_edict['ULFRCO'] = self.ULFRCO
        zz_desc['ULFRCO'] = ""
        self.EMUOSCLV = 0x00000002
        zz_edict['EMUOSCLV'] = self.EMUOSCLV
        zz_desc['EMUOSCLV'] = ""
        self.EMUOSCHV = 0x00000003
        zz_edict['EMUOSCHV'] = self.EMUOSCHV
        zz_desc['EMUOSCHV'] = ""
        self.HFXORAW = 0x00000004
        zz_edict['HFXORAW'] = self.HFXORAW
        zz_desc['HFXORAW'] = ""
        self.LFRCOVREF = 0x00000005
        zz_edict['LFRCOVREF'] = self.LFRCOVREF
        zz_desc['LFRCOVREF'] = ""
        super(RM_Enum_CMU_TEST_CLKOUTHIDDENSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_TEST_OSCCTRLSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.ULFRCOEN = 0x00000001
        zz_edict['ULFRCOEN'] = self.ULFRCOEN
        zz_desc['ULFRCOEN'] = ""
        self.LFRCOEN = 0x00000002
        zz_edict['LFRCOEN'] = self.LFRCOEN
        zz_desc['LFRCOEN'] = ""
        self.LFXOCOREEN = 0x00000003
        zz_edict['LFXOCOREEN'] = self.LFXOCOREEN
        zz_desc['LFXOCOREEN'] = ""
        self.LFXOBUFFEREN = 0x00000004
        zz_edict['LFXOBUFFEREN'] = self.LFXOBUFFEREN
        zz_desc['LFXOBUFFEREN'] = ""
        self.HFRCOEN = 0x00000005
        zz_edict['HFRCOEN'] = self.HFRCOEN
        zz_desc['HFRCOEN'] = ""
        self.AUXHFRCOEN = 0x00000006
        zz_edict['AUXHFRCOEN'] = self.AUXHFRCOEN
        zz_desc['AUXHFRCOEN'] = ""
        self.HFXOCOREEN = 0x00000007
        zz_edict['HFXOCOREEN'] = self.HFXOCOREEN
        zz_desc['HFXOCOREEN'] = ""
        self.HFXOCLKDIGEN = 0x00000008
        zz_edict['HFXOCLKDIGEN'] = self.HFXOCLKDIGEN
        zz_desc['HFXOCLKDIGEN'] = ""
        self.EMUOSCEN = 0x00000009
        zz_edict['EMUOSCEN'] = self.EMUOSCEN
        zz_desc['EMUOSCEN'] = ""
        super(RM_Enum_CMU_TEST_OSCCTRLSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_TESTLFRCOCTRL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '32KHZDUTY50' to 'E32KHZDUTY50'")
        self.E32KHZDUTY50 = 0x00000000
        zz_edict['E32KHZDUTY50'] = self.E32KHZDUTY50
        zz_desc['E32KHZDUTY50'] = ""
        #print("WARNING: Aliasing enum '64KHZDUTY5' to 'E64KHZDUTY5'")
        self.E64KHZDUTY5 = 0x00000001
        zz_edict['E64KHZDUTY5'] = self.E64KHZDUTY5
        zz_desc['E64KHZDUTY5'] = ""
        #print("WARNING: Aliasing enum '16KHZDUTY50' to 'E16KHZDUTY50'")
        self.E16KHZDUTY50 = 0x00000002
        zz_edict['E16KHZDUTY50'] = self.E16KHZDUTY50
        zz_desc['E16KHZDUTY50'] = ""
        #print("WARNING: Aliasing enum '32KHZDUTY5' to 'E32KHZDUTY5'")
        self.E32KHZDUTY5 = 0x00000003
        zz_edict['E32KHZDUTY5'] = self.E32KHZDUTY5
        zz_desc['E32KHZDUTY5'] = ""
        super(RM_Enum_CMU_TESTLFRCOCTRL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_TESTLFRCOCTRL_SELCLKDIV(Base_RM_Enum):
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
        super(RM_Enum_CMU_TESTLFRCOCTRL_SELCLKDIV, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_TESTLFRCOCTRL_VREFUPDATE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '32CYCLES' to 'E32CYCLES'")
        self.E32CYCLES = 0x00000000
        zz_edict['E32CYCLES'] = self.E32CYCLES
        zz_desc['E32CYCLES'] = ""
        #print("WARNING: Aliasing enum '64CYCLES' to 'E64CYCLES'")
        self.E64CYCLES = 0x00000001
        zz_edict['E64CYCLES'] = self.E64CYCLES
        zz_desc['E64CYCLES'] = ""
        #print("WARNING: Aliasing enum '128CYCLES' to 'E128CYCLES'")
        self.E128CYCLES = 0x00000002
        zz_edict['E128CYCLES'] = self.E128CYCLES
        zz_desc['E128CYCLES'] = ""
        #print("WARNING: Aliasing enum '256CYCLES' to 'E256CYCLES'")
        self.E256CYCLES = 0x00000003
        zz_edict['E256CYCLES'] = self.E256CYCLES
        zz_desc['E256CYCLES'] = ""
        super(RM_Enum_CMU_TESTLFRCOCTRL_VREFUPDATE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CMU_TESTLFRCOCTRL_VREFPRECH(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '2CYCLES' to 'E2CYCLES'")
        self.E2CYCLES = 0x00000000
        zz_edict['E2CYCLES'] = self.E2CYCLES
        zz_desc['E2CYCLES'] = ""
        #print("WARNING: Aliasing enum '4CYCLES' to 'E4CYCLES'")
        self.E4CYCLES = 0x00000001
        zz_edict['E4CYCLES'] = self.E4CYCLES
        zz_desc['E4CYCLES'] = ""
        #print("WARNING: Aliasing enum '8CYCLES' to 'E8CYCLES'")
        self.E8CYCLES = 0x00000002
        zz_edict['E8CYCLES'] = self.E8CYCLES
        zz_desc['E8CYCLES'] = ""
        #print("WARNING: Aliasing enum '16CYCLES' to 'E16CYCLES'")
        self.E16CYCLES = 0x00000003
        zz_edict['E16CYCLES'] = self.E16CYCLES
        zz_desc['E16CYCLES'] = ""
        super(RM_Enum_CMU_TESTLFRCOCTRL_VREFPRECH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


