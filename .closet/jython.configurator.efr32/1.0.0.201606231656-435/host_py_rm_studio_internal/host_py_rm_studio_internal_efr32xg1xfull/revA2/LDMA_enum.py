
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_LDMA_CH0_REQSEL_SOURCESEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.PRS = 0x00000001
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.ADC0 = 0x00000008
        zz_edict['ADC0'] = self.ADC0
        zz_desc['ADC0'] = ""
        self.USART0 = 0x0000000C
        zz_edict['USART0'] = self.USART0
        zz_desc['USART0'] = ""
        self.USART1 = 0x0000000D
        zz_edict['USART1'] = self.USART1
        zz_desc['USART1'] = ""
        self.LEUART0 = 0x00000010
        zz_edict['LEUART0'] = self.LEUART0
        zz_desc['LEUART0'] = ""
        self.I2C0 = 0x00000014
        zz_edict['I2C0'] = self.I2C0
        zz_desc['I2C0'] = ""
        self.TIMER0 = 0x00000018
        zz_edict['TIMER0'] = self.TIMER0
        zz_desc['TIMER0'] = ""
        self.TIMER1 = 0x00000019
        zz_edict['TIMER1'] = self.TIMER1
        zz_desc['TIMER1'] = ""
        self.PROTIMER = 0x00000024
        zz_edict['PROTIMER'] = self.PROTIMER
        zz_desc['PROTIMER'] = ""
        self.MODEM = 0x00000026
        zz_edict['MODEM'] = self.MODEM
        zz_desc['MODEM'] = ""
        self.AGC = 0x00000027
        zz_edict['AGC'] = self.AGC
        zz_desc['AGC'] = ""
        self.MSC = 0x00000030
        zz_edict['MSC'] = self.MSC
        zz_desc['MSC'] = ""
        self.CRYPTO = 0x00000031
        zz_edict['CRYPTO'] = self.CRYPTO
        zz_desc['CRYPTO'] = ""
        super(RM_Enum_LDMA_CH0_REQSEL_SOURCESEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH0_CFG_ARBSLOTS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.EIGHT = 0x00000003
        zz_edict['EIGHT'] = self.EIGHT
        zz_desc['EIGHT'] = ""
        super(RM_Enum_LDMA_CH0_CFG_ARBSLOTS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH0_CTRL_STRUCTTYPE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.TRANSFER = 0x00000000
        zz_edict['TRANSFER'] = self.TRANSFER
        zz_desc['TRANSFER'] = ""
        self.SYNCHRONIZE = 0x00000001
        zz_edict['SYNCHRONIZE'] = self.SYNCHRONIZE
        zz_desc['SYNCHRONIZE'] = ""
        self.WRITE = 0x00000002
        zz_edict['WRITE'] = self.WRITE
        zz_desc['WRITE'] = ""
        super(RM_Enum_LDMA_CH0_CTRL_STRUCTTYPE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH0_CTRL_BLOCKSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.UNIT1 = 0x00000000
        zz_edict['UNIT1'] = self.UNIT1
        zz_desc['UNIT1'] = ""
        self.UNIT2 = 0x00000001
        zz_edict['UNIT2'] = self.UNIT2
        zz_desc['UNIT2'] = ""
        self.UNIT3 = 0x00000002
        zz_edict['UNIT3'] = self.UNIT3
        zz_desc['UNIT3'] = ""
        self.UNIT4 = 0x00000003
        zz_edict['UNIT4'] = self.UNIT4
        zz_desc['UNIT4'] = ""
        self.UNIT6 = 0x00000004
        zz_edict['UNIT6'] = self.UNIT6
        zz_desc['UNIT6'] = ""
        self.UNIT8 = 0x00000005
        zz_edict['UNIT8'] = self.UNIT8
        zz_desc['UNIT8'] = ""
        self.UNIT16 = 0x00000007
        zz_edict['UNIT16'] = self.UNIT16
        zz_desc['UNIT16'] = ""
        self.UNIT32 = 0x00000009
        zz_edict['UNIT32'] = self.UNIT32
        zz_desc['UNIT32'] = ""
        self.UNIT64 = 0x0000000A
        zz_edict['UNIT64'] = self.UNIT64
        zz_desc['UNIT64'] = ""
        self.UNIT128 = 0x0000000B
        zz_edict['UNIT128'] = self.UNIT128
        zz_desc['UNIT128'] = ""
        self.UNIT256 = 0x0000000C
        zz_edict['UNIT256'] = self.UNIT256
        zz_desc['UNIT256'] = ""
        self.UNIT512 = 0x0000000D
        zz_edict['UNIT512'] = self.UNIT512
        zz_desc['UNIT512'] = ""
        self.UNIT1024 = 0x0000000E
        zz_edict['UNIT1024'] = self.UNIT1024
        zz_desc['UNIT1024'] = ""
        self.ALL = 0x0000000F
        zz_edict['ALL'] = self.ALL
        zz_desc['ALL'] = ""
        super(RM_Enum_LDMA_CH0_CTRL_BLOCKSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH0_CTRL_SRCINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH0_CTRL_SRCINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH0_CTRL_SIZE(Base_RM_Enum):
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
        super(RM_Enum_LDMA_CH0_CTRL_SIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH0_CTRL_DSTINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH0_CTRL_DSTINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH1_REQSEL_SOURCESEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.PRS = 0x00000001
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.ADC0 = 0x00000008
        zz_edict['ADC0'] = self.ADC0
        zz_desc['ADC0'] = ""
        self.USART0 = 0x0000000C
        zz_edict['USART0'] = self.USART0
        zz_desc['USART0'] = ""
        self.USART1 = 0x0000000D
        zz_edict['USART1'] = self.USART1
        zz_desc['USART1'] = ""
        self.LEUART0 = 0x00000010
        zz_edict['LEUART0'] = self.LEUART0
        zz_desc['LEUART0'] = ""
        self.I2C0 = 0x00000014
        zz_edict['I2C0'] = self.I2C0
        zz_desc['I2C0'] = ""
        self.TIMER0 = 0x00000018
        zz_edict['TIMER0'] = self.TIMER0
        zz_desc['TIMER0'] = ""
        self.TIMER1 = 0x00000019
        zz_edict['TIMER1'] = self.TIMER1
        zz_desc['TIMER1'] = ""
        self.PROTIMER = 0x00000024
        zz_edict['PROTIMER'] = self.PROTIMER
        zz_desc['PROTIMER'] = ""
        self.MODEM = 0x00000026
        zz_edict['MODEM'] = self.MODEM
        zz_desc['MODEM'] = ""
        self.AGC = 0x00000027
        zz_edict['AGC'] = self.AGC
        zz_desc['AGC'] = ""
        self.MSC = 0x00000030
        zz_edict['MSC'] = self.MSC
        zz_desc['MSC'] = ""
        self.CRYPTO = 0x00000031
        zz_edict['CRYPTO'] = self.CRYPTO
        zz_desc['CRYPTO'] = ""
        super(RM_Enum_LDMA_CH1_REQSEL_SOURCESEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH1_CFG_ARBSLOTS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.EIGHT = 0x00000003
        zz_edict['EIGHT'] = self.EIGHT
        zz_desc['EIGHT'] = ""
        super(RM_Enum_LDMA_CH1_CFG_ARBSLOTS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH1_CTRL_STRUCTTYPE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.TRANSFER = 0x00000000
        zz_edict['TRANSFER'] = self.TRANSFER
        zz_desc['TRANSFER'] = ""
        self.SYNCHRONIZE = 0x00000001
        zz_edict['SYNCHRONIZE'] = self.SYNCHRONIZE
        zz_desc['SYNCHRONIZE'] = ""
        self.WRITE = 0x00000002
        zz_edict['WRITE'] = self.WRITE
        zz_desc['WRITE'] = ""
        super(RM_Enum_LDMA_CH1_CTRL_STRUCTTYPE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH1_CTRL_BLOCKSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.UNIT1 = 0x00000000
        zz_edict['UNIT1'] = self.UNIT1
        zz_desc['UNIT1'] = ""
        self.UNIT2 = 0x00000001
        zz_edict['UNIT2'] = self.UNIT2
        zz_desc['UNIT2'] = ""
        self.UNIT3 = 0x00000002
        zz_edict['UNIT3'] = self.UNIT3
        zz_desc['UNIT3'] = ""
        self.UNIT4 = 0x00000003
        zz_edict['UNIT4'] = self.UNIT4
        zz_desc['UNIT4'] = ""
        self.UNIT6 = 0x00000004
        zz_edict['UNIT6'] = self.UNIT6
        zz_desc['UNIT6'] = ""
        self.UNIT8 = 0x00000005
        zz_edict['UNIT8'] = self.UNIT8
        zz_desc['UNIT8'] = ""
        self.UNIT16 = 0x00000007
        zz_edict['UNIT16'] = self.UNIT16
        zz_desc['UNIT16'] = ""
        self.UNIT32 = 0x00000009
        zz_edict['UNIT32'] = self.UNIT32
        zz_desc['UNIT32'] = ""
        self.UNIT64 = 0x0000000A
        zz_edict['UNIT64'] = self.UNIT64
        zz_desc['UNIT64'] = ""
        self.UNIT128 = 0x0000000B
        zz_edict['UNIT128'] = self.UNIT128
        zz_desc['UNIT128'] = ""
        self.UNIT256 = 0x0000000C
        zz_edict['UNIT256'] = self.UNIT256
        zz_desc['UNIT256'] = ""
        self.UNIT512 = 0x0000000D
        zz_edict['UNIT512'] = self.UNIT512
        zz_desc['UNIT512'] = ""
        self.UNIT1024 = 0x0000000E
        zz_edict['UNIT1024'] = self.UNIT1024
        zz_desc['UNIT1024'] = ""
        self.ALL = 0x0000000F
        zz_edict['ALL'] = self.ALL
        zz_desc['ALL'] = ""
        super(RM_Enum_LDMA_CH1_CTRL_BLOCKSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH1_CTRL_SRCINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH1_CTRL_SRCINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH1_CTRL_SIZE(Base_RM_Enum):
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
        super(RM_Enum_LDMA_CH1_CTRL_SIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH1_CTRL_DSTINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH1_CTRL_DSTINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH2_REQSEL_SOURCESEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.PRS = 0x00000001
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.ADC0 = 0x00000008
        zz_edict['ADC0'] = self.ADC0
        zz_desc['ADC0'] = ""
        self.USART0 = 0x0000000C
        zz_edict['USART0'] = self.USART0
        zz_desc['USART0'] = ""
        self.USART1 = 0x0000000D
        zz_edict['USART1'] = self.USART1
        zz_desc['USART1'] = ""
        self.LEUART0 = 0x00000010
        zz_edict['LEUART0'] = self.LEUART0
        zz_desc['LEUART0'] = ""
        self.I2C0 = 0x00000014
        zz_edict['I2C0'] = self.I2C0
        zz_desc['I2C0'] = ""
        self.TIMER0 = 0x00000018
        zz_edict['TIMER0'] = self.TIMER0
        zz_desc['TIMER0'] = ""
        self.TIMER1 = 0x00000019
        zz_edict['TIMER1'] = self.TIMER1
        zz_desc['TIMER1'] = ""
        self.PROTIMER = 0x00000024
        zz_edict['PROTIMER'] = self.PROTIMER
        zz_desc['PROTIMER'] = ""
        self.MODEM = 0x00000026
        zz_edict['MODEM'] = self.MODEM
        zz_desc['MODEM'] = ""
        self.AGC = 0x00000027
        zz_edict['AGC'] = self.AGC
        zz_desc['AGC'] = ""
        self.MSC = 0x00000030
        zz_edict['MSC'] = self.MSC
        zz_desc['MSC'] = ""
        self.CRYPTO = 0x00000031
        zz_edict['CRYPTO'] = self.CRYPTO
        zz_desc['CRYPTO'] = ""
        super(RM_Enum_LDMA_CH2_REQSEL_SOURCESEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH2_CFG_ARBSLOTS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.EIGHT = 0x00000003
        zz_edict['EIGHT'] = self.EIGHT
        zz_desc['EIGHT'] = ""
        super(RM_Enum_LDMA_CH2_CFG_ARBSLOTS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH2_CTRL_STRUCTTYPE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.TRANSFER = 0x00000000
        zz_edict['TRANSFER'] = self.TRANSFER
        zz_desc['TRANSFER'] = ""
        self.SYNCHRONIZE = 0x00000001
        zz_edict['SYNCHRONIZE'] = self.SYNCHRONIZE
        zz_desc['SYNCHRONIZE'] = ""
        self.WRITE = 0x00000002
        zz_edict['WRITE'] = self.WRITE
        zz_desc['WRITE'] = ""
        super(RM_Enum_LDMA_CH2_CTRL_STRUCTTYPE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH2_CTRL_BLOCKSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.UNIT1 = 0x00000000
        zz_edict['UNIT1'] = self.UNIT1
        zz_desc['UNIT1'] = ""
        self.UNIT2 = 0x00000001
        zz_edict['UNIT2'] = self.UNIT2
        zz_desc['UNIT2'] = ""
        self.UNIT3 = 0x00000002
        zz_edict['UNIT3'] = self.UNIT3
        zz_desc['UNIT3'] = ""
        self.UNIT4 = 0x00000003
        zz_edict['UNIT4'] = self.UNIT4
        zz_desc['UNIT4'] = ""
        self.UNIT6 = 0x00000004
        zz_edict['UNIT6'] = self.UNIT6
        zz_desc['UNIT6'] = ""
        self.UNIT8 = 0x00000005
        zz_edict['UNIT8'] = self.UNIT8
        zz_desc['UNIT8'] = ""
        self.UNIT16 = 0x00000007
        zz_edict['UNIT16'] = self.UNIT16
        zz_desc['UNIT16'] = ""
        self.UNIT32 = 0x00000009
        zz_edict['UNIT32'] = self.UNIT32
        zz_desc['UNIT32'] = ""
        self.UNIT64 = 0x0000000A
        zz_edict['UNIT64'] = self.UNIT64
        zz_desc['UNIT64'] = ""
        self.UNIT128 = 0x0000000B
        zz_edict['UNIT128'] = self.UNIT128
        zz_desc['UNIT128'] = ""
        self.UNIT256 = 0x0000000C
        zz_edict['UNIT256'] = self.UNIT256
        zz_desc['UNIT256'] = ""
        self.UNIT512 = 0x0000000D
        zz_edict['UNIT512'] = self.UNIT512
        zz_desc['UNIT512'] = ""
        self.UNIT1024 = 0x0000000E
        zz_edict['UNIT1024'] = self.UNIT1024
        zz_desc['UNIT1024'] = ""
        self.ALL = 0x0000000F
        zz_edict['ALL'] = self.ALL
        zz_desc['ALL'] = ""
        super(RM_Enum_LDMA_CH2_CTRL_BLOCKSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH2_CTRL_SRCINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH2_CTRL_SRCINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH2_CTRL_SIZE(Base_RM_Enum):
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
        super(RM_Enum_LDMA_CH2_CTRL_SIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH2_CTRL_DSTINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH2_CTRL_DSTINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH3_REQSEL_SOURCESEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.PRS = 0x00000001
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.ADC0 = 0x00000008
        zz_edict['ADC0'] = self.ADC0
        zz_desc['ADC0'] = ""
        self.USART0 = 0x0000000C
        zz_edict['USART0'] = self.USART0
        zz_desc['USART0'] = ""
        self.USART1 = 0x0000000D
        zz_edict['USART1'] = self.USART1
        zz_desc['USART1'] = ""
        self.LEUART0 = 0x00000010
        zz_edict['LEUART0'] = self.LEUART0
        zz_desc['LEUART0'] = ""
        self.I2C0 = 0x00000014
        zz_edict['I2C0'] = self.I2C0
        zz_desc['I2C0'] = ""
        self.TIMER0 = 0x00000018
        zz_edict['TIMER0'] = self.TIMER0
        zz_desc['TIMER0'] = ""
        self.TIMER1 = 0x00000019
        zz_edict['TIMER1'] = self.TIMER1
        zz_desc['TIMER1'] = ""
        self.PROTIMER = 0x00000024
        zz_edict['PROTIMER'] = self.PROTIMER
        zz_desc['PROTIMER'] = ""
        self.MODEM = 0x00000026
        zz_edict['MODEM'] = self.MODEM
        zz_desc['MODEM'] = ""
        self.AGC = 0x00000027
        zz_edict['AGC'] = self.AGC
        zz_desc['AGC'] = ""
        self.MSC = 0x00000030
        zz_edict['MSC'] = self.MSC
        zz_desc['MSC'] = ""
        self.CRYPTO = 0x00000031
        zz_edict['CRYPTO'] = self.CRYPTO
        zz_desc['CRYPTO'] = ""
        super(RM_Enum_LDMA_CH3_REQSEL_SOURCESEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH3_CFG_ARBSLOTS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.EIGHT = 0x00000003
        zz_edict['EIGHT'] = self.EIGHT
        zz_desc['EIGHT'] = ""
        super(RM_Enum_LDMA_CH3_CFG_ARBSLOTS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH3_CTRL_STRUCTTYPE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.TRANSFER = 0x00000000
        zz_edict['TRANSFER'] = self.TRANSFER
        zz_desc['TRANSFER'] = ""
        self.SYNCHRONIZE = 0x00000001
        zz_edict['SYNCHRONIZE'] = self.SYNCHRONIZE
        zz_desc['SYNCHRONIZE'] = ""
        self.WRITE = 0x00000002
        zz_edict['WRITE'] = self.WRITE
        zz_desc['WRITE'] = ""
        super(RM_Enum_LDMA_CH3_CTRL_STRUCTTYPE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH3_CTRL_BLOCKSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.UNIT1 = 0x00000000
        zz_edict['UNIT1'] = self.UNIT1
        zz_desc['UNIT1'] = ""
        self.UNIT2 = 0x00000001
        zz_edict['UNIT2'] = self.UNIT2
        zz_desc['UNIT2'] = ""
        self.UNIT3 = 0x00000002
        zz_edict['UNIT3'] = self.UNIT3
        zz_desc['UNIT3'] = ""
        self.UNIT4 = 0x00000003
        zz_edict['UNIT4'] = self.UNIT4
        zz_desc['UNIT4'] = ""
        self.UNIT6 = 0x00000004
        zz_edict['UNIT6'] = self.UNIT6
        zz_desc['UNIT6'] = ""
        self.UNIT8 = 0x00000005
        zz_edict['UNIT8'] = self.UNIT8
        zz_desc['UNIT8'] = ""
        self.UNIT16 = 0x00000007
        zz_edict['UNIT16'] = self.UNIT16
        zz_desc['UNIT16'] = ""
        self.UNIT32 = 0x00000009
        zz_edict['UNIT32'] = self.UNIT32
        zz_desc['UNIT32'] = ""
        self.UNIT64 = 0x0000000A
        zz_edict['UNIT64'] = self.UNIT64
        zz_desc['UNIT64'] = ""
        self.UNIT128 = 0x0000000B
        zz_edict['UNIT128'] = self.UNIT128
        zz_desc['UNIT128'] = ""
        self.UNIT256 = 0x0000000C
        zz_edict['UNIT256'] = self.UNIT256
        zz_desc['UNIT256'] = ""
        self.UNIT512 = 0x0000000D
        zz_edict['UNIT512'] = self.UNIT512
        zz_desc['UNIT512'] = ""
        self.UNIT1024 = 0x0000000E
        zz_edict['UNIT1024'] = self.UNIT1024
        zz_desc['UNIT1024'] = ""
        self.ALL = 0x0000000F
        zz_edict['ALL'] = self.ALL
        zz_desc['ALL'] = ""
        super(RM_Enum_LDMA_CH3_CTRL_BLOCKSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH3_CTRL_SRCINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH3_CTRL_SRCINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH3_CTRL_SIZE(Base_RM_Enum):
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
        super(RM_Enum_LDMA_CH3_CTRL_SIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH3_CTRL_DSTINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH3_CTRL_DSTINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH4_REQSEL_SOURCESEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.PRS = 0x00000001
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.ADC0 = 0x00000008
        zz_edict['ADC0'] = self.ADC0
        zz_desc['ADC0'] = ""
        self.USART0 = 0x0000000C
        zz_edict['USART0'] = self.USART0
        zz_desc['USART0'] = ""
        self.USART1 = 0x0000000D
        zz_edict['USART1'] = self.USART1
        zz_desc['USART1'] = ""
        self.LEUART0 = 0x00000010
        zz_edict['LEUART0'] = self.LEUART0
        zz_desc['LEUART0'] = ""
        self.I2C0 = 0x00000014
        zz_edict['I2C0'] = self.I2C0
        zz_desc['I2C0'] = ""
        self.TIMER0 = 0x00000018
        zz_edict['TIMER0'] = self.TIMER0
        zz_desc['TIMER0'] = ""
        self.TIMER1 = 0x00000019
        zz_edict['TIMER1'] = self.TIMER1
        zz_desc['TIMER1'] = ""
        self.PROTIMER = 0x00000024
        zz_edict['PROTIMER'] = self.PROTIMER
        zz_desc['PROTIMER'] = ""
        self.MODEM = 0x00000026
        zz_edict['MODEM'] = self.MODEM
        zz_desc['MODEM'] = ""
        self.AGC = 0x00000027
        zz_edict['AGC'] = self.AGC
        zz_desc['AGC'] = ""
        self.MSC = 0x00000030
        zz_edict['MSC'] = self.MSC
        zz_desc['MSC'] = ""
        self.CRYPTO = 0x00000031
        zz_edict['CRYPTO'] = self.CRYPTO
        zz_desc['CRYPTO'] = ""
        super(RM_Enum_LDMA_CH4_REQSEL_SOURCESEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH4_CFG_ARBSLOTS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.EIGHT = 0x00000003
        zz_edict['EIGHT'] = self.EIGHT
        zz_desc['EIGHT'] = ""
        super(RM_Enum_LDMA_CH4_CFG_ARBSLOTS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH4_CTRL_STRUCTTYPE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.TRANSFER = 0x00000000
        zz_edict['TRANSFER'] = self.TRANSFER
        zz_desc['TRANSFER'] = ""
        self.SYNCHRONIZE = 0x00000001
        zz_edict['SYNCHRONIZE'] = self.SYNCHRONIZE
        zz_desc['SYNCHRONIZE'] = ""
        self.WRITE = 0x00000002
        zz_edict['WRITE'] = self.WRITE
        zz_desc['WRITE'] = ""
        super(RM_Enum_LDMA_CH4_CTRL_STRUCTTYPE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH4_CTRL_BLOCKSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.UNIT1 = 0x00000000
        zz_edict['UNIT1'] = self.UNIT1
        zz_desc['UNIT1'] = ""
        self.UNIT2 = 0x00000001
        zz_edict['UNIT2'] = self.UNIT2
        zz_desc['UNIT2'] = ""
        self.UNIT3 = 0x00000002
        zz_edict['UNIT3'] = self.UNIT3
        zz_desc['UNIT3'] = ""
        self.UNIT4 = 0x00000003
        zz_edict['UNIT4'] = self.UNIT4
        zz_desc['UNIT4'] = ""
        self.UNIT6 = 0x00000004
        zz_edict['UNIT6'] = self.UNIT6
        zz_desc['UNIT6'] = ""
        self.UNIT8 = 0x00000005
        zz_edict['UNIT8'] = self.UNIT8
        zz_desc['UNIT8'] = ""
        self.UNIT16 = 0x00000007
        zz_edict['UNIT16'] = self.UNIT16
        zz_desc['UNIT16'] = ""
        self.UNIT32 = 0x00000009
        zz_edict['UNIT32'] = self.UNIT32
        zz_desc['UNIT32'] = ""
        self.UNIT64 = 0x0000000A
        zz_edict['UNIT64'] = self.UNIT64
        zz_desc['UNIT64'] = ""
        self.UNIT128 = 0x0000000B
        zz_edict['UNIT128'] = self.UNIT128
        zz_desc['UNIT128'] = ""
        self.UNIT256 = 0x0000000C
        zz_edict['UNIT256'] = self.UNIT256
        zz_desc['UNIT256'] = ""
        self.UNIT512 = 0x0000000D
        zz_edict['UNIT512'] = self.UNIT512
        zz_desc['UNIT512'] = ""
        self.UNIT1024 = 0x0000000E
        zz_edict['UNIT1024'] = self.UNIT1024
        zz_desc['UNIT1024'] = ""
        self.ALL = 0x0000000F
        zz_edict['ALL'] = self.ALL
        zz_desc['ALL'] = ""
        super(RM_Enum_LDMA_CH4_CTRL_BLOCKSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH4_CTRL_SRCINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH4_CTRL_SRCINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH4_CTRL_SIZE(Base_RM_Enum):
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
        super(RM_Enum_LDMA_CH4_CTRL_SIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH4_CTRL_DSTINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH4_CTRL_DSTINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH5_REQSEL_SOURCESEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.PRS = 0x00000001
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.ADC0 = 0x00000008
        zz_edict['ADC0'] = self.ADC0
        zz_desc['ADC0'] = ""
        self.USART0 = 0x0000000C
        zz_edict['USART0'] = self.USART0
        zz_desc['USART0'] = ""
        self.USART1 = 0x0000000D
        zz_edict['USART1'] = self.USART1
        zz_desc['USART1'] = ""
        self.LEUART0 = 0x00000010
        zz_edict['LEUART0'] = self.LEUART0
        zz_desc['LEUART0'] = ""
        self.I2C0 = 0x00000014
        zz_edict['I2C0'] = self.I2C0
        zz_desc['I2C0'] = ""
        self.TIMER0 = 0x00000018
        zz_edict['TIMER0'] = self.TIMER0
        zz_desc['TIMER0'] = ""
        self.TIMER1 = 0x00000019
        zz_edict['TIMER1'] = self.TIMER1
        zz_desc['TIMER1'] = ""
        self.PROTIMER = 0x00000024
        zz_edict['PROTIMER'] = self.PROTIMER
        zz_desc['PROTIMER'] = ""
        self.MODEM = 0x00000026
        zz_edict['MODEM'] = self.MODEM
        zz_desc['MODEM'] = ""
        self.AGC = 0x00000027
        zz_edict['AGC'] = self.AGC
        zz_desc['AGC'] = ""
        self.MSC = 0x00000030
        zz_edict['MSC'] = self.MSC
        zz_desc['MSC'] = ""
        self.CRYPTO = 0x00000031
        zz_edict['CRYPTO'] = self.CRYPTO
        zz_desc['CRYPTO'] = ""
        super(RM_Enum_LDMA_CH5_REQSEL_SOURCESEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH5_CFG_ARBSLOTS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.EIGHT = 0x00000003
        zz_edict['EIGHT'] = self.EIGHT
        zz_desc['EIGHT'] = ""
        super(RM_Enum_LDMA_CH5_CFG_ARBSLOTS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH5_CTRL_STRUCTTYPE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.TRANSFER = 0x00000000
        zz_edict['TRANSFER'] = self.TRANSFER
        zz_desc['TRANSFER'] = ""
        self.SYNCHRONIZE = 0x00000001
        zz_edict['SYNCHRONIZE'] = self.SYNCHRONIZE
        zz_desc['SYNCHRONIZE'] = ""
        self.WRITE = 0x00000002
        zz_edict['WRITE'] = self.WRITE
        zz_desc['WRITE'] = ""
        super(RM_Enum_LDMA_CH5_CTRL_STRUCTTYPE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH5_CTRL_BLOCKSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.UNIT1 = 0x00000000
        zz_edict['UNIT1'] = self.UNIT1
        zz_desc['UNIT1'] = ""
        self.UNIT2 = 0x00000001
        zz_edict['UNIT2'] = self.UNIT2
        zz_desc['UNIT2'] = ""
        self.UNIT3 = 0x00000002
        zz_edict['UNIT3'] = self.UNIT3
        zz_desc['UNIT3'] = ""
        self.UNIT4 = 0x00000003
        zz_edict['UNIT4'] = self.UNIT4
        zz_desc['UNIT4'] = ""
        self.UNIT6 = 0x00000004
        zz_edict['UNIT6'] = self.UNIT6
        zz_desc['UNIT6'] = ""
        self.UNIT8 = 0x00000005
        zz_edict['UNIT8'] = self.UNIT8
        zz_desc['UNIT8'] = ""
        self.UNIT16 = 0x00000007
        zz_edict['UNIT16'] = self.UNIT16
        zz_desc['UNIT16'] = ""
        self.UNIT32 = 0x00000009
        zz_edict['UNIT32'] = self.UNIT32
        zz_desc['UNIT32'] = ""
        self.UNIT64 = 0x0000000A
        zz_edict['UNIT64'] = self.UNIT64
        zz_desc['UNIT64'] = ""
        self.UNIT128 = 0x0000000B
        zz_edict['UNIT128'] = self.UNIT128
        zz_desc['UNIT128'] = ""
        self.UNIT256 = 0x0000000C
        zz_edict['UNIT256'] = self.UNIT256
        zz_desc['UNIT256'] = ""
        self.UNIT512 = 0x0000000D
        zz_edict['UNIT512'] = self.UNIT512
        zz_desc['UNIT512'] = ""
        self.UNIT1024 = 0x0000000E
        zz_edict['UNIT1024'] = self.UNIT1024
        zz_desc['UNIT1024'] = ""
        self.ALL = 0x0000000F
        zz_edict['ALL'] = self.ALL
        zz_desc['ALL'] = ""
        super(RM_Enum_LDMA_CH5_CTRL_BLOCKSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH5_CTRL_SRCINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH5_CTRL_SRCINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH5_CTRL_SIZE(Base_RM_Enum):
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
        super(RM_Enum_LDMA_CH5_CTRL_SIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH5_CTRL_DSTINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH5_CTRL_DSTINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH6_REQSEL_SOURCESEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.PRS = 0x00000001
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.ADC0 = 0x00000008
        zz_edict['ADC0'] = self.ADC0
        zz_desc['ADC0'] = ""
        self.USART0 = 0x0000000C
        zz_edict['USART0'] = self.USART0
        zz_desc['USART0'] = ""
        self.USART1 = 0x0000000D
        zz_edict['USART1'] = self.USART1
        zz_desc['USART1'] = ""
        self.LEUART0 = 0x00000010
        zz_edict['LEUART0'] = self.LEUART0
        zz_desc['LEUART0'] = ""
        self.I2C0 = 0x00000014
        zz_edict['I2C0'] = self.I2C0
        zz_desc['I2C0'] = ""
        self.TIMER0 = 0x00000018
        zz_edict['TIMER0'] = self.TIMER0
        zz_desc['TIMER0'] = ""
        self.TIMER1 = 0x00000019
        zz_edict['TIMER1'] = self.TIMER1
        zz_desc['TIMER1'] = ""
        self.PROTIMER = 0x00000024
        zz_edict['PROTIMER'] = self.PROTIMER
        zz_desc['PROTIMER'] = ""
        self.MODEM = 0x00000026
        zz_edict['MODEM'] = self.MODEM
        zz_desc['MODEM'] = ""
        self.AGC = 0x00000027
        zz_edict['AGC'] = self.AGC
        zz_desc['AGC'] = ""
        self.MSC = 0x00000030
        zz_edict['MSC'] = self.MSC
        zz_desc['MSC'] = ""
        self.CRYPTO = 0x00000031
        zz_edict['CRYPTO'] = self.CRYPTO
        zz_desc['CRYPTO'] = ""
        super(RM_Enum_LDMA_CH6_REQSEL_SOURCESEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH6_CFG_ARBSLOTS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.EIGHT = 0x00000003
        zz_edict['EIGHT'] = self.EIGHT
        zz_desc['EIGHT'] = ""
        super(RM_Enum_LDMA_CH6_CFG_ARBSLOTS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH6_CTRL_STRUCTTYPE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.TRANSFER = 0x00000000
        zz_edict['TRANSFER'] = self.TRANSFER
        zz_desc['TRANSFER'] = ""
        self.SYNCHRONIZE = 0x00000001
        zz_edict['SYNCHRONIZE'] = self.SYNCHRONIZE
        zz_desc['SYNCHRONIZE'] = ""
        self.WRITE = 0x00000002
        zz_edict['WRITE'] = self.WRITE
        zz_desc['WRITE'] = ""
        super(RM_Enum_LDMA_CH6_CTRL_STRUCTTYPE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH6_CTRL_BLOCKSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.UNIT1 = 0x00000000
        zz_edict['UNIT1'] = self.UNIT1
        zz_desc['UNIT1'] = ""
        self.UNIT2 = 0x00000001
        zz_edict['UNIT2'] = self.UNIT2
        zz_desc['UNIT2'] = ""
        self.UNIT3 = 0x00000002
        zz_edict['UNIT3'] = self.UNIT3
        zz_desc['UNIT3'] = ""
        self.UNIT4 = 0x00000003
        zz_edict['UNIT4'] = self.UNIT4
        zz_desc['UNIT4'] = ""
        self.UNIT6 = 0x00000004
        zz_edict['UNIT6'] = self.UNIT6
        zz_desc['UNIT6'] = ""
        self.UNIT8 = 0x00000005
        zz_edict['UNIT8'] = self.UNIT8
        zz_desc['UNIT8'] = ""
        self.UNIT16 = 0x00000007
        zz_edict['UNIT16'] = self.UNIT16
        zz_desc['UNIT16'] = ""
        self.UNIT32 = 0x00000009
        zz_edict['UNIT32'] = self.UNIT32
        zz_desc['UNIT32'] = ""
        self.UNIT64 = 0x0000000A
        zz_edict['UNIT64'] = self.UNIT64
        zz_desc['UNIT64'] = ""
        self.UNIT128 = 0x0000000B
        zz_edict['UNIT128'] = self.UNIT128
        zz_desc['UNIT128'] = ""
        self.UNIT256 = 0x0000000C
        zz_edict['UNIT256'] = self.UNIT256
        zz_desc['UNIT256'] = ""
        self.UNIT512 = 0x0000000D
        zz_edict['UNIT512'] = self.UNIT512
        zz_desc['UNIT512'] = ""
        self.UNIT1024 = 0x0000000E
        zz_edict['UNIT1024'] = self.UNIT1024
        zz_desc['UNIT1024'] = ""
        self.ALL = 0x0000000F
        zz_edict['ALL'] = self.ALL
        zz_desc['ALL'] = ""
        super(RM_Enum_LDMA_CH6_CTRL_BLOCKSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH6_CTRL_SRCINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH6_CTRL_SRCINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH6_CTRL_SIZE(Base_RM_Enum):
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
        super(RM_Enum_LDMA_CH6_CTRL_SIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH6_CTRL_DSTINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH6_CTRL_DSTINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH7_REQSEL_SOURCESEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NONE = 0x00000000
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        self.PRS = 0x00000001
        zz_edict['PRS'] = self.PRS
        zz_desc['PRS'] = ""
        self.ADC0 = 0x00000008
        zz_edict['ADC0'] = self.ADC0
        zz_desc['ADC0'] = ""
        self.USART0 = 0x0000000C
        zz_edict['USART0'] = self.USART0
        zz_desc['USART0'] = ""
        self.USART1 = 0x0000000D
        zz_edict['USART1'] = self.USART1
        zz_desc['USART1'] = ""
        self.LEUART0 = 0x00000010
        zz_edict['LEUART0'] = self.LEUART0
        zz_desc['LEUART0'] = ""
        self.I2C0 = 0x00000014
        zz_edict['I2C0'] = self.I2C0
        zz_desc['I2C0'] = ""
        self.TIMER0 = 0x00000018
        zz_edict['TIMER0'] = self.TIMER0
        zz_desc['TIMER0'] = ""
        self.TIMER1 = 0x00000019
        zz_edict['TIMER1'] = self.TIMER1
        zz_desc['TIMER1'] = ""
        self.PROTIMER = 0x00000024
        zz_edict['PROTIMER'] = self.PROTIMER
        zz_desc['PROTIMER'] = ""
        self.MODEM = 0x00000026
        zz_edict['MODEM'] = self.MODEM
        zz_desc['MODEM'] = ""
        self.AGC = 0x00000027
        zz_edict['AGC'] = self.AGC
        zz_desc['AGC'] = ""
        self.MSC = 0x00000030
        zz_edict['MSC'] = self.MSC
        zz_desc['MSC'] = ""
        self.CRYPTO = 0x00000031
        zz_edict['CRYPTO'] = self.CRYPTO
        zz_desc['CRYPTO'] = ""
        super(RM_Enum_LDMA_CH7_REQSEL_SOURCESEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH7_CFG_ARBSLOTS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.EIGHT = 0x00000003
        zz_edict['EIGHT'] = self.EIGHT
        zz_desc['EIGHT'] = ""
        super(RM_Enum_LDMA_CH7_CFG_ARBSLOTS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH7_CTRL_STRUCTTYPE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.TRANSFER = 0x00000000
        zz_edict['TRANSFER'] = self.TRANSFER
        zz_desc['TRANSFER'] = ""
        self.SYNCHRONIZE = 0x00000001
        zz_edict['SYNCHRONIZE'] = self.SYNCHRONIZE
        zz_desc['SYNCHRONIZE'] = ""
        self.WRITE = 0x00000002
        zz_edict['WRITE'] = self.WRITE
        zz_desc['WRITE'] = ""
        super(RM_Enum_LDMA_CH7_CTRL_STRUCTTYPE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH7_CTRL_BLOCKSIZE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.UNIT1 = 0x00000000
        zz_edict['UNIT1'] = self.UNIT1
        zz_desc['UNIT1'] = ""
        self.UNIT2 = 0x00000001
        zz_edict['UNIT2'] = self.UNIT2
        zz_desc['UNIT2'] = ""
        self.UNIT3 = 0x00000002
        zz_edict['UNIT3'] = self.UNIT3
        zz_desc['UNIT3'] = ""
        self.UNIT4 = 0x00000003
        zz_edict['UNIT4'] = self.UNIT4
        zz_desc['UNIT4'] = ""
        self.UNIT6 = 0x00000004
        zz_edict['UNIT6'] = self.UNIT6
        zz_desc['UNIT6'] = ""
        self.UNIT8 = 0x00000005
        zz_edict['UNIT8'] = self.UNIT8
        zz_desc['UNIT8'] = ""
        self.UNIT16 = 0x00000007
        zz_edict['UNIT16'] = self.UNIT16
        zz_desc['UNIT16'] = ""
        self.UNIT32 = 0x00000009
        zz_edict['UNIT32'] = self.UNIT32
        zz_desc['UNIT32'] = ""
        self.UNIT64 = 0x0000000A
        zz_edict['UNIT64'] = self.UNIT64
        zz_desc['UNIT64'] = ""
        self.UNIT128 = 0x0000000B
        zz_edict['UNIT128'] = self.UNIT128
        zz_desc['UNIT128'] = ""
        self.UNIT256 = 0x0000000C
        zz_edict['UNIT256'] = self.UNIT256
        zz_desc['UNIT256'] = ""
        self.UNIT512 = 0x0000000D
        zz_edict['UNIT512'] = self.UNIT512
        zz_desc['UNIT512'] = ""
        self.UNIT1024 = 0x0000000E
        zz_edict['UNIT1024'] = self.UNIT1024
        zz_desc['UNIT1024'] = ""
        self.ALL = 0x0000000F
        zz_edict['ALL'] = self.ALL
        zz_desc['ALL'] = ""
        super(RM_Enum_LDMA_CH7_CTRL_BLOCKSIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH7_CTRL_SRCINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH7_CTRL_SRCINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH7_CTRL_SIZE(Base_RM_Enum):
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
        super(RM_Enum_LDMA_CH7_CTRL_SIZE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_LDMA_CH7_CTRL_DSTINC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ONE = 0x00000000
        zz_edict['ONE'] = self.ONE
        zz_desc['ONE'] = ""
        self.TWO = 0x00000001
        zz_edict['TWO'] = self.TWO
        zz_desc['TWO'] = ""
        self.FOUR = 0x00000002
        zz_edict['FOUR'] = self.FOUR
        zz_desc['FOUR'] = ""
        self.NONE = 0x00000003
        zz_edict['NONE'] = self.NONE
        zz_desc['NONE'] = ""
        super(RM_Enum_LDMA_CH7_CTRL_DSTINC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


