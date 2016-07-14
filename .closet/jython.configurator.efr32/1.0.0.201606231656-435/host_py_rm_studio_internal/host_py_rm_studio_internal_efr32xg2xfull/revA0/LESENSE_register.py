
from static import Base_RM_Register
from LESENSE_field_1 import *
from LESENSE_field_2 import *


class RM_Register_LESENSE_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CTRL, self).__init__(rmio, label,
            0x40055000, 0x000,
            'CTRL', 'LESENSE.CTRL', 'read-write',
            "",
            0x00000000, 0x007B29BF)

        self.SCANMODE = RM_Field_LESENSE_CTRL_SCANMODE(self)
        self.zz_fdict['SCANMODE'] = self.SCANMODE
        self.PRSSEL = RM_Field_LESENSE_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.SCANCONF = RM_Field_LESENSE_CTRL_SCANCONF(self)
        self.zz_fdict['SCANCONF'] = self.SCANCONF
        self.ALTEXMAP = RM_Field_LESENSE_CTRL_ALTEXMAP(self)
        self.zz_fdict['ALTEXMAP'] = self.ALTEXMAP
        self.DUALSAMPLE = RM_Field_LESENSE_CTRL_DUALSAMPLE(self)
        self.zz_fdict['DUALSAMPLE'] = self.DUALSAMPLE
        self.BUFOW = RM_Field_LESENSE_CTRL_BUFOW(self)
        self.zz_fdict['BUFOW'] = self.BUFOW
        self.STRSCANRES = RM_Field_LESENSE_CTRL_STRSCANRES(self)
        self.zz_fdict['STRSCANRES'] = self.STRSCANRES
        self.BUFIDL = RM_Field_LESENSE_CTRL_BUFIDL(self)
        self.zz_fdict['BUFIDL'] = self.BUFIDL
        self.DMAWU = RM_Field_LESENSE_CTRL_DMAWU(self)
        self.zz_fdict['DMAWU'] = self.DMAWU
        self.DEBUGRUN = RM_Field_LESENSE_CTRL_DEBUGRUN(self)
        self.zz_fdict['DEBUGRUN'] = self.DEBUGRUN
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_TIMCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_TIMCTRL, self).__init__(rmio, label,
            0x40055000, 0x004,
            'TIMCTRL', 'LESENSE.TIMCTRL', 'read-write',
            "",
            0x00000000, 0x10CFF773)

        self.AUXPRESC = RM_Field_LESENSE_TIMCTRL_AUXPRESC(self)
        self.zz_fdict['AUXPRESC'] = self.AUXPRESC
        self.LFPRESC = RM_Field_LESENSE_TIMCTRL_LFPRESC(self)
        self.zz_fdict['LFPRESC'] = self.LFPRESC
        self.PCPRESC = RM_Field_LESENSE_TIMCTRL_PCPRESC(self)
        self.zz_fdict['PCPRESC'] = self.PCPRESC
        self.PCTOP = RM_Field_LESENSE_TIMCTRL_PCTOP(self)
        self.zz_fdict['PCTOP'] = self.PCTOP
        self.STARTDLY = RM_Field_LESENSE_TIMCTRL_STARTDLY(self)
        self.zz_fdict['STARTDLY'] = self.STARTDLY
        self.AUXSTARTUP = RM_Field_LESENSE_TIMCTRL_AUXSTARTUP(self)
        self.zz_fdict['AUXSTARTUP'] = self.AUXSTARTUP
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_PERCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_PERCTRL, self).__init__(rmio, label,
            0x40055000, 0x008,
            'PERCTRL', 'LESENSE.PERCTRL', 'read-write',
            "",
            0x00000000, 0x3FF0014F)

        self.DACCH0EN = RM_Field_LESENSE_PERCTRL_DACCH0EN(self)
        self.zz_fdict['DACCH0EN'] = self.DACCH0EN
        self.DACCH1EN = RM_Field_LESENSE_PERCTRL_DACCH1EN(self)
        self.zz_fdict['DACCH1EN'] = self.DACCH1EN
        self.DACCH0DATA = RM_Field_LESENSE_PERCTRL_DACCH0DATA(self)
        self.zz_fdict['DACCH0DATA'] = self.DACCH0DATA
        self.DACCH1DATA = RM_Field_LESENSE_PERCTRL_DACCH1DATA(self)
        self.zz_fdict['DACCH1DATA'] = self.DACCH1DATA
        self.DACSTARTUP = RM_Field_LESENSE_PERCTRL_DACSTARTUP(self)
        self.zz_fdict['DACSTARTUP'] = self.DACSTARTUP
        self.DACCONVTRIG = RM_Field_LESENSE_PERCTRL_DACCONVTRIG(self)
        self.zz_fdict['DACCONVTRIG'] = self.DACCONVTRIG
        self.ACMP0MODE = RM_Field_LESENSE_PERCTRL_ACMP0MODE(self)
        self.zz_fdict['ACMP0MODE'] = self.ACMP0MODE
        self.ACMP1MODE = RM_Field_LESENSE_PERCTRL_ACMP1MODE(self)
        self.zz_fdict['ACMP1MODE'] = self.ACMP1MODE
        self.ACMP0INV = RM_Field_LESENSE_PERCTRL_ACMP0INV(self)
        self.zz_fdict['ACMP0INV'] = self.ACMP0INV
        self.ACMP1INV = RM_Field_LESENSE_PERCTRL_ACMP1INV(self)
        self.zz_fdict['ACMP1INV'] = self.ACMP1INV
        self.ACMP0HYSTEN = RM_Field_LESENSE_PERCTRL_ACMP0HYSTEN(self)
        self.zz_fdict['ACMP0HYSTEN'] = self.ACMP0HYSTEN
        self.ACMP1HYSTEN = RM_Field_LESENSE_PERCTRL_ACMP1HYSTEN(self)
        self.zz_fdict['ACMP1HYSTEN'] = self.ACMP1HYSTEN
        self.WARMUPMODE = RM_Field_LESENSE_PERCTRL_WARMUPMODE(self)
        self.zz_fdict['WARMUPMODE'] = self.WARMUPMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_DECCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_DECCTRL, self).__init__(rmio, label,
            0x40055000, 0x00C,
            'DECCTRL', 'LESENSE.DECCTRL', 'read-write',
            "",
            0x00000000, 0x1EF7BDFF)

        self.DISABLE = RM_Field_LESENSE_DECCTRL_DISABLE(self)
        self.zz_fdict['DISABLE'] = self.DISABLE
        self.ERRCHK = RM_Field_LESENSE_DECCTRL_ERRCHK(self)
        self.zz_fdict['ERRCHK'] = self.ERRCHK
        self.INTMAP = RM_Field_LESENSE_DECCTRL_INTMAP(self)
        self.zz_fdict['INTMAP'] = self.INTMAP
        self.HYSTPRS0 = RM_Field_LESENSE_DECCTRL_HYSTPRS0(self)
        self.zz_fdict['HYSTPRS0'] = self.HYSTPRS0
        self.HYSTPRS1 = RM_Field_LESENSE_DECCTRL_HYSTPRS1(self)
        self.zz_fdict['HYSTPRS1'] = self.HYSTPRS1
        self.HYSTPRS2 = RM_Field_LESENSE_DECCTRL_HYSTPRS2(self)
        self.zz_fdict['HYSTPRS2'] = self.HYSTPRS2
        self.HYSTIRQ = RM_Field_LESENSE_DECCTRL_HYSTIRQ(self)
        self.zz_fdict['HYSTIRQ'] = self.HYSTIRQ
        self.PRSCNT = RM_Field_LESENSE_DECCTRL_PRSCNT(self)
        self.zz_fdict['PRSCNT'] = self.PRSCNT
        self.INPUT = RM_Field_LESENSE_DECCTRL_INPUT(self)
        self.zz_fdict['INPUT'] = self.INPUT
        self.PRSSEL0 = RM_Field_LESENSE_DECCTRL_PRSSEL0(self)
        self.zz_fdict['PRSSEL0'] = self.PRSSEL0
        self.PRSSEL1 = RM_Field_LESENSE_DECCTRL_PRSSEL1(self)
        self.zz_fdict['PRSSEL1'] = self.PRSSEL1
        self.PRSSEL2 = RM_Field_LESENSE_DECCTRL_PRSSEL2(self)
        self.zz_fdict['PRSSEL2'] = self.PRSSEL2
        self.PRSSEL3 = RM_Field_LESENSE_DECCTRL_PRSSEL3(self)
        self.zz_fdict['PRSSEL3'] = self.PRSSEL3
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BIASCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BIASCTRL, self).__init__(rmio, label,
            0x40055000, 0x010,
            'BIASCTRL', 'LESENSE.BIASCTRL', 'read-write',
            "",
            0x00000000, 0x00000103)

        self.BIASMODE = RM_Field_LESENSE_BIASCTRL_BIASMODE(self)
        self.zz_fdict['BIASMODE'] = self.BIASMODE
        self.BGRHIGHACCEN = RM_Field_LESENSE_BIASCTRL_BGRHIGHACCEN(self)
        self.zz_fdict['BGRHIGHACCEN'] = self.BGRHIGHACCEN
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_EVALCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_EVALCTRL, self).__init__(rmio, label,
            0x40055000, 0x014,
            'EVALCTRL', 'LESENSE.EVALCTRL', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.WINSIZE = RM_Field_LESENSE_EVALCTRL_WINSIZE(self)
        self.zz_fdict['WINSIZE'] = self.WINSIZE
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_PRSCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_PRSCTRL, self).__init__(rmio, label,
            0x40055000, 0x018,
            'PRSCTRL', 'LESENSE.PRSCTRL', 'read-write',
            "",
            0x00000000, 0x00011F1F)

        self.DECCMPVAL = RM_Field_LESENSE_PRSCTRL_DECCMPVAL(self)
        self.zz_fdict['DECCMPVAL'] = self.DECCMPVAL
        self.DECCMPMASK = RM_Field_LESENSE_PRSCTRL_DECCMPMASK(self)
        self.zz_fdict['DECCMPMASK'] = self.DECCMPMASK
        self.DECCMPEN = RM_Field_LESENSE_PRSCTRL_DECCMPEN(self)
        self.zz_fdict['DECCMPEN'] = self.DECCMPEN
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CMD, self).__init__(rmio, label,
            0x40055000, 0x01C,
            'CMD', 'LESENSE.CMD', 'write-only',
            "",
            0x00000000, 0x0000000F)

        self.START = RM_Field_LESENSE_CMD_START(self)
        self.zz_fdict['START'] = self.START
        self.STOP = RM_Field_LESENSE_CMD_STOP(self)
        self.zz_fdict['STOP'] = self.STOP
        self.DECODE = RM_Field_LESENSE_CMD_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.CLEARBUF = RM_Field_LESENSE_CMD_CLEARBUF(self)
        self.zz_fdict['CLEARBUF'] = self.CLEARBUF
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CHEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CHEN, self).__init__(rmio, label,
            0x40055000, 0x020,
            'CHEN', 'LESENSE.CHEN', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.CHEN = RM_Field_LESENSE_CHEN_CHEN(self)
        self.zz_fdict['CHEN'] = self.CHEN
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_SCANRES(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_SCANRES, self).__init__(rmio, label,
            0x40055000, 0x024,
            'SCANRES', 'LESENSE.SCANRES', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.SCANRES = RM_Field_LESENSE_SCANRES_SCANRES(self)
        self.zz_fdict['SCANRES'] = self.SCANRES
        self.STEPDIR = RM_Field_LESENSE_SCANRES_STEPDIR(self)
        self.zz_fdict['STEPDIR'] = self.STEPDIR
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_STATUS, self).__init__(rmio, label,
            0x40055000, 0x028,
            'STATUS', 'LESENSE.STATUS', 'read-only',
            "",
            0x00000000, 0x0000003F)

        self.BUFDATAV = RM_Field_LESENSE_STATUS_BUFDATAV(self)
        self.zz_fdict['BUFDATAV'] = self.BUFDATAV
        self.BUFHALFFULL = RM_Field_LESENSE_STATUS_BUFHALFFULL(self)
        self.zz_fdict['BUFHALFFULL'] = self.BUFHALFFULL
        self.BUFFULL = RM_Field_LESENSE_STATUS_BUFFULL(self)
        self.zz_fdict['BUFFULL'] = self.BUFFULL
        self.RUNNING = RM_Field_LESENSE_STATUS_RUNNING(self)
        self.zz_fdict['RUNNING'] = self.RUNNING
        self.SCANACTIVE = RM_Field_LESENSE_STATUS_SCANACTIVE(self)
        self.zz_fdict['SCANACTIVE'] = self.SCANACTIVE
        self.DACACTIVE = RM_Field_LESENSE_STATUS_DACACTIVE(self)
        self.zz_fdict['DACACTIVE'] = self.DACACTIVE
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_PTR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_PTR, self).__init__(rmio, label,
            0x40055000, 0x02C,
            'PTR', 'LESENSE.PTR', 'read-only',
            "",
            0x00000000, 0x000000FF)

        self.RD = RM_Field_LESENSE_PTR_RD(self)
        self.zz_fdict['RD'] = self.RD
        self.WR = RM_Field_LESENSE_PTR_WR(self)
        self.zz_fdict['WR'] = self.WR
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUFDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUFDATA, self).__init__(rmio, label,
            0x40055000, 0x030,
            'BUFDATA', 'LESENSE.BUFDATA', 'read-only',
            "",
            0x00000000, 0x00FFFFFF)

        self.BUFDATA = RM_Field_LESENSE_BUFDATA_BUFDATA(self)
        self.zz_fdict['BUFDATA'] = self.BUFDATA
        self.BUFDATASRC = RM_Field_LESENSE_BUFDATA_BUFDATASRC(self)
        self.zz_fdict['BUFDATASRC'] = self.BUFDATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUFDATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CURCH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CURCH, self).__init__(rmio, label,
            0x40055000, 0x034,
            'CURCH', 'LESENSE.CURCH', 'read-only',
            "",
            0x00000000, 0x0000000F)

        self.CURCH = RM_Field_LESENSE_CURCH_CURCH(self)
        self.zz_fdict['CURCH'] = self.CURCH
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_DECSTATE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_DECSTATE, self).__init__(rmio, label,
            0x40055000, 0x038,
            'DECSTATE', 'LESENSE.DECSTATE', 'read-write',
            "",
            0x00000000, 0x0000001F)

        self.DECSTATE = RM_Field_LESENSE_DECSTATE_DECSTATE(self)
        self.zz_fdict['DECSTATE'] = self.DECSTATE
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_SENSORSTATE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_SENSORSTATE, self).__init__(rmio, label,
            0x40055000, 0x03C,
            'SENSORSTATE', 'LESENSE.SENSORSTATE', 'read-write',
            "",
            0x00000000, 0x0000000F)

        self.SENSORSTATE = RM_Field_LESENSE_SENSORSTATE_SENSORSTATE(self)
        self.zz_fdict['SENSORSTATE'] = self.SENSORSTATE
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_IDLECONF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_IDLECONF, self).__init__(rmio, label,
            0x40055000, 0x040,
            'IDLECONF', 'LESENSE.IDLECONF', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.CH0 = RM_Field_LESENSE_IDLECONF_CH0(self)
        self.zz_fdict['CH0'] = self.CH0
        self.CH1 = RM_Field_LESENSE_IDLECONF_CH1(self)
        self.zz_fdict['CH1'] = self.CH1
        self.CH2 = RM_Field_LESENSE_IDLECONF_CH2(self)
        self.zz_fdict['CH2'] = self.CH2
        self.CH3 = RM_Field_LESENSE_IDLECONF_CH3(self)
        self.zz_fdict['CH3'] = self.CH3
        self.CH4 = RM_Field_LESENSE_IDLECONF_CH4(self)
        self.zz_fdict['CH4'] = self.CH4
        self.CH5 = RM_Field_LESENSE_IDLECONF_CH5(self)
        self.zz_fdict['CH5'] = self.CH5
        self.CH6 = RM_Field_LESENSE_IDLECONF_CH6(self)
        self.zz_fdict['CH6'] = self.CH6
        self.CH7 = RM_Field_LESENSE_IDLECONF_CH7(self)
        self.zz_fdict['CH7'] = self.CH7
        self.CH8 = RM_Field_LESENSE_IDLECONF_CH8(self)
        self.zz_fdict['CH8'] = self.CH8
        self.CH9 = RM_Field_LESENSE_IDLECONF_CH9(self)
        self.zz_fdict['CH9'] = self.CH9
        self.CH10 = RM_Field_LESENSE_IDLECONF_CH10(self)
        self.zz_fdict['CH10'] = self.CH10
        self.CH11 = RM_Field_LESENSE_IDLECONF_CH11(self)
        self.zz_fdict['CH11'] = self.CH11
        self.CH12 = RM_Field_LESENSE_IDLECONF_CH12(self)
        self.zz_fdict['CH12'] = self.CH12
        self.CH13 = RM_Field_LESENSE_IDLECONF_CH13(self)
        self.zz_fdict['CH13'] = self.CH13
        self.CH14 = RM_Field_LESENSE_IDLECONF_CH14(self)
        self.zz_fdict['CH14'] = self.CH14
        self.CH15 = RM_Field_LESENSE_IDLECONF_CH15(self)
        self.zz_fdict['CH15'] = self.CH15
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ALTEXCONF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ALTEXCONF, self).__init__(rmio, label,
            0x40055000, 0x044,
            'ALTEXCONF', 'LESENSE.ALTEXCONF', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.IDLECONF0 = RM_Field_LESENSE_ALTEXCONF_IDLECONF0(self)
        self.zz_fdict['IDLECONF0'] = self.IDLECONF0
        self.IDLECONF1 = RM_Field_LESENSE_ALTEXCONF_IDLECONF1(self)
        self.zz_fdict['IDLECONF1'] = self.IDLECONF1
        self.IDLECONF2 = RM_Field_LESENSE_ALTEXCONF_IDLECONF2(self)
        self.zz_fdict['IDLECONF2'] = self.IDLECONF2
        self.IDLECONF3 = RM_Field_LESENSE_ALTEXCONF_IDLECONF3(self)
        self.zz_fdict['IDLECONF3'] = self.IDLECONF3
        self.IDLECONF4 = RM_Field_LESENSE_ALTEXCONF_IDLECONF4(self)
        self.zz_fdict['IDLECONF4'] = self.IDLECONF4
        self.IDLECONF5 = RM_Field_LESENSE_ALTEXCONF_IDLECONF5(self)
        self.zz_fdict['IDLECONF5'] = self.IDLECONF5
        self.IDLECONF6 = RM_Field_LESENSE_ALTEXCONF_IDLECONF6(self)
        self.zz_fdict['IDLECONF6'] = self.IDLECONF6
        self.IDLECONF7 = RM_Field_LESENSE_ALTEXCONF_IDLECONF7(self)
        self.zz_fdict['IDLECONF7'] = self.IDLECONF7
        self.AEX0 = RM_Field_LESENSE_ALTEXCONF_AEX0(self)
        self.zz_fdict['AEX0'] = self.AEX0
        self.AEX1 = RM_Field_LESENSE_ALTEXCONF_AEX1(self)
        self.zz_fdict['AEX1'] = self.AEX1
        self.AEX2 = RM_Field_LESENSE_ALTEXCONF_AEX2(self)
        self.zz_fdict['AEX2'] = self.AEX2
        self.AEX3 = RM_Field_LESENSE_ALTEXCONF_AEX3(self)
        self.zz_fdict['AEX3'] = self.AEX3
        self.AEX4 = RM_Field_LESENSE_ALTEXCONF_AEX4(self)
        self.zz_fdict['AEX4'] = self.AEX4
        self.AEX5 = RM_Field_LESENSE_ALTEXCONF_AEX5(self)
        self.zz_fdict['AEX5'] = self.AEX5
        self.AEX6 = RM_Field_LESENSE_ALTEXCONF_AEX6(self)
        self.zz_fdict['AEX6'] = self.AEX6
        self.AEX7 = RM_Field_LESENSE_ALTEXCONF_AEX7(self)
        self.zz_fdict['AEX7'] = self.AEX7
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_IF, self).__init__(rmio, label,
            0x40055000, 0x050,
            'IF', 'LESENSE.IF', 'read-only',
            "",
            0x00000000, 0x007FFFFF)

        self.CH0 = RM_Field_LESENSE_IF_CH0(self)
        self.zz_fdict['CH0'] = self.CH0
        self.CH1 = RM_Field_LESENSE_IF_CH1(self)
        self.zz_fdict['CH1'] = self.CH1
        self.CH2 = RM_Field_LESENSE_IF_CH2(self)
        self.zz_fdict['CH2'] = self.CH2
        self.CH3 = RM_Field_LESENSE_IF_CH3(self)
        self.zz_fdict['CH3'] = self.CH3
        self.CH4 = RM_Field_LESENSE_IF_CH4(self)
        self.zz_fdict['CH4'] = self.CH4
        self.CH5 = RM_Field_LESENSE_IF_CH5(self)
        self.zz_fdict['CH5'] = self.CH5
        self.CH6 = RM_Field_LESENSE_IF_CH6(self)
        self.zz_fdict['CH6'] = self.CH6
        self.CH7 = RM_Field_LESENSE_IF_CH7(self)
        self.zz_fdict['CH7'] = self.CH7
        self.CH8 = RM_Field_LESENSE_IF_CH8(self)
        self.zz_fdict['CH8'] = self.CH8
        self.CH9 = RM_Field_LESENSE_IF_CH9(self)
        self.zz_fdict['CH9'] = self.CH9
        self.CH10 = RM_Field_LESENSE_IF_CH10(self)
        self.zz_fdict['CH10'] = self.CH10
        self.CH11 = RM_Field_LESENSE_IF_CH11(self)
        self.zz_fdict['CH11'] = self.CH11
        self.CH12 = RM_Field_LESENSE_IF_CH12(self)
        self.zz_fdict['CH12'] = self.CH12
        self.CH13 = RM_Field_LESENSE_IF_CH13(self)
        self.zz_fdict['CH13'] = self.CH13
        self.CH14 = RM_Field_LESENSE_IF_CH14(self)
        self.zz_fdict['CH14'] = self.CH14
        self.CH15 = RM_Field_LESENSE_IF_CH15(self)
        self.zz_fdict['CH15'] = self.CH15
        self.SCANCOMPLETE = RM_Field_LESENSE_IF_SCANCOMPLETE(self)
        self.zz_fdict['SCANCOMPLETE'] = self.SCANCOMPLETE
        self.DEC = RM_Field_LESENSE_IF_DEC(self)
        self.zz_fdict['DEC'] = self.DEC
        self.DECERR = RM_Field_LESENSE_IF_DECERR(self)
        self.zz_fdict['DECERR'] = self.DECERR
        self.BUFDATAV = RM_Field_LESENSE_IF_BUFDATAV(self)
        self.zz_fdict['BUFDATAV'] = self.BUFDATAV
        self.BUFLEVEL = RM_Field_LESENSE_IF_BUFLEVEL(self)
        self.zz_fdict['BUFLEVEL'] = self.BUFLEVEL
        self.BUFOF = RM_Field_LESENSE_IF_BUFOF(self)
        self.zz_fdict['BUFOF'] = self.BUFOF
        self.CNTOF = RM_Field_LESENSE_IF_CNTOF(self)
        self.zz_fdict['CNTOF'] = self.CNTOF
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_IFS, self).__init__(rmio, label,
            0x40055000, 0x054,
            'IFS', 'LESENSE.IFS', 'write-only',
            "",
            0x00000000, 0x007FFFFF)

        self.CH0 = RM_Field_LESENSE_IFS_CH0(self)
        self.zz_fdict['CH0'] = self.CH0
        self.CH1 = RM_Field_LESENSE_IFS_CH1(self)
        self.zz_fdict['CH1'] = self.CH1
        self.CH2 = RM_Field_LESENSE_IFS_CH2(self)
        self.zz_fdict['CH2'] = self.CH2
        self.CH3 = RM_Field_LESENSE_IFS_CH3(self)
        self.zz_fdict['CH3'] = self.CH3
        self.CH4 = RM_Field_LESENSE_IFS_CH4(self)
        self.zz_fdict['CH4'] = self.CH4
        self.CH5 = RM_Field_LESENSE_IFS_CH5(self)
        self.zz_fdict['CH5'] = self.CH5
        self.CH6 = RM_Field_LESENSE_IFS_CH6(self)
        self.zz_fdict['CH6'] = self.CH6
        self.CH7 = RM_Field_LESENSE_IFS_CH7(self)
        self.zz_fdict['CH7'] = self.CH7
        self.CH8 = RM_Field_LESENSE_IFS_CH8(self)
        self.zz_fdict['CH8'] = self.CH8
        self.CH9 = RM_Field_LESENSE_IFS_CH9(self)
        self.zz_fdict['CH9'] = self.CH9
        self.CH10 = RM_Field_LESENSE_IFS_CH10(self)
        self.zz_fdict['CH10'] = self.CH10
        self.CH11 = RM_Field_LESENSE_IFS_CH11(self)
        self.zz_fdict['CH11'] = self.CH11
        self.CH12 = RM_Field_LESENSE_IFS_CH12(self)
        self.zz_fdict['CH12'] = self.CH12
        self.CH13 = RM_Field_LESENSE_IFS_CH13(self)
        self.zz_fdict['CH13'] = self.CH13
        self.CH14 = RM_Field_LESENSE_IFS_CH14(self)
        self.zz_fdict['CH14'] = self.CH14
        self.CH15 = RM_Field_LESENSE_IFS_CH15(self)
        self.zz_fdict['CH15'] = self.CH15
        self.SCANCOMPLETE = RM_Field_LESENSE_IFS_SCANCOMPLETE(self)
        self.zz_fdict['SCANCOMPLETE'] = self.SCANCOMPLETE
        self.DEC = RM_Field_LESENSE_IFS_DEC(self)
        self.zz_fdict['DEC'] = self.DEC
        self.DECERR = RM_Field_LESENSE_IFS_DECERR(self)
        self.zz_fdict['DECERR'] = self.DECERR
        self.BUFDATAV = RM_Field_LESENSE_IFS_BUFDATAV(self)
        self.zz_fdict['BUFDATAV'] = self.BUFDATAV
        self.BUFLEVEL = RM_Field_LESENSE_IFS_BUFLEVEL(self)
        self.zz_fdict['BUFLEVEL'] = self.BUFLEVEL
        self.BUFOF = RM_Field_LESENSE_IFS_BUFOF(self)
        self.zz_fdict['BUFOF'] = self.BUFOF
        self.CNTOF = RM_Field_LESENSE_IFS_CNTOF(self)
        self.zz_fdict['CNTOF'] = self.CNTOF
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_IFC, self).__init__(rmio, label,
            0x40055000, 0x058,
            'IFC', 'LESENSE.IFC', 'write-only',
            "",
            0x00000000, 0x007FFFFF)

        self.CH0 = RM_Field_LESENSE_IFC_CH0(self)
        self.zz_fdict['CH0'] = self.CH0
        self.CH1 = RM_Field_LESENSE_IFC_CH1(self)
        self.zz_fdict['CH1'] = self.CH1
        self.CH2 = RM_Field_LESENSE_IFC_CH2(self)
        self.zz_fdict['CH2'] = self.CH2
        self.CH3 = RM_Field_LESENSE_IFC_CH3(self)
        self.zz_fdict['CH3'] = self.CH3
        self.CH4 = RM_Field_LESENSE_IFC_CH4(self)
        self.zz_fdict['CH4'] = self.CH4
        self.CH5 = RM_Field_LESENSE_IFC_CH5(self)
        self.zz_fdict['CH5'] = self.CH5
        self.CH6 = RM_Field_LESENSE_IFC_CH6(self)
        self.zz_fdict['CH6'] = self.CH6
        self.CH7 = RM_Field_LESENSE_IFC_CH7(self)
        self.zz_fdict['CH7'] = self.CH7
        self.CH8 = RM_Field_LESENSE_IFC_CH8(self)
        self.zz_fdict['CH8'] = self.CH8
        self.CH9 = RM_Field_LESENSE_IFC_CH9(self)
        self.zz_fdict['CH9'] = self.CH9
        self.CH10 = RM_Field_LESENSE_IFC_CH10(self)
        self.zz_fdict['CH10'] = self.CH10
        self.CH11 = RM_Field_LESENSE_IFC_CH11(self)
        self.zz_fdict['CH11'] = self.CH11
        self.CH12 = RM_Field_LESENSE_IFC_CH12(self)
        self.zz_fdict['CH12'] = self.CH12
        self.CH13 = RM_Field_LESENSE_IFC_CH13(self)
        self.zz_fdict['CH13'] = self.CH13
        self.CH14 = RM_Field_LESENSE_IFC_CH14(self)
        self.zz_fdict['CH14'] = self.CH14
        self.CH15 = RM_Field_LESENSE_IFC_CH15(self)
        self.zz_fdict['CH15'] = self.CH15
        self.SCANCOMPLETE = RM_Field_LESENSE_IFC_SCANCOMPLETE(self)
        self.zz_fdict['SCANCOMPLETE'] = self.SCANCOMPLETE
        self.DEC = RM_Field_LESENSE_IFC_DEC(self)
        self.zz_fdict['DEC'] = self.DEC
        self.DECERR = RM_Field_LESENSE_IFC_DECERR(self)
        self.zz_fdict['DECERR'] = self.DECERR
        self.BUFDATAV = RM_Field_LESENSE_IFC_BUFDATAV(self)
        self.zz_fdict['BUFDATAV'] = self.BUFDATAV
        self.BUFLEVEL = RM_Field_LESENSE_IFC_BUFLEVEL(self)
        self.zz_fdict['BUFLEVEL'] = self.BUFLEVEL
        self.BUFOF = RM_Field_LESENSE_IFC_BUFOF(self)
        self.zz_fdict['BUFOF'] = self.BUFOF
        self.CNTOF = RM_Field_LESENSE_IFC_CNTOF(self)
        self.zz_fdict['CNTOF'] = self.CNTOF
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_IEN, self).__init__(rmio, label,
            0x40055000, 0x05C,
            'IEN', 'LESENSE.IEN', 'read-write',
            "",
            0x00000000, 0x007FFFFF)

        self.CH0 = RM_Field_LESENSE_IEN_CH0(self)
        self.zz_fdict['CH0'] = self.CH0
        self.CH1 = RM_Field_LESENSE_IEN_CH1(self)
        self.zz_fdict['CH1'] = self.CH1
        self.CH2 = RM_Field_LESENSE_IEN_CH2(self)
        self.zz_fdict['CH2'] = self.CH2
        self.CH3 = RM_Field_LESENSE_IEN_CH3(self)
        self.zz_fdict['CH3'] = self.CH3
        self.CH4 = RM_Field_LESENSE_IEN_CH4(self)
        self.zz_fdict['CH4'] = self.CH4
        self.CH5 = RM_Field_LESENSE_IEN_CH5(self)
        self.zz_fdict['CH5'] = self.CH5
        self.CH6 = RM_Field_LESENSE_IEN_CH6(self)
        self.zz_fdict['CH6'] = self.CH6
        self.CH7 = RM_Field_LESENSE_IEN_CH7(self)
        self.zz_fdict['CH7'] = self.CH7
        self.CH8 = RM_Field_LESENSE_IEN_CH8(self)
        self.zz_fdict['CH8'] = self.CH8
        self.CH9 = RM_Field_LESENSE_IEN_CH9(self)
        self.zz_fdict['CH9'] = self.CH9
        self.CH10 = RM_Field_LESENSE_IEN_CH10(self)
        self.zz_fdict['CH10'] = self.CH10
        self.CH11 = RM_Field_LESENSE_IEN_CH11(self)
        self.zz_fdict['CH11'] = self.CH11
        self.CH12 = RM_Field_LESENSE_IEN_CH12(self)
        self.zz_fdict['CH12'] = self.CH12
        self.CH13 = RM_Field_LESENSE_IEN_CH13(self)
        self.zz_fdict['CH13'] = self.CH13
        self.CH14 = RM_Field_LESENSE_IEN_CH14(self)
        self.zz_fdict['CH14'] = self.CH14
        self.CH15 = RM_Field_LESENSE_IEN_CH15(self)
        self.zz_fdict['CH15'] = self.CH15
        self.SCANCOMPLETE = RM_Field_LESENSE_IEN_SCANCOMPLETE(self)
        self.zz_fdict['SCANCOMPLETE'] = self.SCANCOMPLETE
        self.DEC = RM_Field_LESENSE_IEN_DEC(self)
        self.zz_fdict['DEC'] = self.DEC
        self.DECERR = RM_Field_LESENSE_IEN_DECERR(self)
        self.zz_fdict['DECERR'] = self.DECERR
        self.BUFDATAV = RM_Field_LESENSE_IEN_BUFDATAV(self)
        self.zz_fdict['BUFDATAV'] = self.BUFDATAV
        self.BUFLEVEL = RM_Field_LESENSE_IEN_BUFLEVEL(self)
        self.zz_fdict['BUFLEVEL'] = self.BUFLEVEL
        self.BUFOF = RM_Field_LESENSE_IEN_BUFOF(self)
        self.zz_fdict['BUFOF'] = self.BUFOF
        self.CNTOF = RM_Field_LESENSE_IEN_CNTOF(self)
        self.zz_fdict['CNTOF'] = self.CNTOF
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_SYNCBUSY(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_SYNCBUSY, self).__init__(rmio, label,
            0x40055000, 0x060,
            'SYNCBUSY', 'LESENSE.SYNCBUSY', 'read-only',
            "",
            0x00000000, 0x00000080)

        self.CMD = RM_Field_LESENSE_SYNCBUSY_CMD(self)
        self.zz_fdict['CMD'] = self.CMD
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ROUTEPEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ROUTEPEN, self).__init__(rmio, label,
            0x40055000, 0x064,
            'ROUTEPEN', 'LESENSE.ROUTEPEN', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.CH0PEN = RM_Field_LESENSE_ROUTEPEN_CH0PEN(self)
        self.zz_fdict['CH0PEN'] = self.CH0PEN
        self.CH1PEN = RM_Field_LESENSE_ROUTEPEN_CH1PEN(self)
        self.zz_fdict['CH1PEN'] = self.CH1PEN
        self.CH2PEN = RM_Field_LESENSE_ROUTEPEN_CH2PEN(self)
        self.zz_fdict['CH2PEN'] = self.CH2PEN
        self.CH3PEN = RM_Field_LESENSE_ROUTEPEN_CH3PEN(self)
        self.zz_fdict['CH3PEN'] = self.CH3PEN
        self.CH4PEN = RM_Field_LESENSE_ROUTEPEN_CH4PEN(self)
        self.zz_fdict['CH4PEN'] = self.CH4PEN
        self.CH5PEN = RM_Field_LESENSE_ROUTEPEN_CH5PEN(self)
        self.zz_fdict['CH5PEN'] = self.CH5PEN
        self.CH6PEN = RM_Field_LESENSE_ROUTEPEN_CH6PEN(self)
        self.zz_fdict['CH6PEN'] = self.CH6PEN
        self.CH7PEN = RM_Field_LESENSE_ROUTEPEN_CH7PEN(self)
        self.zz_fdict['CH7PEN'] = self.CH7PEN
        self.CH8PEN = RM_Field_LESENSE_ROUTEPEN_CH8PEN(self)
        self.zz_fdict['CH8PEN'] = self.CH8PEN
        self.CH9PEN = RM_Field_LESENSE_ROUTEPEN_CH9PEN(self)
        self.zz_fdict['CH9PEN'] = self.CH9PEN
        self.CH10PEN = RM_Field_LESENSE_ROUTEPEN_CH10PEN(self)
        self.zz_fdict['CH10PEN'] = self.CH10PEN
        self.CH11PEN = RM_Field_LESENSE_ROUTEPEN_CH11PEN(self)
        self.zz_fdict['CH11PEN'] = self.CH11PEN
        self.CH12PEN = RM_Field_LESENSE_ROUTEPEN_CH12PEN(self)
        self.zz_fdict['CH12PEN'] = self.CH12PEN
        self.CH13PEN = RM_Field_LESENSE_ROUTEPEN_CH13PEN(self)
        self.zz_fdict['CH13PEN'] = self.CH13PEN
        self.CH14PEN = RM_Field_LESENSE_ROUTEPEN_CH14PEN(self)
        self.zz_fdict['CH14PEN'] = self.CH14PEN
        self.CH15PEN = RM_Field_LESENSE_ROUTEPEN_CH15PEN(self)
        self.zz_fdict['CH15PEN'] = self.CH15PEN
        self.ALTEX0PEN = RM_Field_LESENSE_ROUTEPEN_ALTEX0PEN(self)
        self.zz_fdict['ALTEX0PEN'] = self.ALTEX0PEN
        self.ALTEX1PEN = RM_Field_LESENSE_ROUTEPEN_ALTEX1PEN(self)
        self.zz_fdict['ALTEX1PEN'] = self.ALTEX1PEN
        self.ALTEX2PEN = RM_Field_LESENSE_ROUTEPEN_ALTEX2PEN(self)
        self.zz_fdict['ALTEX2PEN'] = self.ALTEX2PEN
        self.ALTEX3PEN = RM_Field_LESENSE_ROUTEPEN_ALTEX3PEN(self)
        self.zz_fdict['ALTEX3PEN'] = self.ALTEX3PEN
        self.ALTEX4PEN = RM_Field_LESENSE_ROUTEPEN_ALTEX4PEN(self)
        self.zz_fdict['ALTEX4PEN'] = self.ALTEX4PEN
        self.ALTEX5PEN = RM_Field_LESENSE_ROUTEPEN_ALTEX5PEN(self)
        self.zz_fdict['ALTEX5PEN'] = self.ALTEX5PEN
        self.ALTEX6PEN = RM_Field_LESENSE_ROUTEPEN_ALTEX6PEN(self)
        self.zz_fdict['ALTEX6PEN'] = self.ALTEX6PEN
        self.ALTEX7PEN = RM_Field_LESENSE_ROUTEPEN_ALTEX7PEN(self)
        self.zz_fdict['ALTEX7PEN'] = self.ALTEX7PEN
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_FEATURECONF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_FEATURECONF, self).__init__(rmio, label,
            0x40055000, 0x090,
            'FEATURECONF', 'LESENSE.FEATURECONF', 'read-write',
            "",
            0x00000000, 0x00000006)

        self.FCDISDAC = RM_Field_LESENSE_FEATURECONF_FCDISDAC(self)
        self.zz_fdict['FCDISDAC'] = self.FCDISDAC
        self.FCDISDEC = RM_Field_LESENSE_FEATURECONF_FCDISDEC(self)
        self.zz_fdict['FCDISDEC'] = self.FCDISDEC
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_TESTCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_TESTCTRL, self).__init__(rmio, label,
            0x40055000, 0x094,
            'TESTCTRL', 'LESENSE.TESTCTRL', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.RIPCNTCLK = RM_Field_LESENSE_TESTCTRL_RIPCNTCLK(self)
        self.zz_fdict['RIPCNTCLK'] = self.RIPCNTCLK
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_RIPCNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_RIPCNT, self).__init__(rmio, label,
            0x40055000, 0x098,
            'RIPCNT', 'LESENSE.RIPCNT', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.RIPCNT = RM_Field_LESENSE_RIPCNT_RIPCNT(self)
        self.zz_fdict['RIPCNT'] = self.RIPCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST0_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST0_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x100,
            'ST0_TCONFA', 'LESENSE.ST0_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST0_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST0_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST0_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST0_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST0_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST0_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST0_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST0_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST0_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST0_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x104,
            'ST0_TCONFB', 'LESENSE.ST0_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST0_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST0_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST0_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST0_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST0_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST0_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST0_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST1_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST1_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x108,
            'ST1_TCONFA', 'LESENSE.ST1_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST1_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST1_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST1_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST1_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST1_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST1_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST1_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST1_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST1_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST1_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x10C,
            'ST1_TCONFB', 'LESENSE.ST1_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST1_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST1_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST1_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST1_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST1_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST1_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST1_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST2_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST2_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x110,
            'ST2_TCONFA', 'LESENSE.ST2_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST2_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST2_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST2_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST2_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST2_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST2_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST2_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST2_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST2_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST2_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x114,
            'ST2_TCONFB', 'LESENSE.ST2_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST2_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST2_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST2_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST2_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST2_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST2_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST2_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST3_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST3_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x118,
            'ST3_TCONFA', 'LESENSE.ST3_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST3_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST3_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST3_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST3_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST3_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST3_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST3_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST3_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST3_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST3_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x11C,
            'ST3_TCONFB', 'LESENSE.ST3_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST3_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST3_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST3_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST3_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST3_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST3_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST3_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST4_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST4_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x120,
            'ST4_TCONFA', 'LESENSE.ST4_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST4_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST4_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST4_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST4_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST4_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST4_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST4_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST4_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST4_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST4_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x124,
            'ST4_TCONFB', 'LESENSE.ST4_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST4_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST4_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST4_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST4_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST4_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST4_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST4_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST5_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST5_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x128,
            'ST5_TCONFA', 'LESENSE.ST5_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST5_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST5_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST5_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST5_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST5_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST5_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST5_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST5_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST5_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST5_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x12C,
            'ST5_TCONFB', 'LESENSE.ST5_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST5_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST5_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST5_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST5_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST5_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST5_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST5_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST6_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST6_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x130,
            'ST6_TCONFA', 'LESENSE.ST6_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST6_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST6_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST6_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST6_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST6_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST6_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST6_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST6_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST6_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST6_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x134,
            'ST6_TCONFB', 'LESENSE.ST6_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST6_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST6_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST6_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST6_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST6_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST6_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST6_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST7_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST7_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x138,
            'ST7_TCONFA', 'LESENSE.ST7_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST7_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST7_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST7_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST7_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST7_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST7_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST7_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST7_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST7_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST7_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x13C,
            'ST7_TCONFB', 'LESENSE.ST7_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST7_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST7_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST7_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST7_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST7_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST7_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST7_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST8_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST8_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x140,
            'ST8_TCONFA', 'LESENSE.ST8_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST8_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST8_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST8_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST8_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST8_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST8_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST8_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST8_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST8_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST8_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x144,
            'ST8_TCONFB', 'LESENSE.ST8_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST8_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST8_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST8_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST8_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST8_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST8_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST8_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST9_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST9_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x148,
            'ST9_TCONFA', 'LESENSE.ST9_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST9_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST9_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST9_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST9_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST9_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST9_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST9_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST9_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST9_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST9_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x14C,
            'ST9_TCONFB', 'LESENSE.ST9_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST9_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST9_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST9_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST9_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST9_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST9_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST9_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST10_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST10_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x150,
            'ST10_TCONFA', 'LESENSE.ST10_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST10_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST10_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST10_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST10_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST10_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST10_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST10_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST10_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST10_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST10_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x154,
            'ST10_TCONFB', 'LESENSE.ST10_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST10_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST10_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST10_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST10_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST10_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST10_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST10_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST11_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST11_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x158,
            'ST11_TCONFA', 'LESENSE.ST11_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST11_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST11_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST11_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST11_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST11_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST11_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST11_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST11_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST11_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST11_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x15C,
            'ST11_TCONFB', 'LESENSE.ST11_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST11_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST11_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST11_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST11_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST11_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST11_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST11_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST12_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST12_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x160,
            'ST12_TCONFA', 'LESENSE.ST12_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST12_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST12_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST12_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST12_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST12_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST12_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST12_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST12_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST12_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST12_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x164,
            'ST12_TCONFB', 'LESENSE.ST12_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST12_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST12_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST12_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST12_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST12_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST12_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST12_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST13_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST13_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x168,
            'ST13_TCONFA', 'LESENSE.ST13_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST13_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST13_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST13_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST13_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST13_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST13_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST13_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST13_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST13_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST13_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x16C,
            'ST13_TCONFB', 'LESENSE.ST13_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST13_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST13_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST13_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST13_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST13_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST13_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST13_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST14_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST14_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x170,
            'ST14_TCONFA', 'LESENSE.ST14_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST14_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST14_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST14_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST14_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST14_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST14_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST14_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST14_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST14_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST14_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x174,
            'ST14_TCONFB', 'LESENSE.ST14_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST14_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST14_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST14_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST14_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST14_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST14_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST14_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST15_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST15_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x178,
            'ST15_TCONFA', 'LESENSE.ST15_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST15_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST15_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST15_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST15_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST15_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST15_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST15_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST15_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST15_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST15_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x17C,
            'ST15_TCONFB', 'LESENSE.ST15_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST15_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST15_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST15_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST15_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST15_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST15_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST15_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST16_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST16_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x180,
            'ST16_TCONFA', 'LESENSE.ST16_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST16_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST16_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST16_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST16_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST16_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST16_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST16_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST16_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST16_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST16_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x184,
            'ST16_TCONFB', 'LESENSE.ST16_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST16_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST16_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST16_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST16_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST16_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST16_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST16_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST17_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST17_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x188,
            'ST17_TCONFA', 'LESENSE.ST17_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST17_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST17_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST17_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST17_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST17_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST17_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST17_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST17_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST17_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST17_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x18C,
            'ST17_TCONFB', 'LESENSE.ST17_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST17_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST17_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST17_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST17_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST17_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST17_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST17_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST18_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST18_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x190,
            'ST18_TCONFA', 'LESENSE.ST18_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST18_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST18_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST18_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST18_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST18_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST18_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST18_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST18_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST18_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST18_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x194,
            'ST18_TCONFB', 'LESENSE.ST18_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST18_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST18_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST18_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST18_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST18_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST18_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST18_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST19_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST19_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x198,
            'ST19_TCONFA', 'LESENSE.ST19_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST19_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST19_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST19_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST19_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST19_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST19_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST19_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST19_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST19_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST19_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x19C,
            'ST19_TCONFB', 'LESENSE.ST19_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST19_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST19_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST19_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST19_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST19_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST19_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST19_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST20_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST20_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x1A0,
            'ST20_TCONFA', 'LESENSE.ST20_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST20_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST20_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST20_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST20_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST20_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST20_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST20_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST20_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST20_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST20_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x1A4,
            'ST20_TCONFB', 'LESENSE.ST20_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST20_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST20_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST20_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST20_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST20_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST20_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST20_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST21_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST21_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x1A8,
            'ST21_TCONFA', 'LESENSE.ST21_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST21_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST21_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST21_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST21_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST21_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST21_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST21_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST21_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST21_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST21_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x1AC,
            'ST21_TCONFB', 'LESENSE.ST21_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST21_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST21_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST21_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST21_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST21_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST21_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST21_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST22_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST22_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x1B0,
            'ST22_TCONFA', 'LESENSE.ST22_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST22_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST22_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST22_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST22_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST22_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST22_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST22_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST22_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST22_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST22_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x1B4,
            'ST22_TCONFB', 'LESENSE.ST22_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST22_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST22_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST22_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST22_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST22_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST22_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST22_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST23_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST23_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x1B8,
            'ST23_TCONFA', 'LESENSE.ST23_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST23_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST23_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST23_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST23_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST23_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST23_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST23_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST23_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST23_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST23_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x1BC,
            'ST23_TCONFB', 'LESENSE.ST23_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST23_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST23_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST23_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST23_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST23_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST23_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST23_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST24_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST24_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x1C0,
            'ST24_TCONFA', 'LESENSE.ST24_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST24_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST24_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST24_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST24_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST24_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST24_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST24_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST24_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST24_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST24_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x1C4,
            'ST24_TCONFB', 'LESENSE.ST24_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST24_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST24_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST24_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST24_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST24_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST24_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST24_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST25_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST25_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x1C8,
            'ST25_TCONFA', 'LESENSE.ST25_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST25_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST25_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST25_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST25_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST25_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST25_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST25_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST25_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST25_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST25_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x1CC,
            'ST25_TCONFB', 'LESENSE.ST25_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST25_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST25_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST25_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST25_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST25_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST25_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST25_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST26_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST26_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x1D0,
            'ST26_TCONFA', 'LESENSE.ST26_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST26_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST26_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST26_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST26_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST26_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST26_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST26_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST26_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST26_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST26_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x1D4,
            'ST26_TCONFB', 'LESENSE.ST26_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST26_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST26_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST26_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST26_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST26_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST26_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST26_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST27_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST27_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x1D8,
            'ST27_TCONFA', 'LESENSE.ST27_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST27_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST27_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST27_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST27_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST27_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST27_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST27_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST27_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST27_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST27_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x1DC,
            'ST27_TCONFB', 'LESENSE.ST27_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST27_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST27_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST27_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST27_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST27_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST27_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST27_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST28_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST28_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x1E0,
            'ST28_TCONFA', 'LESENSE.ST28_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST28_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST28_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST28_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST28_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST28_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST28_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST28_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST28_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST28_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST28_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x1E4,
            'ST28_TCONFB', 'LESENSE.ST28_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST28_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST28_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST28_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST28_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST28_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST28_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST28_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST29_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST29_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x1E8,
            'ST29_TCONFA', 'LESENSE.ST29_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST29_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST29_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST29_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST29_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST29_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST29_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST29_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST29_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST29_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST29_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x1EC,
            'ST29_TCONFB', 'LESENSE.ST29_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST29_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST29_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST29_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST29_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST29_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST29_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST29_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST30_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST30_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x1F0,
            'ST30_TCONFA', 'LESENSE.ST30_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST30_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST30_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST30_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST30_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST30_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST30_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST30_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST30_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST30_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST30_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x1F4,
            'ST30_TCONFB', 'LESENSE.ST30_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST30_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST30_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST30_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST30_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST30_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST30_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST30_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST31_TCONFA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST31_TCONFA, self).__init__(rmio, label,
            0x40055000, 0x1F8,
            'ST31_TCONFA', 'LESENSE.ST31_TCONFA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST31_TCONFA_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST31_TCONFA_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST31_TCONFA_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST31_TCONFA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.CHAIN = RM_Field_LESENSE_ST31_TCONFA_CHAIN(self)
        self.zz_fdict['CHAIN'] = self.CHAIN
        self.SETIF = RM_Field_LESENSE_ST31_TCONFA_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST31_TCONFA_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST31_TCONFA_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_ST31_TCONFB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_ST31_TCONFB, self).__init__(rmio, label,
            0x40055000, 0x1FC,
            'ST31_TCONFB', 'LESENSE.ST31_TCONFB', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMP = RM_Field_LESENSE_ST31_TCONFB_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.MASK = RM_Field_LESENSE_ST31_TCONFB_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.NEXTSTATE = RM_Field_LESENSE_ST31_TCONFB_NEXTSTATE(self)
        self.zz_fdict['NEXTSTATE'] = self.NEXTSTATE
        self.RESERVED0 = RM_Field_LESENSE_ST31_TCONFB_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.SETIF = RM_Field_LESENSE_ST31_TCONFB_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.PRSACT = RM_Field_LESENSE_ST31_TCONFB_PRSACT(self)
        self.zz_fdict['PRSACT'] = self.PRSACT
        self.RESERVED1 = RM_Field_LESENSE_ST31_TCONFB_RESERVED1(self)
        self.zz_fdict['RESERVED1'] = self.RESERVED1
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF0_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF0_DATA, self).__init__(rmio, label,
            0x40055000, 0x200,
            'BUF0_DATA', 'LESENSE.BUF0_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF0_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF0_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF0_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF1_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF1_DATA, self).__init__(rmio, label,
            0x40055000, 0x204,
            'BUF1_DATA', 'LESENSE.BUF1_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF1_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF1_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF1_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF2_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF2_DATA, self).__init__(rmio, label,
            0x40055000, 0x208,
            'BUF2_DATA', 'LESENSE.BUF2_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF2_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF2_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF2_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF3_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF3_DATA, self).__init__(rmio, label,
            0x40055000, 0x20C,
            'BUF3_DATA', 'LESENSE.BUF3_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF3_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF3_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF3_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF4_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF4_DATA, self).__init__(rmio, label,
            0x40055000, 0x210,
            'BUF4_DATA', 'LESENSE.BUF4_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF4_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF4_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF4_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF5_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF5_DATA, self).__init__(rmio, label,
            0x40055000, 0x214,
            'BUF5_DATA', 'LESENSE.BUF5_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF5_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF5_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF5_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF6_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF6_DATA, self).__init__(rmio, label,
            0x40055000, 0x218,
            'BUF6_DATA', 'LESENSE.BUF6_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF6_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF6_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF6_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF7_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF7_DATA, self).__init__(rmio, label,
            0x40055000, 0x21C,
            'BUF7_DATA', 'LESENSE.BUF7_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF7_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF7_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF7_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF8_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF8_DATA, self).__init__(rmio, label,
            0x40055000, 0x220,
            'BUF8_DATA', 'LESENSE.BUF8_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF8_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF8_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF8_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF9_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF9_DATA, self).__init__(rmio, label,
            0x40055000, 0x224,
            'BUF9_DATA', 'LESENSE.BUF9_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF9_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF9_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF9_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF10_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF10_DATA, self).__init__(rmio, label,
            0x40055000, 0x228,
            'BUF10_DATA', 'LESENSE.BUF10_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF10_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF10_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF10_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF11_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF11_DATA, self).__init__(rmio, label,
            0x40055000, 0x22C,
            'BUF11_DATA', 'LESENSE.BUF11_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF11_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF11_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF11_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF12_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF12_DATA, self).__init__(rmio, label,
            0x40055000, 0x230,
            'BUF12_DATA', 'LESENSE.BUF12_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF12_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF12_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF12_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF13_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF13_DATA, self).__init__(rmio, label,
            0x40055000, 0x234,
            'BUF13_DATA', 'LESENSE.BUF13_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF13_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF13_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF13_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF14_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF14_DATA, self).__init__(rmio, label,
            0x40055000, 0x238,
            'BUF14_DATA', 'LESENSE.BUF14_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF14_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF14_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF14_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_BUF15_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_BUF15_DATA, self).__init__(rmio, label,
            0x40055000, 0x23C,
            'BUF15_DATA', 'LESENSE.BUF15_DATA', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.DATA = RM_Field_LESENSE_BUF15_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.DATASRC = RM_Field_LESENSE_BUF15_DATA_DATASRC(self)
        self.zz_fdict['DATASRC'] = self.DATASRC
        self.RESERVED0 = RM_Field_LESENSE_BUF15_DATA_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH0_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH0_TIMING, self).__init__(rmio, label,
            0x40055000, 0x240,
            'CH0_TIMING', 'LESENSE.CH0_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH0_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH0_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH0_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH0_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH0_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x244,
            'CH0_INTERACT', 'LESENSE.CH0_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH0_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH0_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH0_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH0_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH0_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH0_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH0_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH0_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH0_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH0_EVAL, self).__init__(rmio, label,
            0x40055000, 0x248,
            'CH0_EVAL', 'LESENSE.CH0_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH0_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH0_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH0_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH0_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH0_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH0_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH0_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH1_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH1_TIMING, self).__init__(rmio, label,
            0x40055000, 0x250,
            'CH1_TIMING', 'LESENSE.CH1_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH1_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH1_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH1_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH1_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH1_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x254,
            'CH1_INTERACT', 'LESENSE.CH1_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH1_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH1_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH1_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH1_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH1_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH1_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH1_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH1_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH1_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH1_EVAL, self).__init__(rmio, label,
            0x40055000, 0x258,
            'CH1_EVAL', 'LESENSE.CH1_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH1_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH1_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH1_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH1_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH1_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH1_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH1_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH2_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH2_TIMING, self).__init__(rmio, label,
            0x40055000, 0x260,
            'CH2_TIMING', 'LESENSE.CH2_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH2_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH2_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH2_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH2_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH2_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x264,
            'CH2_INTERACT', 'LESENSE.CH2_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH2_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH2_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH2_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH2_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH2_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH2_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH2_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH2_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH2_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH2_EVAL, self).__init__(rmio, label,
            0x40055000, 0x268,
            'CH2_EVAL', 'LESENSE.CH2_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH2_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH2_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH2_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH2_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH2_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH2_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH2_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH3_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH3_TIMING, self).__init__(rmio, label,
            0x40055000, 0x270,
            'CH3_TIMING', 'LESENSE.CH3_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH3_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH3_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH3_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH3_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH3_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x274,
            'CH3_INTERACT', 'LESENSE.CH3_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH3_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH3_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH3_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH3_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH3_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH3_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH3_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH3_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH3_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH3_EVAL, self).__init__(rmio, label,
            0x40055000, 0x278,
            'CH3_EVAL', 'LESENSE.CH3_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH3_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH3_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH3_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH3_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH3_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH3_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH3_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH4_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH4_TIMING, self).__init__(rmio, label,
            0x40055000, 0x280,
            'CH4_TIMING', 'LESENSE.CH4_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH4_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH4_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH4_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH4_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH4_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x284,
            'CH4_INTERACT', 'LESENSE.CH4_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH4_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH4_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH4_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH4_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH4_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH4_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH4_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH4_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH4_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH4_EVAL, self).__init__(rmio, label,
            0x40055000, 0x288,
            'CH4_EVAL', 'LESENSE.CH4_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH4_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH4_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH4_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH4_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH4_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH4_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH4_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH5_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH5_TIMING, self).__init__(rmio, label,
            0x40055000, 0x290,
            'CH5_TIMING', 'LESENSE.CH5_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH5_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH5_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH5_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH5_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH5_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x294,
            'CH5_INTERACT', 'LESENSE.CH5_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH5_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH5_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH5_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH5_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH5_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH5_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH5_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH5_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH5_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH5_EVAL, self).__init__(rmio, label,
            0x40055000, 0x298,
            'CH5_EVAL', 'LESENSE.CH5_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH5_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH5_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH5_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH5_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH5_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH5_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH5_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH6_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH6_TIMING, self).__init__(rmio, label,
            0x40055000, 0x2A0,
            'CH6_TIMING', 'LESENSE.CH6_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH6_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH6_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH6_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH6_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH6_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x2A4,
            'CH6_INTERACT', 'LESENSE.CH6_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH6_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH6_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH6_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH6_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH6_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH6_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH6_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH6_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH6_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH6_EVAL, self).__init__(rmio, label,
            0x40055000, 0x2A8,
            'CH6_EVAL', 'LESENSE.CH6_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH6_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH6_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH6_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH6_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH6_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH6_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH6_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH7_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH7_TIMING, self).__init__(rmio, label,
            0x40055000, 0x2B0,
            'CH7_TIMING', 'LESENSE.CH7_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH7_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH7_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH7_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH7_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH7_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x2B4,
            'CH7_INTERACT', 'LESENSE.CH7_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH7_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH7_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH7_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH7_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH7_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH7_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH7_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH7_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH7_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH7_EVAL, self).__init__(rmio, label,
            0x40055000, 0x2B8,
            'CH7_EVAL', 'LESENSE.CH7_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH7_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH7_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH7_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH7_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH7_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH7_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH7_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH8_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH8_TIMING, self).__init__(rmio, label,
            0x40055000, 0x2C0,
            'CH8_TIMING', 'LESENSE.CH8_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH8_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH8_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH8_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH8_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH8_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x2C4,
            'CH8_INTERACT', 'LESENSE.CH8_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH8_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH8_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH8_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH8_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH8_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH8_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH8_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH8_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH8_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH8_EVAL, self).__init__(rmio, label,
            0x40055000, 0x2C8,
            'CH8_EVAL', 'LESENSE.CH8_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH8_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH8_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH8_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH8_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH8_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH8_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH8_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH9_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH9_TIMING, self).__init__(rmio, label,
            0x40055000, 0x2D0,
            'CH9_TIMING', 'LESENSE.CH9_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH9_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH9_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH9_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH9_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH9_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x2D4,
            'CH9_INTERACT', 'LESENSE.CH9_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH9_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH9_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH9_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH9_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH9_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH9_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH9_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH9_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH9_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH9_EVAL, self).__init__(rmio, label,
            0x40055000, 0x2D8,
            'CH9_EVAL', 'LESENSE.CH9_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH9_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH9_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH9_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH9_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH9_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH9_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH9_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH10_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH10_TIMING, self).__init__(rmio, label,
            0x40055000, 0x2E0,
            'CH10_TIMING', 'LESENSE.CH10_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH10_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH10_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH10_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH10_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH10_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x2E4,
            'CH10_INTERACT', 'LESENSE.CH10_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH10_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH10_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH10_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH10_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH10_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH10_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH10_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH10_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH10_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH10_EVAL, self).__init__(rmio, label,
            0x40055000, 0x2E8,
            'CH10_EVAL', 'LESENSE.CH10_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH10_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH10_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH10_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH10_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH10_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH10_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH10_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH11_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH11_TIMING, self).__init__(rmio, label,
            0x40055000, 0x2F0,
            'CH11_TIMING', 'LESENSE.CH11_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH11_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH11_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH11_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH11_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH11_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x2F4,
            'CH11_INTERACT', 'LESENSE.CH11_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH11_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH11_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH11_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH11_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH11_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH11_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH11_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH11_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH11_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH11_EVAL, self).__init__(rmio, label,
            0x40055000, 0x2F8,
            'CH11_EVAL', 'LESENSE.CH11_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH11_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH11_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH11_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH11_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH11_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH11_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH11_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH12_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH12_TIMING, self).__init__(rmio, label,
            0x40055000, 0x300,
            'CH12_TIMING', 'LESENSE.CH12_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH12_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH12_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH12_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH12_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH12_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x304,
            'CH12_INTERACT', 'LESENSE.CH12_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH12_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH12_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH12_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH12_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH12_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH12_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH12_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH12_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH12_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH12_EVAL, self).__init__(rmio, label,
            0x40055000, 0x308,
            'CH12_EVAL', 'LESENSE.CH12_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH12_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH12_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH12_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH12_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH12_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH12_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH12_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH13_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH13_TIMING, self).__init__(rmio, label,
            0x40055000, 0x310,
            'CH13_TIMING', 'LESENSE.CH13_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH13_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH13_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH13_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH13_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH13_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x314,
            'CH13_INTERACT', 'LESENSE.CH13_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH13_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH13_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH13_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH13_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH13_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH13_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH13_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH13_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH13_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH13_EVAL, self).__init__(rmio, label,
            0x40055000, 0x318,
            'CH13_EVAL', 'LESENSE.CH13_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH13_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH13_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH13_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH13_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH13_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH13_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH13_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH14_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH14_TIMING, self).__init__(rmio, label,
            0x40055000, 0x320,
            'CH14_TIMING', 'LESENSE.CH14_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH14_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH14_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH14_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH14_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH14_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x324,
            'CH14_INTERACT', 'LESENSE.CH14_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH14_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH14_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH14_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH14_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH14_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH14_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH14_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH14_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH14_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH14_EVAL, self).__init__(rmio, label,
            0x40055000, 0x328,
            'CH14_EVAL', 'LESENSE.CH14_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH14_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH14_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH14_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH14_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH14_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH14_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH14_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH15_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH15_TIMING, self).__init__(rmio, label,
            0x40055000, 0x330,
            'CH15_TIMING', 'LESENSE.CH15_TIMING', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.EXTIME = RM_Field_LESENSE_CH15_TIMING_EXTIME(self)
        self.zz_fdict['EXTIME'] = self.EXTIME
        self.SAMPLEDLY = RM_Field_LESENSE_CH15_TIMING_SAMPLEDLY(self)
        self.zz_fdict['SAMPLEDLY'] = self.SAMPLEDLY
        self.MEASUREDLY = RM_Field_LESENSE_CH15_TIMING_MEASUREDLY(self)
        self.zz_fdict['MEASUREDLY'] = self.MEASUREDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH15_INTERACT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH15_INTERACT, self).__init__(rmio, label,
            0x40055000, 0x334,
            'CH15_INTERACT', 'LESENSE.CH15_INTERACT', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.THRES = RM_Field_LESENSE_CH15_INTERACT_THRES(self)
        self.zz_fdict['THRES'] = self.THRES
        self.SAMPLE = RM_Field_LESENSE_CH15_INTERACT_SAMPLE(self)
        self.zz_fdict['SAMPLE'] = self.SAMPLE
        self.SETIF = RM_Field_LESENSE_CH15_INTERACT_SETIF(self)
        self.zz_fdict['SETIF'] = self.SETIF
        self.EXMODE = RM_Field_LESENSE_CH15_INTERACT_EXMODE(self)
        self.zz_fdict['EXMODE'] = self.EXMODE
        self.EXCLK = RM_Field_LESENSE_CH15_INTERACT_EXCLK(self)
        self.zz_fdict['EXCLK'] = self.EXCLK
        self.SAMPLECLK = RM_Field_LESENSE_CH15_INTERACT_SAMPLECLK(self)
        self.zz_fdict['SAMPLECLK'] = self.SAMPLECLK
        self.ALTEX = RM_Field_LESENSE_CH15_INTERACT_ALTEX(self)
        self.zz_fdict['ALTEX'] = self.ALTEX
        self.RESERVED0 = RM_Field_LESENSE_CH15_INTERACT_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


class RM_Register_LESENSE_CH15_EVAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LESENSE_CH15_EVAL, self).__init__(rmio, label,
            0x40055000, 0x338,
            'CH15_EVAL', 'LESENSE.CH15_EVAL', 'read-write',
            "",
            0x00000000, 0x00FFFFFF)

        self.COMPTHRES = RM_Field_LESENSE_CH15_EVAL_COMPTHRES(self)
        self.zz_fdict['COMPTHRES'] = self.COMPTHRES
        self.COMP = RM_Field_LESENSE_CH15_EVAL_COMP(self)
        self.zz_fdict['COMP'] = self.COMP
        self.DECODE = RM_Field_LESENSE_CH15_EVAL_DECODE(self)
        self.zz_fdict['DECODE'] = self.DECODE
        self.STRSAMPLE = RM_Field_LESENSE_CH15_EVAL_STRSAMPLE(self)
        self.zz_fdict['STRSAMPLE'] = self.STRSAMPLE
        self.SCANRESINV = RM_Field_LESENSE_CH15_EVAL_SCANRESINV(self)
        self.zz_fdict['SCANRESINV'] = self.SCANRESINV
        self.MODE = RM_Field_LESENSE_CH15_EVAL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.RESERVED0 = RM_Field_LESENSE_CH15_EVAL_RESERVED0(self)
        self.zz_fdict['RESERVED0'] = self.RESERVED0
        self.__dict__['zz_frozen'] = True


