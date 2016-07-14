
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_AGC_STATUS1_CFLOOPSTATE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.IDLE = 0x00000000
        zz_edict['IDLE'] = self.IDLE
        zz_desc['IDLE'] = ""
        self.PWRMEAS = 0x00000001
        zz_edict['PWRMEAS'] = self.PWRMEAS
        zz_desc['PWRMEAS'] = ""
        self.CFDELAY = 0x00000002
        zz_edict['CFDELAY'] = self.CFDELAY
        zz_desc['CFDELAY'] = ""
        self.NOP = 0x00000003
        zz_edict['NOP'] = self.NOP
        zz_desc['NOP'] = ""
        super(RM_Enum_AGC_STATUS1_CFLOOPSTATE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_AGC_STATUS1_FASTLOOPSTATE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.IDLE = 0x00000000
        zz_edict['IDLE'] = self.IDLE
        zz_desc['IDLE'] = ""
        self.PEAKCHK = 0x00000001
        zz_edict['PEAKCHK'] = self.PEAKCHK
        zz_desc['PEAKCHK'] = ""
        self.FEDELAY = 0x00000002
        zz_edict['FEDELAY'] = self.FEDELAY
        zz_desc['FEDELAY'] = ""
        self.PEAKRST = 0x00000003
        zz_edict['PEAKRST'] = self.PEAKRST
        zz_desc['PEAKRST'] = ""
        self.PEAKWAIT = 0x00000004
        zz_edict['PEAKWAIT'] = self.PEAKWAIT
        zz_desc['PEAKWAIT'] = ""
        super(RM_Enum_AGC_STATUS1_FASTLOOPSTATE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_AGC_CTRL0_MODE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.CONT = 0x00000000
        zz_edict['CONT'] = self.CONT
        zz_desc['CONT'] = ""
        self.LOCKPREDET = 0x00000001
        zz_edict['LOCKPREDET'] = self.LOCKPREDET
        zz_desc['LOCKPREDET'] = ""
        self.LOCKFRAMEDET = 0x00000002
        zz_edict['LOCKFRAMEDET'] = self.LOCKFRAMEDET
        zz_desc['LOCKFRAMEDET'] = ""
        super(RM_Enum_AGC_CTRL0_MODE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_AGC_CTRL2_ADCRSTFASTLOOP(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.GAINREDUCTION = 0x00000000
        zz_edict['GAINREDUCTION'] = self.GAINREDUCTION
        zz_desc['GAINREDUCTION'] = ""
        self.ALWAYS = 0x00000001
        zz_edict['ALWAYS'] = self.ALWAYS
        zz_desc['ALWAYS'] = ""
        self.NEVER = 0x00000002
        zz_edict['NEVER'] = self.NEVER
        zz_desc['NEVER'] = ""
        super(RM_Enum_AGC_CTRL2_ADCRSTFASTLOOP, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


