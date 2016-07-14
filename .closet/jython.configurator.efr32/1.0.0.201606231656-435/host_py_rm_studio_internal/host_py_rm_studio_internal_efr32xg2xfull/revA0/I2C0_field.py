
from static import Base_RM_Field
from I2C0_enum import *


class RM_Field_I2C0_CTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CTRL_EN, self).__init__(register,
            'EN', 'I2C0.CTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CTRL_SLAVE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CTRL_SLAVE, self).__init__(register,
            'SLAVE', 'I2C0.CTRL.SLAVE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CTRL_AUTOACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CTRL_AUTOACK, self).__init__(register,
            'AUTOACK', 'I2C0.CTRL.AUTOACK', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CTRL_AUTOSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CTRL_AUTOSE, self).__init__(register,
            'AUTOSE', 'I2C0.CTRL.AUTOSE', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CTRL_AUTOSN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CTRL_AUTOSN, self).__init__(register,
            'AUTOSN', 'I2C0.CTRL.AUTOSN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CTRL_ARBDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CTRL_ARBDIS, self).__init__(register,
            'ARBDIS', 'I2C0.CTRL.ARBDIS', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CTRL_GCAMEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CTRL_GCAMEN, self).__init__(register,
            'GCAMEN', 'I2C0.CTRL.GCAMEN', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CTRL_TXBIL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CTRL_TXBIL, self).__init__(register,
            'TXBIL', 'I2C0.CTRL.TXBIL', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CTRL_CLHR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CTRL_CLHR, self).__init__(register,
            'CLHR', 'I2C0.CTRL.CLHR', 'read-write',
            "",
            8, 2,
            RM_Enum_I2C0_CTRL_CLHR(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CTRL_BITO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CTRL_BITO, self).__init__(register,
            'BITO', 'I2C0.CTRL.BITO', 'read-write',
            "",
            12, 2,
            RM_Enum_I2C0_CTRL_BITO(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CTRL_GIBITO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CTRL_GIBITO, self).__init__(register,
            'GIBITO', 'I2C0.CTRL.GIBITO', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CTRL_CLTO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CTRL_CLTO, self).__init__(register,
            'CLTO', 'I2C0.CTRL.CLTO', 'read-write',
            "",
            16, 3,
            RM_Enum_I2C0_CTRL_CLTO(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CMD_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CMD_START, self).__init__(register,
            'START', 'I2C0.CMD.START', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CMD_STOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CMD_STOP, self).__init__(register,
            'STOP', 'I2C0.CMD.STOP', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CMD_ACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CMD_ACK, self).__init__(register,
            'ACK', 'I2C0.CMD.ACK', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CMD_NACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CMD_NACK, self).__init__(register,
            'NACK', 'I2C0.CMD.NACK', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CMD_CONT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CMD_CONT, self).__init__(register,
            'CONT', 'I2C0.CMD.CONT', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CMD_ABORT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CMD_ABORT, self).__init__(register,
            'ABORT', 'I2C0.CMD.ABORT', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CMD_CLEARTX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CMD_CLEARTX, self).__init__(register,
            'CLEARTX', 'I2C0.CMD.CLEARTX', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CMD_CLEARPC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CMD_CLEARPC, self).__init__(register,
            'CLEARPC', 'I2C0.CMD.CLEARPC', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATE_BUSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATE_BUSY, self).__init__(register,
            'BUSY', 'I2C0.STATE.BUSY', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATE_MASTER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATE_MASTER, self).__init__(register,
            'MASTER', 'I2C0.STATE.MASTER', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATE_TRANSMITTER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATE_TRANSMITTER, self).__init__(register,
            'TRANSMITTER', 'I2C0.STATE.TRANSMITTER', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATE_NACKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATE_NACKED, self).__init__(register,
            'NACKED', 'I2C0.STATE.NACKED', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATE_BUSHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATE_BUSHOLD, self).__init__(register,
            'BUSHOLD', 'I2C0.STATE.BUSHOLD', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATE_STATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATE_STATE, self).__init__(register,
            'STATE', 'I2C0.STATE.STATE', 'read-only',
            "",
            5, 3,
            RM_Enum_I2C0_STATE_STATE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATUS_PSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATUS_PSTART, self).__init__(register,
            'PSTART', 'I2C0.STATUS.PSTART', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATUS_PSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATUS_PSTOP, self).__init__(register,
            'PSTOP', 'I2C0.STATUS.PSTOP', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATUS_PACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATUS_PACK, self).__init__(register,
            'PACK', 'I2C0.STATUS.PACK', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATUS_PNACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATUS_PNACK, self).__init__(register,
            'PNACK', 'I2C0.STATUS.PNACK', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATUS_PCONT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATUS_PCONT, self).__init__(register,
            'PCONT', 'I2C0.STATUS.PCONT', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATUS_PABORT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATUS_PABORT, self).__init__(register,
            'PABORT', 'I2C0.STATUS.PABORT', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATUS_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATUS_TXC, self).__init__(register,
            'TXC', 'I2C0.STATUS.TXC', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATUS_TXBL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATUS_TXBL, self).__init__(register,
            'TXBL', 'I2C0.STATUS.TXBL', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATUS_RXDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATUS_RXDATAV, self).__init__(register,
            'RXDATAV', 'I2C0.STATUS.RXDATAV', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_STATUS_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_STATUS_RXFULL, self).__init__(register,
            'RXFULL', 'I2C0.STATUS.RXFULL', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_CLKDIV_DIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_CLKDIV_DIV, self).__init__(register,
            'DIV', 'I2C0.CLKDIV.DIV', 'read-write',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_SADDR_ADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_SADDR_ADDR, self).__init__(register,
            'ADDR', 'I2C0.SADDR.ADDR', 'read-write',
            "",
            1, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_SADDRMASK_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_SADDRMASK_MASK, self).__init__(register,
            'MASK', 'I2C0.SADDRMASK.MASK', 'read-write',
            "",
            1, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_RXDATA_RXDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_RXDATA_RXDATA, self).__init__(register,
            'RXDATA', 'I2C0.RXDATA.RXDATA', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_RXDOUBLE_RXDATA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_RXDOUBLE_RXDATA0, self).__init__(register,
            'RXDATA0', 'I2C0.RXDOUBLE.RXDATA0', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_RXDOUBLE_RXDATA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_RXDOUBLE_RXDATA1, self).__init__(register,
            'RXDATA1', 'I2C0.RXDOUBLE.RXDATA1', 'read-only',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_RXDATAP_RXDATAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_RXDATAP_RXDATAP, self).__init__(register,
            'RXDATAP', 'I2C0.RXDATAP.RXDATAP', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_RXDOUBLEP_RXDATAP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_RXDOUBLEP_RXDATAP0, self).__init__(register,
            'RXDATAP0', 'I2C0.RXDOUBLEP.RXDATAP0', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_RXDOUBLEP_RXDATAP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_RXDOUBLEP_RXDATAP1, self).__init__(register,
            'RXDATAP1', 'I2C0.RXDOUBLEP.RXDATAP1', 'read-only',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_TXDATA_TXDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_TXDATA_TXDATA, self).__init__(register,
            'TXDATA', 'I2C0.TXDATA.TXDATA', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_TXDOUBLE_TXDATA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_TXDOUBLE_TXDATA0, self).__init__(register,
            'TXDATA0', 'I2C0.TXDOUBLE.TXDATA0', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_TXDOUBLE_TXDATA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_TXDOUBLE_TXDATA1, self).__init__(register,
            'TXDATA1', 'I2C0.TXDOUBLE.TXDATA1', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_START, self).__init__(register,
            'START', 'I2C0.IF.START', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_RSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_RSTART, self).__init__(register,
            'RSTART', 'I2C0.IF.RSTART', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_ADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_ADDR, self).__init__(register,
            'ADDR', 'I2C0.IF.ADDR', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_TXC, self).__init__(register,
            'TXC', 'I2C0.IF.TXC', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_TXBL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_TXBL, self).__init__(register,
            'TXBL', 'I2C0.IF.TXBL', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_RXDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_RXDATAV, self).__init__(register,
            'RXDATAV', 'I2C0.IF.RXDATAV', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_ACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_ACK, self).__init__(register,
            'ACK', 'I2C0.IF.ACK', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_NACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_NACK, self).__init__(register,
            'NACK', 'I2C0.IF.NACK', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_MSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_MSTOP, self).__init__(register,
            'MSTOP', 'I2C0.IF.MSTOP', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_ARBLOST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_ARBLOST, self).__init__(register,
            'ARBLOST', 'I2C0.IF.ARBLOST', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_BUSERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_BUSERR, self).__init__(register,
            'BUSERR', 'I2C0.IF.BUSERR', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_BUSHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_BUSHOLD, self).__init__(register,
            'BUSHOLD', 'I2C0.IF.BUSHOLD', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_TXOF, self).__init__(register,
            'TXOF', 'I2C0.IF.TXOF', 'read-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_RXUF, self).__init__(register,
            'RXUF', 'I2C0.IF.RXUF', 'read-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_BITO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_BITO, self).__init__(register,
            'BITO', 'I2C0.IF.BITO', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_CLTO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_CLTO, self).__init__(register,
            'CLTO', 'I2C0.IF.CLTO', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_SSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_SSTOP, self).__init__(register,
            'SSTOP', 'I2C0.IF.SSTOP', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_RXFULL, self).__init__(register,
            'RXFULL', 'I2C0.IF.RXFULL', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IF_CLERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IF_CLERR, self).__init__(register,
            'CLERR', 'I2C0.IF.CLERR', 'read-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_START, self).__init__(register,
            'START', 'I2C0.IFS.START', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_RSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_RSTART, self).__init__(register,
            'RSTART', 'I2C0.IFS.RSTART', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_ADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_ADDR, self).__init__(register,
            'ADDR', 'I2C0.IFS.ADDR', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_TXC, self).__init__(register,
            'TXC', 'I2C0.IFS.TXC', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_ACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_ACK, self).__init__(register,
            'ACK', 'I2C0.IFS.ACK', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_NACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_NACK, self).__init__(register,
            'NACK', 'I2C0.IFS.NACK', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_MSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_MSTOP, self).__init__(register,
            'MSTOP', 'I2C0.IFS.MSTOP', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_ARBLOST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_ARBLOST, self).__init__(register,
            'ARBLOST', 'I2C0.IFS.ARBLOST', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_BUSERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_BUSERR, self).__init__(register,
            'BUSERR', 'I2C0.IFS.BUSERR', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_BUSHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_BUSHOLD, self).__init__(register,
            'BUSHOLD', 'I2C0.IFS.BUSHOLD', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_TXOF, self).__init__(register,
            'TXOF', 'I2C0.IFS.TXOF', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_RXUF, self).__init__(register,
            'RXUF', 'I2C0.IFS.RXUF', 'write-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_BITO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_BITO, self).__init__(register,
            'BITO', 'I2C0.IFS.BITO', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_CLTO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_CLTO, self).__init__(register,
            'CLTO', 'I2C0.IFS.CLTO', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_SSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_SSTOP, self).__init__(register,
            'SSTOP', 'I2C0.IFS.SSTOP', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_RXFULL, self).__init__(register,
            'RXFULL', 'I2C0.IFS.RXFULL', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFS_CLERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFS_CLERR, self).__init__(register,
            'CLERR', 'I2C0.IFS.CLERR', 'write-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_START, self).__init__(register,
            'START', 'I2C0.IFC.START', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_RSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_RSTART, self).__init__(register,
            'RSTART', 'I2C0.IFC.RSTART', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_ADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_ADDR, self).__init__(register,
            'ADDR', 'I2C0.IFC.ADDR', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_TXC, self).__init__(register,
            'TXC', 'I2C0.IFC.TXC', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_ACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_ACK, self).__init__(register,
            'ACK', 'I2C0.IFC.ACK', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_NACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_NACK, self).__init__(register,
            'NACK', 'I2C0.IFC.NACK', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_MSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_MSTOP, self).__init__(register,
            'MSTOP', 'I2C0.IFC.MSTOP', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_ARBLOST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_ARBLOST, self).__init__(register,
            'ARBLOST', 'I2C0.IFC.ARBLOST', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_BUSERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_BUSERR, self).__init__(register,
            'BUSERR', 'I2C0.IFC.BUSERR', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_BUSHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_BUSHOLD, self).__init__(register,
            'BUSHOLD', 'I2C0.IFC.BUSHOLD', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_TXOF, self).__init__(register,
            'TXOF', 'I2C0.IFC.TXOF', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_RXUF, self).__init__(register,
            'RXUF', 'I2C0.IFC.RXUF', 'write-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_BITO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_BITO, self).__init__(register,
            'BITO', 'I2C0.IFC.BITO', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_CLTO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_CLTO, self).__init__(register,
            'CLTO', 'I2C0.IFC.CLTO', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_SSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_SSTOP, self).__init__(register,
            'SSTOP', 'I2C0.IFC.SSTOP', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_RXFULL, self).__init__(register,
            'RXFULL', 'I2C0.IFC.RXFULL', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IFC_CLERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IFC_CLERR, self).__init__(register,
            'CLERR', 'I2C0.IFC.CLERR', 'write-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_START, self).__init__(register,
            'START', 'I2C0.IEN.START', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_RSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_RSTART, self).__init__(register,
            'RSTART', 'I2C0.IEN.RSTART', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_ADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_ADDR, self).__init__(register,
            'ADDR', 'I2C0.IEN.ADDR', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_TXC, self).__init__(register,
            'TXC', 'I2C0.IEN.TXC', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_TXBL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_TXBL, self).__init__(register,
            'TXBL', 'I2C0.IEN.TXBL', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_RXDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_RXDATAV, self).__init__(register,
            'RXDATAV', 'I2C0.IEN.RXDATAV', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_ACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_ACK, self).__init__(register,
            'ACK', 'I2C0.IEN.ACK', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_NACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_NACK, self).__init__(register,
            'NACK', 'I2C0.IEN.NACK', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_MSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_MSTOP, self).__init__(register,
            'MSTOP', 'I2C0.IEN.MSTOP', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_ARBLOST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_ARBLOST, self).__init__(register,
            'ARBLOST', 'I2C0.IEN.ARBLOST', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_BUSERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_BUSERR, self).__init__(register,
            'BUSERR', 'I2C0.IEN.BUSERR', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_BUSHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_BUSHOLD, self).__init__(register,
            'BUSHOLD', 'I2C0.IEN.BUSHOLD', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_TXOF, self).__init__(register,
            'TXOF', 'I2C0.IEN.TXOF', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_RXUF, self).__init__(register,
            'RXUF', 'I2C0.IEN.RXUF', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_BITO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_BITO, self).__init__(register,
            'BITO', 'I2C0.IEN.BITO', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_CLTO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_CLTO, self).__init__(register,
            'CLTO', 'I2C0.IEN.CLTO', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_SSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_SSTOP, self).__init__(register,
            'SSTOP', 'I2C0.IEN.SSTOP', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_RXFULL, self).__init__(register,
            'RXFULL', 'I2C0.IEN.RXFULL', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_IEN_CLERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_IEN_CLERR, self).__init__(register,
            'CLERR', 'I2C0.IEN.CLERR', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_ROUTEPEN_SDAPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_ROUTEPEN_SDAPEN, self).__init__(register,
            'SDAPEN', 'I2C0.ROUTEPEN.SDAPEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_ROUTEPEN_SCLPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_ROUTEPEN_SCLPEN, self).__init__(register,
            'SCLPEN', 'I2C0.ROUTEPEN.SCLPEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_ROUTELOC0_SDALOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_ROUTELOC0_SDALOC, self).__init__(register,
            'SDALOC', 'I2C0.ROUTELOC0.SDALOC', 'read-write',
            "",
            0, 6,
            RM_Enum_I2C0_ROUTELOC0_SDALOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C0_ROUTELOC0_SCLLOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C0_ROUTELOC0_SCLLOC, self).__init__(register,
            'SCLLOC', 'I2C0.ROUTELOC0.SCLLOC', 'read-write',
            "",
            8, 6,
            RM_Enum_I2C0_ROUTELOC0_SCLLOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


