
from static import Base_RM_Register
from I2C0_field import *


class RM_Register_I2C0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_CTRL, self).__init__(rmio, label,
            0x4000c000, 0x000,
            'CTRL', 'I2C0.CTRL', 'read-write',
            "",
            0x00000000, 0x0007B3FF)

        self.EN = RM_Field_I2C0_CTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.SLAVE = RM_Field_I2C0_CTRL_SLAVE(self)
        self.zz_fdict['SLAVE'] = self.SLAVE
        self.AUTOACK = RM_Field_I2C0_CTRL_AUTOACK(self)
        self.zz_fdict['AUTOACK'] = self.AUTOACK
        self.AUTOSE = RM_Field_I2C0_CTRL_AUTOSE(self)
        self.zz_fdict['AUTOSE'] = self.AUTOSE
        self.AUTOSN = RM_Field_I2C0_CTRL_AUTOSN(self)
        self.zz_fdict['AUTOSN'] = self.AUTOSN
        self.ARBDIS = RM_Field_I2C0_CTRL_ARBDIS(self)
        self.zz_fdict['ARBDIS'] = self.ARBDIS
        self.GCAMEN = RM_Field_I2C0_CTRL_GCAMEN(self)
        self.zz_fdict['GCAMEN'] = self.GCAMEN
        self.TXBIL = RM_Field_I2C0_CTRL_TXBIL(self)
        self.zz_fdict['TXBIL'] = self.TXBIL
        self.CLHR = RM_Field_I2C0_CTRL_CLHR(self)
        self.zz_fdict['CLHR'] = self.CLHR
        self.BITO = RM_Field_I2C0_CTRL_BITO(self)
        self.zz_fdict['BITO'] = self.BITO
        self.GIBITO = RM_Field_I2C0_CTRL_GIBITO(self)
        self.zz_fdict['GIBITO'] = self.GIBITO
        self.CLTO = RM_Field_I2C0_CTRL_CLTO(self)
        self.zz_fdict['CLTO'] = self.CLTO
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_CMD, self).__init__(rmio, label,
            0x4000c000, 0x004,
            'CMD', 'I2C0.CMD', 'write-only',
            "",
            0x00000000, 0x000000FF)

        self.START = RM_Field_I2C0_CMD_START(self)
        self.zz_fdict['START'] = self.START
        self.STOP = RM_Field_I2C0_CMD_STOP(self)
        self.zz_fdict['STOP'] = self.STOP
        self.ACK = RM_Field_I2C0_CMD_ACK(self)
        self.zz_fdict['ACK'] = self.ACK
        self.NACK = RM_Field_I2C0_CMD_NACK(self)
        self.zz_fdict['NACK'] = self.NACK
        self.CONT = RM_Field_I2C0_CMD_CONT(self)
        self.zz_fdict['CONT'] = self.CONT
        self.ABORT = RM_Field_I2C0_CMD_ABORT(self)
        self.zz_fdict['ABORT'] = self.ABORT
        self.CLEARTX = RM_Field_I2C0_CMD_CLEARTX(self)
        self.zz_fdict['CLEARTX'] = self.CLEARTX
        self.CLEARPC = RM_Field_I2C0_CMD_CLEARPC(self)
        self.zz_fdict['CLEARPC'] = self.CLEARPC
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_STATE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_STATE, self).__init__(rmio, label,
            0x4000c000, 0x008,
            'STATE', 'I2C0.STATE', 'read-only',
            "",
            0x00000001, 0x000000FF)

        self.BUSY = RM_Field_I2C0_STATE_BUSY(self)
        self.zz_fdict['BUSY'] = self.BUSY
        self.MASTER = RM_Field_I2C0_STATE_MASTER(self)
        self.zz_fdict['MASTER'] = self.MASTER
        self.TRANSMITTER = RM_Field_I2C0_STATE_TRANSMITTER(self)
        self.zz_fdict['TRANSMITTER'] = self.TRANSMITTER
        self.NACKED = RM_Field_I2C0_STATE_NACKED(self)
        self.zz_fdict['NACKED'] = self.NACKED
        self.BUSHOLD = RM_Field_I2C0_STATE_BUSHOLD(self)
        self.zz_fdict['BUSHOLD'] = self.BUSHOLD
        self.STATE = RM_Field_I2C0_STATE_STATE(self)
        self.zz_fdict['STATE'] = self.STATE
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_STATUS, self).__init__(rmio, label,
            0x4000c000, 0x00C,
            'STATUS', 'I2C0.STATUS', 'read-only',
            "",
            0x00000080, 0x000003FF)

        self.PSTART = RM_Field_I2C0_STATUS_PSTART(self)
        self.zz_fdict['PSTART'] = self.PSTART
        self.PSTOP = RM_Field_I2C0_STATUS_PSTOP(self)
        self.zz_fdict['PSTOP'] = self.PSTOP
        self.PACK = RM_Field_I2C0_STATUS_PACK(self)
        self.zz_fdict['PACK'] = self.PACK
        self.PNACK = RM_Field_I2C0_STATUS_PNACK(self)
        self.zz_fdict['PNACK'] = self.PNACK
        self.PCONT = RM_Field_I2C0_STATUS_PCONT(self)
        self.zz_fdict['PCONT'] = self.PCONT
        self.PABORT = RM_Field_I2C0_STATUS_PABORT(self)
        self.zz_fdict['PABORT'] = self.PABORT
        self.TXC = RM_Field_I2C0_STATUS_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.TXBL = RM_Field_I2C0_STATUS_TXBL(self)
        self.zz_fdict['TXBL'] = self.TXBL
        self.RXDATAV = RM_Field_I2C0_STATUS_RXDATAV(self)
        self.zz_fdict['RXDATAV'] = self.RXDATAV
        self.RXFULL = RM_Field_I2C0_STATUS_RXFULL(self)
        self.zz_fdict['RXFULL'] = self.RXFULL
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_CLKDIV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_CLKDIV, self).__init__(rmio, label,
            0x4000c000, 0x010,
            'CLKDIV', 'I2C0.CLKDIV', 'read-write',
            "",
            0x00000000, 0x000001FF)

        self.DIV = RM_Field_I2C0_CLKDIV_DIV(self)
        self.zz_fdict['DIV'] = self.DIV
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_SADDR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_SADDR, self).__init__(rmio, label,
            0x4000c000, 0x014,
            'SADDR', 'I2C0.SADDR', 'read-write',
            "",
            0x00000000, 0x000000FE)

        self.ADDR = RM_Field_I2C0_SADDR_ADDR(self)
        self.zz_fdict['ADDR'] = self.ADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_SADDRMASK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_SADDRMASK, self).__init__(rmio, label,
            0x4000c000, 0x018,
            'SADDRMASK', 'I2C0.SADDRMASK', 'read-write',
            "",
            0x00000000, 0x000000FE)

        self.MASK = RM_Field_I2C0_SADDRMASK_MASK(self)
        self.zz_fdict['MASK'] = self.MASK
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_RXDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_RXDATA, self).__init__(rmio, label,
            0x4000c000, 0x01C,
            'RXDATA', 'I2C0.RXDATA', 'read-only',
            "",
            0x00000000, 0x000000FF)

        self.RXDATA = RM_Field_I2C0_RXDATA_RXDATA(self)
        self.zz_fdict['RXDATA'] = self.RXDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_RXDOUBLE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_RXDOUBLE, self).__init__(rmio, label,
            0x4000c000, 0x020,
            'RXDOUBLE', 'I2C0.RXDOUBLE', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.RXDATA0 = RM_Field_I2C0_RXDOUBLE_RXDATA0(self)
        self.zz_fdict['RXDATA0'] = self.RXDATA0
        self.RXDATA1 = RM_Field_I2C0_RXDOUBLE_RXDATA1(self)
        self.zz_fdict['RXDATA1'] = self.RXDATA1
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_RXDATAP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_RXDATAP, self).__init__(rmio, label,
            0x4000c000, 0x024,
            'RXDATAP', 'I2C0.RXDATAP', 'read-only',
            "",
            0x00000000, 0x000000FF)

        self.RXDATAP = RM_Field_I2C0_RXDATAP_RXDATAP(self)
        self.zz_fdict['RXDATAP'] = self.RXDATAP
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_RXDOUBLEP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_RXDOUBLEP, self).__init__(rmio, label,
            0x4000c000, 0x028,
            'RXDOUBLEP', 'I2C0.RXDOUBLEP', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.RXDATAP0 = RM_Field_I2C0_RXDOUBLEP_RXDATAP0(self)
        self.zz_fdict['RXDATAP0'] = self.RXDATAP0
        self.RXDATAP1 = RM_Field_I2C0_RXDOUBLEP_RXDATAP1(self)
        self.zz_fdict['RXDATAP1'] = self.RXDATAP1
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_TXDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_TXDATA, self).__init__(rmio, label,
            0x4000c000, 0x02C,
            'TXDATA', 'I2C0.TXDATA', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.TXDATA = RM_Field_I2C0_TXDATA_TXDATA(self)
        self.zz_fdict['TXDATA'] = self.TXDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_TXDOUBLE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_TXDOUBLE, self).__init__(rmio, label,
            0x4000c000, 0x030,
            'TXDOUBLE', 'I2C0.TXDOUBLE', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TXDATA0 = RM_Field_I2C0_TXDOUBLE_TXDATA0(self)
        self.zz_fdict['TXDATA0'] = self.TXDATA0
        self.TXDATA1 = RM_Field_I2C0_TXDOUBLE_TXDATA1(self)
        self.zz_fdict['TXDATA1'] = self.TXDATA1
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_IF, self).__init__(rmio, label,
            0x4000c000, 0x034,
            'IF', 'I2C0.IF', 'read-only',
            "",
            0x00000010, 0x0007FFFF)

        self.START = RM_Field_I2C0_IF_START(self)
        self.zz_fdict['START'] = self.START
        self.RSTART = RM_Field_I2C0_IF_RSTART(self)
        self.zz_fdict['RSTART'] = self.RSTART
        self.ADDR = RM_Field_I2C0_IF_ADDR(self)
        self.zz_fdict['ADDR'] = self.ADDR
        self.TXC = RM_Field_I2C0_IF_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.TXBL = RM_Field_I2C0_IF_TXBL(self)
        self.zz_fdict['TXBL'] = self.TXBL
        self.RXDATAV = RM_Field_I2C0_IF_RXDATAV(self)
        self.zz_fdict['RXDATAV'] = self.RXDATAV
        self.ACK = RM_Field_I2C0_IF_ACK(self)
        self.zz_fdict['ACK'] = self.ACK
        self.NACK = RM_Field_I2C0_IF_NACK(self)
        self.zz_fdict['NACK'] = self.NACK
        self.MSTOP = RM_Field_I2C0_IF_MSTOP(self)
        self.zz_fdict['MSTOP'] = self.MSTOP
        self.ARBLOST = RM_Field_I2C0_IF_ARBLOST(self)
        self.zz_fdict['ARBLOST'] = self.ARBLOST
        self.BUSERR = RM_Field_I2C0_IF_BUSERR(self)
        self.zz_fdict['BUSERR'] = self.BUSERR
        self.BUSHOLD = RM_Field_I2C0_IF_BUSHOLD(self)
        self.zz_fdict['BUSHOLD'] = self.BUSHOLD
        self.TXOF = RM_Field_I2C0_IF_TXOF(self)
        self.zz_fdict['TXOF'] = self.TXOF
        self.RXUF = RM_Field_I2C0_IF_RXUF(self)
        self.zz_fdict['RXUF'] = self.RXUF
        self.BITO = RM_Field_I2C0_IF_BITO(self)
        self.zz_fdict['BITO'] = self.BITO
        self.CLTO = RM_Field_I2C0_IF_CLTO(self)
        self.zz_fdict['CLTO'] = self.CLTO
        self.SSTOP = RM_Field_I2C0_IF_SSTOP(self)
        self.zz_fdict['SSTOP'] = self.SSTOP
        self.RXFULL = RM_Field_I2C0_IF_RXFULL(self)
        self.zz_fdict['RXFULL'] = self.RXFULL
        self.CLERR = RM_Field_I2C0_IF_CLERR(self)
        self.zz_fdict['CLERR'] = self.CLERR
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_IFS, self).__init__(rmio, label,
            0x4000c000, 0x038,
            'IFS', 'I2C0.IFS', 'write-only',
            "",
            0x00000000, 0x0007FFCF)

        self.START = RM_Field_I2C0_IFS_START(self)
        self.zz_fdict['START'] = self.START
        self.RSTART = RM_Field_I2C0_IFS_RSTART(self)
        self.zz_fdict['RSTART'] = self.RSTART
        self.ADDR = RM_Field_I2C0_IFS_ADDR(self)
        self.zz_fdict['ADDR'] = self.ADDR
        self.TXC = RM_Field_I2C0_IFS_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.ACK = RM_Field_I2C0_IFS_ACK(self)
        self.zz_fdict['ACK'] = self.ACK
        self.NACK = RM_Field_I2C0_IFS_NACK(self)
        self.zz_fdict['NACK'] = self.NACK
        self.MSTOP = RM_Field_I2C0_IFS_MSTOP(self)
        self.zz_fdict['MSTOP'] = self.MSTOP
        self.ARBLOST = RM_Field_I2C0_IFS_ARBLOST(self)
        self.zz_fdict['ARBLOST'] = self.ARBLOST
        self.BUSERR = RM_Field_I2C0_IFS_BUSERR(self)
        self.zz_fdict['BUSERR'] = self.BUSERR
        self.BUSHOLD = RM_Field_I2C0_IFS_BUSHOLD(self)
        self.zz_fdict['BUSHOLD'] = self.BUSHOLD
        self.TXOF = RM_Field_I2C0_IFS_TXOF(self)
        self.zz_fdict['TXOF'] = self.TXOF
        self.RXUF = RM_Field_I2C0_IFS_RXUF(self)
        self.zz_fdict['RXUF'] = self.RXUF
        self.BITO = RM_Field_I2C0_IFS_BITO(self)
        self.zz_fdict['BITO'] = self.BITO
        self.CLTO = RM_Field_I2C0_IFS_CLTO(self)
        self.zz_fdict['CLTO'] = self.CLTO
        self.SSTOP = RM_Field_I2C0_IFS_SSTOP(self)
        self.zz_fdict['SSTOP'] = self.SSTOP
        self.RXFULL = RM_Field_I2C0_IFS_RXFULL(self)
        self.zz_fdict['RXFULL'] = self.RXFULL
        self.CLERR = RM_Field_I2C0_IFS_CLERR(self)
        self.zz_fdict['CLERR'] = self.CLERR
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_IFC, self).__init__(rmio, label,
            0x4000c000, 0x03C,
            'IFC', 'I2C0.IFC', 'write-only',
            "",
            0x00000000, 0x0007FFCF)

        self.START = RM_Field_I2C0_IFC_START(self)
        self.zz_fdict['START'] = self.START
        self.RSTART = RM_Field_I2C0_IFC_RSTART(self)
        self.zz_fdict['RSTART'] = self.RSTART
        self.ADDR = RM_Field_I2C0_IFC_ADDR(self)
        self.zz_fdict['ADDR'] = self.ADDR
        self.TXC = RM_Field_I2C0_IFC_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.ACK = RM_Field_I2C0_IFC_ACK(self)
        self.zz_fdict['ACK'] = self.ACK
        self.NACK = RM_Field_I2C0_IFC_NACK(self)
        self.zz_fdict['NACK'] = self.NACK
        self.MSTOP = RM_Field_I2C0_IFC_MSTOP(self)
        self.zz_fdict['MSTOP'] = self.MSTOP
        self.ARBLOST = RM_Field_I2C0_IFC_ARBLOST(self)
        self.zz_fdict['ARBLOST'] = self.ARBLOST
        self.BUSERR = RM_Field_I2C0_IFC_BUSERR(self)
        self.zz_fdict['BUSERR'] = self.BUSERR
        self.BUSHOLD = RM_Field_I2C0_IFC_BUSHOLD(self)
        self.zz_fdict['BUSHOLD'] = self.BUSHOLD
        self.TXOF = RM_Field_I2C0_IFC_TXOF(self)
        self.zz_fdict['TXOF'] = self.TXOF
        self.RXUF = RM_Field_I2C0_IFC_RXUF(self)
        self.zz_fdict['RXUF'] = self.RXUF
        self.BITO = RM_Field_I2C0_IFC_BITO(self)
        self.zz_fdict['BITO'] = self.BITO
        self.CLTO = RM_Field_I2C0_IFC_CLTO(self)
        self.zz_fdict['CLTO'] = self.CLTO
        self.SSTOP = RM_Field_I2C0_IFC_SSTOP(self)
        self.zz_fdict['SSTOP'] = self.SSTOP
        self.RXFULL = RM_Field_I2C0_IFC_RXFULL(self)
        self.zz_fdict['RXFULL'] = self.RXFULL
        self.CLERR = RM_Field_I2C0_IFC_CLERR(self)
        self.zz_fdict['CLERR'] = self.CLERR
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_IEN, self).__init__(rmio, label,
            0x4000c000, 0x040,
            'IEN', 'I2C0.IEN', 'read-write',
            "",
            0x00000000, 0x0007FFFF)

        self.START = RM_Field_I2C0_IEN_START(self)
        self.zz_fdict['START'] = self.START
        self.RSTART = RM_Field_I2C0_IEN_RSTART(self)
        self.zz_fdict['RSTART'] = self.RSTART
        self.ADDR = RM_Field_I2C0_IEN_ADDR(self)
        self.zz_fdict['ADDR'] = self.ADDR
        self.TXC = RM_Field_I2C0_IEN_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.TXBL = RM_Field_I2C0_IEN_TXBL(self)
        self.zz_fdict['TXBL'] = self.TXBL
        self.RXDATAV = RM_Field_I2C0_IEN_RXDATAV(self)
        self.zz_fdict['RXDATAV'] = self.RXDATAV
        self.ACK = RM_Field_I2C0_IEN_ACK(self)
        self.zz_fdict['ACK'] = self.ACK
        self.NACK = RM_Field_I2C0_IEN_NACK(self)
        self.zz_fdict['NACK'] = self.NACK
        self.MSTOP = RM_Field_I2C0_IEN_MSTOP(self)
        self.zz_fdict['MSTOP'] = self.MSTOP
        self.ARBLOST = RM_Field_I2C0_IEN_ARBLOST(self)
        self.zz_fdict['ARBLOST'] = self.ARBLOST
        self.BUSERR = RM_Field_I2C0_IEN_BUSERR(self)
        self.zz_fdict['BUSERR'] = self.BUSERR
        self.BUSHOLD = RM_Field_I2C0_IEN_BUSHOLD(self)
        self.zz_fdict['BUSHOLD'] = self.BUSHOLD
        self.TXOF = RM_Field_I2C0_IEN_TXOF(self)
        self.zz_fdict['TXOF'] = self.TXOF
        self.RXUF = RM_Field_I2C0_IEN_RXUF(self)
        self.zz_fdict['RXUF'] = self.RXUF
        self.BITO = RM_Field_I2C0_IEN_BITO(self)
        self.zz_fdict['BITO'] = self.BITO
        self.CLTO = RM_Field_I2C0_IEN_CLTO(self)
        self.zz_fdict['CLTO'] = self.CLTO
        self.SSTOP = RM_Field_I2C0_IEN_SSTOP(self)
        self.zz_fdict['SSTOP'] = self.SSTOP
        self.RXFULL = RM_Field_I2C0_IEN_RXFULL(self)
        self.zz_fdict['RXFULL'] = self.RXFULL
        self.CLERR = RM_Field_I2C0_IEN_CLERR(self)
        self.zz_fdict['CLERR'] = self.CLERR
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_ROUTEPEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_ROUTEPEN, self).__init__(rmio, label,
            0x4000c000, 0x044,
            'ROUTEPEN', 'I2C0.ROUTEPEN', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.SDAPEN = RM_Field_I2C0_ROUTEPEN_SDAPEN(self)
        self.zz_fdict['SDAPEN'] = self.SDAPEN
        self.SCLPEN = RM_Field_I2C0_ROUTEPEN_SCLPEN(self)
        self.zz_fdict['SCLPEN'] = self.SCLPEN
        self.__dict__['zz_frozen'] = True


class RM_Register_I2C0_ROUTELOC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_I2C0_ROUTELOC0, self).__init__(rmio, label,
            0x4000c000, 0x048,
            'ROUTELOC0', 'I2C0.ROUTELOC0', 'read-write',
            "",
            0x00000000, 0x00003F3F)

        self.SDALOC = RM_Field_I2C0_ROUTELOC0_SDALOC(self)
        self.zz_fdict['SDALOC'] = self.SDALOC
        self.SCLLOC = RM_Field_I2C0_ROUTELOC0_SCLLOC(self)
        self.zz_fdict['SCLLOC'] = self.SCLLOC
        self.__dict__['zz_frozen'] = True


