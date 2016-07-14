
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_GPCRC_SNOOP0_CTRL_SNOOPSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BYTE = 0x00000000
        zz_edict['BYTE'] = self.BYTE
        zz_desc['BYTE'] = ""
        self.HALFWORD = 0x00000001
        zz_edict['HALFWORD'] = self.HALFWORD
        zz_desc['HALFWORD'] = ""
        self.WORD = 0x00000002
        zz_edict['WORD'] = self.WORD
        zz_desc['WORD'] = ""
        super(RM_Enum_GPCRC_SNOOP0_CTRL_SNOOPSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPCRC_SNOOP1_CTRL_SNOOPSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BYTE = 0x00000000
        zz_edict['BYTE'] = self.BYTE
        zz_desc['BYTE'] = ""
        self.HALFWORD = 0x00000001
        zz_edict['HALFWORD'] = self.HALFWORD
        zz_desc['HALFWORD'] = ""
        self.WORD = 0x00000002
        zz_edict['WORD'] = self.WORD
        zz_desc['WORD'] = ""
        super(RM_Enum_GPCRC_SNOOP1_CTRL_SNOOPSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPCRC_SNOOP2_CTRL_SNOOPSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BYTE = 0x00000000
        zz_edict['BYTE'] = self.BYTE
        zz_desc['BYTE'] = ""
        self.HALFWORD = 0x00000001
        zz_edict['HALFWORD'] = self.HALFWORD
        zz_desc['HALFWORD'] = ""
        self.WORD = 0x00000002
        zz_edict['WORD'] = self.WORD
        zz_desc['WORD'] = ""
        super(RM_Enum_GPCRC_SNOOP2_CTRL_SNOOPSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


