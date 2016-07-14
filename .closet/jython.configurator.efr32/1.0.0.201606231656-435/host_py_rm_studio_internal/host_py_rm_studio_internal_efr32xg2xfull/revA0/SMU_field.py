
from static import Base_RM_Field
from SMU_enum import *


class RM_Field_SMU_IF_SPBGPRIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_IF_SPBGPRIV, self).__init__(register,
            'SPBGPRIV', 'SMU.IF.SPBGPRIV', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_IFS_SPBGPRIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_IFS_SPBGPRIV, self).__init__(register,
            'SPBGPRIV', 'SMU.IFS.SPBGPRIV', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_IFC_SPBGPRIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_IFC_SPBGPRIV, self).__init__(register,
            'SPBGPRIV', 'SMU.IFC.SPBGPRIV', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_IEN_SPBGPRIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_IEN_SPBGPRIV, self).__init__(register,
            'SPBGPRIV', 'SMU.IEN.SPBGPRIV', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGCTRL_ENABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGCTRL_ENABLE, self).__init__(register,
            'ENABLE', 'SMU.SPBGCTRL.ENABLE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGCTRL_BUSFAULTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGCTRL_BUSFAULTEN, self).__init__(register,
            'BUSFAULTEN', 'SMU.SPBGCTRL.BUSFAULTEN', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_ACMP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_ACMP0, self).__init__(register,
            'ACMP0', 'SMU.SPBGPATD0.ACMP0', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_ACMP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_ACMP1, self).__init__(register,
            'ACMP1', 'SMU.SPBGPATD0.ACMP1', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_ADC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_ADC0, self).__init__(register,
            'ADC0', 'SMU.SPBGPATD0.ADC0', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_AGC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_AGC, self).__init__(register,
            'AGC', 'SMU.SPBGPATD0.AGC', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_BUFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_BUFC, self).__init__(register,
            'BUFC', 'SMU.SPBGPATD0.BUFC', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_CMU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_CMU, self).__init__(register,
            'CMU', 'SMU.SPBGPATD0.CMU', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_CRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_CRC, self).__init__(register,
            'CRC', 'SMU.SPBGPATD0.CRC', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_CRYOTIMER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_CRYOTIMER, self).__init__(register,
            'CRYOTIMER', 'SMU.SPBGPATD0.CRYOTIMER', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_CRYPTO0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_CRYPTO0, self).__init__(register,
            'CRYPTO0', 'SMU.SPBGPATD0.CRYPTO0', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_CRYPTO1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_CRYPTO1, self).__init__(register,
            'CRYPTO1', 'SMU.SPBGPATD0.CRYPTO1', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_CSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_CSEN, self).__init__(register,
            'CSEN', 'SMU.SPBGPATD0.CSEN', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_VDAC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_VDAC0, self).__init__(register,
            'VDAC0', 'SMU.SPBGPATD0.VDAC0', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_PRS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_PRS, self).__init__(register,
            'PRS', 'SMU.SPBGPATD0.PRS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_EMU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_EMU, self).__init__(register,
            'EMU', 'SMU.SPBGPATD0.EMU', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_FPUEH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_FPUEH, self).__init__(register,
            'FPUEH', 'SMU.SPBGPATD0.FPUEH', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_FRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_FRC, self).__init__(register,
            'FRC', 'SMU.SPBGPATD0.FRC', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_GPCRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_GPCRC, self).__init__(register,
            'GPCRC', 'SMU.SPBGPATD0.GPCRC', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_GPIO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_GPIO, self).__init__(register,
            'GPIO', 'SMU.SPBGPATD0.GPIO', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_I2C0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_I2C0, self).__init__(register,
            'I2C0', 'SMU.SPBGPATD0.I2C0', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_I2C1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_I2C1, self).__init__(register,
            'I2C1', 'SMU.SPBGPATD0.I2C1', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_IDAC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_IDAC0, self).__init__(register,
            'IDAC0', 'SMU.SPBGPATD0.IDAC0', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_MSC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_MSC, self).__init__(register,
            'MSC', 'SMU.SPBGPATD0.MSC', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_LDMA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_LDMA, self).__init__(register,
            'LDMA', 'SMU.SPBGPATD0.LDMA', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_LESENSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_LESENSE, self).__init__(register,
            'LESENSE', 'SMU.SPBGPATD0.LESENSE', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_LETIMER0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_LETIMER0, self).__init__(register,
            'LETIMER0', 'SMU.SPBGPATD0.LETIMER0', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_LEUART0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_LEUART0, self).__init__(register,
            'LEUART0', 'SMU.SPBGPATD0.LEUART0', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_MODEM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_MODEM, self).__init__(register,
            'MODEM', 'SMU.SPBGPATD0.MODEM', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_PCNT0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_PCNT0, self).__init__(register,
            'PCNT0', 'SMU.SPBGPATD0.PCNT0', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_PCNT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_PCNT1, self).__init__(register,
            'PCNT1', 'SMU.SPBGPATD0.PCNT1', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_PCNT2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_PCNT2, self).__init__(register,
            'PCNT2', 'SMU.SPBGPATD0.PCNT2', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_PROTIMER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_PROTIMER, self).__init__(register,
            'PROTIMER', 'SMU.SPBGPATD0.PROTIMER', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD0_RAC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD0_RAC, self).__init__(register,
            'RAC', 'SMU.SPBGPATD0.RAC', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_RFSENSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_RFSENSE, self).__init__(register,
            'RFSENSE', 'SMU.SPBGPATD1.RFSENSE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_RMU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_RMU, self).__init__(register,
            'RMU', 'SMU.SPBGPATD1.RMU', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_RTCC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_RTCC, self).__init__(register,
            'RTCC', 'SMU.SPBGPATD1.RTCC', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_SMU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_SMU, self).__init__(register,
            'SMU', 'SMU.SPBGPATD1.SMU', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_SYNTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_SYNTH, self).__init__(register,
            'SYNTH', 'SMU.SPBGPATD1.SYNTH', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_TIMER0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_TIMER0, self).__init__(register,
            'TIMER0', 'SMU.SPBGPATD1.TIMER0', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_TIMER1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_TIMER1, self).__init__(register,
            'TIMER1', 'SMU.SPBGPATD1.TIMER1', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_TRNG0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_TRNG0, self).__init__(register,
            'TRNG0', 'SMU.SPBGPATD1.TRNG0', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_USART0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_USART0, self).__init__(register,
            'USART0', 'SMU.SPBGPATD1.USART0', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_USART1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_USART1, self).__init__(register,
            'USART1', 'SMU.SPBGPATD1.USART1', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_USART2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_USART2, self).__init__(register,
            'USART2', 'SMU.SPBGPATD1.USART2', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_USART3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_USART3, self).__init__(register,
            'USART3', 'SMU.SPBGPATD1.USART3', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_WDOG0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_WDOG0, self).__init__(register,
            'WDOG0', 'SMU.SPBGPATD1.WDOG0', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_WDOG1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_WDOG1, self).__init__(register,
            'WDOG1', 'SMU.SPBGPATD1.WDOG1', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_WTIMER0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_WTIMER0, self).__init__(register,
            'WTIMER0', 'SMU.SPBGPATD1.WTIMER0', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_WTIMER1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_WTIMER1, self).__init__(register,
            'WTIMER1', 'SMU.SPBGPATD1.WTIMER1', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGPATD1_SYSCFG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGPATD1_SYSCFG, self).__init__(register,
            'SYSCFG', 'SMU.SPBGPATD1.SYSCFG', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SMU_SPBGFS_PERIPHID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SMU_SPBGFS_PERIPHID, self).__init__(register,
            'PERIPHID', 'SMU.SPBGFS.PERIPHID', 'read-only',
            "",
            0, 7)
        self.__dict__['zz_frozen'] = True


