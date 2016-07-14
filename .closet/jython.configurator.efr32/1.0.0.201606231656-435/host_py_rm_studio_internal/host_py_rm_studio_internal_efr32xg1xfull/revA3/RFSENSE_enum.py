
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_RFSENSE_CTRL_OSCSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.RF = 0x00000000
        zz_edict['RF'] = self.RF
        zz_desc['RF'] = ""
        self.LFRCO = 0x00000001
        zz_edict['LFRCO'] = self.LFRCO
        zz_desc['LFRCO'] = ""
        self.LFXO = 0x00000002
        zz_edict['LFXO'] = self.LFXO
        zz_desc['LFXO'] = ""
        self.ULFRCO = 0x00000003
        zz_edict['ULFRCO'] = self.ULFRCO
        zz_desc['ULFRCO'] = ""
        super(RM_Enum_RFSENSE_CTRL_OSCSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


