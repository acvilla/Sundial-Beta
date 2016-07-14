
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_CM4_CHIPREVMINORMSB_MINORREVMSB(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.FPGA = 0x00000008
        zz_edict['FPGA'] = self.FPGA
        zz_desc['FPGA'] = ""
        super(RM_Enum_CM4_CHIPREVMINORMSB_MINORREVMSB, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


