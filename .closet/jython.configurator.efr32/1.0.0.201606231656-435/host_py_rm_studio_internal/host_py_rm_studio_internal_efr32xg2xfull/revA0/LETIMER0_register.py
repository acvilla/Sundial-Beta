
from static import Base_RM_Register
from LETIMER0_field import *


class RM_Register_LETIMER0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_CTRL, self).__init__(rmio, label,
            0x40046000, 0x000,
            'CTRL', 'LETIMER0.CTRL', 'read-write',
            "",
            0x00000000, 0x000013FF)

        self.REPMODE = RM_Field_LETIMER0_CTRL_REPMODE(self)
        self.zz_fdict['REPMODE'] = self.REPMODE
        self.UFOA0 = RM_Field_LETIMER0_CTRL_UFOA0(self)
        self.zz_fdict['UFOA0'] = self.UFOA0
        self.UFOA1 = RM_Field_LETIMER0_CTRL_UFOA1(self)
        self.zz_fdict['UFOA1'] = self.UFOA1
        self.OPOL0 = RM_Field_LETIMER0_CTRL_OPOL0(self)
        self.zz_fdict['OPOL0'] = self.OPOL0
        self.OPOL1 = RM_Field_LETIMER0_CTRL_OPOL1(self)
        self.zz_fdict['OPOL1'] = self.OPOL1
        self.BUFTOP = RM_Field_LETIMER0_CTRL_BUFTOP(self)
        self.zz_fdict['BUFTOP'] = self.BUFTOP
        self.COMP0TOP = RM_Field_LETIMER0_CTRL_COMP0TOP(self)
        self.zz_fdict['COMP0TOP'] = self.COMP0TOP
        self.DEBUGRUN = RM_Field_LETIMER0_CTRL_DEBUGRUN(self)
        self.zz_fdict['DEBUGRUN'] = self.DEBUGRUN
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_CMD, self).__init__(rmio, label,
            0x40046000, 0x004,
            'CMD', 'LETIMER0.CMD', 'write-only',
            "",
            0x00000000, 0x0000001F)

        self.START = RM_Field_LETIMER0_CMD_START(self)
        self.zz_fdict['START'] = self.START
        self.STOP = RM_Field_LETIMER0_CMD_STOP(self)
        self.zz_fdict['STOP'] = self.STOP
        self.CLEAR = RM_Field_LETIMER0_CMD_CLEAR(self)
        self.zz_fdict['CLEAR'] = self.CLEAR
        self.CTO0 = RM_Field_LETIMER0_CMD_CTO0(self)
        self.zz_fdict['CTO0'] = self.CTO0
        self.CTO1 = RM_Field_LETIMER0_CMD_CTO1(self)
        self.zz_fdict['CTO1'] = self.CTO1
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_STATUS, self).__init__(rmio, label,
            0x40046000, 0x008,
            'STATUS', 'LETIMER0.STATUS', 'read-only',
            "",
            0x00000000, 0x00000001)

        self.RUNNING = RM_Field_LETIMER0_STATUS_RUNNING(self)
        self.zz_fdict['RUNNING'] = self.RUNNING
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_CNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_CNT, self).__init__(rmio, label,
            0x40046000, 0x00C,
            'CNT', 'LETIMER0.CNT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.CNT = RM_Field_LETIMER0_CNT_CNT(self)
        self.zz_fdict['CNT'] = self.CNT
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_COMP0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_COMP0, self).__init__(rmio, label,
            0x40046000, 0x010,
            'COMP0', 'LETIMER0.COMP0', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.COMP0 = RM_Field_LETIMER0_COMP0_COMP0(self)
        self.zz_fdict['COMP0'] = self.COMP0
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_COMP1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_COMP1, self).__init__(rmio, label,
            0x40046000, 0x014,
            'COMP1', 'LETIMER0.COMP1', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.COMP1 = RM_Field_LETIMER0_COMP1_COMP1(self)
        self.zz_fdict['COMP1'] = self.COMP1
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_REP0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_REP0, self).__init__(rmio, label,
            0x40046000, 0x018,
            'REP0', 'LETIMER0.REP0', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.REP0 = RM_Field_LETIMER0_REP0_REP0(self)
        self.zz_fdict['REP0'] = self.REP0
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_REP1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_REP1, self).__init__(rmio, label,
            0x40046000, 0x01C,
            'REP1', 'LETIMER0.REP1', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.REP1 = RM_Field_LETIMER0_REP1_REP1(self)
        self.zz_fdict['REP1'] = self.REP1
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_IF, self).__init__(rmio, label,
            0x40046000, 0x020,
            'IF', 'LETIMER0.IF', 'read-only',
            "",
            0x00000000, 0x0000001F)

        self.COMP0 = RM_Field_LETIMER0_IF_COMP0(self)
        self.zz_fdict['COMP0'] = self.COMP0
        self.COMP1 = RM_Field_LETIMER0_IF_COMP1(self)
        self.zz_fdict['COMP1'] = self.COMP1
        self.UF = RM_Field_LETIMER0_IF_UF(self)
        self.zz_fdict['UF'] = self.UF
        self.REP0 = RM_Field_LETIMER0_IF_REP0(self)
        self.zz_fdict['REP0'] = self.REP0
        self.REP1 = RM_Field_LETIMER0_IF_REP1(self)
        self.zz_fdict['REP1'] = self.REP1
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_IFS, self).__init__(rmio, label,
            0x40046000, 0x024,
            'IFS', 'LETIMER0.IFS', 'write-only',
            "",
            0x00000000, 0x0000001F)

        self.COMP0 = RM_Field_LETIMER0_IFS_COMP0(self)
        self.zz_fdict['COMP0'] = self.COMP0
        self.COMP1 = RM_Field_LETIMER0_IFS_COMP1(self)
        self.zz_fdict['COMP1'] = self.COMP1
        self.UF = RM_Field_LETIMER0_IFS_UF(self)
        self.zz_fdict['UF'] = self.UF
        self.REP0 = RM_Field_LETIMER0_IFS_REP0(self)
        self.zz_fdict['REP0'] = self.REP0
        self.REP1 = RM_Field_LETIMER0_IFS_REP1(self)
        self.zz_fdict['REP1'] = self.REP1
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_IFC, self).__init__(rmio, label,
            0x40046000, 0x028,
            'IFC', 'LETIMER0.IFC', 'write-only',
            "",
            0x00000000, 0x0000001F)

        self.COMP0 = RM_Field_LETIMER0_IFC_COMP0(self)
        self.zz_fdict['COMP0'] = self.COMP0
        self.COMP1 = RM_Field_LETIMER0_IFC_COMP1(self)
        self.zz_fdict['COMP1'] = self.COMP1
        self.UF = RM_Field_LETIMER0_IFC_UF(self)
        self.zz_fdict['UF'] = self.UF
        self.REP0 = RM_Field_LETIMER0_IFC_REP0(self)
        self.zz_fdict['REP0'] = self.REP0
        self.REP1 = RM_Field_LETIMER0_IFC_REP1(self)
        self.zz_fdict['REP1'] = self.REP1
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_IEN, self).__init__(rmio, label,
            0x40046000, 0x02C,
            'IEN', 'LETIMER0.IEN', 'read-write',
            "",
            0x00000000, 0x0000001F)

        self.COMP0 = RM_Field_LETIMER0_IEN_COMP0(self)
        self.zz_fdict['COMP0'] = self.COMP0
        self.COMP1 = RM_Field_LETIMER0_IEN_COMP1(self)
        self.zz_fdict['COMP1'] = self.COMP1
        self.UF = RM_Field_LETIMER0_IEN_UF(self)
        self.zz_fdict['UF'] = self.UF
        self.REP0 = RM_Field_LETIMER0_IEN_REP0(self)
        self.zz_fdict['REP0'] = self.REP0
        self.REP1 = RM_Field_LETIMER0_IEN_REP1(self)
        self.zz_fdict['REP1'] = self.REP1
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_SYNCBUSY(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_SYNCBUSY, self).__init__(rmio, label,
            0x40046000, 0x034,
            'SYNCBUSY', 'LETIMER0.SYNCBUSY', 'read-only',
            "",
            0x00000000, 0x00000002)

        self.CMD = RM_Field_LETIMER0_SYNCBUSY_CMD(self)
        self.zz_fdict['CMD'] = self.CMD
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_ROUTEPEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_ROUTEPEN, self).__init__(rmio, label,
            0x40046000, 0x040,
            'ROUTEPEN', 'LETIMER0.ROUTEPEN', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.OUT0PEN = RM_Field_LETIMER0_ROUTEPEN_OUT0PEN(self)
        self.zz_fdict['OUT0PEN'] = self.OUT0PEN
        self.OUT1PEN = RM_Field_LETIMER0_ROUTEPEN_OUT1PEN(self)
        self.zz_fdict['OUT1PEN'] = self.OUT1PEN
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_ROUTELOC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_ROUTELOC0, self).__init__(rmio, label,
            0x40046000, 0x044,
            'ROUTELOC0', 'LETIMER0.ROUTELOC0', 'read-write',
            "",
            0x00000000, 0x00003F3F)

        self.OUT0LOC = RM_Field_LETIMER0_ROUTELOC0_OUT0LOC(self)
        self.zz_fdict['OUT0LOC'] = self.OUT0LOC
        self.OUT1LOC = RM_Field_LETIMER0_ROUTELOC0_OUT1LOC(self)
        self.zz_fdict['OUT1LOC'] = self.OUT1LOC
        self.__dict__['zz_frozen'] = True


