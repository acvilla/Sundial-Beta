
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_CRYOTIMER_CTRL_OSCSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LFRCO = 0x00000000
        zz_edict['LFRCO'] = self.LFRCO
        zz_desc['LFRCO'] = ""
        self.LFXO = 0x00000001
        zz_edict['LFXO'] = self.LFXO
        zz_desc['LFXO'] = ""
        self.ULFRCO = 0x00000002
        zz_edict['ULFRCO'] = self.ULFRCO
        zz_desc['ULFRCO'] = ""
        super(RM_Enum_CRYOTIMER_CTRL_OSCSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_CRYOTIMER_CTRL_PRESC(Base_RM_Enum):
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
        super(RM_Enum_CRYOTIMER_CTRL_PRESC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


