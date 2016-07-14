
from static import Base_RM_Field
from RTCC_enum import *


class RM_Field_RTCC_CTRL_ENABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CTRL_ENABLE, self).__init__(register,
            'ENABLE', 'RTCC.CTRL.ENABLE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CTRL_DEBUGRUN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CTRL_DEBUGRUN, self).__init__(register,
            'DEBUGRUN', 'RTCC.CTRL.DEBUGRUN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CTRL_PRECCV0TOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CTRL_PRECCV0TOP, self).__init__(register,
            'PRECCV0TOP', 'RTCC.CTRL.PRECCV0TOP', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CTRL_CCV1TOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CTRL_CCV1TOP, self).__init__(register,
            'CCV1TOP', 'RTCC.CTRL.CCV1TOP', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CTRL_CNTPRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CTRL_CNTPRESC, self).__init__(register,
            'CNTPRESC', 'RTCC.CTRL.CNTPRESC', 'read-write',
            "",
            8, 4,
            RM_Enum_RTCC_CTRL_CNTPRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CTRL_CNTTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CTRL_CNTTICK, self).__init__(register,
            'CNTTICK', 'RTCC.CTRL.CNTTICK', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CTRL_OSCFDETEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CTRL_OSCFDETEN, self).__init__(register,
            'OSCFDETEN', 'RTCC.CTRL.OSCFDETEN', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CTRL_CNTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CTRL_CNTMODE, self).__init__(register,
            'CNTMODE', 'RTCC.CTRL.CNTMODE', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CTRL_LYEARCORRDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CTRL_LYEARCORRDIS, self).__init__(register,
            'LYEARCORRDIS', 'RTCC.CTRL.LYEARCORRDIS', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_PRECNT_PRECNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_PRECNT_PRECNT, self).__init__(register,
            'PRECNT', 'RTCC.PRECNT.PRECNT', 'read-write',
            "",
            0, 15)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CNT_CNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CNT_CNT, self).__init__(register,
            'CNT', 'RTCC.CNT.CNT', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_COMBCNT_PRECNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_COMBCNT_PRECNT, self).__init__(register,
            'PRECNT', 'RTCC.COMBCNT.PRECNT', 'read-only',
            "",
            0, 15)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_COMBCNT_CNTLSB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_COMBCNT_CNTLSB, self).__init__(register,
            'CNTLSB', 'RTCC.COMBCNT.CNTLSB', 'read-only',
            "",
            15, 17)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_TIME_SECU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_TIME_SECU, self).__init__(register,
            'SECU', 'RTCC.TIME.SECU', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_TIME_SECT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_TIME_SECT, self).__init__(register,
            'SECT', 'RTCC.TIME.SECT', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_TIME_MINU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_TIME_MINU, self).__init__(register,
            'MINU', 'RTCC.TIME.MINU', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_TIME_MINT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_TIME_MINT, self).__init__(register,
            'MINT', 'RTCC.TIME.MINT', 'read-write',
            "",
            12, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_TIME_HOURU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_TIME_HOURU, self).__init__(register,
            'HOURU', 'RTCC.TIME.HOURU', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_TIME_HOURT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_TIME_HOURT, self).__init__(register,
            'HOURT', 'RTCC.TIME.HOURT', 'read-write',
            "",
            20, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_DATE_DAYOMU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_DATE_DAYOMU, self).__init__(register,
            'DAYOMU', 'RTCC.DATE.DAYOMU', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_DATE_DAYOMT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_DATE_DAYOMT, self).__init__(register,
            'DAYOMT', 'RTCC.DATE.DAYOMT', 'read-write',
            "",
            4, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_DATE_MONTHU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_DATE_MONTHU, self).__init__(register,
            'MONTHU', 'RTCC.DATE.MONTHU', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_DATE_MONTHT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_DATE_MONTHT, self).__init__(register,
            'MONTHT', 'RTCC.DATE.MONTHT', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_DATE_YEARU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_DATE_YEARU, self).__init__(register,
            'YEARU', 'RTCC.DATE.YEARU', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_DATE_YEART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_DATE_YEART, self).__init__(register,
            'YEART', 'RTCC.DATE.YEART', 'read-write',
            "",
            20, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_DATE_DAYOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_DATE_DAYOW, self).__init__(register,
            'DAYOW', 'RTCC.DATE.DAYOW', 'read-write',
            "",
            24, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IF_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IF_OF, self).__init__(register,
            'OF', 'RTCC.IF.OF', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IF_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IF_CC0, self).__init__(register,
            'CC0', 'RTCC.IF.CC0', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IF_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IF_CC1, self).__init__(register,
            'CC1', 'RTCC.IF.CC1', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IF_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IF_CC2, self).__init__(register,
            'CC2', 'RTCC.IF.CC2', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IF_OSCFAIL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IF_OSCFAIL, self).__init__(register,
            'OSCFAIL', 'RTCC.IF.OSCFAIL', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IF_CNTTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IF_CNTTICK, self).__init__(register,
            'CNTTICK', 'RTCC.IF.CNTTICK', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IF_MINTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IF_MINTICK, self).__init__(register,
            'MINTICK', 'RTCC.IF.MINTICK', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IF_HOURTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IF_HOURTICK, self).__init__(register,
            'HOURTICK', 'RTCC.IF.HOURTICK', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IF_DAYTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IF_DAYTICK, self).__init__(register,
            'DAYTICK', 'RTCC.IF.DAYTICK', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IF_DAYOWOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IF_DAYOWOF, self).__init__(register,
            'DAYOWOF', 'RTCC.IF.DAYOWOF', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IF_MONTHTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IF_MONTHTICK, self).__init__(register,
            'MONTHTICK', 'RTCC.IF.MONTHTICK', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFS_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFS_OF, self).__init__(register,
            'OF', 'RTCC.IFS.OF', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFS_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFS_CC0, self).__init__(register,
            'CC0', 'RTCC.IFS.CC0', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFS_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFS_CC1, self).__init__(register,
            'CC1', 'RTCC.IFS.CC1', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFS_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFS_CC2, self).__init__(register,
            'CC2', 'RTCC.IFS.CC2', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFS_OSCFAIL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFS_OSCFAIL, self).__init__(register,
            'OSCFAIL', 'RTCC.IFS.OSCFAIL', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFS_CNTTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFS_CNTTICK, self).__init__(register,
            'CNTTICK', 'RTCC.IFS.CNTTICK', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFS_MINTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFS_MINTICK, self).__init__(register,
            'MINTICK', 'RTCC.IFS.MINTICK', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFS_HOURTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFS_HOURTICK, self).__init__(register,
            'HOURTICK', 'RTCC.IFS.HOURTICK', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFS_DAYTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFS_DAYTICK, self).__init__(register,
            'DAYTICK', 'RTCC.IFS.DAYTICK', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFS_DAYOWOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFS_DAYOWOF, self).__init__(register,
            'DAYOWOF', 'RTCC.IFS.DAYOWOF', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFS_MONTHTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFS_MONTHTICK, self).__init__(register,
            'MONTHTICK', 'RTCC.IFS.MONTHTICK', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFC_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFC_OF, self).__init__(register,
            'OF', 'RTCC.IFC.OF', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFC_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFC_CC0, self).__init__(register,
            'CC0', 'RTCC.IFC.CC0', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFC_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFC_CC1, self).__init__(register,
            'CC1', 'RTCC.IFC.CC1', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFC_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFC_CC2, self).__init__(register,
            'CC2', 'RTCC.IFC.CC2', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFC_OSCFAIL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFC_OSCFAIL, self).__init__(register,
            'OSCFAIL', 'RTCC.IFC.OSCFAIL', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFC_CNTTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFC_CNTTICK, self).__init__(register,
            'CNTTICK', 'RTCC.IFC.CNTTICK', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFC_MINTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFC_MINTICK, self).__init__(register,
            'MINTICK', 'RTCC.IFC.MINTICK', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFC_HOURTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFC_HOURTICK, self).__init__(register,
            'HOURTICK', 'RTCC.IFC.HOURTICK', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFC_DAYTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFC_DAYTICK, self).__init__(register,
            'DAYTICK', 'RTCC.IFC.DAYTICK', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFC_DAYOWOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFC_DAYOWOF, self).__init__(register,
            'DAYOWOF', 'RTCC.IFC.DAYOWOF', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IFC_MONTHTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IFC_MONTHTICK, self).__init__(register,
            'MONTHTICK', 'RTCC.IFC.MONTHTICK', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IEN_OF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IEN_OF, self).__init__(register,
            'OF', 'RTCC.IEN.OF', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IEN_CC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IEN_CC0, self).__init__(register,
            'CC0', 'RTCC.IEN.CC0', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IEN_CC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IEN_CC1, self).__init__(register,
            'CC1', 'RTCC.IEN.CC1', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IEN_CC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IEN_CC2, self).__init__(register,
            'CC2', 'RTCC.IEN.CC2', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IEN_OSCFAIL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IEN_OSCFAIL, self).__init__(register,
            'OSCFAIL', 'RTCC.IEN.OSCFAIL', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IEN_CNTTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IEN_CNTTICK, self).__init__(register,
            'CNTTICK', 'RTCC.IEN.CNTTICK', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IEN_MINTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IEN_MINTICK, self).__init__(register,
            'MINTICK', 'RTCC.IEN.MINTICK', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IEN_HOURTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IEN_HOURTICK, self).__init__(register,
            'HOURTICK', 'RTCC.IEN.HOURTICK', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IEN_DAYTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IEN_DAYTICK, self).__init__(register,
            'DAYTICK', 'RTCC.IEN.DAYTICK', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IEN_DAYOWOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IEN_DAYOWOF, self).__init__(register,
            'DAYOWOF', 'RTCC.IEN.DAYOWOF', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_IEN_MONTHTICK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_IEN_MONTHTICK, self).__init__(register,
            'MONTHTICK', 'RTCC.IEN.MONTHTICK', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CMD_CLRSTATUS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CMD_CLRSTATUS, self).__init__(register,
            'CLRSTATUS', 'RTCC.CMD.CLRSTATUS', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_SYNCBUSY_CMD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_SYNCBUSY_CMD, self).__init__(register,
            'CMD', 'RTCC.SYNCBUSY.CMD', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_POWERDOWN_RAM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_POWERDOWN_RAM, self).__init__(register,
            'RAM', 'RTCC.POWERDOWN.RAM', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_LOCK_LOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_LOCK_LOCKKEY, self).__init__(register,
            'LOCKKEY', 'RTCC.LOCK.LOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_RTCC_LOCK_LOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_EM4WUEN_EM4WU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_EM4WUEN_EM4WU, self).__init__(register,
            'EM4WU', 'RTCC.EM4WUEN.EM4WU', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_CTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_CTRL_MODE, self).__init__(register,
            'MODE', 'RTCC.CC0_CTRL.MODE', 'read-write',
            "",
            0, 2,
            RM_Enum_RTCC_CC0_CTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_CTRL_CMOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_CTRL_CMOA, self).__init__(register,
            'CMOA', 'RTCC.CC0_CTRL.CMOA', 'read-write',
            "",
            2, 2,
            RM_Enum_RTCC_CC0_CTRL_CMOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'RTCC.CC0_CTRL.ICEDGE', 'read-write',
            "",
            4, 2,
            RM_Enum_RTCC_CC0_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'RTCC.CC0_CTRL.PRSSEL', 'read-write',
            "",
            6, 4,
            RM_Enum_RTCC_CC0_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_CTRL_COMPBASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_CTRL_COMPBASE, self).__init__(register,
            'COMPBASE', 'RTCC.CC0_CTRL.COMPBASE', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_CTRL_COMPMASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_CTRL_COMPMASK, self).__init__(register,
            'COMPMASK', 'RTCC.CC0_CTRL.COMPMASK', 'read-write',
            "",
            12, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_CTRL_DAYCC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_CTRL_DAYCC, self).__init__(register,
            'DAYCC', 'RTCC.CC0_CTRL.DAYCC', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_CCV_CCV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_CCV_CCV, self).__init__(register,
            'CCV', 'RTCC.CC0_CCV.CCV', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_TIME_SECU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_TIME_SECU, self).__init__(register,
            'SECU', 'RTCC.CC0_TIME.SECU', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_TIME_SECT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_TIME_SECT, self).__init__(register,
            'SECT', 'RTCC.CC0_TIME.SECT', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_TIME_MINU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_TIME_MINU, self).__init__(register,
            'MINU', 'RTCC.CC0_TIME.MINU', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_TIME_MINT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_TIME_MINT, self).__init__(register,
            'MINT', 'RTCC.CC0_TIME.MINT', 'read-write',
            "",
            12, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_TIME_HOURU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_TIME_HOURU, self).__init__(register,
            'HOURU', 'RTCC.CC0_TIME.HOURU', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_TIME_HOURT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_TIME_HOURT, self).__init__(register,
            'HOURT', 'RTCC.CC0_TIME.HOURT', 'read-write',
            "",
            20, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_DATE_DAYU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_DATE_DAYU, self).__init__(register,
            'DAYU', 'RTCC.CC0_DATE.DAYU', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_DATE_DAYT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_DATE_DAYT, self).__init__(register,
            'DAYT', 'RTCC.CC0_DATE.DAYT', 'read-write',
            "",
            4, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_DATE_MONTHU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_DATE_MONTHU, self).__init__(register,
            'MONTHU', 'RTCC.CC0_DATE.MONTHU', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC0_DATE_MONTHT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC0_DATE_MONTHT, self).__init__(register,
            'MONTHT', 'RTCC.CC0_DATE.MONTHT', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_CTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_CTRL_MODE, self).__init__(register,
            'MODE', 'RTCC.CC1_CTRL.MODE', 'read-write',
            "",
            0, 2,
            RM_Enum_RTCC_CC1_CTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_CTRL_CMOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_CTRL_CMOA, self).__init__(register,
            'CMOA', 'RTCC.CC1_CTRL.CMOA', 'read-write',
            "",
            2, 2,
            RM_Enum_RTCC_CC1_CTRL_CMOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'RTCC.CC1_CTRL.ICEDGE', 'read-write',
            "",
            4, 2,
            RM_Enum_RTCC_CC1_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'RTCC.CC1_CTRL.PRSSEL', 'read-write',
            "",
            6, 4,
            RM_Enum_RTCC_CC1_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_CTRL_COMPBASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_CTRL_COMPBASE, self).__init__(register,
            'COMPBASE', 'RTCC.CC1_CTRL.COMPBASE', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_CTRL_COMPMASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_CTRL_COMPMASK, self).__init__(register,
            'COMPMASK', 'RTCC.CC1_CTRL.COMPMASK', 'read-write',
            "",
            12, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_CTRL_DAYCC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_CTRL_DAYCC, self).__init__(register,
            'DAYCC', 'RTCC.CC1_CTRL.DAYCC', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_CCV_CCV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_CCV_CCV, self).__init__(register,
            'CCV', 'RTCC.CC1_CCV.CCV', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_TIME_SECU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_TIME_SECU, self).__init__(register,
            'SECU', 'RTCC.CC1_TIME.SECU', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_TIME_SECT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_TIME_SECT, self).__init__(register,
            'SECT', 'RTCC.CC1_TIME.SECT', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_TIME_MINU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_TIME_MINU, self).__init__(register,
            'MINU', 'RTCC.CC1_TIME.MINU', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_TIME_MINT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_TIME_MINT, self).__init__(register,
            'MINT', 'RTCC.CC1_TIME.MINT', 'read-write',
            "",
            12, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_TIME_HOURU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_TIME_HOURU, self).__init__(register,
            'HOURU', 'RTCC.CC1_TIME.HOURU', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_TIME_HOURT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_TIME_HOURT, self).__init__(register,
            'HOURT', 'RTCC.CC1_TIME.HOURT', 'read-write',
            "",
            20, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_DATE_DAYU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_DATE_DAYU, self).__init__(register,
            'DAYU', 'RTCC.CC1_DATE.DAYU', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_DATE_DAYT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_DATE_DAYT, self).__init__(register,
            'DAYT', 'RTCC.CC1_DATE.DAYT', 'read-write',
            "",
            4, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_DATE_MONTHU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_DATE_MONTHU, self).__init__(register,
            'MONTHU', 'RTCC.CC1_DATE.MONTHU', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC1_DATE_MONTHT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC1_DATE_MONTHT, self).__init__(register,
            'MONTHT', 'RTCC.CC1_DATE.MONTHT', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_CTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_CTRL_MODE, self).__init__(register,
            'MODE', 'RTCC.CC2_CTRL.MODE', 'read-write',
            "",
            0, 2,
            RM_Enum_RTCC_CC2_CTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_CTRL_CMOA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_CTRL_CMOA, self).__init__(register,
            'CMOA', 'RTCC.CC2_CTRL.CMOA', 'read-write',
            "",
            2, 2,
            RM_Enum_RTCC_CC2_CTRL_CMOA(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_CTRL_ICEDGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_CTRL_ICEDGE, self).__init__(register,
            'ICEDGE', 'RTCC.CC2_CTRL.ICEDGE', 'read-write',
            "",
            4, 2,
            RM_Enum_RTCC_CC2_CTRL_ICEDGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_CTRL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_CTRL_PRSSEL, self).__init__(register,
            'PRSSEL', 'RTCC.CC2_CTRL.PRSSEL', 'read-write',
            "",
            6, 4,
            RM_Enum_RTCC_CC2_CTRL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_CTRL_COMPBASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_CTRL_COMPBASE, self).__init__(register,
            'COMPBASE', 'RTCC.CC2_CTRL.COMPBASE', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_CTRL_COMPMASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_CTRL_COMPMASK, self).__init__(register,
            'COMPMASK', 'RTCC.CC2_CTRL.COMPMASK', 'read-write',
            "",
            12, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_CTRL_DAYCC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_CTRL_DAYCC, self).__init__(register,
            'DAYCC', 'RTCC.CC2_CTRL.DAYCC', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_CCV_CCV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_CCV_CCV, self).__init__(register,
            'CCV', 'RTCC.CC2_CCV.CCV', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_TIME_SECU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_TIME_SECU, self).__init__(register,
            'SECU', 'RTCC.CC2_TIME.SECU', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_TIME_SECT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_TIME_SECT, self).__init__(register,
            'SECT', 'RTCC.CC2_TIME.SECT', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_TIME_MINU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_TIME_MINU, self).__init__(register,
            'MINU', 'RTCC.CC2_TIME.MINU', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_TIME_MINT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_TIME_MINT, self).__init__(register,
            'MINT', 'RTCC.CC2_TIME.MINT', 'read-write',
            "",
            12, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_TIME_HOURU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_TIME_HOURU, self).__init__(register,
            'HOURU', 'RTCC.CC2_TIME.HOURU', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_TIME_HOURT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_TIME_HOURT, self).__init__(register,
            'HOURT', 'RTCC.CC2_TIME.HOURT', 'read-write',
            "",
            20, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_DATE_DAYU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_DATE_DAYU, self).__init__(register,
            'DAYU', 'RTCC.CC2_DATE.DAYU', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_DATE_DAYT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_DATE_DAYT, self).__init__(register,
            'DAYT', 'RTCC.CC2_DATE.DAYT', 'read-write',
            "",
            4, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_DATE_MONTHU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_DATE_MONTHU, self).__init__(register,
            'MONTHU', 'RTCC.CC2_DATE.MONTHU', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_CC2_DATE_MONTHT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_CC2_DATE_MONTHT, self).__init__(register,
            'MONTHT', 'RTCC.CC2_DATE.MONTHT', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET0_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET0_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET0_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET1_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET1_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET1_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET2_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET2_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET2_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET3_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET3_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET3_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET4_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET4_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET4_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET5_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET5_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET5_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET6_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET6_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET6_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET7_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET7_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET7_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET8_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET8_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET8_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET9_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET9_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET9_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET10_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET10_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET10_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET11_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET11_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET11_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET12_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET12_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET12_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET13_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET13_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET13_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET14_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET14_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET14_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET15_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET15_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET15_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET16_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET16_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET16_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET17_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET17_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET17_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET18_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET18_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET18_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET19_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET19_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET19_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET20_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET20_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET20_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET21_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET21_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET21_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET22_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET22_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET22_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET23_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET23_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET23_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET24_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET24_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET24_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET25_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET25_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET25_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET26_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET26_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET26_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET27_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET27_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET27_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET28_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET28_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET28_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET29_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET29_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET29_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET30_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET30_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET30_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_RTCC_RET31_REG_REG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_RTCC_RET31_REG_REG, self).__init__(register,
            'REG', 'RTCC.RET31_REG.REG', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


