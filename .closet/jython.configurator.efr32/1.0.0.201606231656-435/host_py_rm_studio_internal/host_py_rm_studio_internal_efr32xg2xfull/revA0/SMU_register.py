
from static import Base_RM_Register
from SMU_field import *


class RM_Register_SMU_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SMU_IF, self).__init__(rmio, label,
            0x40022000, 0x00C,
            'IF', 'SMU.IF', 'read-only',
            "",
            0x00000000, 0x00000001)

        self.SPBGPRIV = RM_Field_SMU_IF_SPBGPRIV(self)
        self.zz_fdict['SPBGPRIV'] = self.SPBGPRIV
        self.__dict__['zz_frozen'] = True


class RM_Register_SMU_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SMU_IFS, self).__init__(rmio, label,
            0x40022000, 0x010,
            'IFS', 'SMU.IFS', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.SPBGPRIV = RM_Field_SMU_IFS_SPBGPRIV(self)
        self.zz_fdict['SPBGPRIV'] = self.SPBGPRIV
        self.__dict__['zz_frozen'] = True


class RM_Register_SMU_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SMU_IFC, self).__init__(rmio, label,
            0x40022000, 0x014,
            'IFC', 'SMU.IFC', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.SPBGPRIV = RM_Field_SMU_IFC_SPBGPRIV(self)
        self.zz_fdict['SPBGPRIV'] = self.SPBGPRIV
        self.__dict__['zz_frozen'] = True


class RM_Register_SMU_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SMU_IEN, self).__init__(rmio, label,
            0x40022000, 0x018,
            'IEN', 'SMU.IEN', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.SPBGPRIV = RM_Field_SMU_IEN_SPBGPRIV(self)
        self.zz_fdict['SPBGPRIV'] = self.SPBGPRIV
        self.__dict__['zz_frozen'] = True


class RM_Register_SMU_SPBGCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SMU_SPBGCTRL, self).__init__(rmio, label,
            0x40022000, 0x040,
            'SPBGCTRL', 'SMU.SPBGCTRL', 'read-write',
            "",
            0x00000000, 0x00010001)

        self.ENABLE = RM_Field_SMU_SPBGCTRL_ENABLE(self)
        self.zz_fdict['ENABLE'] = self.ENABLE
        self.BUSFAULTEN = RM_Field_SMU_SPBGCTRL_BUSFAULTEN(self)
        self.zz_fdict['BUSFAULTEN'] = self.BUSFAULTEN
        self.__dict__['zz_frozen'] = True


