
from static import Base_RM_Field
from SEQ_enum import *


class RM_Field_SEQ_MISC_SQBMODETX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SEQ_MISC_SQBMODETX, self).__init__(register,
            'SQBMODETX', 'SEQ.MISC.SQBMODETX', 'read-write',
            "",
            10, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_SEQ_SYNTHLPFCTRLRX_SYNTHLPFCTRLRX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SEQ_SYNTHLPFCTRLRX_SYNTHLPFCTRLRX, self).__init__(register,
            'SYNTHLPFCTRLRX', 'SEQ.SYNTHLPFCTRLRX.SYNTHLPFCTRLRX', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_SEQ_SYNTHLPFCTRLTX_SYNTHLPFCTRLTX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_SEQ_SYNTHLPFCTRLTX_SYNTHLPFCTRLTX, self).__init__(register,
            'SYNTHLPFCTRLTX', 'SEQ.SYNTHLPFCTRLTX.SYNTHLPFCTRLTX', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


