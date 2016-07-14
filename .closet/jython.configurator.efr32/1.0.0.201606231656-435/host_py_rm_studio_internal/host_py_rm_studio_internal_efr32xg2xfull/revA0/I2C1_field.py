
from static import Base_RM_Field
from I2C1_enum import *


class RM_Field_I2C1_CTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CTRL_EN, self).__init__(register,
            'EN', 'I2C1.CTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CTRL_SLAVE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CTRL_SLAVE, self).__init__(register,
            'SLAVE', 'I2C1.CTRL.SLAVE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CTRL_AUTOACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CTRL_AUTOACK, self).__init__(register,
            'AUTOACK', 'I2C1.CTRL.AUTOACK', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CTRL_AUTOSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CTRL_AUTOSE, self).__init__(register,
            'AUTOSE', 'I2C1.CTRL.AUTOSE', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CTRL_AUTOSN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CTRL_AUTOSN, self).__init__(register,
            'AUTOSN', 'I2C1.CTRL.AUTOSN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CTRL_ARBDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CTRL_ARBDIS, self).__init__(register,
            'ARBDIS', 'I2C1.CTRL.ARBDIS', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CTRL_GCAMEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CTRL_GCAMEN, self).__init__(register,
            'GCAMEN', 'I2C1.CTRL.GCAMEN', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CTRL_TXBIL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CTRL_TXBIL, self).__init__(register,
            'TXBIL', 'I2C1.CTRL.TXBIL', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CTRL_CLHR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CTRL_CLHR, self).__init__(register,
            'CLHR', 'I2C1.CTRL.CLHR', 'read-write',
            "",
            8, 2,
            RM_Enum_I2C1_CTRL_CLHR(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CTRL_BITO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CTRL_BITO, self).__init__(register,
            'BITO', 'I2C1.CTRL.BITO', 'read-write',
            "",
            12, 2,
            RM_Enum_I2C1_CTRL_BITO(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CTRL_GIBITO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CTRL_GIBITO, self).__init__(register,
            'GIBITO', 'I2C1.CTRL.GIBITO', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CTRL_CLTO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CTRL_CLTO, self).__init__(register,
            'CLTO', 'I2C1.CTRL.CLTO', 'read-write',
            "",
            16, 3,
            RM_Enum_I2C1_CTRL_CLTO(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CMD_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CMD_START, self).__init__(register,
            'START', 'I2C1.CMD.START', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CMD_STOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CMD_STOP, self).__init__(register,
            'STOP', 'I2C1.CMD.STOP', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CMD_ACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CMD_ACK, self).__init__(register,
            'ACK', 'I2C1.CMD.ACK', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CMD_NACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CMD_NACK, self).__init__(register,
            'NACK', 'I2C1.CMD.NACK', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CMD_CONT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CMD_CONT, self).__init__(register,
            'CONT', 'I2C1.CMD.CONT', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CMD_ABORT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CMD_ABORT, self).__init__(register,
            'ABORT', 'I2C1.CMD.ABORT', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CMD_CLEARTX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CMD_CLEARTX, self).__init__(register,
            'CLEARTX', 'I2C1.CMD.CLEARTX', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CMD_CLEARPC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CMD_CLEARPC, self).__init__(register,
            'CLEARPC', 'I2C1.CMD.CLEARPC', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATE_BUSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATE_BUSY, self).__init__(register,
            'BUSY', 'I2C1.STATE.BUSY', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATE_MASTER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATE_MASTER, self).__init__(register,
            'MASTER', 'I2C1.STATE.MASTER', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATE_TRANSMITTER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATE_TRANSMITTER, self).__init__(register,
            'TRANSMITTER', 'I2C1.STATE.TRANSMITTER', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATE_NACKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATE_NACKED, self).__init__(register,
            'NACKED', 'I2C1.STATE.NACKED', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATE_BUSHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATE_BUSHOLD, self).__init__(register,
            'BUSHOLD', 'I2C1.STATE.BUSHOLD', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATE_STATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATE_STATE, self).__init__(register,
            'STATE', 'I2C1.STATE.STATE', 'read-only',
            "",
            5, 3,
            RM_Enum_I2C1_STATE_STATE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATUS_PSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATUS_PSTART, self).__init__(register,
            'PSTART', 'I2C1.STATUS.PSTART', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATUS_PSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATUS_PSTOP, self).__init__(register,
            'PSTOP', 'I2C1.STATUS.PSTOP', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATUS_PACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATUS_PACK, self).__init__(register,
            'PACK', 'I2C1.STATUS.PACK', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATUS_PNACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATUS_PNACK, self).__init__(register,
            'PNACK', 'I2C1.STATUS.PNACK', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATUS_PCONT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATUS_PCONT, self).__init__(register,
            'PCONT', 'I2C1.STATUS.PCONT', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATUS_PABORT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATUS_PABORT, self).__init__(register,
            'PABORT', 'I2C1.STATUS.PABORT', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATUS_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATUS_TXC, self).__init__(register,
            'TXC', 'I2C1.STATUS.TXC', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATUS_TXBL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATUS_TXBL, self).__init__(register,
            'TXBL', 'I2C1.STATUS.TXBL', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATUS_RXDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATUS_RXDATAV, self).__init__(register,
            'RXDATAV', 'I2C1.STATUS.RXDATAV', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_STATUS_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_STATUS_RXFULL, self).__init__(register,
            'RXFULL', 'I2C1.STATUS.RXFULL', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_CLKDIV_DIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_CLKDIV_DIV, self).__init__(register,
            'DIV', 'I2C1.CLKDIV.DIV', 'read-write',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_SADDR_ADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_SADDR_ADDR, self).__init__(register,
            'ADDR', 'I2C1.SADDR.ADDR', 'read-write',
            "",
            1, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_SADDRMASK_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_SADDRMASK_MASK, self).__init__(register,
            'MASK', 'I2C1.SADDRMASK.MASK', 'read-write',
            "",
            1, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_RXDATA_RXDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_RXDATA_RXDATA, self).__init__(register,
            'RXDATA', 'I2C1.RXDATA.RXDATA', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_RXDOUBLE_RXDATA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_RXDOUBLE_RXDATA0, self).__init__(register,
            'RXDATA0', 'I2C1.RXDOUBLE.RXDATA0', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_RXDOUBLE_RXDATA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_RXDOUBLE_RXDATA1, self).__init__(register,
            'RXDATA1', 'I2C1.RXDOUBLE.RXDATA1', 'read-only',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_RXDATAP_RXDATAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_RXDATAP_RXDATAP, self).__init__(register,
            'RXDATAP', 'I2C1.RXDATAP.RXDATAP', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_RXDOUBLEP_RXDATAP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_RXDOUBLEP_RXDATAP0, self).__init__(register,
            'RXDATAP0', 'I2C1.RXDOUBLEP.RXDATAP0', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_RXDOUBLEP_RXDATAP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_RXDOUBLEP_RXDATAP1, self).__init__(register,
            'RXDATAP1', 'I2C1.RXDOUBLEP.RXDATAP1', 'read-only',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_TXDATA_TXDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_TXDATA_TXDATA, self).__init__(register,
            'TXDATA', 'I2C1.TXDATA.TXDATA', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_TXDOUBLE_TXDATA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_TXDOUBLE_TXDATA0, self).__init__(register,
            'TXDATA0', 'I2C1.TXDOUBLE.TXDATA0', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_TXDOUBLE_TXDATA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_TXDOUBLE_TXDATA1, self).__init__(register,
            'TXDATA1', 'I2C1.TXDOUBLE.TXDATA1', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_START, self).__init__(register,
            'START', 'I2C1.IF.START', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_RSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_RSTART, self).__init__(register,
            'RSTART', 'I2C1.IF.RSTART', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_ADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_ADDR, self).__init__(register,
            'ADDR', 'I2C1.IF.ADDR', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_TXC, self).__init__(register,
            'TXC', 'I2C1.IF.TXC', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_TXBL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_TXBL, self).__init__(register,
            'TXBL', 'I2C1.IF.TXBL', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_RXDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_RXDATAV, self).__init__(register,
            'RXDATAV', 'I2C1.IF.RXDATAV', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_ACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_ACK, self).__init__(register,
            'ACK', 'I2C1.IF.ACK', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_NACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_NACK, self).__init__(register,
            'NACK', 'I2C1.IF.NACK', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_MSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_MSTOP, self).__init__(register,
            'MSTOP', 'I2C1.IF.MSTOP', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_ARBLOST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_ARBLOST, self).__init__(register,
            'ARBLOST', 'I2C1.IF.ARBLOST', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_BUSERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_BUSERR, self).__init__(register,
            'BUSERR', 'I2C1.IF.BUSERR', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_BUSHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_BUSHOLD, self).__init__(register,
            'BUSHOLD', 'I2C1.IF.BUSHOLD', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_TXOF, self).__init__(register,
            'TXOF', 'I2C1.IF.TXOF', 'read-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_RXUF, self).__init__(register,
            'RXUF', 'I2C1.IF.RXUF', 'read-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_BITO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_BITO, self).__init__(register,
            'BITO', 'I2C1.IF.BITO', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_CLTO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_CLTO, self).__init__(register,
            'CLTO', 'I2C1.IF.CLTO', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_SSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_SSTOP, self).__init__(register,
            'SSTOP', 'I2C1.IF.SSTOP', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_RXFULL, self).__init__(register,
            'RXFULL', 'I2C1.IF.RXFULL', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IF_CLERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IF_CLERR, self).__init__(register,
            'CLERR', 'I2C1.IF.CLERR', 'read-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_START, self).__init__(register,
            'START', 'I2C1.IFS.START', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_RSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_RSTART, self).__init__(register,
            'RSTART', 'I2C1.IFS.RSTART', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_ADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_ADDR, self).__init__(register,
            'ADDR', 'I2C1.IFS.ADDR', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_TXC, self).__init__(register,
            'TXC', 'I2C1.IFS.TXC', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_ACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_ACK, self).__init__(register,
            'ACK', 'I2C1.IFS.ACK', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_NACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_NACK, self).__init__(register,
            'NACK', 'I2C1.IFS.NACK', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_MSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_MSTOP, self).__init__(register,
            'MSTOP', 'I2C1.IFS.MSTOP', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_ARBLOST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_ARBLOST, self).__init__(register,
            'ARBLOST', 'I2C1.IFS.ARBLOST', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_BUSERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_BUSERR, self).__init__(register,
            'BUSERR', 'I2C1.IFS.BUSERR', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_BUSHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_BUSHOLD, self).__init__(register,
            'BUSHOLD', 'I2C1.IFS.BUSHOLD', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_TXOF, self).__init__(register,
            'TXOF', 'I2C1.IFS.TXOF', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_RXUF, self).__init__(register,
            'RXUF', 'I2C1.IFS.RXUF', 'write-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_BITO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_BITO, self).__init__(register,
            'BITO', 'I2C1.IFS.BITO', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_CLTO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_CLTO, self).__init__(register,
            'CLTO', 'I2C1.IFS.CLTO', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_SSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_SSTOP, self).__init__(register,
            'SSTOP', 'I2C1.IFS.SSTOP', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_RXFULL, self).__init__(register,
            'RXFULL', 'I2C1.IFS.RXFULL', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFS_CLERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFS_CLERR, self).__init__(register,
            'CLERR', 'I2C1.IFS.CLERR', 'write-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_START, self).__init__(register,
            'START', 'I2C1.IFC.START', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_RSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_RSTART, self).__init__(register,
            'RSTART', 'I2C1.IFC.RSTART', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_ADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_ADDR, self).__init__(register,
            'ADDR', 'I2C1.IFC.ADDR', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_TXC, self).__init__(register,
            'TXC', 'I2C1.IFC.TXC', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_ACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_ACK, self).__init__(register,
            'ACK', 'I2C1.IFC.ACK', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_NACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_NACK, self).__init__(register,
            'NACK', 'I2C1.IFC.NACK', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_MSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_MSTOP, self).__init__(register,
            'MSTOP', 'I2C1.IFC.MSTOP', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_ARBLOST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_ARBLOST, self).__init__(register,
            'ARBLOST', 'I2C1.IFC.ARBLOST', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_BUSERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_BUSERR, self).__init__(register,
            'BUSERR', 'I2C1.IFC.BUSERR', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_BUSHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_BUSHOLD, self).__init__(register,
            'BUSHOLD', 'I2C1.IFC.BUSHOLD', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_TXOF, self).__init__(register,
            'TXOF', 'I2C1.IFC.TXOF', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_RXUF, self).__init__(register,
            'RXUF', 'I2C1.IFC.RXUF', 'write-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_BITO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_BITO, self).__init__(register,
            'BITO', 'I2C1.IFC.BITO', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_CLTO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_CLTO, self).__init__(register,
            'CLTO', 'I2C1.IFC.CLTO', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_SSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_SSTOP, self).__init__(register,
            'SSTOP', 'I2C1.IFC.SSTOP', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_RXFULL, self).__init__(register,
            'RXFULL', 'I2C1.IFC.RXFULL', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IFC_CLERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IFC_CLERR, self).__init__(register,
            'CLERR', 'I2C1.IFC.CLERR', 'write-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_START, self).__init__(register,
            'START', 'I2C1.IEN.START', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_RSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_RSTART, self).__init__(register,
            'RSTART', 'I2C1.IEN.RSTART', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_ADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_ADDR, self).__init__(register,
            'ADDR', 'I2C1.IEN.ADDR', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_TXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_TXC, self).__init__(register,
            'TXC', 'I2C1.IEN.TXC', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_TXBL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_TXBL, self).__init__(register,
            'TXBL', 'I2C1.IEN.TXBL', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_RXDATAV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_RXDATAV, self).__init__(register,
            'RXDATAV', 'I2C1.IEN.RXDATAV', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_ACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_ACK, self).__init__(register,
            'ACK', 'I2C1.IEN.ACK', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_NACK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_NACK, self).__init__(register,
            'NACK', 'I2C1.IEN.NACK', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_MSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_MSTOP, self).__init__(register,
            'MSTOP', 'I2C1.IEN.MSTOP', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_ARBLOST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_ARBLOST, self).__init__(register,
            'ARBLOST', 'I2C1.IEN.ARBLOST', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_BUSERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_BUSERR, self).__init__(register,
            'BUSERR', 'I2C1.IEN.BUSERR', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_BUSHOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_BUSHOLD, self).__init__(register,
            'BUSHOLD', 'I2C1.IEN.BUSHOLD', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_TXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_TXOF, self).__init__(register,
            'TXOF', 'I2C1.IEN.TXOF', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_RXUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_RXUF, self).__init__(register,
            'RXUF', 'I2C1.IEN.RXUF', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_BITO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_BITO, self).__init__(register,
            'BITO', 'I2C1.IEN.BITO', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_CLTO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_CLTO, self).__init__(register,
            'CLTO', 'I2C1.IEN.CLTO', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_SSTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_SSTOP, self).__init__(register,
            'SSTOP', 'I2C1.IEN.SSTOP', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_RXFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_RXFULL, self).__init__(register,
            'RXFULL', 'I2C1.IEN.RXFULL', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_IEN_CLERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_IEN_CLERR, self).__init__(register,
            'CLERR', 'I2C1.IEN.CLERR', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_ROUTEPEN_SDAPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_ROUTEPEN_SDAPEN, self).__init__(register,
            'SDAPEN', 'I2C1.ROUTEPEN.SDAPEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_ROUTEPEN_SCLPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_ROUTEPEN_SCLPEN, self).__init__(register,
            'SCLPEN', 'I2C1.ROUTEPEN.SCLPEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_ROUTELOC0_SDALOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_ROUTELOC0_SDALOC, self).__init__(register,
            'SDALOC', 'I2C1.ROUTELOC0.SDALOC', 'read-write',
            "",
            0, 6,
            RM_Enum_I2C1_ROUTELOC0_SDALOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_I2C1_ROUTELOC0_SCLLOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_I2C1_ROUTELOC0_SCLLOC, self).__init__(register,
            'SCLLOC', 'I2C1.ROUTELOC0.SCLLOC', 'read-write',
            "",
            8, 6,
            RM_Enum_I2C1_ROUTELOC0_SCLLOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


