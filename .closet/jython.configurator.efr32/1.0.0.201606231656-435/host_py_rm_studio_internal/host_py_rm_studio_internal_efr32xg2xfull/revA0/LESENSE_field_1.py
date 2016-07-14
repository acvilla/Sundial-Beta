
from static import Base_RM_Field
from LESENSE_enum import *


class RM_Field_LESENSE_CTRL_SCANMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CTRL_SCANMODE, self).__init__(register,
            'SCANMODE', 'LESENSE.CTRL.SCANMODE', 'read-write',
            "",
            0, 2,
            RM_Enum_LESENSE_CTRL_SCANMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'LESENSE.CTRL.PRSSEL', 'read-write',
            "",
            2, 4,
            RM_Enum_LESENSE_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CTRL_SCANCONF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CTRL_SCANCONF, self).__init__(register,
            'SCANCONF', 'LESENSE.CTRL.SCANCONF', 'read-write',
            "",
            7, 2,
            RM_Enum_LESENSE_CTRL_SCANCONF(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CTRL_ALTEXMAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CTRL_ALTEXMAP, self).__init__(register,
            'ALTEXMAP', 'LESENSE.CTRL.ALTEXMAP', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CTRL_DUALSAMPLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CTRL_DUALSAMPLE, self).__init__(register,
            'DUALSAMPLE', 'LESENSE.CTRL.DUALSAMPLE', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CTRL_BUFOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CTRL_BUFOW, self).__init__(register,
            'BUFOW', 'LESENSE.CTRL.BUFOW', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CTRL_STRSCANRES(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CTRL_STRSCANRES, self).__init__(register,
            'STRSCANRES', 'LESENSE.CTRL.STRSCANRES', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CTRL_BUFIDL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CTRL_BUFIDL, self).__init__(register,
            'BUFIDL', 'LESENSE.CTRL.BUFIDL', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CTRL_DMAWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CTRL_DMAWU, self).__init__(register,
            'DMAWU', 'LESENSE.CTRL.DMAWU', 'read-write',
            "",
            20, 2,
            RM_Enum_LESENSE_CTRL_DMAWU(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CTRL_DEBUGRUN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CTRL_DEBUGRUN, self).__init__(register,
            'DEBUGRUN', 'LESENSE.CTRL.DEBUGRUN', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_TIMCTRL_AUXPRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_TIMCTRL_AUXPRESC, self).__init__(register,
            'AUXPRESC', 'LESENSE.TIMCTRL.AUXPRESC', 'read-write',
            "",
            0, 2,
            RM_Enum_LESENSE_TIMCTRL_AUXPRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_TIMCTRL_LFPRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_TIMCTRL_LFPRESC, self).__init__(register,
            'LFPRESC', 'LESENSE.TIMCTRL.LFPRESC', 'read-write',
            "",
            4, 3,
            RM_Enum_LESENSE_TIMCTRL_LFPRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_TIMCTRL_PCPRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_TIMCTRL_PCPRESC, self).__init__(register,
            'PCPRESC', 'LESENSE.TIMCTRL.PCPRESC', 'read-write',
            "",
            8, 3,
            RM_Enum_LESENSE_TIMCTRL_PCPRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_TIMCTRL_PCTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_TIMCTRL_PCTOP, self).__init__(register,
            'PCTOP', 'LESENSE.TIMCTRL.PCTOP', 'read-write',
            "",
            12, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_TIMCTRL_STARTDLY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_TIMCTRL_STARTDLY, self).__init__(register,
            'STARTDLY', 'LESENSE.TIMCTRL.STARTDLY', 'read-write',
            "",
            22, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_TIMCTRL_AUXSTARTUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_TIMCTRL_AUXSTARTUP, self).__init__(register,
            'AUXSTARTUP', 'LESENSE.TIMCTRL.AUXSTARTUP', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PERCTRL_DACCH0EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PERCTRL_DACCH0EN, self).__init__(register,
            'DACCH0EN', 'LESENSE.PERCTRL.DACCH0EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PERCTRL_DACCH1EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PERCTRL_DACCH1EN, self).__init__(register,
            'DACCH1EN', 'LESENSE.PERCTRL.DACCH1EN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PERCTRL_DACCH0DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PERCTRL_DACCH0DATA, self).__init__(register,
            'DACCH0DATA', 'LESENSE.PERCTRL.DACCH0DATA', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PERCTRL_DACCH1DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PERCTRL_DACCH1DATA, self).__init__(register,
            'DACCH1DATA', 'LESENSE.PERCTRL.DACCH1DATA', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PERCTRL_DACSTARTUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PERCTRL_DACSTARTUP, self).__init__(register,
            'DACSTARTUP', 'LESENSE.PERCTRL.DACSTARTUP', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PERCTRL_DACCONVTRIG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PERCTRL_DACCONVTRIG, self).__init__(register,
            'DACCONVTRIG', 'LESENSE.PERCTRL.DACCONVTRIG', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PERCTRL_ACMP0MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PERCTRL_ACMP0MODE, self).__init__(register,
            'ACMP0MODE', 'LESENSE.PERCTRL.ACMP0MODE', 'read-write',
            "",
            20, 2,
            RM_Enum_LESENSE_PERCTRL_ACMP0MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PERCTRL_ACMP1MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PERCTRL_ACMP1MODE, self).__init__(register,
            'ACMP1MODE', 'LESENSE.PERCTRL.ACMP1MODE', 'read-write',
            "",
            22, 2,
            RM_Enum_LESENSE_PERCTRL_ACMP1MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PERCTRL_ACMP0INV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PERCTRL_ACMP0INV, self).__init__(register,
            'ACMP0INV', 'LESENSE.PERCTRL.ACMP0INV', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PERCTRL_ACMP1INV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PERCTRL_ACMP1INV, self).__init__(register,
            'ACMP1INV', 'LESENSE.PERCTRL.ACMP1INV', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PERCTRL_ACMP0HYSTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PERCTRL_ACMP0HYSTEN, self).__init__(register,
            'ACMP0HYSTEN', 'LESENSE.PERCTRL.ACMP0HYSTEN', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PERCTRL_ACMP1HYSTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PERCTRL_ACMP1HYSTEN, self).__init__(register,
            'ACMP1HYSTEN', 'LESENSE.PERCTRL.ACMP1HYSTEN', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PERCTRL_WARMUPMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PERCTRL_WARMUPMODE, self).__init__(register,
            'WARMUPMODE', 'LESENSE.PERCTRL.WARMUPMODE', 'read-write',
            "",
            28, 2,
            RM_Enum_LESENSE_PERCTRL_WARMUPMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_DECCTRL_DISABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_DECCTRL_DISABLE, self).__init__(register,
            'DISABLE', 'LESENSE.DECCTRL.DISABLE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_DECCTRL_ERRCHK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_DECCTRL_ERRCHK, self).__init__(register,
            'ERRCHK', 'LESENSE.DECCTRL.ERRCHK', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_DECCTRL_INTMAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_DECCTRL_INTMAP, self).__init__(register,
            'INTMAP', 'LESENSE.DECCTRL.INTMAP', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_DECCTRL_HYSTPRS0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_DECCTRL_HYSTPRS0, self).__init__(register,
            'HYSTPRS0', 'LESENSE.DECCTRL.HYSTPRS0', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_DECCTRL_HYSTPRS1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_DECCTRL_HYSTPRS1, self).__init__(register,
            'HYSTPRS1', 'LESENSE.DECCTRL.HYSTPRS1', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_DECCTRL_HYSTPRS2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_DECCTRL_HYSTPRS2, self).__init__(register,
            'HYSTPRS2', 'LESENSE.DECCTRL.HYSTPRS2', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_DECCTRL_HYSTIRQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_DECCTRL_HYSTIRQ, self).__init__(register,
            'HYSTIRQ', 'LESENSE.DECCTRL.HYSTIRQ', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_DECCTRL_PRSCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_DECCTRL_PRSCNT, self).__init__(register,
            'PRSCNT', 'LESENSE.DECCTRL.PRSCNT', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_DECCTRL_INPUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_DECCTRL_INPUT, self).__init__(register,
            'INPUT', 'LESENSE.DECCTRL.INPUT', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_DECCTRL_PRSSEL0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_DECCTRL_PRSSEL0, self).__init__(register,
            'PRSSEL0', 'LESENSE.DECCTRL.PRSSEL0', 'read-write',
            "",
            10, 4,
            RM_Enum_LESENSE_DECCTRL_PRSSEL0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_DECCTRL_PRSSEL1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_DECCTRL_PRSSEL1, self).__init__(register,
            'PRSSEL1', 'LESENSE.DECCTRL.PRSSEL1', 'read-write',
            "",
            15, 4,
            RM_Enum_LESENSE_DECCTRL_PRSSEL1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_DECCTRL_PRSSEL2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_DECCTRL_PRSSEL2, self).__init__(register,
            'PRSSEL2', 'LESENSE.DECCTRL.PRSSEL2', 'read-write',
            "",
            20, 4,
            RM_Enum_LESENSE_DECCTRL_PRSSEL2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_DECCTRL_PRSSEL3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_DECCTRL_PRSSEL3, self).__init__(register,
            'PRSSEL3', 'LESENSE.DECCTRL.PRSSEL3', 'read-write',
            "",
            25, 4,
            RM_Enum_LESENSE_DECCTRL_PRSSEL3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_BIASCTRL_BIASMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_BIASCTRL_BIASMODE, self).__init__(register,
            'BIASMODE', 'LESENSE.BIASCTRL.BIASMODE', 'read-write',
            "",
            0, 2,
            RM_Enum_LESENSE_BIASCTRL_BIASMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_BIASCTRL_BGRHIGHACCEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_BIASCTRL_BGRHIGHACCEN, self).__init__(register,
            'BGRHIGHACCEN', 'LESENSE.BIASCTRL.BGRHIGHACCEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_EVALCTRL_WINSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_EVALCTRL_WINSIZE, self).__init__(register,
            'WINSIZE', 'LESENSE.EVALCTRL.WINSIZE', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PRSCTRL_DECCMPVAL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PRSCTRL_DECCMPVAL, self).__init__(register,
            'DECCMPVAL', 'LESENSE.PRSCTRL.DECCMPVAL', 'read-write',
            "",
            0, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PRSCTRL_DECCMPMASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PRSCTRL_DECCMPMASK, self).__init__(register,
            'DECCMPMASK', 'LESENSE.PRSCTRL.DECCMPMASK', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PRSCTRL_DECCMPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PRSCTRL_DECCMPEN, self).__init__(register,
            'DECCMPEN', 'LESENSE.PRSCTRL.DECCMPEN', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CMD_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CMD_START, self).__init__(register,
            'START', 'LESENSE.CMD.START', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CMD_STOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CMD_STOP, self).__init__(register,
            'STOP', 'LESENSE.CMD.STOP', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CMD_DECODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CMD_DECODE, self).__init__(register,
            'DECODE', 'LESENSE.CMD.DECODE', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CMD_CLEARBUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CMD_CLEARBUF, self).__init__(register,
            'CLEARBUF', 'LESENSE.CMD.CLEARBUF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CHEN_CHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CHEN_CHEN, self).__init__(register,
            'CHEN', 'LESENSE.CHEN.CHEN', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_SCANRES_SCANRES(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_SCANRES_SCANRES, self).__init__(register,
            'SCANRES', 'LESENSE.SCANRES.SCANRES', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_SCANRES_STEPDIR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_SCANRES_STEPDIR, self).__init__(register,
            'STEPDIR', 'LESENSE.SCANRES.STEPDIR', 'read-write',
            "",
            16, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_STATUS_BUFDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_STATUS_BUFDATAV, self).__init__(register,
            'BUFDATAV', 'LESENSE.STATUS.BUFDATAV', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_STATUS_BUFHALFFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_STATUS_BUFHALFFULL, self).__init__(register,
            'BUFHALFFULL', 'LESENSE.STATUS.BUFHALFFULL', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_STATUS_BUFFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_STATUS_BUFFULL, self).__init__(register,
            'BUFFULL', 'LESENSE.STATUS.BUFFULL', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_STATUS_RUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_STATUS_RUNNING, self).__init__(register,
            'RUNNING', 'LESENSE.STATUS.RUNNING', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_STATUS_SCANACTIVE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_STATUS_SCANACTIVE, self).__init__(register,
            'SCANACTIVE', 'LESENSE.STATUS.SCANACTIVE', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_STATUS_DACACTIVE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_STATUS_DACACTIVE, self).__init__(register,
            'DACACTIVE', 'LESENSE.STATUS.DACACTIVE', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PTR_RD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PTR_RD, self).__init__(register,
            'RD', 'LESENSE.PTR.RD', 'read-only',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_PTR_WR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_PTR_WR, self).__init__(register,
            'WR', 'LESENSE.PTR.WR', 'read-only',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_BUFDATA_BUFDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_BUFDATA_BUFDATA, self).__init__(register,
            'BUFDATA', 'LESENSE.BUFDATA.BUFDATA', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_BUFDATA_BUFDATASRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_BUFDATA_BUFDATASRC, self).__init__(register,
            'BUFDATASRC', 'LESENSE.BUFDATA.BUFDATASRC', 'read-only',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_BUFDATA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_BUFDATA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.BUFDATA.RESERVED0', 'read-only',
            "",
            20, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_CURCH_CURCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_CURCH_CURCH, self).__init__(register,
            'CURCH', 'LESENSE.CURCH.CURCH', 'read-only',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_DECSTATE_DECSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_DECSTATE_DECSTATE, self).__init__(register,
            'DECSTATE', 'LESENSE.DECSTATE.DECSTATE', 'read-write',
            "",
            0, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_SENSORSTATE_SENSORSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_SENSORSTATE_SENSORSTATE, self).__init__(register,
            'SENSORSTATE', 'LESENSE.SENSORSTATE.SENSORSTATE', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH0, self).__init__(register,
            'CH0', 'LESENSE.IDLECONF.CH0', 'read-write',
            "",
            0, 2,
            RM_Enum_LESENSE_IDLECONF_CH0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH1, self).__init__(register,
            'CH1', 'LESENSE.IDLECONF.CH1', 'read-write',
            "",
            2, 2,
            RM_Enum_LESENSE_IDLECONF_CH1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH2, self).__init__(register,
            'CH2', 'LESENSE.IDLECONF.CH2', 'read-write',
            "",
            4, 2,
            RM_Enum_LESENSE_IDLECONF_CH2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH3, self).__init__(register,
            'CH3', 'LESENSE.IDLECONF.CH3', 'read-write',
            "",
            6, 2,
            RM_Enum_LESENSE_IDLECONF_CH3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH4, self).__init__(register,
            'CH4', 'LESENSE.IDLECONF.CH4', 'read-write',
            "",
            8, 2,
            RM_Enum_LESENSE_IDLECONF_CH4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH5, self).__init__(register,
            'CH5', 'LESENSE.IDLECONF.CH5', 'read-write',
            "",
            10, 2,
            RM_Enum_LESENSE_IDLECONF_CH5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH6, self).__init__(register,
            'CH6', 'LESENSE.IDLECONF.CH6', 'read-write',
            "",
            12, 2,
            RM_Enum_LESENSE_IDLECONF_CH6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH7, self).__init__(register,
            'CH7', 'LESENSE.IDLECONF.CH7', 'read-write',
            "",
            14, 2,
            RM_Enum_LESENSE_IDLECONF_CH7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH8, self).__init__(register,
            'CH8', 'LESENSE.IDLECONF.CH8', 'read-write',
            "",
            16, 2,
            RM_Enum_LESENSE_IDLECONF_CH8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH9, self).__init__(register,
            'CH9', 'LESENSE.IDLECONF.CH9', 'read-write',
            "",
            18, 2,
            RM_Enum_LESENSE_IDLECONF_CH9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH10, self).__init__(register,
            'CH10', 'LESENSE.IDLECONF.CH10', 'read-write',
            "",
            20, 2,
            RM_Enum_LESENSE_IDLECONF_CH10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH11, self).__init__(register,
            'CH11', 'LESENSE.IDLECONF.CH11', 'read-write',
            "",
            22, 2,
            RM_Enum_LESENSE_IDLECONF_CH11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH12, self).__init__(register,
            'CH12', 'LESENSE.IDLECONF.CH12', 'read-write',
            "",
            24, 2,
            RM_Enum_LESENSE_IDLECONF_CH12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH13, self).__init__(register,
            'CH13', 'LESENSE.IDLECONF.CH13', 'read-write',
            "",
            26, 2,
            RM_Enum_LESENSE_IDLECONF_CH13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH14, self).__init__(register,
            'CH14', 'LESENSE.IDLECONF.CH14', 'read-write',
            "",
            28, 2,
            RM_Enum_LESENSE_IDLECONF_CH14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IDLECONF_CH15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IDLECONF_CH15, self).__init__(register,
            'CH15', 'LESENSE.IDLECONF.CH15', 'read-write',
            "",
            30, 2,
            RM_Enum_LESENSE_IDLECONF_CH15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_IDLECONF0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_IDLECONF0, self).__init__(register,
            'IDLECONF0', 'LESENSE.ALTEXCONF.IDLECONF0', 'read-write',
            "",
            0, 2,
            RM_Enum_LESENSE_ALTEXCONF_IDLECONF0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_IDLECONF1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_IDLECONF1, self).__init__(register,
            'IDLECONF1', 'LESENSE.ALTEXCONF.IDLECONF1', 'read-write',
            "",
            2, 2,
            RM_Enum_LESENSE_ALTEXCONF_IDLECONF1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_IDLECONF2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_IDLECONF2, self).__init__(register,
            'IDLECONF2', 'LESENSE.ALTEXCONF.IDLECONF2', 'read-write',
            "",
            4, 2,
            RM_Enum_LESENSE_ALTEXCONF_IDLECONF2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_IDLECONF3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_IDLECONF3, self).__init__(register,
            'IDLECONF3', 'LESENSE.ALTEXCONF.IDLECONF3', 'read-write',
            "",
            6, 2,
            RM_Enum_LESENSE_ALTEXCONF_IDLECONF3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_IDLECONF4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_IDLECONF4, self).__init__(register,
            'IDLECONF4', 'LESENSE.ALTEXCONF.IDLECONF4', 'read-write',
            "",
            8, 2,
            RM_Enum_LESENSE_ALTEXCONF_IDLECONF4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_IDLECONF5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_IDLECONF5, self).__init__(register,
            'IDLECONF5', 'LESENSE.ALTEXCONF.IDLECONF5', 'read-write',
            "",
            10, 2,
            RM_Enum_LESENSE_ALTEXCONF_IDLECONF5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_IDLECONF6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_IDLECONF6, self).__init__(register,
            'IDLECONF6', 'LESENSE.ALTEXCONF.IDLECONF6', 'read-write',
            "",
            12, 2,
            RM_Enum_LESENSE_ALTEXCONF_IDLECONF6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_IDLECONF7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_IDLECONF7, self).__init__(register,
            'IDLECONF7', 'LESENSE.ALTEXCONF.IDLECONF7', 'read-write',
            "",
            14, 2,
            RM_Enum_LESENSE_ALTEXCONF_IDLECONF7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_AEX0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_AEX0, self).__init__(register,
            'AEX0', 'LESENSE.ALTEXCONF.AEX0', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_AEX1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_AEX1, self).__init__(register,
            'AEX1', 'LESENSE.ALTEXCONF.AEX1', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_AEX2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_AEX2, self).__init__(register,
            'AEX2', 'LESENSE.ALTEXCONF.AEX2', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_AEX3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_AEX3, self).__init__(register,
            'AEX3', 'LESENSE.ALTEXCONF.AEX3', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_AEX4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_AEX4, self).__init__(register,
            'AEX4', 'LESENSE.ALTEXCONF.AEX4', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_AEX5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_AEX5, self).__init__(register,
            'AEX5', 'LESENSE.ALTEXCONF.AEX5', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_AEX6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_AEX6, self).__init__(register,
            'AEX6', 'LESENSE.ALTEXCONF.AEX6', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ALTEXCONF_AEX7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ALTEXCONF_AEX7, self).__init__(register,
            'AEX7', 'LESENSE.ALTEXCONF.AEX7', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH0, self).__init__(register,
            'CH0', 'LESENSE.IF.CH0', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH1, self).__init__(register,
            'CH1', 'LESENSE.IF.CH1', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH2, self).__init__(register,
            'CH2', 'LESENSE.IF.CH2', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH3, self).__init__(register,
            'CH3', 'LESENSE.IF.CH3', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH4, self).__init__(register,
            'CH4', 'LESENSE.IF.CH4', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH5, self).__init__(register,
            'CH5', 'LESENSE.IF.CH5', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH6, self).__init__(register,
            'CH6', 'LESENSE.IF.CH6', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH7, self).__init__(register,
            'CH7', 'LESENSE.IF.CH7', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH8, self).__init__(register,
            'CH8', 'LESENSE.IF.CH8', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH9, self).__init__(register,
            'CH9', 'LESENSE.IF.CH9', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH10, self).__init__(register,
            'CH10', 'LESENSE.IF.CH10', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH11, self).__init__(register,
            'CH11', 'LESENSE.IF.CH11', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH12, self).__init__(register,
            'CH12', 'LESENSE.IF.CH12', 'read-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH13, self).__init__(register,
            'CH13', 'LESENSE.IF.CH13', 'read-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH14, self).__init__(register,
            'CH14', 'LESENSE.IF.CH14', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CH15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CH15, self).__init__(register,
            'CH15', 'LESENSE.IF.CH15', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_SCANCOMPLETE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_SCANCOMPLETE, self).__init__(register,
            'SCANCOMPLETE', 'LESENSE.IF.SCANCOMPLETE', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_DEC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_DEC, self).__init__(register,
            'DEC', 'LESENSE.IF.DEC', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_DECERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_DECERR, self).__init__(register,
            'DECERR', 'LESENSE.IF.DECERR', 'read-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_BUFDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_BUFDATAV, self).__init__(register,
            'BUFDATAV', 'LESENSE.IF.BUFDATAV', 'read-only',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_BUFLEVEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_BUFLEVEL, self).__init__(register,
            'BUFLEVEL', 'LESENSE.IF.BUFLEVEL', 'read-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_BUFOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_BUFOF, self).__init__(register,
            'BUFOF', 'LESENSE.IF.BUFOF', 'read-only',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IF_CNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IF_CNTOF, self).__init__(register,
            'CNTOF', 'LESENSE.IF.CNTOF', 'read-only',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH0, self).__init__(register,
            'CH0', 'LESENSE.IFS.CH0', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH1, self).__init__(register,
            'CH1', 'LESENSE.IFS.CH1', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH2, self).__init__(register,
            'CH2', 'LESENSE.IFS.CH2', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH3, self).__init__(register,
            'CH3', 'LESENSE.IFS.CH3', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH4, self).__init__(register,
            'CH4', 'LESENSE.IFS.CH4', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH5, self).__init__(register,
            'CH5', 'LESENSE.IFS.CH5', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH6, self).__init__(register,
            'CH6', 'LESENSE.IFS.CH6', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH7, self).__init__(register,
            'CH7', 'LESENSE.IFS.CH7', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH8, self).__init__(register,
            'CH8', 'LESENSE.IFS.CH8', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH9, self).__init__(register,
            'CH9', 'LESENSE.IFS.CH9', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH10, self).__init__(register,
            'CH10', 'LESENSE.IFS.CH10', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH11, self).__init__(register,
            'CH11', 'LESENSE.IFS.CH11', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH12, self).__init__(register,
            'CH12', 'LESENSE.IFS.CH12', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH13, self).__init__(register,
            'CH13', 'LESENSE.IFS.CH13', 'write-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH14, self).__init__(register,
            'CH14', 'LESENSE.IFS.CH14', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CH15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CH15, self).__init__(register,
            'CH15', 'LESENSE.IFS.CH15', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_SCANCOMPLETE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_SCANCOMPLETE, self).__init__(register,
            'SCANCOMPLETE', 'LESENSE.IFS.SCANCOMPLETE', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_DEC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_DEC, self).__init__(register,
            'DEC', 'LESENSE.IFS.DEC', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_DECERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_DECERR, self).__init__(register,
            'DECERR', 'LESENSE.IFS.DECERR', 'write-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_BUFDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_BUFDATAV, self).__init__(register,
            'BUFDATAV', 'LESENSE.IFS.BUFDATAV', 'write-only',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_BUFLEVEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_BUFLEVEL, self).__init__(register,
            'BUFLEVEL', 'LESENSE.IFS.BUFLEVEL', 'write-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_BUFOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_BUFOF, self).__init__(register,
            'BUFOF', 'LESENSE.IFS.BUFOF', 'write-only',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFS_CNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFS_CNTOF, self).__init__(register,
            'CNTOF', 'LESENSE.IFS.CNTOF', 'write-only',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH0, self).__init__(register,
            'CH0', 'LESENSE.IFC.CH0', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH1, self).__init__(register,
            'CH1', 'LESENSE.IFC.CH1', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH2, self).__init__(register,
            'CH2', 'LESENSE.IFC.CH2', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH3, self).__init__(register,
            'CH3', 'LESENSE.IFC.CH3', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH4, self).__init__(register,
            'CH4', 'LESENSE.IFC.CH4', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH5, self).__init__(register,
            'CH5', 'LESENSE.IFC.CH5', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH6, self).__init__(register,
            'CH6', 'LESENSE.IFC.CH6', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH7, self).__init__(register,
            'CH7', 'LESENSE.IFC.CH7', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH8, self).__init__(register,
            'CH8', 'LESENSE.IFC.CH8', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH9, self).__init__(register,
            'CH9', 'LESENSE.IFC.CH9', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH10, self).__init__(register,
            'CH10', 'LESENSE.IFC.CH10', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH11, self).__init__(register,
            'CH11', 'LESENSE.IFC.CH11', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH12, self).__init__(register,
            'CH12', 'LESENSE.IFC.CH12', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH13, self).__init__(register,
            'CH13', 'LESENSE.IFC.CH13', 'write-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH14, self).__init__(register,
            'CH14', 'LESENSE.IFC.CH14', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CH15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CH15, self).__init__(register,
            'CH15', 'LESENSE.IFC.CH15', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_SCANCOMPLETE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_SCANCOMPLETE, self).__init__(register,
            'SCANCOMPLETE', 'LESENSE.IFC.SCANCOMPLETE', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_DEC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_DEC, self).__init__(register,
            'DEC', 'LESENSE.IFC.DEC', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_DECERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_DECERR, self).__init__(register,
            'DECERR', 'LESENSE.IFC.DECERR', 'write-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_BUFDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_BUFDATAV, self).__init__(register,
            'BUFDATAV', 'LESENSE.IFC.BUFDATAV', 'write-only',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_BUFLEVEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_BUFLEVEL, self).__init__(register,
            'BUFLEVEL', 'LESENSE.IFC.BUFLEVEL', 'write-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_BUFOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_BUFOF, self).__init__(register,
            'BUFOF', 'LESENSE.IFC.BUFOF', 'write-only',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IFC_CNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IFC_CNTOF, self).__init__(register,
            'CNTOF', 'LESENSE.IFC.CNTOF', 'write-only',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH0, self).__init__(register,
            'CH0', 'LESENSE.IEN.CH0', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH1, self).__init__(register,
            'CH1', 'LESENSE.IEN.CH1', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH2, self).__init__(register,
            'CH2', 'LESENSE.IEN.CH2', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH3, self).__init__(register,
            'CH3', 'LESENSE.IEN.CH3', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH4, self).__init__(register,
            'CH4', 'LESENSE.IEN.CH4', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH5, self).__init__(register,
            'CH5', 'LESENSE.IEN.CH5', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH6, self).__init__(register,
            'CH6', 'LESENSE.IEN.CH6', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH7, self).__init__(register,
            'CH7', 'LESENSE.IEN.CH7', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH8, self).__init__(register,
            'CH8', 'LESENSE.IEN.CH8', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH9, self).__init__(register,
            'CH9', 'LESENSE.IEN.CH9', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH10, self).__init__(register,
            'CH10', 'LESENSE.IEN.CH10', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH11, self).__init__(register,
            'CH11', 'LESENSE.IEN.CH11', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH12, self).__init__(register,
            'CH12', 'LESENSE.IEN.CH12', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH13, self).__init__(register,
            'CH13', 'LESENSE.IEN.CH13', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH14, self).__init__(register,
            'CH14', 'LESENSE.IEN.CH14', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CH15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CH15, self).__init__(register,
            'CH15', 'LESENSE.IEN.CH15', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_SCANCOMPLETE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_SCANCOMPLETE, self).__init__(register,
            'SCANCOMPLETE', 'LESENSE.IEN.SCANCOMPLETE', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_DEC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_DEC, self).__init__(register,
            'DEC', 'LESENSE.IEN.DEC', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_DECERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_DECERR, self).__init__(register,
            'DECERR', 'LESENSE.IEN.DECERR', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_BUFDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_BUFDATAV, self).__init__(register,
            'BUFDATAV', 'LESENSE.IEN.BUFDATAV', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_BUFLEVEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_BUFLEVEL, self).__init__(register,
            'BUFLEVEL', 'LESENSE.IEN.BUFLEVEL', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_BUFOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_BUFOF, self).__init__(register,
            'BUFOF', 'LESENSE.IEN.BUFOF', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_IEN_CNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_IEN_CNTOF, self).__init__(register,
            'CNTOF', 'LESENSE.IEN.CNTOF', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_SYNCBUSY_CMD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_SYNCBUSY_CMD, self).__init__(register,
            'CMD', 'LESENSE.SYNCBUSY.CMD', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH0PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH0PEN, self).__init__(register,
            'CH0PEN', 'LESENSE.ROUTEPEN.CH0PEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH1PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH1PEN, self).__init__(register,
            'CH1PEN', 'LESENSE.ROUTEPEN.CH1PEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH2PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH2PEN, self).__init__(register,
            'CH2PEN', 'LESENSE.ROUTEPEN.CH2PEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH3PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH3PEN, self).__init__(register,
            'CH3PEN', 'LESENSE.ROUTEPEN.CH3PEN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH4PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH4PEN, self).__init__(register,
            'CH4PEN', 'LESENSE.ROUTEPEN.CH4PEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH5PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH5PEN, self).__init__(register,
            'CH5PEN', 'LESENSE.ROUTEPEN.CH5PEN', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH6PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH6PEN, self).__init__(register,
            'CH6PEN', 'LESENSE.ROUTEPEN.CH6PEN', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH7PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH7PEN, self).__init__(register,
            'CH7PEN', 'LESENSE.ROUTEPEN.CH7PEN', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH8PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH8PEN, self).__init__(register,
            'CH8PEN', 'LESENSE.ROUTEPEN.CH8PEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH9PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH9PEN, self).__init__(register,
            'CH9PEN', 'LESENSE.ROUTEPEN.CH9PEN', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH10PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH10PEN, self).__init__(register,
            'CH10PEN', 'LESENSE.ROUTEPEN.CH10PEN', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH11PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH11PEN, self).__init__(register,
            'CH11PEN', 'LESENSE.ROUTEPEN.CH11PEN', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH12PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH12PEN, self).__init__(register,
            'CH12PEN', 'LESENSE.ROUTEPEN.CH12PEN', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH13PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH13PEN, self).__init__(register,
            'CH13PEN', 'LESENSE.ROUTEPEN.CH13PEN', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH14PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH14PEN, self).__init__(register,
            'CH14PEN', 'LESENSE.ROUTEPEN.CH14PEN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_CH15PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_CH15PEN, self).__init__(register,
            'CH15PEN', 'LESENSE.ROUTEPEN.CH15PEN', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_ALTEX0PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_ALTEX0PEN, self).__init__(register,
            'ALTEX0PEN', 'LESENSE.ROUTEPEN.ALTEX0PEN', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_ALTEX1PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_ALTEX1PEN, self).__init__(register,
            'ALTEX1PEN', 'LESENSE.ROUTEPEN.ALTEX1PEN', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_ALTEX2PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_ALTEX2PEN, self).__init__(register,
            'ALTEX2PEN', 'LESENSE.ROUTEPEN.ALTEX2PEN', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_ALTEX3PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_ALTEX3PEN, self).__init__(register,
            'ALTEX3PEN', 'LESENSE.ROUTEPEN.ALTEX3PEN', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_ALTEX4PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_ALTEX4PEN, self).__init__(register,
            'ALTEX4PEN', 'LESENSE.ROUTEPEN.ALTEX4PEN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_ALTEX5PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_ALTEX5PEN, self).__init__(register,
            'ALTEX5PEN', 'LESENSE.ROUTEPEN.ALTEX5PEN', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_ALTEX6PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_ALTEX6PEN, self).__init__(register,
            'ALTEX6PEN', 'LESENSE.ROUTEPEN.ALTEX6PEN', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ROUTEPEN_ALTEX7PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ROUTEPEN_ALTEX7PEN, self).__init__(register,
            'ALTEX7PEN', 'LESENSE.ROUTEPEN.ALTEX7PEN', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_FEATURECONF_FCDISDAC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_FEATURECONF_FCDISDAC, self).__init__(register,
            'FCDISDAC', 'LESENSE.FEATURECONF.FCDISDAC', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_FEATURECONF_FCDISDEC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_FEATURECONF_FCDISDEC, self).__init__(register,
            'FCDISDEC', 'LESENSE.FEATURECONF.FCDISDEC', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_TESTCTRL_RIPCNTCLK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_TESTCTRL_RIPCNTCLK, self).__init__(register,
            'RIPCNTCLK', 'LESENSE.TESTCTRL.RIPCNTCLK', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_RIPCNT_RIPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_RIPCNT_RIPCNT, self).__init__(register,
            'RIPCNT', 'LESENSE.RIPCNT.RIPCNT', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST0_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST0_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST0_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST0_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST0_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST0_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST0_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST0_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST0_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST0_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST0_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST0_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST0_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST0_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST0_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST0_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST0_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST1_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST1_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST1_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST1_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST1_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST1_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST1_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST1_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST1_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST1_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST1_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST1_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST1_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST1_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST1_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST1_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST1_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST2_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST2_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST2_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST2_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST2_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST2_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST2_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST2_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST2_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST2_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST2_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST2_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST2_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST2_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST2_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST2_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST2_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST3_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST3_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST3_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST3_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST3_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST3_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST3_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST3_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST3_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST3_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST3_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST3_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST3_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST3_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST3_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST3_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST3_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST4_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST4_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST4_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST4_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST4_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST4_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST4_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST4_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST4_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST4_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST4_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST4_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST4_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST4_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST4_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST4_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST4_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST5_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST5_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST5_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST5_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST5_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST5_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST5_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST5_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST5_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST5_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST5_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST5_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST5_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST5_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST5_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST5_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST5_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST6_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST6_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST6_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST6_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST6_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST6_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST6_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST6_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST6_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST6_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST6_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST6_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST6_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST6_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST6_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST6_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST6_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST7_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST7_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST7_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST7_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST7_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST7_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST7_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST7_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST7_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST7_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST7_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST7_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST7_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST7_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST7_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST7_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST7_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST8_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST8_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST8_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST8_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST8_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST8_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST8_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST8_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST8_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST8_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST8_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST8_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST8_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST8_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST8_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST8_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST8_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST9_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST9_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST9_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST9_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST9_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST9_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST9_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST9_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST9_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST9_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST9_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST9_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST9_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST9_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST9_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST9_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST9_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST10_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST10_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST10_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST10_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST10_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST10_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST10_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST10_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST10_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST10_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST10_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST10_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST10_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST10_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST10_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST10_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST10_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST11_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST11_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST11_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST11_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST11_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST11_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST11_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST11_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST11_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST11_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST11_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST11_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST11_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST11_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST11_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST11_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST11_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST12_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST12_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST12_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST12_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST12_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST12_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST12_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST12_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST12_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST12_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST12_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST12_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST12_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST12_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST12_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST12_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST12_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST13_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST13_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST13_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST13_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST13_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST13_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST13_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST13_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST13_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST13_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST13_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST13_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST13_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST13_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST13_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST13_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST13_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST14_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST14_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST14_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST14_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST14_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST14_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST14_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST14_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST14_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST14_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST14_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST14_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST14_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST14_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST14_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST14_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST14_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST15_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST15_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST15_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST15_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST15_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST15_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST15_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST15_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST15_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST15_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST15_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST15_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST15_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST15_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST15_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST15_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST15_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST16_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST16_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST16_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST16_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST16_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST16_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST16_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST16_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST16_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST16_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST16_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST16_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST16_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST16_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST16_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST16_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST16_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST17_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST17_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST17_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST17_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST17_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST17_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST17_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST17_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST17_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST17_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST17_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST17_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST17_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST17_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST17_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST17_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST17_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST18_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST18_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST18_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST18_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST18_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST18_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST18_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST18_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST18_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST18_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST18_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST18_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST18_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST18_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST18_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST18_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST18_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST19_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST19_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST19_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST19_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST19_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST19_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST19_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST19_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST19_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST19_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST19_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST19_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST19_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST19_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST19_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST19_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST19_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST20_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST20_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST20_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST20_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST20_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST20_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST20_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST20_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST20_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST20_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST20_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST20_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST20_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST20_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST20_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST20_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST20_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST21_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST21_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST21_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST21_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST21_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST21_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST21_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST21_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST21_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST21_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST21_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST21_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST21_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST21_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST21_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST21_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST21_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST22_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST22_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST22_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST22_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST22_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST22_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST22_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST22_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST22_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST22_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST22_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST22_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST22_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST22_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST22_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST22_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST22_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST23_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST23_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST23_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST23_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST23_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST23_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST23_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST23_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST23_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST23_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST23_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST23_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST23_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST23_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST23_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST23_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST23_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST24_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST24_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST24_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST24_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST24_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST24_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST24_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST24_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST24_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST24_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST24_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST24_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST24_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST24_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST24_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST24_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST24_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST25_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST25_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST25_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST25_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST25_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST25_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST25_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST25_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST25_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST25_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST25_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST25_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST25_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST25_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST25_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST25_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST25_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST26_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST26_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST26_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST26_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST26_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST26_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST26_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST26_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST26_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST26_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST26_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST26_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST26_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST26_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST26_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST26_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST26_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST27_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST27_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST27_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST27_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST27_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST27_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST27_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST27_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST27_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST27_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST27_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST27_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST27_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST27_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST27_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST27_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST27_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST28_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST28_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST28_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST28_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST28_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST28_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST28_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST28_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST28_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST28_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST28_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST28_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST28_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST28_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST28_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST28_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST28_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST29_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST29_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST29_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST29_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST29_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST29_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST29_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST29_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST29_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST29_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST29_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST29_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST29_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST29_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST29_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST29_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST29_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST30_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST30_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST30_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST30_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST30_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST30_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST30_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST30_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST30_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST30_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST30_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST30_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST30_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST30_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST30_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST30_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST30_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFA_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFA_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST31_TCONFA.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFA_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFA_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST31_TCONFA.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFA_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFA_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST31_TCONFA.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFA_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFA_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST31_TCONFA.RESERVED0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFA_CHAIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFA_CHAIN, self).__init__(register,
            'CHAIN', 'LESENSE.ST31_TCONFA.CHAIN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFA_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFA_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST31_TCONFA.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFA_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFA_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST31_TCONFA.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFA_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFA_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST31_TCONFA.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFB_COMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFB_COMP, self).__init__(register,
            'COMP', 'LESENSE.ST31_TCONFB.COMP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFB_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFB_MASK, self).__init__(register,
            'MASK', 'LESENSE.ST31_TCONFB.MASK', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFB_NEXTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFB_NEXTSTATE, self).__init__(register,
            'NEXTSTATE', 'LESENSE.ST31_TCONFB.NEXTSTATE', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFB_RESERVED0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFB_RESERVED0, self).__init__(register,
            'RESERVED0', 'LESENSE.ST31_TCONFB.RESERVED0', 'read-write',
            "",
            13, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFB_SETIF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFB_SETIF, self).__init__(register,
            'SETIF', 'LESENSE.ST31_TCONFB.SETIF', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFB_PRSACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFB_PRSACT, self).__init__(register,
            'PRSACT', 'LESENSE.ST31_TCONFB.PRSACT', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LESENSE_ST31_TCONFB_RESERVED1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LESENSE_ST31_TCONFB_RESERVED1, self).__init__(register,
            'RESERVED1', 'LESENSE.ST31_TCONFB.RESERVED1', 'read-write',
            "",
            19, 5)
        self.__dict__['zz_frozen'] = True


