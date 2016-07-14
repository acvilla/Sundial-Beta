
from static import Base_RM_Register
from PROTIMER_field import *


class RM_Register_PROTIMER_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CTRL, self).__init__(rmio, label,
            0x40085000, 0x000,
            'CTRL', 'PROTIMER.CTRL', 'read-write',
            "",
            0x00000000, 0x3FF33336)

        self.DEBUGRUN = RM_Field_PROTIMER_CTRL_DEBUGRUN(self)
        self.zz_fdict['DEBUGRUN'] = self.DEBUGRUN
        self.DMACLRACT = RM_Field_PROTIMER_CTRL_DMACLRACT(self)
        self.zz_fdict['DMACLRACT'] = self.DMACLRACT
        self.OSMEN = RM_Field_PROTIMER_CTRL_OSMEN(self)
        self.zz_fdict['OSMEN'] = self.OSMEN
        self.ZEROSTARTEN = RM_Field_PROTIMER_CTRL_ZEROSTARTEN(self)
        self.zz_fdict['ZEROSTARTEN'] = self.ZEROSTARTEN
        self.PRECNTSRC = RM_Field_PROTIMER_CTRL_PRECNTSRC(self)
        self.zz_fdict['PRECNTSRC'] = self.PRECNTSRC
        self.BASECNTSRC = RM_Field_PROTIMER_CTRL_BASECNTSRC(self)
        self.zz_fdict['BASECNTSRC'] = self.BASECNTSRC
        self.WRAPCNTSRC = RM_Field_PROTIMER_CTRL_WRAPCNTSRC(self)
        self.zz_fdict['WRAPCNTSRC'] = self.WRAPCNTSRC
        self.TOUT0SRC = RM_Field_PROTIMER_CTRL_TOUT0SRC(self)
        self.zz_fdict['TOUT0SRC'] = self.TOUT0SRC
        self.TOUT0SYNCSRC = RM_Field_PROTIMER_CTRL_TOUT0SYNCSRC(self)
        self.zz_fdict['TOUT0SYNCSRC'] = self.TOUT0SYNCSRC
        self.TOUT1SRC = RM_Field_PROTIMER_CTRL_TOUT1SRC(self)
        self.zz_fdict['TOUT1SRC'] = self.TOUT1SRC
        self.TOUT1SYNCSRC = RM_Field_PROTIMER_CTRL_TOUT1SYNCSRC(self)
        self.zz_fdict['TOUT1SYNCSRC'] = self.TOUT1SYNCSRC
        self.TOUT0MODE = RM_Field_PROTIMER_CTRL_TOUT0MODE(self)
        self.zz_fdict['TOUT0MODE'] = self.TOUT0MODE
        self.TOUT1MODE = RM_Field_PROTIMER_CTRL_TOUT1MODE(self)
        self.zz_fdict['TOUT1MODE'] = self.TOUT1MODE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CMD, self).__init__(rmio, label,
            0x40085000, 0x004,
            'CMD', 'PROTIMER.CMD', 'write-only',
            "",
            0x00000000, 0x000700F7)

        self.START = RM_Field_PROTIMER_CMD_START(self)
        self.zz_fdict['START'] = self.START
        self.RTCSYNCSTART = RM_Field_PROTIMER_CMD_RTCSYNCSTART(self)
        self.zz_fdict['RTCSYNCSTART'] = self.RTCSYNCSTART
        self.STOP = RM_Field_PROTIMER_CMD_STOP(self)
        self.zz_fdict['STOP'] = self.STOP
        self.TOUT0START = RM_Field_PROTIMER_CMD_TOUT0START(self)
        self.zz_fdict['TOUT0START'] = self.TOUT0START
        self.TOUT0STOP = RM_Field_PROTIMER_CMD_TOUT0STOP(self)
        self.zz_fdict['TOUT0STOP'] = self.TOUT0STOP
        self.TOUT1START = RM_Field_PROTIMER_CMD_TOUT1START(self)
        self.zz_fdict['TOUT1START'] = self.TOUT1START
        self.TOUT1STOP = RM_Field_PROTIMER_CMD_TOUT1STOP(self)
        self.zz_fdict['TOUT1STOP'] = self.TOUT1STOP
        self.LBTSTART = RM_Field_PROTIMER_CMD_LBTSTART(self)
        self.zz_fdict['LBTSTART'] = self.LBTSTART
        self.LBTPAUSE = RM_Field_PROTIMER_CMD_LBTPAUSE(self)
        self.zz_fdict['LBTPAUSE'] = self.LBTPAUSE
        self.LBTSTOP = RM_Field_PROTIMER_CMD_LBTSTOP(self)
        self.zz_fdict['LBTSTOP'] = self.LBTSTOP
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_PRSCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_PRSCTRL, self).__init__(rmio, label,
            0x40085000, 0x008,
            'PRSCTRL', 'PROTIMER.PRSCTRL', 'read-write',
            "",
            0x00000000, 0x00FEFEFE)

        self.STARTPRSEN = RM_Field_PROTIMER_PRSCTRL_STARTPRSEN(self)
        self.zz_fdict['STARTPRSEN'] = self.STARTPRSEN
        self.STARTEDGE = RM_Field_PROTIMER_PRSCTRL_STARTEDGE(self)
        self.zz_fdict['STARTEDGE'] = self.STARTEDGE
        self.STARTPRSSEL = RM_Field_PROTIMER_PRSCTRL_STARTPRSSEL(self)
        self.zz_fdict['STARTPRSSEL'] = self.STARTPRSSEL
        self.STOPPRSEN = RM_Field_PROTIMER_PRSCTRL_STOPPRSEN(self)
        self.zz_fdict['STOPPRSEN'] = self.STOPPRSEN
        self.STOPEDGE = RM_Field_PROTIMER_PRSCTRL_STOPEDGE(self)
        self.zz_fdict['STOPEDGE'] = self.STOPEDGE
        self.STOPPRSSEL = RM_Field_PROTIMER_PRSCTRL_STOPPRSSEL(self)
        self.zz_fdict['STOPPRSSEL'] = self.STOPPRSSEL
        self.RTCCTRIGGERPRSEN = RM_Field_PROTIMER_PRSCTRL_RTCCTRIGGERPRSEN(self)
        self.zz_fdict['RTCCTRIGGERPRSEN'] = self.RTCCTRIGGERPRSEN
        self.RTCCTRIGGEREDGE = RM_Field_PROTIMER_PRSCTRL_RTCCTRIGGEREDGE(self)
        self.zz_fdict['RTCCTRIGGEREDGE'] = self.RTCCTRIGGEREDGE
        self.RTCCTRIGGERPRSSEL = RM_Field_PROTIMER_PRSCTRL_RTCCTRIGGERPRSSEL(self)
        self.zz_fdict['RTCCTRIGGERPRSSEL'] = self.RTCCTRIGGERPRSSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_STATUS, self).__init__(rmio, label,
            0x40085000, 0x00C,
            'STATUS', 'PROTIMER.STATUS', 'read-only',
            "",
            0x00000000, 0x00001FFF)

        self.RUNNING = RM_Field_PROTIMER_STATUS_RUNNING(self)
        self.zz_fdict['RUNNING'] = self.RUNNING
        self.LBTSYNC = RM_Field_PROTIMER_STATUS_LBTSYNC(self)
        self.zz_fdict['LBTSYNC'] = self.LBTSYNC
        self.LBTRUNNING = RM_Field_PROTIMER_STATUS_LBTRUNNING(self)
        self.zz_fdict['LBTRUNNING'] = self.LBTRUNNING
        self.LBTPAUSED = RM_Field_PROTIMER_STATUS_LBTPAUSED(self)
        self.zz_fdict['LBTPAUSED'] = self.LBTPAUSED
        self.TOUT0RUNNING = RM_Field_PROTIMER_STATUS_TOUT0RUNNING(self)
        self.zz_fdict['TOUT0RUNNING'] = self.TOUT0RUNNING
        self.TOUT0SYNC = RM_Field_PROTIMER_STATUS_TOUT0SYNC(self)
        self.zz_fdict['TOUT0SYNC'] = self.TOUT0SYNC
        self.TOUT1RUNNING = RM_Field_PROTIMER_STATUS_TOUT1RUNNING(self)
        self.zz_fdict['TOUT1RUNNING'] = self.TOUT1RUNNING
        self.TOUT1SYNC = RM_Field_PROTIMER_STATUS_TOUT1SYNC(self)
        self.zz_fdict['TOUT1SYNC'] = self.TOUT1SYNC
        self.ICV0 = RM_Field_PROTIMER_STATUS_ICV0(self)
        self.zz_fdict['ICV0'] = self.ICV0
        self.ICV1 = RM_Field_PROTIMER_STATUS_ICV1(self)
        self.zz_fdict['ICV1'] = self.ICV1
        self.ICV2 = RM_Field_PROTIMER_STATUS_ICV2(self)
        self.zz_fdict['ICV2'] = self.ICV2
        self.ICV3 = RM_Field_PROTIMER_STATUS_ICV3(self)
        self.zz_fdict['ICV3'] = self.ICV3
        self.ICV4 = RM_Field_PROTIMER_STATUS_ICV4(self)
        self.zz_fdict['ICV4'] = self.ICV4
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_PRECNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_PRECNT, self).__init__(rmio, label,
            0x40085000, 0x010,
            'PRECNT', 'PROTIMER.PRECNT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.PRECNT = RM_Field_PROTIMER_PRECNT_PRECNT(self)
        self.zz_fdict['PRECNT'] = self.PRECNT
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_BASECNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_BASECNT, self).__init__(rmio, label,
            0x40085000, 0x014,
            'BASECNT', 'PROTIMER.BASECNT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.BASECNT = RM_Field_PROTIMER_BASECNT_BASECNT(self)
        self.zz_fdict['BASECNT'] = self.BASECNT
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_WRAPCNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_WRAPCNT, self).__init__(rmio, label,
            0x40085000, 0x018,
            'WRAPCNT', 'PROTIMER.WRAPCNT', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.WRAPCNT = RM_Field_PROTIMER_WRAPCNT_WRAPCNT(self)
        self.zz_fdict['WRAPCNT'] = self.WRAPCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_BASEPRE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_BASEPRE, self).__init__(rmio, label,
            0x40085000, 0x01C,
            'BASEPRE', 'PROTIMER.BASEPRE', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.PRECNTV = RM_Field_PROTIMER_BASEPRE_PRECNTV(self)
        self.zz_fdict['PRECNTV'] = self.PRECNTV
        self.BASECNTV = RM_Field_PROTIMER_BASEPRE_BASECNTV(self)
        self.zz_fdict['BASECNTV'] = self.BASECNTV
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_LWRAPCNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_LWRAPCNT, self).__init__(rmio, label,
            0x40085000, 0x020,
            'LWRAPCNT', 'PROTIMER.LWRAPCNT', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.LWRAPCNT = RM_Field_PROTIMER_LWRAPCNT_LWRAPCNT(self)
        self.zz_fdict['LWRAPCNT'] = self.LWRAPCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_PRECNTTOPADJ(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_PRECNTTOPADJ, self).__init__(rmio, label,
            0x40085000, 0x024,
            'PRECNTTOPADJ', 'PROTIMER.PRECNTTOPADJ', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.PRECNTTOPADJ = RM_Field_PROTIMER_PRECNTTOPADJ_PRECNTTOPADJ(self)
        self.zz_fdict['PRECNTTOPADJ'] = self.PRECNTTOPADJ
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_PRECNTTOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_PRECNTTOP, self).__init__(rmio, label,
            0x40085000, 0x028,
            'PRECNTTOP', 'PROTIMER.PRECNTTOP', 'read-write',
            "",
            0x00FFFF00, 0x00FFFFFF)

        self.PRECNTTOPFRAC = RM_Field_PROTIMER_PRECNTTOP_PRECNTTOPFRAC(self)
        self.zz_fdict['PRECNTTOPFRAC'] = self.PRECNTTOPFRAC
        self.PRECNTTOP = RM_Field_PROTIMER_PRECNTTOP_PRECNTTOP(self)
        self.zz_fdict['PRECNTTOP'] = self.PRECNTTOP
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_BASECNTTOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_BASECNTTOP, self).__init__(rmio, label,
            0x40085000, 0x02C,
            'BASECNTTOP', 'PROTIMER.BASECNTTOP', 'read-write',
            "",
            0x0000FFFF, 0x0000FFFF)

        self.BASECNTTOP = RM_Field_PROTIMER_BASECNTTOP_BASECNTTOP(self)
        self.zz_fdict['BASECNTTOP'] = self.BASECNTTOP
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_WRAPCNTTOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_WRAPCNTTOP, self).__init__(rmio, label,
            0x40085000, 0x030,
            'WRAPCNTTOP', 'PROTIMER.WRAPCNTTOP', 'read-write',
            "",
            0xFFFFFFFF, 0xFFFFFFFF)

        self.WRAPCNTTOP = RM_Field_PROTIMER_WRAPCNTTOP_WRAPCNTTOP(self)
        self.zz_fdict['WRAPCNTTOP'] = self.WRAPCNTTOP
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_TOUT0CNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_TOUT0CNT, self).__init__(rmio, label,
            0x40085000, 0x034,
            'TOUT0CNT', 'PROTIMER.TOUT0CNT', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.TOUT0PCNT = RM_Field_PROTIMER_TOUT0CNT_TOUT0PCNT(self)
        self.zz_fdict['TOUT0PCNT'] = self.TOUT0PCNT
        self.TOUT0CNT = RM_Field_PROTIMER_TOUT0CNT_TOUT0CNT(self)
        self.zz_fdict['TOUT0CNT'] = self.TOUT0CNT
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_TOUT0CNTTOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_TOUT0CNTTOP, self).__init__(rmio, label,
            0x40085000, 0x038,
            'TOUT0CNTTOP', 'PROTIMER.TOUT0CNTTOP', 'read-write',
            "",
            0x00FF00FF, 0xFFFFFFFF)

        self.TOUT0PCNTTOP = RM_Field_PROTIMER_TOUT0CNTTOP_TOUT0PCNTTOP(self)
        self.zz_fdict['TOUT0PCNTTOP'] = self.TOUT0PCNTTOP
        self.TOUT0CNTTOP = RM_Field_PROTIMER_TOUT0CNTTOP_TOUT0CNTTOP(self)
        self.zz_fdict['TOUT0CNTTOP'] = self.TOUT0CNTTOP
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_TOUT0COMP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_TOUT0COMP, self).__init__(rmio, label,
            0x40085000, 0x03C,
            'TOUT0COMP', 'PROTIMER.TOUT0COMP', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.TOUT0PCNTCOMP = RM_Field_PROTIMER_TOUT0COMP_TOUT0PCNTCOMP(self)
        self.zz_fdict['TOUT0PCNTCOMP'] = self.TOUT0PCNTCOMP
        self.TOUT0CNTCOMP = RM_Field_PROTIMER_TOUT0COMP_TOUT0CNTCOMP(self)
        self.zz_fdict['TOUT0CNTCOMP'] = self.TOUT0CNTCOMP
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_TOUT1CNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_TOUT1CNT, self).__init__(rmio, label,
            0x40085000, 0x040,
            'TOUT1CNT', 'PROTIMER.TOUT1CNT', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.TOUT1PCNT = RM_Field_PROTIMER_TOUT1CNT_TOUT1PCNT(self)
        self.zz_fdict['TOUT1PCNT'] = self.TOUT1PCNT
        self.TOUT1CNT = RM_Field_PROTIMER_TOUT1CNT_TOUT1CNT(self)
        self.zz_fdict['TOUT1CNT'] = self.TOUT1CNT
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_TOUT1CNTTOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_TOUT1CNTTOP, self).__init__(rmio, label,
            0x40085000, 0x044,
            'TOUT1CNTTOP', 'PROTIMER.TOUT1CNTTOP', 'read-write',
            "",
            0x00FF00FF, 0xFFFFFFFF)

        self.TOUT1PCNTTOP = RM_Field_PROTIMER_TOUT1CNTTOP_TOUT1PCNTTOP(self)
        self.zz_fdict['TOUT1PCNTTOP'] = self.TOUT1PCNTTOP
        self.TOUT1CNTTOP = RM_Field_PROTIMER_TOUT1CNTTOP_TOUT1CNTTOP(self)
        self.zz_fdict['TOUT1CNTTOP'] = self.TOUT1CNTTOP
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_TOUT1COMP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_TOUT1COMP, self).__init__(rmio, label,
            0x40085000, 0x048,
            'TOUT1COMP', 'PROTIMER.TOUT1COMP', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.TOUT1PCNTCOMP = RM_Field_PROTIMER_TOUT1COMP_TOUT1PCNTCOMP(self)
        self.zz_fdict['TOUT1PCNTCOMP'] = self.TOUT1PCNTCOMP
        self.TOUT1CNTCOMP = RM_Field_PROTIMER_TOUT1COMP_TOUT1CNTCOMP(self)
        self.zz_fdict['TOUT1CNTCOMP'] = self.TOUT1CNTCOMP
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_LBTCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_LBTCTRL, self).__init__(rmio, label,
            0x40085000, 0x04C,
            'LBTCTRL', 'PROTIMER.LBTCTRL', 'read-write',
            "",
            0x00000000, 0x0F1F1FFF)

        self.STARTEXP = RM_Field_PROTIMER_LBTCTRL_STARTEXP(self)
        self.zz_fdict['STARTEXP'] = self.STARTEXP
        self.MAXEXP = RM_Field_PROTIMER_LBTCTRL_MAXEXP(self)
        self.zz_fdict['MAXEXP'] = self.MAXEXP
        self.CCADELAY = RM_Field_PROTIMER_LBTCTRL_CCADELAY(self)
        self.zz_fdict['CCADELAY'] = self.CCADELAY
        self.CCAREPEAT = RM_Field_PROTIMER_LBTCTRL_CCAREPEAT(self)
        self.zz_fdict['CCAREPEAT'] = self.CCAREPEAT
        self.FIXEDBACKOFF = RM_Field_PROTIMER_LBTCTRL_FIXEDBACKOFF(self)
        self.zz_fdict['FIXEDBACKOFF'] = self.FIXEDBACKOFF
        self.RETRYLIMIT = RM_Field_PROTIMER_LBTCTRL_RETRYLIMIT(self)
        self.zz_fdict['RETRYLIMIT'] = self.RETRYLIMIT
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_LBTPRSCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_LBTPRSCTRL, self).__init__(rmio, label,
            0x40085000, 0x050,
            'LBTPRSCTRL', 'PROTIMER.LBTPRSCTRL', 'read-write',
            "",
            0x00000000, 0x1F1F1F00)

        self.LBTSTARTPRSEN = RM_Field_PROTIMER_LBTPRSCTRL_LBTSTARTPRSEN(self)
        self.zz_fdict['LBTSTARTPRSEN'] = self.LBTSTARTPRSEN
        self.LBTSTARTPRSSEL = RM_Field_PROTIMER_LBTPRSCTRL_LBTSTARTPRSSEL(self)
        self.zz_fdict['LBTSTARTPRSSEL'] = self.LBTSTARTPRSSEL
        self.LBTPAUSEPRSEN = RM_Field_PROTIMER_LBTPRSCTRL_LBTPAUSEPRSEN(self)
        self.zz_fdict['LBTPAUSEPRSEN'] = self.LBTPAUSEPRSEN
        self.LBTPAUSEPRSSEL = RM_Field_PROTIMER_LBTPRSCTRL_LBTPAUSEPRSSEL(self)
        self.zz_fdict['LBTPAUSEPRSSEL'] = self.LBTPAUSEPRSSEL
        self.LBTSTOPPRSEN = RM_Field_PROTIMER_LBTPRSCTRL_LBTSTOPPRSEN(self)
        self.zz_fdict['LBTSTOPPRSEN'] = self.LBTSTOPPRSEN
        self.LBTSTOPPRSSEL = RM_Field_PROTIMER_LBTPRSCTRL_LBTSTOPPRSSEL(self)
        self.zz_fdict['LBTSTOPPRSSEL'] = self.LBTSTOPPRSSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_LBTSTATE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_LBTSTATE, self).__init__(rmio, label,
            0x40085000, 0x054,
            'LBTSTATE', 'PROTIMER.LBTSTATE', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.TOUT0PCNT = RM_Field_PROTIMER_LBTSTATE_TOUT0PCNT(self)
        self.zz_fdict['TOUT0PCNT'] = self.TOUT0PCNT
        self.TOUT0CNT = RM_Field_PROTIMER_LBTSTATE_TOUT0CNT(self)
        self.zz_fdict['TOUT0CNT'] = self.TOUT0CNT
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_RANDOM(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_RANDOM, self).__init__(rmio, label,
            0x40085000, 0x058,
            'RANDOM', 'PROTIMER.RANDOM', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.RANDOM = RM_Field_PROTIMER_RANDOM_RANDOM(self)
        self.zz_fdict['RANDOM'] = self.RANDOM
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_IF, self).__init__(rmio, label,
            0x40085000, 0x05C,
            'IF', 'PROTIMER.IF', 'read-only',
            "",
            0x00000000, 0x03F3FFF7)

        self.PRECNTOF = RM_Field_PROTIMER_IF_PRECNTOF(self)
        self.zz_fdict['PRECNTOF'] = self.PRECNTOF
        self.BASECNTOF = RM_Field_PROTIMER_IF_BASECNTOF(self)
        self.zz_fdict['BASECNTOF'] = self.BASECNTOF
        self.WRAPCNTOF = RM_Field_PROTIMER_IF_WRAPCNTOF(self)
        self.zz_fdict['WRAPCNTOF'] = self.WRAPCNTOF
        self.TOUT0 = RM_Field_PROTIMER_IF_TOUT0(self)
        self.zz_fdict['TOUT0'] = self.TOUT0
        self.TOUT1 = RM_Field_PROTIMER_IF_TOUT1(self)
        self.zz_fdict['TOUT1'] = self.TOUT1
        self.TOUT0MATCH = RM_Field_PROTIMER_IF_TOUT0MATCH(self)
        self.zz_fdict['TOUT0MATCH'] = self.TOUT0MATCH
        self.TOUT1MATCH = RM_Field_PROTIMER_IF_TOUT1MATCH(self)
        self.zz_fdict['TOUT1MATCH'] = self.TOUT1MATCH
        self.CC0 = RM_Field_PROTIMER_IF_CC0(self)
        self.zz_fdict['CC0'] = self.CC0
        self.CC1 = RM_Field_PROTIMER_IF_CC1(self)
        self.zz_fdict['CC1'] = self.CC1
        self.CC2 = RM_Field_PROTIMER_IF_CC2(self)
        self.zz_fdict['CC2'] = self.CC2
        self.CC3 = RM_Field_PROTIMER_IF_CC3(self)
        self.zz_fdict['CC3'] = self.CC3
        self.CC4 = RM_Field_PROTIMER_IF_CC4(self)
        self.zz_fdict['CC4'] = self.CC4
        self.COF0 = RM_Field_PROTIMER_IF_COF0(self)
        self.zz_fdict['COF0'] = self.COF0
        self.COF1 = RM_Field_PROTIMER_IF_COF1(self)
        self.zz_fdict['COF1'] = self.COF1
        self.COF2 = RM_Field_PROTIMER_IF_COF2(self)
        self.zz_fdict['COF2'] = self.COF2
        self.COF3 = RM_Field_PROTIMER_IF_COF3(self)
        self.zz_fdict['COF3'] = self.COF3
        self.COF4 = RM_Field_PROTIMER_IF_COF4(self)
        self.zz_fdict['COF4'] = self.COF4
        self.LBTSUCCESS = RM_Field_PROTIMER_IF_LBTSUCCESS(self)
        self.zz_fdict['LBTSUCCESS'] = self.LBTSUCCESS
        self.LBTRETRY = RM_Field_PROTIMER_IF_LBTRETRY(self)
        self.zz_fdict['LBTRETRY'] = self.LBTRETRY
        self.LBTFAILURE = RM_Field_PROTIMER_IF_LBTFAILURE(self)
        self.zz_fdict['LBTFAILURE'] = self.LBTFAILURE
        self.LBTPAUSED = RM_Field_PROTIMER_IF_LBTPAUSED(self)
        self.zz_fdict['LBTPAUSED'] = self.LBTPAUSED
        self.RTCCSYNCHED = RM_Field_PROTIMER_IF_RTCCSYNCHED(self)
        self.zz_fdict['RTCCSYNCHED'] = self.RTCCSYNCHED
        self.TOUT0MATCHLBT = RM_Field_PROTIMER_IF_TOUT0MATCHLBT(self)
        self.zz_fdict['TOUT0MATCHLBT'] = self.TOUT0MATCHLBT
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_IFS, self).__init__(rmio, label,
            0x40085000, 0x060,
            'IFS', 'PROTIMER.IFS', 'write-only',
            "",
            0x00000000, 0x03F3FFF7)

        self.PRECNTOF = RM_Field_PROTIMER_IFS_PRECNTOF(self)
        self.zz_fdict['PRECNTOF'] = self.PRECNTOF
        self.BASECNTOF = RM_Field_PROTIMER_IFS_BASECNTOF(self)
        self.zz_fdict['BASECNTOF'] = self.BASECNTOF
        self.WRAPCNTOF = RM_Field_PROTIMER_IFS_WRAPCNTOF(self)
        self.zz_fdict['WRAPCNTOF'] = self.WRAPCNTOF
        self.TOUT0 = RM_Field_PROTIMER_IFS_TOUT0(self)
        self.zz_fdict['TOUT0'] = self.TOUT0
        self.TOUT1 = RM_Field_PROTIMER_IFS_TOUT1(self)
        self.zz_fdict['TOUT1'] = self.TOUT1
        self.TOUT0MATCH = RM_Field_PROTIMER_IFS_TOUT0MATCH(self)
        self.zz_fdict['TOUT0MATCH'] = self.TOUT0MATCH
        self.TOUT1MATCH = RM_Field_PROTIMER_IFS_TOUT1MATCH(self)
        self.zz_fdict['TOUT1MATCH'] = self.TOUT1MATCH
        self.CC0 = RM_Field_PROTIMER_IFS_CC0(self)
        self.zz_fdict['CC0'] = self.CC0
        self.CC1 = RM_Field_PROTIMER_IFS_CC1(self)
        self.zz_fdict['CC1'] = self.CC1
        self.CC2 = RM_Field_PROTIMER_IFS_CC2(self)
        self.zz_fdict['CC2'] = self.CC2
        self.CC3 = RM_Field_PROTIMER_IFS_CC3(self)
        self.zz_fdict['CC3'] = self.CC3
        self.CC4 = RM_Field_PROTIMER_IFS_CC4(self)
        self.zz_fdict['CC4'] = self.CC4
        self.COF0 = RM_Field_PROTIMER_IFS_COF0(self)
        self.zz_fdict['COF0'] = self.COF0
        self.COF1 = RM_Field_PROTIMER_IFS_COF1(self)
        self.zz_fdict['COF1'] = self.COF1
        self.COF2 = RM_Field_PROTIMER_IFS_COF2(self)
        self.zz_fdict['COF2'] = self.COF2
        self.COF3 = RM_Field_PROTIMER_IFS_COF3(self)
        self.zz_fdict['COF3'] = self.COF3
        self.COF4 = RM_Field_PROTIMER_IFS_COF4(self)
        self.zz_fdict['COF4'] = self.COF4
        self.LBTSUCCESS = RM_Field_PROTIMER_IFS_LBTSUCCESS(self)
        self.zz_fdict['LBTSUCCESS'] = self.LBTSUCCESS
        self.LBTRETRY = RM_Field_PROTIMER_IFS_LBTRETRY(self)
        self.zz_fdict['LBTRETRY'] = self.LBTRETRY
        self.LBTFAILURE = RM_Field_PROTIMER_IFS_LBTFAILURE(self)
        self.zz_fdict['LBTFAILURE'] = self.LBTFAILURE
        self.LBTPAUSED = RM_Field_PROTIMER_IFS_LBTPAUSED(self)
        self.zz_fdict['LBTPAUSED'] = self.LBTPAUSED
        self.RTCCSYNCHED = RM_Field_PROTIMER_IFS_RTCCSYNCHED(self)
        self.zz_fdict['RTCCSYNCHED'] = self.RTCCSYNCHED
        self.TOUT0MATCHLBT = RM_Field_PROTIMER_IFS_TOUT0MATCHLBT(self)
        self.zz_fdict['TOUT0MATCHLBT'] = self.TOUT0MATCHLBT
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_IFC, self).__init__(rmio, label,
            0x40085000, 0x064,
            'IFC', 'PROTIMER.IFC', 'write-only',
            "",
            0x00000000, 0x03F3FFF7)

        self.PRECNTOF = RM_Field_PROTIMER_IFC_PRECNTOF(self)
        self.zz_fdict['PRECNTOF'] = self.PRECNTOF
        self.BASECNTOF = RM_Field_PROTIMER_IFC_BASECNTOF(self)
        self.zz_fdict['BASECNTOF'] = self.BASECNTOF
        self.WRAPCNTOF = RM_Field_PROTIMER_IFC_WRAPCNTOF(self)
        self.zz_fdict['WRAPCNTOF'] = self.WRAPCNTOF
        self.TOUT0 = RM_Field_PROTIMER_IFC_TOUT0(self)
        self.zz_fdict['TOUT0'] = self.TOUT0
        self.TOUT1 = RM_Field_PROTIMER_IFC_TOUT1(self)
        self.zz_fdict['TOUT1'] = self.TOUT1
        self.TOUT0MATCH = RM_Field_PROTIMER_IFC_TOUT0MATCH(self)
        self.zz_fdict['TOUT0MATCH'] = self.TOUT0MATCH
        self.TOUT1MATCH = RM_Field_PROTIMER_IFC_TOUT1MATCH(self)
        self.zz_fdict['TOUT1MATCH'] = self.TOUT1MATCH
        self.CC0 = RM_Field_PROTIMER_IFC_CC0(self)
        self.zz_fdict['CC0'] = self.CC0
        self.CC1 = RM_Field_PROTIMER_IFC_CC1(self)
        self.zz_fdict['CC1'] = self.CC1
        self.CC2 = RM_Field_PROTIMER_IFC_CC2(self)
        self.zz_fdict['CC2'] = self.CC2
        self.CC3 = RM_Field_PROTIMER_IFC_CC3(self)
        self.zz_fdict['CC3'] = self.CC3
        self.CC4 = RM_Field_PROTIMER_IFC_CC4(self)
        self.zz_fdict['CC4'] = self.CC4
        self.COF0 = RM_Field_PROTIMER_IFC_COF0(self)
        self.zz_fdict['COF0'] = self.COF0
        self.COF1 = RM_Field_PROTIMER_IFC_COF1(self)
        self.zz_fdict['COF1'] = self.COF1
        self.COF2 = RM_Field_PROTIMER_IFC_COF2(self)
        self.zz_fdict['COF2'] = self.COF2
        self.COF3 = RM_Field_PROTIMER_IFC_COF3(self)
        self.zz_fdict['COF3'] = self.COF3
        self.COF4 = RM_Field_PROTIMER_IFC_COF4(self)
        self.zz_fdict['COF4'] = self.COF4
        self.LBTSUCCESS = RM_Field_PROTIMER_IFC_LBTSUCCESS(self)
        self.zz_fdict['LBTSUCCESS'] = self.LBTSUCCESS
        self.LBTRETRY = RM_Field_PROTIMER_IFC_LBTRETRY(self)
        self.zz_fdict['LBTRETRY'] = self.LBTRETRY
        self.LBTFAILURE = RM_Field_PROTIMER_IFC_LBTFAILURE(self)
        self.zz_fdict['LBTFAILURE'] = self.LBTFAILURE
        self.LBTPAUSED = RM_Field_PROTIMER_IFC_LBTPAUSED(self)
        self.zz_fdict['LBTPAUSED'] = self.LBTPAUSED
        self.RTCCSYNCHED = RM_Field_PROTIMER_IFC_RTCCSYNCHED(self)
        self.zz_fdict['RTCCSYNCHED'] = self.RTCCSYNCHED
        self.TOUT0MATCHLBT = RM_Field_PROTIMER_IFC_TOUT0MATCHLBT(self)
        self.zz_fdict['TOUT0MATCHLBT'] = self.TOUT0MATCHLBT
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_IEN, self).__init__(rmio, label,
            0x40085000, 0x068,
            'IEN', 'PROTIMER.IEN', 'read-write',
            "",
            0x00000000, 0x03F3FFF7)

        self.PRECNTOF = RM_Field_PROTIMER_IEN_PRECNTOF(self)
        self.zz_fdict['PRECNTOF'] = self.PRECNTOF
        self.BASECNTOF = RM_Field_PROTIMER_IEN_BASECNTOF(self)
        self.zz_fdict['BASECNTOF'] = self.BASECNTOF
        self.WRAPCNTOF = RM_Field_PROTIMER_IEN_WRAPCNTOF(self)
        self.zz_fdict['WRAPCNTOF'] = self.WRAPCNTOF
        self.TOUT0 = RM_Field_PROTIMER_IEN_TOUT0(self)
        self.zz_fdict['TOUT0'] = self.TOUT0
        self.TOUT1 = RM_Field_PROTIMER_IEN_TOUT1(self)
        self.zz_fdict['TOUT1'] = self.TOUT1
        self.TOUT0MATCH = RM_Field_PROTIMER_IEN_TOUT0MATCH(self)
        self.zz_fdict['TOUT0MATCH'] = self.TOUT0MATCH
        self.TOUT1MATCH = RM_Field_PROTIMER_IEN_TOUT1MATCH(self)
        self.zz_fdict['TOUT1MATCH'] = self.TOUT1MATCH
        self.CC0 = RM_Field_PROTIMER_IEN_CC0(self)
        self.zz_fdict['CC0'] = self.CC0
        self.CC1 = RM_Field_PROTIMER_IEN_CC1(self)
        self.zz_fdict['CC1'] = self.CC1
        self.CC2 = RM_Field_PROTIMER_IEN_CC2(self)
        self.zz_fdict['CC2'] = self.CC2
        self.CC3 = RM_Field_PROTIMER_IEN_CC3(self)
        self.zz_fdict['CC3'] = self.CC3
        self.CC4 = RM_Field_PROTIMER_IEN_CC4(self)
        self.zz_fdict['CC4'] = self.CC4
        self.COF0 = RM_Field_PROTIMER_IEN_COF0(self)
        self.zz_fdict['COF0'] = self.COF0
        self.COF1 = RM_Field_PROTIMER_IEN_COF1(self)
        self.zz_fdict['COF1'] = self.COF1
        self.COF2 = RM_Field_PROTIMER_IEN_COF2(self)
        self.zz_fdict['COF2'] = self.COF2
        self.COF3 = RM_Field_PROTIMER_IEN_COF3(self)
        self.zz_fdict['COF3'] = self.COF3
        self.COF4 = RM_Field_PROTIMER_IEN_COF4(self)
        self.zz_fdict['COF4'] = self.COF4
        self.LBTSUCCESS = RM_Field_PROTIMER_IEN_LBTSUCCESS(self)
        self.zz_fdict['LBTSUCCESS'] = self.LBTSUCCESS
        self.LBTRETRY = RM_Field_PROTIMER_IEN_LBTRETRY(self)
        self.zz_fdict['LBTRETRY'] = self.LBTRETRY
        self.LBTFAILURE = RM_Field_PROTIMER_IEN_LBTFAILURE(self)
        self.zz_fdict['LBTFAILURE'] = self.LBTFAILURE
        self.LBTPAUSED = RM_Field_PROTIMER_IEN_LBTPAUSED(self)
        self.zz_fdict['LBTPAUSED'] = self.LBTPAUSED
        self.RTCCSYNCHED = RM_Field_PROTIMER_IEN_RTCCSYNCHED(self)
        self.zz_fdict['RTCCSYNCHED'] = self.RTCCSYNCHED
        self.TOUT0MATCHLBT = RM_Field_PROTIMER_IEN_TOUT0MATCHLBT(self)
        self.zz_fdict['TOUT0MATCHLBT'] = self.TOUT0MATCHLBT
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_RXCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_RXCTRL, self).__init__(rmio, label,
            0x40085000, 0x06C,
            'RXCTRL', 'PROTIMER.RXCTRL', 'read-write',
            "",
            0x00000000, 0x1F1F1F1F)

        self.RXSETEVENT1 = RM_Field_PROTIMER_RXCTRL_RXSETEVENT1(self)
        self.zz_fdict['RXSETEVENT1'] = self.RXSETEVENT1
        self.RXSETEVENT2 = RM_Field_PROTIMER_RXCTRL_RXSETEVENT2(self)
        self.zz_fdict['RXSETEVENT2'] = self.RXSETEVENT2
        self.RXCLREVENT1 = RM_Field_PROTIMER_RXCTRL_RXCLREVENT1(self)
        self.zz_fdict['RXCLREVENT1'] = self.RXCLREVENT1
        self.RXCLREVENT2 = RM_Field_PROTIMER_RXCTRL_RXCLREVENT2(self)
        self.zz_fdict['RXCLREVENT2'] = self.RXCLREVENT2
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_TXCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_TXCTRL, self).__init__(rmio, label,
            0x40085000, 0x070,
            'TXCTRL', 'PROTIMER.TXCTRL', 'read-write',
            "",
            0x00000000, 0x00001F1F)

        self.TXSETEVENT1 = RM_Field_PROTIMER_TXCTRL_TXSETEVENT1(self)
        self.zz_fdict['TXSETEVENT1'] = self.TXSETEVENT1
        self.TXSETEVENT2 = RM_Field_PROTIMER_TXCTRL_TXSETEVENT2(self)
        self.zz_fdict['TXSETEVENT2'] = self.TXSETEVENT2
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_ETSI(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_ETSI, self).__init__(rmio, label,
            0x40085000, 0x074,
            'ETSI', 'PROTIMER.ETSI', 'read-write',
            "",
            0x00000000, 0x00000FFF)

        self.ETSIEN = RM_Field_PROTIMER_ETSI_ETSIEN(self)
        self.zz_fdict['ETSIEN'] = self.ETSIEN
        self.GRANULARLESSTHANRXWARM = RM_Field_PROTIMER_ETSI_GRANULARLESSTHANRXWARM(self)
        self.zz_fdict['GRANULARLESSTHANRXWARM'] = self.GRANULARLESSTHANRXWARM
        self.RXWARMTHLD = RM_Field_PROTIMER_ETSI_RXWARMTHLD(self)
        self.zz_fdict['RXWARMTHLD'] = self.RXWARMTHLD
        self.CCAFIXED = RM_Field_PROTIMER_ETSI_CCAFIXED(self)
        self.zz_fdict['CCAFIXED'] = self.CCAFIXED
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_LBTSTATE1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_LBTSTATE1, self).__init__(rmio, label,
            0x40085000, 0x078,
            'LBTSTATE1', 'PROTIMER.LBTSTATE1', 'read-write',
            "",
            0x00000000, 0x00000FFF)

        self.CCACNT = RM_Field_PROTIMER_LBTSTATE1_CCACNT(self)
        self.zz_fdict['CCACNT'] = self.CCACNT
        self.EXP = RM_Field_PROTIMER_LBTSTATE1_EXP(self)
        self.zz_fdict['EXP'] = self.EXP
        self.RETRYCNT = RM_Field_PROTIMER_LBTSTATE1_RETRYCNT(self)
        self.zz_fdict['RETRYCNT'] = self.RETRYCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_RANDOMFW0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_RANDOMFW0, self).__init__(rmio, label,
            0x40085000, 0x07C,
            'RANDOMFW0', 'PROTIMER.RANDOMFW0', 'read-write',
            "",
            0x00000000, 0x07FFFFFF)

        self.RANDOM0 = RM_Field_PROTIMER_RANDOMFW0_RANDOM0(self)
        self.zz_fdict['RANDOM0'] = self.RANDOM0
        self.RANDOM1 = RM_Field_PROTIMER_RANDOMFW0_RANDOM1(self)
        self.zz_fdict['RANDOM1'] = self.RANDOM1
        self.RANDOM2 = RM_Field_PROTIMER_RANDOMFW0_RANDOM2(self)
        self.zz_fdict['RANDOM2'] = self.RANDOM2
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_RANDOMFW1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_RANDOMFW1, self).__init__(rmio, label,
            0x40085000, 0x080,
            'RANDOMFW1', 'PROTIMER.RANDOMFW1', 'read-write',
            "",
            0x00000000, 0x07FFFFFF)

        self.RANDOM3 = RM_Field_PROTIMER_RANDOMFW1_RANDOM3(self)
        self.zz_fdict['RANDOM3'] = self.RANDOM3
        self.RANDOM4 = RM_Field_PROTIMER_RANDOMFW1_RANDOM4(self)
        self.zz_fdict['RANDOM4'] = self.RANDOM4
        self.RANDOM5 = RM_Field_PROTIMER_RANDOMFW1_RANDOM5(self)
        self.zz_fdict['RANDOM5'] = self.RANDOM5
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_RANDOMFW2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_RANDOMFW2, self).__init__(rmio, label,
            0x40085000, 0x084,
            'RANDOMFW2', 'PROTIMER.RANDOMFW2', 'read-write',
            "",
            0x00000000, 0x0003FFFF)

        self.RANDOM6 = RM_Field_PROTIMER_RANDOMFW2_RANDOM6(self)
        self.zz_fdict['RANDOM6'] = self.RANDOM6
        self.RANDOM7 = RM_Field_PROTIMER_RANDOMFW2_RANDOM7(self)
        self.zz_fdict['RANDOM7'] = self.RANDOM7
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC0_CTRL, self).__init__(rmio, label,
            0x40085000, 0x100,
            'CC0_CTRL', 'PROTIMER.CC0_CTRL', 'read-write',
            "",
            0x00000000, 0x03EF7F7F)

        self.ENABLE = RM_Field_PROTIMER_CC0_CTRL_ENABLE(self)
        self.zz_fdict['ENABLE'] = self.ENABLE
        self.CCMODE = RM_Field_PROTIMER_CC0_CTRL_CCMODE(self)
        self.zz_fdict['CCMODE'] = self.CCMODE
        self.PREMATCHEN = RM_Field_PROTIMER_CC0_CTRL_PREMATCHEN(self)
        self.zz_fdict['PREMATCHEN'] = self.PREMATCHEN
        self.BASEMATCHEN = RM_Field_PROTIMER_CC0_CTRL_BASEMATCHEN(self)
        self.zz_fdict['BASEMATCHEN'] = self.BASEMATCHEN
        self.WRAPMATCHEN = RM_Field_PROTIMER_CC0_CTRL_WRAPMATCHEN(self)
        self.zz_fdict['WRAPMATCHEN'] = self.WRAPMATCHEN
        self.OIST = RM_Field_PROTIMER_CC0_CTRL_OIST(self)
        self.zz_fdict['OIST'] = self.OIST
        self.OUTINV = RM_Field_PROTIMER_CC0_CTRL_OUTINV(self)
        self.zz_fdict['OUTINV'] = self.OUTINV
        self.MOA = RM_Field_PROTIMER_CC0_CTRL_MOA(self)
        self.zz_fdict['MOA'] = self.MOA
        self.OFOA = RM_Field_PROTIMER_CC0_CTRL_OFOA(self)
        self.zz_fdict['OFOA'] = self.OFOA
        self.OFSEL = RM_Field_PROTIMER_CC0_CTRL_OFSEL(self)
        self.zz_fdict['OFSEL'] = self.OFSEL
        self.PRSCONF = RM_Field_PROTIMER_CC0_CTRL_PRSCONF(self)
        self.zz_fdict['PRSCONF'] = self.PRSCONF
        self.PRSSEL = RM_Field_PROTIMER_CC0_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.INSEL = RM_Field_PROTIMER_CC0_CTRL_INSEL(self)
        self.zz_fdict['INSEL'] = self.INSEL
        self.ICEDGE = RM_Field_PROTIMER_CC0_CTRL_ICEDGE(self)
        self.zz_fdict['ICEDGE'] = self.ICEDGE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC0_PRE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC0_PRE, self).__init__(rmio, label,
            0x40085000, 0x104,
            'CC0_PRE', 'PROTIMER.CC0_PRE', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.PRE = RM_Field_PROTIMER_CC0_PRE_PRE(self)
        self.zz_fdict['PRE'] = self.PRE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC0_BASE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC0_BASE, self).__init__(rmio, label,
            0x40085000, 0x108,
            'CC0_BASE', 'PROTIMER.CC0_BASE', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.BASE = RM_Field_PROTIMER_CC0_BASE_BASE(self)
        self.zz_fdict['BASE'] = self.BASE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC0_WRAP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC0_WRAP, self).__init__(rmio, label,
            0x40085000, 0x10C,
            'CC0_WRAP', 'PROTIMER.CC0_WRAP', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.WRAP = RM_Field_PROTIMER_CC0_WRAP_WRAP(self)
        self.zz_fdict['WRAP'] = self.WRAP
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC1_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC1_CTRL, self).__init__(rmio, label,
            0x40085000, 0x110,
            'CC1_CTRL', 'PROTIMER.CC1_CTRL', 'read-write',
            "",
            0x00000000, 0x03EF7F7F)

        self.ENABLE = RM_Field_PROTIMER_CC1_CTRL_ENABLE(self)
        self.zz_fdict['ENABLE'] = self.ENABLE
        self.CCMODE = RM_Field_PROTIMER_CC1_CTRL_CCMODE(self)
        self.zz_fdict['CCMODE'] = self.CCMODE
        self.PREMATCHEN = RM_Field_PROTIMER_CC1_CTRL_PREMATCHEN(self)
        self.zz_fdict['PREMATCHEN'] = self.PREMATCHEN
        self.BASEMATCHEN = RM_Field_PROTIMER_CC1_CTRL_BASEMATCHEN(self)
        self.zz_fdict['BASEMATCHEN'] = self.BASEMATCHEN
        self.WRAPMATCHEN = RM_Field_PROTIMER_CC1_CTRL_WRAPMATCHEN(self)
        self.zz_fdict['WRAPMATCHEN'] = self.WRAPMATCHEN
        self.OIST = RM_Field_PROTIMER_CC1_CTRL_OIST(self)
        self.zz_fdict['OIST'] = self.OIST
        self.OUTINV = RM_Field_PROTIMER_CC1_CTRL_OUTINV(self)
        self.zz_fdict['OUTINV'] = self.OUTINV
        self.MOA = RM_Field_PROTIMER_CC1_CTRL_MOA(self)
        self.zz_fdict['MOA'] = self.MOA
        self.OFOA = RM_Field_PROTIMER_CC1_CTRL_OFOA(self)
        self.zz_fdict['OFOA'] = self.OFOA
        self.OFSEL = RM_Field_PROTIMER_CC1_CTRL_OFSEL(self)
        self.zz_fdict['OFSEL'] = self.OFSEL
        self.PRSCONF = RM_Field_PROTIMER_CC1_CTRL_PRSCONF(self)
        self.zz_fdict['PRSCONF'] = self.PRSCONF
        self.PRSSEL = RM_Field_PROTIMER_CC1_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.INSEL = RM_Field_PROTIMER_CC1_CTRL_INSEL(self)
        self.zz_fdict['INSEL'] = self.INSEL
        self.ICEDGE = RM_Field_PROTIMER_CC1_CTRL_ICEDGE(self)
        self.zz_fdict['ICEDGE'] = self.ICEDGE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC1_PRE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC1_PRE, self).__init__(rmio, label,
            0x40085000, 0x114,
            'CC1_PRE', 'PROTIMER.CC1_PRE', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.PRE = RM_Field_PROTIMER_CC1_PRE_PRE(self)
        self.zz_fdict['PRE'] = self.PRE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC1_BASE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC1_BASE, self).__init__(rmio, label,
            0x40085000, 0x118,
            'CC1_BASE', 'PROTIMER.CC1_BASE', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.BASE = RM_Field_PROTIMER_CC1_BASE_BASE(self)
        self.zz_fdict['BASE'] = self.BASE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC1_WRAP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC1_WRAP, self).__init__(rmio, label,
            0x40085000, 0x11C,
            'CC1_WRAP', 'PROTIMER.CC1_WRAP', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.WRAP = RM_Field_PROTIMER_CC1_WRAP_WRAP(self)
        self.zz_fdict['WRAP'] = self.WRAP
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC2_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC2_CTRL, self).__init__(rmio, label,
            0x40085000, 0x120,
            'CC2_CTRL', 'PROTIMER.CC2_CTRL', 'read-write',
            "",
            0x00000000, 0x03EF7F7F)

        self.ENABLE = RM_Field_PROTIMER_CC2_CTRL_ENABLE(self)
        self.zz_fdict['ENABLE'] = self.ENABLE
        self.CCMODE = RM_Field_PROTIMER_CC2_CTRL_CCMODE(self)
        self.zz_fdict['CCMODE'] = self.CCMODE
        self.PREMATCHEN = RM_Field_PROTIMER_CC2_CTRL_PREMATCHEN(self)
        self.zz_fdict['PREMATCHEN'] = self.PREMATCHEN
        self.BASEMATCHEN = RM_Field_PROTIMER_CC2_CTRL_BASEMATCHEN(self)
        self.zz_fdict['BASEMATCHEN'] = self.BASEMATCHEN
        self.WRAPMATCHEN = RM_Field_PROTIMER_CC2_CTRL_WRAPMATCHEN(self)
        self.zz_fdict['WRAPMATCHEN'] = self.WRAPMATCHEN
        self.OIST = RM_Field_PROTIMER_CC2_CTRL_OIST(self)
        self.zz_fdict['OIST'] = self.OIST
        self.OUTINV = RM_Field_PROTIMER_CC2_CTRL_OUTINV(self)
        self.zz_fdict['OUTINV'] = self.OUTINV
        self.MOA = RM_Field_PROTIMER_CC2_CTRL_MOA(self)
        self.zz_fdict['MOA'] = self.MOA
        self.OFOA = RM_Field_PROTIMER_CC2_CTRL_OFOA(self)
        self.zz_fdict['OFOA'] = self.OFOA
        self.OFSEL = RM_Field_PROTIMER_CC2_CTRL_OFSEL(self)
        self.zz_fdict['OFSEL'] = self.OFSEL
        self.PRSCONF = RM_Field_PROTIMER_CC2_CTRL_PRSCONF(self)
        self.zz_fdict['PRSCONF'] = self.PRSCONF
        self.PRSSEL = RM_Field_PROTIMER_CC2_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.INSEL = RM_Field_PROTIMER_CC2_CTRL_INSEL(self)
        self.zz_fdict['INSEL'] = self.INSEL
        self.ICEDGE = RM_Field_PROTIMER_CC2_CTRL_ICEDGE(self)
        self.zz_fdict['ICEDGE'] = self.ICEDGE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC2_PRE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC2_PRE, self).__init__(rmio, label,
            0x40085000, 0x124,
            'CC2_PRE', 'PROTIMER.CC2_PRE', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.PRE = RM_Field_PROTIMER_CC2_PRE_PRE(self)
        self.zz_fdict['PRE'] = self.PRE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC2_BASE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC2_BASE, self).__init__(rmio, label,
            0x40085000, 0x128,
            'CC2_BASE', 'PROTIMER.CC2_BASE', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.BASE = RM_Field_PROTIMER_CC2_BASE_BASE(self)
        self.zz_fdict['BASE'] = self.BASE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC2_WRAP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC2_WRAP, self).__init__(rmio, label,
            0x40085000, 0x12C,
            'CC2_WRAP', 'PROTIMER.CC2_WRAP', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.WRAP = RM_Field_PROTIMER_CC2_WRAP_WRAP(self)
        self.zz_fdict['WRAP'] = self.WRAP
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC3_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC3_CTRL, self).__init__(rmio, label,
            0x40085000, 0x130,
            'CC3_CTRL', 'PROTIMER.CC3_CTRL', 'read-write',
            "",
            0x00000000, 0x03EF7F7F)

        self.ENABLE = RM_Field_PROTIMER_CC3_CTRL_ENABLE(self)
        self.zz_fdict['ENABLE'] = self.ENABLE
        self.CCMODE = RM_Field_PROTIMER_CC3_CTRL_CCMODE(self)
        self.zz_fdict['CCMODE'] = self.CCMODE
        self.PREMATCHEN = RM_Field_PROTIMER_CC3_CTRL_PREMATCHEN(self)
        self.zz_fdict['PREMATCHEN'] = self.PREMATCHEN
        self.BASEMATCHEN = RM_Field_PROTIMER_CC3_CTRL_BASEMATCHEN(self)
        self.zz_fdict['BASEMATCHEN'] = self.BASEMATCHEN
        self.WRAPMATCHEN = RM_Field_PROTIMER_CC3_CTRL_WRAPMATCHEN(self)
        self.zz_fdict['WRAPMATCHEN'] = self.WRAPMATCHEN
        self.OIST = RM_Field_PROTIMER_CC3_CTRL_OIST(self)
        self.zz_fdict['OIST'] = self.OIST
        self.OUTINV = RM_Field_PROTIMER_CC3_CTRL_OUTINV(self)
        self.zz_fdict['OUTINV'] = self.OUTINV
        self.MOA = RM_Field_PROTIMER_CC3_CTRL_MOA(self)
        self.zz_fdict['MOA'] = self.MOA
        self.OFOA = RM_Field_PROTIMER_CC3_CTRL_OFOA(self)
        self.zz_fdict['OFOA'] = self.OFOA
        self.OFSEL = RM_Field_PROTIMER_CC3_CTRL_OFSEL(self)
        self.zz_fdict['OFSEL'] = self.OFSEL
        self.PRSCONF = RM_Field_PROTIMER_CC3_CTRL_PRSCONF(self)
        self.zz_fdict['PRSCONF'] = self.PRSCONF
        self.PRSSEL = RM_Field_PROTIMER_CC3_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.INSEL = RM_Field_PROTIMER_CC3_CTRL_INSEL(self)
        self.zz_fdict['INSEL'] = self.INSEL
        self.ICEDGE = RM_Field_PROTIMER_CC3_CTRL_ICEDGE(self)
        self.zz_fdict['ICEDGE'] = self.ICEDGE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC3_PRE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC3_PRE, self).__init__(rmio, label,
            0x40085000, 0x134,
            'CC3_PRE', 'PROTIMER.CC3_PRE', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.PRE = RM_Field_PROTIMER_CC3_PRE_PRE(self)
        self.zz_fdict['PRE'] = self.PRE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC3_BASE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC3_BASE, self).__init__(rmio, label,
            0x40085000, 0x138,
            'CC3_BASE', 'PROTIMER.CC3_BASE', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.BASE = RM_Field_PROTIMER_CC3_BASE_BASE(self)
        self.zz_fdict['BASE'] = self.BASE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC3_WRAP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC3_WRAP, self).__init__(rmio, label,
            0x40085000, 0x13C,
            'CC3_WRAP', 'PROTIMER.CC3_WRAP', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.WRAP = RM_Field_PROTIMER_CC3_WRAP_WRAP(self)
        self.zz_fdict['WRAP'] = self.WRAP
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC4_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC4_CTRL, self).__init__(rmio, label,
            0x40085000, 0x140,
            'CC4_CTRL', 'PROTIMER.CC4_CTRL', 'read-write',
            "",
            0x00000000, 0x03EF7F7F)

        self.ENABLE = RM_Field_PROTIMER_CC4_CTRL_ENABLE(self)
        self.zz_fdict['ENABLE'] = self.ENABLE
        self.CCMODE = RM_Field_PROTIMER_CC4_CTRL_CCMODE(self)
        self.zz_fdict['CCMODE'] = self.CCMODE
        self.PREMATCHEN = RM_Field_PROTIMER_CC4_CTRL_PREMATCHEN(self)
        self.zz_fdict['PREMATCHEN'] = self.PREMATCHEN
        self.BASEMATCHEN = RM_Field_PROTIMER_CC4_CTRL_BASEMATCHEN(self)
        self.zz_fdict['BASEMATCHEN'] = self.BASEMATCHEN
        self.WRAPMATCHEN = RM_Field_PROTIMER_CC4_CTRL_WRAPMATCHEN(self)
        self.zz_fdict['WRAPMATCHEN'] = self.WRAPMATCHEN
        self.OIST = RM_Field_PROTIMER_CC4_CTRL_OIST(self)
        self.zz_fdict['OIST'] = self.OIST
        self.OUTINV = RM_Field_PROTIMER_CC4_CTRL_OUTINV(self)
        self.zz_fdict['OUTINV'] = self.OUTINV
        self.MOA = RM_Field_PROTIMER_CC4_CTRL_MOA(self)
        self.zz_fdict['MOA'] = self.MOA
        self.OFOA = RM_Field_PROTIMER_CC4_CTRL_OFOA(self)
        self.zz_fdict['OFOA'] = self.OFOA
        self.OFSEL = RM_Field_PROTIMER_CC4_CTRL_OFSEL(self)
        self.zz_fdict['OFSEL'] = self.OFSEL
        self.PRSCONF = RM_Field_PROTIMER_CC4_CTRL_PRSCONF(self)
        self.zz_fdict['PRSCONF'] = self.PRSCONF
        self.PRSSEL = RM_Field_PROTIMER_CC4_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.INSEL = RM_Field_PROTIMER_CC4_CTRL_INSEL(self)
        self.zz_fdict['INSEL'] = self.INSEL
        self.ICEDGE = RM_Field_PROTIMER_CC4_CTRL_ICEDGE(self)
        self.zz_fdict['ICEDGE'] = self.ICEDGE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC4_PRE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC4_PRE, self).__init__(rmio, label,
            0x40085000, 0x144,
            'CC4_PRE', 'PROTIMER.CC4_PRE', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.PRE = RM_Field_PROTIMER_CC4_PRE_PRE(self)
        self.zz_fdict['PRE'] = self.PRE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC4_BASE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC4_BASE, self).__init__(rmio, label,
            0x40085000, 0x148,
            'CC4_BASE', 'PROTIMER.CC4_BASE', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.BASE = RM_Field_PROTIMER_CC4_BASE_BASE(self)
        self.zz_fdict['BASE'] = self.BASE
        self.__dict__['zz_frozen'] = True


class RM_Register_PROTIMER_CC4_WRAP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PROTIMER_CC4_WRAP, self).__init__(rmio, label,
            0x40085000, 0x14C,
            'CC4_WRAP', 'PROTIMER.CC4_WRAP', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.WRAP = RM_Field_PROTIMER_CC4_WRAP_WRAP(self)
        self.zz_fdict['WRAP'] = self.WRAP
        self.__dict__['zz_frozen'] = True


