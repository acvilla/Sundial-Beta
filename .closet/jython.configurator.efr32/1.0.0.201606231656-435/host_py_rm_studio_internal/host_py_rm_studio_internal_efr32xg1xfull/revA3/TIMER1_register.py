
from static import Base_RM_Register
from TIMER1_field import *


class RM_Register_TIMER1_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CTRL, self).__init__(rmio, label,
            0x40018400, 0x000,
            'CTRL', 'TIMER1.CTRL', 'read-write',
            "",
            0x00000000, 0x3F032FFB)

        self.MODE = RM_Field_TIMER1_CTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.SYNC = RM_Field_TIMER1_CTRL_SYNC(self)
        self.zz_fdict['SYNC'] = self.SYNC
        self.OSMEN = RM_Field_TIMER1_CTRL_OSMEN(self)
        self.zz_fdict['OSMEN'] = self.OSMEN
        self.QDM = RM_Field_TIMER1_CTRL_QDM(self)
        self.zz_fdict['QDM'] = self.QDM
        self.DEBUGRUN = RM_Field_TIMER1_CTRL_DEBUGRUN(self)
        self.zz_fdict['DEBUGRUN'] = self.DEBUGRUN
        self.DMACLRACT = RM_Field_TIMER1_CTRL_DMACLRACT(self)
        self.zz_fdict['DMACLRACT'] = self.DMACLRACT
        self.RISEA = RM_Field_TIMER1_CTRL_RISEA(self)
        self.zz_fdict['RISEA'] = self.RISEA
        self.FALLA = RM_Field_TIMER1_CTRL_FALLA(self)
        self.zz_fdict['FALLA'] = self.FALLA
        self.X2CNT = RM_Field_TIMER1_CTRL_X2CNT(self)
        self.zz_fdict['X2CNT'] = self.X2CNT
        self.CLKSEL = RM_Field_TIMER1_CTRL_CLKSEL(self)
        self.zz_fdict['CLKSEL'] = self.CLKSEL
        self.PRESC = RM_Field_TIMER1_CTRL_PRESC(self)
        self.zz_fdict['PRESC'] = self.PRESC
        self.ATI = RM_Field_TIMER1_CTRL_ATI(self)
        self.zz_fdict['ATI'] = self.ATI
        self.RSSCOIST = RM_Field_TIMER1_CTRL_RSSCOIST(self)
        self.zz_fdict['RSSCOIST'] = self.RSSCOIST
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CMD, self).__init__(rmio, label,
            0x40018400, 0x004,
            'CMD', 'TIMER1.CMD', 'write-only',
            "",
            0x00000000, 0x00000003)

        self.START = RM_Field_TIMER1_CMD_START(self)
        self.zz_fdict['START'] = self.START
        self.STOP = RM_Field_TIMER1_CMD_STOP(self)
        self.zz_fdict['STOP'] = self.STOP
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_STATUS, self).__init__(rmio, label,
            0x40018400, 0x008,
            'STATUS', 'TIMER1.STATUS', 'read-only',
            "",
            0x00000000, 0x0F0F0F07)

        self.RUNNING = RM_Field_TIMER1_STATUS_RUNNING(self)
        self.zz_fdict['RUNNING'] = self.RUNNING
        self.DIR = RM_Field_TIMER1_STATUS_DIR(self)
        self.zz_fdict['DIR'] = self.DIR
        self.TOPBV = RM_Field_TIMER1_STATUS_TOPBV(self)
        self.zz_fdict['TOPBV'] = self.TOPBV
        self.CCVBV0 = RM_Field_TIMER1_STATUS_CCVBV0(self)
        self.zz_fdict['CCVBV0'] = self.CCVBV0
        self.CCVBV1 = RM_Field_TIMER1_STATUS_CCVBV1(self)
        self.zz_fdict['CCVBV1'] = self.CCVBV1
        self.CCVBV2 = RM_Field_TIMER1_STATUS_CCVBV2(self)
        self.zz_fdict['CCVBV2'] = self.CCVBV2
        self.CCVBV3 = RM_Field_TIMER1_STATUS_CCVBV3(self)
        self.zz_fdict['CCVBV3'] = self.CCVBV3
        self.ICV0 = RM_Field_TIMER1_STATUS_ICV0(self)
        self.zz_fdict['ICV0'] = self.ICV0
        self.ICV1 = RM_Field_TIMER1_STATUS_ICV1(self)
        self.zz_fdict['ICV1'] = self.ICV1
        self.ICV2 = RM_Field_TIMER1_STATUS_ICV2(self)
        self.zz_fdict['ICV2'] = self.ICV2
        self.ICV3 = RM_Field_TIMER1_STATUS_ICV3(self)
        self.zz_fdict['ICV3'] = self.ICV3
        self.CCPOL0 = RM_Field_TIMER1_STATUS_CCPOL0(self)
        self.zz_fdict['CCPOL0'] = self.CCPOL0
        self.CCPOL1 = RM_Field_TIMER1_STATUS_CCPOL1(self)
        self.zz_fdict['CCPOL1'] = self.CCPOL1
        self.CCPOL2 = RM_Field_TIMER1_STATUS_CCPOL2(self)
        self.zz_fdict['CCPOL2'] = self.CCPOL2
        self.CCPOL3 = RM_Field_TIMER1_STATUS_CCPOL3(self)
        self.zz_fdict['CCPOL3'] = self.CCPOL3
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_IF, self).__init__(rmio, label,
            0x40018400, 0x00C,
            'IF', 'TIMER1.IF', 'read-only',
            "",
            0x00000000, 0x00000FF7)

        self.OF = RM_Field_TIMER1_IF_OF(self)
        self.zz_fdict['OF'] = self.OF
        self.UF = RM_Field_TIMER1_IF_UF(self)
        self.zz_fdict['UF'] = self.UF
        self.DIRCHG = RM_Field_TIMER1_IF_DIRCHG(self)
        self.zz_fdict['DIRCHG'] = self.DIRCHG
        self.CC0 = RM_Field_TIMER1_IF_CC0(self)
        self.zz_fdict['CC0'] = self.CC0
        self.CC1 = RM_Field_TIMER1_IF_CC1(self)
        self.zz_fdict['CC1'] = self.CC1
        self.CC2 = RM_Field_TIMER1_IF_CC2(self)
        self.zz_fdict['CC2'] = self.CC2
        self.CC3 = RM_Field_TIMER1_IF_CC3(self)
        self.zz_fdict['CC3'] = self.CC3
        self.ICBOF0 = RM_Field_TIMER1_IF_ICBOF0(self)
        self.zz_fdict['ICBOF0'] = self.ICBOF0
        self.ICBOF1 = RM_Field_TIMER1_IF_ICBOF1(self)
        self.zz_fdict['ICBOF1'] = self.ICBOF1
        self.ICBOF2 = RM_Field_TIMER1_IF_ICBOF2(self)
        self.zz_fdict['ICBOF2'] = self.ICBOF2
        self.ICBOF3 = RM_Field_TIMER1_IF_ICBOF3(self)
        self.zz_fdict['ICBOF3'] = self.ICBOF3
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_IFS, self).__init__(rmio, label,
            0x40018400, 0x010,
            'IFS', 'TIMER1.IFS', 'write-only',
            "",
            0x00000000, 0x00000FF7)

        self.OF = RM_Field_TIMER1_IFS_OF(self)
        self.zz_fdict['OF'] = self.OF
        self.UF = RM_Field_TIMER1_IFS_UF(self)
        self.zz_fdict['UF'] = self.UF
        self.DIRCHG = RM_Field_TIMER1_IFS_DIRCHG(self)
        self.zz_fdict['DIRCHG'] = self.DIRCHG
        self.CC0 = RM_Field_TIMER1_IFS_CC0(self)
        self.zz_fdict['CC0'] = self.CC0
        self.CC1 = RM_Field_TIMER1_IFS_CC1(self)
        self.zz_fdict['CC1'] = self.CC1
        self.CC2 = RM_Field_TIMER1_IFS_CC2(self)
        self.zz_fdict['CC2'] = self.CC2
        self.CC3 = RM_Field_TIMER1_IFS_CC3(self)
        self.zz_fdict['CC3'] = self.CC3
        self.ICBOF0 = RM_Field_TIMER1_IFS_ICBOF0(self)
        self.zz_fdict['ICBOF0'] = self.ICBOF0
        self.ICBOF1 = RM_Field_TIMER1_IFS_ICBOF1(self)
        self.zz_fdict['ICBOF1'] = self.ICBOF1
        self.ICBOF2 = RM_Field_TIMER1_IFS_ICBOF2(self)
        self.zz_fdict['ICBOF2'] = self.ICBOF2
        self.ICBOF3 = RM_Field_TIMER1_IFS_ICBOF3(self)
        self.zz_fdict['ICBOF3'] = self.ICBOF3
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_IFC, self).__init__(rmio, label,
            0x40018400, 0x014,
            'IFC', 'TIMER1.IFC', 'write-only',
            "",
            0x00000000, 0x00000FF7)

        self.OF = RM_Field_TIMER1_IFC_OF(self)
        self.zz_fdict['OF'] = self.OF
        self.UF = RM_Field_TIMER1_IFC_UF(self)
        self.zz_fdict['UF'] = self.UF
        self.DIRCHG = RM_Field_TIMER1_IFC_DIRCHG(self)
        self.zz_fdict['DIRCHG'] = self.DIRCHG
        self.CC0 = RM_Field_TIMER1_IFC_CC0(self)
        self.zz_fdict['CC0'] = self.CC0
        self.CC1 = RM_Field_TIMER1_IFC_CC1(self)
        self.zz_fdict['CC1'] = self.CC1
        self.CC2 = RM_Field_TIMER1_IFC_CC2(self)
        self.zz_fdict['CC2'] = self.CC2
        self.CC3 = RM_Field_TIMER1_IFC_CC3(self)
        self.zz_fdict['CC3'] = self.CC3
        self.ICBOF0 = RM_Field_TIMER1_IFC_ICBOF0(self)
        self.zz_fdict['ICBOF0'] = self.ICBOF0
        self.ICBOF1 = RM_Field_TIMER1_IFC_ICBOF1(self)
        self.zz_fdict['ICBOF1'] = self.ICBOF1
        self.ICBOF2 = RM_Field_TIMER1_IFC_ICBOF2(self)
        self.zz_fdict['ICBOF2'] = self.ICBOF2
        self.ICBOF3 = RM_Field_TIMER1_IFC_ICBOF3(self)
        self.zz_fdict['ICBOF3'] = self.ICBOF3
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_IEN, self).__init__(rmio, label,
            0x40018400, 0x018,
            'IEN', 'TIMER1.IEN', 'read-write',
            "",
            0x00000000, 0x00000FF7)

        self.OF = RM_Field_TIMER1_IEN_OF(self)
        self.zz_fdict['OF'] = self.OF
        self.UF = RM_Field_TIMER1_IEN_UF(self)
        self.zz_fdict['UF'] = self.UF
        self.DIRCHG = RM_Field_TIMER1_IEN_DIRCHG(self)
        self.zz_fdict['DIRCHG'] = self.DIRCHG
        self.CC0 = RM_Field_TIMER1_IEN_CC0(self)
        self.zz_fdict['CC0'] = self.CC0
        self.CC1 = RM_Field_TIMER1_IEN_CC1(self)
        self.zz_fdict['CC1'] = self.CC1
        self.CC2 = RM_Field_TIMER1_IEN_CC2(self)
        self.zz_fdict['CC2'] = self.CC2
        self.CC3 = RM_Field_TIMER1_IEN_CC3(self)
        self.zz_fdict['CC3'] = self.CC3
        self.ICBOF0 = RM_Field_TIMER1_IEN_ICBOF0(self)
        self.zz_fdict['ICBOF0'] = self.ICBOF0
        self.ICBOF1 = RM_Field_TIMER1_IEN_ICBOF1(self)
        self.zz_fdict['ICBOF1'] = self.ICBOF1
        self.ICBOF2 = RM_Field_TIMER1_IEN_ICBOF2(self)
        self.zz_fdict['ICBOF2'] = self.ICBOF2
        self.ICBOF3 = RM_Field_TIMER1_IEN_ICBOF3(self)
        self.zz_fdict['ICBOF3'] = self.ICBOF3
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_TOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_TOP, self).__init__(rmio, label,
            0x40018400, 0x01C,
            'TOP', 'TIMER1.TOP', 'read-write',
            "",
            0x0000FFFF, 0x0000FFFF)

        self.TOP = RM_Field_TIMER1_TOP_TOP(self)
        self.zz_fdict['TOP'] = self.TOP
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_TOPB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_TOPB, self).__init__(rmio, label,
            0x40018400, 0x020,
            'TOPB', 'TIMER1.TOPB', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TOPB = RM_Field_TIMER1_TOPB_TOPB(self)
        self.zz_fdict['TOPB'] = self.TOPB
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CNT, self).__init__(rmio, label,
            0x40018400, 0x024,
            'CNT', 'TIMER1.CNT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.CNT = RM_Field_TIMER1_CNT_CNT(self)
        self.zz_fdict['CNT'] = self.CNT
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_LOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_LOCK, self).__init__(rmio, label,
            0x40018400, 0x02C,
            'LOCK', 'TIMER1.LOCK', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TIMERLOCKKEY = RM_Field_TIMER1_LOCK_TIMERLOCKKEY(self)
        self.zz_fdict['TIMERLOCKKEY'] = self.TIMERLOCKKEY
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_ROUTEPEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_ROUTEPEN, self).__init__(rmio, label,
            0x40018400, 0x030,
            'ROUTEPEN', 'TIMER1.ROUTEPEN', 'read-write',
            "",
            0x00000000, 0x0000070F)

        self.CC0PEN = RM_Field_TIMER1_ROUTEPEN_CC0PEN(self)
        self.zz_fdict['CC0PEN'] = self.CC0PEN
        self.CC1PEN = RM_Field_TIMER1_ROUTEPEN_CC1PEN(self)
        self.zz_fdict['CC1PEN'] = self.CC1PEN
        self.CC2PEN = RM_Field_TIMER1_ROUTEPEN_CC2PEN(self)
        self.zz_fdict['CC2PEN'] = self.CC2PEN
        self.CC3PEN = RM_Field_TIMER1_ROUTEPEN_CC3PEN(self)
        self.zz_fdict['CC3PEN'] = self.CC3PEN
        self.CDTI0PEN = RM_Field_TIMER1_ROUTEPEN_CDTI0PEN(self)
        self.zz_fdict['CDTI0PEN'] = self.CDTI0PEN
        self.CDTI1PEN = RM_Field_TIMER1_ROUTEPEN_CDTI1PEN(self)
        self.zz_fdict['CDTI1PEN'] = self.CDTI1PEN
        self.CDTI2PEN = RM_Field_TIMER1_ROUTEPEN_CDTI2PEN(self)
        self.zz_fdict['CDTI2PEN'] = self.CDTI2PEN
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_ROUTELOC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_ROUTELOC0, self).__init__(rmio, label,
            0x40018400, 0x034,
            'ROUTELOC0', 'TIMER1.ROUTELOC0', 'read-write',
            "",
            0x00000000, 0x3F3F3F3F)

        self.CC0LOC = RM_Field_TIMER1_ROUTELOC0_CC0LOC(self)
        self.zz_fdict['CC0LOC'] = self.CC0LOC
        self.CC1LOC = RM_Field_TIMER1_ROUTELOC0_CC1LOC(self)
        self.zz_fdict['CC1LOC'] = self.CC1LOC
        self.CC2LOC = RM_Field_TIMER1_ROUTELOC0_CC2LOC(self)
        self.zz_fdict['CC2LOC'] = self.CC2LOC
        self.CC3LOC = RM_Field_TIMER1_ROUTELOC0_CC3LOC(self)
        self.zz_fdict['CC3LOC'] = self.CC3LOC
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_ROUTELOC2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_ROUTELOC2, self).__init__(rmio, label,
            0x40018400, 0x03C,
            'ROUTELOC2', 'TIMER1.ROUTELOC2', 'read-write',
            "",
            0x00000000, 0x003F3F3F)

        self.CDTI0LOC = RM_Field_TIMER1_ROUTELOC2_CDTI0LOC(self)
        self.zz_fdict['CDTI0LOC'] = self.CDTI0LOC
        self.CDTI1LOC = RM_Field_TIMER1_ROUTELOC2_CDTI1LOC(self)
        self.zz_fdict['CDTI1LOC'] = self.CDTI1LOC
        self.CDTI2LOC = RM_Field_TIMER1_ROUTELOC2_CDTI2LOC(self)
        self.zz_fdict['CDTI2LOC'] = self.CDTI2LOC
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC0_CTRL, self).__init__(rmio, label,
            0x40018400, 0x060,
            'CC0_CTRL', 'TIMER1.CC0_CTRL', 'read-write',
            "",
            0x00000000, 0x7F0F3F17)

        self.MODE = RM_Field_TIMER1_CC0_CTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.OUTINV = RM_Field_TIMER1_CC0_CTRL_OUTINV(self)
        self.zz_fdict['OUTINV'] = self.OUTINV
        self.COIST = RM_Field_TIMER1_CC0_CTRL_COIST(self)
        self.zz_fdict['COIST'] = self.COIST
        self.CMOA = RM_Field_TIMER1_CC0_CTRL_CMOA(self)
        self.zz_fdict['CMOA'] = self.CMOA
        self.COFOA = RM_Field_TIMER1_CC0_CTRL_COFOA(self)
        self.zz_fdict['COFOA'] = self.COFOA
        self.CUFOA = RM_Field_TIMER1_CC0_CTRL_CUFOA(self)
        self.zz_fdict['CUFOA'] = self.CUFOA
        self.PRSSEL = RM_Field_TIMER1_CC0_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.ICEDGE = RM_Field_TIMER1_CC0_CTRL_ICEDGE(self)
        self.zz_fdict['ICEDGE'] = self.ICEDGE
        self.ICEVCTRL = RM_Field_TIMER1_CC0_CTRL_ICEVCTRL(self)
        self.zz_fdict['ICEVCTRL'] = self.ICEVCTRL
        self.PRSCONF = RM_Field_TIMER1_CC0_CTRL_PRSCONF(self)
        self.zz_fdict['PRSCONF'] = self.PRSCONF
        self.INSEL = RM_Field_TIMER1_CC0_CTRL_INSEL(self)
        self.zz_fdict['INSEL'] = self.INSEL
        self.FILT = RM_Field_TIMER1_CC0_CTRL_FILT(self)
        self.zz_fdict['FILT'] = self.FILT
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC0_CCV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC0_CCV, self).__init__(rmio, label,
            0x40018400, 0x064,
            'CC0_CCV', 'TIMER1.CC0_CCV', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.CCV = RM_Field_TIMER1_CC0_CCV_CCV(self)
        self.zz_fdict['CCV'] = self.CCV
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC0_CCVP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC0_CCVP, self).__init__(rmio, label,
            0x40018400, 0x068,
            'CC0_CCVP', 'TIMER1.CC0_CCVP', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.CCVP = RM_Field_TIMER1_CC0_CCVP_CCVP(self)
        self.zz_fdict['CCVP'] = self.CCVP
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC0_CCVB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC0_CCVB, self).__init__(rmio, label,
            0x40018400, 0x06C,
            'CC0_CCVB', 'TIMER1.CC0_CCVB', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.CCVB = RM_Field_TIMER1_CC0_CCVB_CCVB(self)
        self.zz_fdict['CCVB'] = self.CCVB
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC1_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC1_CTRL, self).__init__(rmio, label,
            0x40018400, 0x070,
            'CC1_CTRL', 'TIMER1.CC1_CTRL', 'read-write',
            "",
            0x00000000, 0x7F0F3F17)

        self.MODE = RM_Field_TIMER1_CC1_CTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.OUTINV = RM_Field_TIMER1_CC1_CTRL_OUTINV(self)
        self.zz_fdict['OUTINV'] = self.OUTINV
        self.COIST = RM_Field_TIMER1_CC1_CTRL_COIST(self)
        self.zz_fdict['COIST'] = self.COIST
        self.CMOA = RM_Field_TIMER1_CC1_CTRL_CMOA(self)
        self.zz_fdict['CMOA'] = self.CMOA
        self.COFOA = RM_Field_TIMER1_CC1_CTRL_COFOA(self)
        self.zz_fdict['COFOA'] = self.COFOA
        self.CUFOA = RM_Field_TIMER1_CC1_CTRL_CUFOA(self)
        self.zz_fdict['CUFOA'] = self.CUFOA
        self.PRSSEL = RM_Field_TIMER1_CC1_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.ICEDGE = RM_Field_TIMER1_CC1_CTRL_ICEDGE(self)
        self.zz_fdict['ICEDGE'] = self.ICEDGE
        self.ICEVCTRL = RM_Field_TIMER1_CC1_CTRL_ICEVCTRL(self)
        self.zz_fdict['ICEVCTRL'] = self.ICEVCTRL
        self.PRSCONF = RM_Field_TIMER1_CC1_CTRL_PRSCONF(self)
        self.zz_fdict['PRSCONF'] = self.PRSCONF
        self.INSEL = RM_Field_TIMER1_CC1_CTRL_INSEL(self)
        self.zz_fdict['INSEL'] = self.INSEL
        self.FILT = RM_Field_TIMER1_CC1_CTRL_FILT(self)
        self.zz_fdict['FILT'] = self.FILT
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC1_CCV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC1_CCV, self).__init__(rmio, label,
            0x40018400, 0x074,
            'CC1_CCV', 'TIMER1.CC1_CCV', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.CCV = RM_Field_TIMER1_CC1_CCV_CCV(self)
        self.zz_fdict['CCV'] = self.CCV
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC1_CCVP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC1_CCVP, self).__init__(rmio, label,
            0x40018400, 0x078,
            'CC1_CCVP', 'TIMER1.CC1_CCVP', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.CCVP = RM_Field_TIMER1_CC1_CCVP_CCVP(self)
        self.zz_fdict['CCVP'] = self.CCVP
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC1_CCVB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC1_CCVB, self).__init__(rmio, label,
            0x40018400, 0x07C,
            'CC1_CCVB', 'TIMER1.CC1_CCVB', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.CCVB = RM_Field_TIMER1_CC1_CCVB_CCVB(self)
        self.zz_fdict['CCVB'] = self.CCVB
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC2_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC2_CTRL, self).__init__(rmio, label,
            0x40018400, 0x080,
            'CC2_CTRL', 'TIMER1.CC2_CTRL', 'read-write',
            "",
            0x00000000, 0x7F0F3F17)

        self.MODE = RM_Field_TIMER1_CC2_CTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.OUTINV = RM_Field_TIMER1_CC2_CTRL_OUTINV(self)
        self.zz_fdict['OUTINV'] = self.OUTINV
        self.COIST = RM_Field_TIMER1_CC2_CTRL_COIST(self)
        self.zz_fdict['COIST'] = self.COIST
        self.CMOA = RM_Field_TIMER1_CC2_CTRL_CMOA(self)
        self.zz_fdict['CMOA'] = self.CMOA
        self.COFOA = RM_Field_TIMER1_CC2_CTRL_COFOA(self)
        self.zz_fdict['COFOA'] = self.COFOA
        self.CUFOA = RM_Field_TIMER1_CC2_CTRL_CUFOA(self)
        self.zz_fdict['CUFOA'] = self.CUFOA
        self.PRSSEL = RM_Field_TIMER1_CC2_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.ICEDGE = RM_Field_TIMER1_CC2_CTRL_ICEDGE(self)
        self.zz_fdict['ICEDGE'] = self.ICEDGE
        self.ICEVCTRL = RM_Field_TIMER1_CC2_CTRL_ICEVCTRL(self)
        self.zz_fdict['ICEVCTRL'] = self.ICEVCTRL
        self.PRSCONF = RM_Field_TIMER1_CC2_CTRL_PRSCONF(self)
        self.zz_fdict['PRSCONF'] = self.PRSCONF
        self.INSEL = RM_Field_TIMER1_CC2_CTRL_INSEL(self)
        self.zz_fdict['INSEL'] = self.INSEL
        self.FILT = RM_Field_TIMER1_CC2_CTRL_FILT(self)
        self.zz_fdict['FILT'] = self.FILT
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC2_CCV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC2_CCV, self).__init__(rmio, label,
            0x40018400, 0x084,
            'CC2_CCV', 'TIMER1.CC2_CCV', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.CCV = RM_Field_TIMER1_CC2_CCV_CCV(self)
        self.zz_fdict['CCV'] = self.CCV
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC2_CCVP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC2_CCVP, self).__init__(rmio, label,
            0x40018400, 0x088,
            'CC2_CCVP', 'TIMER1.CC2_CCVP', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.CCVP = RM_Field_TIMER1_CC2_CCVP_CCVP(self)
        self.zz_fdict['CCVP'] = self.CCVP
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC2_CCVB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC2_CCVB, self).__init__(rmio, label,
            0x40018400, 0x08C,
            'CC2_CCVB', 'TIMER1.CC2_CCVB', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.CCVB = RM_Field_TIMER1_CC2_CCVB_CCVB(self)
        self.zz_fdict['CCVB'] = self.CCVB
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC3_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC3_CTRL, self).__init__(rmio, label,
            0x40018400, 0x090,
            'CC3_CTRL', 'TIMER1.CC3_CTRL', 'read-write',
            "",
            0x00000000, 0x7F0F3F17)

        self.MODE = RM_Field_TIMER1_CC3_CTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.OUTINV = RM_Field_TIMER1_CC3_CTRL_OUTINV(self)
        self.zz_fdict['OUTINV'] = self.OUTINV
        self.COIST = RM_Field_TIMER1_CC3_CTRL_COIST(self)
        self.zz_fdict['COIST'] = self.COIST
        self.CMOA = RM_Field_TIMER1_CC3_CTRL_CMOA(self)
        self.zz_fdict['CMOA'] = self.CMOA
        self.COFOA = RM_Field_TIMER1_CC3_CTRL_COFOA(self)
        self.zz_fdict['COFOA'] = self.COFOA
        self.CUFOA = RM_Field_TIMER1_CC3_CTRL_CUFOA(self)
        self.zz_fdict['CUFOA'] = self.CUFOA
        self.PRSSEL = RM_Field_TIMER1_CC3_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.ICEDGE = RM_Field_TIMER1_CC3_CTRL_ICEDGE(self)
        self.zz_fdict['ICEDGE'] = self.ICEDGE
        self.ICEVCTRL = RM_Field_TIMER1_CC3_CTRL_ICEVCTRL(self)
        self.zz_fdict['ICEVCTRL'] = self.ICEVCTRL
        self.PRSCONF = RM_Field_TIMER1_CC3_CTRL_PRSCONF(self)
        self.zz_fdict['PRSCONF'] = self.PRSCONF
        self.INSEL = RM_Field_TIMER1_CC3_CTRL_INSEL(self)
        self.zz_fdict['INSEL'] = self.INSEL
        self.FILT = RM_Field_TIMER1_CC3_CTRL_FILT(self)
        self.zz_fdict['FILT'] = self.FILT
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC3_CCV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC3_CCV, self).__init__(rmio, label,
            0x40018400, 0x094,
            'CC3_CCV', 'TIMER1.CC3_CCV', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.CCV = RM_Field_TIMER1_CC3_CCV_CCV(self)
        self.zz_fdict['CCV'] = self.CCV
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC3_CCVP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC3_CCVP, self).__init__(rmio, label,
            0x40018400, 0x098,
            'CC3_CCVP', 'TIMER1.CC3_CCVP', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.CCVP = RM_Field_TIMER1_CC3_CCVP_CCVP(self)
        self.zz_fdict['CCVP'] = self.CCVP
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_CC3_CCVB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_CC3_CCVB, self).__init__(rmio, label,
            0x40018400, 0x09C,
            'CC3_CCVB', 'TIMER1.CC3_CCVB', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.CCVB = RM_Field_TIMER1_CC3_CCVB_CCVB(self)
        self.zz_fdict['CCVB'] = self.CCVB
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_DTCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_DTCTRL, self).__init__(rmio, label,
            0x40018400, 0x0A0,
            'DTCTRL', 'TIMER1.DTCTRL', 'read-write',
            "",
            0x00000000, 0x010006FF)

        self.DTEN = RM_Field_TIMER1_DTCTRL_DTEN(self)
        self.zz_fdict['DTEN'] = self.DTEN
        self.DTDAS = RM_Field_TIMER1_DTCTRL_DTDAS(self)
        self.zz_fdict['DTDAS'] = self.DTDAS
        self.DTIPOL = RM_Field_TIMER1_DTCTRL_DTIPOL(self)
        self.zz_fdict['DTIPOL'] = self.DTIPOL
        self.DTCINV = RM_Field_TIMER1_DTCTRL_DTCINV(self)
        self.zz_fdict['DTCINV'] = self.DTCINV
        self.DTPRSSEL = RM_Field_TIMER1_DTCTRL_DTPRSSEL(self)
        self.zz_fdict['DTPRSSEL'] = self.DTPRSSEL
        self.DTAR = RM_Field_TIMER1_DTCTRL_DTAR(self)
        self.zz_fdict['DTAR'] = self.DTAR
        self.DTFATS = RM_Field_TIMER1_DTCTRL_DTFATS(self)
        self.zz_fdict['DTFATS'] = self.DTFATS
        self.DTPRSEN = RM_Field_TIMER1_DTCTRL_DTPRSEN(self)
        self.zz_fdict['DTPRSEN'] = self.DTPRSEN
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_DTTIME(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_DTTIME, self).__init__(rmio, label,
            0x40018400, 0x0A4,
            'DTTIME', 'TIMER1.DTTIME', 'read-write',
            "",
            0x00000000, 0x003F3F0F)

        self.DTPRESC = RM_Field_TIMER1_DTTIME_DTPRESC(self)
        self.zz_fdict['DTPRESC'] = self.DTPRESC
        self.DTRISET = RM_Field_TIMER1_DTTIME_DTRISET(self)
        self.zz_fdict['DTRISET'] = self.DTRISET
        self.DTFALLT = RM_Field_TIMER1_DTTIME_DTFALLT(self)
        self.zz_fdict['DTFALLT'] = self.DTFALLT
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_DTFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_DTFC, self).__init__(rmio, label,
            0x40018400, 0x0A8,
            'DTFC', 'TIMER1.DTFC', 'read-write',
            "",
            0x00000000, 0x0F030F0F)

        self.DTPRS0FSEL = RM_Field_TIMER1_DTFC_DTPRS0FSEL(self)
        self.zz_fdict['DTPRS0FSEL'] = self.DTPRS0FSEL
        self.DTPRS1FSEL = RM_Field_TIMER1_DTFC_DTPRS1FSEL(self)
        self.zz_fdict['DTPRS1FSEL'] = self.DTPRS1FSEL
        self.DTFA = RM_Field_TIMER1_DTFC_DTFA(self)
        self.zz_fdict['DTFA'] = self.DTFA
        self.DTPRS0FEN = RM_Field_TIMER1_DTFC_DTPRS0FEN(self)
        self.zz_fdict['DTPRS0FEN'] = self.DTPRS0FEN
        self.DTPRS1FEN = RM_Field_TIMER1_DTFC_DTPRS1FEN(self)
        self.zz_fdict['DTPRS1FEN'] = self.DTPRS1FEN
        self.DTDBGFEN = RM_Field_TIMER1_DTFC_DTDBGFEN(self)
        self.zz_fdict['DTDBGFEN'] = self.DTDBGFEN
        self.DTLOCKUPFEN = RM_Field_TIMER1_DTFC_DTLOCKUPFEN(self)
        self.zz_fdict['DTLOCKUPFEN'] = self.DTLOCKUPFEN
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_DTOGEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_DTOGEN, self).__init__(rmio, label,
            0x40018400, 0x0AC,
            'DTOGEN', 'TIMER1.DTOGEN', 'read-write',
            "",
            0x00000000, 0x0000003F)

        self.DTOGCC0EN = RM_Field_TIMER1_DTOGEN_DTOGCC0EN(self)
        self.zz_fdict['DTOGCC0EN'] = self.DTOGCC0EN
        self.DTOGCC1EN = RM_Field_TIMER1_DTOGEN_DTOGCC1EN(self)
        self.zz_fdict['DTOGCC1EN'] = self.DTOGCC1EN
        self.DTOGCC2EN = RM_Field_TIMER1_DTOGEN_DTOGCC2EN(self)
        self.zz_fdict['DTOGCC2EN'] = self.DTOGCC2EN
        self.DTOGCDTI0EN = RM_Field_TIMER1_DTOGEN_DTOGCDTI0EN(self)
        self.zz_fdict['DTOGCDTI0EN'] = self.DTOGCDTI0EN
        self.DTOGCDTI1EN = RM_Field_TIMER1_DTOGEN_DTOGCDTI1EN(self)
        self.zz_fdict['DTOGCDTI1EN'] = self.DTOGCDTI1EN
        self.DTOGCDTI2EN = RM_Field_TIMER1_DTOGEN_DTOGCDTI2EN(self)
        self.zz_fdict['DTOGCDTI2EN'] = self.DTOGCDTI2EN
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_DTFAULT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_DTFAULT, self).__init__(rmio, label,
            0x40018400, 0x0B0,
            'DTFAULT', 'TIMER1.DTFAULT', 'read-only',
            "",
            0x00000000, 0x0000000F)

        self.DTPRS0F = RM_Field_TIMER1_DTFAULT_DTPRS0F(self)
        self.zz_fdict['DTPRS0F'] = self.DTPRS0F
        self.DTPRS1F = RM_Field_TIMER1_DTFAULT_DTPRS1F(self)
        self.zz_fdict['DTPRS1F'] = self.DTPRS1F
        self.DTDBGF = RM_Field_TIMER1_DTFAULT_DTDBGF(self)
        self.zz_fdict['DTDBGF'] = self.DTDBGF
        self.DTLOCKUPF = RM_Field_TIMER1_DTFAULT_DTLOCKUPF(self)
        self.zz_fdict['DTLOCKUPF'] = self.DTLOCKUPF
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_DTFAULTC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_DTFAULTC, self).__init__(rmio, label,
            0x40018400, 0x0B4,
            'DTFAULTC', 'TIMER1.DTFAULTC', 'write-only',
            "",
            0x00000000, 0x0000000F)

        self.DTPRS0FC = RM_Field_TIMER1_DTFAULTC_DTPRS0FC(self)
        self.zz_fdict['DTPRS0FC'] = self.DTPRS0FC
        self.DTPRS1FC = RM_Field_TIMER1_DTFAULTC_DTPRS1FC(self)
        self.zz_fdict['DTPRS1FC'] = self.DTPRS1FC
        self.DTDBGFC = RM_Field_TIMER1_DTFAULTC_DTDBGFC(self)
        self.zz_fdict['DTDBGFC'] = self.DTDBGFC
        self.TLOCKUPFC = RM_Field_TIMER1_DTFAULTC_TLOCKUPFC(self)
        self.zz_fdict['TLOCKUPFC'] = self.TLOCKUPFC
        self.__dict__['zz_frozen'] = True


class RM_Register_TIMER1_DTLOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_TIMER1_DTLOCK, self).__init__(rmio, label,
            0x40018400, 0x0B8,
            'DTLOCK', 'TIMER1.DTLOCK', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.LOCKKEY = RM_Field_TIMER1_DTLOCK_LOCKKEY(self)
        self.zz_fdict['LOCKKEY'] = self.LOCKKEY
        self.__dict__['zz_frozen'] = True


