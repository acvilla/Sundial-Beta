
from static import Base_RM_Field
from GPIO_enum import *


class RM_Field_GPIO_PA_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'GPIO.PA_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_CTRL_SLEWRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_CTRL_SLEWRATE, self).__init__(register,
            'SLEWRATE', 'GPIO.PA_CTRL.SLEWRATE', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_CTRL_DINDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_CTRL_DINDIS, self).__init__(register,
            'DINDIS', 'GPIO.PA_CTRL.DINDIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_CTRL_DRIVESTRENGTHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_CTRL_DRIVESTRENGTHALT, self).__init__(register,
            'DRIVESTRENGTHALT', 'GPIO.PA_CTRL.DRIVESTRENGTHALT', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_CTRL_SLEWRATEALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_CTRL_SLEWRATEALT, self).__init__(register,
            'SLEWRATEALT', 'GPIO.PA_CTRL.SLEWRATEALT', 'read-write',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_CTRL_DINDISALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_CTRL_DINDISALT, self).__init__(register,
            'DINDISALT', 'GPIO.PA_CTRL.DINDISALT', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEL_MODE0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEL_MODE0, self).__init__(register,
            'MODE0', 'GPIO.PA_MODEL.MODE0', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PA_MODEL_MODE0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEL_MODE1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEL_MODE1, self).__init__(register,
            'MODE1', 'GPIO.PA_MODEL.MODE1', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PA_MODEL_MODE1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEL_MODE2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEL_MODE2, self).__init__(register,
            'MODE2', 'GPIO.PA_MODEL.MODE2', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PA_MODEL_MODE2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEL_MODE3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEL_MODE3, self).__init__(register,
            'MODE3', 'GPIO.PA_MODEL.MODE3', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PA_MODEL_MODE3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEL_MODE4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEL_MODE4, self).__init__(register,
            'MODE4', 'GPIO.PA_MODEL.MODE4', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PA_MODEL_MODE4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEL_MODE5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEL_MODE5, self).__init__(register,
            'MODE5', 'GPIO.PA_MODEL.MODE5', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PA_MODEL_MODE5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEL_MODE6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEL_MODE6, self).__init__(register,
            'MODE6', 'GPIO.PA_MODEL.MODE6', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PA_MODEL_MODE6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEL_MODE7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEL_MODE7, self).__init__(register,
            'MODE7', 'GPIO.PA_MODEL.MODE7', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PA_MODEL_MODE7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEH_MODE8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEH_MODE8, self).__init__(register,
            'MODE8', 'GPIO.PA_MODEH.MODE8', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PA_MODEH_MODE8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEH_MODE9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEH_MODE9, self).__init__(register,
            'MODE9', 'GPIO.PA_MODEH.MODE9', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PA_MODEH_MODE9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEH_MODE10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEH_MODE10, self).__init__(register,
            'MODE10', 'GPIO.PA_MODEH.MODE10', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PA_MODEH_MODE10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEH_MODE11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEH_MODE11, self).__init__(register,
            'MODE11', 'GPIO.PA_MODEH.MODE11', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PA_MODEH_MODE11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEH_MODE12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEH_MODE12, self).__init__(register,
            'MODE12', 'GPIO.PA_MODEH.MODE12', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PA_MODEH_MODE12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEH_MODE13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEH_MODE13, self).__init__(register,
            'MODE13', 'GPIO.PA_MODEH.MODE13', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PA_MODEH_MODE13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEH_MODE14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEH_MODE14, self).__init__(register,
            'MODE14', 'GPIO.PA_MODEH.MODE14', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PA_MODEH_MODE14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_MODEH_MODE15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_MODEH_MODE15, self).__init__(register,
            'MODE15', 'GPIO.PA_MODEH.MODE15', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PA_MODEH_MODE15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_DOUT_DOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_DOUT_DOUT, self).__init__(register,
            'DOUT', 'GPIO.PA_DOUT.DOUT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_DOUTTGL_DOUTTGL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_DOUTTGL_DOUTTGL, self).__init__(register,
            'DOUTTGL', 'GPIO.PA_DOUTTGL.DOUTTGL', 'write-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_DIN_DIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_DIN_DIN, self).__init__(register,
            'DIN', 'GPIO.PA_DIN.DIN', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_PINLOCKN_PINLOCKN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_PINLOCKN_PINLOCKN, self).__init__(register,
            'PINLOCKN', 'GPIO.PA_PINLOCKN.PINLOCKN', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PA_TOL5VDIS_TOL5VDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PA_TOL5VDIS_TOL5VDIS, self).__init__(register,
            'TOL5VDIS', 'GPIO.PA_TOL5VDIS.TOL5VDIS', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'GPIO.PB_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_CTRL_SLEWRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_CTRL_SLEWRATE, self).__init__(register,
            'SLEWRATE', 'GPIO.PB_CTRL.SLEWRATE', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_CTRL_DINDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_CTRL_DINDIS, self).__init__(register,
            'DINDIS', 'GPIO.PB_CTRL.DINDIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_CTRL_DRIVESTRENGTHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_CTRL_DRIVESTRENGTHALT, self).__init__(register,
            'DRIVESTRENGTHALT', 'GPIO.PB_CTRL.DRIVESTRENGTHALT', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_CTRL_SLEWRATEALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_CTRL_SLEWRATEALT, self).__init__(register,
            'SLEWRATEALT', 'GPIO.PB_CTRL.SLEWRATEALT', 'read-write',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_CTRL_DINDISALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_CTRL_DINDISALT, self).__init__(register,
            'DINDISALT', 'GPIO.PB_CTRL.DINDISALT', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEL_MODE0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEL_MODE0, self).__init__(register,
            'MODE0', 'GPIO.PB_MODEL.MODE0', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PB_MODEL_MODE0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEL_MODE1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEL_MODE1, self).__init__(register,
            'MODE1', 'GPIO.PB_MODEL.MODE1', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PB_MODEL_MODE1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEL_MODE2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEL_MODE2, self).__init__(register,
            'MODE2', 'GPIO.PB_MODEL.MODE2', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PB_MODEL_MODE2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEL_MODE3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEL_MODE3, self).__init__(register,
            'MODE3', 'GPIO.PB_MODEL.MODE3', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PB_MODEL_MODE3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEL_MODE4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEL_MODE4, self).__init__(register,
            'MODE4', 'GPIO.PB_MODEL.MODE4', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PB_MODEL_MODE4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEL_MODE5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEL_MODE5, self).__init__(register,
            'MODE5', 'GPIO.PB_MODEL.MODE5', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PB_MODEL_MODE5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEL_MODE6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEL_MODE6, self).__init__(register,
            'MODE6', 'GPIO.PB_MODEL.MODE6', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PB_MODEL_MODE6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEL_MODE7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEL_MODE7, self).__init__(register,
            'MODE7', 'GPIO.PB_MODEL.MODE7', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PB_MODEL_MODE7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEH_MODE8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEH_MODE8, self).__init__(register,
            'MODE8', 'GPIO.PB_MODEH.MODE8', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PB_MODEH_MODE8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEH_MODE9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEH_MODE9, self).__init__(register,
            'MODE9', 'GPIO.PB_MODEH.MODE9', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PB_MODEH_MODE9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEH_MODE10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEH_MODE10, self).__init__(register,
            'MODE10', 'GPIO.PB_MODEH.MODE10', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PB_MODEH_MODE10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEH_MODE11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEH_MODE11, self).__init__(register,
            'MODE11', 'GPIO.PB_MODEH.MODE11', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PB_MODEH_MODE11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEH_MODE12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEH_MODE12, self).__init__(register,
            'MODE12', 'GPIO.PB_MODEH.MODE12', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PB_MODEH_MODE12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEH_MODE13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEH_MODE13, self).__init__(register,
            'MODE13', 'GPIO.PB_MODEH.MODE13', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PB_MODEH_MODE13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEH_MODE14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEH_MODE14, self).__init__(register,
            'MODE14', 'GPIO.PB_MODEH.MODE14', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PB_MODEH_MODE14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_MODEH_MODE15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_MODEH_MODE15, self).__init__(register,
            'MODE15', 'GPIO.PB_MODEH.MODE15', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PB_MODEH_MODE15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_DOUT_DOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_DOUT_DOUT, self).__init__(register,
            'DOUT', 'GPIO.PB_DOUT.DOUT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_DOUTTGL_DOUTTGL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_DOUTTGL_DOUTTGL, self).__init__(register,
            'DOUTTGL', 'GPIO.PB_DOUTTGL.DOUTTGL', 'write-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_DIN_DIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_DIN_DIN, self).__init__(register,
            'DIN', 'GPIO.PB_DIN.DIN', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_PINLOCKN_PINLOCKN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_PINLOCKN_PINLOCKN, self).__init__(register,
            'PINLOCKN', 'GPIO.PB_PINLOCKN.PINLOCKN', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PB_TOL5VDIS_TOL5VDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PB_TOL5VDIS_TOL5VDIS, self).__init__(register,
            'TOL5VDIS', 'GPIO.PB_TOL5VDIS.TOL5VDIS', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'GPIO.PC_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_CTRL_SLEWRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_CTRL_SLEWRATE, self).__init__(register,
            'SLEWRATE', 'GPIO.PC_CTRL.SLEWRATE', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_CTRL_DINDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_CTRL_DINDIS, self).__init__(register,
            'DINDIS', 'GPIO.PC_CTRL.DINDIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_CTRL_DRIVESTRENGTHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_CTRL_DRIVESTRENGTHALT, self).__init__(register,
            'DRIVESTRENGTHALT', 'GPIO.PC_CTRL.DRIVESTRENGTHALT', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_CTRL_SLEWRATEALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_CTRL_SLEWRATEALT, self).__init__(register,
            'SLEWRATEALT', 'GPIO.PC_CTRL.SLEWRATEALT', 'read-write',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_CTRL_DINDISALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_CTRL_DINDISALT, self).__init__(register,
            'DINDISALT', 'GPIO.PC_CTRL.DINDISALT', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEL_MODE0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEL_MODE0, self).__init__(register,
            'MODE0', 'GPIO.PC_MODEL.MODE0', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PC_MODEL_MODE0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEL_MODE1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEL_MODE1, self).__init__(register,
            'MODE1', 'GPIO.PC_MODEL.MODE1', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PC_MODEL_MODE1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEL_MODE2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEL_MODE2, self).__init__(register,
            'MODE2', 'GPIO.PC_MODEL.MODE2', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PC_MODEL_MODE2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEL_MODE3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEL_MODE3, self).__init__(register,
            'MODE3', 'GPIO.PC_MODEL.MODE3', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PC_MODEL_MODE3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEL_MODE4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEL_MODE4, self).__init__(register,
            'MODE4', 'GPIO.PC_MODEL.MODE4', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PC_MODEL_MODE4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEL_MODE5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEL_MODE5, self).__init__(register,
            'MODE5', 'GPIO.PC_MODEL.MODE5', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PC_MODEL_MODE5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEL_MODE6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEL_MODE6, self).__init__(register,
            'MODE6', 'GPIO.PC_MODEL.MODE6', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PC_MODEL_MODE6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEL_MODE7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEL_MODE7, self).__init__(register,
            'MODE7', 'GPIO.PC_MODEL.MODE7', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PC_MODEL_MODE7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEH_MODE8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEH_MODE8, self).__init__(register,
            'MODE8', 'GPIO.PC_MODEH.MODE8', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PC_MODEH_MODE8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEH_MODE9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEH_MODE9, self).__init__(register,
            'MODE9', 'GPIO.PC_MODEH.MODE9', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PC_MODEH_MODE9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEH_MODE10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEH_MODE10, self).__init__(register,
            'MODE10', 'GPIO.PC_MODEH.MODE10', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PC_MODEH_MODE10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEH_MODE11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEH_MODE11, self).__init__(register,
            'MODE11', 'GPIO.PC_MODEH.MODE11', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PC_MODEH_MODE11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEH_MODE12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEH_MODE12, self).__init__(register,
            'MODE12', 'GPIO.PC_MODEH.MODE12', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PC_MODEH_MODE12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEH_MODE13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEH_MODE13, self).__init__(register,
            'MODE13', 'GPIO.PC_MODEH.MODE13', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PC_MODEH_MODE13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEH_MODE14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEH_MODE14, self).__init__(register,
            'MODE14', 'GPIO.PC_MODEH.MODE14', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PC_MODEH_MODE14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_MODEH_MODE15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_MODEH_MODE15, self).__init__(register,
            'MODE15', 'GPIO.PC_MODEH.MODE15', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PC_MODEH_MODE15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_DOUT_DOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_DOUT_DOUT, self).__init__(register,
            'DOUT', 'GPIO.PC_DOUT.DOUT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_DOUTTGL_DOUTTGL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_DOUTTGL_DOUTTGL, self).__init__(register,
            'DOUTTGL', 'GPIO.PC_DOUTTGL.DOUTTGL', 'write-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_DIN_DIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_DIN_DIN, self).__init__(register,
            'DIN', 'GPIO.PC_DIN.DIN', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_PINLOCKN_PINLOCKN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_PINLOCKN_PINLOCKN, self).__init__(register,
            'PINLOCKN', 'GPIO.PC_PINLOCKN.PINLOCKN', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PC_TOL5VDIS_TOL5VDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PC_TOL5VDIS_TOL5VDIS, self).__init__(register,
            'TOL5VDIS', 'GPIO.PC_TOL5VDIS.TOL5VDIS', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'GPIO.PD_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_CTRL_SLEWRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_CTRL_SLEWRATE, self).__init__(register,
            'SLEWRATE', 'GPIO.PD_CTRL.SLEWRATE', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_CTRL_DINDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_CTRL_DINDIS, self).__init__(register,
            'DINDIS', 'GPIO.PD_CTRL.DINDIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_CTRL_DRIVESTRENGTHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_CTRL_DRIVESTRENGTHALT, self).__init__(register,
            'DRIVESTRENGTHALT', 'GPIO.PD_CTRL.DRIVESTRENGTHALT', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_CTRL_SLEWRATEALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_CTRL_SLEWRATEALT, self).__init__(register,
            'SLEWRATEALT', 'GPIO.PD_CTRL.SLEWRATEALT', 'read-write',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_CTRL_DINDISALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_CTRL_DINDISALT, self).__init__(register,
            'DINDISALT', 'GPIO.PD_CTRL.DINDISALT', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEL_MODE0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEL_MODE0, self).__init__(register,
            'MODE0', 'GPIO.PD_MODEL.MODE0', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PD_MODEL_MODE0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEL_MODE1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEL_MODE1, self).__init__(register,
            'MODE1', 'GPIO.PD_MODEL.MODE1', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PD_MODEL_MODE1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEL_MODE2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEL_MODE2, self).__init__(register,
            'MODE2', 'GPIO.PD_MODEL.MODE2', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PD_MODEL_MODE2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEL_MODE3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEL_MODE3, self).__init__(register,
            'MODE3', 'GPIO.PD_MODEL.MODE3', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PD_MODEL_MODE3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEL_MODE4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEL_MODE4, self).__init__(register,
            'MODE4', 'GPIO.PD_MODEL.MODE4', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PD_MODEL_MODE4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEL_MODE5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEL_MODE5, self).__init__(register,
            'MODE5', 'GPIO.PD_MODEL.MODE5', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PD_MODEL_MODE5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEL_MODE6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEL_MODE6, self).__init__(register,
            'MODE6', 'GPIO.PD_MODEL.MODE6', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PD_MODEL_MODE6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEL_MODE7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEL_MODE7, self).__init__(register,
            'MODE7', 'GPIO.PD_MODEL.MODE7', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PD_MODEL_MODE7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEH_MODE8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEH_MODE8, self).__init__(register,
            'MODE8', 'GPIO.PD_MODEH.MODE8', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PD_MODEH_MODE8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEH_MODE9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEH_MODE9, self).__init__(register,
            'MODE9', 'GPIO.PD_MODEH.MODE9', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PD_MODEH_MODE9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEH_MODE10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEH_MODE10, self).__init__(register,
            'MODE10', 'GPIO.PD_MODEH.MODE10', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PD_MODEH_MODE10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEH_MODE11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEH_MODE11, self).__init__(register,
            'MODE11', 'GPIO.PD_MODEH.MODE11', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PD_MODEH_MODE11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEH_MODE12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEH_MODE12, self).__init__(register,
            'MODE12', 'GPIO.PD_MODEH.MODE12', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PD_MODEH_MODE12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEH_MODE13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEH_MODE13, self).__init__(register,
            'MODE13', 'GPIO.PD_MODEH.MODE13', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PD_MODEH_MODE13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEH_MODE14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEH_MODE14, self).__init__(register,
            'MODE14', 'GPIO.PD_MODEH.MODE14', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PD_MODEH_MODE14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_MODEH_MODE15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_MODEH_MODE15, self).__init__(register,
            'MODE15', 'GPIO.PD_MODEH.MODE15', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PD_MODEH_MODE15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_DOUT_DOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_DOUT_DOUT, self).__init__(register,
            'DOUT', 'GPIO.PD_DOUT.DOUT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_DOUTTGL_DOUTTGL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_DOUTTGL_DOUTTGL, self).__init__(register,
            'DOUTTGL', 'GPIO.PD_DOUTTGL.DOUTTGL', 'write-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_DIN_DIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_DIN_DIN, self).__init__(register,
            'DIN', 'GPIO.PD_DIN.DIN', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_PINLOCKN_PINLOCKN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_PINLOCKN_PINLOCKN, self).__init__(register,
            'PINLOCKN', 'GPIO.PD_PINLOCKN.PINLOCKN', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PD_TOL5VDIS_TOL5VDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PD_TOL5VDIS_TOL5VDIS, self).__init__(register,
            'TOL5VDIS', 'GPIO.PD_TOL5VDIS.TOL5VDIS', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'GPIO.PE_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_CTRL_SLEWRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_CTRL_SLEWRATE, self).__init__(register,
            'SLEWRATE', 'GPIO.PE_CTRL.SLEWRATE', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_CTRL_DINDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_CTRL_DINDIS, self).__init__(register,
            'DINDIS', 'GPIO.PE_CTRL.DINDIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_CTRL_DRIVESTRENGTHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_CTRL_DRIVESTRENGTHALT, self).__init__(register,
            'DRIVESTRENGTHALT', 'GPIO.PE_CTRL.DRIVESTRENGTHALT', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_CTRL_SLEWRATEALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_CTRL_SLEWRATEALT, self).__init__(register,
            'SLEWRATEALT', 'GPIO.PE_CTRL.SLEWRATEALT', 'read-write',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_CTRL_DINDISALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_CTRL_DINDISALT, self).__init__(register,
            'DINDISALT', 'GPIO.PE_CTRL.DINDISALT', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEL_MODE0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEL_MODE0, self).__init__(register,
            'MODE0', 'GPIO.PE_MODEL.MODE0', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PE_MODEL_MODE0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEL_MODE1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEL_MODE1, self).__init__(register,
            'MODE1', 'GPIO.PE_MODEL.MODE1', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PE_MODEL_MODE1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEL_MODE2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEL_MODE2, self).__init__(register,
            'MODE2', 'GPIO.PE_MODEL.MODE2', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PE_MODEL_MODE2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEL_MODE3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEL_MODE3, self).__init__(register,
            'MODE3', 'GPIO.PE_MODEL.MODE3', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PE_MODEL_MODE3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEL_MODE4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEL_MODE4, self).__init__(register,
            'MODE4', 'GPIO.PE_MODEL.MODE4', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PE_MODEL_MODE4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEL_MODE5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEL_MODE5, self).__init__(register,
            'MODE5', 'GPIO.PE_MODEL.MODE5', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PE_MODEL_MODE5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEL_MODE6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEL_MODE6, self).__init__(register,
            'MODE6', 'GPIO.PE_MODEL.MODE6', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PE_MODEL_MODE6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEL_MODE7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEL_MODE7, self).__init__(register,
            'MODE7', 'GPIO.PE_MODEL.MODE7', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PE_MODEL_MODE7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEH_MODE8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEH_MODE8, self).__init__(register,
            'MODE8', 'GPIO.PE_MODEH.MODE8', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PE_MODEH_MODE8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEH_MODE9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEH_MODE9, self).__init__(register,
            'MODE9', 'GPIO.PE_MODEH.MODE9', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PE_MODEH_MODE9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEH_MODE10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEH_MODE10, self).__init__(register,
            'MODE10', 'GPIO.PE_MODEH.MODE10', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PE_MODEH_MODE10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEH_MODE11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEH_MODE11, self).__init__(register,
            'MODE11', 'GPIO.PE_MODEH.MODE11', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PE_MODEH_MODE11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEH_MODE12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEH_MODE12, self).__init__(register,
            'MODE12', 'GPIO.PE_MODEH.MODE12', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PE_MODEH_MODE12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEH_MODE13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEH_MODE13, self).__init__(register,
            'MODE13', 'GPIO.PE_MODEH.MODE13', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PE_MODEH_MODE13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEH_MODE14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEH_MODE14, self).__init__(register,
            'MODE14', 'GPIO.PE_MODEH.MODE14', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PE_MODEH_MODE14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_MODEH_MODE15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_MODEH_MODE15, self).__init__(register,
            'MODE15', 'GPIO.PE_MODEH.MODE15', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PE_MODEH_MODE15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_DOUT_DOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_DOUT_DOUT, self).__init__(register,
            'DOUT', 'GPIO.PE_DOUT.DOUT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_DOUTTGL_DOUTTGL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_DOUTTGL_DOUTTGL, self).__init__(register,
            'DOUTTGL', 'GPIO.PE_DOUTTGL.DOUTTGL', 'write-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_DIN_DIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_DIN_DIN, self).__init__(register,
            'DIN', 'GPIO.PE_DIN.DIN', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_PINLOCKN_PINLOCKN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_PINLOCKN_PINLOCKN, self).__init__(register,
            'PINLOCKN', 'GPIO.PE_PINLOCKN.PINLOCKN', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PE_TOL5VDIS_TOL5VDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PE_TOL5VDIS_TOL5VDIS, self).__init__(register,
            'TOL5VDIS', 'GPIO.PE_TOL5VDIS.TOL5VDIS', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'GPIO.PF_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_CTRL_SLEWRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_CTRL_SLEWRATE, self).__init__(register,
            'SLEWRATE', 'GPIO.PF_CTRL.SLEWRATE', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_CTRL_DINDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_CTRL_DINDIS, self).__init__(register,
            'DINDIS', 'GPIO.PF_CTRL.DINDIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_CTRL_DRIVESTRENGTHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_CTRL_DRIVESTRENGTHALT, self).__init__(register,
            'DRIVESTRENGTHALT', 'GPIO.PF_CTRL.DRIVESTRENGTHALT', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_CTRL_SLEWRATEALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_CTRL_SLEWRATEALT, self).__init__(register,
            'SLEWRATEALT', 'GPIO.PF_CTRL.SLEWRATEALT', 'read-write',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_CTRL_DINDISALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_CTRL_DINDISALT, self).__init__(register,
            'DINDISALT', 'GPIO.PF_CTRL.DINDISALT', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEL_MODE0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEL_MODE0, self).__init__(register,
            'MODE0', 'GPIO.PF_MODEL.MODE0', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PF_MODEL_MODE0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEL_MODE1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEL_MODE1, self).__init__(register,
            'MODE1', 'GPIO.PF_MODEL.MODE1', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PF_MODEL_MODE1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEL_MODE2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEL_MODE2, self).__init__(register,
            'MODE2', 'GPIO.PF_MODEL.MODE2', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PF_MODEL_MODE2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEL_MODE3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEL_MODE3, self).__init__(register,
            'MODE3', 'GPIO.PF_MODEL.MODE3', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PF_MODEL_MODE3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEL_MODE4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEL_MODE4, self).__init__(register,
            'MODE4', 'GPIO.PF_MODEL.MODE4', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PF_MODEL_MODE4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEL_MODE5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEL_MODE5, self).__init__(register,
            'MODE5', 'GPIO.PF_MODEL.MODE5', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PF_MODEL_MODE5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEL_MODE6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEL_MODE6, self).__init__(register,
            'MODE6', 'GPIO.PF_MODEL.MODE6', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PF_MODEL_MODE6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEL_MODE7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEL_MODE7, self).__init__(register,
            'MODE7', 'GPIO.PF_MODEL.MODE7', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PF_MODEL_MODE7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEH_MODE8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEH_MODE8, self).__init__(register,
            'MODE8', 'GPIO.PF_MODEH.MODE8', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PF_MODEH_MODE8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEH_MODE9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEH_MODE9, self).__init__(register,
            'MODE9', 'GPIO.PF_MODEH.MODE9', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PF_MODEH_MODE9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEH_MODE10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEH_MODE10, self).__init__(register,
            'MODE10', 'GPIO.PF_MODEH.MODE10', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PF_MODEH_MODE10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEH_MODE11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEH_MODE11, self).__init__(register,
            'MODE11', 'GPIO.PF_MODEH.MODE11', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PF_MODEH_MODE11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEH_MODE12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEH_MODE12, self).__init__(register,
            'MODE12', 'GPIO.PF_MODEH.MODE12', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PF_MODEH_MODE12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEH_MODE13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEH_MODE13, self).__init__(register,
            'MODE13', 'GPIO.PF_MODEH.MODE13', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PF_MODEH_MODE13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEH_MODE14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEH_MODE14, self).__init__(register,
            'MODE14', 'GPIO.PF_MODEH.MODE14', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PF_MODEH_MODE14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_MODEH_MODE15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_MODEH_MODE15, self).__init__(register,
            'MODE15', 'GPIO.PF_MODEH.MODE15', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PF_MODEH_MODE15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_DOUT_DOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_DOUT_DOUT, self).__init__(register,
            'DOUT', 'GPIO.PF_DOUT.DOUT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_DOUTTGL_DOUTTGL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_DOUTTGL_DOUTTGL, self).__init__(register,
            'DOUTTGL', 'GPIO.PF_DOUTTGL.DOUTTGL', 'write-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_DIN_DIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_DIN_DIN, self).__init__(register,
            'DIN', 'GPIO.PF_DIN.DIN', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_PINLOCKN_PINLOCKN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_PINLOCKN_PINLOCKN, self).__init__(register,
            'PINLOCKN', 'GPIO.PF_PINLOCKN.PINLOCKN', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PF_TOL5VDIS_TOL5VDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PF_TOL5VDIS_TOL5VDIS, self).__init__(register,
            'TOL5VDIS', 'GPIO.PF_TOL5VDIS.TOL5VDIS', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'GPIO.PG_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_CTRL_SLEWRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_CTRL_SLEWRATE, self).__init__(register,
            'SLEWRATE', 'GPIO.PG_CTRL.SLEWRATE', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_CTRL_DINDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_CTRL_DINDIS, self).__init__(register,
            'DINDIS', 'GPIO.PG_CTRL.DINDIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_CTRL_DRIVESTRENGTHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_CTRL_DRIVESTRENGTHALT, self).__init__(register,
            'DRIVESTRENGTHALT', 'GPIO.PG_CTRL.DRIVESTRENGTHALT', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_CTRL_SLEWRATEALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_CTRL_SLEWRATEALT, self).__init__(register,
            'SLEWRATEALT', 'GPIO.PG_CTRL.SLEWRATEALT', 'read-write',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_CTRL_DINDISALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_CTRL_DINDISALT, self).__init__(register,
            'DINDISALT', 'GPIO.PG_CTRL.DINDISALT', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEL_MODE0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEL_MODE0, self).__init__(register,
            'MODE0', 'GPIO.PG_MODEL.MODE0', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PG_MODEL_MODE0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEL_MODE1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEL_MODE1, self).__init__(register,
            'MODE1', 'GPIO.PG_MODEL.MODE1', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PG_MODEL_MODE1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEL_MODE2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEL_MODE2, self).__init__(register,
            'MODE2', 'GPIO.PG_MODEL.MODE2', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PG_MODEL_MODE2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEL_MODE3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEL_MODE3, self).__init__(register,
            'MODE3', 'GPIO.PG_MODEL.MODE3', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PG_MODEL_MODE3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEL_MODE4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEL_MODE4, self).__init__(register,
            'MODE4', 'GPIO.PG_MODEL.MODE4', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PG_MODEL_MODE4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEL_MODE5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEL_MODE5, self).__init__(register,
            'MODE5', 'GPIO.PG_MODEL.MODE5', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PG_MODEL_MODE5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEL_MODE6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEL_MODE6, self).__init__(register,
            'MODE6', 'GPIO.PG_MODEL.MODE6', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PG_MODEL_MODE6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEL_MODE7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEL_MODE7, self).__init__(register,
            'MODE7', 'GPIO.PG_MODEL.MODE7', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PG_MODEL_MODE7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEH_MODE8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEH_MODE8, self).__init__(register,
            'MODE8', 'GPIO.PG_MODEH.MODE8', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PG_MODEH_MODE8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEH_MODE9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEH_MODE9, self).__init__(register,
            'MODE9', 'GPIO.PG_MODEH.MODE9', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PG_MODEH_MODE9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEH_MODE10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEH_MODE10, self).__init__(register,
            'MODE10', 'GPIO.PG_MODEH.MODE10', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PG_MODEH_MODE10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEH_MODE11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEH_MODE11, self).__init__(register,
            'MODE11', 'GPIO.PG_MODEH.MODE11', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PG_MODEH_MODE11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEH_MODE12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEH_MODE12, self).__init__(register,
            'MODE12', 'GPIO.PG_MODEH.MODE12', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PG_MODEH_MODE12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEH_MODE13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEH_MODE13, self).__init__(register,
            'MODE13', 'GPIO.PG_MODEH.MODE13', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PG_MODEH_MODE13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEH_MODE14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEH_MODE14, self).__init__(register,
            'MODE14', 'GPIO.PG_MODEH.MODE14', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PG_MODEH_MODE14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_MODEH_MODE15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_MODEH_MODE15, self).__init__(register,
            'MODE15', 'GPIO.PG_MODEH.MODE15', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PG_MODEH_MODE15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_DOUT_DOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_DOUT_DOUT, self).__init__(register,
            'DOUT', 'GPIO.PG_DOUT.DOUT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_DOUTTGL_DOUTTGL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_DOUTTGL_DOUTTGL, self).__init__(register,
            'DOUTTGL', 'GPIO.PG_DOUTTGL.DOUTTGL', 'write-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_DIN_DIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_DIN_DIN, self).__init__(register,
            'DIN', 'GPIO.PG_DIN.DIN', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_PINLOCKN_PINLOCKN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_PINLOCKN_PINLOCKN, self).__init__(register,
            'PINLOCKN', 'GPIO.PG_PINLOCKN.PINLOCKN', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PG_TOL5VDIS_TOL5VDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PG_TOL5VDIS_TOL5VDIS, self).__init__(register,
            'TOL5VDIS', 'GPIO.PG_TOL5VDIS.TOL5VDIS', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'GPIO.PH_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_CTRL_SLEWRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_CTRL_SLEWRATE, self).__init__(register,
            'SLEWRATE', 'GPIO.PH_CTRL.SLEWRATE', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_CTRL_DINDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_CTRL_DINDIS, self).__init__(register,
            'DINDIS', 'GPIO.PH_CTRL.DINDIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_CTRL_DRIVESTRENGTHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_CTRL_DRIVESTRENGTHALT, self).__init__(register,
            'DRIVESTRENGTHALT', 'GPIO.PH_CTRL.DRIVESTRENGTHALT', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_CTRL_SLEWRATEALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_CTRL_SLEWRATEALT, self).__init__(register,
            'SLEWRATEALT', 'GPIO.PH_CTRL.SLEWRATEALT', 'read-write',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_CTRL_DINDISALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_CTRL_DINDISALT, self).__init__(register,
            'DINDISALT', 'GPIO.PH_CTRL.DINDISALT', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEL_MODE0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEL_MODE0, self).__init__(register,
            'MODE0', 'GPIO.PH_MODEL.MODE0', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PH_MODEL_MODE0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEL_MODE1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEL_MODE1, self).__init__(register,
            'MODE1', 'GPIO.PH_MODEL.MODE1', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PH_MODEL_MODE1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEL_MODE2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEL_MODE2, self).__init__(register,
            'MODE2', 'GPIO.PH_MODEL.MODE2', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PH_MODEL_MODE2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEL_MODE3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEL_MODE3, self).__init__(register,
            'MODE3', 'GPIO.PH_MODEL.MODE3', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PH_MODEL_MODE3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEL_MODE4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEL_MODE4, self).__init__(register,
            'MODE4', 'GPIO.PH_MODEL.MODE4', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PH_MODEL_MODE4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEL_MODE5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEL_MODE5, self).__init__(register,
            'MODE5', 'GPIO.PH_MODEL.MODE5', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PH_MODEL_MODE5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEL_MODE6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEL_MODE6, self).__init__(register,
            'MODE6', 'GPIO.PH_MODEL.MODE6', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PH_MODEL_MODE6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEL_MODE7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEL_MODE7, self).__init__(register,
            'MODE7', 'GPIO.PH_MODEL.MODE7', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PH_MODEL_MODE7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEH_MODE8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEH_MODE8, self).__init__(register,
            'MODE8', 'GPIO.PH_MODEH.MODE8', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PH_MODEH_MODE8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEH_MODE9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEH_MODE9, self).__init__(register,
            'MODE9', 'GPIO.PH_MODEH.MODE9', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PH_MODEH_MODE9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEH_MODE10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEH_MODE10, self).__init__(register,
            'MODE10', 'GPIO.PH_MODEH.MODE10', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PH_MODEH_MODE10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEH_MODE11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEH_MODE11, self).__init__(register,
            'MODE11', 'GPIO.PH_MODEH.MODE11', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PH_MODEH_MODE11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEH_MODE12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEH_MODE12, self).__init__(register,
            'MODE12', 'GPIO.PH_MODEH.MODE12', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PH_MODEH_MODE12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEH_MODE13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEH_MODE13, self).__init__(register,
            'MODE13', 'GPIO.PH_MODEH.MODE13', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PH_MODEH_MODE13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEH_MODE14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEH_MODE14, self).__init__(register,
            'MODE14', 'GPIO.PH_MODEH.MODE14', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PH_MODEH_MODE14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_MODEH_MODE15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_MODEH_MODE15, self).__init__(register,
            'MODE15', 'GPIO.PH_MODEH.MODE15', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PH_MODEH_MODE15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_DOUT_DOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_DOUT_DOUT, self).__init__(register,
            'DOUT', 'GPIO.PH_DOUT.DOUT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_DOUTTGL_DOUTTGL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_DOUTTGL_DOUTTGL, self).__init__(register,
            'DOUTTGL', 'GPIO.PH_DOUTTGL.DOUTTGL', 'write-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_DIN_DIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_DIN_DIN, self).__init__(register,
            'DIN', 'GPIO.PH_DIN.DIN', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_PINLOCKN_PINLOCKN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_PINLOCKN_PINLOCKN, self).__init__(register,
            'PINLOCKN', 'GPIO.PH_PINLOCKN.PINLOCKN', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PH_TOL5VDIS_TOL5VDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PH_TOL5VDIS_TOL5VDIS, self).__init__(register,
            'TOL5VDIS', 'GPIO.PH_TOL5VDIS.TOL5VDIS', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'GPIO.PI_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_CTRL_SLEWRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_CTRL_SLEWRATE, self).__init__(register,
            'SLEWRATE', 'GPIO.PI_CTRL.SLEWRATE', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_CTRL_DINDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_CTRL_DINDIS, self).__init__(register,
            'DINDIS', 'GPIO.PI_CTRL.DINDIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_CTRL_DRIVESTRENGTHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_CTRL_DRIVESTRENGTHALT, self).__init__(register,
            'DRIVESTRENGTHALT', 'GPIO.PI_CTRL.DRIVESTRENGTHALT', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_CTRL_SLEWRATEALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_CTRL_SLEWRATEALT, self).__init__(register,
            'SLEWRATEALT', 'GPIO.PI_CTRL.SLEWRATEALT', 'read-write',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_CTRL_DINDISALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_CTRL_DINDISALT, self).__init__(register,
            'DINDISALT', 'GPIO.PI_CTRL.DINDISALT', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEL_MODE0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEL_MODE0, self).__init__(register,
            'MODE0', 'GPIO.PI_MODEL.MODE0', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PI_MODEL_MODE0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEL_MODE1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEL_MODE1, self).__init__(register,
            'MODE1', 'GPIO.PI_MODEL.MODE1', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PI_MODEL_MODE1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEL_MODE2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEL_MODE2, self).__init__(register,
            'MODE2', 'GPIO.PI_MODEL.MODE2', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PI_MODEL_MODE2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEL_MODE3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEL_MODE3, self).__init__(register,
            'MODE3', 'GPIO.PI_MODEL.MODE3', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PI_MODEL_MODE3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEL_MODE4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEL_MODE4, self).__init__(register,
            'MODE4', 'GPIO.PI_MODEL.MODE4', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PI_MODEL_MODE4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEL_MODE5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEL_MODE5, self).__init__(register,
            'MODE5', 'GPIO.PI_MODEL.MODE5', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PI_MODEL_MODE5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEL_MODE6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEL_MODE6, self).__init__(register,
            'MODE6', 'GPIO.PI_MODEL.MODE6', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PI_MODEL_MODE6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEL_MODE7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEL_MODE7, self).__init__(register,
            'MODE7', 'GPIO.PI_MODEL.MODE7', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PI_MODEL_MODE7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEH_MODE8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEH_MODE8, self).__init__(register,
            'MODE8', 'GPIO.PI_MODEH.MODE8', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PI_MODEH_MODE8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEH_MODE9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEH_MODE9, self).__init__(register,
            'MODE9', 'GPIO.PI_MODEH.MODE9', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PI_MODEH_MODE9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEH_MODE10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEH_MODE10, self).__init__(register,
            'MODE10', 'GPIO.PI_MODEH.MODE10', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PI_MODEH_MODE10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEH_MODE11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEH_MODE11, self).__init__(register,
            'MODE11', 'GPIO.PI_MODEH.MODE11', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PI_MODEH_MODE11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEH_MODE12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEH_MODE12, self).__init__(register,
            'MODE12', 'GPIO.PI_MODEH.MODE12', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PI_MODEH_MODE12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEH_MODE13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEH_MODE13, self).__init__(register,
            'MODE13', 'GPIO.PI_MODEH.MODE13', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PI_MODEH_MODE13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEH_MODE14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEH_MODE14, self).__init__(register,
            'MODE14', 'GPIO.PI_MODEH.MODE14', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PI_MODEH_MODE14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_MODEH_MODE15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_MODEH_MODE15, self).__init__(register,
            'MODE15', 'GPIO.PI_MODEH.MODE15', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PI_MODEH_MODE15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_DOUT_DOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_DOUT_DOUT, self).__init__(register,
            'DOUT', 'GPIO.PI_DOUT.DOUT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_DOUTTGL_DOUTTGL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_DOUTTGL_DOUTTGL, self).__init__(register,
            'DOUTTGL', 'GPIO.PI_DOUTTGL.DOUTTGL', 'write-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_DIN_DIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_DIN_DIN, self).__init__(register,
            'DIN', 'GPIO.PI_DIN.DIN', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_PINLOCKN_PINLOCKN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_PINLOCKN_PINLOCKN, self).__init__(register,
            'PINLOCKN', 'GPIO.PI_PINLOCKN.PINLOCKN', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PI_TOL5VDIS_TOL5VDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PI_TOL5VDIS_TOL5VDIS, self).__init__(register,
            'TOL5VDIS', 'GPIO.PI_TOL5VDIS.TOL5VDIS', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'GPIO.PJ_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_CTRL_SLEWRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_CTRL_SLEWRATE, self).__init__(register,
            'SLEWRATE', 'GPIO.PJ_CTRL.SLEWRATE', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_CTRL_DINDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_CTRL_DINDIS, self).__init__(register,
            'DINDIS', 'GPIO.PJ_CTRL.DINDIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_CTRL_DRIVESTRENGTHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_CTRL_DRIVESTRENGTHALT, self).__init__(register,
            'DRIVESTRENGTHALT', 'GPIO.PJ_CTRL.DRIVESTRENGTHALT', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_CTRL_SLEWRATEALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_CTRL_SLEWRATEALT, self).__init__(register,
            'SLEWRATEALT', 'GPIO.PJ_CTRL.SLEWRATEALT', 'read-write',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_CTRL_DINDISALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_CTRL_DINDISALT, self).__init__(register,
            'DINDISALT', 'GPIO.PJ_CTRL.DINDISALT', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEL_MODE0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEL_MODE0, self).__init__(register,
            'MODE0', 'GPIO.PJ_MODEL.MODE0', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PJ_MODEL_MODE0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEL_MODE1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEL_MODE1, self).__init__(register,
            'MODE1', 'GPIO.PJ_MODEL.MODE1', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PJ_MODEL_MODE1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEL_MODE2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEL_MODE2, self).__init__(register,
            'MODE2', 'GPIO.PJ_MODEL.MODE2', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PJ_MODEL_MODE2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEL_MODE3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEL_MODE3, self).__init__(register,
            'MODE3', 'GPIO.PJ_MODEL.MODE3', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PJ_MODEL_MODE3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEL_MODE4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEL_MODE4, self).__init__(register,
            'MODE4', 'GPIO.PJ_MODEL.MODE4', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PJ_MODEL_MODE4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEL_MODE5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEL_MODE5, self).__init__(register,
            'MODE5', 'GPIO.PJ_MODEL.MODE5', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PJ_MODEL_MODE5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEL_MODE6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEL_MODE6, self).__init__(register,
            'MODE6', 'GPIO.PJ_MODEL.MODE6', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PJ_MODEL_MODE6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEL_MODE7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEL_MODE7, self).__init__(register,
            'MODE7', 'GPIO.PJ_MODEL.MODE7', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PJ_MODEL_MODE7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEH_MODE8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEH_MODE8, self).__init__(register,
            'MODE8', 'GPIO.PJ_MODEH.MODE8', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PJ_MODEH_MODE8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEH_MODE9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEH_MODE9, self).__init__(register,
            'MODE9', 'GPIO.PJ_MODEH.MODE9', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PJ_MODEH_MODE9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEH_MODE10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEH_MODE10, self).__init__(register,
            'MODE10', 'GPIO.PJ_MODEH.MODE10', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PJ_MODEH_MODE10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEH_MODE11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEH_MODE11, self).__init__(register,
            'MODE11', 'GPIO.PJ_MODEH.MODE11', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PJ_MODEH_MODE11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEH_MODE12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEH_MODE12, self).__init__(register,
            'MODE12', 'GPIO.PJ_MODEH.MODE12', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PJ_MODEH_MODE12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEH_MODE13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEH_MODE13, self).__init__(register,
            'MODE13', 'GPIO.PJ_MODEH.MODE13', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PJ_MODEH_MODE13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEH_MODE14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEH_MODE14, self).__init__(register,
            'MODE14', 'GPIO.PJ_MODEH.MODE14', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PJ_MODEH_MODE14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_MODEH_MODE15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_MODEH_MODE15, self).__init__(register,
            'MODE15', 'GPIO.PJ_MODEH.MODE15', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PJ_MODEH_MODE15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_DOUT_DOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_DOUT_DOUT, self).__init__(register,
            'DOUT', 'GPIO.PJ_DOUT.DOUT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_DOUTTGL_DOUTTGL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_DOUTTGL_DOUTTGL, self).__init__(register,
            'DOUTTGL', 'GPIO.PJ_DOUTTGL.DOUTTGL', 'write-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_DIN_DIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_DIN_DIN, self).__init__(register,
            'DIN', 'GPIO.PJ_DIN.DIN', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_PINLOCKN_PINLOCKN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_PINLOCKN_PINLOCKN, self).__init__(register,
            'PINLOCKN', 'GPIO.PJ_PINLOCKN.PINLOCKN', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PJ_TOL5VDIS_TOL5VDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PJ_TOL5VDIS_TOL5VDIS, self).__init__(register,
            'TOL5VDIS', 'GPIO.PJ_TOL5VDIS.TOL5VDIS', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'GPIO.PK_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_CTRL_SLEWRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_CTRL_SLEWRATE, self).__init__(register,
            'SLEWRATE', 'GPIO.PK_CTRL.SLEWRATE', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_CTRL_DINDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_CTRL_DINDIS, self).__init__(register,
            'DINDIS', 'GPIO.PK_CTRL.DINDIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_CTRL_DRIVESTRENGTHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_CTRL_DRIVESTRENGTHALT, self).__init__(register,
            'DRIVESTRENGTHALT', 'GPIO.PK_CTRL.DRIVESTRENGTHALT', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_CTRL_SLEWRATEALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_CTRL_SLEWRATEALT, self).__init__(register,
            'SLEWRATEALT', 'GPIO.PK_CTRL.SLEWRATEALT', 'read-write',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_CTRL_DINDISALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_CTRL_DINDISALT, self).__init__(register,
            'DINDISALT', 'GPIO.PK_CTRL.DINDISALT', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEL_MODE0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEL_MODE0, self).__init__(register,
            'MODE0', 'GPIO.PK_MODEL.MODE0', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PK_MODEL_MODE0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEL_MODE1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEL_MODE1, self).__init__(register,
            'MODE1', 'GPIO.PK_MODEL.MODE1', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PK_MODEL_MODE1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEL_MODE2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEL_MODE2, self).__init__(register,
            'MODE2', 'GPIO.PK_MODEL.MODE2', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PK_MODEL_MODE2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEL_MODE3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEL_MODE3, self).__init__(register,
            'MODE3', 'GPIO.PK_MODEL.MODE3', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PK_MODEL_MODE3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEL_MODE4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEL_MODE4, self).__init__(register,
            'MODE4', 'GPIO.PK_MODEL.MODE4', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PK_MODEL_MODE4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEL_MODE5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEL_MODE5, self).__init__(register,
            'MODE5', 'GPIO.PK_MODEL.MODE5', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PK_MODEL_MODE5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEL_MODE6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEL_MODE6, self).__init__(register,
            'MODE6', 'GPIO.PK_MODEL.MODE6', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PK_MODEL_MODE6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEL_MODE7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEL_MODE7, self).__init__(register,
            'MODE7', 'GPIO.PK_MODEL.MODE7', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PK_MODEL_MODE7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEH_MODE8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEH_MODE8, self).__init__(register,
            'MODE8', 'GPIO.PK_MODEH.MODE8', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PK_MODEH_MODE8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEH_MODE9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEH_MODE9, self).__init__(register,
            'MODE9', 'GPIO.PK_MODEH.MODE9', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PK_MODEH_MODE9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEH_MODE10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEH_MODE10, self).__init__(register,
            'MODE10', 'GPIO.PK_MODEH.MODE10', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PK_MODEH_MODE10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEH_MODE11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEH_MODE11, self).__init__(register,
            'MODE11', 'GPIO.PK_MODEH.MODE11', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PK_MODEH_MODE11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEH_MODE12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEH_MODE12, self).__init__(register,
            'MODE12', 'GPIO.PK_MODEH.MODE12', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PK_MODEH_MODE12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEH_MODE13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEH_MODE13, self).__init__(register,
            'MODE13', 'GPIO.PK_MODEH.MODE13', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PK_MODEH_MODE13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEH_MODE14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEH_MODE14, self).__init__(register,
            'MODE14', 'GPIO.PK_MODEH.MODE14', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PK_MODEH_MODE14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_MODEH_MODE15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_MODEH_MODE15, self).__init__(register,
            'MODE15', 'GPIO.PK_MODEH.MODE15', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PK_MODEH_MODE15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_DOUT_DOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_DOUT_DOUT, self).__init__(register,
            'DOUT', 'GPIO.PK_DOUT.DOUT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_DOUTTGL_DOUTTGL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_DOUTTGL_DOUTTGL, self).__init__(register,
            'DOUTTGL', 'GPIO.PK_DOUTTGL.DOUTTGL', 'write-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_DIN_DIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_DIN_DIN, self).__init__(register,
            'DIN', 'GPIO.PK_DIN.DIN', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_PINLOCKN_PINLOCKN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_PINLOCKN_PINLOCKN, self).__init__(register,
            'PINLOCKN', 'GPIO.PK_PINLOCKN.PINLOCKN', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PK_TOL5VDIS_TOL5VDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PK_TOL5VDIS_TOL5VDIS, self).__init__(register,
            'TOL5VDIS', 'GPIO.PK_TOL5VDIS.TOL5VDIS', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_CTRL_DRIVESTRENGTH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_CTRL_DRIVESTRENGTH, self).__init__(register,
            'DRIVESTRENGTH', 'GPIO.PL_CTRL.DRIVESTRENGTH', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_CTRL_SLEWRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_CTRL_SLEWRATE, self).__init__(register,
            'SLEWRATE', 'GPIO.PL_CTRL.SLEWRATE', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_CTRL_DINDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_CTRL_DINDIS, self).__init__(register,
            'DINDIS', 'GPIO.PL_CTRL.DINDIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_CTRL_DRIVESTRENGTHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_CTRL_DRIVESTRENGTHALT, self).__init__(register,
            'DRIVESTRENGTHALT', 'GPIO.PL_CTRL.DRIVESTRENGTHALT', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_CTRL_SLEWRATEALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_CTRL_SLEWRATEALT, self).__init__(register,
            'SLEWRATEALT', 'GPIO.PL_CTRL.SLEWRATEALT', 'read-write',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_CTRL_DINDISALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_CTRL_DINDISALT, self).__init__(register,
            'DINDISALT', 'GPIO.PL_CTRL.DINDISALT', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEL_MODE0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEL_MODE0, self).__init__(register,
            'MODE0', 'GPIO.PL_MODEL.MODE0', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PL_MODEL_MODE0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEL_MODE1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEL_MODE1, self).__init__(register,
            'MODE1', 'GPIO.PL_MODEL.MODE1', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PL_MODEL_MODE1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEL_MODE2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEL_MODE2, self).__init__(register,
            'MODE2', 'GPIO.PL_MODEL.MODE2', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PL_MODEL_MODE2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEL_MODE3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEL_MODE3, self).__init__(register,
            'MODE3', 'GPIO.PL_MODEL.MODE3', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PL_MODEL_MODE3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEL_MODE4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEL_MODE4, self).__init__(register,
            'MODE4', 'GPIO.PL_MODEL.MODE4', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PL_MODEL_MODE4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEL_MODE5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEL_MODE5, self).__init__(register,
            'MODE5', 'GPIO.PL_MODEL.MODE5', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PL_MODEL_MODE5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEL_MODE6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEL_MODE6, self).__init__(register,
            'MODE6', 'GPIO.PL_MODEL.MODE6', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PL_MODEL_MODE6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEL_MODE7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEL_MODE7, self).__init__(register,
            'MODE7', 'GPIO.PL_MODEL.MODE7', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PL_MODEL_MODE7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEH_MODE8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEH_MODE8, self).__init__(register,
            'MODE8', 'GPIO.PL_MODEH.MODE8', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_PL_MODEH_MODE8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEH_MODE9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEH_MODE9, self).__init__(register,
            'MODE9', 'GPIO.PL_MODEH.MODE9', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_PL_MODEH_MODE9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEH_MODE10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEH_MODE10, self).__init__(register,
            'MODE10', 'GPIO.PL_MODEH.MODE10', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_PL_MODEH_MODE10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEH_MODE11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEH_MODE11, self).__init__(register,
            'MODE11', 'GPIO.PL_MODEH.MODE11', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_PL_MODEH_MODE11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEH_MODE12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEH_MODE12, self).__init__(register,
            'MODE12', 'GPIO.PL_MODEH.MODE12', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_PL_MODEH_MODE12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEH_MODE13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEH_MODE13, self).__init__(register,
            'MODE13', 'GPIO.PL_MODEH.MODE13', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_PL_MODEH_MODE13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEH_MODE14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEH_MODE14, self).__init__(register,
            'MODE14', 'GPIO.PL_MODEH.MODE14', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_PL_MODEH_MODE14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_MODEH_MODE15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_MODEH_MODE15, self).__init__(register,
            'MODE15', 'GPIO.PL_MODEH.MODE15', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_PL_MODEH_MODE15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_DOUT_DOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_DOUT_DOUT, self).__init__(register,
            'DOUT', 'GPIO.PL_DOUT.DOUT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_DOUTTGL_DOUTTGL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_DOUTTGL_DOUTTGL, self).__init__(register,
            'DOUTTGL', 'GPIO.PL_DOUTTGL.DOUTTGL', 'write-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_DIN_DIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_DIN_DIN, self).__init__(register,
            'DIN', 'GPIO.PL_DIN.DIN', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_PINLOCKN_PINLOCKN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_PINLOCKN_PINLOCKN, self).__init__(register,
            'PINLOCKN', 'GPIO.PL_PINLOCKN.PINLOCKN', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_PL_TOL5VDIS_TOL5VDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_PL_TOL5VDIS_TOL5VDIS, self).__init__(register,
            'TOL5VDIS', 'GPIO.PL_TOL5VDIS.TOL5VDIS', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELL_EXTIPSEL0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELL_EXTIPSEL0, self).__init__(register,
            'EXTIPSEL0', 'GPIO.EXTIPSELL.EXTIPSEL0', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_EXTIPSELL_EXTIPSEL0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELL_EXTIPSEL1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELL_EXTIPSEL1, self).__init__(register,
            'EXTIPSEL1', 'GPIO.EXTIPSELL.EXTIPSEL1', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_EXTIPSELL_EXTIPSEL1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELL_EXTIPSEL2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELL_EXTIPSEL2, self).__init__(register,
            'EXTIPSEL2', 'GPIO.EXTIPSELL.EXTIPSEL2', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_EXTIPSELL_EXTIPSEL2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELL_EXTIPSEL3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELL_EXTIPSEL3, self).__init__(register,
            'EXTIPSEL3', 'GPIO.EXTIPSELL.EXTIPSEL3', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_EXTIPSELL_EXTIPSEL3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELL_EXTIPSEL4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELL_EXTIPSEL4, self).__init__(register,
            'EXTIPSEL4', 'GPIO.EXTIPSELL.EXTIPSEL4', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_EXTIPSELL_EXTIPSEL4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELL_EXTIPSEL5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELL_EXTIPSEL5, self).__init__(register,
            'EXTIPSEL5', 'GPIO.EXTIPSELL.EXTIPSEL5', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_EXTIPSELL_EXTIPSEL5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELL_EXTIPSEL6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELL_EXTIPSEL6, self).__init__(register,
            'EXTIPSEL6', 'GPIO.EXTIPSELL.EXTIPSEL6', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_EXTIPSELL_EXTIPSEL6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELL_EXTIPSEL7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELL_EXTIPSEL7, self).__init__(register,
            'EXTIPSEL7', 'GPIO.EXTIPSELL.EXTIPSEL7', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_EXTIPSELL_EXTIPSEL7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELH_EXTIPSEL8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELH_EXTIPSEL8, self).__init__(register,
            'EXTIPSEL8', 'GPIO.EXTIPSELH.EXTIPSEL8', 'read-write',
            "",
            0, 4,
            RM_Enum_GPIO_EXTIPSELH_EXTIPSEL8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELH_EXTIPSEL9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELH_EXTIPSEL9, self).__init__(register,
            'EXTIPSEL9', 'GPIO.EXTIPSELH.EXTIPSEL9', 'read-write',
            "",
            4, 4,
            RM_Enum_GPIO_EXTIPSELH_EXTIPSEL9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELH_EXTIPSEL10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELH_EXTIPSEL10, self).__init__(register,
            'EXTIPSEL10', 'GPIO.EXTIPSELH.EXTIPSEL10', 'read-write',
            "",
            8, 4,
            RM_Enum_GPIO_EXTIPSELH_EXTIPSEL10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELH_EXTIPSEL11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELH_EXTIPSEL11, self).__init__(register,
            'EXTIPSEL11', 'GPIO.EXTIPSELH.EXTIPSEL11', 'read-write',
            "",
            12, 4,
            RM_Enum_GPIO_EXTIPSELH_EXTIPSEL11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELH_EXTIPSEL12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELH_EXTIPSEL12, self).__init__(register,
            'EXTIPSEL12', 'GPIO.EXTIPSELH.EXTIPSEL12', 'read-write',
            "",
            16, 4,
            RM_Enum_GPIO_EXTIPSELH_EXTIPSEL12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELH_EXTIPSEL13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELH_EXTIPSEL13, self).__init__(register,
            'EXTIPSEL13', 'GPIO.EXTIPSELH.EXTIPSEL13', 'read-write',
            "",
            20, 4,
            RM_Enum_GPIO_EXTIPSELH_EXTIPSEL13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELH_EXTIPSEL14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELH_EXTIPSEL14, self).__init__(register,
            'EXTIPSEL14', 'GPIO.EXTIPSELH.EXTIPSEL14', 'read-write',
            "",
            24, 4,
            RM_Enum_GPIO_EXTIPSELH_EXTIPSEL14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIPSELH_EXTIPSEL15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIPSELH_EXTIPSEL15, self).__init__(register,
            'EXTIPSEL15', 'GPIO.EXTIPSELH.EXTIPSEL15', 'read-write',
            "",
            28, 4,
            RM_Enum_GPIO_EXTIPSELH_EXTIPSEL15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELL_EXTIGSEL0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELL_EXTIGSEL0, self).__init__(register,
            'EXTIGSEL0', 'GPIO.EXTIGSELL.EXTIGSEL0', 'read-write',
            "",
            0, 2,
            RM_Enum_GPIO_EXTIGSELL_EXTIGSEL0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELL_EXTIGSEL1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELL_EXTIGSEL1, self).__init__(register,
            'EXTIGSEL1', 'GPIO.EXTIGSELL.EXTIGSEL1', 'read-write',
            "",
            4, 2,
            RM_Enum_GPIO_EXTIGSELL_EXTIGSEL1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELL_EXTIGSEL2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELL_EXTIGSEL2, self).__init__(register,
            'EXTIGSEL2', 'GPIO.EXTIGSELL.EXTIGSEL2', 'read-write',
            "",
            8, 2,
            RM_Enum_GPIO_EXTIGSELL_EXTIGSEL2(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELL_EXTIGSEL3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELL_EXTIGSEL3, self).__init__(register,
            'EXTIGSEL3', 'GPIO.EXTIGSELL.EXTIGSEL3', 'read-write',
            "",
            12, 2,
            RM_Enum_GPIO_EXTIGSELL_EXTIGSEL3(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELL_EXTIGSEL4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELL_EXTIGSEL4, self).__init__(register,
            'EXTIGSEL4', 'GPIO.EXTIGSELL.EXTIGSEL4', 'read-write',
            "",
            16, 2,
            RM_Enum_GPIO_EXTIGSELL_EXTIGSEL4(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELL_EXTIGSEL5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELL_EXTIGSEL5, self).__init__(register,
            'EXTIGSEL5', 'GPIO.EXTIGSELL.EXTIGSEL5', 'read-write',
            "",
            20, 2,
            RM_Enum_GPIO_EXTIGSELL_EXTIGSEL5(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELL_EXTIGSEL6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELL_EXTIGSEL6, self).__init__(register,
            'EXTIGSEL6', 'GPIO.EXTIGSELL.EXTIGSEL6', 'read-write',
            "",
            24, 2,
            RM_Enum_GPIO_EXTIGSELL_EXTIGSEL6(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELL_EXTIGSEL7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELL_EXTIGSEL7, self).__init__(register,
            'EXTIGSEL7', 'GPIO.EXTIGSELL.EXTIGSEL7', 'read-write',
            "",
            28, 2,
            RM_Enum_GPIO_EXTIGSELL_EXTIGSEL7(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELH_EXTIGSEL8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELH_EXTIGSEL8, self).__init__(register,
            'EXTIGSEL8', 'GPIO.EXTIGSELH.EXTIGSEL8', 'read-write',
            "",
            0, 2,
            RM_Enum_GPIO_EXTIGSELH_EXTIGSEL8(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELH_EXTIGSEL9(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELH_EXTIGSEL9, self).__init__(register,
            'EXTIGSEL9', 'GPIO.EXTIGSELH.EXTIGSEL9', 'read-write',
            "",
            4, 2,
            RM_Enum_GPIO_EXTIGSELH_EXTIGSEL9(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELH_EXTIGSEL10(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELH_EXTIGSEL10, self).__init__(register,
            'EXTIGSEL10', 'GPIO.EXTIGSELH.EXTIGSEL10', 'read-write',
            "",
            8, 2,
            RM_Enum_GPIO_EXTIGSELH_EXTIGSEL10(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELH_EXTIGSEL11(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELH_EXTIGSEL11, self).__init__(register,
            'EXTIGSEL11', 'GPIO.EXTIGSELH.EXTIGSEL11', 'read-write',
            "",
            12, 2,
            RM_Enum_GPIO_EXTIGSELH_EXTIGSEL11(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELH_EXTIGSEL12(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELH_EXTIGSEL12, self).__init__(register,
            'EXTIGSEL12', 'GPIO.EXTIGSELH.EXTIGSEL12', 'read-write',
            "",
            16, 2,
            RM_Enum_GPIO_EXTIGSELH_EXTIGSEL12(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELH_EXTIGSEL13(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELH_EXTIGSEL13, self).__init__(register,
            'EXTIGSEL13', 'GPIO.EXTIGSELH.EXTIGSEL13', 'read-write',
            "",
            20, 2,
            RM_Enum_GPIO_EXTIGSELH_EXTIGSEL13(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELH_EXTIGSEL14(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELH_EXTIGSEL14, self).__init__(register,
            'EXTIGSEL14', 'GPIO.EXTIGSELH.EXTIGSEL14', 'read-write',
            "",
            24, 2,
            RM_Enum_GPIO_EXTIGSELH_EXTIGSEL14(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIGSELH_EXTIGSEL15(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIGSELH_EXTIGSEL15, self).__init__(register,
            'EXTIGSEL15', 'GPIO.EXTIGSELH.EXTIGSEL15', 'read-write',
            "",
            28, 2,
            RM_Enum_GPIO_EXTIGSELH_EXTIGSEL15(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIRISE_EXTIRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIRISE_EXTIRISE, self).__init__(register,
            'EXTIRISE', 'GPIO.EXTIRISE.EXTIRISE', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTIFALL_EXTIFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTIFALL_EXTIFALL, self).__init__(register,
            'EXTIFALL', 'GPIO.EXTIFALL.EXTIFALL', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EXTILEVEL_EM4WULEVEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EXTILEVEL_EM4WULEVEL, self).__init__(register,
            'EM4WULEVEL', 'GPIO.EXTILEVEL.EM4WULEVEL', 'read-write',
            "",
            16, 6,
            RM_Enum_GPIO_EXTILEVEL_EM4WULEVEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_IF_EXT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_IF_EXT, self).__init__(register,
            'EXT', 'GPIO.IF.EXT', 'read-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_IF_EM4WU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_IF_EM4WU, self).__init__(register,
            'EM4WU', 'GPIO.IF.EM4WU', 'read-only',
            "",
            16, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_IFS_EXT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_IFS_EXT, self).__init__(register,
            'EXT', 'GPIO.IFS.EXT', 'write-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_IFS_EM4WU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_IFS_EM4WU, self).__init__(register,
            'EM4WU', 'GPIO.IFS.EM4WU', 'write-only',
            "",
            16, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_IFC_EXT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_IFC_EXT, self).__init__(register,
            'EXT', 'GPIO.IFC.EXT', 'write-only',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_IFC_EM4WU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_IFC_EM4WU, self).__init__(register,
            'EM4WU', 'GPIO.IFC.EM4WU', 'write-only',
            "",
            16, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_IEN_EXT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_IEN_EXT, self).__init__(register,
            'EXT', 'GPIO.IEN.EXT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_IEN_EM4WU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_IEN_EM4WU, self).__init__(register,
            'EM4WU', 'GPIO.IEN.EM4WU', 'read-write',
            "",
            16, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_EM4WUEN_EM4WUEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_EM4WUEN_EM4WUEN, self).__init__(register,
            'EM4WUEN', 'GPIO.EM4WUEN.EM4WUEN', 'read-write',
            "",
            16, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_ROUTEPEN_SWCLKTCKPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_ROUTEPEN_SWCLKTCKPEN, self).__init__(register,
            'SWCLKTCKPEN', 'GPIO.ROUTEPEN.SWCLKTCKPEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_ROUTEPEN_SWDIOTMSPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_ROUTEPEN_SWDIOTMSPEN, self).__init__(register,
            'SWDIOTMSPEN', 'GPIO.ROUTEPEN.SWDIOTMSPEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_ROUTEPEN_TDOPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_ROUTEPEN_TDOPEN, self).__init__(register,
            'TDOPEN', 'GPIO.ROUTEPEN.TDOPEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_ROUTEPEN_TDIPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_ROUTEPEN_TDIPEN, self).__init__(register,
            'TDIPEN', 'GPIO.ROUTEPEN.TDIPEN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_ROUTEPEN_SWVPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_ROUTEPEN_SWVPEN, self).__init__(register,
            'SWVPEN', 'GPIO.ROUTEPEN.SWVPEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_ROUTELOC0_SWVLOC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_ROUTELOC0_SWVLOC, self).__init__(register,
            'SWVLOC', 'GPIO.ROUTELOC0.SWVLOC', 'read-write',
            "",
            0, 2,
            RM_Enum_GPIO_ROUTELOC0_SWVLOC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_INSENSE_INT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_INSENSE_INT, self).__init__(register,
            'INT', 'GPIO.INSENSE.INT', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_INSENSE_EM4WU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_INSENSE_EM4WU, self).__init__(register,
            'EM4WU', 'GPIO.INSENSE.EM4WU', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_GPIO_LOCK_LOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_GPIO_LOCK_LOCKKEY, self).__init__(register,
            'LOCKKEY', 'GPIO.LOCK.LOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_GPIO_LOCK_LOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


