
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_MODEM_STATUS_DEMODSTATE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.OFF = 0x00000000
        zz_edict['OFF'] = self.OFF
        zz_desc['OFF'] = ""
        self.TIMINGSEARCH = 0x00000001
        zz_edict['TIMINGSEARCH'] = self.TIMINGSEARCH
        zz_desc['TIMINGSEARCH'] = ""
        self.PRESEARCH = 0x00000002
        zz_edict['PRESEARCH'] = self.PRESEARCH
        zz_desc['PRESEARCH'] = ""
        self.FRAMESEARCH = 0x00000003
        zz_edict['FRAMESEARCH'] = self.FRAMESEARCH
        zz_desc['FRAMESEARCH'] = ""
        self.RXFRAME = 0x00000004
        zz_edict['RXFRAME'] = self.RXFRAME
        zz_desc['RXFRAME'] = ""
        self.FRAMEDETMODE0 = 0x00000005
        zz_edict['FRAMEDETMODE0'] = self.FRAMEDETMODE0
        zz_desc['FRAMEDETMODE0'] = ""
        super(RM_Enum_MODEM_STATUS_DEMODSTATE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_MIXCTRL_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NORMAL = 0x00000000
        zz_edict['NORMAL'] = self.NORMAL
        zz_desc['NORMAL'] = ""
        self.CONJUGATE = 0x00000002
        zz_edict['CONJUGATE'] = self.CONJUGATE
        zz_desc['CONJUGATE'] = ""
        super(RM_Enum_MODEM_MIXCTRL_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL0_MAPFSK(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.MAP0 = 0x00000000
        zz_edict['MAP0'] = self.MAP0
        zz_desc['MAP0'] = ""
        self.MAP1 = 0x00000001
        zz_edict['MAP1'] = self.MAP1
        zz_desc['MAP1'] = ""
        self.MAP2 = 0x00000002
        zz_edict['MAP2'] = self.MAP2
        zz_desc['MAP2'] = ""
        self.MAP3 = 0x00000003
        zz_edict['MAP3'] = self.MAP3
        zz_desc['MAP3'] = ""
        self.MAP4 = 0x00000004
        zz_edict['MAP4'] = self.MAP4
        zz_desc['MAP4'] = ""
        self.MAP5 = 0x00000005
        zz_edict['MAP5'] = self.MAP5
        zz_desc['MAP5'] = ""
        self.MAP6 = 0x00000006
        zz_edict['MAP6'] = self.MAP6
        zz_desc['MAP6'] = ""
        self.MAP7 = 0x00000007
        zz_edict['MAP7'] = self.MAP7
        zz_desc['MAP7'] = ""
        super(RM_Enum_MODEM_CTRL0_MAPFSK, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL0_CODING(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NRZ = 0x00000000
        zz_edict['NRZ'] = self.NRZ
        zz_desc['NRZ'] = ""
        self.MANCHESTER = 0x00000001
        zz_edict['MANCHESTER'] = self.MANCHESTER
        zz_desc['MANCHESTER'] = ""
        self.DSSS = 0x00000002
        zz_edict['DSSS'] = self.DSSS
        zz_desc['DSSS'] = ""
        super(RM_Enum_MODEM_CTRL0_CODING, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL0_MODFORMAT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.FSK2 = 0x00000000
        zz_edict['FSK2'] = self.FSK2
        zz_desc['FSK2'] = ""
        self.FSK4 = 0x00000001
        zz_edict['FSK4'] = self.FSK4
        zz_desc['FSK4'] = ""
        self.BPSK = 0x00000002
        zz_edict['BPSK'] = self.BPSK
        zz_desc['BPSK'] = ""
        self.DBPSK = 0x00000003
        zz_edict['DBPSK'] = self.DBPSK
        zz_desc['DBPSK'] = ""
        self.OQPSK = 0x00000004
        zz_edict['OQPSK'] = self.OQPSK
        zz_desc['OQPSK'] = ""
        self.MSK = 0x00000005
        zz_edict['MSK'] = self.MSK
        zz_desc['MSK'] = ""
        self.OOKASK = 0x00000006
        zz_edict['OOKASK'] = self.OOKASK
        zz_desc['OOKASK'] = ""
        super(RM_Enum_MODEM_CTRL0_MODFORMAT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL0_DSSSSHIFTS(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NOSHIFT = 0x00000000
        zz_edict['NOSHIFT'] = self.NOSHIFT
        zz_desc['NOSHIFT'] = ""
        self.SHIFT1 = 0x00000001
        zz_edict['SHIFT1'] = self.SHIFT1
        zz_desc['SHIFT1'] = ""
        self.SHIFT2 = 0x00000002
        zz_edict['SHIFT2'] = self.SHIFT2
        zz_desc['SHIFT2'] = ""
        self.SHIFT4 = 0x00000003
        zz_edict['SHIFT4'] = self.SHIFT4
        zz_desc['SHIFT4'] = ""
        self.SHIFT8 = 0x00000004
        zz_edict['SHIFT8'] = self.SHIFT8
        zz_desc['SHIFT8'] = ""
        self.SHIFT16 = 0x00000005
        zz_edict['SHIFT16'] = self.SHIFT16
        zz_desc['SHIFT16'] = ""
        super(RM_Enum_MODEM_CTRL0_DSSSSHIFTS, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL0_DSSSDOUBLE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIS = 0x00000000
        zz_edict['DIS'] = self.DIS
        zz_desc['DIS'] = ""
        self.INV = 0x00000001
        zz_edict['INV'] = self.INV
        zz_desc['INV'] = ""
        self.CONJ = 0x00000002
        zz_edict['CONJ'] = self.CONJ
        zz_desc['CONJ'] = ""
        super(RM_Enum_MODEM_CTRL0_DSSSDOUBLE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL0_DIFFENCMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIS = 0x00000000
        zz_edict['DIS'] = self.DIS
        zz_desc['DIS'] = ""
        self.RR0 = 0x00000001
        zz_edict['RR0'] = self.RR0
        zz_desc['RR0'] = ""
        self.RE0 = 0x00000002
        zz_edict['RE0'] = self.RE0
        zz_desc['RE0'] = ""
        self.RR1 = 0x00000003
        zz_edict['RR1'] = self.RR1
        zz_desc['RR1'] = ""
        self.RE1 = 0x00000004
        zz_edict['RE1'] = self.RE1
        zz_desc['RE1'] = ""
        super(RM_Enum_MODEM_CTRL0_DIFFENCMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL0_SHAPING(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.ODDLENGTH = 0x00000001
        zz_edict['ODDLENGTH'] = self.ODDLENGTH
        zz_desc['ODDLENGTH'] = ""
        self.EVENLENGTH = 0x00000002
        zz_edict['EVENLENGTH'] = self.EVENLENGTH
        zz_desc['EVENLENGTH'] = ""
        self.ASYMMETRIC = 0x00000003
        zz_edict['ASYMMETRIC'] = self.ASYMMETRIC
        zz_desc['ASYMMETRIC'] = ""
        super(RM_Enum_MODEM_CTRL0_SHAPING, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL0_DEMODRAWDATASEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIS = 0x00000000
        zz_edict['DIS'] = self.DIS
        zz_desc['DIS'] = ""
        self.ENTROPY = 0x00000001
        zz_edict['ENTROPY'] = self.ENTROPY
        zz_desc['ENTROPY'] = ""
        self.ADC = 0x00000002
        zz_edict['ADC'] = self.ADC
        zz_desc['ADC'] = ""
        self.FILTLSB = 0x00000003
        zz_edict['FILTLSB'] = self.FILTLSB
        zz_desc['FILTLSB'] = ""
        self.FILTMSB = 0x00000004
        zz_edict['FILTMSB'] = self.FILTMSB
        zz_desc['FILTMSB'] = ""
        self.FILTFULL = 0x00000005
        zz_edict['FILTFULL'] = self.FILTFULL
        zz_desc['FILTFULL'] = ""
        self.FREQ = 0x00000006
        zz_edict['FREQ'] = self.FREQ
        zz_desc['FREQ'] = ""
        self.DEMOD = 0x00000007
        zz_edict['DEMOD'] = self.DEMOD
        zz_desc['DEMOD'] = ""
        super(RM_Enum_MODEM_CTRL0_DEMODRAWDATASEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL0_FRAMEDETDEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DEL0 = 0x00000000
        zz_edict['DEL0'] = self.DEL0
        zz_desc['DEL0'] = ""
        self.DEL8 = 0x00000001
        zz_edict['DEL8'] = self.DEL8
        zz_desc['DEL8'] = ""
        self.DEL16 = 0x00000002
        zz_edict['DEL16'] = self.DEL16
        zz_desc['DEL16'] = ""
        self.DEL32 = 0x00000003
        zz_edict['DEL32'] = self.DEL32
        zz_desc['DEL32'] = ""
        super(RM_Enum_MODEM_CTRL0_FRAMEDETDEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL1_COMPMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIS = 0x00000000
        zz_edict['DIS'] = self.DIS
        zz_desc['DIS'] = ""
        self.PRELOCK = 0x00000001
        zz_edict['PRELOCK'] = self.PRELOCK
        zz_desc['PRELOCK'] = ""
        self.FRAMELOCK = 0x00000002
        zz_edict['FRAMELOCK'] = self.FRAMELOCK
        zz_desc['FRAMELOCK'] = ""
        self.NOLOCK = 0x00000003
        zz_edict['NOLOCK'] = self.NOLOCK
        zz_desc['NOLOCK'] = ""
        super(RM_Enum_MODEM_CTRL1_COMPMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL1_PHASEDEMOD(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.BDD = 0x00000000
        zz_edict['BDD'] = self.BDD
        zz_desc['BDD'] = ""
        self.MBDD = 0x00000001
        zz_edict['MBDD'] = self.MBDD
        zz_desc['MBDD'] = ""
        self.POC = 0x00000002
        zz_edict['POC'] = self.POC
        zz_desc['POC'] = ""
        super(RM_Enum_MODEM_CTRL1_PHASEDEMOD, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL2_TXPINMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.OFF = 0x00000000
        zz_edict['OFF'] = self.OFF
        zz_desc['OFF'] = ""
        self.UNUSED = 0x00000001
        zz_edict['UNUSED'] = self.UNUSED
        zz_desc['UNUSED'] = ""
        self.ASYNCHRONOUS = 0x00000002
        zz_edict['ASYNCHRONOUS'] = self.ASYNCHRONOUS
        zz_desc['ASYNCHRONOUS'] = ""
        self.SYNCHRONOUS = 0x00000003
        zz_edict['SYNCHRONOUS'] = self.SYNCHRONOUS
        zz_desc['SYNCHRONOUS'] = ""
        super(RM_Enum_MODEM_CTRL2_TXPINMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL2_DATAFILTER(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DISABLED = 0x00000000
        zz_edict['DISABLED'] = self.DISABLED
        zz_desc['DISABLED'] = ""
        self.SHORT = 0x00000001
        zz_edict['SHORT'] = self.SHORT
        zz_desc['SHORT'] = ""
        self.MEDIUM = 0x00000002
        zz_edict['MEDIUM'] = self.MEDIUM
        zz_desc['MEDIUM'] = ""
        self.LONG = 0x00000003
        zz_edict['LONG'] = self.LONG
        zz_desc['LONG'] = ""
        super(RM_Enum_MODEM_CTRL2_DATAFILTER, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL2_RATESELMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.NOCHANGE = 0x00000000
        zz_edict['NOCHANGE'] = self.NOCHANGE
        zz_desc['NOCHANGE'] = ""
        self.PAYLOAD = 0x00000001
        zz_edict['PAYLOAD'] = self.PAYLOAD
        zz_desc['PAYLOAD'] = ""
        self.FRC     = 0x00000002
        zz_edict['FRC    '] = self.FRC    
        zz_desc['FRC    '] = ""
        self.SYNC    = 0x00000003
        zz_edict['SYNC   '] = self.SYNC   
        zz_desc['SYNC   '] = ""
        super(RM_Enum_MODEM_CTRL2_RATESELMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL2_DMASEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.SOFT = 0x00000000
        zz_edict['SOFT'] = self.SOFT
        zz_desc['SOFT'] = ""
        self.CORR = 0x00000001
        zz_edict['CORR'] = self.CORR
        zz_desc['CORR'] = ""
        self.FREQOFFEST = 0x00000002
        zz_edict['FREQOFFEST'] = self.FREQOFFEST
        zz_desc['FREQOFFEST'] = ""
        self.POE = 0x00000003
        zz_edict['POE'] = self.POE
        zz_desc['POE'] = ""
        super(RM_Enum_MODEM_CTRL2_DMASEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL3_PRSDINSEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PRSCH0 = 0x00000000
        zz_edict['PRSCH0'] = self.PRSCH0
        zz_desc['PRSCH0'] = ""
        self.PRSCH1 = 0x00000001
        zz_edict['PRSCH1'] = self.PRSCH1
        zz_desc['PRSCH1'] = ""
        self.PRSCH2 = 0x00000002
        zz_edict['PRSCH2'] = self.PRSCH2
        zz_desc['PRSCH2'] = ""
        self.PRSCH3 = 0x00000003
        zz_edict['PRSCH3'] = self.PRSCH3
        zz_desc['PRSCH3'] = ""
        self.PRSCH4 = 0x00000004
        zz_edict['PRSCH4'] = self.PRSCH4
        zz_desc['PRSCH4'] = ""
        self.PRSCH5 = 0x00000005
        zz_edict['PRSCH5'] = self.PRSCH5
        zz_desc['PRSCH5'] = ""
        self.PRSCH6 = 0x00000006
        zz_edict['PRSCH6'] = self.PRSCH6
        zz_desc['PRSCH6'] = ""
        self.PRSCH7 = 0x00000007
        zz_edict['PRSCH7'] = self.PRSCH7
        zz_desc['PRSCH7'] = ""
        self.PRSCH8 = 0x00000008
        zz_edict['PRSCH8'] = self.PRSCH8
        zz_desc['PRSCH8'] = ""
        self.PRSCH9 = 0x00000009
        zz_edict['PRSCH9'] = self.PRSCH9
        zz_desc['PRSCH9'] = ""
        self.PRSCH10 = 0x0000000A
        zz_edict['PRSCH10'] = self.PRSCH10
        zz_desc['PRSCH10'] = ""
        self.PRSCH11 = 0x0000000B
        zz_edict['PRSCH11'] = self.PRSCH11
        zz_desc['PRSCH11'] = ""
        super(RM_Enum_MODEM_CTRL3_PRSDINSEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL3_ANTDIVMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ANTENNA0 = 0x00000000
        zz_edict['ANTENNA0'] = self.ANTENNA0
        zz_desc['ANTENNA0'] = ""
        self.ANTENNA1 = 0x00000001
        zz_edict['ANTENNA1'] = self.ANTENNA1
        zz_desc['ANTENNA1'] = ""
        self.ANTSELFIRST = 0x00000002
        zz_edict['ANTSELFIRST'] = self.ANTSELFIRST
        zz_desc['ANTSELFIRST'] = ""
        self.ANTSELCORR = 0x00000003
        zz_edict['ANTSELCORR'] = self.ANTSELCORR
        zz_desc['ANTSELCORR'] = ""
        self.ANTSELRSSI = 0x00000004
        zz_edict['ANTSELRSSI'] = self.ANTSELRSSI
        zz_desc['ANTSELRSSI'] = ""
        super(RM_Enum_MODEM_CTRL3_ANTDIVMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL3_TSAMPMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.OFF = 0x00000000
        zz_edict['OFF'] = self.OFF
        zz_desc['OFF'] = ""
        self.ON = 0x00000001
        zz_edict['ON'] = self.ON
        zz_desc['ON'] = ""
        super(RM_Enum_MODEM_CTRL3_TSAMPMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL4_ADCSATLEVEL(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CONS1 = 0x00000000
        zz_edict['CONS1'] = self.CONS1
        zz_desc['CONS1'] = ""
        self.CONS2 = 0x00000001
        zz_edict['CONS2'] = self.CONS2
        zz_desc['CONS2'] = ""
        self.CONS4 = 0x00000002
        zz_edict['CONS4'] = self.CONS4
        zz_desc['CONS4'] = ""
        self.CONS8 = 0x00000003
        zz_edict['CONS8'] = self.CONS8
        zz_desc['CONS8'] = ""
        self.CONS16 = 0x00000004
        zz_edict['CONS16'] = self.CONS16
        zz_desc['CONS16'] = ""
        self.CONS32 = 0x00000005
        zz_edict['CONS32'] = self.CONS32
        zz_desc['CONS32'] = ""
        self.CONS64 = 0x00000006
        zz_edict['CONS64'] = self.CONS64
        zz_desc['CONS64'] = ""
        super(RM_Enum_MODEM_CTRL4_ADCSATLEVEL, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CTRL5_BRCALMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.PEAK = 0x00000000
        zz_edict['PEAK'] = self.PEAK
        zz_desc['PEAK'] = ""
        self.ZERO = 0x00000001
        zz_edict['ZERO'] = self.ZERO
        zz_desc['ZERO'] = ""
        self.PEAKZERO = 0x00000002
        zz_edict['PEAKZERO'] = self.PEAKZERO
        zz_desc['PEAKZERO'] = ""
        super(RM_Enum_MODEM_CTRL5_BRCALMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CF_DEC0(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DF3 = 0x00000000
        zz_edict['DF3'] = self.DF3
        zz_desc['DF3'] = ""
        self.DF4WIDE = 0x00000001
        zz_edict['DF4WIDE'] = self.DF4WIDE
        zz_desc['DF4WIDE'] = ""
        self.DF4NARROW = 0x00000002
        zz_edict['DF4NARROW'] = self.DF4NARROW
        zz_desc['DF4NARROW'] = ""
        self.DF8WIDE = 0x00000003
        zz_edict['DF8WIDE'] = self.DF8WIDE
        zz_desc['DF8WIDE'] = ""
        self.DF8NARROW = 0x00000004
        zz_edict['DF8NARROW'] = self.DF8NARROW
        zz_desc['DF8NARROW'] = ""
        super(RM_Enum_MODEM_CF_DEC0, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CF_CFOSR(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CF7 = 0x00000000
        zz_edict['CF7'] = self.CF7
        zz_desc['CF7'] = ""
        self.CF8 = 0x00000001
        zz_edict['CF8'] = self.CF8
        zz_desc['CF8'] = ""
        self.CF12 = 0x00000002
        zz_edict['CF12'] = self.CF12
        zz_desc['CF12'] = ""
        self.CF16 = 0x00000003
        zz_edict['CF16'] = self.CF16
        zz_desc['CF16'] = ""
        self.CF32 = 0x00000004
        zz_edict['CF32'] = self.CF32
        zz_desc['CF32'] = ""
        self.CF0 = 0x00000005
        zz_edict['CF0'] = self.CF0
        zz_desc['CF0'] = ""
        super(RM_Enum_MODEM_CF_CFOSR, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_CF_DEC1GAIN(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.ADD0 = 0x00000000
        zz_edict['ADD0'] = self.ADD0
        zz_desc['ADD0'] = ""
        self.ADD6 = 0x00000001
        zz_edict['ADD6'] = self.ADD6
        zz_desc['ADD6'] = ""
        self.ADD12 = 0x00000002
        zz_edict['ADD12'] = self.ADD12
        zz_desc['ADD12'] = ""
        super(RM_Enum_MODEM_CF_DEC1GAIN, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_TIMING_FASTRESYNC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIS = 0x00000000
        zz_edict['DIS'] = self.DIS
        zz_desc['DIS'] = ""
        self.PREDET = 0x00000001
        zz_edict['PREDET'] = self.PREDET
        zz_desc['PREDET'] = ""
        self.FRAMEDET = 0x00000002
        zz_edict['FRAMEDET'] = self.FRAMEDET
        zz_desc['FRAMEDET'] = ""
        super(RM_Enum_MODEM_TIMING_FASTRESYNC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_AFC_AFCRXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIS = 0x00000000
        zz_edict['DIS'] = self.DIS
        zz_desc['DIS'] = ""
        self.FREE = 0x00000001
        zz_edict['FREE'] = self.FREE
        zz_desc['FREE'] = ""
        self.FREEPRESTART = 0x00000002
        zz_edict['FREEPRESTART'] = self.FREEPRESTART
        zz_desc['FREEPRESTART'] = ""
        self.TIMLOCK = 0x00000003
        zz_edict['TIMLOCK'] = self.TIMLOCK
        zz_desc['TIMLOCK'] = ""
        self.PRELOCK = 0x00000004
        zz_edict['PRELOCK'] = self.PRELOCK
        zz_desc['PRELOCK'] = ""
        self.FRAMELOCK = 0x00000005
        zz_edict['FRAMELOCK'] = self.FRAMELOCK
        zz_desc['FRAMELOCK'] = ""
        self.FRAMELOCKPRESTART = 0x00000006
        zz_edict['FRAMELOCKPRESTART'] = self.FRAMELOCKPRESTART
        zz_desc['FRAMELOCKPRESTART'] = ""
        super(RM_Enum_MODEM_AFC_AFCRXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_AFC_AFCTXMODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.DIS = 0x00000000
        zz_edict['DIS'] = self.DIS
        zz_desc['DIS'] = ""
        self.PRELOCK = 0x00000001
        zz_edict['PRELOCK'] = self.PRELOCK
        zz_desc['PRELOCK'] = ""
        self.FRAMELOCK = 0x00000002
        zz_edict['FRAMELOCK'] = self.FRAMELOCK
        zz_desc['FRAMELOCK'] = ""
        super(RM_Enum_MODEM_AFC_AFCTXMODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_ROUTELOC0_DINLOC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOC0 = 0x00000000
        zz_edict['LOC0'] = self.LOC0
        zz_desc['LOC0'] = ""
        self.LOC1 = 0x00000001
        zz_edict['LOC1'] = self.LOC1
        zz_desc['LOC1'] = ""
        self.LOC2 = 0x00000002
        zz_edict['LOC2'] = self.LOC2
        zz_desc['LOC2'] = ""
        self.LOC3 = 0x00000003
        zz_edict['LOC3'] = self.LOC3
        zz_desc['LOC3'] = ""
        self.LOC4 = 0x00000004
        zz_edict['LOC4'] = self.LOC4
        zz_desc['LOC4'] = ""
        self.LOC5 = 0x00000005
        zz_edict['LOC5'] = self.LOC5
        zz_desc['LOC5'] = ""
        self.LOC6 = 0x00000006
        zz_edict['LOC6'] = self.LOC6
        zz_desc['LOC6'] = ""
        self.LOC7 = 0x00000007
        zz_edict['LOC7'] = self.LOC7
        zz_desc['LOC7'] = ""
        self.LOC8 = 0x00000008
        zz_edict['LOC8'] = self.LOC8
        zz_desc['LOC8'] = ""
        self.LOC9 = 0x00000009
        zz_edict['LOC9'] = self.LOC9
        zz_desc['LOC9'] = ""
        self.LOC10 = 0x0000000A
        zz_edict['LOC10'] = self.LOC10
        zz_desc['LOC10'] = ""
        self.LOC11 = 0x0000000B
        zz_edict['LOC11'] = self.LOC11
        zz_desc['LOC11'] = ""
        self.LOC12 = 0x0000000C
        zz_edict['LOC12'] = self.LOC12
        zz_desc['LOC12'] = ""
        self.LOC13 = 0x0000000D
        zz_edict['LOC13'] = self.LOC13
        zz_desc['LOC13'] = ""
        self.LOC14 = 0x0000000E
        zz_edict['LOC14'] = self.LOC14
        zz_desc['LOC14'] = ""
        self.LOC15 = 0x0000000F
        zz_edict['LOC15'] = self.LOC15
        zz_desc['LOC15'] = ""
        self.LOC16 = 0x00000010
        zz_edict['LOC16'] = self.LOC16
        zz_desc['LOC16'] = ""
        self.LOC17 = 0x00000011
        zz_edict['LOC17'] = self.LOC17
        zz_desc['LOC17'] = ""
        self.LOC18 = 0x00000012
        zz_edict['LOC18'] = self.LOC18
        zz_desc['LOC18'] = ""
        self.LOC19 = 0x00000013
        zz_edict['LOC19'] = self.LOC19
        zz_desc['LOC19'] = ""
        self.LOC20 = 0x00000014
        zz_edict['LOC20'] = self.LOC20
        zz_desc['LOC20'] = ""
        self.LOC21 = 0x00000015
        zz_edict['LOC21'] = self.LOC21
        zz_desc['LOC21'] = ""
        self.LOC22 = 0x00000016
        zz_edict['LOC22'] = self.LOC22
        zz_desc['LOC22'] = ""
        self.LOC23 = 0x00000017
        zz_edict['LOC23'] = self.LOC23
        zz_desc['LOC23'] = ""
        self.LOC24 = 0x00000018
        zz_edict['LOC24'] = self.LOC24
        zz_desc['LOC24'] = ""
        self.LOC25 = 0x00000019
        zz_edict['LOC25'] = self.LOC25
        zz_desc['LOC25'] = ""
        self.LOC26 = 0x0000001A
        zz_edict['LOC26'] = self.LOC26
        zz_desc['LOC26'] = ""
        self.LOC27 = 0x0000001B
        zz_edict['LOC27'] = self.LOC27
        zz_desc['LOC27'] = ""
        self.LOC28 = 0x0000001C
        zz_edict['LOC28'] = self.LOC28
        zz_desc['LOC28'] = ""
        self.LOC29 = 0x0000001D
        zz_edict['LOC29'] = self.LOC29
        zz_desc['LOC29'] = ""
        self.LOC30 = 0x0000001E
        zz_edict['LOC30'] = self.LOC30
        zz_desc['LOC30'] = ""
        self.LOC31 = 0x0000001F
        zz_edict['LOC31'] = self.LOC31
        zz_desc['LOC31'] = ""
        super(RM_Enum_MODEM_ROUTELOC0_DINLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_ROUTELOC0_DOUTLOC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOC0 = 0x00000000
        zz_edict['LOC0'] = self.LOC0
        zz_desc['LOC0'] = ""
        self.LOC1 = 0x00000001
        zz_edict['LOC1'] = self.LOC1
        zz_desc['LOC1'] = ""
        self.LOC2 = 0x00000002
        zz_edict['LOC2'] = self.LOC2
        zz_desc['LOC2'] = ""
        self.LOC3 = 0x00000003
        zz_edict['LOC3'] = self.LOC3
        zz_desc['LOC3'] = ""
        self.LOC4 = 0x00000004
        zz_edict['LOC4'] = self.LOC4
        zz_desc['LOC4'] = ""
        self.LOC5 = 0x00000005
        zz_edict['LOC5'] = self.LOC5
        zz_desc['LOC5'] = ""
        self.LOC6 = 0x00000006
        zz_edict['LOC6'] = self.LOC6
        zz_desc['LOC6'] = ""
        self.LOC7 = 0x00000007
        zz_edict['LOC7'] = self.LOC7
        zz_desc['LOC7'] = ""
        self.LOC8 = 0x00000008
        zz_edict['LOC8'] = self.LOC8
        zz_desc['LOC8'] = ""
        self.LOC9 = 0x00000009
        zz_edict['LOC9'] = self.LOC9
        zz_desc['LOC9'] = ""
        self.LOC10 = 0x0000000A
        zz_edict['LOC10'] = self.LOC10
        zz_desc['LOC10'] = ""
        self.LOC11 = 0x0000000B
        zz_edict['LOC11'] = self.LOC11
        zz_desc['LOC11'] = ""
        self.LOC12 = 0x0000000C
        zz_edict['LOC12'] = self.LOC12
        zz_desc['LOC12'] = ""
        self.LOC13 = 0x0000000D
        zz_edict['LOC13'] = self.LOC13
        zz_desc['LOC13'] = ""
        self.LOC14 = 0x0000000E
        zz_edict['LOC14'] = self.LOC14
        zz_desc['LOC14'] = ""
        self.LOC15 = 0x0000000F
        zz_edict['LOC15'] = self.LOC15
        zz_desc['LOC15'] = ""
        self.LOC16 = 0x00000010
        zz_edict['LOC16'] = self.LOC16
        zz_desc['LOC16'] = ""
        self.LOC17 = 0x00000011
        zz_edict['LOC17'] = self.LOC17
        zz_desc['LOC17'] = ""
        self.LOC18 = 0x00000012
        zz_edict['LOC18'] = self.LOC18
        zz_desc['LOC18'] = ""
        self.LOC19 = 0x00000013
        zz_edict['LOC19'] = self.LOC19
        zz_desc['LOC19'] = ""
        self.LOC20 = 0x00000014
        zz_edict['LOC20'] = self.LOC20
        zz_desc['LOC20'] = ""
        self.LOC21 = 0x00000015
        zz_edict['LOC21'] = self.LOC21
        zz_desc['LOC21'] = ""
        self.LOC22 = 0x00000016
        zz_edict['LOC22'] = self.LOC22
        zz_desc['LOC22'] = ""
        self.LOC23 = 0x00000017
        zz_edict['LOC23'] = self.LOC23
        zz_desc['LOC23'] = ""
        self.LOC24 = 0x00000018
        zz_edict['LOC24'] = self.LOC24
        zz_desc['LOC24'] = ""
        self.LOC25 = 0x00000019
        zz_edict['LOC25'] = self.LOC25
        zz_desc['LOC25'] = ""
        self.LOC26 = 0x0000001A
        zz_edict['LOC26'] = self.LOC26
        zz_desc['LOC26'] = ""
        self.LOC27 = 0x0000001B
        zz_edict['LOC27'] = self.LOC27
        zz_desc['LOC27'] = ""
        self.LOC28 = 0x0000001C
        zz_edict['LOC28'] = self.LOC28
        zz_desc['LOC28'] = ""
        self.LOC29 = 0x0000001D
        zz_edict['LOC29'] = self.LOC29
        zz_desc['LOC29'] = ""
        self.LOC30 = 0x0000001E
        zz_edict['LOC30'] = self.LOC30
        zz_desc['LOC30'] = ""
        self.LOC31 = 0x0000001F
        zz_edict['LOC31'] = self.LOC31
        zz_desc['LOC31'] = ""
        super(RM_Enum_MODEM_ROUTELOC0_DOUTLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_ROUTELOC0_DCLKLOC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOC0 = 0x00000000
        zz_edict['LOC0'] = self.LOC0
        zz_desc['LOC0'] = ""
        self.LOC1 = 0x00000001
        zz_edict['LOC1'] = self.LOC1
        zz_desc['LOC1'] = ""
        self.LOC2 = 0x00000002
        zz_edict['LOC2'] = self.LOC2
        zz_desc['LOC2'] = ""
        self.LOC3 = 0x00000003
        zz_edict['LOC3'] = self.LOC3
        zz_desc['LOC3'] = ""
        self.LOC4 = 0x00000004
        zz_edict['LOC4'] = self.LOC4
        zz_desc['LOC4'] = ""
        self.LOC5 = 0x00000005
        zz_edict['LOC5'] = self.LOC5
        zz_desc['LOC5'] = ""
        self.LOC6 = 0x00000006
        zz_edict['LOC6'] = self.LOC6
        zz_desc['LOC6'] = ""
        self.LOC7 = 0x00000007
        zz_edict['LOC7'] = self.LOC7
        zz_desc['LOC7'] = ""
        self.LOC8 = 0x00000008
        zz_edict['LOC8'] = self.LOC8
        zz_desc['LOC8'] = ""
        self.LOC9 = 0x00000009
        zz_edict['LOC9'] = self.LOC9
        zz_desc['LOC9'] = ""
        self.LOC10 = 0x0000000A
        zz_edict['LOC10'] = self.LOC10
        zz_desc['LOC10'] = ""
        self.LOC11 = 0x0000000B
        zz_edict['LOC11'] = self.LOC11
        zz_desc['LOC11'] = ""
        self.LOC12 = 0x0000000C
        zz_edict['LOC12'] = self.LOC12
        zz_desc['LOC12'] = ""
        self.LOC13 = 0x0000000D
        zz_edict['LOC13'] = self.LOC13
        zz_desc['LOC13'] = ""
        self.LOC14 = 0x0000000E
        zz_edict['LOC14'] = self.LOC14
        zz_desc['LOC14'] = ""
        self.LOC15 = 0x0000000F
        zz_edict['LOC15'] = self.LOC15
        zz_desc['LOC15'] = ""
        self.LOC16 = 0x00000010
        zz_edict['LOC16'] = self.LOC16
        zz_desc['LOC16'] = ""
        self.LOC17 = 0x00000011
        zz_edict['LOC17'] = self.LOC17
        zz_desc['LOC17'] = ""
        self.LOC18 = 0x00000012
        zz_edict['LOC18'] = self.LOC18
        zz_desc['LOC18'] = ""
        self.LOC19 = 0x00000013
        zz_edict['LOC19'] = self.LOC19
        zz_desc['LOC19'] = ""
        self.LOC20 = 0x00000014
        zz_edict['LOC20'] = self.LOC20
        zz_desc['LOC20'] = ""
        self.LOC21 = 0x00000015
        zz_edict['LOC21'] = self.LOC21
        zz_desc['LOC21'] = ""
        self.LOC22 = 0x00000016
        zz_edict['LOC22'] = self.LOC22
        zz_desc['LOC22'] = ""
        self.LOC23 = 0x00000017
        zz_edict['LOC23'] = self.LOC23
        zz_desc['LOC23'] = ""
        self.LOC24 = 0x00000018
        zz_edict['LOC24'] = self.LOC24
        zz_desc['LOC24'] = ""
        self.LOC25 = 0x00000019
        zz_edict['LOC25'] = self.LOC25
        zz_desc['LOC25'] = ""
        self.LOC26 = 0x0000001A
        zz_edict['LOC26'] = self.LOC26
        zz_desc['LOC26'] = ""
        self.LOC27 = 0x0000001B
        zz_edict['LOC27'] = self.LOC27
        zz_desc['LOC27'] = ""
        self.LOC28 = 0x0000001C
        zz_edict['LOC28'] = self.LOC28
        zz_desc['LOC28'] = ""
        self.LOC29 = 0x0000001D
        zz_edict['LOC29'] = self.LOC29
        zz_desc['LOC29'] = ""
        self.LOC30 = 0x0000001E
        zz_edict['LOC30'] = self.LOC30
        zz_desc['LOC30'] = ""
        self.LOC31 = 0x0000001F
        zz_edict['LOC31'] = self.LOC31
        zz_desc['LOC31'] = ""
        super(RM_Enum_MODEM_ROUTELOC0_DCLKLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_ROUTELOC1_ANT0LOC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOC0 = 0x00000000
        zz_edict['LOC0'] = self.LOC0
        zz_desc['LOC0'] = ""
        self.LOC1 = 0x00000001
        zz_edict['LOC1'] = self.LOC1
        zz_desc['LOC1'] = ""
        self.LOC2 = 0x00000002
        zz_edict['LOC2'] = self.LOC2
        zz_desc['LOC2'] = ""
        self.LOC3 = 0x00000003
        zz_edict['LOC3'] = self.LOC3
        zz_desc['LOC3'] = ""
        self.LOC4 = 0x00000004
        zz_edict['LOC4'] = self.LOC4
        zz_desc['LOC4'] = ""
        self.LOC5 = 0x00000005
        zz_edict['LOC5'] = self.LOC5
        zz_desc['LOC5'] = ""
        self.LOC6 = 0x00000006
        zz_edict['LOC6'] = self.LOC6
        zz_desc['LOC6'] = ""
        self.LOC7 = 0x00000007
        zz_edict['LOC7'] = self.LOC7
        zz_desc['LOC7'] = ""
        self.LOC8 = 0x00000008
        zz_edict['LOC8'] = self.LOC8
        zz_desc['LOC8'] = ""
        self.LOC9 = 0x00000009
        zz_edict['LOC9'] = self.LOC9
        zz_desc['LOC9'] = ""
        self.LOC10 = 0x0000000A
        zz_edict['LOC10'] = self.LOC10
        zz_desc['LOC10'] = ""
        self.LOC11 = 0x0000000B
        zz_edict['LOC11'] = self.LOC11
        zz_desc['LOC11'] = ""
        self.LOC12 = 0x0000000C
        zz_edict['LOC12'] = self.LOC12
        zz_desc['LOC12'] = ""
        self.LOC13 = 0x0000000D
        zz_edict['LOC13'] = self.LOC13
        zz_desc['LOC13'] = ""
        self.LOC14 = 0x0000000E
        zz_edict['LOC14'] = self.LOC14
        zz_desc['LOC14'] = ""
        self.LOC15 = 0x0000000F
        zz_edict['LOC15'] = self.LOC15
        zz_desc['LOC15'] = ""
        self.LOC16 = 0x00000010
        zz_edict['LOC16'] = self.LOC16
        zz_desc['LOC16'] = ""
        self.LOC17 = 0x00000011
        zz_edict['LOC17'] = self.LOC17
        zz_desc['LOC17'] = ""
        self.LOC18 = 0x00000012
        zz_edict['LOC18'] = self.LOC18
        zz_desc['LOC18'] = ""
        self.LOC19 = 0x00000013
        zz_edict['LOC19'] = self.LOC19
        zz_desc['LOC19'] = ""
        self.LOC20 = 0x00000014
        zz_edict['LOC20'] = self.LOC20
        zz_desc['LOC20'] = ""
        self.LOC21 = 0x00000015
        zz_edict['LOC21'] = self.LOC21
        zz_desc['LOC21'] = ""
        self.LOC22 = 0x00000016
        zz_edict['LOC22'] = self.LOC22
        zz_desc['LOC22'] = ""
        self.LOC23 = 0x00000017
        zz_edict['LOC23'] = self.LOC23
        zz_desc['LOC23'] = ""
        self.LOC24 = 0x00000018
        zz_edict['LOC24'] = self.LOC24
        zz_desc['LOC24'] = ""
        self.LOC25 = 0x00000019
        zz_edict['LOC25'] = self.LOC25
        zz_desc['LOC25'] = ""
        self.LOC26 = 0x0000001A
        zz_edict['LOC26'] = self.LOC26
        zz_desc['LOC26'] = ""
        self.LOC27 = 0x0000001B
        zz_edict['LOC27'] = self.LOC27
        zz_desc['LOC27'] = ""
        self.LOC28 = 0x0000001C
        zz_edict['LOC28'] = self.LOC28
        zz_desc['LOC28'] = ""
        self.LOC29 = 0x0000001D
        zz_edict['LOC29'] = self.LOC29
        zz_desc['LOC29'] = ""
        self.LOC30 = 0x0000001E
        zz_edict['LOC30'] = self.LOC30
        zz_desc['LOC30'] = ""
        self.LOC31 = 0x0000001F
        zz_edict['LOC31'] = self.LOC31
        zz_desc['LOC31'] = ""
        super(RM_Enum_MODEM_ROUTELOC1_ANT0LOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_ROUTELOC1_ANT1LOC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOC0 = 0x00000000
        zz_edict['LOC0'] = self.LOC0
        zz_desc['LOC0'] = ""
        self.LOC1 = 0x00000001
        zz_edict['LOC1'] = self.LOC1
        zz_desc['LOC1'] = ""
        self.LOC2 = 0x00000002
        zz_edict['LOC2'] = self.LOC2
        zz_desc['LOC2'] = ""
        self.LOC3 = 0x00000003
        zz_edict['LOC3'] = self.LOC3
        zz_desc['LOC3'] = ""
        self.LOC4 = 0x00000004
        zz_edict['LOC4'] = self.LOC4
        zz_desc['LOC4'] = ""
        self.LOC5 = 0x00000005
        zz_edict['LOC5'] = self.LOC5
        zz_desc['LOC5'] = ""
        self.LOC6 = 0x00000006
        zz_edict['LOC6'] = self.LOC6
        zz_desc['LOC6'] = ""
        self.LOC7 = 0x00000007
        zz_edict['LOC7'] = self.LOC7
        zz_desc['LOC7'] = ""
        self.LOC8 = 0x00000008
        zz_edict['LOC8'] = self.LOC8
        zz_desc['LOC8'] = ""
        self.LOC9 = 0x00000009
        zz_edict['LOC9'] = self.LOC9
        zz_desc['LOC9'] = ""
        self.LOC10 = 0x0000000A
        zz_edict['LOC10'] = self.LOC10
        zz_desc['LOC10'] = ""
        self.LOC11 = 0x0000000B
        zz_edict['LOC11'] = self.LOC11
        zz_desc['LOC11'] = ""
        self.LOC12 = 0x0000000C
        zz_edict['LOC12'] = self.LOC12
        zz_desc['LOC12'] = ""
        self.LOC13 = 0x0000000D
        zz_edict['LOC13'] = self.LOC13
        zz_desc['LOC13'] = ""
        self.LOC14 = 0x0000000E
        zz_edict['LOC14'] = self.LOC14
        zz_desc['LOC14'] = ""
        self.LOC15 = 0x0000000F
        zz_edict['LOC15'] = self.LOC15
        zz_desc['LOC15'] = ""
        self.LOC16 = 0x00000010
        zz_edict['LOC16'] = self.LOC16
        zz_desc['LOC16'] = ""
        self.LOC17 = 0x00000011
        zz_edict['LOC17'] = self.LOC17
        zz_desc['LOC17'] = ""
        self.LOC18 = 0x00000012
        zz_edict['LOC18'] = self.LOC18
        zz_desc['LOC18'] = ""
        self.LOC19 = 0x00000013
        zz_edict['LOC19'] = self.LOC19
        zz_desc['LOC19'] = ""
        self.LOC20 = 0x00000014
        zz_edict['LOC20'] = self.LOC20
        zz_desc['LOC20'] = ""
        self.LOC21 = 0x00000015
        zz_edict['LOC21'] = self.LOC21
        zz_desc['LOC21'] = ""
        self.LOC22 = 0x00000016
        zz_edict['LOC22'] = self.LOC22
        zz_desc['LOC22'] = ""
        self.LOC23 = 0x00000017
        zz_edict['LOC23'] = self.LOC23
        zz_desc['LOC23'] = ""
        self.LOC24 = 0x00000018
        zz_edict['LOC24'] = self.LOC24
        zz_desc['LOC24'] = ""
        self.LOC25 = 0x00000019
        zz_edict['LOC25'] = self.LOC25
        zz_desc['LOC25'] = ""
        self.LOC26 = 0x0000001A
        zz_edict['LOC26'] = self.LOC26
        zz_desc['LOC26'] = ""
        self.LOC27 = 0x0000001B
        zz_edict['LOC27'] = self.LOC27
        zz_desc['LOC27'] = ""
        self.LOC28 = 0x0000001C
        zz_edict['LOC28'] = self.LOC28
        zz_desc['LOC28'] = ""
        self.LOC29 = 0x0000001D
        zz_edict['LOC29'] = self.LOC29
        zz_desc['LOC29'] = ""
        self.LOC30 = 0x0000001E
        zz_edict['LOC30'] = self.LOC30
        zz_desc['LOC30'] = ""
        self.LOC31 = 0x0000001F
        zz_edict['LOC31'] = self.LOC31
        zz_desc['LOC31'] = ""
        super(RM_Enum_MODEM_ROUTELOC1_ANT1LOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_MODEM_DCCOMP_DCLIMIT(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.FULLSCALE = 0x00000000
        zz_edict['FULLSCALE'] = self.FULLSCALE
        zz_desc['FULLSCALE'] = ""
        self.FULLSCALEBY4 = 0x00000001
        zz_edict['FULLSCALEBY4'] = self.FULLSCALEBY4
        zz_desc['FULLSCALEBY4'] = ""
        self.FULLSCALEBY8 = 0x00000002
        zz_edict['FULLSCALEBY8'] = self.FULLSCALEBY8
        zz_desc['FULLSCALEBY8'] = ""
        self.FULLSCALEBY16 = 0x00000003
        zz_edict['FULLSCALEBY16'] = self.FULLSCALEBY16
        zz_desc['FULLSCALEBY16'] = ""
        super(RM_Enum_MODEM_DCCOMP_DCLIMIT, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


