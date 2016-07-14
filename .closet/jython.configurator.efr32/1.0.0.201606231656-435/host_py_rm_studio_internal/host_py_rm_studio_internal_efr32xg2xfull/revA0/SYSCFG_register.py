
from static import Base_RM_Register
from SYSCFG_field import *


class RM_Register_SYSCFG_CTRLPMON(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SYSCFG_CTRLPMON, self).__init__(rmio, label,
            0x400e7000, 0x000,
            'CTRLPMON', 'SYSCFG.CTRLPMON', 'read-write',
            "",
            0x00000080, 0x0000FFBF)

        self.EN = RM_Field_SYSCFG_CTRLPMON_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.SELBRANCH = RM_Field_SYSCFG_CTRLPMON_SELBRANCH(self)
        self.zz_fdict['SELBRANCH'] = self.SELBRANCH
        self.SWGEN = RM_Field_SYSCFG_CTRLPMON_SWGEN(self)
        self.zz_fdict['SWGEN'] = self.SWGEN
        self.SWSEN = RM_Field_SYSCFG_CTRLPMON_SWSEN(self)
        self.zz_fdict['SWSEN'] = self.SWSEN
        self.SWBEN = RM_Field_SYSCFG_CTRLPMON_SWBEN(self)
        self.zz_fdict['SWBEN'] = self.SWBEN
        self.IDACCURRENT = RM_Field_SYSCFG_CTRLPMON_IDACCURRENT(self)
        self.zz_fdict['IDACCURRENT'] = self.IDACCURRENT
        self.SWTEN = RM_Field_SYSCFG_CTRLPMON_SWTEN(self)
        self.zz_fdict['SWTEN'] = self.SWTEN
        self.__dict__['zz_frozen'] = True


class RM_Register_SYSCFG_AMUXCP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SYSCFG_AMUXCP, self).__init__(rmio, label,
            0x400e7000, 0x010,
            'AMUXCP', 'SYSCFG.AMUXCP', 'read-write',
            "",
            0x00000000, 0x00000FFE)

        self.FLOATVREG = RM_Field_SYSCFG_AMUXCP_FLOATVREG(self)
        self.zz_fdict['FLOATVREG'] = self.FLOATVREG
        self.ENPUMP = RM_Field_SYSCFG_AMUXCP_ENPUMP(self)
        self.zz_fdict['ENPUMP'] = self.ENPUMP
        self.BOOST = RM_Field_SYSCFG_AMUXCP_BOOST(self)
        self.zz_fdict['BOOST'] = self.BOOST
        self.BOOSTSMPL = RM_Field_SYSCFG_AMUXCP_BOOSTSMPL(self)
        self.zz_fdict['BOOSTSMPL'] = self.BOOSTSMPL
        self.FORCE2X = RM_Field_SYSCFG_AMUXCP_FORCE2X(self)
        self.zz_fdict['FORCE2X'] = self.FORCE2X
        self.FORCE3X = RM_Field_SYSCFG_AMUXCP_FORCE3X(self)
        self.zz_fdict['FORCE3X'] = self.FORCE3X
        self.BYPASSDIV2 = RM_Field_SYSCFG_AMUXCP_BYPASSDIV2(self)
        self.zz_fdict['BYPASSDIV2'] = self.BYPASSDIV2
        self.SYNCMODE = RM_Field_SYSCFG_AMUXCP_SYNCMODE(self)
        self.zz_fdict['SYNCMODE'] = self.SYNCMODE
        self.SYNCCLK = RM_Field_SYSCFG_AMUXCP_SYNCCLK(self)
        self.zz_fdict['SYNCCLK'] = self.SYNCCLK
        self.DUTYFSEL = RM_Field_SYSCFG_AMUXCP_DUTYFSEL(self)
        self.zz_fdict['DUTYFSEL'] = self.DUTYFSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_SYSCFG_AMUXCPCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SYSCFG_AMUXCPCTRL, self).__init__(rmio, label,
            0x400e7000, 0x014,
            'AMUXCPCTRL', 'SYSCFG.AMUXCPCTRL', 'read-write',
            "",
            0x00000000, 0x0000000F)

        self.FORCEEN = RM_Field_SYSCFG_AMUXCPCTRL_FORCEEN(self)
        self.zz_fdict['FORCEEN'] = self.FORCEEN
        self.FORCEIBIAS = RM_Field_SYSCFG_AMUXCPCTRL_FORCEIBIAS(self)
        self.zz_fdict['FORCEIBIAS'] = self.FORCEIBIAS
        self.FORCEPUMPCAP = RM_Field_SYSCFG_AMUXCPCTRL_FORCEPUMPCAP(self)
        self.zz_fdict['FORCEPUMPCAP'] = self.FORCEPUMPCAP
        self.FORCEOFF = RM_Field_SYSCFG_AMUXCPCTRL_FORCEOFF(self)
        self.zz_fdict['FORCEOFF'] = self.FORCEOFF
        self.__dict__['zz_frozen'] = True


