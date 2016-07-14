
from static import Base_RM_Field
from LETIMER0_enum import *


class RM_Field_LETIMER0_CTRL_REPMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_CTRL_REPMODE, self).__init__(register,
            'REPMODE', 'LETIMER0.CTRL.REPMODE', 'read-write',
            "",
            0, 2,
            RM_Enum_LETIMER0_CTRL_REPMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_CTRL_UFOA0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_CTRL_UFOA0, self).__init__(register,
            'UFOA0', 'LETIMER0.CTRL.UFOA0', 'read-write',
            "",
            2, 2,
            RM_Enum_LETIMER0_CTRL_UFOA0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_CTRL_UFOA1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_CTRL_UFOA1, self).__init__(register,
            'UFOA1', 'LETIMER0.CTRL.UFOA1', 'read-write',
            "",
            4, 2,
            RM_Enum_LETIMER0_CTRL_UFOA1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_CTRL_OPOL0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_CTRL_OPOL0, self).__init__(register,
            'OPOL0', 'LETIMER0.CTRL.OPOL0', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_CTRL_OPOL1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_CTRL_OPOL1, self).__init__(register,
            'OPOL1', 'LETIMER0.CTRL.OPOL1', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_CTRL_BUFTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_CTRL_BUFTOP, self).__init__(register,
            'BUFTOP', 'LETIMER0.CTRL.BUFTOP', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_CTRL_COMP0TOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_CTRL_COMP0TOP, self).__init__(register,
            'COMP0TOP', 'LETIMER0.CTRL.COMP0TOP', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_CTRL_DEBUGRUN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_CTRL_DEBUGRUN, self).__init__(register,
            'DEBUGRUN', 'LETIMER0.CTRL.DEBUGRUN', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_CMD_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_CMD_START, self).__init__(register,
            'START', 'LETIMER0.CMD.START', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_CMD_STOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_CMD_STOP, self).__init__(register,
            'STOP', 'LETIMER0.CMD.STOP', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_CMD_CLEAR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_CMD_CLEAR, self).__init__(register,
            'CLEAR', 'LETIMER0.CMD.CLEAR', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_CMD_CTO0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_CMD_CTO0, self).__init__(register,
            'CTO0', 'LETIMER0.CMD.CTO0', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_CMD_CTO1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_CMD_CTO1, self).__init__(register,
            'CTO1', 'LETIMER0.CMD.CTO1', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_STATUS_RUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_STATUS_RUNNING, self).__init__(register,
            'RUNNING', 'LETIMER0.STATUS.RUNNING', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_CNT_CNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_CNT_CNT, self).__init__(register,
            'CNT', 'LETIMER0.CNT.CNT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_COMP0_COMP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_COMP0_COMP0, self).__init__(register,
            'COMP0', 'LETIMER0.COMP0.COMP0', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_COMP1_COMP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_COMP1_COMP1, self).__init__(register,
            'COMP1', 'LETIMER0.COMP1.COMP1', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_REP0_REP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_REP0_REP0, self).__init__(register,
            'REP0', 'LETIMER0.REP0.REP0', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_REP1_REP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_REP1_REP1, self).__init__(register,
            'REP1', 'LETIMER0.REP1.REP1', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IF_COMP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IF_COMP0, self).__init__(register,
            'COMP0', 'LETIMER0.IF.COMP0', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IF_COMP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IF_COMP1, self).__init__(register,
            'COMP1', 'LETIMER0.IF.COMP1', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IF_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IF_UF, self).__init__(register,
            'UF', 'LETIMER0.IF.UF', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IF_REP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IF_REP0, self).__init__(register,
            'REP0', 'LETIMER0.IF.REP0', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IF_REP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IF_REP1, self).__init__(register,
            'REP1', 'LETIMER0.IF.REP1', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IFS_COMP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IFS_COMP0, self).__init__(register,
            'COMP0', 'LETIMER0.IFS.COMP0', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IFS_COMP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IFS_COMP1, self).__init__(register,
            'COMP1', 'LETIMER0.IFS.COMP1', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IFS_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IFS_UF, self).__init__(register,
            'UF', 'LETIMER0.IFS.UF', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IFS_REP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IFS_REP0, self).__init__(register,
            'REP0', 'LETIMER0.IFS.REP0', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IFS_REP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IFS_REP1, self).__init__(register,
            'REP1', 'LETIMER0.IFS.REP1', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IFC_COMP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IFC_COMP0, self).__init__(register,
            'COMP0', 'LETIMER0.IFC.COMP0', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IFC_COMP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IFC_COMP1, self).__init__(register,
            'COMP1', 'LETIMER0.IFC.COMP1', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IFC_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IFC_UF, self).__init__(register,
            'UF', 'LETIMER0.IFC.UF', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IFC_REP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IFC_REP0, self).__init__(register,
            'REP0', 'LETIMER0.IFC.REP0', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IFC_REP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IFC_REP1, self).__init__(register,
            'REP1', 'LETIMER0.IFC.REP1', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IEN_COMP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IEN_COMP0, self).__init__(register,
            'COMP0', 'LETIMER0.IEN.COMP0', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IEN_COMP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IEN_COMP1, self).__init__(register,
            'COMP1', 'LETIMER0.IEN.COMP1', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IEN_UF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IEN_UF, self).__init__(register,
            'UF', 'LETIMER0.IEN.UF', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IEN_REP0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IEN_REP0, self).__init__(register,
            'REP0', 'LETIMER0.IEN.REP0', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_IEN_REP1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_IEN_REP1, self).__init__(register,
            'REP1', 'LETIMER0.IEN.REP1', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_SYNCBUSY_CMD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_SYNCBUSY_CMD, self).__init__(register,
            'CMD', 'LETIMER0.SYNCBUSY.CMD', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_ROUTEPEN_OUT0PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_ROUTEPEN_OUT0PEN, self).__init__(register,
            'OUT0PEN', 'LETIMER0.ROUTEPEN.OUT0PEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_ROUTEPEN_OUT1PEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_ROUTEPEN_OUT1PEN, self).__init__(register,
            'OUT1PEN', 'LETIMER0.ROUTEPEN.OUT1PEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_ROUTELOC0_OUT0LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_ROUTELOC0_OUT0LOC, self).__init__(register,
            'OUT0LOC', 'LETIMER0.ROUTELOC0.OUT0LOC', 'read-write',
            "",
            0, 6,
            RM_Enum_LETIMER0_ROUTELOC0_OUT0LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_ROUTELOC0_OUT1LOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_ROUTELOC0_OUT1LOC, self).__init__(register,
            'OUT1LOC', 'LETIMER0.ROUTELOC0.OUT1LOC', 'read-write',
            "",
            8, 6,
            RM_Enum_LETIMER0_ROUTELOC0_OUT1LOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_PRSSEL_PRSSTARTSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_PRSSEL_PRSSTARTSEL, self).__init__(register,
            'PRSSTARTSEL', 'LETIMER0.PRSSEL.PRSSTARTSEL', 'read-write',
            "",
            0, 4,
            RM_Enum_LETIMER0_PRSSEL_PRSSTARTSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_PRSSEL_PRSSTOPSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_PRSSEL_PRSSTOPSEL, self).__init__(register,
            'PRSSTOPSEL', 'LETIMER0.PRSSEL.PRSSTOPSEL', 'read-write',
            "",
            6, 4,
            RM_Enum_LETIMER0_PRSSEL_PRSSTOPSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_PRSSEL_PRSCLEARSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_PRSSEL_PRSCLEARSEL, self).__init__(register,
            'PRSCLEARSEL', 'LETIMER0.PRSSEL.PRSCLEARSEL', 'read-write',
            "",
            12, 4,
            RM_Enum_LETIMER0_PRSSEL_PRSCLEARSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_PRSSEL_PRSSTARTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_PRSSEL_PRSSTARTMODE, self).__init__(register,
            'PRSSTARTMODE', 'LETIMER0.PRSSEL.PRSSTARTMODE', 'read-write',
            "",
            18, 2,
            RM_Enum_LETIMER0_PRSSEL_PRSSTARTMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_PRSSEL_PRSSTOPMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_PRSSEL_PRSSTOPMODE, self).__init__(register,
            'PRSSTOPMODE', 'LETIMER0.PRSSEL.PRSSTOPMODE', 'read-write',
            "",
            22, 2,
            RM_Enum_LETIMER0_PRSSEL_PRSSTOPMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LETIMER0_PRSSEL_PRSCLEARMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LETIMER0_PRSSEL_PRSCLEARMODE, self).__init__(register,
            'PRSCLEARMODE', 'LETIMER0.PRSSEL.PRSCLEARMODE', 'read-write',
            "",
            26, 2,
            RM_Enum_LETIMER0_PRSSEL_PRSCLEARMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