class RM_Register_LETIMER0_PRSSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LETIMER0_PRSSEL, self).__init__(rmio, label,
            0x40046000, 0x050,
            'PRSSEL', 'LETIMER0.PRSSEL', 'read-write',
            "",
            0x00000000, 0x0CCCF3CF)

        self.PRSSTARTSEL = RM_Field_LETIMER0_PRSSEL_PRSSTARTSEL(self)
        self.zz_fdict['PRSSTARTSEL'] = self.PRSSTARTSEL
        self.PRSSTOPSEL = RM_Field_LETIMER0_PRSSEL_PRSSTOPSEL(self)
        self.zz_fdict['PRSSTOPSEL'] = self.PRSSTOPSEL
        self.PRSCLEARSEL = RM_Field_LETIMER0_PRSSEL_PRSCLEARSEL(self)
        self.zz_fdict['PRSCLEARSEL'] = self.PRSCLEARSEL
        self.PRSSTARTMODE = RM_Field_LETIMER0_PRSSEL_PRSSTARTMODE(self)
        self.zz_fdict['PRSSTARTMODE'] = self.PRSSTARTMODE
        self.PRSSTOPMODE = RM_Field_LETIMER0_PRSSEL_PRSSTOPMODE(self)
        self.zz_fdict['PRSSTOPMODE'] = self.PRSSTOPMODE
        self.PRSCLEARMODE = RM_Field_LETIMER0_PRSSEL_PRSCLEARMODE(self)
        self.zz_fdict['PRSCLEARMODE'] = self.PRSCLEARMODE
        self.__dict__['zz_frozen'] = True