class RM_Register_SYSCFG_AMUXCPCAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SYSCFG_AMUXCPCAL, self).__init__(rmio, label,
            0x400e7000, 0x018,
            'AMUXCPCAL', 'SYSCFG.AMUXCPCAL', 'read-write',
            "",
            0x6B090004, 0x7B7B3F07)

        self.CALVDDX = RM_Field_SYSCFG_AMUXCPCAL_CALVDDX(self)
        self.zz_fdict['CALVDDX'] = self.CALVDDX
        self.CALVREF = RM_Field_SYSCFG_AMUXCPCAL_CALVREF(self)
        self.zz_fdict['CALVREF'] = self.CALVREF
        self.PUMPCAPLP = RM_Field_SYSCFG_AMUXCPCAL_PUMPCAPLP(self)
        self.zz_fdict['PUMPCAPLP'] = self.PUMPCAPLP
        self.IBIASLP = RM_Field_SYSCFG_AMUXCPCAL_IBIASLP(self)
        self.zz_fdict['IBIASLP'] = self.IBIASLP
        self.PUMPCAPHP = RM_Field_SYSCFG_AMUXCPCAL_PUMPCAPHP(self)
        self.zz_fdict['PUMPCAPHP'] = self.PUMPCAPHP
        self.IBIASHP = RM_Field_SYSCFG_AMUXCPCAL_IBIASHP(self)
        self.zz_fdict['IBIASHP'] = self.IBIASHP
        self.__dict__['zz_frozen'] = True


class RM_Register_SYSCFG_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SYSCFG_IF, self).__init__(rmio, label,
            0x400e7000, 0x040,
            'IF', 'SYSCFG.IF', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.SW = RM_Field_SYSCFG_IF_SW(self)
        self.zz_fdict['SW'] = self.SW
        self.__dict__['zz_frozen'] = True


class RM_Register_SYSCFG_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SYSCFG_IFS, self).__init__(rmio, label,
            0x400e7000, 0x044,
            'IFS', 'SYSCFG.IFS', 'write-only',
            "",
            0x00000000, 0x00000003)

        self.SW = RM_Field_SYSCFG_IFS_SW(self)
        self.zz_fdict['SW'] = self.SW
        self.__dict__['zz_frozen'] = True


class RM_Register_SYSCFG_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SYSCFG_IFC, self).__init__(rmio, label,
            0x400e7000, 0x048,
            'IFC', 'SYSCFG.IFC', 'write-only',
            "",
            0x00000000, 0x00000003)

        self.SW = RM_Field_SYSCFG_IFC_SW(self)
        self.zz_fdict['SW'] = self.SW
        self.__dict__['zz_frozen'] = True


class RM_Register_SYSCFG_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SYSCFG_IEN, self).__init__(rmio, label,
            0x400e7000, 0x04C,
            'IEN', 'SYSCFG.IEN', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.SW = RM_Field_SYSCFG_IEN_SW(self)
        self.zz_fdict['SW'] = self.SW
        self.__dict__['zz_frozen'] = True