class RM_Register_SMU_SPBGPATD0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SMU_SPBGPATD0, self).__init__(rmio, label,
            0x40022000, 0x050,
            'SPBGPATD0', 'SMU.SPBGPATD0', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.ACMP0 = RM_Field_SMU_SPBGPATD0_ACMP0(self)
        self.zz_fdict['ACMP0'] = self.ACMP0
        self.ACMP1 = RM_Field_SMU_SPBGPATD0_ACMP1(self)
        self.zz_fdict['ACMP1'] = self.ACMP1
        self.ADC0 = RM_Field_SMU_SPBGPATD0_ADC0(self)
        self.zz_fdict['ADC0'] = self.ADC0
        self.AGC = RM_Field_SMU_SPBGPATD0_AGC(self)
        self.zz_fdict['AGC'] = self.AGC
        self.BUFC = RM_Field_SMU_SPBGPATD0_BUFC(self)
        self.zz_fdict['BUFC'] = self.BUFC
        self.CMU = RM_Field_SMU_SPBGPATD0_CMU(self)
        self.zz_fdict['CMU'] = self.CMU
        self.CRC = RM_Field_SMU_SPBGPATD0_CRC(self)
        self.zz_fdict['CRC'] = self.CRC
        self.CRYOTIMER = RM_Field_SMU_SPBGPATD0_CRYOTIMER(self)
        self.zz_fdict['CRYOTIMER'] = self.CRYOTIMER
        self.CRYPTO0 = RM_Field_SMU_SPBGPATD0_CRYPTO0(self)
        self.zz_fdict['CRYPTO0'] = self.CRYPTO0
        self.CRYPTO1 = RM_Field_SMU_SPBGPATD0_CRYPTO1(self)
        self.zz_fdict['CRYPTO1'] = self.CRYPTO1
        self.CSEN = RM_Field_SMU_SPBGPATD0_CSEN(self)
        self.zz_fdict['CSEN'] = self.CSEN
        self.VDAC0 = RM_Field_SMU_SPBGPATD0_VDAC0(self)
        self.zz_fdict['VDAC0'] = self.VDAC0
        self.PRS = RM_Field_SMU_SPBGPATD0_PRS(self)
        self.zz_fdict['PRS'] = self.PRS
        self.EMU = RM_Field_SMU_SPBGPATD0_EMU(self)
        self.zz_fdict['EMU'] = self.EMU
        self.FPUEH = RM_Field_SMU_SPBGPATD0_FPUEH(self)
        self.zz_fdict['FPUEH'] = self.FPUEH
        self.FRC = RM_Field_SMU_SPBGPATD0_FRC(self)
        self.zz_fdict['FRC'] = self.FRC
        self.GPCRC = RM_Field_SMU_SPBGPATD0_GPCRC(self)
        self.zz_fdict['GPCRC'] = self.GPCRC
        self.GPIO = RM_Field_SMU_SPBGPATD0_GPIO(self)
        self.zz_fdict['GPIO'] = self.GPIO
        self.I2C0 = RM_Field_SMU_SPBGPATD0_I2C0(self)
        self.zz_fdict['I2C0'] = self.I2C0
        self.I2C1 = RM_Field_SMU_SPBGPATD0_I2C1(self)
        self.zz_fdict['I2C1'] = self.I2C1
        self.IDAC0 = RM_Field_SMU_SPBGPATD0_IDAC0(self)
        self.zz_fdict['IDAC0'] = self.IDAC0
        self.MSC = RM_Field_SMU_SPBGPATD0_MSC(self)
        self.zz_fdict['MSC'] = self.MSC
        self.LDMA = RM_Field_SMU_SPBGPATD0_LDMA(self)
        self.zz_fdict['LDMA'] = self.LDMA
        self.LESENSE = RM_Field_SMU_SPBGPATD0_LESENSE(self)
        self.zz_fdict['LESENSE'] = self.LESENSE
        self.LETIMER0 = RM_Field_SMU_SPBGPATD0_LETIMER0(self)
        self.zz_fdict['LETIMER0'] = self.LETIMER0
        self.LEUART0 = RM_Field_SMU_SPBGPATD0_LEUART0(self)
        self.zz_fdict['LEUART0'] = self.LEUART0
        self.MODEM = RM_Field_SMU_SPBGPATD0_MODEM(self)
        self.zz_fdict['MODEM'] = self.MODEM
        self.PCNT0 = RM_Field_SMU_SPBGPATD0_PCNT0(self)
        self.zz_fdict['PCNT0'] = self.PCNT0
        self.PCNT1 = RM_Field_SMU_SPBGPATD0_PCNT1(self)
        self.zz_fdict['PCNT1'] = self.PCNT1
        self.PCNT2 = RM_Field_SMU_SPBGPATD0_PCNT2(self)
        self.zz_fdict['PCNT2'] = self.PCNT2
        self.PROTIMER = RM_Field_SMU_SPBGPATD0_PROTIMER(self)
        self.zz_fdict['PROTIMER'] = self.PROTIMER
        self.RAC = RM_Field_SMU_SPBGPATD0_RAC(self)
        self.zz_fdict['RAC'] = self.RAC
        self.__dict__['zz_frozen'] = True


class RM_Register_SMU_SPBGPATD1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SMU_SPBGPATD1, self).__init__(rmio, label,
            0x40022000, 0x054,
            'SPBGPATD1', 'SMU.SPBGPATD1', 'read-write',
            "",
            0x00000000, 0x0001FFFF)

        self.RFSENSE = RM_Field_SMU_SPBGPATD1_RFSENSE(self)
        self.zz_fdict['RFSENSE'] = self.RFSENSE
        self.RMU = RM_Field_SMU_SPBGPATD1_RMU(self)
        self.zz_fdict['RMU'] = self.RMU
        self.RTCC = RM_Field_SMU_SPBGPATD1_RTCC(self)
        self.zz_fdict['RTCC'] = self.RTCC
        self.SMU = RM_Field_SMU_SPBGPATD1_SMU(self)
        self.zz_fdict['SMU'] = self.SMU
        self.SYNTH = RM_Field_SMU_SPBGPATD1_SYNTH(self)
        self.zz_fdict['SYNTH'] = self.SYNTH
        self.TIMER0 = RM_Field_SMU_SPBGPATD1_TIMER0(self)
        self.zz_fdict['TIMER0'] = self.TIMER0
        self.TIMER1 = RM_Field_SMU_SPBGPATD1_TIMER1(self)
        self.zz_fdict['TIMER1'] = self.TIMER1
        self.TRNG0 = RM_Field_SMU_SPBGPATD1_TRNG0(self)
        self.zz_fdict['TRNG0'] = self.TRNG0
        self.USART0 = RM_Field_SMU_SPBGPATD1_USART0(self)
        self.zz_fdict['USART0'] = self.USART0
        self.USART1 = RM_Field_SMU_SPBGPATD1_USART1(self)
        self.zz_fdict['USART1'] = self.USART1
        self.USART2 = RM_Field_SMU_SPBGPATD1_USART2(self)
        self.zz_fdict['USART2'] = self.USART2
        self.USART3 = RM_Field_SMU_SPBGPATD1_USART3(self)
        self.zz_fdict['USART3'] = self.USART3
        self.WDOG0 = RM_Field_SMU_SPBGPATD1_WDOG0(self)
        self.zz_fdict['WDOG0'] = self.WDOG0
        self.WDOG1 = RM_Field_SMU_SPBGPATD1_WDOG1(self)
        self.zz_fdict['WDOG1'] = self.WDOG1
        self.WTIMER0 = RM_Field_SMU_SPBGPATD1_WTIMER0(self)
        self.zz_fdict['WTIMER0'] = self.WTIMER0
        self.WTIMER1 = RM_Field_SMU_SPBGPATD1_WTIMER1(self)
        self.zz_fdict['WTIMER1'] = self.WTIMER1
        self.SYSCFG = RM_Field_SMU_SPBGPATD1_SYSCFG(self)
        self.zz_fdict['SYSCFG'] = self.SYSCFG
        self.__dict__['zz_frozen'] = True


class RM_Register_SMU_SPBGFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SMU_SPBGFS, self).__init__(rmio, label,
            0x40022000, 0x090,
            'SPBGFS', 'SMU.SPBGFS', 'read-only',
            "",
            0x00000000, 0x0000007F)

        self.PERIPHID = RM_Field_SMU_SPBGFS_PERIPHID(self)
        self.zz_fdict['PERIPHID'] = self.PERIPHID
        self.__dict__['zz_frozen'] = True


