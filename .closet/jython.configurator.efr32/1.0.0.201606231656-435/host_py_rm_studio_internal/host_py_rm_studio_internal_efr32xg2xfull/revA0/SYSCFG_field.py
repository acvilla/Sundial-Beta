
from static import Base_RM_Field
from SYSCFG_enum import *


class RM_Field_SYSCFG_CTRLPMON_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_CTRLPMON_EN, self).__init__(register,
            'EN', 'SYSCFG.CTRLPMON.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_CTRLPMON_SELBRANCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_CTRLPMON_SELBRANCH, self).__init__(register,
            'SELBRANCH', 'SYSCFG.CTRLPMON.SELBRANCH', 'read-write',
            "",
            1, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_CTRLPMON_SWGEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_CTRLPMON_SWGEN, self).__init__(register,
            'SWGEN', 'SYSCFG.CTRLPMON.SWGEN', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_CTRLPMON_SWSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_CTRLPMON_SWSEN, self).__init__(register,
            'SWSEN', 'SYSCFG.CTRLPMON.SWSEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_CTRLPMON_SWBEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_CTRLPMON_SWBEN, self).__init__(register,
            'SWBEN', 'SYSCFG.CTRLPMON.SWBEN', 'read-write',
            "",
            9, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_CTRLPMON_IDACCURRENT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_CTRLPMON_IDACCURRENT, self).__init__(register,
            'IDACCURRENT', 'SYSCFG.CTRLPMON.IDACCURRENT', 'read-write',
            "",
            11, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_CTRLPMON_SWTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_CTRLPMON_SWTEN, self).__init__(register,
            'SWTEN', 'SYSCFG.CTRLPMON.SWTEN', 'read-write',
            "",
            14, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCP_FLOATVREG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCP_FLOATVREG, self).__init__(register,
            'FLOATVREG', 'SYSCFG.AMUXCP.FLOATVREG', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCP_ENPUMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCP_ENPUMP, self).__init__(register,
            'ENPUMP', 'SYSCFG.AMUXCP.ENPUMP', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCP_BOOST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCP_BOOST, self).__init__(register,
            'BOOST', 'SYSCFG.AMUXCP.BOOST', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCP_BOOSTSMPL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCP_BOOSTSMPL, self).__init__(register,
            'BOOSTSMPL', 'SYSCFG.AMUXCP.BOOSTSMPL', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCP_FORCE2X(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCP_FORCE2X, self).__init__(register,
            'FORCE2X', 'SYSCFG.AMUXCP.FORCE2X', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCP_FORCE3X(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCP_FORCE3X, self).__init__(register,
            'FORCE3X', 'SYSCFG.AMUXCP.FORCE3X', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCP_BYPASSDIV2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCP_BYPASSDIV2, self).__init__(register,
            'BYPASSDIV2', 'SYSCFG.AMUXCP.BYPASSDIV2', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCP_SYNCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCP_SYNCMODE, self).__init__(register,
            'SYNCMODE', 'SYSCFG.AMUXCP.SYNCMODE', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCP_SYNCCLK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCP_SYNCCLK, self).__init__(register,
            'SYNCCLK', 'SYSCFG.AMUXCP.SYNCCLK', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCP_DUTYFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCP_DUTYFSEL, self).__init__(register,
            'DUTYFSEL', 'SYSCFG.AMUXCP.DUTYFSEL', 'read-write',
            "",
            10, 2,
            RM_Enum_SYSCFG_AMUXCP_DUTYFSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCPCTRL_FORCEEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCPCTRL_FORCEEN, self).__init__(register,
            'FORCEEN', 'SYSCFG.AMUXCPCTRL.FORCEEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCPCTRL_FORCEIBIAS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCPCTRL_FORCEIBIAS, self).__init__(register,
            'FORCEIBIAS', 'SYSCFG.AMUXCPCTRL.FORCEIBIAS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCPCTRL_FORCEPUMPCAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCPCTRL_FORCEPUMPCAP, self).__init__(register,
            'FORCEPUMPCAP', 'SYSCFG.AMUXCPCTRL.FORCEPUMPCAP', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCPCTRL_FORCEOFF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCPCTRL_FORCEOFF, self).__init__(register,
            'FORCEOFF', 'SYSCFG.AMUXCPCTRL.FORCEOFF', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCPCAL_CALVDDX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCPCAL_CALVDDX, self).__init__(register,
            'CALVDDX', 'SYSCFG.AMUXCPCAL.CALVDDX', 'read-write',
            "",
            0, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCPCAL_CALVREF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCPCAL_CALVREF, self).__init__(register,
            'CALVREF', 'SYSCFG.AMUXCPCAL.CALVREF', 'read-write',
            "",
            8, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCPCAL_PUMPCAPLP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCPCAL_PUMPCAPLP, self).__init__(register,
            'PUMPCAPLP', 'SYSCFG.AMUXCPCAL.PUMPCAPLP', 'read-write',
            "",
            16, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCPCAL_IBIASLP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCPCAL_IBIASLP, self).__init__(register,
            'IBIASLP', 'SYSCFG.AMUXCPCAL.IBIASLP', 'read-write',
            "",
            19, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCPCAL_PUMPCAPHP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCPCAL_PUMPCAPHP, self).__init__(register,
            'PUMPCAPHP', 'SYSCFG.AMUXCPCAL.PUMPCAPHP', 'read-write',
            "",
            24, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_AMUXCPCAL_IBIASHP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_AMUXCPCAL_IBIASHP, self).__init__(register,
            'IBIASHP', 'SYSCFG.AMUXCPCAL.IBIASHP', 'read-write',
            "",
            27, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_IF_SW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_IF_SW, self).__init__(register,
            'SW', 'SYSCFG.IF.SW', 'read-write',
            "",
            0, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_IFS_SW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_IFS_SW, self).__init__(register,
            'SW', 'SYSCFG.IFS.SW', 'write-only',
            "",
            0, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_IFC_SW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_IFC_SW, self).__init__(register,
            'SW', 'SYSCFG.IFC.SW', 'write-only',
            "",
            0, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_SYSCFG_IEN_SW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SYSCFG_IEN_SW, self).__init__(register,
            'SW', 'SYSCFG.IEN.SW', 'read-write',
            "",
            0, 2)
        self.__dict__['zz_frozen'] = True


