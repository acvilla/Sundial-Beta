
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_SYSCFG_AMUXCP_DUTYFSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.F0 = 0x00000000
        zz_edict['F0'] = self.F0
        zz_desc['F0'] = ""
        self.F1 = 0x00000001
        zz_edict['F1'] = self.F1
        zz_desc['F1'] = ""
        self.F2 = 0x00000002
        zz_edict['F2'] = self.F2
        zz_desc['F2'] = ""
        self.F3 = 0x00000003
        zz_edict['F3'] = self.F3
        zz_desc['F3'] = ""
        super(RM_Enum_SYSCFG_AMUXCP_DUTYFSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


