
from static import Base_RM_Field
from USART1_enum import *


class RM_Field_USART1_CTRL_SYNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_SYNC, self).__init__(register,
            'SYNC', 'USART1.CTRL.SYNC', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_LOOPBK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_LOOPBK, self).__init__(register,
            'LOOPBK', 'USART1.CTRL.LOOPBK', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_CCEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_CCEN, self).__init__(register,
            'CCEN', 'USART1.CTRL.CCEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_MPM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_MPM, self).__init__(register,
            'MPM', 'USART1.CTRL.MPM', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_MPAB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_MPAB, self).__init__(register,
            'MPAB', 'USART1.CTRL.MPAB', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_OVS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_OVS, self).__init__(register,
            'OVS', 'USART1.CTRL.OVS', 'read-write',
            "",
            5, 2,
            RM_Enum_USART1_CTRL_OVS(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_CLKPOL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_CLKPOL, self).__init__(register,
            'CLKPOL', 'USART1.CTRL.CLKPOL', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_CLKPHA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_CLKPHA, self).__init__(register,
            'CLKPHA', 'USART1.CTRL.CLKPHA', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_MSBF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_MSBF, self).__init__(register,
            'MSBF', 'USART1.CTRL.MSBF', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_CSMA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_CSMA, self).__init__(register,
            'CSMA', 'USART1.CTRL.CSMA', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_TXBIL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_TXBIL, self).__init__(register,
            'TXBIL', 'USART1.CTRL.TXBIL', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_RXINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_RXINV, self).__init__(register,
            'RXINV', 'USART1.CTRL.RXINV', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_TXINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_TXINV, self).__init__(register,
            'TXINV', 'USART1.CTRL.TXINV', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_CSINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_CSINV, self).__init__(register,
            'CSINV', 'USART1.CTRL.CSINV', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_AUTOCS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_AUTOCS, self).__init__(register,
            'AUTOCS', 'USART1.CTRL.AUTOCS', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_AUTOTRI(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_AUTOTRI, self).__init__(register,
            'AUTOTRI', 'USART1.CTRL.AUTOTRI', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_SCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_SCMODE, self).__init__(register,
            'SCMODE', 'USART1.CTRL.SCMODE', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_SCRETRANS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_SCRETRANS, self).__init__(register,
            'SCRETRANS', 'USART1.CTRL.SCRETRANS', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_SKIPPERRF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_SKIPPERRF, self).__init__(register,
            'SKIPPERRF', 'USART1.CTRL.SKIPPERRF', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_BIT8DV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_BIT8DV, self).__init__(register,
            'BIT8DV', 'USART1.CTRL.BIT8DV', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_ERRSDMA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_ERRSDMA, self).__init__(register,
            'ERRSDMA', 'USART1.CTRL.ERRSDMA', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_ERRSRX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_ERRSRX, self).__init__(register,
            'ERRSRX', 'USART1.CTRL.ERRSRX', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_ERRSTX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_ERRSTX, self).__init__(register,
            'ERRSTX', 'USART1.CTRL.ERRSTX', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_SSSEARLY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_SSSEARLY, self).__init__(register,
            'SSSEARLY', 'USART1.CTRL.SSSEARLY', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_BYTESWAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_BYTESWAP, self).__init__(register,
            'BYTESWAP', 'USART1.CTRL.BYTESWAP', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_AUTOTX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_AUTOTX, self).__init__(register,
            'AUTOTX', 'USART1.CTRL.AUTOTX', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_MVDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_MVDIS, self).__init__(register,
            'MVDIS', 'USART1.CTRL.MVDIS', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRL_SMSDELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRL_SMSDELAY, self).__init__(register,
            'SMSDELAY', 'USART1.CTRL.SMSDELAY', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_FRAME_DATABITS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_FRAME_DATABITS, self).__init__(register,
            'DATABITS', 'USART1.FRAME.DATABITS', 'read-write',
            "",
            0, 4,
            RM_Enum_USART1_FRAME_DATABITS(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_FRAME_PARITY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_FRAME_PARITY, self).__init__(register,
            'PARITY', 'USART1.FRAME.PARITY', 'read-write',
            "",
            8, 2,
            RM_Enum_USART1_FRAME_PARITY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_FRAME_STOPBITS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_FRAME_STOPBITS, self).__init__(register,
            'STOPBITS', 'USART1.FRAME.STOPBITS', 'read-write',
            "",
            12, 2,
            RM_Enum_USART1_FRAME_STOPBITS(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TRIGCTRL_RXTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TRIGCTRL_RXTEN, self).__init__(register,
            'RXTEN', 'USART1.TRIGCTRL.RXTEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TRIGCTRL_TXTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TRIGCTRL_TXTEN, self).__init__(register,
            'TXTEN', 'USART1.TRIGCTRL.TXTEN', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TRIGCTRL_AUTOTXTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TRIGCTRL_AUTOTXTEN, self).__init__(register,
            'AUTOTXTEN', 'USART1.TRIGCTRL.AUTOTXTEN', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TRIGCTRL_TXARX0EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TRIGCTRL_TXARX0EN, self).__init__(register,
            'TXARX0EN', 'USART1.TRIGCTRL.TXARX0EN', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TRIGCTRL_TXARX1EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TRIGCTRL_TXARX1EN, self).__init__(register,
            'TXARX1EN', 'USART1.TRIGCTRL.TXARX1EN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TRIGCTRL_TXARX2EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TRIGCTRL_TXARX2EN, self).__init__(register,
            'TXARX2EN', 'USART1.TRIGCTRL.TXARX2EN', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TRIGCTRL_RXATX0EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TRIGCTRL_RXATX0EN, self).__init__(register,
            'RXATX0EN', 'USART1.TRIGCTRL.RXATX0EN', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TRIGCTRL_RXATX1EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TRIGCTRL_RXATX1EN, self).__init__(register,
            'RXATX1EN', 'USART1.TRIGCTRL.RXATX1EN', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TRIGCTRL_RXATX2EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TRIGCTRL_RXATX2EN, self).__init__(register,
            'RXATX2EN', 'USART1.TRIGCTRL.RXATX2EN', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TRIGCTRL_TSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TRIGCTRL_TSEL, self).__init__(register,
            'TSEL', 'USART1.TRIGCTRL.TSEL', 'read-write',
            "",
            16, 4,
            RM_Enum_USART1_TRIGCTRL_TSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CMD_RXEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CMD_RXEN, self).__init__(register,
            'RXEN', 'USART1.CMD.RXEN', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CMD_RXDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CMD_RXDIS, self).__init__(register,
            'RXDIS', 'USART1.CMD.RXDIS', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CMD_TXEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CMD_TXEN, self).__init__(register,
            'TXEN', 'USART1.CMD.TXEN', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CMD_TXDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CMD_TXDIS, self).__init__(register,
            'TXDIS', 'USART1.CMD.TXDIS', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CMD_MASTEREN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CMD_MASTEREN, self).__init__(register,
            'MASTEREN', 'USART1.CMD.MASTEREN', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CMD_MASTERDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CMD_MASTERDIS, self).__init__(register,
            'MASTERDIS', 'USART1.CMD.MASTERDIS', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CMD_RXBLOCKEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CMD_RXBLOCKEN, self).__init__(register,
            'RXBLOCKEN', 'USART1.CMD.RXBLOCKEN', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CMD_RXBLOCKDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CMD_RXBLOCKDIS, self).__init__(register,
            'RXBLOCKDIS', 'USART1.CMD.RXBLOCKDIS', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CMD_TXTRIEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CMD_TXTRIEN, self).__init__(register,
            'TXTRIEN', 'USART1.CMD.TXTRIEN', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CMD_TXTRIDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CMD_TXTRIDIS, self).__init__(register,
            'TXTRIDIS', 'USART1.CMD.TXTRIDIS', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CMD_CLEARTX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CMD_CLEARTX, self).__init__(register,
            'CLEARTX', 'USART1.CMD.CLEARTX', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CMD_CLEARRX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CMD_CLEARRX, self).__init__(register,
            'CLEARRX', 'USART1.CMD.CLEARRX', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_RXENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_RXENS, self).__init__(register,
            'RXENS', 'USART1.STATUS.RXENS', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_TXENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_TXENS, self).__init__(register,
            'TXENS', 'USART1.STATUS.TXENS', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_MASTER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_MASTER, self).__init__(register,
            'MASTER', 'USART1.STATUS.MASTER', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_RXBLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_RXBLOCK, self).__init__(register,
            'RXBLOCK', 'USART1.STATUS.RXBLOCK', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_TXTRI(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_TXTRI, self).__init__(register,
            'TXTRI', 'USART1.STATUS.TXTRI', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_TXC, self).__init__(register,
            'TXC', 'USART1.STATUS.TXC', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_TXBL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_TXBL, self).__init__(register,
            'TXBL', 'USART1.STATUS.TXBL', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_RXDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_RXDATAV, self).__init__(register,
            'RXDATAV', 'USART1.STATUS.RXDATAV', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_RXFULL, self).__init__(register,
            'RXFULL', 'USART1.STATUS.RXFULL', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_TXBDRIGHT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_TXBDRIGHT, self).__init__(register,
            'TXBDRIGHT', 'USART1.STATUS.TXBDRIGHT', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_TXBSRIGHT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_TXBSRIGHT, self).__init__(register,
            'TXBSRIGHT', 'USART1.STATUS.TXBSRIGHT', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_RXDATAVRIGHT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_RXDATAVRIGHT, self).__init__(register,
            'RXDATAVRIGHT', 'USART1.STATUS.RXDATAVRIGHT', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_RXFULLRIGHT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_RXFULLRIGHT, self).__init__(register,
            'RXFULLRIGHT', 'USART1.STATUS.RXFULLRIGHT', 'read-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_TXIDLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_TXIDLE, self).__init__(register,
            'TXIDLE', 'USART1.STATUS.TXIDLE', 'read-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_TIMERRESTARTED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_TIMERRESTARTED, self).__init__(register,
            'TIMERRESTARTED', 'USART1.STATUS.TIMERRESTARTED', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_STATUS_TXBUFCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_STATUS_TXBUFCNT, self).__init__(register,
            'TXBUFCNT', 'USART1.STATUS.TXBUFCNT', 'read-only',
            "",
            16, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CLKDIV_DIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CLKDIV_DIV, self).__init__(register,
            'DIV', 'USART1.CLKDIV.DIV', 'read-write',
            "",
            3, 20)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CLKDIV_AUTOBAUDEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CLKDIV_AUTOBAUDEN, self).__init__(register,
            'AUTOBAUDEN', 'USART1.CLKDIV.AUTOBAUDEN', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDATAX_RXDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDATAX_RXDATA, self).__init__(register,
            'RXDATA', 'USART1.RXDATAX.RXDATA', 'read-only',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDATAX_PERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDATAX_PERR, self).__init__(register,
            'PERR', 'USART1.RXDATAX.PERR', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDATAX_FERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDATAX_FERR, self).__init__(register,
            'FERR', 'USART1.RXDATAX.FERR', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDATA_RXDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDATA_RXDATA, self).__init__(register,
            'RXDATA', 'USART1.RXDATA.RXDATA', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDOUBLEX_RXDATA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDOUBLEX_RXDATA0, self).__init__(register,
            'RXDATA0', 'USART1.RXDOUBLEX.RXDATA0', 'read-only',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDOUBLEX_PERR0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDOUBLEX_PERR0, self).__init__(register,
            'PERR0', 'USART1.RXDOUBLEX.PERR0', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDOUBLEX_FERR0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDOUBLEX_FERR0, self).__init__(register,
            'FERR0', 'USART1.RXDOUBLEX.FERR0', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDOUBLEX_RXDATA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDOUBLEX_RXDATA1, self).__init__(register,
            'RXDATA1', 'USART1.RXDOUBLEX.RXDATA1', 'read-only',
            "",
            16, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDOUBLEX_PERR1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDOUBLEX_PERR1, self).__init__(register,
            'PERR1', 'USART1.RXDOUBLEX.PERR1', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDOUBLEX_FERR1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDOUBLEX_FERR1, self).__init__(register,
            'FERR1', 'USART1.RXDOUBLEX.FERR1', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDOUBLE_RXDATA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDOUBLE_RXDATA0, self).__init__(register,
            'RXDATA0', 'USART1.RXDOUBLE.RXDATA0', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDOUBLE_RXDATA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDOUBLE_RXDATA1, self).__init__(register,
            'RXDATA1', 'USART1.RXDOUBLE.RXDATA1', 'read-only',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDATAXP_RXDATAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDATAXP_RXDATAP, self).__init__(register,
            'RXDATAP', 'USART1.RXDATAXP.RXDATAP', 'read-only',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDATAXP_PERRP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDATAXP_PERRP, self).__init__(register,
            'PERRP', 'USART1.RXDATAXP.PERRP', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDATAXP_FERRP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDATAXP_FERRP, self).__init__(register,
            'FERRP', 'USART1.RXDATAXP.FERRP', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDOUBLEXP_RXDATAP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDOUBLEXP_RXDATAP0, self).__init__(register,
            'RXDATAP0', 'USART1.RXDOUBLEXP.RXDATAP0', 'read-only',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDOUBLEXP_PERRP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDOUBLEXP_PERRP0, self).__init__(register,
            'PERRP0', 'USART1.RXDOUBLEXP.PERRP0', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDOUBLEXP_FERRP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDOUBLEXP_FERRP0, self).__init__(register,
            'FERRP0', 'USART1.RXDOUBLEXP.FERRP0', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDOUBLEXP_RXDATAP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDOUBLEXP_RXDATAP1, self).__init__(register,
            'RXDATAP1', 'USART1.RXDOUBLEXP.RXDATAP1', 'read-only',
            "",
            16, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDOUBLEXP_PERRP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDOUBLEXP_PERRP1, self).__init__(register,
            'PERRP1', 'USART1.RXDOUBLEXP.PERRP1', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_RXDOUBLEXP_FERRP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_RXDOUBLEXP_FERRP1, self).__init__(register,
            'FERRP1', 'USART1.RXDOUBLEXP.FERRP1', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDATAX_TXDATAX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDATAX_TXDATAX, self).__init__(register,
            'TXDATAX', 'USART1.TXDATAX.TXDATAX', 'read-write',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDATAX_UBRXAT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDATAX_UBRXAT, self).__init__(register,
            'UBRXAT', 'USART1.TXDATAX.UBRXAT', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDATAX_TXTRIAT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDATAX_TXTRIAT, self).__init__(register,
            'TXTRIAT', 'USART1.TXDATAX.TXTRIAT', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDATAX_TXBREAK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDATAX_TXBREAK, self).__init__(register,
            'TXBREAK', 'USART1.TXDATAX.TXBREAK', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDATAX_TXDISAT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDATAX_TXDISAT, self).__init__(register,
            'TXDISAT', 'USART1.TXDATAX.TXDISAT', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDATAX_RXENAT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDATAX_RXENAT, self).__init__(register,
            'RXENAT', 'USART1.TXDATAX.RXENAT', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDATA_TXDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDATA_TXDATA, self).__init__(register,
            'TXDATA', 'USART1.TXDATA.TXDATA', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDOUBLEX_TXDATA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDOUBLEX_TXDATA0, self).__init__(register,
            'TXDATA0', 'USART1.TXDOUBLEX.TXDATA0', 'read-write',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDOUBLEX_UBRXAT0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDOUBLEX_UBRXAT0, self).__init__(register,
            'UBRXAT0', 'USART1.TXDOUBLEX.UBRXAT0', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDOUBLEX_TXTRIAT0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDOUBLEX_TXTRIAT0, self).__init__(register,
            'TXTRIAT0', 'USART1.TXDOUBLEX.TXTRIAT0', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDOUBLEX_TXBREAK0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDOUBLEX_TXBREAK0, self).__init__(register,
            'TXBREAK0', 'USART1.TXDOUBLEX.TXBREAK0', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDOUBLEX_TXDISAT0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDOUBLEX_TXDISAT0, self).__init__(register,
            'TXDISAT0', 'USART1.TXDOUBLEX.TXDISAT0', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDOUBLEX_RXENAT0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDOUBLEX_RXENAT0, self).__init__(register,
            'RXENAT0', 'USART1.TXDOUBLEX.RXENAT0', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDOUBLEX_TXDATA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDOUBLEX_TXDATA1, self).__init__(register,
            'TXDATA1', 'USART1.TXDOUBLEX.TXDATA1', 'read-write',
            "",
            16, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDOUBLEX_UBRXAT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDOUBLEX_UBRXAT1, self).__init__(register,
            'UBRXAT1', 'USART1.TXDOUBLEX.UBRXAT1', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDOUBLEX_TXTRIAT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDOUBLEX_TXTRIAT1, self).__init__(register,
            'TXTRIAT1', 'USART1.TXDOUBLEX.TXTRIAT1', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDOUBLEX_TXBREAK1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDOUBLEX_TXBREAK1, self).__init__(register,
            'TXBREAK1', 'USART1.TXDOUBLEX.TXBREAK1', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDOUBLEX_TXDISAT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDOUBLEX_TXDISAT1, self).__init__(register,
            'TXDISAT1', 'USART1.TXDOUBLEX.TXDISAT1', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDOUBLEX_RXENAT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDOUBLEX_RXENAT1, self).__init__(register,
            'RXENAT1', 'USART1.TXDOUBLEX.RXENAT1', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDOUBLE_TXDATA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDOUBLE_TXDATA0, self).__init__(register,
            'TXDATA0', 'USART1.TXDOUBLE.TXDATA0', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TXDOUBLE_TXDATA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TXDOUBLE_TXDATA1, self).__init__(register,
            'TXDATA1', 'USART1.TXDOUBLE.TXDATA1', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_TXC, self).__init__(register,
            'TXC', 'USART1.IF.TXC', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_TXBL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_TXBL, self).__init__(register,
            'TXBL', 'USART1.IF.TXBL', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_RXDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_RXDATAV, self).__init__(register,
            'RXDATAV', 'USART1.IF.RXDATAV', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_RXFULL, self).__init__(register,
            'RXFULL', 'USART1.IF.RXFULL', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_RXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_RXOF, self).__init__(register,
            'RXOF', 'USART1.IF.RXOF', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_RXUF, self).__init__(register,
            'RXUF', 'USART1.IF.RXUF', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_TXOF, self).__init__(register,
            'TXOF', 'USART1.IF.TXOF', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_TXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_TXUF, self).__init__(register,
            'TXUF', 'USART1.IF.TXUF', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_PERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_PERR, self).__init__(register,
            'PERR', 'USART1.IF.PERR', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_FERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_FERR, self).__init__(register,
            'FERR', 'USART1.IF.FERR', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_MPAF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_MPAF, self).__init__(register,
            'MPAF', 'USART1.IF.MPAF', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_SSM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_SSM, self).__init__(register,
            'SSM', 'USART1.IF.SSM', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_CCF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_CCF, self).__init__(register,
            'CCF', 'USART1.IF.CCF', 'read-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_TXIDLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_TXIDLE, self).__init__(register,
            'TXIDLE', 'USART1.IF.TXIDLE', 'read-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_TCMP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_TCMP0, self).__init__(register,
            'TCMP0', 'USART1.IF.TCMP0', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_TCMP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_TCMP1, self).__init__(register,
            'TCMP1', 'USART1.IF.TCMP1', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IF_TCMP2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IF_TCMP2, self).__init__(register,
            'TCMP2', 'USART1.IF.TCMP2', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_TXC, self).__init__(register,
            'TXC', 'USART1.IFS.TXC', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_RXFULL, self).__init__(register,
            'RXFULL', 'USART1.IFS.RXFULL', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_RXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_RXOF, self).__init__(register,
            'RXOF', 'USART1.IFS.RXOF', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_RXUF, self).__init__(register,
            'RXUF', 'USART1.IFS.RXUF', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_TXOF, self).__init__(register,
            'TXOF', 'USART1.IFS.TXOF', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_TXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_TXUF, self).__init__(register,
            'TXUF', 'USART1.IFS.TXUF', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_PERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_PERR, self).__init__(register,
            'PERR', 'USART1.IFS.PERR', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_FERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_FERR, self).__init__(register,
            'FERR', 'USART1.IFS.FERR', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_MPAF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_MPAF, self).__init__(register,
            'MPAF', 'USART1.IFS.MPAF', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_SSM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_SSM, self).__init__(register,
            'SSM', 'USART1.IFS.SSM', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_CCF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_CCF, self).__init__(register,
            'CCF', 'USART1.IFS.CCF', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_TXIDLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_TXIDLE, self).__init__(register,
            'TXIDLE', 'USART1.IFS.TXIDLE', 'write-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_TCMP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_TCMP0, self).__init__(register,
            'TCMP0', 'USART1.IFS.TCMP0', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_TCMP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_TCMP1, self).__init__(register,
            'TCMP1', 'USART1.IFS.TCMP1', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFS_TCMP2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFS_TCMP2, self).__init__(register,
            'TCMP2', 'USART1.IFS.TCMP2', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_TXC, self).__init__(register,
            'TXC', 'USART1.IFC.TXC', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_RXFULL, self).__init__(register,
            'RXFULL', 'USART1.IFC.RXFULL', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_RXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_RXOF, self).__init__(register,
            'RXOF', 'USART1.IFC.RXOF', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_RXUF, self).__init__(register,
            'RXUF', 'USART1.IFC.RXUF', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_TXOF, self).__init__(register,
            'TXOF', 'USART1.IFC.TXOF', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_TXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_TXUF, self).__init__(register,
            'TXUF', 'USART1.IFC.TXUF', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_PERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_PERR, self).__init__(register,
            'PERR', 'USART1.IFC.PERR', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_FERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_FERR, self).__init__(register,
            'FERR', 'USART1.IFC.FERR', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_MPAF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_MPAF, self).__init__(register,
            'MPAF', 'USART1.IFC.MPAF', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_SSM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_SSM, self).__init__(register,
            'SSM', 'USART1.IFC.SSM', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_CCF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_CCF, self).__init__(register,
            'CCF', 'USART1.IFC.CCF', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_TXIDLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_TXIDLE, self).__init__(register,
            'TXIDLE', 'USART1.IFC.TXIDLE', 'write-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_TCMP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_TCMP0, self).__init__(register,
            'TCMP0', 'USART1.IFC.TCMP0', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_TCMP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_TCMP1, self).__init__(register,
            'TCMP1', 'USART1.IFC.TCMP1', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IFC_TCMP2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IFC_TCMP2, self).__init__(register,
            'TCMP2', 'USART1.IFC.TCMP2', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_TXC, self).__init__(register,
            'TXC', 'USART1.IEN.TXC', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_TXBL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_TXBL, self).__init__(register,
            'TXBL', 'USART1.IEN.TXBL', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_RXDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_RXDATAV, self).__init__(register,
            'RXDATAV', 'USART1.IEN.RXDATAV', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_RXFULL, self).__init__(register,
            'RXFULL', 'USART1.IEN.RXFULL', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_RXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_RXOF, self).__init__(register,
            'RXOF', 'USART1.IEN.RXOF', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_RXUF, self).__init__(register,
            'RXUF', 'USART1.IEN.RXUF', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_TXOF, self).__init__(register,
            'TXOF', 'USART1.IEN.TXOF', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_TXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_TXUF, self).__init__(register,
            'TXUF', 'USART1.IEN.TXUF', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_PERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_PERR, self).__init__(register,
            'PERR', 'USART1.IEN.PERR', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_FERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_FERR, self).__init__(register,
            'FERR', 'USART1.IEN.FERR', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_MPAF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_MPAF, self).__init__(register,
            'MPAF', 'USART1.IEN.MPAF', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_SSM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_SSM, self).__init__(register,
            'SSM', 'USART1.IEN.SSM', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_CCF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_CCF, self).__init__(register,
            'CCF', 'USART1.IEN.CCF', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_TXIDLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_TXIDLE, self).__init__(register,
            'TXIDLE', 'USART1.IEN.TXIDLE', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_TCMP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_TCMP0, self).__init__(register,
            'TCMP0', 'USART1.IEN.TCMP0', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_TCMP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_TCMP1, self).__init__(register,
            'TCMP1', 'USART1.IEN.TCMP1', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IEN_TCMP2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IEN_TCMP2, self).__init__(register,
            'TCMP2', 'USART1.IEN.TCMP2', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IRCTRL_IREN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IRCTRL_IREN, self).__init__(register,
            'IREN', 'USART1.IRCTRL.IREN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IRCTRL_IRPW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IRCTRL_IRPW, self).__init__(register,
            'IRPW', 'USART1.IRCTRL.IRPW', 'read-write',
            "",
            1, 2,
            RM_Enum_USART1_IRCTRL_IRPW(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IRCTRL_IRFILT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IRCTRL_IRFILT, self).__init__(register,
            'IRFILT', 'USART1.IRCTRL.IRFILT', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IRCTRL_IRPRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IRCTRL_IRPRSEN, self).__init__(register,
            'IRPRSEN', 'USART1.IRCTRL.IRPRSEN', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_IRCTRL_IRPRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_IRCTRL_IRPRSSEL, self).__init__(register,
            'IRPRSSEL', 'USART1.IRCTRL.IRPRSSEL', 'read-write',
            "",
            8, 4,
            RM_Enum_USART1_IRCTRL_IRPRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_INPUT_RXPRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_INPUT_RXPRSSEL, self).__init__(register,
            'RXPRSSEL', 'USART1.INPUT.RXPRSSEL', 'read-write',
            "",
            0, 4,
            RM_Enum_USART1_INPUT_RXPRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_INPUT_RXPRS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_INPUT_RXPRS, self).__init__(register,
            'RXPRS', 'USART1.INPUT.RXPRS', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_INPUT_CLKPRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_INPUT_CLKPRSSEL, self).__init__(register,
            'CLKPRSSEL', 'USART1.INPUT.CLKPRSSEL', 'read-write',
            "",
            8, 4,
            RM_Enum_USART1_INPUT_CLKPRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_INPUT_CLKPRS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_INPUT_CLKPRS, self).__init__(register,
            'CLKPRS', 'USART1.INPUT.CLKPRS', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_I2SCTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_I2SCTRL_EN, self).__init__(register,
            'EN', 'USART1.I2SCTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_I2SCTRL_MONO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_I2SCTRL_MONO, self).__init__(register,
            'MONO', 'USART1.I2SCTRL.MONO', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_I2SCTRL_JUSTIFY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_I2SCTRL_JUSTIFY, self).__init__(register,
            'JUSTIFY', 'USART1.I2SCTRL.JUSTIFY', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_I2SCTRL_DMASPLIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_I2SCTRL_DMASPLIT, self).__init__(register,
            'DMASPLIT', 'USART1.I2SCTRL.DMASPLIT', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_I2SCTRL_DELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_I2SCTRL_DELAY, self).__init__(register,
            'DELAY', 'USART1.I2SCTRL.DELAY', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_I2SCTRL_FORMAT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_I2SCTRL_FORMAT, self).__init__(register,
            'FORMAT', 'USART1.I2SCTRL.FORMAT', 'read-write',
            "",
            8, 3,
            RM_Enum_USART1_I2SCTRL_FORMAT(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMING_TXDELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMING_TXDELAY, self).__init__(register,
            'TXDELAY', 'USART1.TIMING.TXDELAY', 'read-write',
            "",
            16, 3,
            RM_Enum_USART1_TIMING_TXDELAY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMING_CSSETUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMING_CSSETUP, self).__init__(register,
            'CSSETUP', 'USART1.TIMING.CSSETUP', 'read-write',
            "",
            20, 3,
            RM_Enum_USART1_TIMING_CSSETUP(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMING_ICS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMING_ICS, self).__init__(register,
            'ICS', 'USART1.TIMING.ICS', 'read-write',
            "",
            24, 3,
            RM_Enum_USART1_TIMING_ICS(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMING_CSHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMING_CSHOLD, self).__init__(register,
            'CSHOLD', 'USART1.TIMING.CSHOLD', 'read-write',
            "",
            28, 3,
            RM_Enum_USART1_TIMING_CSHOLD(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRLX_DBGHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRLX_DBGHALT, self).__init__(register,
            'DBGHALT', 'USART1.CTRLX.DBGHALT', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRLX_CTSINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRLX_CTSINV, self).__init__(register,
            'CTSINV', 'USART1.CTRLX.CTSINV', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRLX_CTSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRLX_CTSEN, self).__init__(register,
            'CTSEN', 'USART1.CTRLX.CTSEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRLX_RTSINV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRLX_RTSINV, self).__init__(register,
            'RTSINV', 'USART1.CTRLX.RTSINV', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_CTRLX_GPIODELAYXOREN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_CTRLX_GPIODELAYXOREN, self).__init__(register,
            'GPIODELAYXOREN', 'USART1.CTRLX.GPIODELAYXOREN', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMECMP0_TCMPVAL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMECMP0_TCMPVAL, self).__init__(register,
            'TCMPVAL', 'USART1.TIMECMP0.TCMPVAL', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMECMP0_TSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMECMP0_TSTART, self).__init__(register,
            'TSTART', 'USART1.TIMECMP0.TSTART', 'read-write',
            "",
            16, 3,
            RM_Enum_USART1_TIMECMP0_TSTART(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMECMP0_TSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMECMP0_TSTOP, self).__init__(register,
            'TSTOP', 'USART1.TIMECMP0.TSTOP', 'read-write',
            "",
            20, 3,
            RM_Enum_USART1_TIMECMP0_TSTOP(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMECMP0_RESTARTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMECMP0_RESTARTEN, self).__init__(register,
            'RESTARTEN', 'USART1.TIMECMP0.RESTARTEN', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMECMP1_TCMPVAL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMECMP1_TCMPVAL, self).__init__(register,
            'TCMPVAL', 'USART1.TIMECMP1.TCMPVAL', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMECMP1_TSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMECMP1_TSTART, self).__init__(register,
            'TSTART', 'USART1.TIMECMP1.TSTART', 'read-write',
            "",
            16, 3,
            RM_Enum_USART1_TIMECMP1_TSTART(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMECMP1_TSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMECMP1_TSTOP, self).__init__(register,
            'TSTOP', 'USART1.TIMECMP1.TSTOP', 'read-write',
            "",
            20, 3,
            RM_Enum_USART1_TIMECMP1_TSTOP(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMECMP1_RESTARTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMECMP1_RESTARTEN, self).__init__(register,
            'RESTARTEN', 'USART1.TIMECMP1.RESTARTEN', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMECMP2_TCMPVAL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMECMP2_TCMPVAL, self).__init__(register,
            'TCMPVAL', 'USART1.TIMECMP2.TCMPVAL', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMECMP2_TSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMECMP2_TSTART, self).__init__(register,
            'TSTART', 'USART1.TIMECMP2.TSTART', 'read-write',
            "",
            16, 3,
            RM_Enum_USART1_TIMECMP2_TSTART(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMECMP2_TSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMECMP2_TSTOP, self).__init__(register,
            'TSTOP', 'USART1.TIMECMP2.TSTOP', 'read-write',
            "",
            20, 3,
            RM_Enum_USART1_TIMECMP2_TSTOP(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TIMECMP2_RESTARTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TIMECMP2_RESTARTEN, self).__init__(register,
            'RESTARTEN', 'USART1.TIMECMP2.RESTARTEN', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_ROUTEPEN_RXPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_ROUTEPEN_RXPEN, self).__init__(register,
            'RXPEN', 'USART1.ROUTEPEN.RXPEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_ROUTEPEN_TXPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_ROUTEPEN_TXPEN, self).__init__(register,
            'TXPEN', 'USART1.ROUTEPEN.TXPEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_ROUTEPEN_CSPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_ROUTEPEN_CSPEN, self).__init__(register,
            'CSPEN', 'USART1.ROUTEPEN.CSPEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_ROUTEPEN_CLKPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_ROUTEPEN_CLKPEN, self).__init__(register,
            'CLKPEN', 'USART1.ROUTEPEN.CLKPEN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_ROUTEPEN_CTSPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_ROUTEPEN_CTSPEN, self).__init__(register,
            'CTSPEN', 'USART1.ROUTEPEN.CTSPEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_ROUTEPEN_RTSPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_ROUTEPEN_RTSPEN, self).__init__(register,
            'RTSPEN', 'USART1.ROUTEPEN.RTSPEN', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_ROUTELOC0_RXLOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_ROUTELOC0_RXLOC, self).__init__(register,
            'RXLOC', 'USART1.ROUTELOC0.RXLOC', 'read-write',
            "",
            0, 6,
            RM_Enum_USART1_ROUTELOC0_RXLOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_ROUTELOC0_TXLOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_ROUTELOC0_TXLOC, self).__init__(register,
            'TXLOC', 'USART1.ROUTELOC0.TXLOC', 'read-write',
            "",
            8, 6,
            RM_Enum_USART1_ROUTELOC0_TXLOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_ROUTELOC0_CSLOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_ROUTELOC0_CSLOC, self).__init__(register,
            'CSLOC', 'USART1.ROUTELOC0.CSLOC', 'read-write',
            "",
            16, 6,
            RM_Enum_USART1_ROUTELOC0_CSLOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_ROUTELOC0_CLKLOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_ROUTELOC0_CLKLOC, self).__init__(register,
            'CLKLOC', 'USART1.ROUTELOC0.CLKLOC', 'read-write',
            "",
            24, 6,
            RM_Enum_USART1_ROUTELOC0_CLKLOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_ROUTELOC1_CTSLOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_ROUTELOC1_CTSLOC, self).__init__(register,
            'CTSLOC', 'USART1.ROUTELOC1.CTSLOC', 'read-write',
            "",
            0, 6,
            RM_Enum_USART1_ROUTELOC1_CTSLOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_ROUTELOC1_RTSLOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_ROUTELOC1_RTSLOC, self).__init__(register,
            'RTSLOC', 'USART1.ROUTELOC1.RTSLOC', 'read-write',
            "",
            8, 6,
            RM_Enum_USART1_ROUTELOC1_RTSLOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TEST_GPIODELAYSTABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TEST_GPIODELAYSTABLE, self).__init__(register,
            'GPIODELAYSTABLE', 'USART1.TEST.GPIODELAYSTABLE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_USART1_TEST_GPIODELAYXOR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_USART1_TEST_GPIODELAYXOR, self).__init__(register,
            'GPIODELAYXOR', 'USART1.TEST.GPIODELAYXOR', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


