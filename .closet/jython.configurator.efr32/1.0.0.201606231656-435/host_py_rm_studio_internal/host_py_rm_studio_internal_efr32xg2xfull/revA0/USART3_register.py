
from static import Base_RM_Register
from USART3_field import *


class RM_Register_USART3_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_CTRL, self).__init__(rmio, label,
            0x40010c00, 0x000,
            'CTRL', 'USART3.CTRL', 'read-write',
            "",
            0x00000000, 0xF3FFFF7F)

        self.SYNC = RM_Field_USART3_CTRL_SYNC(self)
        self.zz_fdict['SYNC'] = self.SYNC
        self.LOOPBK = RM_Field_USART3_CTRL_LOOPBK(self)
        self.zz_fdict['LOOPBK'] = self.LOOPBK
        self.CCEN = RM_Field_USART3_CTRL_CCEN(self)
        self.zz_fdict['CCEN'] = self.CCEN
        self.MPM = RM_Field_USART3_CTRL_MPM(self)
        self.zz_fdict['MPM'] = self.MPM
        self.MPAB = RM_Field_USART3_CTRL_MPAB(self)
        self.zz_fdict['MPAB'] = self.MPAB
        self.OVS = RM_Field_USART3_CTRL_OVS(self)
        self.zz_fdict['OVS'] = self.OVS
        self.CLKPOL = RM_Field_USART3_CTRL_CLKPOL(self)
        self.zz_fdict['CLKPOL'] = self.CLKPOL
        self.CLKPHA = RM_Field_USART3_CTRL_CLKPHA(self)
        self.zz_fdict['CLKPHA'] = self.CLKPHA
        self.MSBF = RM_Field_USART3_CTRL_MSBF(self)
        self.zz_fdict['MSBF'] = self.MSBF
        self.CSMA = RM_Field_USART3_CTRL_CSMA(self)
        self.zz_fdict['CSMA'] = self.CSMA
        self.TXBIL = RM_Field_USART3_CTRL_TXBIL(self)
        self.zz_fdict['TXBIL'] = self.TXBIL
        self.RXINV = RM_Field_USART3_CTRL_RXINV(self)
        self.zz_fdict['RXINV'] = self.RXINV
        self.TXINV = RM_Field_USART3_CTRL_TXINV(self)
        self.zz_fdict['TXINV'] = self.TXINV
        self.CSINV = RM_Field_USART3_CTRL_CSINV(self)
        self.zz_fdict['CSINV'] = self.CSINV
        self.AUTOCS = RM_Field_USART3_CTRL_AUTOCS(self)
        self.zz_fdict['AUTOCS'] = self.AUTOCS
        self.AUTOTRI = RM_Field_USART3_CTRL_AUTOTRI(self)
        self.zz_fdict['AUTOTRI'] = self.AUTOTRI
        self.SCMODE = RM_Field_USART3_CTRL_SCMODE(self)
        self.zz_fdict['SCMODE'] = self.SCMODE
        self.SCRETRANS = RM_Field_USART3_CTRL_SCRETRANS(self)
        self.zz_fdict['SCRETRANS'] = self.SCRETRANS
        self.SKIPPERRF = RM_Field_USART3_CTRL_SKIPPERRF(self)
        self.zz_fdict['SKIPPERRF'] = self.SKIPPERRF
        self.BIT8DV = RM_Field_USART3_CTRL_BIT8DV(self)
        self.zz_fdict['BIT8DV'] = self.BIT8DV
        self.ERRSDMA = RM_Field_USART3_CTRL_ERRSDMA(self)
        self.zz_fdict['ERRSDMA'] = self.ERRSDMA
        self.ERRSRX = RM_Field_USART3_CTRL_ERRSRX(self)
        self.zz_fdict['ERRSRX'] = self.ERRSRX
        self.ERRSTX = RM_Field_USART3_CTRL_ERRSTX(self)
        self.zz_fdict['ERRSTX'] = self.ERRSTX
        self.SSSEARLY = RM_Field_USART3_CTRL_SSSEARLY(self)
        self.zz_fdict['SSSEARLY'] = self.SSSEARLY
        self.BYTESWAP = RM_Field_USART3_CTRL_BYTESWAP(self)
        self.zz_fdict['BYTESWAP'] = self.BYTESWAP
        self.AUTOTX = RM_Field_USART3_CTRL_AUTOTX(self)
        self.zz_fdict['AUTOTX'] = self.AUTOTX
        self.MVDIS = RM_Field_USART3_CTRL_MVDIS(self)
        self.zz_fdict['MVDIS'] = self.MVDIS
        self.SMSDELAY = RM_Field_USART3_CTRL_SMSDELAY(self)
        self.zz_fdict['SMSDELAY'] = self.SMSDELAY
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_FRAME(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_FRAME, self).__init__(rmio, label,
            0x40010c00, 0x004,
            'FRAME', 'USART3.FRAME', 'read-write',
            "",
            0x00001005, 0x0000330F)

        self.DATABITS = RM_Field_USART3_FRAME_DATABITS(self)
        self.zz_fdict['DATABITS'] = self.DATABITS
        self.PARITY = RM_Field_USART3_FRAME_PARITY(self)
        self.zz_fdict['PARITY'] = self.PARITY
        self.STOPBITS = RM_Field_USART3_FRAME_STOPBITS(self)
        self.zz_fdict['STOPBITS'] = self.STOPBITS
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_TRIGCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_TRIGCTRL, self).__init__(rmio, label,
            0x40010c00, 0x008,
            'TRIGCTRL', 'USART3.TRIGCTRL', 'read-write',
            "",
            0x00000000, 0x000F1FF0)

        self.RXTEN = RM_Field_USART3_TRIGCTRL_RXTEN(self)
        self.zz_fdict['RXTEN'] = self.RXTEN
        self.TXTEN = RM_Field_USART3_TRIGCTRL_TXTEN(self)
        self.zz_fdict['TXTEN'] = self.TXTEN
        self.AUTOTXTEN = RM_Field_USART3_TRIGCTRL_AUTOTXTEN(self)
        self.zz_fdict['AUTOTXTEN'] = self.AUTOTXTEN
        self.TXARX0EN = RM_Field_USART3_TRIGCTRL_TXARX0EN(self)
        self.zz_fdict['TXARX0EN'] = self.TXARX0EN
        self.TXARX1EN = RM_Field_USART3_TRIGCTRL_TXARX1EN(self)
        self.zz_fdict['TXARX1EN'] = self.TXARX1EN
        self.TXARX2EN = RM_Field_USART3_TRIGCTRL_TXARX2EN(self)
        self.zz_fdict['TXARX2EN'] = self.TXARX2EN
        self.RXATX0EN = RM_Field_USART3_TRIGCTRL_RXATX0EN(self)
        self.zz_fdict['RXATX0EN'] = self.RXATX0EN
        self.RXATX1EN = RM_Field_USART3_TRIGCTRL_RXATX1EN(self)
        self.zz_fdict['RXATX1EN'] = self.RXATX1EN
        self.RXATX2EN = RM_Field_USART3_TRIGCTRL_RXATX2EN(self)
        self.zz_fdict['RXATX2EN'] = self.RXATX2EN
        self.TSEL = RM_Field_USART3_TRIGCTRL_TSEL(self)
        self.zz_fdict['TSEL'] = self.TSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_CMD, self).__init__(rmio, label,
            0x40010c00, 0x00C,
            'CMD', 'USART3.CMD', 'write-only',
            "",
            0x00000000, 0x00000FFF)

        self.RXEN = RM_Field_USART3_CMD_RXEN(self)
        self.zz_fdict['RXEN'] = self.RXEN
        self.RXDIS = RM_Field_USART3_CMD_RXDIS(self)
        self.zz_fdict['RXDIS'] = self.RXDIS
        self.TXEN = RM_Field_USART3_CMD_TXEN(self)
        self.zz_fdict['TXEN'] = self.TXEN
        self.TXDIS = RM_Field_USART3_CMD_TXDIS(self)
        self.zz_fdict['TXDIS'] = self.TXDIS
        self.MASTEREN = RM_Field_USART3_CMD_MASTEREN(self)
        self.zz_fdict['MASTEREN'] = self.MASTEREN
        self.MASTERDIS = RM_Field_USART3_CMD_MASTERDIS(self)
        self.zz_fdict['MASTERDIS'] = self.MASTERDIS
        self.RXBLOCKEN = RM_Field_USART3_CMD_RXBLOCKEN(self)
        self.zz_fdict['RXBLOCKEN'] = self.RXBLOCKEN
        self.RXBLOCKDIS = RM_Field_USART3_CMD_RXBLOCKDIS(self)
        self.zz_fdict['RXBLOCKDIS'] = self.RXBLOCKDIS
        self.TXTRIEN = RM_Field_USART3_CMD_TXTRIEN(self)
        self.zz_fdict['TXTRIEN'] = self.TXTRIEN
        self.TXTRIDIS = RM_Field_USART3_CMD_TXTRIDIS(self)
        self.zz_fdict['TXTRIDIS'] = self.TXTRIDIS
        self.CLEARTX = RM_Field_USART3_CMD_CLEARTX(self)
        self.zz_fdict['CLEARTX'] = self.CLEARTX
        self.CLEARRX = RM_Field_USART3_CMD_CLEARRX(self)
        self.zz_fdict['CLEARRX'] = self.CLEARRX
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_STATUS, self).__init__(rmio, label,
            0x40010c00, 0x010,
            'STATUS', 'USART3.STATUS', 'read-only',
            "",
            0x00002040, 0x00037FFF)

        self.RXENS = RM_Field_USART3_STATUS_RXENS(self)
        self.zz_fdict['RXENS'] = self.RXENS
        self.TXENS = RM_Field_USART3_STATUS_TXENS(self)
        self.zz_fdict['TXENS'] = self.TXENS
        self.MASTER = RM_Field_USART3_STATUS_MASTER(self)
        self.zz_fdict['MASTER'] = self.MASTER
        self.RXBLOCK = RM_Field_USART3_STATUS_RXBLOCK(self)
        self.zz_fdict['RXBLOCK'] = self.RXBLOCK
        self.TXTRI = RM_Field_USART3_STATUS_TXTRI(self)
        self.zz_fdict['TXTRI'] = self.TXTRI
        self.TXC = RM_Field_USART3_STATUS_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.TXBL = RM_Field_USART3_STATUS_TXBL(self)
        self.zz_fdict['TXBL'] = self.TXBL
        self.RXDATAV = RM_Field_USART3_STATUS_RXDATAV(self)
        self.zz_fdict['RXDATAV'] = self.RXDATAV
        self.RXFULL = RM_Field_USART3_STATUS_RXFULL(self)
        self.zz_fdict['RXFULL'] = self.RXFULL
        self.TXBDRIGHT = RM_Field_USART3_STATUS_TXBDRIGHT(self)
        self.zz_fdict['TXBDRIGHT'] = self.TXBDRIGHT
        self.TXBSRIGHT = RM_Field_USART3_STATUS_TXBSRIGHT(self)
        self.zz_fdict['TXBSRIGHT'] = self.TXBSRIGHT
        self.RXDATAVRIGHT = RM_Field_USART3_STATUS_RXDATAVRIGHT(self)
        self.zz_fdict['RXDATAVRIGHT'] = self.RXDATAVRIGHT
        self.RXFULLRIGHT = RM_Field_USART3_STATUS_RXFULLRIGHT(self)
        self.zz_fdict['RXFULLRIGHT'] = self.RXFULLRIGHT
        self.TXIDLE = RM_Field_USART3_STATUS_TXIDLE(self)
        self.zz_fdict['TXIDLE'] = self.TXIDLE
        self.TIMERRESTARTED = RM_Field_USART3_STATUS_TIMERRESTARTED(self)
        self.zz_fdict['TIMERRESTARTED'] = self.TIMERRESTARTED
        self.TXBUFCNT = RM_Field_USART3_STATUS_TXBUFCNT(self)
        self.zz_fdict['TXBUFCNT'] = self.TXBUFCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_CLKDIV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_CLKDIV, self).__init__(rmio, label,
            0x40010c00, 0x014,
            'CLKDIV', 'USART3.CLKDIV', 'read-write',
            "",
            0x00000000, 0x807FFFF8)

        self.DIV = RM_Field_USART3_CLKDIV_DIV(self)
        self.zz_fdict['DIV'] = self.DIV
        self.AUTOBAUDEN = RM_Field_USART3_CLKDIV_AUTOBAUDEN(self)
        self.zz_fdict['AUTOBAUDEN'] = self.AUTOBAUDEN
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_RXDATAX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_RXDATAX, self).__init__(rmio, label,
            0x40010c00, 0x018,
            'RXDATAX', 'USART3.RXDATAX', 'read-only',
            "",
            0x00000000, 0x0000C1FF)

        self.RXDATA = RM_Field_USART3_RXDATAX_RXDATA(self)
        self.zz_fdict['RXDATA'] = self.RXDATA
        self.PERR = RM_Field_USART3_RXDATAX_PERR(self)
        self.zz_fdict['PERR'] = self.PERR
        self.FERR = RM_Field_USART3_RXDATAX_FERR(self)
        self.zz_fdict['FERR'] = self.FERR
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_RXDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_RXDATA, self).__init__(rmio, label,
            0x40010c00, 0x01C,
            'RXDATA', 'USART3.RXDATA', 'read-only',
            "",
            0x00000000, 0x000000FF)

        self.RXDATA = RM_Field_USART3_RXDATA_RXDATA(self)
        self.zz_fdict['RXDATA'] = self.RXDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_RXDOUBLEX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_RXDOUBLEX, self).__init__(rmio, label,
            0x40010c00, 0x020,
            'RXDOUBLEX', 'USART3.RXDOUBLEX', 'read-only',
            "",
            0x00000000, 0xC1FFC1FF)

        self.RXDATA0 = RM_Field_USART3_RXDOUBLEX_RXDATA0(self)
        self.zz_fdict['RXDATA0'] = self.RXDATA0
        self.PERR0 = RM_Field_USART3_RXDOUBLEX_PERR0(self)
        self.zz_fdict['PERR0'] = self.PERR0
        self.FERR0 = RM_Field_USART3_RXDOUBLEX_FERR0(self)
        self.zz_fdict['FERR0'] = self.FERR0
        self.RXDATA1 = RM_Field_USART3_RXDOUBLEX_RXDATA1(self)
        self.zz_fdict['RXDATA1'] = self.RXDATA1
        self.PERR1 = RM_Field_USART3_RXDOUBLEX_PERR1(self)
        self.zz_fdict['PERR1'] = self.PERR1
        self.FERR1 = RM_Field_USART3_RXDOUBLEX_FERR1(self)
        self.zz_fdict['FERR1'] = self.FERR1
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_RXDOUBLE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_RXDOUBLE, self).__init__(rmio, label,
            0x40010c00, 0x024,
            'RXDOUBLE', 'USART3.RXDOUBLE', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.RXDATA0 = RM_Field_USART3_RXDOUBLE_RXDATA0(self)
        self.zz_fdict['RXDATA0'] = self.RXDATA0
        self.RXDATA1 = RM_Field_USART3_RXDOUBLE_RXDATA1(self)
        self.zz_fdict['RXDATA1'] = self.RXDATA1
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_RXDATAXP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_RXDATAXP, self).__init__(rmio, label,
            0x40010c00, 0x028,
            'RXDATAXP', 'USART3.RXDATAXP', 'read-only',
            "",
            0x00000000, 0x0000C1FF)

        self.RXDATAP = RM_Field_USART3_RXDATAXP_RXDATAP(self)
        self.zz_fdict['RXDATAP'] = self.RXDATAP
        self.PERRP = RM_Field_USART3_RXDATAXP_PERRP(self)
        self.zz_fdict['PERRP'] = self.PERRP
        self.FERRP = RM_Field_USART3_RXDATAXP_FERRP(self)
        self.zz_fdict['FERRP'] = self.FERRP
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_RXDOUBLEXP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_RXDOUBLEXP, self).__init__(rmio, label,
            0x40010c00, 0x02C,
            'RXDOUBLEXP', 'USART3.RXDOUBLEXP', 'read-only',
            "",
            0x00000000, 0xC1FFC1FF)

        self.RXDATAP0 = RM_Field_USART3_RXDOUBLEXP_RXDATAP0(self)
        self.zz_fdict['RXDATAP0'] = self.RXDATAP0
        self.PERRP0 = RM_Field_USART3_RXDOUBLEXP_PERRP0(self)
        self.zz_fdict['PERRP0'] = self.PERRP0
        self.FERRP0 = RM_Field_USART3_RXDOUBLEXP_FERRP0(self)
        self.zz_fdict['FERRP0'] = self.FERRP0
        self.RXDATAP1 = RM_Field_USART3_RXDOUBLEXP_RXDATAP1(self)
        self.zz_fdict['RXDATAP1'] = self.RXDATAP1
        self.PERRP1 = RM_Field_USART3_RXDOUBLEXP_PERRP1(self)
        self.zz_fdict['PERRP1'] = self.PERRP1
        self.FERRP1 = RM_Field_USART3_RXDOUBLEXP_FERRP1(self)
        self.zz_fdict['FERRP1'] = self.FERRP1
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_TXDATAX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_TXDATAX, self).__init__(rmio, label,
            0x40010c00, 0x030,
            'TXDATAX', 'USART3.TXDATAX', 'read-write',
            "",
            0x00000000, 0x0000F9FF)

        self.TXDATAX = RM_Field_USART3_TXDATAX_TXDATAX(self)
        self.zz_fdict['TXDATAX'] = self.TXDATAX
        self.UBRXAT = RM_Field_USART3_TXDATAX_UBRXAT(self)
        self.zz_fdict['UBRXAT'] = self.UBRXAT
        self.TXTRIAT = RM_Field_USART3_TXDATAX_TXTRIAT(self)
        self.zz_fdict['TXTRIAT'] = self.TXTRIAT
        self.TXBREAK = RM_Field_USART3_TXDATAX_TXBREAK(self)
        self.zz_fdict['TXBREAK'] = self.TXBREAK
        self.TXDISAT = RM_Field_USART3_TXDATAX_TXDISAT(self)
        self.zz_fdict['TXDISAT'] = self.TXDISAT
        self.RXENAT = RM_Field_USART3_TXDATAX_RXENAT(self)
        self.zz_fdict['RXENAT'] = self.RXENAT
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_TXDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_TXDATA, self).__init__(rmio, label,
            0x40010c00, 0x034,
            'TXDATA', 'USART3.TXDATA', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.TXDATA = RM_Field_USART3_TXDATA_TXDATA(self)
        self.zz_fdict['TXDATA'] = self.TXDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_TXDOUBLEX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_TXDOUBLEX, self).__init__(rmio, label,
            0x40010c00, 0x038,
            'TXDOUBLEX', 'USART3.TXDOUBLEX', 'read-write',
            "",
            0x00000000, 0xF9FFF9FF)

        self.TXDATA0 = RM_Field_USART3_TXDOUBLEX_TXDATA0(self)
        self.zz_fdict['TXDATA0'] = self.TXDATA0
        self.UBRXAT0 = RM_Field_USART3_TXDOUBLEX_UBRXAT0(self)
        self.zz_fdict['UBRXAT0'] = self.UBRXAT0
        self.TXTRIAT0 = RM_Field_USART3_TXDOUBLEX_TXTRIAT0(self)
        self.zz_fdict['TXTRIAT0'] = self.TXTRIAT0
        self.TXBREAK0 = RM_Field_USART3_TXDOUBLEX_TXBREAK0(self)
        self.zz_fdict['TXBREAK0'] = self.TXBREAK0
        self.TXDISAT0 = RM_Field_USART3_TXDOUBLEX_TXDISAT0(self)
        self.zz_fdict['TXDISAT0'] = self.TXDISAT0
        self.RXENAT0 = RM_Field_USART3_TXDOUBLEX_RXENAT0(self)
        self.zz_fdict['RXENAT0'] = self.RXENAT0
        self.TXDATA1 = RM_Field_USART3_TXDOUBLEX_TXDATA1(self)
        self.zz_fdict['TXDATA1'] = self.TXDATA1
        self.UBRXAT1 = RM_Field_USART3_TXDOUBLEX_UBRXAT1(self)
        self.zz_fdict['UBRXAT1'] = self.UBRXAT1
        self.TXTRIAT1 = RM_Field_USART3_TXDOUBLEX_TXTRIAT1(self)
        self.zz_fdict['TXTRIAT1'] = self.TXTRIAT1
        self.TXBREAK1 = RM_Field_USART3_TXDOUBLEX_TXBREAK1(self)
        self.zz_fdict['TXBREAK1'] = self.TXBREAK1
        self.TXDISAT1 = RM_Field_USART3_TXDOUBLEX_TXDISAT1(self)
        self.zz_fdict['TXDISAT1'] = self.TXDISAT1
        self.RXENAT1 = RM_Field_USART3_TXDOUBLEX_RXENAT1(self)
        self.zz_fdict['RXENAT1'] = self.RXENAT1
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_TXDOUBLE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_TXDOUBLE, self).__init__(rmio, label,
            0x40010c00, 0x03C,
            'TXDOUBLE', 'USART3.TXDOUBLE', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TXDATA0 = RM_Field_USART3_TXDOUBLE_TXDATA0(self)
        self.zz_fdict['TXDATA0'] = self.TXDATA0
        self.TXDATA1 = RM_Field_USART3_TXDOUBLE_TXDATA1(self)
        self.zz_fdict['TXDATA1'] = self.TXDATA1
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_IF, self).__init__(rmio, label,
            0x40010c00, 0x040,
            'IF', 'USART3.IF', 'read-only',
            "",
            0x00000002, 0x0001FFFF)

        self.TXC = RM_Field_USART3_IF_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.TXBL = RM_Field_USART3_IF_TXBL(self)
        self.zz_fdict['TXBL'] = self.TXBL
        self.RXDATAV = RM_Field_USART3_IF_RXDATAV(self)
        self.zz_fdict['RXDATAV'] = self.RXDATAV
        self.RXFULL = RM_Field_USART3_IF_RXFULL(self)
        self.zz_fdict['RXFULL'] = self.RXFULL
        self.RXOF = RM_Field_USART3_IF_RXOF(self)
        self.zz_fdict['RXOF'] = self.RXOF
        self.RXUF = RM_Field_USART3_IF_RXUF(self)
        self.zz_fdict['RXUF'] = self.RXUF
        self.TXOF = RM_Field_USART3_IF_TXOF(self)
        self.zz_fdict['TXOF'] = self.TXOF
        self.TXUF = RM_Field_USART3_IF_TXUF(self)
        self.zz_fdict['TXUF'] = self.TXUF
        self.PERR = RM_Field_USART3_IF_PERR(self)
        self.zz_fdict['PERR'] = self.PERR
        self.FERR = RM_Field_USART3_IF_FERR(self)
        self.zz_fdict['FERR'] = self.FERR
        self.MPAF = RM_Field_USART3_IF_MPAF(self)
        self.zz_fdict['MPAF'] = self.MPAF
        self.SSM = RM_Field_USART3_IF_SSM(self)
        self.zz_fdict['SSM'] = self.SSM
        self.CCF = RM_Field_USART3_IF_CCF(self)
        self.zz_fdict['CCF'] = self.CCF
        self.TXIDLE = RM_Field_USART3_IF_TXIDLE(self)
        self.zz_fdict['TXIDLE'] = self.TXIDLE
        self.TCMP0 = RM_Field_USART3_IF_TCMP0(self)
        self.zz_fdict['TCMP0'] = self.TCMP0
        self.TCMP1 = RM_Field_USART3_IF_TCMP1(self)
        self.zz_fdict['TCMP1'] = self.TCMP1
        self.TCMP2 = RM_Field_USART3_IF_TCMP2(self)
        self.zz_fdict['TCMP2'] = self.TCMP2
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_IFS, self).__init__(rmio, label,
            0x40010c00, 0x044,
            'IFS', 'USART3.IFS', 'write-only',
            "",
            0x00000000, 0x0001FFF9)

        self.TXC = RM_Field_USART3_IFS_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.RXFULL = RM_Field_USART3_IFS_RXFULL(self)
        self.zz_fdict['RXFULL'] = self.RXFULL
        self.RXOF = RM_Field_USART3_IFS_RXOF(self)
        self.zz_fdict['RXOF'] = self.RXOF
        self.RXUF = RM_Field_USART3_IFS_RXUF(self)
        self.zz_fdict['RXUF'] = self.RXUF
        self.TXOF = RM_Field_USART3_IFS_TXOF(self)
        self.zz_fdict['TXOF'] = self.TXOF
        self.TXUF = RM_Field_USART3_IFS_TXUF(self)
        self.zz_fdict['TXUF'] = self.TXUF
        self.PERR = RM_Field_USART3_IFS_PERR(self)
        self.zz_fdict['PERR'] = self.PERR
        self.FERR = RM_Field_USART3_IFS_FERR(self)
        self.zz_fdict['FERR'] = self.FERR
        self.MPAF = RM_Field_USART3_IFS_MPAF(self)
        self.zz_fdict['MPAF'] = self.MPAF
        self.SSM = RM_Field_USART3_IFS_SSM(self)
        self.zz_fdict['SSM'] = self.SSM
        self.CCF = RM_Field_USART3_IFS_CCF(self)
        self.zz_fdict['CCF'] = self.CCF
        self.TXIDLE = RM_Field_USART3_IFS_TXIDLE(self)
        self.zz_fdict['TXIDLE'] = self.TXIDLE
        self.TCMP0 = RM_Field_USART3_IFS_TCMP0(self)
        self.zz_fdict['TCMP0'] = self.TCMP0
        self.TCMP1 = RM_Field_USART3_IFS_TCMP1(self)
        self.zz_fdict['TCMP1'] = self.TCMP1
        self.TCMP2 = RM_Field_USART3_IFS_TCMP2(self)
        self.zz_fdict['TCMP2'] = self.TCMP2
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_IFC, self).__init__(rmio, label,
            0x40010c00, 0x048,
            'IFC', 'USART3.IFC', 'write-only',
            "",
            0x00000000, 0x0001FFF9)

        self.TXC = RM_Field_USART3_IFC_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.RXFULL = RM_Field_USART3_IFC_RXFULL(self)
        self.zz_fdict['RXFULL'] = self.RXFULL
        self.RXOF = RM_Field_USART3_IFC_RXOF(self)
        self.zz_fdict['RXOF'] = self.RXOF
        self.RXUF = RM_Field_USART3_IFC_RXUF(self)
        self.zz_fdict['RXUF'] = self.RXUF
        self.TXOF = RM_Field_USART3_IFC_TXOF(self)
        self.zz_fdict['TXOF'] = self.TXOF
        self.TXUF = RM_Field_USART3_IFC_TXUF(self)
        self.zz_fdict['TXUF'] = self.TXUF
        self.PERR = RM_Field_USART3_IFC_PERR(self)
        self.zz_fdict['PERR'] = self.PERR
        self.FERR = RM_Field_USART3_IFC_FERR(self)
        self.zz_fdict['FERR'] = self.FERR
        self.MPAF = RM_Field_USART3_IFC_MPAF(self)
        self.zz_fdict['MPAF'] = self.MPAF
        self.SSM = RM_Field_USART3_IFC_SSM(self)
        self.zz_fdict['SSM'] = self.SSM
        self.CCF = RM_Field_USART3_IFC_CCF(self)
        self.zz_fdict['CCF'] = self.CCF
        self.TXIDLE = RM_Field_USART3_IFC_TXIDLE(self)
        self.zz_fdict['TXIDLE'] = self.TXIDLE
        self.TCMP0 = RM_Field_USART3_IFC_TCMP0(self)
        self.zz_fdict['TCMP0'] = self.TCMP0
        self.TCMP1 = RM_Field_USART3_IFC_TCMP1(self)
        self.zz_fdict['TCMP1'] = self.TCMP1
        self.TCMP2 = RM_Field_USART3_IFC_TCMP2(self)
        self.zz_fdict['TCMP2'] = self.TCMP2
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_IEN, self).__init__(rmio, label,
            0x40010c00, 0x04C,
            'IEN', 'USART3.IEN', 'read-write',
            "",
            0x00000000, 0x0001FFFF)

        self.TXC = RM_Field_USART3_IEN_TXC(self)
        self.zz_fdict['TXC'] = self.TXC
        self.TXBL = RM_Field_USART3_IEN_TXBL(self)
        self.zz_fdict['TXBL'] = self.TXBL
        self.RXDATAV = RM_Field_USART3_IEN_RXDATAV(self)
        self.zz_fdict['RXDATAV'] = self.RXDATAV
        self.RXFULL = RM_Field_USART3_IEN_RXFULL(self)
        self.zz_fdict['RXFULL'] = self.RXFULL
        self.RXOF = RM_Field_USART3_IEN_RXOF(self)
        self.zz_fdict['RXOF'] = self.RXOF
        self.RXUF = RM_Field_USART3_IEN_RXUF(self)
        self.zz_fdict['RXUF'] = self.RXUF
        self.TXOF = RM_Field_USART3_IEN_TXOF(self)
        self.zz_fdict['TXOF'] = self.TXOF
        self.TXUF = RM_Field_USART3_IEN_TXUF(self)
        self.zz_fdict['TXUF'] = self.TXUF
        self.PERR = RM_Field_USART3_IEN_PERR(self)
        self.zz_fdict['PERR'] = self.PERR
        self.FERR = RM_Field_USART3_IEN_FERR(self)
        self.zz_fdict['FERR'] = self.FERR
        self.MPAF = RM_Field_USART3_IEN_MPAF(self)
        self.zz_fdict['MPAF'] = self.MPAF
        self.SSM = RM_Field_USART3_IEN_SSM(self)
        self.zz_fdict['SSM'] = self.SSM
        self.CCF = RM_Field_USART3_IEN_CCF(self)
        self.zz_fdict['CCF'] = self.CCF
        self.TXIDLE = RM_Field_USART3_IEN_TXIDLE(self)
        self.zz_fdict['TXIDLE'] = self.TXIDLE
        self.TCMP0 = RM_Field_USART3_IEN_TCMP0(self)
        self.zz_fdict['TCMP0'] = self.TCMP0
        self.TCMP1 = RM_Field_USART3_IEN_TCMP1(self)
        self.zz_fdict['TCMP1'] = self.TCMP1
        self.TCMP2 = RM_Field_USART3_IEN_TCMP2(self)
        self.zz_fdict['TCMP2'] = self.TCMP2
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_IRCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_IRCTRL, self).__init__(rmio, label,
            0x40010c00, 0x050,
            'IRCTRL', 'USART3.IRCTRL', 'read-write',
            "",
            0x00000000, 0x00000F8F)

        self.IREN = RM_Field_USART3_IRCTRL_IREN(self)
        self.zz_fdict['IREN'] = self.IREN
        self.IRPW = RM_Field_USART3_IRCTRL_IRPW(self)
        self.zz_fdict['IRPW'] = self.IRPW
        self.IRFILT = RM_Field_USART3_IRCTRL_IRFILT(self)
        self.zz_fdict['IRFILT'] = self.IRFILT
        self.IRPRSEN = RM_Field_USART3_IRCTRL_IRPRSEN(self)
        self.zz_fdict['IRPRSEN'] = self.IRPRSEN
        self.IRPRSSEL = RM_Field_USART3_IRCTRL_IRPRSSEL(self)
        self.zz_fdict['IRPRSSEL'] = self.IRPRSSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_INPUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_INPUT, self).__init__(rmio, label,
            0x40010c00, 0x058,
            'INPUT', 'USART3.INPUT', 'read-write',
            "",
            0x00000000, 0x00008F8F)

        self.RXPRSSEL = RM_Field_USART3_INPUT_RXPRSSEL(self)
        self.zz_fdict['RXPRSSEL'] = self.RXPRSSEL
        self.RXPRS = RM_Field_USART3_INPUT_RXPRS(self)
        self.zz_fdict['RXPRS'] = self.RXPRS
        self.CLKPRSSEL = RM_Field_USART3_INPUT_CLKPRSSEL(self)
        self.zz_fdict['CLKPRSSEL'] = self.CLKPRSSEL
        self.CLKPRS = RM_Field_USART3_INPUT_CLKPRS(self)
        self.zz_fdict['CLKPRS'] = self.CLKPRS
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_I2SCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_I2SCTRL, self).__init__(rmio, label,
            0x40010c00, 0x05C,
            'I2SCTRL', 'USART3.I2SCTRL', 'read-write',
            "",
            0x00000000, 0x0000071F)

        self.EN = RM_Field_USART3_I2SCTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.MONO = RM_Field_USART3_I2SCTRL_MONO(self)
        self.zz_fdict['MONO'] = self.MONO
        self.JUSTIFY = RM_Field_USART3_I2SCTRL_JUSTIFY(self)
        self.zz_fdict['JUSTIFY'] = self.JUSTIFY
        self.DMASPLIT = RM_Field_USART3_I2SCTRL_DMASPLIT(self)
        self.zz_fdict['DMASPLIT'] = self.DMASPLIT
        self.DELAY = RM_Field_USART3_I2SCTRL_DELAY(self)
        self.zz_fdict['DELAY'] = self.DELAY
        self.FORMAT = RM_Field_USART3_I2SCTRL_FORMAT(self)
        self.zz_fdict['FORMAT'] = self.FORMAT
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_TIMING, self).__init__(rmio, label,
            0x40010c00, 0x060,
            'TIMING', 'USART3.TIMING', 'read-write',
            "",
            0x00000000, 0x77770000)

        self.TXDELAY = RM_Field_USART3_TIMING_TXDELAY(self)
        self.zz_fdict['TXDELAY'] = self.TXDELAY
        self.CSSETUP = RM_Field_USART3_TIMING_CSSETUP(self)
        self.zz_fdict['CSSETUP'] = self.CSSETUP
        self.ICS = RM_Field_USART3_TIMING_ICS(self)
        self.zz_fdict['ICS'] = self.ICS
        self.CSHOLD = RM_Field_USART3_TIMING_CSHOLD(self)
        self.zz_fdict['CSHOLD'] = self.CSHOLD
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_CTRLX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_CTRLX, self).__init__(rmio, label,
            0x40010c00, 0x064,
            'CTRLX', 'USART3.CTRLX', 'read-write',
            "",
            0x00000000, 0x8000000F)

        self.DBGHALT = RM_Field_USART3_CTRLX_DBGHALT(self)
        self.zz_fdict['DBGHALT'] = self.DBGHALT
        self.CTSINV = RM_Field_USART3_CTRLX_CTSINV(self)
        self.zz_fdict['CTSINV'] = self.CTSINV
        self.CTSEN = RM_Field_USART3_CTRLX_CTSEN(self)
        self.zz_fdict['CTSEN'] = self.CTSEN
        self.RTSINV = RM_Field_USART3_CTRLX_RTSINV(self)
        self.zz_fdict['RTSINV'] = self.RTSINV
        self.GPIODELAYXOREN = RM_Field_USART3_CTRLX_GPIODELAYXOREN(self)
        self.zz_fdict['GPIODELAYXOREN'] = self.GPIODELAYXOREN
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_TIMECMP0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_TIMECMP0, self).__init__(rmio, label,
            0x40010c00, 0x068,
            'TIMECMP0', 'USART3.TIMECMP0', 'read-write',
            "",
            0x00000000, 0x017700FF)

        self.TCMPVAL = RM_Field_USART3_TIMECMP0_TCMPVAL(self)
        self.zz_fdict['TCMPVAL'] = self.TCMPVAL
        self.TSTART = RM_Field_USART3_TIMECMP0_TSTART(self)
        self.zz_fdict['TSTART'] = self.TSTART
        self.TSTOP = RM_Field_USART3_TIMECMP0_TSTOP(self)
        self.zz_fdict['TSTOP'] = self.TSTOP
        self.RESTARTEN = RM_Field_USART3_TIMECMP0_RESTARTEN(self)
        self.zz_fdict['RESTARTEN'] = self.RESTARTEN
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_TIMECMP1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_TIMECMP1, self).__init__(rmio, label,
            0x40010c00, 0x06C,
            'TIMECMP1', 'USART3.TIMECMP1', 'read-write',
            "",
            0x00000000, 0x017700FF)

        self.TCMPVAL = RM_Field_USART3_TIMECMP1_TCMPVAL(self)
        self.zz_fdict['TCMPVAL'] = self.TCMPVAL
        self.TSTART = RM_Field_USART3_TIMECMP1_TSTART(self)
        self.zz_fdict['TSTART'] = self.TSTART
        self.TSTOP = RM_Field_USART3_TIMECMP1_TSTOP(self)
        self.zz_fdict['TSTOP'] = self.TSTOP
        self.RESTARTEN = RM_Field_USART3_TIMECMP1_RESTARTEN(self)
        self.zz_fdict['RESTARTEN'] = self.RESTARTEN
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_TIMECMP2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_TIMECMP2, self).__init__(rmio, label,
            0x40010c00, 0x070,
            'TIMECMP2', 'USART3.TIMECMP2', 'read-write',
            "",
            0x00000000, 0x017700FF)

        self.TCMPVAL = RM_Field_USART3_TIMECMP2_TCMPVAL(self)
        self.zz_fdict['TCMPVAL'] = self.TCMPVAL
        self.TSTART = RM_Field_USART3_TIMECMP2_TSTART(self)
        self.zz_fdict['TSTART'] = self.TSTART
        self.TSTOP = RM_Field_USART3_TIMECMP2_TSTOP(self)
        self.zz_fdict['TSTOP'] = self.TSTOP
        self.RESTARTEN = RM_Field_USART3_TIMECMP2_RESTARTEN(self)
        self.zz_fdict['RESTARTEN'] = self.RESTARTEN
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_ROUTEPEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_ROUTEPEN, self).__init__(rmio, label,
            0x40010c00, 0x074,
            'ROUTEPEN', 'USART3.ROUTEPEN', 'read-write',
            "",
            0x00000000, 0x0000003F)

        self.RXPEN = RM_Field_USART3_ROUTEPEN_RXPEN(self)
        self.zz_fdict['RXPEN'] = self.RXPEN
        self.TXPEN = RM_Field_USART3_ROUTEPEN_TXPEN(self)
        self.zz_fdict['TXPEN'] = self.TXPEN
        self.CSPEN = RM_Field_USART3_ROUTEPEN_CSPEN(self)
        self.zz_fdict['CSPEN'] = self.CSPEN
        self.CLKPEN = RM_Field_USART3_ROUTEPEN_CLKPEN(self)
        self.zz_fdict['CLKPEN'] = self.CLKPEN
        self.CTSPEN = RM_Field_USART3_ROUTEPEN_CTSPEN(self)
        self.zz_fdict['CTSPEN'] = self.CTSPEN
        self.RTSPEN = RM_Field_USART3_ROUTEPEN_RTSPEN(self)
        self.zz_fdict['RTSPEN'] = self.RTSPEN
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_ROUTELOC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_ROUTELOC0, self).__init__(rmio, label,
            0x40010c00, 0x078,
            'ROUTELOC0', 'USART3.ROUTELOC0', 'read-write',
            "",
            0x00000000, 0x3F3F3F3F)

        self.RXLOC = RM_Field_USART3_ROUTELOC0_RXLOC(self)
        self.zz_fdict['RXLOC'] = self.RXLOC
        self.TXLOC = RM_Field_USART3_ROUTELOC0_TXLOC(self)
        self.zz_fdict['TXLOC'] = self.TXLOC
        self.CSLOC = RM_Field_USART3_ROUTELOC0_CSLOC(self)
        self.zz_fdict['CSLOC'] = self.CSLOC
        self.CLKLOC = RM_Field_USART3_ROUTELOC0_CLKLOC(self)
        self.zz_fdict['CLKLOC'] = self.CLKLOC
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_ROUTELOC1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_ROUTELOC1, self).__init__(rmio, label,
            0x40010c00, 0x07C,
            'ROUTELOC1', 'USART3.ROUTELOC1', 'read-write',
            "",
            0x00000000, 0x00003F3F)

        self.CTSLOC = RM_Field_USART3_ROUTELOC1_CTSLOC(self)
        self.zz_fdict['CTSLOC'] = self.CTSLOC
        self.RTSLOC = RM_Field_USART3_ROUTELOC1_RTSLOC(self)
        self.zz_fdict['RTSLOC'] = self.RTSLOC
        self.__dict__['zz_frozen'] = True


class RM_Register_USART3_TEST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_USART3_TEST, self).__init__(rmio, label,
            0x40010c00, 0x080,
            'TEST', 'USART3.TEST', 'read-only',
            "",
            0x00000000, 0x00000003)

        self.GPIODELAYSTABLE = RM_Field_USART3_TEST_GPIODELAYSTABLE(self)
        self.zz_fdict['GPIODELAYSTABLE'] = self.GPIODELAYSTABLE
        self.GPIODELAYXOR = RM_Field_USART3_TEST_GPIODELAYXOR(self)
        self.zz_fdict['GPIODELAYXOR'] = self.GPIODELAYXOR
        self.__dict__['zz_frozen'] = True


