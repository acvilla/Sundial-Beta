
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_RMU_CTRL_WDOGRMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.LIMITED = 0x00000001
        zz_edict['LIMITED'] = self.LIMITED
        zz_desc['LIMITED'] = ""
        self.EXTENDED = 0x00000002
        zz_edict['EXTENDED'] = self.EXTENDED
        zz_desc['EXTENDED'] = ""
        self.FULL = 0x00000004
        zz_edict['FULL'] = self.FULL
        zz_desc['FULL'] = ""
        super(RM_Enum_RMU_CTRL_WDOGRMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RMU_CTRL_LOCKUPRMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.LIMITED = 0x00000001
        zz_edict['LIMITED'] = self.LIMITED
        zz_desc['LIMITED'] = ""
        self.EXTENDED = 0x00000002
        zz_edict['EXTENDED'] = self.EXTENDED
        zz_desc['EXTENDED'] = ""
        self.FULL = 0x00000004
        zz_edict['FULL'] = self.FULL
        zz_desc['FULL'] = ""
        super(RM_Enum_RMU_CTRL_LOCKUPRMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RMU_CTRL_SYSRMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.LIMITED = 0x00000001
        zz_edict['LIMITED'] = self.LIMITED
        zz_desc['LIMITED'] = ""
        self.EXTENDED = 0x00000002
        zz_edict['EXTENDED'] = self.EXTENDED
        zz_desc['EXTENDED'] = ""
        self.FULL = 0x00000004
        zz_edict['FULL'] = self.FULL
        zz_desc['FULL'] = ""
        super(RM_Enum_RMU_CTRL_SYSRMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RMU_CTRL_PINRMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.LIMITED = 0x00000001
        zz_edict['LIMITED'] = self.LIMITED
        zz_desc['LIMITED'] = ""
        self.EXTENDED = 0x00000002
        zz_edict['EXTENDED'] = self.EXTENDED
        zz_desc['EXTENDED'] = ""
        self.FULL = 0x00000004
        zz_edict['FULL'] = self.FULL
        zz_desc['FULL'] = ""
        super(RM_Enum_RMU_CTRL_PINRMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_RMU_LOCK_LOCKKEY(Base_RM_Enum):
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
        super(RM_Enum_RMU_LOCK_LOCKKEY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


