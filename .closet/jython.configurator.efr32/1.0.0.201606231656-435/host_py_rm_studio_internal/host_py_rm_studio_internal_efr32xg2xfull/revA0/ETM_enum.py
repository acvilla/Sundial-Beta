
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_ETM_ETMCCR_EXTINPNUM(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ZERO = 0x00000000
        zz_edict['ZERO'] = self.ZERO
        zz_desc['ZERO'] = ""
        self.ONE = 0x00000001
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000002
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        super(RM_Enum_ETM_ETMCCR_EXTINPNUM, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_ETM_ETMAUTHSTATUS_NONSECNONINVDBG(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLE = 0x00000002
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        self.ENABLE = 0x00000003
        zz_edict['ENABLE'] = self.ENABLE
        zz_desc['ENABLE'] = ""
        super(RM_Enum_ETM_ETMAUTHSTATUS_NONSECNONINVDBG, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


