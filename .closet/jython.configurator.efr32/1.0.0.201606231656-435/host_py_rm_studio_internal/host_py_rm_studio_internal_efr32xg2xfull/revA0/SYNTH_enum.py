
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_SYNTH_CTRL_PRSMUX0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INLOCK = 0x00000001
        zz_edict['INLOCK'] = self.INLOCK
        zz_desc['INLOCK'] = ""
        super(RM_Enum_SYNTH_CTRL_PRSMUX0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_SYNTH_CTRL_PRSMUX1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.AUXINLOCK = 0x00000001
        zz_edict['AUXINLOCK'] = self.AUXINLOCK
        zz_desc['AUXINLOCK'] = ""
        super(RM_Enum_SYNTH_CTRL_PRSMUX1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_SYNTH_CALCTRL_CAPCALCYCLEWAIT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CYCLES1 = 0x00000000
        zz_edict['CYCLES1'] = self.CYCLES1
        zz_desc['CYCLES1'] = ""
        self.CYCLES8 = 0x00000001
        zz_edict['CYCLES8'] = self.CYCLES8
        zz_desc['CYCLES8'] = ""
        self.CYCLES16 = 0x00000002
        zz_edict['CYCLES16'] = self.CYCLES16
        zz_desc['CYCLES16'] = ""
        self.CYCLES32 = 0x00000003
        zz_edict['CYCLES32'] = self.CYCLES32
        zz_desc['CYCLES32'] = ""
        super(RM_Enum_SYNTH_CALCTRL_CAPCALCYCLEWAIT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_SYNTH_CALCTRL_AUXCALCYCLEWAIT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CYCLES64 = 0x00000000
        zz_edict['CYCLES64'] = self.CYCLES64
        zz_desc['CYCLES64'] = ""
        self.CYCLES128 = 0x00000001
        zz_edict['CYCLES128'] = self.CYCLES128
        zz_desc['CYCLES128'] = ""
        self.CYCLES192 = 0x00000002
        zz_edict['CYCLES192'] = self.CYCLES192
        zz_desc['CYCLES192'] = ""
        self.CYCLES256 = 0x00000003
        zz_edict['CYCLES256'] = self.CYCLES256
        zz_desc['CYCLES256'] = ""
        super(RM_Enum_SYNTH_CALCTRL_AUXCALCYCLEWAIT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_SYNTH_DIVCTRL_LODIVFREQCTRL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LODIV1 = 0x00000001
        zz_edict['LODIV1'] = self.LODIV1
        zz_desc['LODIV1'] = ""
        self.LODIV2 = 0x00000002
        zz_edict['LODIV2'] = self.LODIV2
        zz_desc['LODIV2'] = ""
        self.LODIV3 = 0x00000003
        zz_edict['LODIV3'] = self.LODIV3
        zz_desc['LODIV3'] = ""
        self.LODIV4 = 0x00000004
        zz_edict['LODIV4'] = self.LODIV4
        zz_desc['LODIV4'] = ""
        self.LODIV5 = 0x00000005
        zz_edict['LODIV5'] = self.LODIV5
        zz_desc['LODIV5'] = ""
        self.LODIV7 = 0x00000007
        zz_edict['LODIV7'] = self.LODIV7
        zz_desc['LODIV7'] = ""
        self.LODIV6 = 0x00000013
        zz_edict['LODIV6'] = self.LODIV6
        zz_desc['LODIV6'] = ""
        self.LODIV8 = 0x00000014
        zz_edict['LODIV8'] = self.LODIV8
        zz_desc['LODIV8'] = ""
        self.LODIV10 = 0x00000015
        zz_edict['LODIV10'] = self.LODIV10
        zz_desc['LODIV10'] = ""
        self.LODIV14 = 0x00000017
        zz_edict['LODIV14'] = self.LODIV14
        zz_desc['LODIV14'] = ""
        self.LODIV9 = 0x0000001B
        zz_edict['LODIV9'] = self.LODIV9
        zz_desc['LODIV9'] = ""
        self.LODIV12 = 0x0000001C
        zz_edict['LODIV12'] = self.LODIV12
        zz_desc['LODIV12'] = ""
        self.LODIV15 = 0x0000001D
        zz_edict['LODIV15'] = self.LODIV15
        zz_desc['LODIV15'] = ""
        self.LODIV16 = 0x00000024
        zz_edict['LODIV16'] = self.LODIV16
        zz_desc['LODIV16'] = ""
        self.LODIV20 = 0x00000025
        zz_edict['LODIV20'] = self.LODIV20
        zz_desc['LODIV20'] = ""
        self.LODIV18 = 0x0000009B
        zz_edict['LODIV18'] = self.LODIV18
        zz_desc['LODIV18'] = ""
        self.LODIV24 = 0x0000009C
        zz_edict['LODIV24'] = self.LODIV24
        zz_desc['LODIV24'] = ""
        super(RM_Enum_SYNTH_DIVCTRL_LODIVFREQCTRL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_SYNTH_DIVCTRL_AUXLODIVFREQCTRL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LODIV1 = 0x00000000
        zz_edict['LODIV1'] = self.LODIV1
        zz_desc['LODIV1'] = ""
        self.LODIV2 = 0x00000001
        zz_edict['LODIV2'] = self.LODIV2
        zz_desc['LODIV2'] = ""
        self.LODIV3 = 0x00000002
        zz_edict['LODIV3'] = self.LODIV3
        zz_desc['LODIV3'] = ""
        self.LODIV4 = 0x00000003
        zz_edict['LODIV4'] = self.LODIV4
        zz_desc['LODIV4'] = ""
        self.LODIV6 = 0x00000006
        zz_edict['LODIV6'] = self.LODIV6
        zz_desc['LODIV6'] = ""
        self.LODIV8 = 0x00000007
        zz_edict['LODIV8'] = self.LODIV8
        zz_desc['LODIV8'] = ""
        self.LODIV9 = 0x0000000A
        zz_edict['LODIV9'] = self.LODIV9
        zz_desc['LODIV9'] = ""
        self.LODIV12 = 0x0000000E
        zz_edict['LODIV12'] = self.LODIV12
        zz_desc['LODIV12'] = ""
        self.LODIV16 = 0x0000000F
        zz_edict['LODIV16'] = self.LODIV16
        zz_desc['LODIV16'] = ""
        self.LODIV18 = 0x0000001A
        zz_edict['LODIV18'] = self.LODIV18
        zz_desc['LODIV18'] = ""
        self.LODIV24 = 0x0000001B
        zz_edict['LODIV24'] = self.LODIV24
        zz_desc['LODIV24'] = ""
        super(RM_Enum_SYNTH_DIVCTRL_AUXLODIVFREQCTRL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_SYNTH_VCORANGE_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.AUTO = 0x00000000
        zz_edict['AUTO'] = self.AUTO
        zz_desc['AUTO'] = ""
        self.SEMIAUTO = 0x00000001
        zz_edict['SEMIAUTO'] = self.SEMIAUTO
        zz_desc['SEMIAUTO'] = ""
        self.MANUAL = 0x00000002
        zz_edict['MANUAL'] = self.MANUAL
        zz_desc['MANUAL'] = ""
        self.DISABLE = 0x00000003
        zz_edict['DISABLE'] = self.DISABLE
        zz_desc['DISABLE'] = ""
        super(RM_Enum_SYNTH_VCORANGE_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


