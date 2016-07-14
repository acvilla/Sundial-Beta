
from static import Base_RM_Register
from FPUEH_field import *


class RM_Register_FPUEH_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FPUEH_IF, self).__init__(rmio, label,
            0x400e1000, 0x000,
            'IF', 'FPUEH.IF', 'read-only',
            "",
            0x00000000, 0x0000003F)

        self.FPIOC = RM_Field_FPUEH_IF_FPIOC(self)
        self.zz_fdict['FPIOC'] = self.FPIOC
        self.FPDZC = RM_Field_FPUEH_IF_FPDZC(self)
        self.zz_fdict['FPDZC'] = self.FPDZC
        self.FPUFC = RM_Field_FPUEH_IF_FPUFC(self)
        self.zz_fdict['FPUFC'] = self.FPUFC
        self.FPOFC = RM_Field_FPUEH_IF_FPOFC(self)
        self.zz_fdict['FPOFC'] = self.FPOFC
        self.FPIDC = RM_Field_FPUEH_IF_FPIDC(self)
        self.zz_fdict['FPIDC'] = self.FPIDC
        self.FPIXC = RM_Field_FPUEH_IF_FPIXC(self)
        self.zz_fdict['FPIXC'] = self.FPIXC
        self.__dict__['zz_frozen'] = True


class RM_Register_FPUEH_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FPUEH_IFS, self).__init__(rmio, label,
            0x400e1000, 0x004,
            'IFS', 'FPUEH.IFS', 'write-only',
            "",
            0x00000000, 0x0000003F)

        self.FPIOC = RM_Field_FPUEH_IFS_FPIOC(self)
        self.zz_fdict['FPIOC'] = self.FPIOC
        self.FPDZC = RM_Field_FPUEH_IFS_FPDZC(self)
        self.zz_fdict['FPDZC'] = self.FPDZC
        self.FPUFC = RM_Field_FPUEH_IFS_FPUFC(self)
        self.zz_fdict['FPUFC'] = self.FPUFC
        self.FPOFC = RM_Field_FPUEH_IFS_FPOFC(self)
        self.zz_fdict['FPOFC'] = self.FPOFC
        self.FPIDC = RM_Field_FPUEH_IFS_FPIDC(self)
        self.zz_fdict['FPIDC'] = self.FPIDC
        self.FPIXC = RM_Field_FPUEH_IFS_FPIXC(self)
        self.zz_fdict['FPIXC'] = self.FPIXC
        self.__dict__['zz_frozen'] = True


class RM_Register_FPUEH_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FPUEH_IFC, self).__init__(rmio, label,
            0x400e1000, 0x008,
            'IFC', 'FPUEH.IFC', 'write-only',
            "",
            0x00000000, 0x0000003F)

        self.FPIOC = RM_Field_FPUEH_IFC_FPIOC(self)
        self.zz_fdict['FPIOC'] = self.FPIOC
        self.FPDZC = RM_Field_FPUEH_IFC_FPDZC(self)
        self.zz_fdict['FPDZC'] = self.FPDZC
        self.FPUFC = RM_Field_FPUEH_IFC_FPUFC(self)
        self.zz_fdict['FPUFC'] = self.FPUFC
        self.FPOFC = RM_Field_FPUEH_IFC_FPOFC(self)
        self.zz_fdict['FPOFC'] = self.FPOFC
        self.FPIDC = RM_Field_FPUEH_IFC_FPIDC(self)
        self.zz_fdict['FPIDC'] = self.FPIDC
        self.FPIXC = RM_Field_FPUEH_IFC_FPIXC(self)
        self.zz_fdict['FPIXC'] = self.FPIXC
        self.__dict__['zz_frozen'] = True


class RM_Register_FPUEH_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FPUEH_IEN, self).__init__(rmio, label,
            0x400e1000, 0x00C,
            'IEN', 'FPUEH.IEN', 'read-write',
            "",
            0x00000000, 0x0000003F)

        self.FPIOC = RM_Field_FPUEH_IEN_FPIOC(self)
        self.zz_fdict['FPIOC'] = self.FPIOC
        self.FPDZC = RM_Field_FPUEH_IEN_FPDZC(self)
        self.zz_fdict['FPDZC'] = self.FPDZC
        self.FPUFC = RM_Field_FPUEH_IEN_FPUFC(self)
        self.zz_fdict['FPUFC'] = self.FPUFC
        self.FPOFC = RM_Field_FPUEH_IEN_FPOFC(self)
        self.zz_fdict['FPOFC'] = self.FPOFC
        self.FPIDC = RM_Field_FPUEH_IEN_FPIDC(self)
        self.zz_fdict['FPIDC'] = self.FPIDC
        self.FPIXC = RM_Field_FPUEH_IEN_FPIXC(self)
        self.zz_fdict['FPIXC'] = self.FPIXC
        self.__dict__['zz_frozen'] = True


