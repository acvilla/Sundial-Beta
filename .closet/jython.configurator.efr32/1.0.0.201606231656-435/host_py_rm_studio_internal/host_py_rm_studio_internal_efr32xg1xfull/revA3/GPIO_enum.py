
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_GPIO_PA_MODEL_MODE0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEL_MODE0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEL_MODE1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEL_MODE1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEL_MODE2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEL_MODE2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEL_MODE3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEL_MODE3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEL_MODE4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEL_MODE4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEL_MODE5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEL_MODE5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEL_MODE6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEL_MODE6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEL_MODE7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEL_MODE7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEH_MODE8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEH_MODE8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEH_MODE9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEH_MODE9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEH_MODE10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEH_MODE10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEH_MODE11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEH_MODE11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEH_MODE12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEH_MODE12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEH_MODE13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEH_MODE13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEH_MODE14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEH_MODE14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PA_MODEH_MODE15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PA_MODEH_MODE15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEL_MODE0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEL_MODE0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEL_MODE1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEL_MODE1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEL_MODE2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEL_MODE2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEL_MODE3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEL_MODE3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEL_MODE4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEL_MODE4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEL_MODE5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEL_MODE5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEL_MODE6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEL_MODE6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEL_MODE7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEL_MODE7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEH_MODE8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEH_MODE8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEH_MODE9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEH_MODE9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEH_MODE10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEH_MODE10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEH_MODE11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEH_MODE11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEH_MODE12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEH_MODE12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEH_MODE13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEH_MODE13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEH_MODE14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEH_MODE14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PB_MODEH_MODE15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PB_MODEH_MODE15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEL_MODE0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEL_MODE0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEL_MODE1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEL_MODE1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEL_MODE2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEL_MODE2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEL_MODE3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEL_MODE3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEL_MODE4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEL_MODE4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEL_MODE5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEL_MODE5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEL_MODE6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEL_MODE6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEL_MODE7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEL_MODE7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEH_MODE8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEH_MODE8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEH_MODE9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEH_MODE9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEH_MODE10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEH_MODE10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEH_MODE11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEH_MODE11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEH_MODE12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEH_MODE12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEH_MODE13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEH_MODE13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEH_MODE14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEH_MODE14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PC_MODEH_MODE15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PC_MODEH_MODE15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEL_MODE0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEL_MODE0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEL_MODE1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEL_MODE1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEL_MODE2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEL_MODE2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEL_MODE3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEL_MODE3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEL_MODE4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEL_MODE4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEL_MODE5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEL_MODE5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEL_MODE6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEL_MODE6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEL_MODE7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEL_MODE7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEH_MODE8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEH_MODE8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEH_MODE9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEH_MODE9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEH_MODE10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEH_MODE10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEH_MODE11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEH_MODE11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEH_MODE12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEH_MODE12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEH_MODE13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEH_MODE13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEH_MODE14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEH_MODE14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PD_MODEH_MODE15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PD_MODEH_MODE15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEL_MODE0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEL_MODE0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEL_MODE1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEL_MODE1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEL_MODE2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEL_MODE2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEL_MODE3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEL_MODE3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEL_MODE4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEL_MODE4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEL_MODE5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEL_MODE5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEL_MODE6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEL_MODE6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEL_MODE7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEL_MODE7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEH_MODE8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEH_MODE8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEH_MODE9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEH_MODE9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEH_MODE10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEH_MODE10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEH_MODE11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEH_MODE11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEH_MODE12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEH_MODE12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEH_MODE13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEH_MODE13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEH_MODE14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEH_MODE14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PE_MODEH_MODE15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PE_MODEH_MODE15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEL_MODE0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEL_MODE0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEL_MODE1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEL_MODE1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEL_MODE2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEL_MODE2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEL_MODE3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEL_MODE3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEL_MODE4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEL_MODE4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEL_MODE5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEL_MODE5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEL_MODE6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEL_MODE6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEL_MODE7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEL_MODE7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEH_MODE8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEH_MODE8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEH_MODE9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEH_MODE9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEH_MODE10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEH_MODE10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEH_MODE11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEH_MODE11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEH_MODE12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEH_MODE12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEH_MODE13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEH_MODE13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEH_MODE14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEH_MODE14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PF_MODEH_MODE15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PF_MODEH_MODE15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEL_MODE0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEL_MODE0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEL_MODE1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEL_MODE1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEL_MODE2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEL_MODE2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEL_MODE3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEL_MODE3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEL_MODE4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEL_MODE4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEL_MODE5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEL_MODE5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEL_MODE6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEL_MODE6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEL_MODE7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEL_MODE7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEH_MODE8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEH_MODE8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEH_MODE9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEH_MODE9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEH_MODE10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEH_MODE10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEH_MODE11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEH_MODE11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEH_MODE12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEH_MODE12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEH_MODE13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEH_MODE13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEH_MODE14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEH_MODE14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PG_MODEH_MODE15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PG_MODEH_MODE15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEL_MODE0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEL_MODE0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEL_MODE1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEL_MODE1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEL_MODE2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEL_MODE2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEL_MODE3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEL_MODE3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEL_MODE4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEL_MODE4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEL_MODE5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEL_MODE5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEL_MODE6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEL_MODE6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEL_MODE7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEL_MODE7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEH_MODE8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEH_MODE8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEH_MODE9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEH_MODE9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEH_MODE10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEH_MODE10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEH_MODE11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEH_MODE11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEH_MODE12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEH_MODE12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEH_MODE13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEH_MODE13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEH_MODE14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEH_MODE14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PH_MODEH_MODE15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PH_MODEH_MODE15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEL_MODE0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEL_MODE0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEL_MODE1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEL_MODE1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEL_MODE2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEL_MODE2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEL_MODE3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEL_MODE3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEL_MODE4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEL_MODE4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEL_MODE5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEL_MODE5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEL_MODE6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEL_MODE6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEL_MODE7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEL_MODE7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEH_MODE8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEH_MODE8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEH_MODE9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEH_MODE9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEH_MODE10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEH_MODE10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEH_MODE11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEH_MODE11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEH_MODE12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEH_MODE12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEH_MODE13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEH_MODE13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEH_MODE14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEH_MODE14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PI_MODEH_MODE15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PI_MODEH_MODE15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEL_MODE0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEL_MODE0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEL_MODE1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEL_MODE1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEL_MODE2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEL_MODE2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEL_MODE3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEL_MODE3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEL_MODE4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEL_MODE4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEL_MODE5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEL_MODE5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEL_MODE6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEL_MODE6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEL_MODE7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEL_MODE7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEH_MODE8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEH_MODE8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEH_MODE9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEH_MODE9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEH_MODE10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEH_MODE10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEH_MODE11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEH_MODE11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEH_MODE12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEH_MODE12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEH_MODE13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEH_MODE13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEH_MODE14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEH_MODE14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PJ_MODEH_MODE15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PJ_MODEH_MODE15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEL_MODE0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEL_MODE0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEL_MODE1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEL_MODE1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEL_MODE2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEL_MODE2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEL_MODE3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEL_MODE3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEL_MODE4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEL_MODE4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEL_MODE5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEL_MODE5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEL_MODE6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEL_MODE6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEL_MODE7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEL_MODE7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEH_MODE8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEH_MODE8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEH_MODE9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEH_MODE9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEH_MODE10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEH_MODE10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEH_MODE11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEH_MODE11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEH_MODE12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEH_MODE12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEH_MODE13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEH_MODE13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEH_MODE14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEH_MODE14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PK_MODEH_MODE15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PK_MODEH_MODE15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEL_MODE0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEL_MODE0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEL_MODE1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEL_MODE1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEL_MODE2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEL_MODE2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEL_MODE3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEL_MODE3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEL_MODE4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEL_MODE4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEL_MODE5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEL_MODE5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEL_MODE6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEL_MODE6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEL_MODE7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEL_MODE7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEH_MODE8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEH_MODE8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEH_MODE9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEH_MODE9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEH_MODE10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEH_MODE10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEH_MODE11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEH_MODE11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEH_MODE12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEH_MODE12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEH_MODE13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEH_MODE13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEH_MODE14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEH_MODE14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_PL_MODEH_MODE15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.INPUT = 0x00000001
        zz_edict['INPUT'] = self.INPUT
        zz_desc['INPUT'] = ""
        self.INPUTPULL = 0x00000002
        zz_edict['INPUTPULL'] = self.INPUTPULL
        zz_desc['INPUTPULL'] = ""
        self.INPUTPULLFILTER = 0x00000003
        zz_edict['INPUTPULLFILTER'] = self.INPUTPULLFILTER
        zz_desc['INPUTPULLFILTER'] = ""
        self.PUSHPULL = 0x00000004
        zz_edict['PUSHPULL'] = self.PUSHPULL
        zz_desc['PUSHPULL'] = ""
        self.PUSHPULLALT = 0x00000005
        zz_edict['PUSHPULLALT'] = self.PUSHPULLALT
        zz_desc['PUSHPULLALT'] = ""
        self.WIREDOR = 0x00000006
        zz_edict['WIREDOR'] = self.WIREDOR
        zz_desc['WIREDOR'] = ""
        self.WIREDORPULLDOWN = 0x00000007
        zz_edict['WIREDORPULLDOWN'] = self.WIREDORPULLDOWN
        zz_desc['WIREDORPULLDOWN'] = ""
        self.WIREDAND = 0x00000008
        zz_edict['WIREDAND'] = self.WIREDAND
        zz_desc['WIREDAND'] = ""
        self.WIREDANDFILTER = 0x00000009
        zz_edict['WIREDANDFILTER'] = self.WIREDANDFILTER
        zz_desc['WIREDANDFILTER'] = ""
        self.WIREDANDPULLUP = 0x0000000A
        zz_edict['WIREDANDPULLUP'] = self.WIREDANDPULLUP
        zz_desc['WIREDANDPULLUP'] = ""
        self.WIREDANDPULLUPFILTER = 0x0000000B
        zz_edict['WIREDANDPULLUPFILTER'] = self.WIREDANDPULLUPFILTER
        zz_desc['WIREDANDPULLUPFILTER'] = ""
        self.WIREDANDALT = 0x0000000C
        zz_edict['WIREDANDALT'] = self.WIREDANDALT
        zz_desc['WIREDANDALT'] = ""
        self.WIREDANDALTFILTER = 0x0000000D
        zz_edict['WIREDANDALTFILTER'] = self.WIREDANDALTFILTER
        zz_desc['WIREDANDALTFILTER'] = ""
        self.WIREDANDALTPULLUP = 0x0000000E
        zz_edict['WIREDANDALTPULLUP'] = self.WIREDANDALTPULLUP
        zz_desc['WIREDANDALTPULLUP'] = ""
        self.WIREDANDALTPULLUPFILTER = 0x0000000F
        zz_edict['WIREDANDALTPULLUPFILTER'] = self.WIREDANDALTPULLUPFILTER
        zz_desc['WIREDANDALTPULLUPFILTER'] = ""
        super(RM_Enum_GPIO_PL_MODEH_MODE15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELL_EXTIPSEL0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELL_EXTIPSEL0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELL_EXTIPSEL1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELL_EXTIPSEL1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELL_EXTIPSEL2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELL_EXTIPSEL2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELL_EXTIPSEL3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELL_EXTIPSEL3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELL_EXTIPSEL4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELL_EXTIPSEL4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELL_EXTIPSEL5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELL_EXTIPSEL5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELL_EXTIPSEL6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELL_EXTIPSEL6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELL_EXTIPSEL7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELL_EXTIPSEL7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELH_EXTIPSEL8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELH_EXTIPSEL8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELH_EXTIPSEL9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELH_EXTIPSEL9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELH_EXTIPSEL10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELH_EXTIPSEL10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELH_EXTIPSEL11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELH_EXTIPSEL11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELH_EXTIPSEL12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELH_EXTIPSEL12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELH_EXTIPSEL13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELH_EXTIPSEL13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELH_EXTIPSEL14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELH_EXTIPSEL14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPSELH_EXTIPSEL15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PORTA = 0x00000000
        zz_edict['PORTA'] = self.PORTA
        zz_desc['PORTA'] = ""
        self.PORTB = 0x00000001
        zz_edict['PORTB'] = self.PORTB
        zz_desc['PORTB'] = ""
        self.PORTC = 0x00000002
        zz_edict['PORTC'] = self.PORTC
        zz_desc['PORTC'] = ""
        self.PORTD = 0x00000003
        zz_edict['PORTD'] = self.PORTD
        zz_desc['PORTD'] = ""
        self.PORTE = 0x00000004
        zz_edict['PORTE'] = self.PORTE
        zz_desc['PORTE'] = ""
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTG = 0x00000006
        zz_edict['PORTG'] = self.PORTG
        zz_desc['PORTG'] = ""
        self.PORTH = 0x00000007
        zz_edict['PORTH'] = self.PORTH
        zz_desc['PORTH'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        self.PORTL = 0x0000000B
        zz_edict['PORTL'] = self.PORTL
        zz_desc['PORTL'] = ""
        super(RM_Enum_GPIO_EXTIPSELH_EXTIPSEL15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELL_EXTIGSEL0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELL_EXTIGSEL0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELL_EXTIGSEL1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELL_EXTIGSEL1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELL_EXTIGSEL2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELL_EXTIGSEL2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELL_EXTIGSEL3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELL_EXTIGSEL3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELL_EXTIGSEL4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELL_EXTIGSEL4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELL_EXTIGSEL5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELL_EXTIGSEL5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELL_EXTIGSEL6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELL_EXTIGSEL6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELL_EXTIGSEL7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELL_EXTIGSEL7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELH_EXTIGSEL8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELH_EXTIGSEL8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELH_EXTIGSEL9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELH_EXTIGSEL9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELH_EXTIGSEL10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELH_EXTIGSEL10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELH_EXTIGSEL11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELH_EXTIGSEL11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELH_EXTIGSEL12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELH_EXTIGSEL12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELH_EXTIGSEL13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELH_EXTIGSEL13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELH_EXTIGSEL14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELH_EXTIGSEL14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIGSELH_EXTIGSEL15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GROUP0 = 0x00000000
        zz_edict['GROUP0'] = self.GROUP0
        zz_desc['GROUP0'] = ""
        self.GROUP1 = 0x00000001
        zz_edict['GROUP1'] = self.GROUP1
        zz_desc['GROUP1'] = ""
        self.GROUP2 = 0x00000002
        zz_edict['GROUP2'] = self.GROUP2
        zz_desc['GROUP2'] = ""
        self.GROUP3 = 0x00000003
        zz_edict['GROUP3'] = self.GROUP3
        zz_desc['GROUP3'] = ""
        super(RM_Enum_GPIO_EXTIGSELH_EXTIGSEL15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTILEVEL_EM4WULEVEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOW = 0x00000000
        zz_edict['LOW'] = self.LOW
        zz_desc['LOW'] = ""
        self.HIGH = 0x00000001
        zz_edict['HIGH'] = self.HIGH
        zz_desc['HIGH'] = ""
        super(RM_Enum_GPIO_EXTILEVEL_EM4WULEVEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_ROUTELOC0_SWVLOC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOC0 = 0x00000000
        zz_edict['LOC0'] = self.LOC0
        zz_desc['LOC0'] = ""
        self.LOC1 = 0x00000001
        zz_edict['LOC1'] = self.LOC1
        zz_desc['LOC1'] = ""
        self.LOC2 = 0x00000002
        zz_edict['LOC2'] = self.LOC2
        zz_desc['LOC2'] = ""
        self.LOC3 = 0x00000003
        zz_edict['LOC3'] = self.LOC3
        zz_desc['LOC3'] = ""
        super(RM_Enum_GPIO_ROUTELOC0_SWVLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_LOCK_LOCKKEY(Base_RM_Enum):
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
        super(RM_Enum_GPIO_LOCK_LOCKKEY, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


