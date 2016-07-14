
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_MSC_READCTRL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.WS0 = 0x00000000
        zz_edict['WS0'] = self.WS0
        zz_desc['WS0'] = ""
        self.WS1 = 0x00000001
        zz_edict['WS1'] = self.WS1
        zz_desc['WS1'] = ""
        self.WS2 = 0x00000002
        zz_edict['WS2'] = self.WS2
        zz_desc['WS2'] = ""
        self.WS3 = 0x00000003
        zz_edict['WS3'] = self.WS3
        zz_desc['WS3'] = ""
        super(RM_Enum_MSC_READCTRL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MSC_MEMFEATURE_FLASHSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        #print("WARNING: Aliasing enum '4K' to 'E4K'")
        self.E4K = 0x00000002
        zz_edict['E4K'] = self.E4K
        zz_desc['E4K'] = ""
        #print("WARNING: Aliasing enum '8K' to 'E8K'")
        self.E8K = 0x00000003
        zz_edict['E8K'] = self.E8K
        zz_desc['E8K'] = ""
        #print("WARNING: Aliasing enum '16K' to 'E16K'")
        self.E16K = 0x00000004
        zz_edict['E16K'] = self.E16K
        zz_desc['E16K'] = ""
        #print("WARNING: Aliasing enum '32K' to 'E32K'")
        self.E32K = 0x00000005
        zz_edict['E32K'] = self.E32K
        zz_desc['E32K'] = ""
        #print("WARNING: Aliasing enum '64K' to 'E64K'")
        self.E64K = 0x00000006
        zz_edict['E64K'] = self.E64K
        zz_desc['E64K'] = ""
        #print("WARNING: Aliasing enum '128K' to 'E128K'")
        self.E128K = 0x00000007
        zz_edict['E128K'] = self.E128K
        zz_desc['E128K'] = ""
        #print("WARNING: Aliasing enum '256K' to 'E256K'")
        self.E256K = 0x00000008
        zz_edict['E256K'] = self.E256K
        zz_desc['E256K'] = ""
        #print("WARNING: Aliasing enum '512K' to 'E512K'")
        self.E512K = 0x00000009
        zz_edict['E512K'] = self.E512K
        zz_desc['E512K'] = ""
        #print("WARNING: Aliasing enum '1024K' to 'E1024K'")
        self.E1024K = 0x0000000A
        zz_edict['E1024K'] = self.E1024K
        zz_desc['E1024K'] = ""
        #print("WARNING: Aliasing enum '2048K' to 'E2048K'")
        self.E2048K = 0x0000000B
        zz_edict['E2048K'] = self.E2048K
        zz_desc['E2048K'] = ""
        super(RM_Enum_MSC_MEMFEATURE_FLASHSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MSC_MEMFEATURE_FLASHRWWMERGE(Base_RM_Enum):
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
        super(RM_Enum_MSC_MEMFEATURE_FLASHRWWMERGE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MSC_LOCK_LOCKKEY(Base_RM_Enum):
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
        super(RM_Enum_MSC_LOCK_LOCKKEY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MSC_MASSLOCK_LOCKKEY(Base_RM_Enum):
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
        super(RM_Enum_MSC_MASSLOCK_LOCKKEY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MSC_BANKSWITCHLOCK_BANKSWITCHLOCKKEY(Base_RM_Enum):
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
        super(RM_Enum_MSC_BANKSWITCHLOCK_BANKSWITCHLOCKKEY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MSC_CACHECONFIG0_CACHELPLEVEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BASE = 0x00000000
        zz_edict['BASE'] = self.BASE
        zz_desc['BASE'] = ""
        self.ADVANCED = 0x00000001
        zz_edict['ADVANCED'] = self.ADVANCED
        zz_desc['ADVANCED'] = ""
        self.MINACTIVITY = 0x00000003
        zz_edict['MINACTIVITY'] = self.MINACTIVITY
        zz_desc['MINACTIVITY'] = ""
        super(RM_Enum_MSC_CACHECONFIG0_CACHELPLEVEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MSC_MBISTCTRL_STATSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.MBISTCTRL = 0x00000000
        zz_edict['MBISTCTRL'] = self.MBISTCTRL
        zz_desc['MBISTCTRL'] = ""
        self.DONESTAT = 0x00000001
        zz_edict['DONESTAT'] = self.DONESTAT
        zz_desc['DONESTAT'] = ""
        self.FAILSTAT = 0x00000002
        zz_edict['FAILSTAT'] = self.FAILSTAT
        zz_desc['FAILSTAT'] = ""
        self.DIAGSTAT1 = 0x00000003
        zz_edict['DIAGSTAT1'] = self.DIAGSTAT1
        zz_desc['DIAGSTAT1'] = ""
        self.DIAGSTAT2 = 0x00000004
        zz_edict['DIAGSTAT2'] = self.DIAGSTAT2
        zz_desc['DIAGSTAT2'] = ""
        self.DIAGSTAT3 = 0x00000005
        zz_edict['DIAGSTAT3'] = self.DIAGSTAT3
        zz_desc['DIAGSTAT3'] = ""
        super(RM_Enum_MSC_MBISTCTRL_STATSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MSC_MBISTCTRL_ALGSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NOALGSEL = 0x00000000
        zz_edict['NOALGSEL'] = self.NOALGSEL
        zz_desc['NOALGSEL'] = ""
        self.MARCHAPLUS = 0x00000001
        zz_edict['MARCHAPLUS'] = self.MARCHAPLUS
        zz_desc['MARCHAPLUS'] = ""
        self.MARCH2 = 0x00000002
        zz_edict['MARCH2'] = self.MARCH2
        zz_desc['MARCH2'] = ""
        self.ADDRDECODEBG0 = 0x00000004
        zz_edict['ADDRDECODEBG0'] = self.ADDRDECODEBG0
        zz_desc['ADDRDECODEBG0'] = ""
        self.ADDRDECODEBG1 = 0x00000008
        zz_edict['ADDRDECODEBG1'] = self.ADDRDECODEBG1
        zz_desc['ADDRDECODEBG1'] = ""
        self.CHKRBOARD = 0x00000010
        zz_edict['CHKRBOARD'] = self.CHKRBOARD
        zz_desc['CHKRBOARD'] = ""
        self.COLMARCH1 = 0x00000020
        zz_edict['COLMARCH1'] = self.COLMARCH1
        zz_desc['COLMARCH1'] = ""
        self.WRITEMASKSHORT = 0x00000040
        zz_edict['WRITEMASKSHORT'] = self.WRITEMASKSHORT
        zz_desc['WRITEMASKSHORT'] = ""
        super(RM_Enum_MSC_MBISTCTRL_ALGSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MSC_MBISTCTRL_ALGSELDP(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NOALGSEL = 0x00000000
        zz_edict['NOALGSEL'] = self.NOALGSEL
        zz_desc['NOALGSEL'] = ""
        self.PORTISOROW = 0x00000001
        zz_edict['PORTISOROW'] = self.PORTISOROW
        zz_desc['PORTISOROW'] = ""
        self.PORTISOCOL = 0x00000002
        zz_edict['PORTISOCOL'] = self.PORTISOCOL
        zz_desc['PORTISOCOL'] = ""
        super(RM_Enum_MSC_MBISTCTRL_ALGSELDP, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MSC_MBISTLOCK_LOCKKEY(Base_RM_Enum):
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
        super(RM_Enum_MSC_MBISTLOCK_LOCKKEY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MSC_TESTCTRL_PATMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ALLONE = 0x00000000
        zz_edict['ALLONE'] = self.ALLONE
        zz_desc['ALLONE'] = ""
        self.ALLZERO = 0x00000001
        zz_edict['ALLZERO'] = self.ALLZERO
        zz_desc['ALLZERO'] = ""
        self.DIAGONAL = 0x00000002
        zz_edict['DIAGONAL'] = self.DIAGONAL
        zz_desc['DIAGONAL'] = ""
        self.XOR = 0x00000003
        zz_edict['XOR'] = self.XOR
        zz_desc['XOR'] = ""
        self.XNOR = 0x00000004
        zz_edict['XNOR'] = self.XNOR
        zz_desc['XNOR'] = ""
        self.LXOR = 0x00000005
        zz_edict['LXOR'] = self.LXOR
        zz_desc['LXOR'] = ""
        self.LXNOR = 0x00000006
        zz_edict['LXNOR'] = self.LXNOR
        zz_desc['LXNOR'] = ""
        super(RM_Enum_MSC_TESTCTRL_PATMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MSC_TESTCTRL_SEMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.SINGLECYCLETOGGLE = 0x00000000
        zz_edict['SINGLECYCLETOGGLE'] = self.SINGLECYCLETOGGLE
        zz_desc['SINGLECYCLETOGGLE'] = ""
        self.DUALCYCLETOGGLE = 0x00000001
        zz_edict['DUALCYCLETOGGLE'] = self.DUALCYCLETOGGLE
        zz_desc['DUALCYCLETOGGLE'] = ""
        self.NOTOGGLE = 0x00000002
        zz_edict['NOTOGGLE'] = self.NOTOGGLE
        zz_desc['NOTOGGLE'] = ""
        super(RM_Enum_MSC_TESTCTRL_SEMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


