
from static import Base_RM_Register
from PCNT0_field import *


class RM_Register_PCNT0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_CTRL, self).__init__(rmio, label,
            0x4004e000, 0x000,
            'CTRL', 'PCNT0.CTRL', 'read-write',
            "",
            0x00000000, 0xBFDBFFFF)

        self.MODE = RM_Field_PCNT0_CTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.FILT = RM_Field_PCNT0_CTRL_FILT(self)
        self.zz_fdict['FILT'] = self.FILT
        self.RSTEN = RM_Field_PCNT0_CTRL_RSTEN(self)
        self.zz_fdict['RSTEN'] = self.RSTEN
        self.CNTRSTEN = RM_Field_PCNT0_CTRL_CNTRSTEN(self)
        self.zz_fdict['CNTRSTEN'] = self.CNTRSTEN
        self.AUXCNTRSTEN = RM_Field_PCNT0_CTRL_AUXCNTRSTEN(self)
        self.zz_fdict['AUXCNTRSTEN'] = self.AUXCNTRSTEN
        self.DEBUGHALT = RM_Field_PCNT0_CTRL_DEBUGHALT(self)
        self.zz_fdict['DEBUGHALT'] = self.DEBUGHALT
        self.HYST = RM_Field_PCNT0_CTRL_HYST(self)
        self.zz_fdict['HYST'] = self.HYST
        self.S1CDIR = RM_Field_PCNT0_CTRL_S1CDIR(self)
        self.zz_fdict['S1CDIR'] = self.S1CDIR
        self.CNTEV = RM_Field_PCNT0_CTRL_CNTEV(self)
        self.zz_fdict['CNTEV'] = self.CNTEV
        self.AUXCNTEV = RM_Field_PCNT0_CTRL_AUXCNTEV(self)
        self.zz_fdict['AUXCNTEV'] = self.AUXCNTEV
        self.CNTDIR = RM_Field_PCNT0_CTRL_CNTDIR(self)
        self.zz_fdict['CNTDIR'] = self.CNTDIR
        self.EDGE = RM_Field_PCNT0_CTRL_EDGE(self)
        self.zz_fdict['EDGE'] = self.EDGE
        self.TCCMODE = RM_Field_PCNT0_CTRL_TCCMODE(self)
        self.zz_fdict['TCCMODE'] = self.TCCMODE
        self.TCCPRESC = RM_Field_PCNT0_CTRL_TCCPRESC(self)
        self.zz_fdict['TCCPRESC'] = self.TCCPRESC
        self.TCCCOMP = RM_Field_PCNT0_CTRL_TCCCOMP(self)
        self.zz_fdict['TCCCOMP'] = self.TCCCOMP
        self.PRSGATEEN = RM_Field_PCNT0_CTRL_PRSGATEEN(self)
        self.zz_fdict['PRSGATEEN'] = self.PRSGATEEN
        self.TCCPRSPOL = RM_Field_PCNT0_CTRL_TCCPRSPOL(self)
        self.zz_fdict['TCCPRSPOL'] = self.TCCPRSPOL
        self.TCCPRSSEL = RM_Field_PCNT0_CTRL_TCCPRSSEL(self)
        self.zz_fdict['TCCPRSSEL'] = self.TCCPRSSEL
        self.TOPBHFSEL = RM_Field_PCNT0_CTRL_TOPBHFSEL(self)
        self.zz_fdict['TOPBHFSEL'] = self.TOPBHFSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_CMD, self).__init__(rmio, label,
            0x4004e000, 0x004,
            'CMD', 'PCNT0.CMD', 'write-only',
            "",
            0x00000000, 0x00000003)

        self.LCNTIM = RM_Field_PCNT0_CMD_LCNTIM(self)
        self.zz_fdict['LCNTIM'] = self.LCNTIM
        self.LTOPBIM = RM_Field_PCNT0_CMD_LTOPBIM(self)
        self.zz_fdict['LTOPBIM'] = self.LTOPBIM
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_STATUS, self).__init__(rmio, label,
            0x4004e000, 0x008,
            'STATUS', 'PCNT0.STATUS', 'read-only',
            "",
            0x00000000, 0x00000001)

        self.DIR = RM_Field_PCNT0_STATUS_DIR(self)
        self.zz_fdict['DIR'] = self.DIR
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_CNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_CNT, self).__init__(rmio, label,
            0x4004e000, 0x00C,
            'CNT', 'PCNT0.CNT', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.CNT = RM_Field_PCNT0_CNT_CNT(self)
        self.zz_fdict['CNT'] = self.CNT
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_TOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_TOP, self).__init__(rmio, label,
            0x4004e000, 0x010,
            'TOP', 'PCNT0.TOP', 'read-only',
            "",
            0x000000FF, 0x0000FFFF)

        self.TOP = RM_Field_PCNT0_TOP_TOP(self)
        self.zz_fdict['TOP'] = self.TOP
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_TOPB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_TOPB, self).__init__(rmio, label,
            0x4004e000, 0x014,
            'TOPB', 'PCNT0.TOPB', 'read-write',
            "",
            0x000000FF, 0x0000FFFF)

        self.TOPB = RM_Field_PCNT0_TOPB_TOPB(self)
        self.zz_fdict['TOPB'] = self.TOPB
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_IF, self).__init__(rmio, label,
            0x4004e000, 0x018,
            'IF', 'PCNT0.IF', 'read-only',
            "",
            0x00000000, 0x0000003F)

        self.UF = RM_Field_PCNT0_IF_UF(self)
        self.zz_fdict['UF'] = self.UF
        self.OF = RM_Field_PCNT0_IF_OF(self)
        self.zz_fdict['OF'] = self.OF
        self.DIRCNG = RM_Field_PCNT0_IF_DIRCNG(self)
        self.zz_fdict['DIRCNG'] = self.DIRCNG
        self.AUXOF = RM_Field_PCNT0_IF_AUXOF(self)
        self.zz_fdict['AUXOF'] = self.AUXOF
        self.TCC = RM_Field_PCNT0_IF_TCC(self)
        self.zz_fdict['TCC'] = self.TCC
        self.OQSTERR = RM_Field_PCNT0_IF_OQSTERR(self)
        self.zz_fdict['OQSTERR'] = self.OQSTERR
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_IFS, self).__init__(rmio, label,
            0x4004e000, 0x01C,
            'IFS', 'PCNT0.IFS', 'write-only',
            "",
            0x00000000, 0x0000003F)

        self.UF = RM_Field_PCNT0_IFS_UF(self)
        self.zz_fdict['UF'] = self.UF
        self.OF = RM_Field_PCNT0_IFS_OF(self)
        self.zz_fdict['OF'] = self.OF
        self.DIRCNG = RM_Field_PCNT0_IFS_DIRCNG(self)
        self.zz_fdict['DIRCNG'] = self.DIRCNG
        self.AUXOF = RM_Field_PCNT0_IFS_AUXOF(self)
        self.zz_fdict['AUXOF'] = self.AUXOF
        self.TCC = RM_Field_PCNT0_IFS_TCC(self)
        self.zz_fdict['TCC'] = self.TCC
        self.OQSTERR = RM_Field_PCNT0_IFS_OQSTERR(self)
        self.zz_fdict['OQSTERR'] = self.OQSTERR
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_IFC, self).__init__(rmio, label,
            0x4004e000, 0x020,
            'IFC', 'PCNT0.IFC', 'write-only',
            "",
            0x00000000, 0x0000003F)

        self.UF = RM_Field_PCNT0_IFC_UF(self)
        self.zz_fdict['UF'] = self.UF
        self.OF = RM_Field_PCNT0_IFC_OF(self)
        self.zz_fdict['OF'] = self.OF
        self.DIRCNG = RM_Field_PCNT0_IFC_DIRCNG(self)
        self.zz_fdict['DIRCNG'] = self.DIRCNG
        self.AUXOF = RM_Field_PCNT0_IFC_AUXOF(self)
        self.zz_fdict['AUXOF'] = self.AUXOF
        self.TCC = RM_Field_PCNT0_IFC_TCC(self)
        self.zz_fdict['TCC'] = self.TCC
        self.OQSTERR = RM_Field_PCNT0_IFC_OQSTERR(self)
        self.zz_fdict['OQSTERR'] = self.OQSTERR
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_IEN, self).__init__(rmio, label,
            0x4004e000, 0x024,
            'IEN', 'PCNT0.IEN', 'read-write',
            "",
            0x00000000, 0x0000003F)

        self.UF = RM_Field_PCNT0_IEN_UF(self)
        self.zz_fdict['UF'] = self.UF
        self.OF = RM_Field_PCNT0_IEN_OF(self)
        self.zz_fdict['OF'] = self.OF
        self.DIRCNG = RM_Field_PCNT0_IEN_DIRCNG(self)
        self.zz_fdict['DIRCNG'] = self.DIRCNG
        self.AUXOF = RM_Field_PCNT0_IEN_AUXOF(self)
        self.zz_fdict['AUXOF'] = self.AUXOF
        self.TCC = RM_Field_PCNT0_IEN_TCC(self)
        self.zz_fdict['TCC'] = self.TCC
        self.OQSTERR = RM_Field_PCNT0_IEN_OQSTERR(self)
        self.zz_fdict['OQSTERR'] = self.OQSTERR
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_ROUTELOC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_ROUTELOC0, self).__init__(rmio, label,
            0x4004e000, 0x02C,
            'ROUTELOC0', 'PCNT0.ROUTELOC0', 'read-write',
            "",
            0x00000000, 0x00003F3F)

        self.S0INLOC = RM_Field_PCNT0_ROUTELOC0_S0INLOC(self)
        self.zz_fdict['S0INLOC'] = self.S0INLOC
        self.S1INLOC = RM_Field_PCNT0_ROUTELOC0_S1INLOC(self)
        self.zz_fdict['S1INLOC'] = self.S1INLOC
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_FREEZE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_FREEZE, self).__init__(rmio, label,
            0x4004e000, 0x040,
            'FREEZE', 'PCNT0.FREEZE', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.REGFREEZE = RM_Field_PCNT0_FREEZE_REGFREEZE(self)
        self.zz_fdict['REGFREEZE'] = self.REGFREEZE
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_SYNCBUSY(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_SYNCBUSY, self).__init__(rmio, label,
            0x4004e000, 0x044,
            'SYNCBUSY', 'PCNT0.SYNCBUSY', 'read-only',
            "",
            0x00000000, 0x0000000F)

        self.CTRL = RM_Field_PCNT0_SYNCBUSY_CTRL(self)
        self.zz_fdict['CTRL'] = self.CTRL
        self.CMD = RM_Field_PCNT0_SYNCBUSY_CMD(self)
        self.zz_fdict['CMD'] = self.CMD
        self.TOPB = RM_Field_PCNT0_SYNCBUSY_TOPB(self)
        self.zz_fdict['TOPB'] = self.TOPB
        self.OVSCFG = RM_Field_PCNT0_SYNCBUSY_OVSCFG(self)
        self.zz_fdict['OVSCFG'] = self.OVSCFG
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_AUXCNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_AUXCNT, self).__init__(rmio, label,
            0x4004e000, 0x064,
            'AUXCNT', 'PCNT0.AUXCNT', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.AUXCNT = RM_Field_PCNT0_AUXCNT_AUXCNT(self)
        self.zz_fdict['AUXCNT'] = self.AUXCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_INPUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_INPUT, self).__init__(rmio, label,
            0x4004e000, 0x068,
            'INPUT', 'PCNT0.INPUT', 'read-write',
            "",
            0x00000000, 0x00000BEF)

        self.S0PRSSEL = RM_Field_PCNT0_INPUT_S0PRSSEL(self)
        self.zz_fdict['S0PRSSEL'] = self.S0PRSSEL
        self.S0PRSEN = RM_Field_PCNT0_INPUT_S0PRSEN(self)
        self.zz_fdict['S0PRSEN'] = self.S0PRSEN
        self.S1PRSSEL = RM_Field_PCNT0_INPUT_S1PRSSEL(self)
        self.zz_fdict['S1PRSSEL'] = self.S1PRSSEL
        self.S1PRSEN = RM_Field_PCNT0_INPUT_S1PRSEN(self)
        self.zz_fdict['S1PRSEN'] = self.S1PRSEN
        self.__dict__['zz_frozen'] = True


class RM_Register_PCNT0_OVSCFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PCNT0_OVSCFG, self).__init__(rmio, label,
            0x4004e000, 0x06C,
            'OVSCFG', 'PCNT0.OVSCFG', 'read-write',
            "",
            0x00000000, 0x000010FF)

        self.FILTLEN = RM_Field_PCNT0_OVSCFG_FILTLEN(self)
        self.zz_fdict['FILTLEN'] = self.FILTLEN
        self.FLUTTERRM = RM_Field_PCNT0_OVSCFG_FLUTTERRM(self)
        self.zz_fdict['FLUTTERRM'] = self.FLUTTERRM
        self.__dict__['zz_frozen'] = True


