
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_CRC_CTRL_CRCWIDTH(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CRCWIDTH8 = 0x00000000
        zz_edict['CRCWIDTH8'] = self.CRCWIDTH8
        zz_desc['CRCWIDTH8'] = ""
        self.CRCWIDTH16 = 0x00000001
        zz_edict['CRCWIDTH16'] = self.CRCWIDTH16
        zz_desc['CRCWIDTH16'] = ""
        self.CRCWIDTH24 = 0x00000002
        zz_edict['CRCWIDTH24'] = self.CRCWIDTH24
        zz_desc['CRCWIDTH24'] = ""
        self.CRCWIDTH32 = 0x00000003
        zz_edict['CRCWIDTH32'] = self.CRCWIDTH32
        zz_desc['CRCWIDTH32'] = ""
        super(RM_Enum_CRC_CTRL_CRCWIDTH, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


