
from static import Base_RM_Field
from FPUEH_enum import *


class RM_Field_FPUEH_IF_FPIOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IF_FPIOC, self).__init__(register,
            'FPIOC', 'FPUEH.IF.FPIOC', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IF_FPDZC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IF_FPDZC, self).__init__(register,
            'FPDZC', 'FPUEH.IF.FPDZC', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IF_FPUFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IF_FPUFC, self).__init__(register,
            'FPUFC', 'FPUEH.IF.FPUFC', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IF_FPOFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IF_FPOFC, self).__init__(register,
            'FPOFC', 'FPUEH.IF.FPOFC', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IF_FPIDC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IF_FPIDC, self).__init__(register,
            'FPIDC', 'FPUEH.IF.FPIDC', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IF_FPIXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IF_FPIXC, self).__init__(register,
            'FPIXC', 'FPUEH.IF.FPIXC', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IFS_FPIOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IFS_FPIOC, self).__init__(register,
            'FPIOC', 'FPUEH.IFS.FPIOC', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IFS_FPDZC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IFS_FPDZC, self).__init__(register,
            'FPDZC', 'FPUEH.IFS.FPDZC', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IFS_FPUFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IFS_FPUFC, self).__init__(register,
            'FPUFC', 'FPUEH.IFS.FPUFC', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IFS_FPOFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IFS_FPOFC, self).__init__(register,
            'FPOFC', 'FPUEH.IFS.FPOFC', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IFS_FPIDC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IFS_FPIDC, self).__init__(register,
            'FPIDC', 'FPUEH.IFS.FPIDC', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IFS_FPIXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IFS_FPIXC, self).__init__(register,
            'FPIXC', 'FPUEH.IFS.FPIXC', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IFC_FPIOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IFC_FPIOC, self).__init__(register,
            'FPIOC', 'FPUEH.IFC.FPIOC', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IFC_FPDZC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IFC_FPDZC, self).__init__(register,
            'FPDZC', 'FPUEH.IFC.FPDZC', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IFC_FPUFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IFC_FPUFC, self).__init__(register,
            'FPUFC', 'FPUEH.IFC.FPUFC', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IFC_FPOFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IFC_FPOFC, self).__init__(register,
            'FPOFC', 'FPUEH.IFC.FPOFC', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IFC_FPIDC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IFC_FPIDC, self).__init__(register,
            'FPIDC', 'FPUEH.IFC.FPIDC', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IFC_FPIXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IFC_FPIXC, self).__init__(register,
            'FPIXC', 'FPUEH.IFC.FPIXC', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IEN_FPIOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IEN_FPIOC, self).__init__(register,
            'FPIOC', 'FPUEH.IEN.FPIOC', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IEN_FPDZC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IEN_FPDZC, self).__init__(register,
            'FPDZC', 'FPUEH.IEN.FPDZC', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IEN_FPUFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IEN_FPUFC, self).__init__(register,
            'FPUFC', 'FPUEH.IEN.FPUFC', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IEN_FPOFC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IEN_FPOFC, self).__init__(register,
            'FPOFC', 'FPUEH.IEN.FPOFC', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IEN_FPIDC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IEN_FPIDC, self).__init__(register,
            'FPIDC', 'FPUEH.IEN.FPIDC', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_FPUEH_IEN_FPIXC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_FPUEH_IEN_FPIXC, self).__init__(register,
            'FPIXC', 'FPUEH.IEN.FPIXC', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


