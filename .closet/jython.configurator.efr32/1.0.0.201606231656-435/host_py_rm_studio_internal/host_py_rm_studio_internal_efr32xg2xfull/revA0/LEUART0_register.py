
from static import Base_RM_Register
from LEUART0_field import *


class RM_Register_LEUART0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_CTRL, self).__init__(rmio, label,
            0x4004a000, 0x000,
            'CTRL', 'LEUART0.CTRL', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.AUTOTRI = RM_Field_LEUART0_CTRL_AUTOTRI(self)
        self.zz_fdict['AUTOTRI'] = self.AUTOTRI
        self.DATABITS = RM_Field_LEUART0_CTRL_DATABITS(self)
        self.zz_fdict['DATABITS'] = self.DATABITS
        self.PARITY = RM_Field_LEUART0_CTRL_PARITY(self)
        self.zz_fdict['PARITY'] = self.PARITY
        self.STOPBITS = RM_Field_LEUART0_CTRL_STOPBITS(self)
        self.zz_fdict['STOPBITS'] = self.STOPBITS
        self.INV = RM_Field_LEUART0_CTRL_INV(self)
        self.zz_fdict['INV'] = self.INV
        self.ERRSDMA = RM_Field_LEUART0_CTRL_ERRSDMA(self)
        self.zz_fdict['ERRSDMA'] = self.ERRSDMA
        self.LOOPBK = RM_Field_LEUART0_CTRL_LOOPBK(self)
        self.zz_fdict['LOOPBK'] = self.LOOPBK
        self.SFUBRX = RM_Field_LEUART0_CTRL_SFUBRX(self)
        self.zz_fdict['SFUBRX'] = self.SFUBRX
        self.MPM = RM_Field_LEUART0_CTRL_MPM(self)
        self.zz_fdict['MPM'] = self.MPM
        self.MPAB = RM_Field_LEUART0_CTRL_MPAB(self)
        self.zz_fdict['MPAB'] = self.MPAB
        self.BIT8DV = RM_Field_LEUART0_CTRL_BIT8DV(self)
        self.zz_fdict['BIT8DV'] = self.BIT8DV
        self.RXDMAWU = RM_Field_LEUART0_CTRL_RXDMAWU(self)
        self.zz_fdict['RXDMAWU'] = self.RXDMAWU
        self.TXDMAWU = RM_Field_LEUART0_CTRL_TXDMAWU(self)
        self.zz_fdict['TXDMAWU'] = self.TXDMAWU
        self.TXDELAY = RM_Field_LEUART0_CTRL_TXDELAY(self)
        self.zz_fdict['TXDELAY'] = self.TXDELAY
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_CMD, self).__init__(rmio, label,
            0x4004a000, 0x004,
            'CMD', 'LEUART0.CMD', 'write-only',
            "",
            0x00000000, 0x000000FF)

        self.RXEN = RM_Field_LEUART0_CMD_RXEN(self)
        self.zz_fdict['RXEN'] = self.RXEN
        self.RXDIS = RM_Field_LEUART0_CMD_RXDIS(self)
        self.zz_fdict['RXDIS'] = self.RXDIS
        self.TXEN = RM_Field_LEUART0_CMD_TXEN(self)
        self.zz_fdict['TXEN'] = self.TXEN
        self.TXDIS = RM_Field_LEUART0_CMD_TXDIS(self)
        self.zz_fdict['TXDIS'] = self.TXDIS
        self.RXBLOCKEN = RM_Field_LEUART0_CMD_RXBLOCKEN(self)
        self.zz_fdict['RXBLOCKEN'] = self.RXBLOCKEN
        self.RXBLOCKDIS = RM_Field_LEUART0_CMD_RXBLOCKDIS(self)
        self.zz_fdict['RXBLOCKDIS'] = self.RXBLOCKDIS
        self.CLEARTX = RM_Field_LEUART0_CMD_CLEARTX(self)
        self.zz_fdict['CLEARTX'] = self.CLEARTX
        self.CLEARRX = RM_Field_LEUART0_CMD_CLEARRX(self)
        self.zz_fdict['CLEARRX'] = self.CLEARRX
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_STATUS, self).__init__(rmio, label,
            0x4004a000, 0x008,
            'STATUS', 'LEUART0.STATUS', 'read-only',
            "",
            0x00000050, 0x0000007F)

        self.RXENS = RM_Field_LEUART0_STATUS_RXENS(self)
        self.zz_fdict['RXENS'] = self.RXENS
        self.TXENS = RM_Field_LEUART0_STATUS_TXENS(self)
        self.zz_fdict['TXENS'] = self.TXENS
        self.RXBLOCK = RM_Field_LEUART0_STATUS_RXBLOCK(self)
        self.zz_fdict['RXBLOCK'] = self.RXBLOCK
        self.TXC = RM_Field_LEUART0_STATUS_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.TXBL = RM_Field_LEUART0_STATUS_TXBL(self)
        self.zz_fdict['TXBL'] = self.TXBL
        self.RXDATAV = RM_Field_LEUART0_STATUS_RXDATAV(self)
        self.zz_fdict['RXDATAV'] = self.RXDATAV
        self.TXIDLE = RM_Field_LEUART0_STATUS_TXIDLE(self)
        self.zz_fdict['TXIDLE'] = self.TXIDLE
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_CLKDIV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_CLKDIV, self).__init__(rmio, label,
            0x4004a000, 0x00C,
            'CLKDIV', 'LEUART0.CLKDIV', 'read-write',
            "",
            0x00000000, 0x0001FFF8)

        self.DIV = RM_Field_LEUART0_CLKDIV_DIV(self)
        self.zz_fdict['DIV'] = self.DIV
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_STARTFRAME(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_STARTFRAME, self).__init__(rmio, label,
            0x4004a000, 0x010,
            'STARTFRAME', 'LEUART0.STARTFRAME', 'read-write',
            "",
            0x00000000, 0x000001FF)

        self.STARTFRAME = RM_Field_LEUART0_STARTFRAME_STARTFRAME(self)
        self.zz_fdict['STARTFRAME'] = self.STARTFRAME
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_SIGFRAME(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_SIGFRAME, self).__init__(rmio, label,
            0x4004a000, 0x014,
            'SIGFRAME', 'LEUART0.SIGFRAME', 'read-write',
            "",
            0x00000000, 0x000001FF)

        self.SIGFRAME = RM_Field_LEUART0_SIGFRAME_SIGFRAME(self)
        self.zz_fdict['SIGFRAME'] = self.SIGFRAME
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_RXDATAX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_RXDATAX, self).__init__(rmio, label,
            0x4004a000, 0x018,
            'RXDATAX', 'LEUART0.RXDATAX', 'read-only',
            "",
            0x00000000, 0x0000C1FF)

        self.RXDATA = RM_Field_LEUART0_RXDATAX_RXDATA(self)
        self.zz_fdict['RXDATA'] = self.RXDATA
        self.PERR = RM_Field_LEUART0_RXDATAX_PERR(self)
        self.zz_fdict['PERR'] = self.PERR
        self.FERR = RM_Field_LEUART0_RXDATAX_FERR(self)
        self.zz_fdict['FERR'] = self.FERR
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_RXDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_RXDATA, self).__init__(rmio, label,
            0x4004a000, 0x01C,
            'RXDATA', 'LEUART0.RXDATA', 'read-only',
            "",
            0x00000000, 0x000000FF)

        self.RXDATA = RM_Field_LEUART0_RXDATA_RXDATA(self)
        self.zz_fdict['RXDATA'] = self.RXDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_RXDATAXP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_RXDATAXP, self).__init__(rmio, label,
            0x4004a000, 0x020,
            'RXDATAXP', 'LEUART0.RXDATAXP', 'read-only',
            "",
            0x00000000, 0x0000C1FF)

        self.RXDATAP = RM_Field_LEUART0_RXDATAXP_RXDATAP(self)
        self.zz_fdict['RXDATAP'] = self.RXDATAP
        self.PERRP = RM_Field_LEUART0_RXDATAXP_PERRP(self)
        self.zz_fdict['PERRP'] = self.PERRP
        self.FERRP = RM_Field_LEUART0_RXDATAXP_FERRP(self)
        self.zz_fdict['FERRP'] = self.FERRP
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_TXDATAX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_TXDATAX, self).__init__(rmio, label,
            0x4004a000, 0x024,
            'TXDATAX', 'LEUART0.TXDATAX', 'read-write',
            "",
            0x00000000, 0x0000E1FF)

        self.TXDATA = RM_Field_LEUART0_TXDATAX_TXDATA(self)
        self.zz_fdict['TXDATA'] = self.TXDATA
        self.TXBREAK = RM_Field_LEUART0_TXDATAX_TXBREAK(self)
        self.zz_fdict['TXBREAK'] = self.TXBREAK
        self.TXDISAT = RM_Field_LEUART0_TXDATAX_TXDISAT(self)
        self.zz_fdict['TXDISAT'] = self.TXDISAT
        self.RXENAT = RM_Field_LEUART0_TXDATAX_RXENAT(self)
        self.zz_fdict['RXENAT'] = self.RXENAT
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_TXDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_TXDATA, self).__init__(rmio, label,
            0x4004a000, 0x028,
            'TXDATA', 'LEUART0.TXDATA', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.TXDATA = RM_Field_LEUART0_TXDATA_TXDATA(self)
        self.zz_fdict['TXDATA'] = self.TXDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_IF, self).__init__(rmio, label,
            0x4004a000, 0x02C,
            'IF', 'LEUART0.IF', 'read-only',
            "",
            0x00000002, 0x000007FF)

        self.TXC = RM_Field_LEUART0_IF_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.TXBL = RM_Field_LEUART0_IF_TXBL(self)
        self.zz_fdict['TXBL'] = self.TXBL
        self.RXDATAV = RM_Field_LEUART0_IF_RXDATAV(self)
        self.zz_fdict['RXDATAV'] = self.RXDATAV
        self.RXOF = RM_Field_LEUART0_IF_RXOF(self)
        self.zz_fdict['RXOF'] = self.RXOF
        self.RXUF = RM_Field_LEUART0_IF_RXUF(self)
        self.zz_fdict['RXUF'] = self.RXUF
        self.TXOF = RM_Field_LEUART0_IF_TXOF(self)
        self.zz_fdict['TXOF'] = self.TXOF
        self.PERR = RM_Field_LEUART0_IF_PERR(self)
        self.zz_fdict['PERR'] = self.PERR
        self.FERR = RM_Field_LEUART0_IF_FERR(self)
        self.zz_fdict['FERR'] = self.FERR
        self.MPAF = RM_Field_LEUART0_IF_MPAF(self)
        self.zz_fdict['MPAF'] = self.MPAF
        self.STARTF = RM_Field_LEUART0_IF_STARTF(self)
        self.zz_fdict['STARTF'] = self.STARTF
        self.SIGF = RM_Field_LEUART0_IF_SIGF(self)
        self.zz_fdict['SIGF'] = self.SIGF
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_IFS, self).__init__(rmio, label,
            0x4004a000, 0x030,
            'IFS', 'LEUART0.IFS', 'write-only',
            "",
            0x00000000, 0x000007F9)

        self.TXC = RM_Field_LEUART0_IFS_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.RXOF = RM_Field_LEUART0_IFS_RXOF(self)
        self.zz_fdict['RXOF'] = self.RXOF
        self.RXUF = RM_Field_LEUART0_IFS_RXUF(self)
        self.zz_fdict['RXUF'] = self.RXUF
        self.TXOF = RM_Field_LEUART0_IFS_TXOF(self)
        self.zz_fdict['TXOF'] = self.TXOF
        self.PERR = RM_Field_LEUART0_IFS_PERR(self)
        self.zz_fdict['PERR'] = self.PERR
        self.FERR = RM_Field_LEUART0_IFS_FERR(self)
        self.zz_fdict['FERR'] = self.FERR
        self.MPAF = RM_Field_LEUART0_IFS_MPAF(self)
        self.zz_fdict['MPAF'] = self.MPAF
        self.STARTF = RM_Field_LEUART0_IFS_STARTF(self)
        self.zz_fdict['STARTF'] = self.STARTF
        self.SIGF = RM_Field_LEUART0_IFS_SIGF(self)
        self.zz_fdict['SIGF'] = self.SIGF
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_IFC, self).__init__(rmio, label,
            0x4004a000, 0x034,
            'IFC', 'LEUART0.IFC', 'write-only',
            "",
            0x00000000, 0x000007F9)

        self.TXC = RM_Field_LEUART0_IFC_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.RXOF = RM_Field_LEUART0_IFC_RXOF(self)
        self.zz_fdict['RXOF'] = self.RXOF
        self.RXUF = RM_Field_LEUART0_IFC_RXUF(self)
        self.zz_fdict['RXUF'] = self.RXUF
        self.TXOF = RM_Field_LEUART0_IFC_TXOF(self)
        self.zz_fdict['TXOF'] = self.TXOF
        self.PERR = RM_Field_LEUART0_IFC_PERR(self)
        self.zz_fdict['PERR'] = self.PERR
        self.FERR = RM_Field_LEUART0_IFC_FERR(self)
        self.zz_fdict['FERR'] = self.FERR
        self.MPAF = RM_Field_LEUART0_IFC_MPAF(self)
        self.zz_fdict['MPAF'] = self.MPAF
        self.STARTF = RM_Field_LEUART0_IFC_STARTF(self)
        self.zz_fdict['STARTF'] = self.STARTF
        self.SIGF = RM_Field_LEUART0_IFC_SIGF(self)
        self.zz_fdict['SIGF'] = self.SIGF
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_IEN, self).__init__(rmio, label,
            0x4004a000, 0x038,
            'IEN', 'LEUART0.IEN', 'read-write',
            "",
            0x00000000, 0x000007FF)

        self.TXC = RM_Field_LEUART0_IEN_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.TXBL = RM_Field_LEUART0_IEN_TXBL(self)
        self.zz_fdict['TXBL'] = self.TXBL
        self.RXDATAV = RM_Field_LEUART0_IEN_RXDATAV(self)
        self.zz_fdict['RXDATAV'] = self.RXDATAV
        self.RXOF = RM_Field_LEUART0_IEN_RXOF(self)
        self.zz_fdict['RXOF'] = self.RXOF
        self.RXUF = RM_Field_LEUART0_IEN_RXUF(self)
        self.zz_fdict['RXUF'] = self.RXUF
        self.TXOF = RM_Field_LEUART0_IEN_TXOF(self)
        self.zz_fdict['TXOF'] = self.TXOF
        self.PERR = RM_Field_LEUART0_IEN_PERR(self)
        self.zz_fdict['PERR'] = self.PERR
        self.FERR = RM_Field_LEUART0_IEN_FERR(self)
        self.zz_fdict['FERR'] = self.FERR
        self.MPAF = RM_Field_LEUART0_IEN_MPAF(self)
        self.zz_fdict['MPAF'] = self.MPAF
        self.STARTF = RM_Field_LEUART0_IEN_STARTF(self)
        self.zz_fdict['STARTF'] = self.STARTF
        self.SIGF = RM_Field_LEUART0_IEN_SIGF(self)
        self.zz_fdict['SIGF'] = self.SIGF
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_PULSECTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_PULSECTRL, self).__init__(rmio, label,
            0x4004a000, 0x03C,
            'PULSECTRL', 'LEUART0.PULSECTRL', 'read-write',
            "",
            0x00000000, 0x0000003F)

        self.PULSEW = RM_Field_LEUART0_PULSECTRL_PULSEW(self)
        self.zz_fdict['PULSEW'] = self.PULSEW
        self.PULSEEN = RM_Field_LEUART0_PULSECTRL_PULSEEN(self)
        self.zz_fdict['PULSEEN'] = self.PULSEEN
        self.PULSEFILT = RM_Field_LEUART0_PULSECTRL_PULSEFILT(self)
        self.zz_fdict['PULSEFILT'] = self.PULSEFILT
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_FREEZE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_FREEZE, self).__init__(rmio, label,
            0x4004a000, 0x040,
            'FREEZE', 'LEUART0.FREEZE', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.REGFREEZE = RM_Field_LEUART0_FREEZE_REGFREEZE(self)
        self.zz_fdict['REGFREEZE'] = self.REGFREEZE
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_SYNCBUSY(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_SYNCBUSY, self).__init__(rmio, label,
            0x4004a000, 0x044,
            'SYNCBUSY', 'LEUART0.SYNCBUSY', 'read-only',
            "",
            0x00000000, 0x000000FF)

        self.CTRL = RM_Field_LEUART0_SYNCBUSY_CTRL(self)
        self.zz_fdict['CTRL'] = self.CTRL
        self.CMD = RM_Field_LEUART0_SYNCBUSY_CMD(self)
        self.zz_fdict['CMD'] = self.CMD
        self.CLKDIV = RM_Field_LEUART0_SYNCBUSY_CLKDIV(self)
        self.zz_fdict['CLKDIV'] = self.CLKDIV
        self.STARTFRAME = RM_Field_LEUART0_SYNCBUSY_STARTFRAME(self)
        self.zz_fdict['STARTFRAME'] = self.STARTFRAME
        self.SIGFRAME = RM_Field_LEUART0_SYNCBUSY_SIGFRAME(self)
        self.zz_fdict['SIGFRAME'] = self.SIGFRAME
        self.TXDATAX = RM_Field_LEUART0_SYNCBUSY_TXDATAX(self)
        self.zz_fdict['TXDATAX'] = self.TXDATAX
        self.TXDATA = RM_Field_LEUART0_SYNCBUSY_TXDATA(self)
        self.zz_fdict['TXDATA'] = self.TXDATA
        self.PULSECTRL = RM_Field_LEUART0_SYNCBUSY_PULSECTRL(self)
        self.zz_fdict['PULSECTRL'] = self.PULSECTRL
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_ROUTEPEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_ROUTEPEN, self).__init__(rmio, label,
            0x4004a000, 0x054,
            'ROUTEPEN', 'LEUART0.ROUTEPEN', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.RXPEN = RM_Field_LEUART0_ROUTEPEN_RXPEN(self)
        self.zz_fdict['RXPEN'] = self.RXPEN
        self.TXPEN = RM_Field_LEUART0_ROUTEPEN_TXPEN(self)
        self.zz_fdict['TXPEN'] = self.TXPEN
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_ROUTELOC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_ROUTELOC0, self).__init__(rmio, label,
            0x4004a000, 0x058,
            'ROUTELOC0', 'LEUART0.ROUTELOC0', 'read-write',
            "",
            0x00000000, 0x00003F3F)

        self.RXLOC = RM_Field_LEUART0_ROUTELOC0_RXLOC(self)
        self.zz_fdict['RXLOC'] = self.RXLOC
        self.TXLOC = RM_Field_LEUART0_ROUTELOC0_TXLOC(self)
        self.zz_fdict['TXLOC'] = self.TXLOC
        self.__dict__['zz_frozen'] = True


class RM_Register_LEUART0_INPUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LEUART0_INPUT, self).__init__(rmio, label,
            0x4004a000, 0x064,
            'INPUT', 'LEUART0.INPUT', 'read-write',
            "",
            0x00000000, 0x0000002F)

        self.RXPRSSEL = RM_Field_LEUART0_INPUT_RXPRSSEL(self)
        self.zz_fdict['RXPRSSEL'] = self.RXPRSSEL
        self.RXPRS = RM_Field_LEUART0_INPUT_RXPRS(self)
        self.zz_fdict['RXPRS'] = self.RXPRS
        self.__dict__['zz_frozen'] = True


