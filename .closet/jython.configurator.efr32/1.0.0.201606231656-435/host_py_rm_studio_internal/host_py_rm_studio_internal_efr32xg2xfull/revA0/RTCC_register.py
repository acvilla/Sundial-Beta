
from static import Base_RM_Register
from RTCC_field import *


class RM_Register_RTCC_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CTRL, self).__init__(rmio, label,
            0x40042000, 0x000,
            'CTRL', 'RTCC.CTRL', 'read-write',
            "",
            0x00000000, 0x00039F35)

        self.ENABLE = RM_Field_RTCC_CTRL_ENABLE(self)
        self.zz_fdict['ENABLE'] = self.ENABLE
        self.DEBUGRUN = RM_Field_RTCC_CTRL_DEBUGRUN(self)
        self.zz_fdict['DEBUGRUN'] = self.DEBUGRUN
        self.PRECCV0TOP = RM_Field_RTCC_CTRL_PRECCV0TOP(self)
        self.zz_fdict['PRECCV0TOP'] = self.PRECCV0TOP
        self.CCV1TOP = RM_Field_RTCC_CTRL_CCV1TOP(self)
        self.zz_fdict['CCV1TOP'] = self.CCV1TOP
        self.CNTPRESC = RM_Field_RTCC_CTRL_CNTPRESC(self)
        self.zz_fdict['CNTPRESC'] = self.CNTPRESC
        self.CNTTICK = RM_Field_RTCC_CTRL_CNTTICK(self)
        self.zz_fdict['CNTTICK'] = self.CNTTICK
        self.OSCFDETEN = RM_Field_RTCC_CTRL_OSCFDETEN(self)
        self.zz_fdict['OSCFDETEN'] = self.OSCFDETEN
        self.CNTMODE = RM_Field_RTCC_CTRL_CNTMODE(self)
        self.zz_fdict['CNTMODE'] = self.CNTMODE
        self.LYEARCORRDIS = RM_Field_RTCC_CTRL_LYEARCORRDIS(self)
        self.zz_fdict['LYEARCORRDIS'] = self.LYEARCORRDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_PRECNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_PRECNT, self).__init__(rmio, label,
            0x40042000, 0x004,
            'PRECNT', 'RTCC.PRECNT', 'read-write',
            "",
            0x00000000, 0x00007FFF)

        self.PRECNT = RM_Field_RTCC_PRECNT_PRECNT(self)
        self.zz_fdict['PRECNT'] = self.PRECNT
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_CNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CNT, self).__init__(rmio, label,
            0x40042000, 0x008,
            'CNT', 'RTCC.CNT', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.CNT = RM_Field_RTCC_CNT_CNT(self)
        self.zz_fdict['CNT'] = self.CNT
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_COMBCNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_COMBCNT, self).__init__(rmio, label,
            0x40042000, 0x00C,
            'COMBCNT', 'RTCC.COMBCNT', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.PRECNT = RM_Field_RTCC_COMBCNT_PRECNT(self)
        self.zz_fdict['PRECNT'] = self.PRECNT
        self.CNTLSB = RM_Field_RTCC_COMBCNT_CNTLSB(self)
        self.zz_fdict['CNTLSB'] = self.CNTLSB
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_TIME(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_TIME, self).__init__(rmio, label,
            0x40042000, 0x010,
            'TIME', 'RTCC.TIME', 'read-write',
            "",
            0x00000000, 0x003F7F7F)

        self.SECU = RM_Field_RTCC_TIME_SECU(self)
        self.zz_fdict['SECU'] = self.SECU
        self.SECT = RM_Field_RTCC_TIME_SECT(self)
        self.zz_fdict['SECT'] = self.SECT
        self.MINU = RM_Field_RTCC_TIME_MINU(self)
        self.zz_fdict['MINU'] = self.MINU
        self.MINT = RM_Field_RTCC_TIME_MINT(self)
        self.zz_fdict['MINT'] = self.MINT
        self.HOURU = RM_Field_RTCC_TIME_HOURU(self)
        self.zz_fdict['HOURU'] = self.HOURU
        self.HOURT = RM_Field_RTCC_TIME_HOURT(self)
        self.zz_fdict['HOURT'] = self.HOURT
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_DATE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_DATE, self).__init__(rmio, label,
            0x40042000, 0x014,
            'DATE', 'RTCC.DATE', 'read-write',
            "",
            0x00000000, 0x07FF1F3F)

        self.DAYOMU = RM_Field_RTCC_DATE_DAYOMU(self)
        self.zz_fdict['DAYOMU'] = self.DAYOMU
        self.DAYOMT = RM_Field_RTCC_DATE_DAYOMT(self)
        self.zz_fdict['DAYOMT'] = self.DAYOMT
        self.MONTHU = RM_Field_RTCC_DATE_MONTHU(self)
        self.zz_fdict['MONTHU'] = self.MONTHU
        self.MONTHT = RM_Field_RTCC_DATE_MONTHT(self)
        self.zz_fdict['MONTHT'] = self.MONTHT
        self.YEARU = RM_Field_RTCC_DATE_YEARU(self)
        self.zz_fdict['YEARU'] = self.YEARU
        self.YEART = RM_Field_RTCC_DATE_YEART(self)
        self.zz_fdict['YEART'] = self.YEART
        self.DAYOW = RM_Field_RTCC_DATE_DAYOW(self)
        self.zz_fdict['DAYOW'] = self.DAYOW
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_IF, self).__init__(rmio, label,
            0x40042000, 0x018,
            'IF', 'RTCC.IF', 'read-only',
            "",
            0x00000000, 0x000007FF)

        self.OF = RM_Field_RTCC_IF_OF(self)
        self.zz_fdict['OF'] = self.OF
        self.CC0 = RM_Field_RTCC_IF_CC0(self)
        self.zz_fdict['CC0'] = self.CC0
        self.CC1 = RM_Field_RTCC_IF_CC1(self)
        self.zz_fdict['CC1'] = self.CC1
        self.CC2 = RM_Field_RTCC_IF_CC2(self)
        self.zz_fdict['CC2'] = self.CC2
        self.OSCFAIL = RM_Field_RTCC_IF_OSCFAIL(self)
        self.zz_fdict['OSCFAIL'] = self.OSCFAIL
        self.CNTTICK = RM_Field_RTCC_IF_CNTTICK(self)
        self.zz_fdict['CNTTICK'] = self.CNTTICK
        self.MINTICK = RM_Field_RTCC_IF_MINTICK(self)
        self.zz_fdict['MINTICK'] = self.MINTICK
        self.HOURTICK = RM_Field_RTCC_IF_HOURTICK(self)
        self.zz_fdict['HOURTICK'] = self.HOURTICK
        self.DAYTICK = RM_Field_RTCC_IF_DAYTICK(self)
        self.zz_fdict['DAYTICK'] = self.DAYTICK
        self.DAYOWOF = RM_Field_RTCC_IF_DAYOWOF(self)
        self.zz_fdict['DAYOWOF'] = self.DAYOWOF
        self.MONTHTICK = RM_Field_RTCC_IF_MONTHTICK(self)
        self.zz_fdict['MONTHTICK'] = self.MONTHTICK
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_IFS, self).__init__(rmio, label,
            0x40042000, 0x01C,
            'IFS', 'RTCC.IFS', 'write-only',
            "",
            0x00000000, 0x000007FF)

        self.OF = RM_Field_RTCC_IFS_OF(self)
        self.zz_fdict['OF'] = self.OF
        self.CC0 = RM_Field_RTCC_IFS_CC0(self)
        self.zz_fdict['CC0'] = self.CC0
        self.CC1 = RM_Field_RTCC_IFS_CC1(self)
        self.zz_fdict['CC1'] = self.CC1
        self.CC2 = RM_Field_RTCC_IFS_CC2(self)
        self.zz_fdict['CC2'] = self.CC2
        self.OSCFAIL = RM_Field_RTCC_IFS_OSCFAIL(self)
        self.zz_fdict['OSCFAIL'] = self.OSCFAIL
        self.CNTTICK = RM_Field_RTCC_IFS_CNTTICK(self)
        self.zz_fdict['CNTTICK'] = self.CNTTICK
        self.MINTICK = RM_Field_RTCC_IFS_MINTICK(self)
        self.zz_fdict['MINTICK'] = self.MINTICK
        self.HOURTICK = RM_Field_RTCC_IFS_HOURTICK(self)
        self.zz_fdict['HOURTICK'] = self.HOURTICK
        self.DAYTICK = RM_Field_RTCC_IFS_DAYTICK(self)
        self.zz_fdict['DAYTICK'] = self.DAYTICK
        self.DAYOWOF = RM_Field_RTCC_IFS_DAYOWOF(self)
        self.zz_fdict['DAYOWOF'] = self.DAYOWOF
        self.MONTHTICK = RM_Field_RTCC_IFS_MONTHTICK(self)
        self.zz_fdict['MONTHTICK'] = self.MONTHTICK
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_IFC, self).__init__(rmio, label,
            0x40042000, 0x020,
            'IFC', 'RTCC.IFC', 'write-only',
            "",
            0x00000000, 0x000007FF)

        self.OF = RM_Field_RTCC_IFC_OF(self)
        self.zz_fdict['OF'] = self.OF
        self.CC0 = RM_Field_RTCC_IFC_CC0(self)
        self.zz_fdict['CC0'] = self.CC0
        self.CC1 = RM_Field_RTCC_IFC_CC1(self)
        self.zz_fdict['CC1'] = self.CC1
        self.CC2 = RM_Field_RTCC_IFC_CC2(self)
        self.zz_fdict['CC2'] = self.CC2
        self.OSCFAIL = RM_Field_RTCC_IFC_OSCFAIL(self)
        self.zz_fdict['OSCFAIL'] = self.OSCFAIL
        self.CNTTICK = RM_Field_RTCC_IFC_CNTTICK(self)
        self.zz_fdict['CNTTICK'] = self.CNTTICK
        self.MINTICK = RM_Field_RTCC_IFC_MINTICK(self)
        self.zz_fdict['MINTICK'] = self.MINTICK
        self.HOURTICK = RM_Field_RTCC_IFC_HOURTICK(self)
        self.zz_fdict['HOURTICK'] = self.HOURTICK
        self.DAYTICK = RM_Field_RTCC_IFC_DAYTICK(self)
        self.zz_fdict['DAYTICK'] = self.DAYTICK
        self.DAYOWOF = RM_Field_RTCC_IFC_DAYOWOF(self)
        self.zz_fdict['DAYOWOF'] = self.DAYOWOF
        self.MONTHTICK = RM_Field_RTCC_IFC_MONTHTICK(self)
        self.zz_fdict['MONTHTICK'] = self.MONTHTICK
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_IEN, self).__init__(rmio, label,
            0x40042000, 0x024,
            'IEN', 'RTCC.IEN', 'read-write',
            "",
            0x00000000, 0x000007FF)

        self.OF = RM_Field_RTCC_IEN_OF(self)
        self.zz_fdict['OF'] = self.OF
        self.CC0 = RM_Field_RTCC_IEN_CC0(self)
        self.zz_fdict['CC0'] = self.CC0
        self.CC1 = RM_Field_RTCC_IEN_CC1(self)
        self.zz_fdict['CC1'] = self.CC1
        self.CC2 = RM_Field_RTCC_IEN_CC2(self)
        self.zz_fdict['CC2'] = self.CC2
        self.OSCFAIL = RM_Field_RTCC_IEN_OSCFAIL(self)
        self.zz_fdict['OSCFAIL'] = self.OSCFAIL
        self.CNTTICK = RM_Field_RTCC_IEN_CNTTICK(self)
        self.zz_fdict['CNTTICK'] = self.CNTTICK
        self.MINTICK = RM_Field_RTCC_IEN_MINTICK(self)
        self.zz_fdict['MINTICK'] = self.MINTICK
        self.HOURTICK = RM_Field_RTCC_IEN_HOURTICK(self)
        self.zz_fdict['HOURTICK'] = self.HOURTICK
        self.DAYTICK = RM_Field_RTCC_IEN_DAYTICK(self)
        self.zz_fdict['DAYTICK'] = self.DAYTICK
        self.DAYOWOF = RM_Field_RTCC_IEN_DAYOWOF(self)
        self.zz_fdict['DAYOWOF'] = self.DAYOWOF
        self.MONTHTICK = RM_Field_RTCC_IEN_MONTHTICK(self)
        self.zz_fdict['MONTHTICK'] = self.MONTHTICK
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CMD, self).__init__(rmio, label,
            0x40042000, 0x02C,
            'CMD', 'RTCC.CMD', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.CLRSTATUS = RM_Field_RTCC_CMD_CLRSTATUS(self)
        self.zz_fdict['CLRSTATUS'] = self.CLRSTATUS
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_SYNCBUSY(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_SYNCBUSY, self).__init__(rmio, label,
            0x40042000, 0x030,
            'SYNCBUSY', 'RTCC.SYNCBUSY', 'read-only',
            "",
            0x00000000, 0x00000020)

        self.CMD = RM_Field_RTCC_SYNCBUSY_CMD(self)
        self.zz_fdict['CMD'] = self.CMD
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_POWERDOWN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_POWERDOWN, self).__init__(rmio, label,
            0x40042000, 0x034,
            'POWERDOWN', 'RTCC.POWERDOWN', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.RAM = RM_Field_RTCC_POWERDOWN_RAM(self)
        self.zz_fdict['RAM'] = self.RAM
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_LOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_LOCK, self).__init__(rmio, label,
            0x40042000, 0x038,
            'LOCK', 'RTCC.LOCK', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.LOCKKEY = RM_Field_RTCC_LOCK_LOCKKEY(self)
        self.zz_fdict['LOCKKEY'] = self.LOCKKEY
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_EM4WUEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_EM4WUEN, self).__init__(rmio, label,
            0x40042000, 0x03C,
            'EM4WUEN', 'RTCC.EM4WUEN', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.EM4WU = RM_Field_RTCC_EM4WUEN_EM4WU(self)
        self.zz_fdict['EM4WU'] = self.EM4WU
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_CC0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CC0_CTRL, self).__init__(rmio, label,
            0x40042000, 0x040,
            'CC0_CTRL', 'RTCC.CC0_CTRL', 'read-write',
            "",
            0x00000000, 0x0003FBFF)

        self.MODE = RM_Field_RTCC_CC0_CTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.CMOA = RM_Field_RTCC_CC0_CTRL_CMOA(self)
        self.zz_fdict['CMOA'] = self.CMOA
        self.ICEDGE = RM_Field_RTCC_CC0_CTRL_ICEDGE(self)
        self.zz_fdict['ICEDGE'] = self.ICEDGE
        self.PRSSEL = RM_Field_RTCC_CC0_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.COMPBASE = RM_Field_RTCC_CC0_CTRL_COMPBASE(self)
        self.zz_fdict['COMPBASE'] = self.COMPBASE
        self.COMPMASK = RM_Field_RTCC_CC0_CTRL_COMPMASK(self)
        self.zz_fdict['COMPMASK'] = self.COMPMASK
        self.DAYCC = RM_Field_RTCC_CC0_CTRL_DAYCC(self)
        self.zz_fdict['DAYCC'] = self.DAYCC
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_CC0_CCV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CC0_CCV, self).__init__(rmio, label,
            0x40042000, 0x044,
            'CC0_CCV', 'RTCC.CC0_CCV', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.CCV = RM_Field_RTCC_CC0_CCV_CCV(self)
        self.zz_fdict['CCV'] = self.CCV
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_CC0_TIME(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CC0_TIME, self).__init__(rmio, label,
            0x40042000, 0x048,
            'CC0_TIME', 'RTCC.CC0_TIME', 'read-write',
            "",
            0x00000000, 0x003F7F7F)

        self.SECU = RM_Field_RTCC_CC0_TIME_SECU(self)
        self.zz_fdict['SECU'] = self.SECU
        self.SECT = RM_Field_RTCC_CC0_TIME_SECT(self)
        self.zz_fdict['SECT'] = self.SECT
        self.MINU = RM_Field_RTCC_CC0_TIME_MINU(self)
        self.zz_fdict['MINU'] = self.MINU
        self.MINT = RM_Field_RTCC_CC0_TIME_MINT(self)
        self.zz_fdict['MINT'] = self.MINT
        self.HOURU = RM_Field_RTCC_CC0_TIME_HOURU(self)
        self.zz_fdict['HOURU'] = self.HOURU
        self.HOURT = RM_Field_RTCC_CC0_TIME_HOURT(self)
        self.zz_fdict['HOURT'] = self.HOURT
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_CC0_DATE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CC0_DATE, self).__init__(rmio, label,
            0x40042000, 0x04C,
            'CC0_DATE', 'RTCC.CC0_DATE', 'read-write',
            "",
            0x00000000, 0x00001F3F)

        self.DAYU = RM_Field_RTCC_CC0_DATE_DAYU(self)
        self.zz_fdict['DAYU'] = self.DAYU
        self.DAYT = RM_Field_RTCC_CC0_DATE_DAYT(self)
        self.zz_fdict['DAYT'] = self.DAYT
        self.MONTHU = RM_Field_RTCC_CC0_DATE_MONTHU(self)
        self.zz_fdict['MONTHU'] = self.MONTHU
        self.MONTHT = RM_Field_RTCC_CC0_DATE_MONTHT(self)
        self.zz_fdict['MONTHT'] = self.MONTHT
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_CC1_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CC1_CTRL, self).__init__(rmio, label,
            0x40042000, 0x050,
            'CC1_CTRL', 'RTCC.CC1_CTRL', 'read-write',
            "",
            0x00000000, 0x0003FBFF)

        self.MODE = RM_Field_RTCC_CC1_CTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.CMOA = RM_Field_RTCC_CC1_CTRL_CMOA(self)
        self.zz_fdict['CMOA'] = self.CMOA
        self.ICEDGE = RM_Field_RTCC_CC1_CTRL_ICEDGE(self)
        self.zz_fdict['ICEDGE'] = self.ICEDGE
        self.PRSSEL = RM_Field_RTCC_CC1_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.COMPBASE = RM_Field_RTCC_CC1_CTRL_COMPBASE(self)
        self.zz_fdict['COMPBASE'] = self.COMPBASE
        self.COMPMASK = RM_Field_RTCC_CC1_CTRL_COMPMASK(self)
        self.zz_fdict['COMPMASK'] = self.COMPMASK
        self.DAYCC = RM_Field_RTCC_CC1_CTRL_DAYCC(self)
        self.zz_fdict['DAYCC'] = self.DAYCC
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_CC1_CCV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CC1_CCV, self).__init__(rmio, label,
            0x40042000, 0x054,
            'CC1_CCV', 'RTCC.CC1_CCV', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.CCV = RM_Field_RTCC_CC1_CCV_CCV(self)
        self.zz_fdict['CCV'] = self.CCV
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_CC1_TIME(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CC1_TIME, self).__init__(rmio, label,
            0x40042000, 0x058,
            'CC1_TIME', 'RTCC.CC1_TIME', 'read-write',
            "",
            0x00000000, 0x003F7F7F)

        self.SECU = RM_Field_RTCC_CC1_TIME_SECU(self)
        self.zz_fdict['SECU'] = self.SECU
        self.SECT = RM_Field_RTCC_CC1_TIME_SECT(self)
        self.zz_fdict['SECT'] = self.SECT
        self.MINU = RM_Field_RTCC_CC1_TIME_MINU(self)
        self.zz_fdict['MINU'] = self.MINU
        self.MINT = RM_Field_RTCC_CC1_TIME_MINT(self)
        self.zz_fdict['MINT'] = self.MINT
        self.HOURU = RM_Field_RTCC_CC1_TIME_HOURU(self)
        self.zz_fdict['HOURU'] = self.HOURU
        self.HOURT = RM_Field_RTCC_CC1_TIME_HOURT(self)
        self.zz_fdict['HOURT'] = self.HOURT
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_CC1_DATE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CC1_DATE, self).__init__(rmio, label,
            0x40042000, 0x05C,
            'CC1_DATE', 'RTCC.CC1_DATE', 'read-write',
            "",
            0x00000000, 0x00001F3F)

        self.DAYU = RM_Field_RTCC_CC1_DATE_DAYU(self)
        self.zz_fdict['DAYU'] = self.DAYU
        self.DAYT = RM_Field_RTCC_CC1_DATE_DAYT(self)
        self.zz_fdict['DAYT'] = self.DAYT
        self.MONTHU = RM_Field_RTCC_CC1_DATE_MONTHU(self)
        self.zz_fdict['MONTHU'] = self.MONTHU
        self.MONTHT = RM_Field_RTCC_CC1_DATE_MONTHT(self)
        self.zz_fdict['MONTHT'] = self.MONTHT
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_CC2_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CC2_CTRL, self).__init__(rmio, label,
            0x40042000, 0x060,
            'CC2_CTRL', 'RTCC.CC2_CTRL', 'read-write',
            "",
            0x00000000, 0x0003FBFF)

        self.MODE = RM_Field_RTCC_CC2_CTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.CMOA = RM_Field_RTCC_CC2_CTRL_CMOA(self)
        self.zz_fdict['CMOA'] = self.CMOA
        self.ICEDGE = RM_Field_RTCC_CC2_CTRL_ICEDGE(self)
        self.zz_fdict['ICEDGE'] = self.ICEDGE
        self.PRSSEL = RM_Field_RTCC_CC2_CTRL_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.COMPBASE = RM_Field_RTCC_CC2_CTRL_COMPBASE(self)
        self.zz_fdict['COMPBASE'] = self.COMPBASE
        self.COMPMASK = RM_Field_RTCC_CC2_CTRL_COMPMASK(self)
        self.zz_fdict['COMPMASK'] = self.COMPMASK
        self.DAYCC = RM_Field_RTCC_CC2_CTRL_DAYCC(self)
        self.zz_fdict['DAYCC'] = self.DAYCC
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_CC2_CCV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CC2_CCV, self).__init__(rmio, label,
            0x40042000, 0x064,
            'CC2_CCV', 'RTCC.CC2_CCV', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.CCV = RM_Field_RTCC_CC2_CCV_CCV(self)
        self.zz_fdict['CCV'] = self.CCV
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_CC2_TIME(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CC2_TIME, self).__init__(rmio, label,
            0x40042000, 0x068,
            'CC2_TIME', 'RTCC.CC2_TIME', 'read-write',
            "",
            0x00000000, 0x003F7F7F)

        self.SECU = RM_Field_RTCC_CC2_TIME_SECU(self)
        self.zz_fdict['SECU'] = self.SECU
        self.SECT = RM_Field_RTCC_CC2_TIME_SECT(self)
        self.zz_fdict['SECT'] = self.SECT
        self.MINU = RM_Field_RTCC_CC2_TIME_MINU(self)
        self.zz_fdict['MINU'] = self.MINU
        self.MINT = RM_Field_RTCC_CC2_TIME_MINT(self)
        self.zz_fdict['MINT'] = self.MINT
        self.HOURU = RM_Field_RTCC_CC2_TIME_HOURU(self)
        self.zz_fdict['HOURU'] = self.HOURU
        self.HOURT = RM_Field_RTCC_CC2_TIME_HOURT(self)
        self.zz_fdict['HOURT'] = self.HOURT
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_CC2_DATE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_CC2_DATE, self).__init__(rmio, label,
            0x40042000, 0x06C,
            'CC2_DATE', 'RTCC.CC2_DATE', 'read-write',
            "",
            0x00000000, 0x00001F3F)

        self.DAYU = RM_Field_RTCC_CC2_DATE_DAYU(self)
        self.zz_fdict['DAYU'] = self.DAYU
        self.DAYT = RM_Field_RTCC_CC2_DATE_DAYT(self)
        self.zz_fdict['DAYT'] = self.DAYT
        self.MONTHU = RM_Field_RTCC_CC2_DATE_MONTHU(self)
        self.zz_fdict['MONTHU'] = self.MONTHU
        self.MONTHT = RM_Field_RTCC_CC2_DATE_MONTHT(self)
        self.zz_fdict['MONTHT'] = self.MONTHT
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET0_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET0_REG, self).__init__(rmio, label,
            0x40042000, 0x104,
            'RET0_REG', 'RTCC.RET0_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET0_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET1_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET1_REG, self).__init__(rmio, label,
            0x40042000, 0x108,
            'RET1_REG', 'RTCC.RET1_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET1_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET2_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET2_REG, self).__init__(rmio, label,
            0x40042000, 0x10C,
            'RET2_REG', 'RTCC.RET2_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET2_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET3_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET3_REG, self).__init__(rmio, label,
            0x40042000, 0x110,
            'RET3_REG', 'RTCC.RET3_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET3_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET4_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET4_REG, self).__init__(rmio, label,
            0x40042000, 0x114,
            'RET4_REG', 'RTCC.RET4_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET4_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET5_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET5_REG, self).__init__(rmio, label,
            0x40042000, 0x118,
            'RET5_REG', 'RTCC.RET5_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET5_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET6_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET6_REG, self).__init__(rmio, label,
            0x40042000, 0x11C,
            'RET6_REG', 'RTCC.RET6_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET6_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET7_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET7_REG, self).__init__(rmio, label,
            0x40042000, 0x120,
            'RET7_REG', 'RTCC.RET7_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET7_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET8_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET8_REG, self).__init__(rmio, label,
            0x40042000, 0x124,
            'RET8_REG', 'RTCC.RET8_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET8_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET9_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET9_REG, self).__init__(rmio, label,
            0x40042000, 0x128,
            'RET9_REG', 'RTCC.RET9_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET9_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET10_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET10_REG, self).__init__(rmio, label,
            0x40042000, 0x12C,
            'RET10_REG', 'RTCC.RET10_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET10_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET11_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET11_REG, self).__init__(rmio, label,
            0x40042000, 0x130,
            'RET11_REG', 'RTCC.RET11_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET11_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET12_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET12_REG, self).__init__(rmio, label,
            0x40042000, 0x134,
            'RET12_REG', 'RTCC.RET12_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET12_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET13_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET13_REG, self).__init__(rmio, label,
            0x40042000, 0x138,
            'RET13_REG', 'RTCC.RET13_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET13_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET14_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET14_REG, self).__init__(rmio, label,
            0x40042000, 0x13C,
            'RET14_REG', 'RTCC.RET14_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET14_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET15_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET15_REG, self).__init__(rmio, label,
            0x40042000, 0x140,
            'RET15_REG', 'RTCC.RET15_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET15_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET16_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET16_REG, self).__init__(rmio, label,
            0x40042000, 0x144,
            'RET16_REG', 'RTCC.RET16_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET16_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET17_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET17_REG, self).__init__(rmio, label,
            0x40042000, 0x148,
            'RET17_REG', 'RTCC.RET17_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET17_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET18_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET18_REG, self).__init__(rmio, label,
            0x40042000, 0x14C,
            'RET18_REG', 'RTCC.RET18_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET18_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET19_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET19_REG, self).__init__(rmio, label,
            0x40042000, 0x150,
            'RET19_REG', 'RTCC.RET19_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET19_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET20_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET20_REG, self).__init__(rmio, label,
            0x40042000, 0x154,
            'RET20_REG', 'RTCC.RET20_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET20_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET21_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET21_REG, self).__init__(rmio, label,
            0x40042000, 0x158,
            'RET21_REG', 'RTCC.RET21_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET21_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET22_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET22_REG, self).__init__(rmio, label,
            0x40042000, 0x15C,
            'RET22_REG', 'RTCC.RET22_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET22_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET23_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET23_REG, self).__init__(rmio, label,
            0x40042000, 0x160,
            'RET23_REG', 'RTCC.RET23_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET23_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET24_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET24_REG, self).__init__(rmio, label,
            0x40042000, 0x164,
            'RET24_REG', 'RTCC.RET24_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET24_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET25_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET25_REG, self).__init__(rmio, label,
            0x40042000, 0x168,
            'RET25_REG', 'RTCC.RET25_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET25_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET26_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET26_REG, self).__init__(rmio, label,
            0x40042000, 0x16C,
            'RET26_REG', 'RTCC.RET26_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET26_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET27_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET27_REG, self).__init__(rmio, label,
            0x40042000, 0x170,
            'RET27_REG', 'RTCC.RET27_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET27_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET28_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET28_REG, self).__init__(rmio, label,
            0x40042000, 0x174,
            'RET28_REG', 'RTCC.RET28_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET28_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET29_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET29_REG, self).__init__(rmio, label,
            0x40042000, 0x178,
            'RET29_REG', 'RTCC.RET29_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET29_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET30_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET30_REG, self).__init__(rmio, label,
            0x40042000, 0x17C,
            'RET30_REG', 'RTCC.RET30_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET30_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


class RM_Register_RTCC_RET31_REG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_RTCC_RET31_REG, self).__init__(rmio, label,
            0x40042000, 0x180,
            'RET31_REG', 'RTCC.RET31_REG', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.REG = RM_Field_RTCC_RET31_REG_REG(self)
        self.zz_fdict['REG'] = self.REG
        self.__dict__['zz_frozen'] = True


