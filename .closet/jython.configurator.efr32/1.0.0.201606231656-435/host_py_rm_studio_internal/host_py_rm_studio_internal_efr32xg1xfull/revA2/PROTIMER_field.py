
from static import Base_RM_Field
from PROTIMER_enum import *


class RM_Field_PROTIMER_CTRL_DEBUGRUN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CTRL_DEBUGRUN, self).__init__(register,
            'DEBUGRUN', 'PROTIMER.CTRL.DEBUGRUN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CTRL_DMACLRACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CTRL_DMACLRACT, self).__init__(register,
            'DMACLRACT', 'PROTIMER.CTRL.DMACLRACT', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CTRL_OSMEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CTRL_OSMEN, self).__init__(register,
            'OSMEN', 'PROTIMER.CTRL.OSMEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CTRL_ZEROSTARTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CTRL_ZEROSTARTEN, self).__init__(register,
            'ZEROSTARTEN', 'PROTIMER.CTRL.ZEROSTARTEN', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CTRL_PRECNTSRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CTRL_PRECNTSRC, self).__init__(register,
            'PRECNTSRC', 'PROTIMER.CTRL.PRECNTSRC', 'read-write',
            "",
            8, 2,
            RM_Enum_PROTIMER_CTRL_PRECNTSRC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CTRL_BASECNTSRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CTRL_BASECNTSRC, self).__init__(register,
            'BASECNTSRC', 'PROTIMER.CTRL.BASECNTSRC', 'read-write',
            "",
            12, 2,
            RM_Enum_PROTIMER_CTRL_BASECNTSRC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CTRL_WRAPCNTSRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CTRL_WRAPCNTSRC, self).__init__(register,
            'WRAPCNTSRC', 'PROTIMER.CTRL.WRAPCNTSRC', 'read-write',
            "",
            16, 2,
            RM_Enum_PROTIMER_CTRL_WRAPCNTSRC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CTRL_TOUT0SRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CTRL_TOUT0SRC, self).__init__(register,
            'TOUT0SRC', 'PROTIMER.CTRL.TOUT0SRC', 'read-write',
            "",
            20, 2,
            RM_Enum_PROTIMER_CTRL_TOUT0SRC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CTRL_TOUT0SYNCSRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CTRL_TOUT0SYNCSRC, self).__init__(register,
            'TOUT0SYNCSRC', 'PROTIMER.CTRL.TOUT0SYNCSRC', 'read-write',
            "",
            22, 2,
            RM_Enum_PROTIMER_CTRL_TOUT0SYNCSRC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CTRL_TOUT1SRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CTRL_TOUT1SRC, self).__init__(register,
            'TOUT1SRC', 'PROTIMER.CTRL.TOUT1SRC', 'read-write',
            "",
            24, 2,
            RM_Enum_PROTIMER_CTRL_TOUT1SRC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CTRL_TOUT1SYNCSRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CTRL_TOUT1SYNCSRC, self).__init__(register,
            'TOUT1SYNCSRC', 'PROTIMER.CTRL.TOUT1SYNCSRC', 'read-write',
            "",
            26, 2,
            RM_Enum_PROTIMER_CTRL_TOUT1SYNCSRC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CTRL_TOUT0MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CTRL_TOUT0MODE, self).__init__(register,
            'TOUT0MODE', 'PROTIMER.CTRL.TOUT0MODE', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CTRL_TOUT1MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CTRL_TOUT1MODE, self).__init__(register,
            'TOUT1MODE', 'PROTIMER.CTRL.TOUT1MODE', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CMD_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CMD_START, self).__init__(register,
            'START', 'PROTIMER.CMD.START', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CMD_RTCSYNCSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CMD_RTCSYNCSTART, self).__init__(register,
            'RTCSYNCSTART', 'PROTIMER.CMD.RTCSYNCSTART', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CMD_STOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CMD_STOP, self).__init__(register,
            'STOP', 'PROTIMER.CMD.STOP', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CMD_TOUT0START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CMD_TOUT0START, self).__init__(register,
            'TOUT0START', 'PROTIMER.CMD.TOUT0START', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CMD_TOUT0STOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CMD_TOUT0STOP, self).__init__(register,
            'TOUT0STOP', 'PROTIMER.CMD.TOUT0STOP', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CMD_TOUT1START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CMD_TOUT1START, self).__init__(register,
            'TOUT1START', 'PROTIMER.CMD.TOUT1START', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CMD_TOUT1STOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CMD_TOUT1STOP, self).__init__(register,
            'TOUT1STOP', 'PROTIMER.CMD.TOUT1STOP', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CMD_LBTSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CMD_LBTSTART, self).__init__(register,
            'LBTSTART', 'PROTIMER.CMD.LBTSTART', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CMD_LBTPAUSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CMD_LBTPAUSE, self).__init__(register,
            'LBTPAUSE', 'PROTIMER.CMD.LBTPAUSE', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CMD_LBTSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CMD_LBTSTOP, self).__init__(register,
            'LBTSTOP', 'PROTIMER.CMD.LBTSTOP', 'write-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_PRSCTRL_STARTPRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_PRSCTRL_STARTPRSEN, self).__init__(register,
            'STARTPRSEN', 'PROTIMER.PRSCTRL.STARTPRSEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_PRSCTRL_STARTEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_PRSCTRL_STARTEDGE, self).__init__(register,
            'STARTEDGE', 'PROTIMER.PRSCTRL.STARTEDGE', 'read-write',
            "",
            2, 2,
            RM_Enum_PROTIMER_PRSCTRL_STARTEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_PRSCTRL_STARTPRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_PRSCTRL_STARTPRSSEL, self).__init__(register,
            'STARTPRSSEL', 'PROTIMER.PRSCTRL.STARTPRSSEL', 'read-write',
            "",
            4, 4,
            RM_Enum_PROTIMER_PRSCTRL_STARTPRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_PRSCTRL_STOPPRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_PRSCTRL_STOPPRSEN, self).__init__(register,
            'STOPPRSEN', 'PROTIMER.PRSCTRL.STOPPRSEN', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_PRSCTRL_STOPEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_PRSCTRL_STOPEDGE, self).__init__(register,
            'STOPEDGE', 'PROTIMER.PRSCTRL.STOPEDGE', 'read-write',
            "",
            10, 2,
            RM_Enum_PROTIMER_PRSCTRL_STOPEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_PRSCTRL_STOPPRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_PRSCTRL_STOPPRSSEL, self).__init__(register,
            'STOPPRSSEL', 'PROTIMER.PRSCTRL.STOPPRSSEL', 'read-write',
            "",
            12, 4,
            RM_Enum_PROTIMER_PRSCTRL_STOPPRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_PRSCTRL_RTCCTRIGGERPRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_PRSCTRL_RTCCTRIGGERPRSEN, self).__init__(register,
            'RTCCTRIGGERPRSEN', 'PROTIMER.PRSCTRL.RTCCTRIGGERPRSEN', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_PRSCTRL_RTCCTRIGGEREDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_PRSCTRL_RTCCTRIGGEREDGE, self).__init__(register,
            'RTCCTRIGGEREDGE', 'PROTIMER.PRSCTRL.RTCCTRIGGEREDGE', 'read-write',
            "",
            18, 2,
            RM_Enum_PROTIMER_PRSCTRL_RTCCTRIGGEREDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_PRSCTRL_RTCCTRIGGERPRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_PRSCTRL_RTCCTRIGGERPRSSEL, self).__init__(register,
            'RTCCTRIGGERPRSSEL', 'PROTIMER.PRSCTRL.RTCCTRIGGERPRSSEL', 'read-write',
            "",
            20, 4,
            RM_Enum_PROTIMER_PRSCTRL_RTCCTRIGGERPRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_STATUS_RUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_STATUS_RUNNING, self).__init__(register,
            'RUNNING', 'PROTIMER.STATUS.RUNNING', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_STATUS_LBTSYNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_STATUS_LBTSYNC, self).__init__(register,
            'LBTSYNC', 'PROTIMER.STATUS.LBTSYNC', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_STATUS_LBTRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_STATUS_LBTRUNNING, self).__init__(register,
            'LBTRUNNING', 'PROTIMER.STATUS.LBTRUNNING', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_STATUS_LBTPAUSED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_STATUS_LBTPAUSED, self).__init__(register,
            'LBTPAUSED', 'PROTIMER.STATUS.LBTPAUSED', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_STATUS_TOUT0RUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_STATUS_TOUT0RUNNING, self).__init__(register,
            'TOUT0RUNNING', 'PROTIMER.STATUS.TOUT0RUNNING', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_STATUS_TOUT0SYNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_STATUS_TOUT0SYNC, self).__init__(register,
            'TOUT0SYNC', 'PROTIMER.STATUS.TOUT0SYNC', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_STATUS_TOUT1RUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_STATUS_TOUT1RUNNING, self).__init__(register,
            'TOUT1RUNNING', 'PROTIMER.STATUS.TOUT1RUNNING', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_STATUS_TOUT1SYNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_STATUS_TOUT1SYNC, self).__init__(register,
            'TOUT1SYNC', 'PROTIMER.STATUS.TOUT1SYNC', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_STATUS_ICV0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_STATUS_ICV0, self).__init__(register,
            'ICV0', 'PROTIMER.STATUS.ICV0', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_STATUS_ICV1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_STATUS_ICV1, self).__init__(register,
            'ICV1', 'PROTIMER.STATUS.ICV1', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_STATUS_ICV2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_STATUS_ICV2, self).__init__(register,
            'ICV2', 'PROTIMER.STATUS.ICV2', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_STATUS_ICV3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_STATUS_ICV3, self).__init__(register,
            'ICV3', 'PROTIMER.STATUS.ICV3', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_STATUS_ICV4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_STATUS_ICV4, self).__init__(register,
            'ICV4', 'PROTIMER.STATUS.ICV4', 'read-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_PRECNT_PRECNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_PRECNT_PRECNT, self).__init__(register,
            'PRECNT', 'PROTIMER.PRECNT.PRECNT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_BASECNT_BASECNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_BASECNT_BASECNT, self).__init__(register,
            'BASECNT', 'PROTIMER.BASECNT.BASECNT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_WRAPCNT_WRAPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_WRAPCNT_WRAPCNT, self).__init__(register,
            'WRAPCNT', 'PROTIMER.WRAPCNT.WRAPCNT', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_BASEPRE_PRECNTV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_BASEPRE_PRECNTV, self).__init__(register,
            'PRECNTV', 'PROTIMER.BASEPRE.PRECNTV', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_BASEPRE_BASECNTV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_BASEPRE_BASECNTV, self).__init__(register,
            'BASECNTV', 'PROTIMER.BASEPRE.BASECNTV', 'read-only',
            "",
            16, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LWRAPCNT_LWRAPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LWRAPCNT_LWRAPCNT, self).__init__(register,
            'LWRAPCNT', 'PROTIMER.LWRAPCNT.LWRAPCNT', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_PRECNTTOPADJ_PRECNTTOPADJ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_PRECNTTOPADJ_PRECNTTOPADJ, self).__init__(register,
            'PRECNTTOPADJ', 'PROTIMER.PRECNTTOPADJ.PRECNTTOPADJ', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_PRECNTTOP_PRECNTTOPFRAC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_PRECNTTOP_PRECNTTOPFRAC, self).__init__(register,
            'PRECNTTOPFRAC', 'PROTIMER.PRECNTTOP.PRECNTTOPFRAC', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_PRECNTTOP_PRECNTTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_PRECNTTOP_PRECNTTOP, self).__init__(register,
            'PRECNTTOP', 'PROTIMER.PRECNTTOP.PRECNTTOP', 'read-write',
            "",
            8, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_BASECNTTOP_BASECNTTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_BASECNTTOP_BASECNTTOP, self).__init__(register,
            'BASECNTTOP', 'PROTIMER.BASECNTTOP.BASECNTTOP', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_WRAPCNTTOP_WRAPCNTTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_WRAPCNTTOP_WRAPCNTTOP, self).__init__(register,
            'WRAPCNTTOP', 'PROTIMER.WRAPCNTTOP.WRAPCNTTOP', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_TOUT0CNT_TOUT0PCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_TOUT0CNT_TOUT0PCNT, self).__init__(register,
            'TOUT0PCNT', 'PROTIMER.TOUT0CNT.TOUT0PCNT', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_TOUT0CNT_TOUT0CNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_TOUT0CNT_TOUT0CNT, self).__init__(register,
            'TOUT0CNT', 'PROTIMER.TOUT0CNT.TOUT0CNT', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_TOUT0CNTTOP_TOUT0PCNTTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_TOUT0CNTTOP_TOUT0PCNTTOP, self).__init__(register,
            'TOUT0PCNTTOP', 'PROTIMER.TOUT0CNTTOP.TOUT0PCNTTOP', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_TOUT0CNTTOP_TOUT0CNTTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_TOUT0CNTTOP_TOUT0CNTTOP, self).__init__(register,
            'TOUT0CNTTOP', 'PROTIMER.TOUT0CNTTOP.TOUT0CNTTOP', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_TOUT0COMP_TOUT0PCNTCOMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_TOUT0COMP_TOUT0PCNTCOMP, self).__init__(register,
            'TOUT0PCNTCOMP', 'PROTIMER.TOUT0COMP.TOUT0PCNTCOMP', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_TOUT0COMP_TOUT0CNTCOMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_TOUT0COMP_TOUT0CNTCOMP, self).__init__(register,
            'TOUT0CNTCOMP', 'PROTIMER.TOUT0COMP.TOUT0CNTCOMP', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_TOUT1CNT_TOUT1PCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_TOUT1CNT_TOUT1PCNT, self).__init__(register,
            'TOUT1PCNT', 'PROTIMER.TOUT1CNT.TOUT1PCNT', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_TOUT1CNT_TOUT1CNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_TOUT1CNT_TOUT1CNT, self).__init__(register,
            'TOUT1CNT', 'PROTIMER.TOUT1CNT.TOUT1CNT', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_TOUT1CNTTOP_TOUT1PCNTTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_TOUT1CNTTOP_TOUT1PCNTTOP, self).__init__(register,
            'TOUT1PCNTTOP', 'PROTIMER.TOUT1CNTTOP.TOUT1PCNTTOP', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_TOUT1CNTTOP_TOUT1CNTTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_TOUT1CNTTOP_TOUT1CNTTOP, self).__init__(register,
            'TOUT1CNTTOP', 'PROTIMER.TOUT1CNTTOP.TOUT1CNTTOP', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_TOUT1COMP_TOUT1PCNTCOMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_TOUT1COMP_TOUT1PCNTCOMP, self).__init__(register,
            'TOUT1PCNTCOMP', 'PROTIMER.TOUT1COMP.TOUT1PCNTCOMP', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_TOUT1COMP_TOUT1CNTCOMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_TOUT1COMP_TOUT1CNTCOMP, self).__init__(register,
            'TOUT1CNTCOMP', 'PROTIMER.TOUT1COMP.TOUT1CNTCOMP', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTCTRL_STARTEXP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTCTRL_STARTEXP, self).__init__(register,
            'STARTEXP', 'PROTIMER.LBTCTRL.STARTEXP', 'read-write',
            "",
            0, 4,
            RM_Enum_PROTIMER_LBTCTRL_STARTEXP(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTCTRL_MAXEXP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTCTRL_MAXEXP, self).__init__(register,
            'MAXEXP', 'PROTIMER.LBTCTRL.MAXEXP', 'read-write',
            "",
            4, 4,
            RM_Enum_PROTIMER_LBTCTRL_MAXEXP(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTCTRL_CCADELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTCTRL_CCADELAY, self).__init__(register,
            'CCADELAY', 'PROTIMER.LBTCTRL.CCADELAY', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTCTRL_CCAREPEAT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTCTRL_CCAREPEAT, self).__init__(register,
            'CCAREPEAT', 'PROTIMER.LBTCTRL.CCAREPEAT', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTCTRL_FIXEDBACKOFF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTCTRL_FIXEDBACKOFF, self).__init__(register,
            'FIXEDBACKOFF', 'PROTIMER.LBTCTRL.FIXEDBACKOFF', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTCTRL_RETRYLIMIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTCTRL_RETRYLIMIT, self).__init__(register,
            'RETRYLIMIT', 'PROTIMER.LBTCTRL.RETRYLIMIT', 'read-write',
            "",
            24, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTPRSCTRL_LBTSTARTPRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTPRSCTRL_LBTSTARTPRSEN, self).__init__(register,
            'LBTSTARTPRSEN', 'PROTIMER.LBTPRSCTRL.LBTSTARTPRSEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTPRSCTRL_LBTSTARTPRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTPRSCTRL_LBTSTARTPRSSEL, self).__init__(register,
            'LBTSTARTPRSSEL', 'PROTIMER.LBTPRSCTRL.LBTSTARTPRSSEL', 'read-write',
            "",
            9, 4,
            RM_Enum_PROTIMER_LBTPRSCTRL_LBTSTARTPRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTPRSCTRL_LBTPAUSEPRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTPRSCTRL_LBTPAUSEPRSEN, self).__init__(register,
            'LBTPAUSEPRSEN', 'PROTIMER.LBTPRSCTRL.LBTPAUSEPRSEN', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTPRSCTRL_LBTPAUSEPRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTPRSCTRL_LBTPAUSEPRSSEL, self).__init__(register,
            'LBTPAUSEPRSSEL', 'PROTIMER.LBTPRSCTRL.LBTPAUSEPRSSEL', 'read-write',
            "",
            17, 4,
            RM_Enum_PROTIMER_LBTPRSCTRL_LBTPAUSEPRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTPRSCTRL_LBTSTOPPRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTPRSCTRL_LBTSTOPPRSEN, self).__init__(register,
            'LBTSTOPPRSEN', 'PROTIMER.LBTPRSCTRL.LBTSTOPPRSEN', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTPRSCTRL_LBTSTOPPRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTPRSCTRL_LBTSTOPPRSSEL, self).__init__(register,
            'LBTSTOPPRSSEL', 'PROTIMER.LBTPRSCTRL.LBTSTOPPRSSEL', 'read-write',
            "",
            25, 4,
            RM_Enum_PROTIMER_LBTPRSCTRL_LBTSTOPPRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTSTATE_TOUT0PCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTSTATE_TOUT0PCNT, self).__init__(register,
            'TOUT0PCNT', 'PROTIMER.LBTSTATE.TOUT0PCNT', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTSTATE_TOUT0CNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTSTATE_TOUT0CNT, self).__init__(register,
            'TOUT0CNT', 'PROTIMER.LBTSTATE.TOUT0CNT', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTSTATE_CCACNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTSTATE_CCACNT, self).__init__(register,
            'CCACNT', 'PROTIMER.LBTSTATE.CCACNT', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTSTATE_EXP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTSTATE_EXP, self).__init__(register,
            'EXP', 'PROTIMER.LBTSTATE.EXP', 'read-write',
            "",
            20, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_LBTSTATE_RETRYCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_LBTSTATE_RETRYCNT, self).__init__(register,
            'RETRYCNT', 'PROTIMER.LBTSTATE.RETRYCNT', 'read-write',
            "",
            24, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_RANDOM_RANDOM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_RANDOM_RANDOM, self).__init__(register,
            'RANDOM', 'PROTIMER.RANDOM.RANDOM', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_PRECNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_PRECNTOF, self).__init__(register,
            'PRECNTOF', 'PROTIMER.IF.PRECNTOF', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_BASECNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_BASECNTOF, self).__init__(register,
            'BASECNTOF', 'PROTIMER.IF.BASECNTOF', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_WRAPCNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_WRAPCNTOF, self).__init__(register,
            'WRAPCNTOF', 'PROTIMER.IF.WRAPCNTOF', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_TOUT0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_TOUT0, self).__init__(register,
            'TOUT0', 'PROTIMER.IF.TOUT0', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_TOUT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_TOUT1, self).__init__(register,
            'TOUT1', 'PROTIMER.IF.TOUT1', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_TOUT0MATCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_TOUT0MATCH, self).__init__(register,
            'TOUT0MATCH', 'PROTIMER.IF.TOUT0MATCH', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_TOUT1MATCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_TOUT1MATCH, self).__init__(register,
            'TOUT1MATCH', 'PROTIMER.IF.TOUT1MATCH', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_CC0, self).__init__(register,
            'CC0', 'PROTIMER.IF.CC0', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_CC1, self).__init__(register,
            'CC1', 'PROTIMER.IF.CC1', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_CC2, self).__init__(register,
            'CC2', 'PROTIMER.IF.CC2', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_CC3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_CC3, self).__init__(register,
            'CC3', 'PROTIMER.IF.CC3', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_CC4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_CC4, self).__init__(register,
            'CC4', 'PROTIMER.IF.CC4', 'read-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_COF0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_COF0, self).__init__(register,
            'COF0', 'PROTIMER.IF.COF0', 'read-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_COF1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_COF1, self).__init__(register,
            'COF1', 'PROTIMER.IF.COF1', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_COF2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_COF2, self).__init__(register,
            'COF2', 'PROTIMER.IF.COF2', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_COF3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_COF3, self).__init__(register,
            'COF3', 'PROTIMER.IF.COF3', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_COF4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_COF4, self).__init__(register,
            'COF4', 'PROTIMER.IF.COF4', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_LBTSUCCESS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_LBTSUCCESS, self).__init__(register,
            'LBTSUCCESS', 'PROTIMER.IF.LBTSUCCESS', 'read-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_LBTRETRY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_LBTRETRY, self).__init__(register,
            'LBTRETRY', 'PROTIMER.IF.LBTRETRY', 'read-only',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_LBTFAILURE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_LBTFAILURE, self).__init__(register,
            'LBTFAILURE', 'PROTIMER.IF.LBTFAILURE', 'read-only',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_LBTPAUSED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_LBTPAUSED, self).__init__(register,
            'LBTPAUSED', 'PROTIMER.IF.LBTPAUSED', 'read-only',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_RTCCSYNCHED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_RTCCSYNCHED, self).__init__(register,
            'RTCCSYNCHED', 'PROTIMER.IF.RTCCSYNCHED', 'read-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IF_TOUT0MATCHLBT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IF_TOUT0MATCHLBT, self).__init__(register,
            'TOUT0MATCHLBT', 'PROTIMER.IF.TOUT0MATCHLBT', 'read-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_PRECNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_PRECNTOF, self).__init__(register,
            'PRECNTOF', 'PROTIMER.IFS.PRECNTOF', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_BASECNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_BASECNTOF, self).__init__(register,
            'BASECNTOF', 'PROTIMER.IFS.BASECNTOF', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_WRAPCNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_WRAPCNTOF, self).__init__(register,
            'WRAPCNTOF', 'PROTIMER.IFS.WRAPCNTOF', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_TOUT0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_TOUT0, self).__init__(register,
            'TOUT0', 'PROTIMER.IFS.TOUT0', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_TOUT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_TOUT1, self).__init__(register,
            'TOUT1', 'PROTIMER.IFS.TOUT1', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_TOUT0MATCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_TOUT0MATCH, self).__init__(register,
            'TOUT0MATCH', 'PROTIMER.IFS.TOUT0MATCH', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_TOUT1MATCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_TOUT1MATCH, self).__init__(register,
            'TOUT1MATCH', 'PROTIMER.IFS.TOUT1MATCH', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_CC0, self).__init__(register,
            'CC0', 'PROTIMER.IFS.CC0', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_CC1, self).__init__(register,
            'CC1', 'PROTIMER.IFS.CC1', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_CC2, self).__init__(register,
            'CC2', 'PROTIMER.IFS.CC2', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_CC3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_CC3, self).__init__(register,
            'CC3', 'PROTIMER.IFS.CC3', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_CC4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_CC4, self).__init__(register,
            'CC4', 'PROTIMER.IFS.CC4', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_COF0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_COF0, self).__init__(register,
            'COF0', 'PROTIMER.IFS.COF0', 'write-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_COF1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_COF1, self).__init__(register,
            'COF1', 'PROTIMER.IFS.COF1', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_COF2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_COF2, self).__init__(register,
            'COF2', 'PROTIMER.IFS.COF2', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_COF3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_COF3, self).__init__(register,
            'COF3', 'PROTIMER.IFS.COF3', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_COF4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_COF4, self).__init__(register,
            'COF4', 'PROTIMER.IFS.COF4', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_LBTSUCCESS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_LBTSUCCESS, self).__init__(register,
            'LBTSUCCESS', 'PROTIMER.IFS.LBTSUCCESS', 'write-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_LBTRETRY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_LBTRETRY, self).__init__(register,
            'LBTRETRY', 'PROTIMER.IFS.LBTRETRY', 'write-only',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_LBTFAILURE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_LBTFAILURE, self).__init__(register,
            'LBTFAILURE', 'PROTIMER.IFS.LBTFAILURE', 'write-only',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_LBTPAUSED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_LBTPAUSED, self).__init__(register,
            'LBTPAUSED', 'PROTIMER.IFS.LBTPAUSED', 'write-only',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_RTCCSYNCHED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_RTCCSYNCHED, self).__init__(register,
            'RTCCSYNCHED', 'PROTIMER.IFS.RTCCSYNCHED', 'write-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFS_TOUT0MATCHLBT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFS_TOUT0MATCHLBT, self).__init__(register,
            'TOUT0MATCHLBT', 'PROTIMER.IFS.TOUT0MATCHLBT', 'write-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_PRECNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_PRECNTOF, self).__init__(register,
            'PRECNTOF', 'PROTIMER.IFC.PRECNTOF', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_BASECNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_BASECNTOF, self).__init__(register,
            'BASECNTOF', 'PROTIMER.IFC.BASECNTOF', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_WRAPCNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_WRAPCNTOF, self).__init__(register,
            'WRAPCNTOF', 'PROTIMER.IFC.WRAPCNTOF', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_TOUT0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_TOUT0, self).__init__(register,
            'TOUT0', 'PROTIMER.IFC.TOUT0', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_TOUT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_TOUT1, self).__init__(register,
            'TOUT1', 'PROTIMER.IFC.TOUT1', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_TOUT0MATCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_TOUT0MATCH, self).__init__(register,
            'TOUT0MATCH', 'PROTIMER.IFC.TOUT0MATCH', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_TOUT1MATCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_TOUT1MATCH, self).__init__(register,
            'TOUT1MATCH', 'PROTIMER.IFC.TOUT1MATCH', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_CC0, self).__init__(register,
            'CC0', 'PROTIMER.IFC.CC0', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_CC1, self).__init__(register,
            'CC1', 'PROTIMER.IFC.CC1', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_CC2, self).__init__(register,
            'CC2', 'PROTIMER.IFC.CC2', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_CC3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_CC3, self).__init__(register,
            'CC3', 'PROTIMER.IFC.CC3', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_CC4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_CC4, self).__init__(register,
            'CC4', 'PROTIMER.IFC.CC4', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_COF0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_COF0, self).__init__(register,
            'COF0', 'PROTIMER.IFC.COF0', 'write-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_COF1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_COF1, self).__init__(register,
            'COF1', 'PROTIMER.IFC.COF1', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_COF2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_COF2, self).__init__(register,
            'COF2', 'PROTIMER.IFC.COF2', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_COF3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_COF3, self).__init__(register,
            'COF3', 'PROTIMER.IFC.COF3', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_COF4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_COF4, self).__init__(register,
            'COF4', 'PROTIMER.IFC.COF4', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_LBTSUCCESS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_LBTSUCCESS, self).__init__(register,
            'LBTSUCCESS', 'PROTIMER.IFC.LBTSUCCESS', 'write-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_LBTRETRY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_LBTRETRY, self).__init__(register,
            'LBTRETRY', 'PROTIMER.IFC.LBTRETRY', 'write-only',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_LBTFAILURE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_LBTFAILURE, self).__init__(register,
            'LBTFAILURE', 'PROTIMER.IFC.LBTFAILURE', 'write-only',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_LBTPAUSED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_LBTPAUSED, self).__init__(register,
            'LBTPAUSED', 'PROTIMER.IFC.LBTPAUSED', 'write-only',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_RTCCSYNCHED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_RTCCSYNCHED, self).__init__(register,
            'RTCCSYNCHED', 'PROTIMER.IFC.RTCCSYNCHED', 'write-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IFC_TOUT0MATCHLBT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IFC_TOUT0MATCHLBT, self).__init__(register,
            'TOUT0MATCHLBT', 'PROTIMER.IFC.TOUT0MATCHLBT', 'write-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_PRECNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_PRECNTOF, self).__init__(register,
            'PRECNTOF', 'PROTIMER.IEN.PRECNTOF', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_BASECNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_BASECNTOF, self).__init__(register,
            'BASECNTOF', 'PROTIMER.IEN.BASECNTOF', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_WRAPCNTOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_WRAPCNTOF, self).__init__(register,
            'WRAPCNTOF', 'PROTIMER.IEN.WRAPCNTOF', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_TOUT0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_TOUT0, self).__init__(register,
            'TOUT0', 'PROTIMER.IEN.TOUT0', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_TOUT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_TOUT1, self).__init__(register,
            'TOUT1', 'PROTIMER.IEN.TOUT1', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_TOUT0MATCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_TOUT0MATCH, self).__init__(register,
            'TOUT0MATCH', 'PROTIMER.IEN.TOUT0MATCH', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_TOUT1MATCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_TOUT1MATCH, self).__init__(register,
            'TOUT1MATCH', 'PROTIMER.IEN.TOUT1MATCH', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_CC0, self).__init__(register,
            'CC0', 'PROTIMER.IEN.CC0', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_CC1, self).__init__(register,
            'CC1', 'PROTIMER.IEN.CC1', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_CC2, self).__init__(register,
            'CC2', 'PROTIMER.IEN.CC2', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_CC3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_CC3, self).__init__(register,
            'CC3', 'PROTIMER.IEN.CC3', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_CC4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_CC4, self).__init__(register,
            'CC4', 'PROTIMER.IEN.CC4', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_COF0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_COF0, self).__init__(register,
            'COF0', 'PROTIMER.IEN.COF0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_COF1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_COF1, self).__init__(register,
            'COF1', 'PROTIMER.IEN.COF1', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_COF2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_COF2, self).__init__(register,
            'COF2', 'PROTIMER.IEN.COF2', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_COF3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_COF3, self).__init__(register,
            'COF3', 'PROTIMER.IEN.COF3', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_COF4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_COF4, self).__init__(register,
            'COF4', 'PROTIMER.IEN.COF4', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_LBTSUCCESS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_LBTSUCCESS, self).__init__(register,
            'LBTSUCCESS', 'PROTIMER.IEN.LBTSUCCESS', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_LBTRETRY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_LBTRETRY, self).__init__(register,
            'LBTRETRY', 'PROTIMER.IEN.LBTRETRY', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_LBTFAILURE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_LBTFAILURE, self).__init__(register,
            'LBTFAILURE', 'PROTIMER.IEN.LBTFAILURE', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_LBTPAUSED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_LBTPAUSED, self).__init__(register,
            'LBTPAUSED', 'PROTIMER.IEN.LBTPAUSED', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_RTCCSYNCHED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_RTCCSYNCHED, self).__init__(register,
            'RTCCSYNCHED', 'PROTIMER.IEN.RTCCSYNCHED', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_IEN_TOUT0MATCHLBT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_IEN_TOUT0MATCHLBT, self).__init__(register,
            'TOUT0MATCHLBT', 'PROTIMER.IEN.TOUT0MATCHLBT', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_RXCTRL_RXSETEVENT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_RXCTRL_RXSETEVENT1, self).__init__(register,
            'RXSETEVENT1', 'PROTIMER.RXCTRL.RXSETEVENT1', 'read-write',
            "",
            0, 5,
            RM_Enum_PROTIMER_RXCTRL_RXSETEVENT1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_RXCTRL_RXSETEVENT2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_RXCTRL_RXSETEVENT2, self).__init__(register,
            'RXSETEVENT2', 'PROTIMER.RXCTRL.RXSETEVENT2', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_RXCTRL_RXCLREVENT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_RXCTRL_RXCLREVENT1, self).__init__(register,
            'RXCLREVENT1', 'PROTIMER.RXCTRL.RXCLREVENT1', 'read-write',
            "",
            16, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_RXCTRL_RXCLREVENT2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_RXCTRL_RXCLREVENT2, self).__init__(register,
            'RXCLREVENT2', 'PROTIMER.RXCTRL.RXCLREVENT2', 'read-write',
            "",
            24, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_TXCTRL_TXSETEVENT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_TXCTRL_TXSETEVENT1, self).__init__(register,
            'TXSETEVENT1', 'PROTIMER.TXCTRL.TXSETEVENT1', 'read-write',
            "",
            0, 5,
            RM_Enum_PROTIMER_TXCTRL_TXSETEVENT1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_TXCTRL_TXSETEVENT2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_TXCTRL_TXSETEVENT2, self).__init__(register,
            'TXSETEVENT2', 'PROTIMER.TXCTRL.TXSETEVENT2', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_CTRL_ENABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_CTRL_ENABLE, self).__init__(register,
            'ENABLE', 'PROTIMER.CC0_CTRL.ENABLE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_CTRL_CCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_CTRL_CCMODE, self).__init__(register,
            'CCMODE', 'PROTIMER.CC0_CTRL.CCMODE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_CTRL_PREMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_CTRL_PREMATCHEN, self).__init__(register,
            'PREMATCHEN', 'PROTIMER.CC0_CTRL.PREMATCHEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_CTRL_BASEMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_CTRL_BASEMATCHEN, self).__init__(register,
            'BASEMATCHEN', 'PROTIMER.CC0_CTRL.BASEMATCHEN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_CTRL_WRAPMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_CTRL_WRAPMATCHEN, self).__init__(register,
            'WRAPMATCHEN', 'PROTIMER.CC0_CTRL.WRAPMATCHEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_CTRL_OIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_CTRL_OIST, self).__init__(register,
            'OIST', 'PROTIMER.CC0_CTRL.OIST', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_CTRL_OUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_CTRL_OUTINV, self).__init__(register,
            'OUTINV', 'PROTIMER.CC0_CTRL.OUTINV', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_CTRL_MOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_CTRL_MOA, self).__init__(register,
            'MOA', 'PROTIMER.CC0_CTRL.MOA', 'read-write',
            "",
            8, 2,
            RM_Enum_PROTIMER_CC0_CTRL_MOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_CTRL_OFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_CTRL_OFOA, self).__init__(register,
            'OFOA', 'PROTIMER.CC0_CTRL.OFOA', 'read-write',
            "",
            10, 2,
            RM_Enum_PROTIMER_CC0_CTRL_OFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_CTRL_OFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_CTRL_OFSEL, self).__init__(register,
            'OFSEL', 'PROTIMER.CC0_CTRL.OFSEL', 'read-write',
            "",
            12, 2,
            RM_Enum_PROTIMER_CC0_CTRL_OFSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_CTRL_PRSCONF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_CTRL_PRSCONF, self).__init__(register,
            'PRSCONF', 'PROTIMER.CC0_CTRL.PRSCONF', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'PROTIMER.CC0_CTRL.PRSSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_PROTIMER_CC0_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_CTRL_INSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_CTRL_INSEL, self).__init__(register,
            'INSEL', 'PROTIMER.CC0_CTRL.INSEL', 'read-write',
            "",
            21, 3,
            RM_Enum_PROTIMER_CC0_CTRL_INSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'PROTIMER.CC0_CTRL.ICEDGE', 'read-write',
            "",
            24, 2,
            RM_Enum_PROTIMER_CC0_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_PRE_PRE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_PRE_PRE, self).__init__(register,
            'PRE', 'PROTIMER.CC0_PRE.PRE', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_BASE_BASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_BASE_BASE, self).__init__(register,
            'BASE', 'PROTIMER.CC0_BASE.BASE', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC0_WRAP_WRAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC0_WRAP_WRAP, self).__init__(register,
            'WRAP', 'PROTIMER.CC0_WRAP.WRAP', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_CTRL_ENABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_CTRL_ENABLE, self).__init__(register,
            'ENABLE', 'PROTIMER.CC1_CTRL.ENABLE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_CTRL_CCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_CTRL_CCMODE, self).__init__(register,
            'CCMODE', 'PROTIMER.CC1_CTRL.CCMODE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_CTRL_PREMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_CTRL_PREMATCHEN, self).__init__(register,
            'PREMATCHEN', 'PROTIMER.CC1_CTRL.PREMATCHEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_CTRL_BASEMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_CTRL_BASEMATCHEN, self).__init__(register,
            'BASEMATCHEN', 'PROTIMER.CC1_CTRL.BASEMATCHEN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_CTRL_WRAPMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_CTRL_WRAPMATCHEN, self).__init__(register,
            'WRAPMATCHEN', 'PROTIMER.CC1_CTRL.WRAPMATCHEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_CTRL_OIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_CTRL_OIST, self).__init__(register,
            'OIST', 'PROTIMER.CC1_CTRL.OIST', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_CTRL_OUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_CTRL_OUTINV, self).__init__(register,
            'OUTINV', 'PROTIMER.CC1_CTRL.OUTINV', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_CTRL_MOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_CTRL_MOA, self).__init__(register,
            'MOA', 'PROTIMER.CC1_CTRL.MOA', 'read-write',
            "",
            8, 2,
            RM_Enum_PROTIMER_CC1_CTRL_MOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_CTRL_OFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_CTRL_OFOA, self).__init__(register,
            'OFOA', 'PROTIMER.CC1_CTRL.OFOA', 'read-write',
            "",
            10, 2,
            RM_Enum_PROTIMER_CC1_CTRL_OFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_CTRL_OFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_CTRL_OFSEL, self).__init__(register,
            'OFSEL', 'PROTIMER.CC1_CTRL.OFSEL', 'read-write',
            "",
            12, 2,
            RM_Enum_PROTIMER_CC1_CTRL_OFSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_CTRL_PRSCONF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_CTRL_PRSCONF, self).__init__(register,
            'PRSCONF', 'PROTIMER.CC1_CTRL.PRSCONF', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'PROTIMER.CC1_CTRL.PRSSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_PROTIMER_CC1_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_CTRL_INSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_CTRL_INSEL, self).__init__(register,
            'INSEL', 'PROTIMER.CC1_CTRL.INSEL', 'read-write',
            "",
            21, 3,
            RM_Enum_PROTIMER_CC1_CTRL_INSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'PROTIMER.CC1_CTRL.ICEDGE', 'read-write',
            "",
            24, 2,
            RM_Enum_PROTIMER_CC1_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_PRE_PRE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_PRE_PRE, self).__init__(register,
            'PRE', 'PROTIMER.CC1_PRE.PRE', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_BASE_BASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_BASE_BASE, self).__init__(register,
            'BASE', 'PROTIMER.CC1_BASE.BASE', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC1_WRAP_WRAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC1_WRAP_WRAP, self).__init__(register,
            'WRAP', 'PROTIMER.CC1_WRAP.WRAP', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_CTRL_ENABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_CTRL_ENABLE, self).__init__(register,
            'ENABLE', 'PROTIMER.CC2_CTRL.ENABLE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_CTRL_CCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_CTRL_CCMODE, self).__init__(register,
            'CCMODE', 'PROTIMER.CC2_CTRL.CCMODE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_CTRL_PREMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_CTRL_PREMATCHEN, self).__init__(register,
            'PREMATCHEN', 'PROTIMER.CC2_CTRL.PREMATCHEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_CTRL_BASEMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_CTRL_BASEMATCHEN, self).__init__(register,
            'BASEMATCHEN', 'PROTIMER.CC2_CTRL.BASEMATCHEN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_CTRL_WRAPMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_CTRL_WRAPMATCHEN, self).__init__(register,
            'WRAPMATCHEN', 'PROTIMER.CC2_CTRL.WRAPMATCHEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_CTRL_OIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_CTRL_OIST, self).__init__(register,
            'OIST', 'PROTIMER.CC2_CTRL.OIST', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_CTRL_OUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_CTRL_OUTINV, self).__init__(register,
            'OUTINV', 'PROTIMER.CC2_CTRL.OUTINV', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_CTRL_MOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_CTRL_MOA, self).__init__(register,
            'MOA', 'PROTIMER.CC2_CTRL.MOA', 'read-write',
            "",
            8, 2,
            RM_Enum_PROTIMER_CC2_CTRL_MOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_CTRL_OFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_CTRL_OFOA, self).__init__(register,
            'OFOA', 'PROTIMER.CC2_CTRL.OFOA', 'read-write',
            "",
            10, 2,
            RM_Enum_PROTIMER_CC2_CTRL_OFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_CTRL_OFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_CTRL_OFSEL, self).__init__(register,
            'OFSEL', 'PROTIMER.CC2_CTRL.OFSEL', 'read-write',
            "",
            12, 2,
            RM_Enum_PROTIMER_CC2_CTRL_OFSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_CTRL_PRSCONF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_CTRL_PRSCONF, self).__init__(register,
            'PRSCONF', 'PROTIMER.CC2_CTRL.PRSCONF', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'PROTIMER.CC2_CTRL.PRSSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_PROTIMER_CC2_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_CTRL_INSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_CTRL_INSEL, self).__init__(register,
            'INSEL', 'PROTIMER.CC2_CTRL.INSEL', 'read-write',
            "",
            21, 3,
            RM_Enum_PROTIMER_CC2_CTRL_INSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'PROTIMER.CC2_CTRL.ICEDGE', 'read-write',
            "",
            24, 2,
            RM_Enum_PROTIMER_CC2_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_PRE_PRE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_PRE_PRE, self).__init__(register,
            'PRE', 'PROTIMER.CC2_PRE.PRE', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_BASE_BASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_BASE_BASE, self).__init__(register,
            'BASE', 'PROTIMER.CC2_BASE.BASE', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC2_WRAP_WRAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC2_WRAP_WRAP, self).__init__(register,
            'WRAP', 'PROTIMER.CC2_WRAP.WRAP', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_CTRL_ENABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_CTRL_ENABLE, self).__init__(register,
            'ENABLE', 'PROTIMER.CC3_CTRL.ENABLE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_CTRL_CCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_CTRL_CCMODE, self).__init__(register,
            'CCMODE', 'PROTIMER.CC3_CTRL.CCMODE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_CTRL_PREMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_CTRL_PREMATCHEN, self).__init__(register,
            'PREMATCHEN', 'PROTIMER.CC3_CTRL.PREMATCHEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_CTRL_BASEMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_CTRL_BASEMATCHEN, self).__init__(register,
            'BASEMATCHEN', 'PROTIMER.CC3_CTRL.BASEMATCHEN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_CTRL_WRAPMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_CTRL_WRAPMATCHEN, self).__init__(register,
            'WRAPMATCHEN', 'PROTIMER.CC3_CTRL.WRAPMATCHEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_CTRL_OIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_CTRL_OIST, self).__init__(register,
            'OIST', 'PROTIMER.CC3_CTRL.OIST', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_CTRL_OUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_CTRL_OUTINV, self).__init__(register,
            'OUTINV', 'PROTIMER.CC3_CTRL.OUTINV', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_CTRL_MOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_CTRL_MOA, self).__init__(register,
            'MOA', 'PROTIMER.CC3_CTRL.MOA', 'read-write',
            "",
            8, 2,
            RM_Enum_PROTIMER_CC3_CTRL_MOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_CTRL_OFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_CTRL_OFOA, self).__init__(register,
            'OFOA', 'PROTIMER.CC3_CTRL.OFOA', 'read-write',
            "",
            10, 2,
            RM_Enum_PROTIMER_CC3_CTRL_OFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_CTRL_OFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_CTRL_OFSEL, self).__init__(register,
            'OFSEL', 'PROTIMER.CC3_CTRL.OFSEL', 'read-write',
            "",
            12, 2,
            RM_Enum_PROTIMER_CC3_CTRL_OFSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_CTRL_PRSCONF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_CTRL_PRSCONF, self).__init__(register,
            'PRSCONF', 'PROTIMER.CC3_CTRL.PRSCONF', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'PROTIMER.CC3_CTRL.PRSSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_PROTIMER_CC3_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_CTRL_INSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_CTRL_INSEL, self).__init__(register,
            'INSEL', 'PROTIMER.CC3_CTRL.INSEL', 'read-write',
            "",
            21, 3,
            RM_Enum_PROTIMER_CC3_CTRL_INSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'PROTIMER.CC3_CTRL.ICEDGE', 'read-write',
            "",
            24, 2,
            RM_Enum_PROTIMER_CC3_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_PRE_PRE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_PRE_PRE, self).__init__(register,
            'PRE', 'PROTIMER.CC3_PRE.PRE', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_BASE_BASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_BASE_BASE, self).__init__(register,
            'BASE', 'PROTIMER.CC3_BASE.BASE', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC3_WRAP_WRAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC3_WRAP_WRAP, self).__init__(register,
            'WRAP', 'PROTIMER.CC3_WRAP.WRAP', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_CTRL_ENABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_CTRL_ENABLE, self).__init__(register,
            'ENABLE', 'PROTIMER.CC4_CTRL.ENABLE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_CTRL_CCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_CTRL_CCMODE, self).__init__(register,
            'CCMODE', 'PROTIMER.CC4_CTRL.CCMODE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_CTRL_PREMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_CTRL_PREMATCHEN, self).__init__(register,
            'PREMATCHEN', 'PROTIMER.CC4_CTRL.PREMATCHEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_CTRL_BASEMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_CTRL_BASEMATCHEN, self).__init__(register,
            'BASEMATCHEN', 'PROTIMER.CC4_CTRL.BASEMATCHEN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_CTRL_WRAPMATCHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_CTRL_WRAPMATCHEN, self).__init__(register,
            'WRAPMATCHEN', 'PROTIMER.CC4_CTRL.WRAPMATCHEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_CTRL_OIST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_CTRL_OIST, self).__init__(register,
            'OIST', 'PROTIMER.CC4_CTRL.OIST', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_CTRL_OUTINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_CTRL_OUTINV, self).__init__(register,
            'OUTINV', 'PROTIMER.CC4_CTRL.OUTINV', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_CTRL_MOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_CTRL_MOA, self).__init__(register,
            'MOA', 'PROTIMER.CC4_CTRL.MOA', 'read-write',
            "",
            8, 2,
            RM_Enum_PROTIMER_CC4_CTRL_MOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_CTRL_OFOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_CTRL_OFOA, self).__init__(register,
            'OFOA', 'PROTIMER.CC4_CTRL.OFOA', 'read-write',
            "",
            10, 2,
            RM_Enum_PROTIMER_CC4_CTRL_OFOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_CTRL_OFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_CTRL_OFSEL, self).__init__(register,
            'OFSEL', 'PROTIMER.CC4_CTRL.OFSEL', 'read-write',
            "",
            12, 2,
            RM_Enum_PROTIMER_CC4_CTRL_OFSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_CTRL_PRSCONF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_CTRL_PRSCONF, self).__init__(register,
            'PRSCONF', 'PROTIMER.CC4_CTRL.PRSCONF', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'PROTIMER.CC4_CTRL.PRSSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_PROTIMER_CC4_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_CTRL_INSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_CTRL_INSEL, self).__init__(register,
            'INSEL', 'PROTIMER.CC4_CTRL.INSEL', 'read-write',
            "",
            21, 3,
            RM_Enum_PROTIMER_CC4_CTRL_INSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'PROTIMER.CC4_CTRL.ICEDGE', 'read-write',
            "",
            24, 2,
            RM_Enum_PROTIMER_CC4_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_PRE_PRE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_PRE_PRE, self).__init__(register,
            'PRE', 'PROTIMER.CC4_PRE.PRE', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_BASE_BASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_BASE_BASE, self).__init__(register,
            'BASE', 'PROTIMER.CC4_BASE.BASE', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PROTIMER_CC4_WRAP_WRAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PROTIMER_CC4_WRAP_WRAP, self).__init__(register,
            'WRAP', 'PROTIMER.CC4_WRAP.WRAP', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


