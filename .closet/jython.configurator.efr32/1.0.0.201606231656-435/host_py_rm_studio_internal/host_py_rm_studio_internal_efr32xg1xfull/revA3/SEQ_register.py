
from static import Base_RM_Register
from SEQ_field import *


class RM_Register_SEQ_MISC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SEQ_MISC, self).__init__(rmio, label,
            0x21000ff4, 0x000,
            'MISC', 'SEQ.MISC', 'read-write',
            "",
            0x00000000, 0x00000000)

        self.SQBMODETX = RM_Field_SEQ_MISC_SQBMODETX(self)
        self.zz_fdict['SQBMODETX'] = self.SQBMODETX
        self.__dict__['zz_frozen'] = True


class RM_Register_SEQ_SYNTHLPFCTRLRX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SEQ_SYNTHLPFCTRLRX, self).__init__(rmio, label,
            0x21000ff4, 0x004,
            'SYNTHLPFCTRLRX', 'SEQ.SYNTHLPFCTRLRX', 'read-write',
            "",
            0x00000000, 0x00000000)

        self.SYNTHLPFCTRLRX = RM_Field_SEQ_SYNTHLPFCTRLRX_SYNTHLPFCTRLRX(self)
        self.zz_fdict['SYNTHLPFCTRLRX'] = self.SYNTHLPFCTRLRX
        self.__dict__['zz_frozen'] = True


class RM_Register_SEQ_SYNTHLPFCTRLTX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_SEQ_SYNTHLPFCTRLTX, self).__init__(rmio, label,
            0x21000ff4, 0x008,
            'SYNTHLPFCTRLTX', 'SEQ.SYNTHLPFCTRLTX', 'read-write',
            "",
            0x00000000, 0x00000000)

        self.SYNTHLPFCTRLTX = RM_Field_SEQ_SYNTHLPFCTRLTX_SYNTHLPFCTRLTX(self)
        self.zz_fdict['SYNTHLPFCTRLTX'] = self.SYNTHLPFCTRLTX
        self.__dict__['zz_frozen'] = True


