
from static import Base_RM_Register
from CSEN_field import *


class RM_Register_CSEN_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_CTRL, self).__init__(rmio, label,
            0x4001f000, 0x000,
            'CTRL', 'CSEN.CTRL', 'read-write',
            "",
            0x00030000, 0x3FFFF336)

        self.EN = RM_Field_CSEN_CTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.CMPPOL = RM_Field_CSEN_CTRL_CMPPOL(self)
        self.zz_fdict['CMPPOL'] = self.CMPPOL
        self.CM = RM_Field_CSEN_CTRL_CM(self)
        self.zz_fdict['CM'] = self.CM
        self.SARCR = RM_Field_CSEN_CTRL_SARCR(self)
        self.zz_fdict['SARCR'] = self.SARCR
        self.ACU = RM_Field_CSEN_CTRL_ACU(self)
        self.zz_fdict['ACU'] = self.ACU
        self.MCEN = RM_Field_CSEN_CTRL_MCEN(self)
        self.zz_fdict['MCEN'] = self.MCEN
        self.STM = RM_Field_CSEN_CTRL_STM(self)
        self.zz_fdict['STM'] = self.STM
        self.CMPEN = RM_Field_CSEN_CTRL_CMPEN(self)
        self.zz_fdict['CMPEN'] = self.CMPEN
        self.DRSF = RM_Field_CSEN_CTRL_DRSF(self)
        self.zz_fdict['DRSF'] = self.DRSF
        self.DMAEN = RM_Field_CSEN_CTRL_DMAEN(self)
        self.zz_fdict['DMAEN'] = self.DMAEN
        self.CONVSEL = RM_Field_CSEN_CTRL_CONVSEL(self)
        self.zz_fdict['CONVSEL'] = self.CONVSEL
        self.CHOPEN = RM_Field_CSEN_CTRL_CHOPEN(self)
        self.zz_fdict['CHOPEN'] = self.CHOPEN
        self.AUTOGND = RM_Field_CSEN_CTRL_AUTOGND(self)
        self.zz_fdict['AUTOGND'] = self.AUTOGND
        self.MXUC = RM_Field_CSEN_CTRL_MXUC(self)
        self.zz_fdict['MXUC'] = self.MXUC
        self.EMACMPEN = RM_Field_CSEN_CTRL_EMACMPEN(self)
        self.zz_fdict['EMACMPEN'] = self.EMACMPEN
        self.WARMUPMODE = RM_Field_CSEN_CTRL_WARMUPMODE(self)
        self.zz_fdict['WARMUPMODE'] = self.WARMUPMODE
        self.LOCALSENS = RM_Field_CSEN_CTRL_LOCALSENS(self)
        self.zz_fdict['LOCALSENS'] = self.LOCALSENS
        self.CPACCURACY = RM_Field_CSEN_CTRL_CPACCURACY(self)
        self.zz_fdict['CPACCURACY'] = self.CPACCURACY
        self.KEEPIBS = RM_Field_CSEN_CTRL_KEEPIBS(self)
        self.zz_fdict['KEEPIBS'] = self.KEEPIBS
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_TIMCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_TIMCTRL, self).__init__(rmio, label,
            0x4001f000, 0x004,
            'TIMCTRL', 'CSEN.TIMCTRL', 'read-write',
            "",
            0x00000000, 0x0003FF07)

        self.PCPRESC = RM_Field_CSEN_TIMCTRL_PCPRESC(self)
        self.zz_fdict['PCPRESC'] = self.PCPRESC
        self.PCTOP = RM_Field_CSEN_TIMCTRL_PCTOP(self)
        self.zz_fdict['PCTOP'] = self.PCTOP
        self.WARMUPCNT = RM_Field_CSEN_TIMCTRL_WARMUPCNT(self)
        self.zz_fdict['WARMUPCNT'] = self.WARMUPCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_CMD, self).__init__(rmio, label,
            0x4001f000, 0x008,
            'CMD', 'CSEN.CMD', 'write-only',
            "",
            0x00000000, 0x0000000D)

        self.START = RM_Field_CSEN_CMD_START(self)
        self.zz_fdict['START'] = self.START
        self.TAZINIT = RM_Field_CSEN_CMD_TAZINIT(self)
        self.zz_fdict['TAZINIT'] = self.TAZINIT
        self.IBISTSTART = RM_Field_CSEN_CMD_IBISTSTART(self)
        self.zz_fdict['IBISTSTART'] = self.IBISTSTART
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_STATUS, self).__init__(rmio, label,
            0x4001f000, 0x00C,
            'STATUS', 'CSEN.STATUS', 'read-only',
            "",
            0x00000000, 0xFFFF0007)

        self.CSENBUSY = RM_Field_CSEN_STATUS_CSENBUSY(self)
        self.zz_fdict['CSENBUSY'] = self.CSENBUSY
        self.DCXBUSY = RM_Field_CSEN_STATUS_DCXBUSY(self)
        self.zz_fdict['DCXBUSY'] = self.DCXBUSY
        self.TCONVBUSY = RM_Field_CSEN_STATUS_TCONVBUSY(self)
        self.zz_fdict['TCONVBUSY'] = self.TCONVBUSY
        self.TSTD = RM_Field_CSEN_STATUS_TSTD(self)
        self.zz_fdict['TSTD'] = self.TSTD
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_PRSSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_PRSSEL, self).__init__(rmio, label,
            0x4001f000, 0x010,
            'PRSSEL', 'CSEN.PRSSEL', 'read-write',
            "",
            0x00000000, 0x0000000F)

        self.PRSSEL = RM_Field_CSEN_PRSSEL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_DATA, self).__init__(rmio, label,
            0x4001f000, 0x014,
            'DATA', 'CSEN.DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_CSEN_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_SCANMASK0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_SCANMASK0, self).__init__(rmio, label,
            0x4001f000, 0x018,
            'SCANMASK0', 'CSEN.SCANMASK0', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.SCANINPUTEN = RM_Field_CSEN_SCANMASK0_SCANINPUTEN(self)
        self.zz_fdict['SCANINPUTEN'] = self.SCANINPUTEN
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_SCANINPUTSEL0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_SCANINPUTSEL0, self).__init__(rmio, label,
            0x4001f000, 0x01C,
            'SCANINPUTSEL0', 'CSEN.SCANINPUTSEL0', 'read-write',
            "",
            0x00000000, 0x0F0F0F0F)

        self.INPUT0TO7SEL = RM_Field_CSEN_SCANINPUTSEL0_INPUT0TO7SEL(self)
        self.zz_fdict['INPUT0TO7SEL'] = self.INPUT0TO7SEL
        self.INPUT8TO15SEL = RM_Field_CSEN_SCANINPUTSEL0_INPUT8TO15SEL(self)
        self.zz_fdict['INPUT8TO15SEL'] = self.INPUT8TO15SEL
        self.INPUT16TO23SEL = RM_Field_CSEN_SCANINPUTSEL0_INPUT16TO23SEL(self)
        self.zz_fdict['INPUT16TO23SEL'] = self.INPUT16TO23SEL
        self.INPUT24TO31SEL = RM_Field_CSEN_SCANINPUTSEL0_INPUT24TO31SEL(self)
        self.zz_fdict['INPUT24TO31SEL'] = self.INPUT24TO31SEL
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_SCANMASK1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_SCANMASK1, self).__init__(rmio, label,
            0x4001f000, 0x020,
            'SCANMASK1', 'CSEN.SCANMASK1', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.SCANINPUTEN = RM_Field_CSEN_SCANMASK1_SCANINPUTEN(self)
        self.zz_fdict['SCANINPUTEN'] = self.SCANINPUTEN
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_SCANINPUTSEL1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_SCANINPUTSEL1, self).__init__(rmio, label,
            0x4001f000, 0x024,
            'SCANINPUTSEL1', 'CSEN.SCANINPUTSEL1', 'read-write',
            "",
            0x00000000, 0x0F0F0F0F)

        self.INPUT32TO39SEL = RM_Field_CSEN_SCANINPUTSEL1_INPUT32TO39SEL(self)
        self.zz_fdict['INPUT32TO39SEL'] = self.INPUT32TO39SEL
        self.INPUT40TO47SEL = RM_Field_CSEN_SCANINPUTSEL1_INPUT40TO47SEL(self)
        self.zz_fdict['INPUT40TO47SEL'] = self.INPUT40TO47SEL
        self.INPUT48TO55SEL = RM_Field_CSEN_SCANINPUTSEL1_INPUT48TO55SEL(self)
        self.zz_fdict['INPUT48TO55SEL'] = self.INPUT48TO55SEL
        self.INPUT56TO63SEL = RM_Field_CSEN_SCANINPUTSEL1_INPUT56TO63SEL(self)
        self.zz_fdict['INPUT56TO63SEL'] = self.INPUT56TO63SEL
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_APORTREQ(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_APORTREQ, self).__init__(rmio, label,
            0x4001f000, 0x028,
            'APORTREQ', 'CSEN.APORTREQ', 'read-only',
            "",
            0x00000000, 0x000003FC)

        self.APORT1XREQ = RM_Field_CSEN_APORTREQ_APORT1XREQ(self)
        self.zz_fdict['APORT1XREQ'] = self.APORT1XREQ
        self.APORT1YREQ = RM_Field_CSEN_APORTREQ_APORT1YREQ(self)
        self.zz_fdict['APORT1YREQ'] = self.APORT1YREQ
        self.APORT2XREQ = RM_Field_CSEN_APORTREQ_APORT2XREQ(self)
        self.zz_fdict['APORT2XREQ'] = self.APORT2XREQ
        self.APORT2YREQ = RM_Field_CSEN_APORTREQ_APORT2YREQ(self)
        self.zz_fdict['APORT2YREQ'] = self.APORT2YREQ
        self.APORT3XREQ = RM_Field_CSEN_APORTREQ_APORT3XREQ(self)
        self.zz_fdict['APORT3XREQ'] = self.APORT3XREQ
        self.APORT3YREQ = RM_Field_CSEN_APORTREQ_APORT3YREQ(self)
        self.zz_fdict['APORT3YREQ'] = self.APORT3YREQ
        self.APORT4XREQ = RM_Field_CSEN_APORTREQ_APORT4XREQ(self)
        self.zz_fdict['APORT4XREQ'] = self.APORT4XREQ
        self.APORT4YREQ = RM_Field_CSEN_APORTREQ_APORT4YREQ(self)
        self.zz_fdict['APORT4YREQ'] = self.APORT4YREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_APORTCONFLICT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_APORTCONFLICT, self).__init__(rmio, label,
            0x4001f000, 0x02C,
            'APORTCONFLICT', 'CSEN.APORTCONFLICT', 'read-only',
            "",
            0x00000000, 0x000003FC)

        self.APORT1XCONFLICT = RM_Field_CSEN_APORTCONFLICT_APORT1XCONFLICT(self)
        self.zz_fdict['APORT1XCONFLICT'] = self.APORT1XCONFLICT
        self.APORT1YCONFLICT = RM_Field_CSEN_APORTCONFLICT_APORT1YCONFLICT(self)
        self.zz_fdict['APORT1YCONFLICT'] = self.APORT1YCONFLICT
        self.APORT2XCONFLICT = RM_Field_CSEN_APORTCONFLICT_APORT2XCONFLICT(self)
        self.zz_fdict['APORT2XCONFLICT'] = self.APORT2XCONFLICT
        self.APORT2YCONFLICT = RM_Field_CSEN_APORTCONFLICT_APORT2YCONFLICT(self)
        self.zz_fdict['APORT2YCONFLICT'] = self.APORT2YCONFLICT
        self.APORT3XCONFLICT = RM_Field_CSEN_APORTCONFLICT_APORT3XCONFLICT(self)
        self.zz_fdict['APORT3XCONFLICT'] = self.APORT3XCONFLICT
        self.APORT3YCONFLICT = RM_Field_CSEN_APORTCONFLICT_APORT3YCONFLICT(self)
        self.zz_fdict['APORT3YCONFLICT'] = self.APORT3YCONFLICT
        self.APORT4XCONFLICT = RM_Field_CSEN_APORTCONFLICT_APORT4XCONFLICT(self)
        self.zz_fdict['APORT4XCONFLICT'] = self.APORT4XCONFLICT
        self.APORT4YCONFLICT = RM_Field_CSEN_APORTCONFLICT_APORT4YCONFLICT(self)
        self.zz_fdict['APORT4YCONFLICT'] = self.APORT4YCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_CMPTHR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_CMPTHR, self).__init__(rmio, label,
            0x4001f000, 0x030,
            'CMPTHR', 'CSEN.CMPTHR', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.CMPTHR = RM_Field_CSEN_CMPTHR_CMPTHR(self)
        self.zz_fdict['CMPTHR'] = self.CMPTHR
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_EMA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_EMA, self).__init__(rmio, label,
            0x4001f000, 0x034,
            'EMA', 'CSEN.EMA', 'read-write',
            "",
            0x00000000, 0x003FFFFF)

        self.EMA = RM_Field_CSEN_EMA_EMA(self)
        self.zz_fdict['EMA'] = self.EMA
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_EMACTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_EMACTRL, self).__init__(rmio, label,
            0x4001f000, 0x038,
            'EMACTRL', 'CSEN.EMACTRL', 'read-write',
            "",
            0x00000000, 0x00000007)

        self.EMASAMPLE = RM_Field_CSEN_EMACTRL_EMASAMPLE(self)
        self.zz_fdict['EMASAMPLE'] = self.EMASAMPLE
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_SINGLECTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_SINGLECTRL, self).__init__(rmio, label,
            0x4001f000, 0x03C,
            'SINGLECTRL', 'CSEN.SINGLECTRL', 'read-write',
            "",
            0x00000000, 0x000007F0)

        self.SINGLESEL = RM_Field_CSEN_SINGLECTRL_SINGLESEL(self)
        self.zz_fdict['SINGLESEL'] = self.SINGLESEL
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_DMBASELINE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_DMBASELINE, self).__init__(rmio, label,
            0x4001f000, 0x040,
            'DMBASELINE', 'CSEN.DMBASELINE', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.BASELINEUP = RM_Field_CSEN_DMBASELINE_BASELINEUP(self)
        self.zz_fdict['BASELINEUP'] = self.BASELINEUP
        self.BASELINEDN = RM_Field_CSEN_DMBASELINE_BASELINEDN(self)
        self.zz_fdict['BASELINEDN'] = self.BASELINEDN
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_DMCFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_DMCFG, self).__init__(rmio, label,
            0x4001f000, 0x044,
            'DMCFG', 'CSEN.DMCFG', 'read-write',
            "",
            0x00000000, 0x103F0FFF)

        self.DMG = RM_Field_CSEN_DMCFG_DMG(self)
        self.zz_fdict['DMG'] = self.DMG
        self.DMR = RM_Field_CSEN_DMCFG_DMR(self)
        self.zz_fdict['DMR'] = self.DMR
        self.DMCR = RM_Field_CSEN_DMCFG_DMCR(self)
        self.zz_fdict['DMCR'] = self.DMCR
        self.CRMODE = RM_Field_CSEN_DMCFG_CRMODE(self)
        self.zz_fdict['CRMODE'] = self.CRMODE
        self.DMGRDIS = RM_Field_CSEN_DMCFG_DMGRDIS(self)
        self.zz_fdict['DMGRDIS'] = self.DMGRDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_ANACTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_ANACTRL, self).__init__(rmio, label,
            0x4001f000, 0x048,
            'ANACTRL', 'CSEN.ANACTRL', 'read-write',
            "",
            0x00000070, 0x03730771)

        self.CREFHALF = RM_Field_CSEN_ANACTRL_CREFHALF(self)
        self.zz_fdict['CREFHALF'] = self.CREFHALF
        self.IREFPROG = RM_Field_CSEN_ANACTRL_IREFPROG(self)
        self.zz_fdict['IREFPROG'] = self.IREFPROG
        self.IDACIREFS = RM_Field_CSEN_ANACTRL_IDACIREFS(self)
        self.zz_fdict['IDACIREFS'] = self.IDACIREFS
        self.DUTYSCALE = RM_Field_CSEN_ANACTRL_DUTYSCALE(self)
        self.zz_fdict['DUTYSCALE'] = self.DUTYSCALE
        self.TRSTPROG = RM_Field_CSEN_ANACTRL_TRSTPROG(self)
        self.zz_fdict['TRSTPROG'] = self.TRSTPROG
        self.BIASPROG = RM_Field_CSEN_ANACTRL_BIASPROG(self)
        self.zz_fdict['BIASPROG'] = self.BIASPROG
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_ANATRIM(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_ANATRIM, self).__init__(rmio, label,
            0x4001f000, 0x04C,
            'ANATRIM', 'CSEN.ANATRIM', 'read-write',
            "",
            0x00000004, 0x00000007)

        self.ILTCUATRIM = RM_Field_CSEN_ANATRIM_ILTCUATRIM(self)
        self.zz_fdict['ILTCUATRIM'] = self.ILTCUATRIM
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_TESTCFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_TESTCFG, self).__init__(rmio, label,
            0x4001f000, 0x050,
            'TESTCFG', 'CSEN.TESTCFG', 'read-write',
            "",
            0x00000115, 0xDFDB1F1F)

        self.BISTCLKL = RM_Field_CSEN_TESTCFG_BISTCLKL(self)
        self.zz_fdict['BISTCLKL'] = self.BISTCLKL
        self.BISTCLKH = RM_Field_CSEN_TESTCFG_BISTCLKH(self)
        self.zz_fdict['BISTCLKH'] = self.BISTCLKH
        self.IDACTST = RM_Field_CSEN_TESTCFG_IDACTST(self)
        self.zz_fdict['IDACTST'] = self.IDACTST
        self.BISTCLKSEL = RM_Field_CSEN_TESTCFG_BISTCLKSEL(self)
        self.zz_fdict['BISTCLKSEL'] = self.BISTCLKSEL
        self.ANATESTEN = RM_Field_CSEN_TESTCFG_ANATESTEN(self)
        self.zz_fdict['ANATESTEN'] = self.ANATESTEN
        self.CHOPPOLTEST = RM_Field_CSEN_TESTCFG_CHOPPOLTEST(self)
        self.zz_fdict['CHOPPOLTEST'] = self.CHOPPOLTEST
        self.CLKSEL = RM_Field_CSEN_TESTCFG_CLKSEL(self)
        self.zz_fdict['CLKSEL'] = self.CLKSEL
        self.CRSTCOMB = RM_Field_CSEN_TESTCFG_CRSTCOMB(self)
        self.zz_fdict['CRSTCOMB'] = self.CRSTCOMB
        self.ILMTOFF = RM_Field_CSEN_TESTCFG_ILMTOFF(self)
        self.zz_fdict['ILMTOFF'] = self.ILMTOFF
        self.VCASHI = RM_Field_CSEN_TESTCFG_VCASHI(self)
        self.zz_fdict['VCASHI'] = self.VCASHI
        self.VRSAMPEN = RM_Field_CSEN_TESTCFG_VRSAMPEN(self)
        self.zz_fdict['VRSAMPEN'] = self.VRSAMPEN
        self.STTLFAST = RM_Field_CSEN_TESTCFG_STTLFAST(self)
        self.zz_fdict['STTLFAST'] = self.STTLFAST
        self.SSCALON = RM_Field_CSEN_TESTCFG_SSCALON(self)
        self.zz_fdict['SSCALON'] = self.SSCALON
        self.VRAMP = RM_Field_CSEN_TESTCFG_VRAMP(self)
        self.zz_fdict['VRAMP'] = self.VRAMP
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_IF, self).__init__(rmio, label,
            0x4001f000, 0x054,
            'IF', 'CSEN.IF', 'read-only',
            "",
            0x00000000, 0x0000001F)

        self.CMP = RM_Field_CSEN_IF_CMP(self)
        self.zz_fdict['CMP'] = self.CMP
        self.CONV = RM_Field_CSEN_IF_CONV(self)
        self.zz_fdict['CONV'] = self.CONV
        self.EOS = RM_Field_CSEN_IF_EOS(self)
        self.zz_fdict['EOS'] = self.EOS
        self.DMAOF = RM_Field_CSEN_IF_DMAOF(self)
        self.zz_fdict['DMAOF'] = self.DMAOF
        self.APORTCONFLICT = RM_Field_CSEN_IF_APORTCONFLICT(self)
        self.zz_fdict['APORTCONFLICT'] = self.APORTCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_IFS, self).__init__(rmio, label,
            0x4001f000, 0x058,
            'IFS', 'CSEN.IFS', 'write-only',
            "",
            0x00000000, 0x0000001F)

        self.CMP = RM_Field_CSEN_IFS_CMP(self)
        self.zz_fdict['CMP'] = self.CMP
        self.CONV = RM_Field_CSEN_IFS_CONV(self)
        self.zz_fdict['CONV'] = self.CONV
        self.EOS = RM_Field_CSEN_IFS_EOS(self)
        self.zz_fdict['EOS'] = self.EOS
        self.DMAOF = RM_Field_CSEN_IFS_DMAOF(self)
        self.zz_fdict['DMAOF'] = self.DMAOF
        self.APORTCONFLICT = RM_Field_CSEN_IFS_APORTCONFLICT(self)
        self.zz_fdict['APORTCONFLICT'] = self.APORTCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_IFC, self).__init__(rmio, label,
            0x4001f000, 0x05C,
            'IFC', 'CSEN.IFC', 'write-only',
            "",
            0x00000000, 0x0000001F)

        self.CMP = RM_Field_CSEN_IFC_CMP(self)
        self.zz_fdict['CMP'] = self.CMP
        self.CONV = RM_Field_CSEN_IFC_CONV(self)
        self.zz_fdict['CONV'] = self.CONV
        self.EOS = RM_Field_CSEN_IFC_EOS(self)
        self.zz_fdict['EOS'] = self.EOS
        self.DMAOF = RM_Field_CSEN_IFC_DMAOF(self)
        self.zz_fdict['DMAOF'] = self.DMAOF
        self.APORTCONFLICT = RM_Field_CSEN_IFC_APORTCONFLICT(self)
        self.zz_fdict['APORTCONFLICT'] = self.APORTCONFLICT
        self.__dict__['zz_frozen'] = True


class RM_Register_CSEN_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CSEN_IEN, self).__init__(rmio, label,
            0x4001f000, 0x060,
            'IEN', 'CSEN.IEN', 'read-write',
            "",
            0x00000000, 0x0000001F)

        self.CMP = RM_Field_CSEN_IEN_CMP(self)
        self.zz_fdict['CMP'] = self.CMP
        self.CONV = RM_Field_CSEN_IEN_CONV(self)
        self.zz_fdict['CONV'] = self.CONV
        self.EOS = RM_Field_CSEN_IEN_EOS(self)
        self.zz_fdict['EOS'] = self.EOS
        self.DMAOF = RM_Field_CSEN_IEN_DMAOF(self)
        self.zz_fdict['DMAOF'] = self.DMAOF
        self.APORTCONFLICT = RM_Field_CSEN_IEN_APORTCONFLICT(self)
        self.zz_fdict['APORTCONFLICT'] = self.APORTCONFLICT
        self.__dict__['zz_frozen'] = True


