
from static import Base_RM_Field
from PCNT0_enum import *


class RM_Field_PCNT0_CTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_MODE, self).__init__(register,
            'MODE', 'PCNT0.CTRL.MODE', 'read-write',
            "",
            0, 3,
            RM_Enum_PCNT0_CTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_FILT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_FILT, self).__init__(register,
            'FILT', 'PCNT0.CTRL.FILT', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_RSTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_RSTEN, self).__init__(register,
            'RSTEN', 'PCNT0.CTRL.RSTEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_CNTRSTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_CNTRSTEN, self).__init__(register,
            'CNTRSTEN', 'PCNT0.CTRL.CNTRSTEN', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_AUXCNTRSTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_AUXCNTRSTEN, self).__init__(register,
            'AUXCNTRSTEN', 'PCNT0.CTRL.AUXCNTRSTEN', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_DEBUGHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_DEBUGHALT, self).__init__(register,
            'DEBUGHALT', 'PCNT0.CTRL.DEBUGHALT', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_HYST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_HYST, self).__init__(register,
            'HYST', 'PCNT0.CTRL.HYST', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_S1CDIR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_S1CDIR, self).__init__(register,
            'S1CDIR', 'PCNT0.CTRL.S1CDIR', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_CNTEV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_CNTEV, self).__init__(register,
            'CNTEV', 'PCNT0.CTRL.CNTEV', 'read-write',
            "",
            10, 2,
            RM_Enum_PCNT0_CTRL_CNTEV(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_AUXCNTEV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_AUXCNTEV, self).__init__(register,
            'AUXCNTEV', 'PCNT0.CTRL.AUXCNTEV', 'read-write',
            "",
            12, 2,
            RM_Enum_PCNT0_CTRL_AUXCNTEV(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_CNTDIR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_CNTDIR, self).__init__(register,
            'CNTDIR', 'PCNT0.CTRL.CNTDIR', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_EDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_EDGE, self).__init__(register,
            'EDGE', 'PCNT0.CTRL.EDGE', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_TCCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_TCCMODE, self).__init__(register,
            'TCCMODE', 'PCNT0.CTRL.TCCMODE', 'read-write',
            "",
            16, 2,
            RM_Enum_PCNT0_CTRL_TCCMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_TCCPRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_TCCPRESC, self).__init__(register,
            'TCCPRESC', 'PCNT0.CTRL.TCCPRESC', 'read-write',
            "",
            19, 2,
            RM_Enum_PCNT0_CTRL_TCCPRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_TCCCOMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_TCCCOMP, self).__init__(register,
            'TCCCOMP', 'PCNT0.CTRL.TCCCOMP', 'read-write',
            "",
            22, 2,
            RM_Enum_PCNT0_CTRL_TCCCOMP(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_PRSGATEEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_PRSGATEEN, self).__init__(register,
            'PRSGATEEN', 'PCNT0.CTRL.PRSGATEEN', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_TCCPRSPOL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_TCCPRSPOL, self).__init__(register,
            'TCCPRSPOL', 'PCNT0.CTRL.TCCPRSPOL', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_TCCPRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_TCCPRSSEL, self).__init__(register,
            'TCCPRSSEL', 'PCNT0.CTRL.TCCPRSSEL', 'read-write',
            "",
            26, 4,
            RM_Enum_PCNT0_CTRL_TCCPRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CTRL_TOPBHFSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CTRL_TOPBHFSEL, self).__init__(register,
            'TOPBHFSEL', 'PCNT0.CTRL.TOPBHFSEL', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CMD_LCNTIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CMD_LCNTIM, self).__init__(register,
            'LCNTIM', 'PCNT0.CMD.LCNTIM', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CMD_LTOPBIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CMD_LTOPBIM, self).__init__(register,
            'LTOPBIM', 'PCNT0.CMD.LTOPBIM', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_STATUS_DIR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_STATUS_DIR, self).__init__(register,
            'DIR', 'PCNT0.STATUS.DIR', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_CNT_CNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_CNT_CNT, self).__init__(register,
            'CNT', 'PCNT0.CNT.CNT', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_TOP_TOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_TOP_TOP, self).__init__(register,
            'TOP', 'PCNT0.TOP.TOP', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_TOPB_TOPB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_TOPB_TOPB, self).__init__(register,
            'TOPB', 'PCNT0.TOPB.TOPB', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IF_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IF_UF, self).__init__(register,
            'UF', 'PCNT0.IF.UF', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IF_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IF_OF, self).__init__(register,
            'OF', 'PCNT0.IF.OF', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IF_DIRCNG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IF_DIRCNG, self).__init__(register,
            'DIRCNG', 'PCNT0.IF.DIRCNG', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IF_AUXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IF_AUXOF, self).__init__(register,
            'AUXOF', 'PCNT0.IF.AUXOF', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IF_TCC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IF_TCC, self).__init__(register,
            'TCC', 'PCNT0.IF.TCC', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IF_OQSTERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IF_OQSTERR, self).__init__(register,
            'OQSTERR', 'PCNT0.IF.OQSTERR', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IFS_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IFS_UF, self).__init__(register,
            'UF', 'PCNT0.IFS.UF', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IFS_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IFS_OF, self).__init__(register,
            'OF', 'PCNT0.IFS.OF', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IFS_DIRCNG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IFS_DIRCNG, self).__init__(register,
            'DIRCNG', 'PCNT0.IFS.DIRCNG', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IFS_AUXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IFS_AUXOF, self).__init__(register,
            'AUXOF', 'PCNT0.IFS.AUXOF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IFS_TCC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IFS_TCC, self).__init__(register,
            'TCC', 'PCNT0.IFS.TCC', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IFS_OQSTERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IFS_OQSTERR, self).__init__(register,
            'OQSTERR', 'PCNT0.IFS.OQSTERR', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IFC_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IFC_UF, self).__init__(register,
            'UF', 'PCNT0.IFC.UF', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IFC_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IFC_OF, self).__init__(register,
            'OF', 'PCNT0.IFC.OF', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IFC_DIRCNG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IFC_DIRCNG, self).__init__(register,
            'DIRCNG', 'PCNT0.IFC.DIRCNG', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IFC_AUXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IFC_AUXOF, self).__init__(register,
            'AUXOF', 'PCNT0.IFC.AUXOF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IFC_TCC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IFC_TCC, self).__init__(register,
            'TCC', 'PCNT0.IFC.TCC', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IFC_OQSTERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IFC_OQSTERR, self).__init__(register,
            'OQSTERR', 'PCNT0.IFC.OQSTERR', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IEN_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IEN_UF, self).__init__(register,
            'UF', 'PCNT0.IEN.UF', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IEN_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IEN_OF, self).__init__(register,
            'OF', 'PCNT0.IEN.OF', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IEN_DIRCNG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IEN_DIRCNG, self).__init__(register,
            'DIRCNG', 'PCNT0.IEN.DIRCNG', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IEN_AUXOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IEN_AUXOF, self).__init__(register,
            'AUXOF', 'PCNT0.IEN.AUXOF', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IEN_TCC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IEN_TCC, self).__init__(register,
            'TCC', 'PCNT0.IEN.TCC', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_IEN_OQSTERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_IEN_OQSTERR, self).__init__(register,
            'OQSTERR', 'PCNT0.IEN.OQSTERR', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_ROUTELOC0_S0INLOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_ROUTELOC0_S0INLOC, self).__init__(register,
            'S0INLOC', 'PCNT0.ROUTELOC0.S0INLOC', 'read-write',
            "",
            0, 6,
            RM_Enum_PCNT0_ROUTELOC0_S0INLOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_ROUTELOC0_S1INLOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_ROUTELOC0_S1INLOC, self).__init__(register,
            'S1INLOC', 'PCNT0.ROUTELOC0.S1INLOC', 'read-write',
            "",
            8, 6,
            RM_Enum_PCNT0_ROUTELOC0_S1INLOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_FREEZE_REGFREEZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_FREEZE_REGFREEZE, self).__init__(register,
            'REGFREEZE', 'PCNT0.FREEZE.REGFREEZE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_SYNCBUSY_CTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_SYNCBUSY_CTRL, self).__init__(register,
            'CTRL', 'PCNT0.SYNCBUSY.CTRL', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_SYNCBUSY_CMD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_SYNCBUSY_CMD, self).__init__(register,
            'CMD', 'PCNT0.SYNCBUSY.CMD', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_SYNCBUSY_TOPB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_SYNCBUSY_TOPB, self).__init__(register,
            'TOPB', 'PCNT0.SYNCBUSY.TOPB', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_SYNCBUSY_OVSCFG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_SYNCBUSY_OVSCFG, self).__init__(register,
            'OVSCFG', 'PCNT0.SYNCBUSY.OVSCFG', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_AUXCNT_AUXCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_AUXCNT_AUXCNT, self).__init__(register,
            'AUXCNT', 'PCNT0.AUXCNT.AUXCNT', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_INPUT_S0PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_INPUT_S0PRSSEL, self).__init__(register,
            'S0PRSSEL', 'PCNT0.INPUT.S0PRSSEL', 'read-write',
            "",
            0, 4,
            RM_Enum_PCNT0_INPUT_S0PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_INPUT_S0PRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_INPUT_S0PRSEN, self).__init__(register,
            'S0PRSEN', 'PCNT0.INPUT.S0PRSEN', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_INPUT_S1PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_INPUT_S1PRSSEL, self).__init__(register,
            'S1PRSSEL', 'PCNT0.INPUT.S1PRSSEL', 'read-write',
            "",
            6, 4,
            RM_Enum_PCNT0_INPUT_S1PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_INPUT_S1PRSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_INPUT_S1PRSEN, self).__init__(register,
            'S1PRSEN', 'PCNT0.INPUT.S1PRSEN', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_OVSCFG_FILTLEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_OVSCFG_FILTLEN, self).__init__(register,
            'FILTLEN', 'PCNT0.OVSCFG.FILTLEN', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_PCNT0_OVSCFG_FLUTTERRM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_PCNT0_OVSCFG_FLUTTERRM, self).__init__(register,
            'FLUTTERRM', 'PCNT0.OVSCFG.FLUTTERRM', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


