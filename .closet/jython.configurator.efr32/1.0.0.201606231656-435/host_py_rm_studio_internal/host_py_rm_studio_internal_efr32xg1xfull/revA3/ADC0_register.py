
from static import Base_RM_Register
from ADC0_field import *


class RM_Register_ADC0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_CTRL, self).__init__(rmio, label,
            0x40002000, 0x000,
            'CTRL', 'ADC0.CTRL', 'read-write',
            "",
            0x001F0000, 0xEF7F7FDF)

        self.WARMUPMODE = RM_Field_ADC0_CTRL_WARMUPMODE(self)
        self.zz_fdict['WARMUPMODE'] = self.WARMUPMODE
        self.SINGLEDMAWU = RM_Field_ADC0_CTRL_SINGLEDMAWU(self)
        self.zz_fdict['SINGLEDMAWU'] = self.SINGLEDMAWU
        self.SCANDMAWU = RM_Field_ADC0_CTRL_SCANDMAWU(self)
        self.zz_fdict['SCANDMAWU'] = self.SCANDMAWU
        self.TAILGATE = RM_Field_ADC0_CTRL_TAILGATE(self)
        self.zz_fdict['TAILGATE'] = self.TAILGATE
        self.ASYNCCLKEN = RM_Field_ADC0_CTRL_ASYNCCLKEN(self)
        self.zz_fdict['ASYNCCLKEN'] = self.ASYNCCLKEN
        self.ADCCLKMODE = RM_Field_ADC0_CTRL_ADCCLKMODE(self)
        self.zz_fdict['ADCCLKMODE'] = self.ADCCLKMODE
        self.PRESC = RM_Field_ADC0_CTRL_PRESC(self)
        self.zz_fdict['PRESC'] = self.PRESC
        self.TIMEBASE = RM_Field_ADC0_CTRL_TIMEBASE(self)
        self.zz_fdict['TIMEBASE'] = self.TIMEBASE
        self.OVSRSEL = RM_Field_ADC0_CTRL_OVSRSEL(self)
        self.zz_fdict['OVSRSEL'] = self.OVSRSEL
        self.CHCONMODE = RM_Field_ADC0_CTRL_CHCONMODE(self)
        self.zz_fdict['CHCONMODE'] = self.CHCONMODE
        self.CHCONIDLE = RM_Field_ADC0_CTRL_CHCONIDLE(self)
        self.zz_fdict['CHCONIDLE'] = self.CHCONIDLE
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_CMD, self).__init__(rmio, label,
            0x40002000, 0x008,
            'CMD', 'ADC0.CMD', 'write-only',
            "",
            0x00000000, 0x0000000F)

        self.SINGLESTART = RM_Field_ADC0_CMD_SINGLESTART(self)
        self.zz_fdict['SINGLESTART'] = self.SINGLESTART
        self.SINGLESTOP = RM_Field_ADC0_CMD_SINGLESTOP(self)
        self.zz_fdict['SINGLESTOP'] = self.SINGLESTOP
        self.SCANSTART = RM_Field_ADC0_CMD_SCANSTART(self)
        self.zz_fdict['SCANSTART'] = self.SCANSTART
        self.SCANSTOP = RM_Field_ADC0_CMD_SCANSTOP(self)
        self.zz_fdict['SCANSTOP'] = self.SCANSTOP
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_STATUS, self).__init__(rmio, label,
            0x40002000, 0x00C,
            'STATUS', 'ADC0.STATUS', 'read-only',
            "",
            0x00000000, 0x00031F03)

        self.SINGLEACT = RM_Field_ADC0_STATUS_SINGLEACT(self)
        self.zz_fdict['SINGLEACT'] = self.SINGLEACT
        self.SCANACT = RM_Field_ADC0_STATUS_SCANACT(self)
        self.zz_fdict['SCANACT'] = self.SCANACT
        self.SINGLEREFWARM = RM_Field_ADC0_STATUS_SINGLEREFWARM(self)
        self.zz_fdict['SINGLEREFWARM'] = self.SINGLEREFWARM
        self.SCANREFWARM = RM_Field_ADC0_STATUS_SCANREFWARM(self)
        self.zz_fdict['SCANREFWARM'] = self.SCANREFWARM
        self.PROGERR = RM_Field_ADC0_STATUS_PROGERR(self)
        self.zz_fdict['PROGERR'] = self.PROGERR
        self.WARM = RM_Field_ADC0_STATUS_WARM(self)
        self.zz_fdict['WARM'] = self.WARM
        self.SINGLEDV = RM_Field_ADC0_STATUS_SINGLEDV(self)
        self.zz_fdict['SINGLEDV'] = self.SINGLEDV
        self.SCANDV = RM_Field_ADC0_STATUS_SCANDV(self)
        self.zz_fdict['SCANDV'] = self.SCANDV
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SINGLECTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SINGLECTRL, self).__init__(rmio, label,
            0x40002000, 0x010,
            'SINGLECTRL', 'ADC0.SINGLECTRL', 'read-write',
            "",
            0x00FFFF00, 0xAFFFFFFF)

        self.REP = RM_Field_ADC0_SINGLECTRL_REP(self)
        self.zz_fdict['REP'] = self.REP
        self.DIFF = RM_Field_ADC0_SINGLECTRL_DIFF(self)
        self.zz_fdict['DIFF'] = self.DIFF
        self.ADJ = RM_Field_ADC0_SINGLECTRL_ADJ(self)
        self.zz_fdict['ADJ'] = self.ADJ
        self.RES = RM_Field_ADC0_SINGLECTRL_RES(self)
        self.zz_fdict['RES'] = self.RES
        self.REF = RM_Field_ADC0_SINGLECTRL_REF(self)
        self.zz_fdict['REF'] = self.REF
        self.POSSEL = RM_Field_ADC0_SINGLECTRL_POSSEL(self)
        self.zz_fdict['POSSEL'] = self.POSSEL
        self.NEGSEL = RM_Field_ADC0_SINGLECTRL_NEGSEL(self)
        self.zz_fdict['NEGSEL'] = self.NEGSEL
        self.AT = RM_Field_ADC0_SINGLECTRL_AT(self)
        self.zz_fdict['AT'] = self.AT
        self.PRSEN = RM_Field_ADC0_SINGLECTRL_PRSEN(self)
        self.zz_fdict['PRSEN'] = self.PRSEN
        self.CMPEN = RM_Field_ADC0_SINGLECTRL_CMPEN(self)
        self.zz_fdict['CMPEN'] = self.CMPEN
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SINGLECTRLX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SINGLECTRLX, self).__init__(rmio, label,
            0x40002000, 0x014,
            'SINGLECTRLX', 'ADC0.SINGLECTRLX', 'read-write',
            "",
            0x00000000, 0x0F1F7FFF)

        self.VREFSEL = RM_Field_ADC0_SINGLECTRLX_VREFSEL(self)
        self.zz_fdict['VREFSEL'] = self.VREFSEL
        self.VREFATTFIX = RM_Field_ADC0_SINGLECTRLX_VREFATTFIX(self)
        self.zz_fdict['VREFATTFIX'] = self.VREFATTFIX
        self.VREFATT = RM_Field_ADC0_SINGLECTRLX_VREFATT(self)
        self.zz_fdict['VREFATT'] = self.VREFATT
        self.VINATT = RM_Field_ADC0_SINGLECTRLX_VINATT(self)
        self.zz_fdict['VINATT'] = self.VINATT
        self.DVL = RM_Field_ADC0_SINGLECTRLX_DVL(self)
        self.zz_fdict['DVL'] = self.DVL
        self.FIFOOFACT = RM_Field_ADC0_SINGLECTRLX_FIFOOFACT(self)
        self.zz_fdict['FIFOOFACT'] = self.FIFOOFACT
        self.PRSMODE = RM_Field_ADC0_SINGLECTRLX_PRSMODE(self)
        self.zz_fdict['PRSMODE'] = self.PRSMODE
        self.PRSSEL = RM_Field_ADC0_SINGLECTRLX_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.CONVSTARTDELAY = RM_Field_ADC0_SINGLECTRLX_CONVSTARTDELAY(self)
        self.zz_fdict['CONVSTARTDELAY'] = self.CONVSTARTDELAY
        self.CONVSTARTDELAYEN = RM_Field_ADC0_SINGLECTRLX_CONVSTARTDELAYEN(self)
        self.zz_fdict['CONVSTARTDELAYEN'] = self.CONVSTARTDELAYEN
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SCANCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SCANCTRL, self).__init__(rmio, label,
            0x40002000, 0x018,
            'SCANCTRL', 'ADC0.SCANCTRL', 'read-write',
            "",
            0x00000000, 0xAF0000FF)

        self.REP = RM_Field_ADC0_SCANCTRL_REP(self)
        self.zz_fdict['REP'] = self.REP
        self.DIFF = RM_Field_ADC0_SCANCTRL_DIFF(self)
        self.zz_fdict['DIFF'] = self.DIFF
        self.ADJ = RM_Field_ADC0_SCANCTRL_ADJ(self)
        self.zz_fdict['ADJ'] = self.ADJ
        self.RES = RM_Field_ADC0_SCANCTRL_RES(self)
        self.zz_fdict['RES'] = self.RES
        self.REF = RM_Field_ADC0_SCANCTRL_REF(self)
        self.zz_fdict['REF'] = self.REF
        self.AT = RM_Field_ADC0_SCANCTRL_AT(self)
        self.zz_fdict['AT'] = self.AT
        self.PRSEN = RM_Field_ADC0_SCANCTRL_PRSEN(self)
        self.zz_fdict['PRSEN'] = self.PRSEN
        self.CMPEN = RM_Field_ADC0_SCANCTRL_CMPEN(self)
        self.zz_fdict['CMPEN'] = self.CMPEN
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SCANCTRLX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SCANCTRLX, self).__init__(rmio, label,
            0x40002000, 0x01C,
            'SCANCTRLX', 'ADC0.SCANCTRLX', 'read-write',
            "",
            0x00000000, 0x0F1F7FFF)

        self.VREFSEL = RM_Field_ADC0_SCANCTRLX_VREFSEL(self)
        self.zz_fdict['VREFSEL'] = self.VREFSEL
        self.VREFATTFIX = RM_Field_ADC0_SCANCTRLX_VREFATTFIX(self)
        self.zz_fdict['VREFATTFIX'] = self.VREFATTFIX
        self.VREFATT = RM_Field_ADC0_SCANCTRLX_VREFATT(self)
        self.zz_fdict['VREFATT'] = self.VREFATT
        self.VINATT = RM_Field_ADC0_SCANCTRLX_VINATT(self)
        self.zz_fdict['VINATT'] = self.VINATT
        self.DVL = RM_Field_ADC0_SCANCTRLX_DVL(self)
        self.zz_fdict['DVL'] = self.DVL
        self.FIFOOFACT = RM_Field_ADC0_SCANCTRLX_FIFOOFACT(self)
        self.zz_fdict['FIFOOFACT'] = self.FIFOOFACT
        self.PRSMODE = RM_Field_ADC0_SCANCTRLX_PRSMODE(self)
        self.zz_fdict['PRSMODE'] = self.PRSMODE
        self.PRSSEL = RM_Field_ADC0_SCANCTRLX_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.REPDELAY = RM_Field_ADC0_SCANCTRLX_REPDELAY(self)
        self.zz_fdict['REPDELAY'] = self.REPDELAY
        self.CONVSTARTDELAYEN = RM_Field_ADC0_SCANCTRLX_CONVSTARTDELAYEN(self)
        self.zz_fdict['CONVSTARTDELAYEN'] = self.CONVSTARTDELAYEN
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SCANMASK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SCANMASK, self).__init__(rmio, label,
            0x40002000, 0x020,
            'SCANMASK', 'ADC0.SCANMASK', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.SCANMASK = RM_Field_ADC0_SCANMASK_SCANMASK(self)
        self.zz_fdict['SCANMASK'] = self.SCANMASK
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SCANCHCONF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SCANCHCONF, self).__init__(rmio, label,
            0x40002000, 0x024,
            'SCANCHCONF', 'ADC0.SCANCHCONF', 'read-write',
            "",
            0x00000000, 0x1F1F1F1F)

        self.CH0TO7SEL = RM_Field_ADC0_SCANCHCONF_CH0TO7SEL(self)
        self.zz_fdict['CH0TO7SEL'] = self.CH0TO7SEL
        self.CH8TO15SEL = RM_Field_ADC0_SCANCHCONF_CH8TO15SEL(self)
        self.zz_fdict['CH8TO15SEL'] = self.CH8TO15SEL
        self.CH16TO23SEL = RM_Field_ADC0_SCANCHCONF_CH16TO23SEL(self)
        self.zz_fdict['CH16TO23SEL'] = self.CH16TO23SEL
        self.CH24TO31SEL = RM_Field_ADC0_SCANCHCONF_CH24TO31SEL(self)
        self.zz_fdict['CH24TO31SEL'] = self.CH24TO31SEL
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SCANNSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SCANNSEL, self).__init__(rmio, label,
            0x40002000, 0x028,
            'SCANNSEL', 'ADC0.SCANNSEL', 'read-write',
            "",
            0x000039E4, 0x0000FFFF)

        self.CH0NSEL = RM_Field_ADC0_SCANNSEL_CH0NSEL(self)
        self.zz_fdict['CH0NSEL'] = self.CH0NSEL
        self.CH2NSEL = RM_Field_ADC0_SCANNSEL_CH2NSEL(self)
        self.zz_fdict['CH2NSEL'] = self.CH2NSEL
        self.CH4NSEL = RM_Field_ADC0_SCANNSEL_CH4NSEL(self)
        self.zz_fdict['CH4NSEL'] = self.CH4NSEL
        self.CH6NSEL = RM_Field_ADC0_SCANNSEL_CH6NSEL(self)
        self.zz_fdict['CH6NSEL'] = self.CH6NSEL
        self.CH9NSEL = RM_Field_ADC0_SCANNSEL_CH9NSEL(self)
        self.zz_fdict['CH9NSEL'] = self.CH9NSEL
        self.CH11NSEL = RM_Field_ADC0_SCANNSEL_CH11NSEL(self)
        self.zz_fdict['CH11NSEL'] = self.CH11NSEL
        self.CH13NSEL = RM_Field_ADC0_SCANNSEL_CH13NSEL(self)
        self.zz_fdict['CH13NSEL'] = self.CH13NSEL
        self.CH15NSEL = RM_Field_ADC0_SCANNSEL_CH15NSEL(self)
        self.zz_fdict['CH15NSEL'] = self.CH15NSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_CMPTHR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_CMPTHR, self).__init__(rmio, label,
            0x40002000, 0x02C,
            'CMPTHR', 'ADC0.CMPTHR', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.ADLT = RM_Field_ADC0_CMPTHR_ADLT(self)
        self.zz_fdict['ADLT'] = self.ADLT
        self.ADGT = RM_Field_ADC0_CMPTHR_ADGT(self)
        self.zz_fdict['ADGT'] = self.ADGT
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_BIASPROG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_BIASPROG, self).__init__(rmio, label,
            0x40002000, 0x030,
            'BIASPROG', 'ADC0.BIASPROG', 'read-write',
            "",
            0x00000000, 0x0001113F)

        self.ADCBIASPROG = RM_Field_ADC0_BIASPROG_ADCBIASPROG(self)
        self.zz_fdict['ADCBIASPROG'] = self.ADCBIASPROG
        self.CONVSPEED = RM_Field_ADC0_BIASPROG_CONVSPEED(self)
        self.zz_fdict['CONVSPEED'] = self.CONVSPEED
        self.VREGSHUNT = RM_Field_ADC0_BIASPROG_VREGSHUNT(self)
        self.zz_fdict['VREGSHUNT'] = self.VREGSHUNT
        self.VFAULTCLR = RM_Field_ADC0_BIASPROG_VFAULTCLR(self)
        self.zz_fdict['VFAULTCLR'] = self.VFAULTCLR
        self.GPBIASACC = RM_Field_ADC0_BIASPROG_GPBIASACC(self)
        self.zz_fdict['GPBIASACC'] = self.GPBIASACC
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_CAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_CAL, self).__init__(rmio, label,
            0x40002000, 0x034,
            'CAL', 'ADC0.CAL', 'read-write',
            "",
            0x40784078, 0xFFFFFFFF)

        self.SINGLEOFFSET = RM_Field_ADC0_CAL_SINGLEOFFSET(self)
        self.zz_fdict['SINGLEOFFSET'] = self.SINGLEOFFSET
        self.SINGLEOFFSETINV = RM_Field_ADC0_CAL_SINGLEOFFSETINV(self)
        self.zz_fdict['SINGLEOFFSETINV'] = self.SINGLEOFFSETINV
        self.SINGLEGAIN = RM_Field_ADC0_CAL_SINGLEGAIN(self)
        self.zz_fdict['SINGLEGAIN'] = self.SINGLEGAIN
        self.OFFSETINVMODE = RM_Field_ADC0_CAL_OFFSETINVMODE(self)
        self.zz_fdict['OFFSETINVMODE'] = self.OFFSETINVMODE
        self.SCANOFFSET = RM_Field_ADC0_CAL_SCANOFFSET(self)
        self.zz_fdict['SCANOFFSET'] = self.SCANOFFSET
        self.SCANOFFSETINV = RM_Field_ADC0_CAL_SCANOFFSETINV(self)
        self.zz_fdict['SCANOFFSETINV'] = self.SCANOFFSETINV
        self.SCANGAIN = RM_Field_ADC0_CAL_SCANGAIN(self)
        self.zz_fdict['SCANGAIN'] = self.SCANGAIN
        self.CALEN = RM_Field_ADC0_CAL_CALEN(self)
        self.zz_fdict['CALEN'] = self.CALEN
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_IF, self).__init__(rmio, label,
            0x40002000, 0x038,
            'IF', 'ADC0.IF', 'read-only',
            "",
            0x00000000, 0x03030F03)

        self.SINGLE = RM_Field_ADC0_IF_SINGLE(self)
        self.zz_fdict['SINGLE'] = self.SINGLE
        self.SCAN = RM_Field_ADC0_IF_SCAN(self)
        self.zz_fdict['SCAN'] = self.SCAN
        self.SINGLEOF = RM_Field_ADC0_IF_SINGLEOF(self)
        self.zz_fdict['SINGLEOF'] = self.SINGLEOF
        self.SCANOF = RM_Field_ADC0_IF_SCANOF(self)
        self.zz_fdict['SCANOF'] = self.SCANOF
        self.SINGLEUF = RM_Field_ADC0_IF_SINGLEUF(self)
        self.zz_fdict['SINGLEUF'] = self.SINGLEUF
        self.SCANUF = RM_Field_ADC0_IF_SCANUF(self)
        self.zz_fdict['SCANUF'] = self.SCANUF
        self.SINGLECMP = RM_Field_ADC0_IF_SINGLECMP(self)
        self.zz_fdict['SINGLECMP'] = self.SINGLECMP
        self.SCANCMP = RM_Field_ADC0_IF_SCANCMP(self)
        self.zz_fdict['SCANCMP'] = self.SCANCMP
        self.VREFOV = RM_Field_ADC0_IF_VREFOV(self)
        self.zz_fdict['VREFOV'] = self.VREFOV
        self.PROGERR = RM_Field_ADC0_IF_PROGERR(self)
        self.zz_fdict['PROGERR'] = self.PROGERR
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_IFS, self).__init__(rmio, label,
            0x40002000, 0x03C,
            'IFS', 'ADC0.IFS', 'write-only',
            "",
            0x00000000, 0x03030F00)

        self.SINGLEOF = RM_Field_ADC0_IFS_SINGLEOF(self)
        self.zz_fdict['SINGLEOF'] = self.SINGLEOF
        self.SCANOF = RM_Field_ADC0_IFS_SCANOF(self)
        self.zz_fdict['SCANOF'] = self.SCANOF
        self.SINGLEUF = RM_Field_ADC0_IFS_SINGLEUF(self)
        self.zz_fdict['SINGLEUF'] = self.SINGLEUF
        self.SCANUF = RM_Field_ADC0_IFS_SCANUF(self)
        self.zz_fdict['SCANUF'] = self.SCANUF
        self.SINGLECMP = RM_Field_ADC0_IFS_SINGLECMP(self)
        self.zz_fdict['SINGLECMP'] = self.SINGLECMP
        self.SCANCMP = RM_Field_ADC0_IFS_SCANCMP(self)
        self.zz_fdict['SCANCMP'] = self.SCANCMP
        self.VREFOV = RM_Field_ADC0_IFS_VREFOV(self)
        self.zz_fdict['VREFOV'] = self.VREFOV
        self.PROGERR = RM_Field_ADC0_IFS_PROGERR(self)
        self.zz_fdict['PROGERR'] = self.PROGERR
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_IFC, self).__init__(rmio, label,
            0x40002000, 0x040,
            'IFC', 'ADC0.IFC', 'write-only',
            "",
            0x00000000, 0x03030F00)

        self.SINGLEOF = RM_Field_ADC0_IFC_SINGLEOF(self)
        self.zz_fdict['SINGLEOF'] = self.SINGLEOF
        self.SCANOF = RM_Field_ADC0_IFC_SCANOF(self)
        self.zz_fdict['SCANOF'] = self.SCANOF
        self.SINGLEUF = RM_Field_ADC0_IFC_SINGLEUF(self)
        self.zz_fdict['SINGLEUF'] = self.SINGLEUF
        self.SCANUF = RM_Field_ADC0_IFC_SCANUF(self)
        self.zz_fdict['SCANUF'] = self.SCANUF
        self.SINGLECMP = RM_Field_ADC0_IFC_SINGLECMP(self)
        self.zz_fdict['SINGLECMP'] = self.SINGLECMP
        self.SCANCMP = RM_Field_ADC0_IFC_SCANCMP(self)
        self.zz_fdict['SCANCMP'] = self.SCANCMP
        self.VREFOV = RM_Field_ADC0_IFC_VREFOV(self)
        self.zz_fdict['VREFOV'] = self.VREFOV
        self.PROGERR = RM_Field_ADC0_IFC_PROGERR(self)
        self.zz_fdict['PROGERR'] = self.PROGERR
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_IEN, self).__init__(rmio, label,
            0x40002000, 0x044,
            'IEN', 'ADC0.IEN', 'read-write',
            "",
            0x00000000, 0x03030F03)

        self.SINGLE = RM_Field_ADC0_IEN_SINGLE(self)
        self.zz_fdict['SINGLE'] = self.SINGLE
        self.SCAN = RM_Field_ADC0_IEN_SCAN(self)
        self.zz_fdict['SCAN'] = self.SCAN
        self.SINGLEOF = RM_Field_ADC0_IEN_SINGLEOF(self)
        self.zz_fdict['SINGLEOF'] = self.SINGLEOF
        self.SCANOF = RM_Field_ADC0_IEN_SCANOF(self)
        self.zz_fdict['SCANOF'] = self.SCANOF
        self.SINGLEUF = RM_Field_ADC0_IEN_SINGLEUF(self)
        self.zz_fdict['SINGLEUF'] = self.SINGLEUF
        self.SCANUF = RM_Field_ADC0_IEN_SCANUF(self)
        self.zz_fdict['SCANUF'] = self.SCANUF
        self.SINGLECMP = RM_Field_ADC0_IEN_SINGLECMP(self)
        self.zz_fdict['SINGLECMP'] = self.SINGLECMP
        self.SCANCMP = RM_Field_ADC0_IEN_SCANCMP(self)
        self.zz_fdict['SCANCMP'] = self.SCANCMP
        self.VREFOV = RM_Field_ADC0_IEN_VREFOV(self)
        self.zz_fdict['VREFOV'] = self.VREFOV
        self.PROGERR = RM_Field_ADC0_IEN_PROGERR(self)
        self.zz_fdict['PROGERR'] = self.PROGERR
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SINGLEDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SINGLEDATA, self).__init__(rmio, label,
            0x40002000, 0x048,
            'SINGLEDATA', 'ADC0.SINGLEDATA', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_ADC0_SINGLEDATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SCANDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SCANDATA, self).__init__(rmio, label,
            0x40002000, 0x04C,
            'SCANDATA', 'ADC0.SCANDATA', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_ADC0_SCANDATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SINGLEDATAP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SINGLEDATAP, self).__init__(rmio, label,
            0x40002000, 0x050,
            'SINGLEDATAP', 'ADC0.SINGLEDATAP', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATAP = RM_Field_ADC0_SINGLEDATAP_DATAP(self)
        self.zz_fdict['DATAP'] = self.DATAP
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SCANDATAP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SCANDATAP, self).__init__(rmio, label,
            0x40002000, 0x054,
            'SCANDATAP', 'ADC0.SCANDATAP', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATAP = RM_Field_ADC0_SCANDATAP_DATAP(self)
        self.zz_fdict['DATAP'] = self.DATAP
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SCANDATAX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SCANDATAX, self).__init__(rmio, label,
            0x40002000, 0x068,
            'SCANDATAX', 'ADC0.SCANDATAX', 'read-only',
            "",
            0x00000000, 0x001FFFFF)

        self.DATA = RM_Field_ADC0_SCANDATAX_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.SCANDATASRC = RM_Field_ADC0_SCANDATAX_SCANDATASRC(self)
        self.zz_fdict['SCANDATASRC'] = self.SCANDATASRC
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SCANDATAXP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SCANDATAXP, self).__init__(rmio, label,
            0x40002000, 0x06C,
            'SCANDATAXP', 'ADC0.SCANDATAXP', 'read-only',
            "",
            0x00000000, 0x001FFFFF)

        self.DATAP = RM_Field_ADC0_SCANDATAXP_DATAP(self)
        self.zz_fdict['DATAP'] = self.DATAP
        self.SCANDATASRCPEEK = RM_Field_ADC0_SCANDATAXP_SCANDATASRCPEEK(self)
        self.zz_fdict['SCANDATASRCPEEK'] = self.SCANDATASRCPEEK
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_TEST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_TEST, self).__init__(rmio, label,
            0x40002000, 0x078,
            'TEST', 'ADC0.TEST', 'read-write',
            "",
            0x00000001, 0x03371F07)

        self.VRPROTEN = RM_Field_ADC0_TEST_VRPROTEN(self)
        self.zz_fdict['VRPROTEN'] = self.VRPROTEN
        self.REFSAMPEN = RM_Field_ADC0_TEST_REFSAMPEN(self)
        self.zz_fdict['REFSAMPEN'] = self.REFSAMPEN
        self.THERMOFF = RM_Field_ADC0_TEST_THERMOFF(self)
        self.zz_fdict['THERMOFF'] = self.THERMOFF
        self.SAMPSYNC = RM_Field_ADC0_TEST_SAMPSYNC(self)
        self.zz_fdict['SAMPSYNC'] = self.SAMPSYNC
        self.AZDISABLE = RM_Field_ADC0_TEST_AZDISABLE(self)
        self.zz_fdict['AZDISABLE'] = self.AZDISABLE
        self.TEMPSENSEN = RM_Field_ADC0_TEST_TEMPSENSEN(self)
        self.zz_fdict['TEMPSENSEN'] = self.TEMPSENSEN
        self.LDOPDDIS = RM_Field_ADC0_TEST_LDOPDDIS(self)
        self.zz_fdict['LDOPDDIS'] = self.LDOPDDIS
        self.GAINONVEXT = RM_Field_ADC0_TEST_GAINONVEXT(self)
        self.zz_fdict['GAINONVEXT'] = self.GAINONVEXT
        self.VREGSTEP = RM_Field_ADC0_TEST_VREGSTEP(self)
        self.zz_fdict['VREGSTEP'] = self.VREGSTEP
        self.VREGRAIL = RM_Field_ADC0_TEST_VREGRAIL(self)
        self.zz_fdict['VREGRAIL'] = self.VREGRAIL
        self.VCMSTEP = RM_Field_ADC0_TEST_VCMSTEP(self)
        self.zz_fdict['VCMSTEP'] = self.VCMSTEP
        self.ILTCEN = RM_Field_ADC0_TEST_ILTCEN(self)
        self.zz_fdict['ILTCEN'] = self.ILTCEN
        self.IVGRSEL = RM_Field_ADC0_TEST_IVGRSEL(self)
        self.zz_fdict['IVGRSEL'] = self.IVGRSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_BUSREQ(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_BUSREQ, self).__init__(rmio, label,
            0x40002000, 0x07C,
            'BUSREQ', 'ADC0.BUSREQ', 'read-only',
            "",
            0x00000000, 0x000003FF)

        self.BUS0XREQ = RM_Field_ADC0_BUSREQ_BUS0XREQ(self)
        self.zz_fdict['BUS0XREQ'] = self.BUS0XREQ
        self.BUS0YREQ = RM_Field_ADC0_BUSREQ_BUS0YREQ(self)
        self.zz_fdict['BUS0YREQ'] = self.BUS0YREQ
        self.BUS1XREQ = RM_Field_ADC0_BUSREQ_BUS1XREQ(self)
        self.zz_fdict['BUS1XREQ'] = self.BUS1XREQ
        self.BUS1YREQ = RM_Field_ADC0_BUSREQ_BUS1YREQ(self)
        self.zz_fdict['BUS1YREQ'] = self.BUS1YREQ
        self.BUS2XREQ = RM_Field_ADC0_BUSREQ_BUS2XREQ(self)
        self.zz_fdict['BUS2XREQ'] = self.BUS2XREQ
        self.BUS2YREQ = RM_Field_ADC0_BUSREQ_BUS2YREQ(self)
        self.zz_fdict['BUS2YREQ'] = self.BUS2YREQ
        self.BUS3XREQ = RM_Field_ADC0_BUSREQ_BUS3XREQ(self)
        self.zz_fdict['BUS3XREQ'] = self.BUS3XREQ
        self.BUS3YREQ = RM_Field_ADC0_BUSREQ_BUS3YREQ(self)
        self.zz_fdict['BUS3YREQ'] = self.BUS3YREQ
        self.BUS4XREQ = RM_Field_ADC0_BUSREQ_BUS4XREQ(self)
        self.zz_fdict['BUS4XREQ'] = self.BUS4XREQ
        self.BUS4YREQ = RM_Field_ADC0_BUSREQ_BUS4YREQ(self)
        self.zz_fdict['BUS4YREQ'] = self.BUS4YREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_BUSCONFLICT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_BUSCONFLICT, self).__init__(rmio, label,
            0x40002000, 0x080,
            'BUSCONFLICT', 'ADC0.BUSCONFLICT', 'read-only',
            "",
            0x00000000, 0x000003FF)

        self.BUS0XCONFLICT = RM_Field_ADC0_BUSCONFLICT_BUS0XCONFLICT(self)
        self.zz_fdict['BUS0XCONFLICT'] = self.BUS0XCONFLICT
        self.BUS0YCONFLICT = RM_Field_ADC0_BUSCONFLICT_BUS0YCONFLICT(self)
        self.zz_fdict['BUS0YCONFLICT'] = self.BUS0YCONFLICT
        self.BUS1XCONFLICT = RM_Field_ADC0_BUSCONFLICT_BUS1XCONFLICT(self)
        self.zz_fdict['BUS1XCONFLICT'] = self.BUS1XCONFLICT
        self.BUS1YCONFLICT = RM_Field_ADC0_BUSCONFLICT_BUS1YCONFLICT(self)
        self.zz_fdict['BUS1YCONFLICT'] = self.BUS1YCONFLICT
        self.BUS2XCONFLICT = RM_Field_ADC0_BUSCONFLICT_BUS2XCONFLICT(self)
        self.zz_fdict['BUS2XCONFLICT'] = self.BUS2XCONFLICT
        self.BUS2YCONFLICT = RM_Field_ADC0_BUSCONFLICT_BUS2YCONFLICT(self)
        self.zz_fdict['BUS2YCONFLICT'] = self.BUS2YCONFLICT
        self.BUS3XCONFLICT = RM_Field_ADC0_BUSCONFLICT_BUS3XCONFLICT(self)
        self.zz_fdict['BUS3XCONFLICT'] = self.BUS3XCONFLICT
        self.BUS3YCONFLICT = RM_Field_ADC0_BUSCONFLICT_BUS3YCONFLICT(self)
        self.zz_fdict['BUS3YCONFLICT'] = self.BUS3YCONFLICT
        self.BUS4XCONFLICT = RM_Field_ADC0_BUSCONFLICT_BUS4XCONFLICT(self)
        self.zz_fdict['BUS4XCONFLICT'] = self.BUS4XCONFLICT
        self.BUS4YCONFLICT = RM_Field_ADC0_BUSCONFLICT_BUS4YCONFLICT(self)
        self.zz_fdict['BUS4YCONFLICT'] = self.BUS4YCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SINGLEFIFOCOUNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SINGLEFIFOCOUNT, self).__init__(rmio, label,
            0x40002000, 0x084,
            'SINGLEFIFOCOUNT', 'ADC0.SINGLEFIFOCOUNT', 'read-only',
            "",
            0x00000000, 0x00000007)

        self.SINGLEDC = RM_Field_ADC0_SINGLEFIFOCOUNT_SINGLEDC(self)
        self.zz_fdict['SINGLEDC'] = self.SINGLEDC
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SCANFIFOCOUNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SCANFIFOCOUNT, self).__init__(rmio, label,
            0x40002000, 0x088,
            'SCANFIFOCOUNT', 'ADC0.SCANFIFOCOUNT', 'read-only',
            "",
            0x00000000, 0x00000007)

        self.SCANDC = RM_Field_ADC0_SCANFIFOCOUNT_SCANDC(self)
        self.zz_fdict['SCANDC'] = self.SCANDC
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SINGLEFIFOCLEAR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SINGLEFIFOCLEAR, self).__init__(rmio, label,
            0x40002000, 0x08C,
            'SINGLEFIFOCLEAR', 'ADC0.SINGLEFIFOCLEAR', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.SINGLEFIFOCLEAR = RM_Field_ADC0_SINGLEFIFOCLEAR_SINGLEFIFOCLEAR(self)
        self.zz_fdict['SINGLEFIFOCLEAR'] = self.SINGLEFIFOCLEAR
        self.__dict__['zz_frozen'] = True


class RM_Register_ADC0_SCANFIFOCLEAR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ADC0_SCANFIFOCLEAR, self).__init__(rmio, label,
            0x40002000, 0x090,
            'SCANFIFOCLEAR', 'ADC0.SCANFIFOCLEAR', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.SCANFIFOCLEAR = RM_Field_ADC0_SCANFIFOCLEAR_SCANFIFOCLEAR(self)
        self.zz_fdict['SCANFIFOCLEAR'] = self.SCANFIFOCLEAR
        self.__dict__['zz_frozen'] = True


