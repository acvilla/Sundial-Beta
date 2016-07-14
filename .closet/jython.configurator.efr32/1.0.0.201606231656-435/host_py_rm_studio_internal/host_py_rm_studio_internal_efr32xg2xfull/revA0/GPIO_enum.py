
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
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
        self.PORTF = 0x00000005
        zz_edict['PORTF'] = self.PORTF
        zz_desc['PORTF'] = ""
        self.PORTI = 0x00000008
        zz_edict['PORTI'] = self.PORTI
        zz_desc['PORTI'] = ""
        self.PORTJ = 0x00000009
        zz_edict['PORTJ'] = self.PORTJ
        zz_desc['PORTJ'] = ""
        self.PORTK = 0x0000000A
        zz_edict['PORTK'] = self.PORTK
        zz_desc['PORTK'] = ""
        super(RM_Enum_GPIO_EXTIPSELH_EXTIPSEL15, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN0 = 0x00000000
        zz_edict['PIN0'] = self.PIN0
        zz_desc['PIN0'] = ""
        self.PIN1 = 0x00000001
        zz_edict['PIN1'] = self.PIN1
        zz_desc['PIN1'] = ""
        self.PIN2 = 0x00000002
        zz_edict['PIN2'] = self.PIN2
        zz_desc['PIN2'] = ""
        self.PIN3 = 0x00000003
        zz_edict['PIN3'] = self.PIN3
        zz_desc['PIN3'] = ""
        super(RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL1(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN0 = 0x00000000
        zz_edict['PIN0'] = self.PIN0
        zz_desc['PIN0'] = ""
        self.PIN1 = 0x00000001
        zz_edict['PIN1'] = self.PIN1
        zz_desc['PIN1'] = ""
        self.PIN2 = 0x00000002
        zz_edict['PIN2'] = self.PIN2
        zz_desc['PIN2'] = ""
        self.PIN3 = 0x00000003
        zz_edict['PIN3'] = self.PIN3
        zz_desc['PIN3'] = ""
        super(RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL1, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL2(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN0 = 0x00000000
        zz_edict['PIN0'] = self.PIN0
        zz_desc['PIN0'] = ""
        self.PIN1 = 0x00000001
        zz_edict['PIN1'] = self.PIN1
        zz_desc['PIN1'] = ""
        self.PIN2 = 0x00000002
        zz_edict['PIN2'] = self.PIN2
        zz_desc['PIN2'] = ""
        self.PIN3 = 0x00000003
        zz_edict['PIN3'] = self.PIN3
        zz_desc['PIN3'] = ""
        super(RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL2, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL3(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN0 = 0x00000000
        zz_edict['PIN0'] = self.PIN0
        zz_desc['PIN0'] = ""
        self.PIN1 = 0x00000001
        zz_edict['PIN1'] = self.PIN1
        zz_desc['PIN1'] = ""
        self.PIN2 = 0x00000002
        zz_edict['PIN2'] = self.PIN2
        zz_desc['PIN2'] = ""
        self.PIN3 = 0x00000003
        zz_edict['PIN3'] = self.PIN3
        zz_desc['PIN3'] = ""
        super(RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL3, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL4(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN4 = 0x00000000
        zz_edict['PIN4'] = self.PIN4
        zz_desc['PIN4'] = ""
        self.PIN5 = 0x00000001
        zz_edict['PIN5'] = self.PIN5
        zz_desc['PIN5'] = ""
        self.PIN6 = 0x00000002
        zz_edict['PIN6'] = self.PIN6
        zz_desc['PIN6'] = ""
        self.PIN7 = 0x00000003
        zz_edict['PIN7'] = self.PIN7
        zz_desc['PIN7'] = ""
        super(RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL4, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL5(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN4 = 0x00000000
        zz_edict['PIN4'] = self.PIN4
        zz_desc['PIN4'] = ""
        self.PIN5 = 0x00000001
        zz_edict['PIN5'] = self.PIN5
        zz_desc['PIN5'] = ""
        self.PIN6 = 0x00000002
        zz_edict['PIN6'] = self.PIN6
        zz_desc['PIN6'] = ""
        self.PIN7 = 0x00000003
        zz_edict['PIN7'] = self.PIN7
        zz_desc['PIN7'] = ""
        super(RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL5, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL6(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN4 = 0x00000000
        zz_edict['PIN4'] = self.PIN4
        zz_desc['PIN4'] = ""
        self.PIN5 = 0x00000001
        zz_edict['PIN5'] = self.PIN5
        zz_desc['PIN5'] = ""
        self.PIN6 = 0x00000002
        zz_edict['PIN6'] = self.PIN6
        zz_desc['PIN6'] = ""
        self.PIN7 = 0x00000003
        zz_edict['PIN7'] = self.PIN7
        zz_desc['PIN7'] = ""
        super(RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL6, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL7(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN4 = 0x00000000
        zz_edict['PIN4'] = self.PIN4
        zz_desc['PIN4'] = ""
        self.PIN5 = 0x00000001
        zz_edict['PIN5'] = self.PIN5
        zz_desc['PIN5'] = ""
        self.PIN6 = 0x00000002
        zz_edict['PIN6'] = self.PIN6
        zz_desc['PIN6'] = ""
        self.PIN7 = 0x00000003
        zz_edict['PIN7'] = self.PIN7
        zz_desc['PIN7'] = ""
        super(RM_Enum_GPIO_EXTIPINSELL_EXTIPINSEL7, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL8(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN8 = 0x00000000
        zz_edict['PIN8'] = self.PIN8
        zz_desc['PIN8'] = ""
        self.PIN9 = 0x00000001
        zz_edict['PIN9'] = self.PIN9
        zz_desc['PIN9'] = ""
        self.PIN10 = 0x00000002
        zz_edict['PIN10'] = self.PIN10
        zz_desc['PIN10'] = ""
        self.PIN11 = 0x00000003
        zz_edict['PIN11'] = self.PIN11
        zz_desc['PIN11'] = ""
        super(RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL8, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL9(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN8 = 0x00000000
        zz_edict['PIN8'] = self.PIN8
        zz_desc['PIN8'] = ""
        self.PIN9 = 0x00000001
        zz_edict['PIN9'] = self.PIN9
        zz_desc['PIN9'] = ""
        self.PIN10 = 0x00000002
        zz_edict['PIN10'] = self.PIN10
        zz_desc['PIN10'] = ""
        self.PIN11 = 0x00000003
        zz_edict['PIN11'] = self.PIN11
        zz_desc['PIN11'] = ""
        super(RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL9, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL10(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN8 = 0x00000000
        zz_edict['PIN8'] = self.PIN8
        zz_desc['PIN8'] = ""
        self.PIN9 = 0x00000001
        zz_edict['PIN9'] = self.PIN9
        zz_desc['PIN9'] = ""
        self.PIN10 = 0x00000002
        zz_edict['PIN10'] = self.PIN10
        zz_desc['PIN10'] = ""
        self.PIN11 = 0x00000003
        zz_edict['PIN11'] = self.PIN11
        zz_desc['PIN11'] = ""
        super(RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL10, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL11(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN8 = 0x00000000
        zz_edict['PIN8'] = self.PIN8
        zz_desc['PIN8'] = ""
        self.PIN9 = 0x00000001
        zz_edict['PIN9'] = self.PIN9
        zz_desc['PIN9'] = ""
        self.PIN10 = 0x00000002
        zz_edict['PIN10'] = self.PIN10
        zz_desc['PIN10'] = ""
        self.PIN11 = 0x00000003
        zz_edict['PIN11'] = self.PIN11
        zz_desc['PIN11'] = ""
        super(RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL11, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL12(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN12 = 0x00000000
        zz_edict['PIN12'] = self.PIN12
        zz_desc['PIN12'] = ""
        self.PIN13 = 0x00000001
        zz_edict['PIN13'] = self.PIN13
        zz_desc['PIN13'] = ""
        self.PIN14 = 0x00000002
        zz_edict['PIN14'] = self.PIN14
        zz_desc['PIN14'] = ""
        self.PIN15 = 0x00000003
        zz_edict['PIN15'] = self.PIN15
        zz_desc['PIN15'] = ""
        super(RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL12, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL13(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN12 = 0x00000000
        zz_edict['PIN12'] = self.PIN12
        zz_desc['PIN12'] = ""
        self.PIN13 = 0x00000001
        zz_edict['PIN13'] = self.PIN13
        zz_desc['PIN13'] = ""
        self.PIN14 = 0x00000002
        zz_edict['PIN14'] = self.PIN14
        zz_desc['PIN14'] = ""
        self.PIN15 = 0x00000003
        zz_edict['PIN15'] = self.PIN15
        zz_desc['PIN15'] = ""
        super(RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL13, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL14(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN12 = 0x00000000
        zz_edict['PIN12'] = self.PIN12
        zz_desc['PIN12'] = ""
        self.PIN13 = 0x00000001
        zz_edict['PIN13'] = self.PIN13
        zz_desc['PIN13'] = ""
        self.PIN14 = 0x00000002
        zz_edict['PIN14'] = self.PIN14
        zz_desc['PIN14'] = ""
        self.PIN15 = 0x00000003
        zz_edict['PIN15'] = self.PIN15
        zz_desc['PIN15'] = ""
        super(RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL14, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL15(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PIN12 = 0x00000000
        zz_edict['PIN12'] = self.PIN12
        zz_desc['PIN12'] = ""
        self.PIN13 = 0x00000001
        zz_edict['PIN13'] = self.PIN13
        zz_desc['PIN13'] = ""
        self.PIN14 = 0x00000002
        zz_edict['PIN14'] = self.PIN14
        zz_desc['PIN14'] = ""
        self.PIN15 = 0x00000003
        zz_edict['PIN15'] = self.PIN15
        zz_desc['PIN15'] = ""
        super(RM_Enum_GPIO_EXTIPINSELH_EXTIPINSEL15, self).__init__(
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


class RM_Enum_GPIO_ROUTELOC1_ETMTCLKLOC(Base_RM_Enum):
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
        super(RM_Enum_GPIO_ROUTELOC1_ETMTCLKLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_ROUTELOC1_ETMTD0LOC(Base_RM_Enum):
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
        super(RM_Enum_GPIO_ROUTELOC1_ETMTD0LOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_ROUTELOC1_ETMTD1LOC(Base_RM_Enum):
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
        super(RM_Enum_GPIO_ROUTELOC1_ETMTD1LOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_ROUTELOC1_ETMTD2LOC(Base_RM_Enum):
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
        super(RM_Enum_GPIO_ROUTELOC1_ETMTD2LOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_GPIO_ROUTELOC1_ETMTD3LOC(Base_RM_Enum):
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
        super(RM_Enum_GPIO_ROUTELOC1_ETMTD3LOC, self).__init__(
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


