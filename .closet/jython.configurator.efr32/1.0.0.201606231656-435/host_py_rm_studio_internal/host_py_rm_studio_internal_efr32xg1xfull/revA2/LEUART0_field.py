
from static import Base_RM_Field
from LEUART0_enum import *


class RM_Field_LEUART0_CTRL_AUTOTRI(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CTRL_AUTOTRI, self).__init__(register,
            'AUTOTRI', 'LEUART0.CTRL.AUTOTRI', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CTRL_DATABITS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CTRL_DATABITS, self).__init__(register,
            'DATABITS', 'LEUART0.CTRL.DATABITS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CTRL_PARITY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CTRL_PARITY, self).__init__(register,
            'PARITY', 'LEUART0.CTRL.PARITY', 'read-write',
            "",
            2, 2,
            RM_Enum_LEUART0_CTRL_PARITY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CTRL_STOPBITS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CTRL_STOPBITS, self).__init__(register,
            'STOPBITS', 'LEUART0.CTRL.STOPBITS', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CTRL_INV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CTRL_INV, self).__init__(register,
            'INV', 'LEUART0.CTRL.INV', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CTRL_ERRSDMA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CTRL_ERRSDMA, self).__init__(register,
            'ERRSDMA', 'LEUART0.CTRL.ERRSDMA', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CTRL_LOOPBK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CTRL_LOOPBK, self).__init__(register,
            'LOOPBK', 'LEUART0.CTRL.LOOPBK', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CTRL_SFUBRX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CTRL_SFUBRX, self).__init__(register,
            'SFUBRX', 'LEUART0.CTRL.SFUBRX', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CTRL_MPM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CTRL_MPM, self).__init__(register,
            'MPM', 'LEUART0.CTRL.MPM', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CTRL_MPAB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CTRL_MPAB, self).__init__(register,
            'MPAB', 'LEUART0.CTRL.MPAB', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CTRL_BIT8DV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CTRL_BIT8DV, self).__init__(register,
            'BIT8DV', 'LEUART0.CTRL.BIT8DV', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CTRL_RXDMAWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CTRL_RXDMAWU, self).__init__(register,
            'RXDMAWU', 'LEUART0.CTRL.RXDMAWU', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CTRL_TXDMAWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CTRL_TXDMAWU, self).__init__(register,
            'TXDMAWU', 'LEUART0.CTRL.TXDMAWU', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CTRL_TXDELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CTRL_TXDELAY, self).__init__(register,
            'TXDELAY', 'LEUART0.CTRL.TXDELAY', 'read-write',
            "",
            14, 2,
            RM_Enum_LEUART0_CTRL_TXDELAY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CMD_RXEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CMD_RXEN, self).__init__(register,
            'RXEN', 'LEUART0.CMD.RXEN', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CMD_RXDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CMD_RXDIS, self).__init__(register,
            'RXDIS', 'LEUART0.CMD.RXDIS', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CMD_TXEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CMD_TXEN, self).__init__(register,
            'TXEN', 'LEUART0.CMD.TXEN', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CMD_TXDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CMD_TXDIS, self).__init__(register,
            'TXDIS', 'LEUART0.CMD.TXDIS', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CMD_RXBLOCKEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CMD_RXBLOCKEN, self).__init__(register,
            'RXBLOCKEN', 'LEUART0.CMD.RXBLOCKEN', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CMD_RXBLOCKDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CMD_RXBLOCKDIS, self).__init__(register,
            'RXBLOCKDIS', 'LEUART0.CMD.RXBLOCKDIS', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CMD_CLEARTX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CMD_CLEARTX, self).__init__(register,
            'CLEARTX', 'LEUART0.CMD.CLEARTX', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CMD_CLEARRX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CMD_CLEARRX, self).__init__(register,
            'CLEARRX', 'LEUART0.CMD.CLEARRX', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_STATUS_RXENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_STATUS_RXENS, self).__init__(register,
            'RXENS', 'LEUART0.STATUS.RXENS', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_STATUS_TXENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_STATUS_TXENS, self).__init__(register,
            'TXENS', 'LEUART0.STATUS.TXENS', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_STATUS_RXBLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_STATUS_RXBLOCK, self).__init__(register,
            'RXBLOCK', 'LEUART0.STATUS.RXBLOCK', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_STATUS_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_STATUS_TXC, self).__init__(register,
            'TXC', 'LEUART0.STATUS.TXC', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_STATUS_TXBL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_STATUS_TXBL, self).__init__(register,
            'TXBL', 'LEUART0.STATUS.TXBL', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_STATUS_RXDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_STATUS_RXDATAV, self).__init__(register,
            'RXDATAV', 'LEUART0.STATUS.RXDATAV', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_STATUS_TXIDLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_STATUS_TXIDLE, self).__init__(register,
            'TXIDLE', 'LEUART0.STATUS.TXIDLE', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_CLKDIV_DIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_CLKDIV_DIV, self).__init__(register,
            'DIV', 'LEUART0.CLKDIV.DIV', 'read-write',
            "",
            3, 14)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_STARTFRAME_STARTFRAME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_STARTFRAME_STARTFRAME, self).__init__(register,
            'STARTFRAME', 'LEUART0.STARTFRAME.STARTFRAME', 'read-write',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_SIGFRAME_SIGFRAME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_SIGFRAME_SIGFRAME, self).__init__(register,
            'SIGFRAME', 'LEUART0.SIGFRAME.SIGFRAME', 'read-write',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_RXDATAX_RXDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_RXDATAX_RXDATA, self).__init__(register,
            'RXDATA', 'LEUART0.RXDATAX.RXDATA', 'read-only',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_RXDATAX_PERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_RXDATAX_PERR, self).__init__(register,
            'PERR', 'LEUART0.RXDATAX.PERR', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_RXDATAX_FERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_RXDATAX_FERR, self).__init__(register,
            'FERR', 'LEUART0.RXDATAX.FERR', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_RXDATA_RXDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_RXDATA_RXDATA, self).__init__(register,
            'RXDATA', 'LEUART0.RXDATA.RXDATA', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_RXDATAXP_RXDATAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_RXDATAXP_RXDATAP, self).__init__(register,
            'RXDATAP', 'LEUART0.RXDATAXP.RXDATAP', 'read-only',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_RXDATAXP_PERRP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_RXDATAXP_PERRP, self).__init__(register,
            'PERRP', 'LEUART0.RXDATAXP.PERRP', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_RXDATAXP_FERRP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_RXDATAXP_FERRP, self).__init__(register,
            'FERRP', 'LEUART0.RXDATAXP.FERRP', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_TXDATAX_TXDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_TXDATAX_TXDATA, self).__init__(register,
            'TXDATA', 'LEUART0.TXDATAX.TXDATA', 'read-write',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_TXDATAX_TXBREAK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_TXDATAX_TXBREAK, self).__init__(register,
            'TXBREAK', 'LEUART0.TXDATAX.TXBREAK', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_TXDATAX_TXDISAT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_TXDATAX_TXDISAT, self).__init__(register,
            'TXDISAT', 'LEUART0.TXDATAX.TXDISAT', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_TXDATAX_RXENAT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_TXDATAX_RXENAT, self).__init__(register,
            'RXENAT', 'LEUART0.TXDATAX.RXENAT', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_TXDATA_TXDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_TXDATA_TXDATA, self).__init__(register,
            'TXDATA', 'LEUART0.TXDATA.TXDATA', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IF_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IF_TXC, self).__init__(register,
            'TXC', 'LEUART0.IF.TXC', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IF_TXBL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IF_TXBL, self).__init__(register,
            'TXBL', 'LEUART0.IF.TXBL', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IF_RXDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IF_RXDATAV, self).__init__(register,
            'RXDATAV', 'LEUART0.IF.RXDATAV', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IF_RXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IF_RXOF, self).__init__(register,
            'RXOF', 'LEUART0.IF.RXOF', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IF_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IF_RXUF, self).__init__(register,
            'RXUF', 'LEUART0.IF.RXUF', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IF_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IF_TXOF, self).__init__(register,
            'TXOF', 'LEUART0.IF.TXOF', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IF_PERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IF_PERR, self).__init__(register,
            'PERR', 'LEUART0.IF.PERR', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IF_FERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IF_FERR, self).__init__(register,
            'FERR', 'LEUART0.IF.FERR', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IF_MPAF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IF_MPAF, self).__init__(register,
            'MPAF', 'LEUART0.IF.MPAF', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IF_STARTF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IF_STARTF, self).__init__(register,
            'STARTF', 'LEUART0.IF.STARTF', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IF_SIGF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IF_SIGF, self).__init__(register,
            'SIGF', 'LEUART0.IF.SIGF', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFS_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFS_TXC, self).__init__(register,
            'TXC', 'LEUART0.IFS.TXC', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFS_RXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFS_RXOF, self).__init__(register,
            'RXOF', 'LEUART0.IFS.RXOF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFS_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFS_RXUF, self).__init__(register,
            'RXUF', 'LEUART0.IFS.RXUF', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFS_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFS_TXOF, self).__init__(register,
            'TXOF', 'LEUART0.IFS.TXOF', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFS_PERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFS_PERR, self).__init__(register,
            'PERR', 'LEUART0.IFS.PERR', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFS_FERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFS_FERR, self).__init__(register,
            'FERR', 'LEUART0.IFS.FERR', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFS_MPAF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFS_MPAF, self).__init__(register,
            'MPAF', 'LEUART0.IFS.MPAF', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFS_STARTF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFS_STARTF, self).__init__(register,
            'STARTF', 'LEUART0.IFS.STARTF', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFS_SIGF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFS_SIGF, self).__init__(register,
            'SIGF', 'LEUART0.IFS.SIGF', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFC_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFC_TXC, self).__init__(register,
            'TXC', 'LEUART0.IFC.TXC', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFC_RXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFC_RXOF, self).__init__(register,
            'RXOF', 'LEUART0.IFC.RXOF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFC_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFC_RXUF, self).__init__(register,
            'RXUF', 'LEUART0.IFC.RXUF', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFC_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFC_TXOF, self).__init__(register,
            'TXOF', 'LEUART0.IFC.TXOF', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFC_PERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFC_PERR, self).__init__(register,
            'PERR', 'LEUART0.IFC.PERR', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFC_FERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFC_FERR, self).__init__(register,
            'FERR', 'LEUART0.IFC.FERR', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFC_MPAF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFC_MPAF, self).__init__(register,
            'MPAF', 'LEUART0.IFC.MPAF', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFC_STARTF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFC_STARTF, self).__init__(register,
            'STARTF', 'LEUART0.IFC.STARTF', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IFC_SIGF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IFC_SIGF, self).__init__(register,
            'SIGF', 'LEUART0.IFC.SIGF', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IEN_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IEN_TXC, self).__init__(register,
            'TXC', 'LEUART0.IEN.TXC', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IEN_TXBL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IEN_TXBL, self).__init__(register,
            'TXBL', 'LEUART0.IEN.TXBL', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IEN_RXDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IEN_RXDATAV, self).__init__(register,
            'RXDATAV', 'LEUART0.IEN.RXDATAV', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IEN_RXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IEN_RXOF, self).__init__(register,
            'RXOF', 'LEUART0.IEN.RXOF', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IEN_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IEN_RXUF, self).__init__(register,
            'RXUF', 'LEUART0.IEN.RXUF', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IEN_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IEN_TXOF, self).__init__(register,
            'TXOF', 'LEUART0.IEN.TXOF', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IEN_PERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IEN_PERR, self).__init__(register,
            'PERR', 'LEUART0.IEN.PERR', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IEN_FERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IEN_FERR, self).__init__(register,
            'FERR', 'LEUART0.IEN.FERR', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IEN_MPAF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IEN_MPAF, self).__init__(register,
            'MPAF', 'LEUART0.IEN.MPAF', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IEN_STARTF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IEN_STARTF, self).__init__(register,
            'STARTF', 'LEUART0.IEN.STARTF', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_IEN_SIGF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_IEN_SIGF, self).__init__(register,
            'SIGF', 'LEUART0.IEN.SIGF', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_PULSECTRL_PULSEW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_PULSECTRL_PULSEW, self).__init__(register,
            'PULSEW', 'LEUART0.PULSECTRL.PULSEW', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_PULSECTRL_PULSEEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_PULSECTRL_PULSEEN, self).__init__(register,
            'PULSEEN', 'LEUART0.PULSECTRL.PULSEEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_PULSECTRL_PULSEFILT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_PULSECTRL_PULSEFILT, self).__init__(register,
            'PULSEFILT', 'LEUART0.PULSECTRL.PULSEFILT', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_FREEZE_REGFREEZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_FREEZE_REGFREEZE, self).__init__(register,
            'REGFREEZE', 'LEUART0.FREEZE.REGFREEZE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_SYNCBUSY_CTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_SYNCBUSY_CTRL, self).__init__(register,
            'CTRL', 'LEUART0.SYNCBUSY.CTRL', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_SYNCBUSY_CMD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_SYNCBUSY_CMD, self).__init__(register,
            'CMD', 'LEUART0.SYNCBUSY.CMD', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_SYNCBUSY_CLKDIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_SYNCBUSY_CLKDIV, self).__init__(register,
            'CLKDIV', 'LEUART0.SYNCBUSY.CLKDIV', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_SYNCBUSY_STARTFRAME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_SYNCBUSY_STARTFRAME, self).__init__(register,
            'STARTFRAME', 'LEUART0.SYNCBUSY.STARTFRAME', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_SYNCBUSY_SIGFRAME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_SYNCBUSY_SIGFRAME, self).__init__(register,
            'SIGFRAME', 'LEUART0.SYNCBUSY.SIGFRAME', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_SYNCBUSY_TXDATAX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_SYNCBUSY_TXDATAX, self).__init__(register,
            'TXDATAX', 'LEUART0.SYNCBUSY.TXDATAX', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_SYNCBUSY_TXDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_SYNCBUSY_TXDATA, self).__init__(register,
            'TXDATA', 'LEUART0.SYNCBUSY.TXDATA', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_SYNCBUSY_PULSECTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_SYNCBUSY_PULSECTRL, self).__init__(register,
            'PULSECTRL', 'LEUART0.SYNCBUSY.PULSECTRL', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_ROUTEPEN_RXPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_ROUTEPEN_RXPEN, self).__init__(register,
            'RXPEN', 'LEUART0.ROUTEPEN.RXPEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_ROUTEPEN_TXPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_ROUTEPEN_TXPEN, self).__init__(register,
            'TXPEN', 'LEUART0.ROUTEPEN.TXPEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_ROUTELOC0_RXLOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_ROUTELOC0_RXLOC, self).__init__(register,
            'RXLOC', 'LEUART0.ROUTELOC0.RXLOC', 'read-write',
            "",
            0, 6,
            RM_Enum_LEUART0_ROUTELOC0_RXLOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_ROUTELOC0_TXLOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_ROUTELOC0_TXLOC, self).__init__(register,
            'TXLOC', 'LEUART0.ROUTELOC0.TXLOC', 'read-write',
            "",
            8, 6,
            RM_Enum_LEUART0_ROUTELOC0_TXLOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_INPUT_RXPRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_INPUT_RXPRSSEL, self).__init__(register,
            'RXPRSSEL', 'LEUART0.INPUT.RXPRSSEL', 'read-write',
            "",
            0, 4,
            RM_Enum_LEUART0_INPUT_RXPRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LEUART0_INPUT_RXPRS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LEUART0_INPUT_RXPRS, self).__init__(register,
            'RXPRS', 'LEUART0.INPUT.RXPRS', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


