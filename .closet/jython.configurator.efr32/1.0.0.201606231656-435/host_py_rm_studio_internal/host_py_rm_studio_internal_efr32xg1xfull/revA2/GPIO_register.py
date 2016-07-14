
from static import Base_RM_Register
from GPIO_field import *


class RM_Register_GPIO_PA_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PA_CTRL, self).__init__(rmio, label,
            0x4000a000, 0x000,
            'PA_CTRL', 'GPIO.PA_CTRL', 'read-write',
            "",
            0x00600060, 0x10711071)

        self.DRIVESTRENGTH = RM_Field_GPIO_PA_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.SLEWRATE = RM_Field_GPIO_PA_CTRL_SLEWRATE(self)
        self.zz_fdict['SLEWRATE'] = self.SLEWRATE
        self.DINDIS = RM_Field_GPIO_PA_CTRL_DINDIS(self)
        self.zz_fdict['DINDIS'] = self.DINDIS
        self.DRIVESTRENGTHALT = RM_Field_GPIO_PA_CTRL_DRIVESTRENGTHALT(self)
        self.zz_fdict['DRIVESTRENGTHALT'] = self.DRIVESTRENGTHALT
        self.SLEWRATEALT = RM_Field_GPIO_PA_CTRL_SLEWRATEALT(self)
        self.zz_fdict['SLEWRATEALT'] = self.SLEWRATEALT
        self.DINDISALT = RM_Field_GPIO_PA_CTRL_DINDISALT(self)
        self.zz_fdict['DINDISALT'] = self.DINDISALT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PA_MODEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PA_MODEL, self).__init__(rmio, label,
            0x4000a000, 0x004,
            'PA_MODEL', 'GPIO.PA_MODEL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE0 = RM_Field_GPIO_PA_MODEL_MODE0(self)
        self.zz_fdict['MODE0'] = self.MODE0
        self.MODE1 = RM_Field_GPIO_PA_MODEL_MODE1(self)
        self.zz_fdict['MODE1'] = self.MODE1
        self.MODE2 = RM_Field_GPIO_PA_MODEL_MODE2(self)
        self.zz_fdict['MODE2'] = self.MODE2
        self.MODE3 = RM_Field_GPIO_PA_MODEL_MODE3(self)
        self.zz_fdict['MODE3'] = self.MODE3
        self.MODE4 = RM_Field_GPIO_PA_MODEL_MODE4(self)
        self.zz_fdict['MODE4'] = self.MODE4
        self.MODE5 = RM_Field_GPIO_PA_MODEL_MODE5(self)
        self.zz_fdict['MODE5'] = self.MODE5
        self.MODE6 = RM_Field_GPIO_PA_MODEL_MODE6(self)
        self.zz_fdict['MODE6'] = self.MODE6
        self.MODE7 = RM_Field_GPIO_PA_MODEL_MODE7(self)
        self.zz_fdict['MODE7'] = self.MODE7
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PA_MODEH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PA_MODEH, self).__init__(rmio, label,
            0x4000a000, 0x008,
            'PA_MODEH', 'GPIO.PA_MODEH', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE8 = RM_Field_GPIO_PA_MODEH_MODE8(self)
        self.zz_fdict['MODE8'] = self.MODE8
        self.MODE9 = RM_Field_GPIO_PA_MODEH_MODE9(self)
        self.zz_fdict['MODE9'] = self.MODE9
        self.MODE10 = RM_Field_GPIO_PA_MODEH_MODE10(self)
        self.zz_fdict['MODE10'] = self.MODE10
        self.MODE11 = RM_Field_GPIO_PA_MODEH_MODE11(self)
        self.zz_fdict['MODE11'] = self.MODE11
        self.MODE12 = RM_Field_GPIO_PA_MODEH_MODE12(self)
        self.zz_fdict['MODE12'] = self.MODE12
        self.MODE13 = RM_Field_GPIO_PA_MODEH_MODE13(self)
        self.zz_fdict['MODE13'] = self.MODE13
        self.MODE14 = RM_Field_GPIO_PA_MODEH_MODE14(self)
        self.zz_fdict['MODE14'] = self.MODE14
        self.MODE15 = RM_Field_GPIO_PA_MODEH_MODE15(self)
        self.zz_fdict['MODE15'] = self.MODE15
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PA_DOUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PA_DOUT, self).__init__(rmio, label,
            0x4000a000, 0x00C,
            'PA_DOUT', 'GPIO.PA_DOUT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUT = RM_Field_GPIO_PA_DOUT_DOUT(self)
        self.zz_fdict['DOUT'] = self.DOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PA_DOUTTGL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PA_DOUTTGL, self).__init__(rmio, label,
            0x4000a000, 0x018,
            'PA_DOUTTGL', 'GPIO.PA_DOUTTGL', 'write-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUTTGL = RM_Field_GPIO_PA_DOUTTGL_DOUTTGL(self)
        self.zz_fdict['DOUTTGL'] = self.DOUTTGL
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PA_DIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PA_DIN, self).__init__(rmio, label,
            0x4000a000, 0x01C,
            'PA_DIN', 'GPIO.PA_DIN', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DIN = RM_Field_GPIO_PA_DIN_DIN(self)
        self.zz_fdict['DIN'] = self.DIN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PA_PINLOCKN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PA_PINLOCKN, self).__init__(rmio, label,
            0x4000a000, 0x020,
            'PA_PINLOCKN', 'GPIO.PA_PINLOCKN', 'read-write',
            "",
            0x0000FFFF, 0x0000FFFF)

        self.PINLOCKN = RM_Field_GPIO_PA_PINLOCKN_PINLOCKN(self)
        self.zz_fdict['PINLOCKN'] = self.PINLOCKN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PA_TOL5VDIS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PA_TOL5VDIS, self).__init__(rmio, label,
            0x4000a000, 0x028,
            'PA_TOL5VDIS', 'GPIO.PA_TOL5VDIS', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TOL5VDIS = RM_Field_GPIO_PA_TOL5VDIS_TOL5VDIS(self)
        self.zz_fdict['TOL5VDIS'] = self.TOL5VDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PB_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PB_CTRL, self).__init__(rmio, label,
            0x4000a000, 0x030,
            'PB_CTRL', 'GPIO.PB_CTRL', 'read-write',
            "",
            0x00600060, 0x10711071)

        self.DRIVESTRENGTH = RM_Field_GPIO_PB_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.SLEWRATE = RM_Field_GPIO_PB_CTRL_SLEWRATE(self)
        self.zz_fdict['SLEWRATE'] = self.SLEWRATE
        self.DINDIS = RM_Field_GPIO_PB_CTRL_DINDIS(self)
        self.zz_fdict['DINDIS'] = self.DINDIS
        self.DRIVESTRENGTHALT = RM_Field_GPIO_PB_CTRL_DRIVESTRENGTHALT(self)
        self.zz_fdict['DRIVESTRENGTHALT'] = self.DRIVESTRENGTHALT
        self.SLEWRATEALT = RM_Field_GPIO_PB_CTRL_SLEWRATEALT(self)
        self.zz_fdict['SLEWRATEALT'] = self.SLEWRATEALT
        self.DINDISALT = RM_Field_GPIO_PB_CTRL_DINDISALT(self)
        self.zz_fdict['DINDISALT'] = self.DINDISALT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PB_MODEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PB_MODEL, self).__init__(rmio, label,
            0x4000a000, 0x034,
            'PB_MODEL', 'GPIO.PB_MODEL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE0 = RM_Field_GPIO_PB_MODEL_MODE0(self)
        self.zz_fdict['MODE0'] = self.MODE0
        self.MODE1 = RM_Field_GPIO_PB_MODEL_MODE1(self)
        self.zz_fdict['MODE1'] = self.MODE1
        self.MODE2 = RM_Field_GPIO_PB_MODEL_MODE2(self)
        self.zz_fdict['MODE2'] = self.MODE2
        self.MODE3 = RM_Field_GPIO_PB_MODEL_MODE3(self)
        self.zz_fdict['MODE3'] = self.MODE3
        self.MODE4 = RM_Field_GPIO_PB_MODEL_MODE4(self)
        self.zz_fdict['MODE4'] = self.MODE4
        self.MODE5 = RM_Field_GPIO_PB_MODEL_MODE5(self)
        self.zz_fdict['MODE5'] = self.MODE5
        self.MODE6 = RM_Field_GPIO_PB_MODEL_MODE6(self)
        self.zz_fdict['MODE6'] = self.MODE6
        self.MODE7 = RM_Field_GPIO_PB_MODEL_MODE7(self)
        self.zz_fdict['MODE7'] = self.MODE7
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PB_MODEH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PB_MODEH, self).__init__(rmio, label,
            0x4000a000, 0x038,
            'PB_MODEH', 'GPIO.PB_MODEH', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE8 = RM_Field_GPIO_PB_MODEH_MODE8(self)
        self.zz_fdict['MODE8'] = self.MODE8
        self.MODE9 = RM_Field_GPIO_PB_MODEH_MODE9(self)
        self.zz_fdict['MODE9'] = self.MODE9
        self.MODE10 = RM_Field_GPIO_PB_MODEH_MODE10(self)
        self.zz_fdict['MODE10'] = self.MODE10
        self.MODE11 = RM_Field_GPIO_PB_MODEH_MODE11(self)
        self.zz_fdict['MODE11'] = self.MODE11
        self.MODE12 = RM_Field_GPIO_PB_MODEH_MODE12(self)
        self.zz_fdict['MODE12'] = self.MODE12
        self.MODE13 = RM_Field_GPIO_PB_MODEH_MODE13(self)
        self.zz_fdict['MODE13'] = self.MODE13
        self.MODE14 = RM_Field_GPIO_PB_MODEH_MODE14(self)
        self.zz_fdict['MODE14'] = self.MODE14
        self.MODE15 = RM_Field_GPIO_PB_MODEH_MODE15(self)
        self.zz_fdict['MODE15'] = self.MODE15
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PB_DOUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PB_DOUT, self).__init__(rmio, label,
            0x4000a000, 0x03C,
            'PB_DOUT', 'GPIO.PB_DOUT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUT = RM_Field_GPIO_PB_DOUT_DOUT(self)
        self.zz_fdict['DOUT'] = self.DOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PB_DOUTTGL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PB_DOUTTGL, self).__init__(rmio, label,
            0x4000a000, 0x048,
            'PB_DOUTTGL', 'GPIO.PB_DOUTTGL', 'write-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUTTGL = RM_Field_GPIO_PB_DOUTTGL_DOUTTGL(self)
        self.zz_fdict['DOUTTGL'] = self.DOUTTGL
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PB_DIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PB_DIN, self).__init__(rmio, label,
            0x4000a000, 0x04C,
            'PB_DIN', 'GPIO.PB_DIN', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DIN = RM_Field_GPIO_PB_DIN_DIN(self)
        self.zz_fdict['DIN'] = self.DIN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PB_PINLOCKN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PB_PINLOCKN, self).__init__(rmio, label,
            0x4000a000, 0x050,
            'PB_PINLOCKN', 'GPIO.PB_PINLOCKN', 'read-write',
            "",
            0x0000FFFF, 0x0000FFFF)

        self.PINLOCKN = RM_Field_GPIO_PB_PINLOCKN_PINLOCKN(self)
        self.zz_fdict['PINLOCKN'] = self.PINLOCKN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PB_TOL5VDIS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PB_TOL5VDIS, self).__init__(rmio, label,
            0x4000a000, 0x058,
            'PB_TOL5VDIS', 'GPIO.PB_TOL5VDIS', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TOL5VDIS = RM_Field_GPIO_PB_TOL5VDIS_TOL5VDIS(self)
        self.zz_fdict['TOL5VDIS'] = self.TOL5VDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PC_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PC_CTRL, self).__init__(rmio, label,
            0x4000a000, 0x060,
            'PC_CTRL', 'GPIO.PC_CTRL', 'read-write',
            "",
            0x00600060, 0x10711071)

        self.DRIVESTRENGTH = RM_Field_GPIO_PC_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.SLEWRATE = RM_Field_GPIO_PC_CTRL_SLEWRATE(self)
        self.zz_fdict['SLEWRATE'] = self.SLEWRATE
        self.DINDIS = RM_Field_GPIO_PC_CTRL_DINDIS(self)
        self.zz_fdict['DINDIS'] = self.DINDIS
        self.DRIVESTRENGTHALT = RM_Field_GPIO_PC_CTRL_DRIVESTRENGTHALT(self)
        self.zz_fdict['DRIVESTRENGTHALT'] = self.DRIVESTRENGTHALT
        self.SLEWRATEALT = RM_Field_GPIO_PC_CTRL_SLEWRATEALT(self)
        self.zz_fdict['SLEWRATEALT'] = self.SLEWRATEALT
        self.DINDISALT = RM_Field_GPIO_PC_CTRL_DINDISALT(self)
        self.zz_fdict['DINDISALT'] = self.DINDISALT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PC_MODEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PC_MODEL, self).__init__(rmio, label,
            0x4000a000, 0x064,
            'PC_MODEL', 'GPIO.PC_MODEL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE0 = RM_Field_GPIO_PC_MODEL_MODE0(self)
        self.zz_fdict['MODE0'] = self.MODE0
        self.MODE1 = RM_Field_GPIO_PC_MODEL_MODE1(self)
        self.zz_fdict['MODE1'] = self.MODE1
        self.MODE2 = RM_Field_GPIO_PC_MODEL_MODE2(self)
        self.zz_fdict['MODE2'] = self.MODE2
        self.MODE3 = RM_Field_GPIO_PC_MODEL_MODE3(self)
        self.zz_fdict['MODE3'] = self.MODE3
        self.MODE4 = RM_Field_GPIO_PC_MODEL_MODE4(self)
        self.zz_fdict['MODE4'] = self.MODE4
        self.MODE5 = RM_Field_GPIO_PC_MODEL_MODE5(self)
        self.zz_fdict['MODE5'] = self.MODE5
        self.MODE6 = RM_Field_GPIO_PC_MODEL_MODE6(self)
        self.zz_fdict['MODE6'] = self.MODE6
        self.MODE7 = RM_Field_GPIO_PC_MODEL_MODE7(self)
        self.zz_fdict['MODE7'] = self.MODE7
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PC_MODEH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PC_MODEH, self).__init__(rmio, label,
            0x4000a000, 0x068,
            'PC_MODEH', 'GPIO.PC_MODEH', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE8 = RM_Field_GPIO_PC_MODEH_MODE8(self)
        self.zz_fdict['MODE8'] = self.MODE8
        self.MODE9 = RM_Field_GPIO_PC_MODEH_MODE9(self)
        self.zz_fdict['MODE9'] = self.MODE9
        self.MODE10 = RM_Field_GPIO_PC_MODEH_MODE10(self)
        self.zz_fdict['MODE10'] = self.MODE10
        self.MODE11 = RM_Field_GPIO_PC_MODEH_MODE11(self)
        self.zz_fdict['MODE11'] = self.MODE11
        self.MODE12 = RM_Field_GPIO_PC_MODEH_MODE12(self)
        self.zz_fdict['MODE12'] = self.MODE12
        self.MODE13 = RM_Field_GPIO_PC_MODEH_MODE13(self)
        self.zz_fdict['MODE13'] = self.MODE13
        self.MODE14 = RM_Field_GPIO_PC_MODEH_MODE14(self)
        self.zz_fdict['MODE14'] = self.MODE14
        self.MODE15 = RM_Field_GPIO_PC_MODEH_MODE15(self)
        self.zz_fdict['MODE15'] = self.MODE15
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PC_DOUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PC_DOUT, self).__init__(rmio, label,
            0x4000a000, 0x06C,
            'PC_DOUT', 'GPIO.PC_DOUT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUT = RM_Field_GPIO_PC_DOUT_DOUT(self)
        self.zz_fdict['DOUT'] = self.DOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PC_DOUTTGL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PC_DOUTTGL, self).__init__(rmio, label,
            0x4000a000, 0x078,
            'PC_DOUTTGL', 'GPIO.PC_DOUTTGL', 'write-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUTTGL = RM_Field_GPIO_PC_DOUTTGL_DOUTTGL(self)
        self.zz_fdict['DOUTTGL'] = self.DOUTTGL
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PC_DIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PC_DIN, self).__init__(rmio, label,
            0x4000a000, 0x07C,
            'PC_DIN', 'GPIO.PC_DIN', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DIN = RM_Field_GPIO_PC_DIN_DIN(self)
        self.zz_fdict['DIN'] = self.DIN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PC_PINLOCKN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PC_PINLOCKN, self).__init__(rmio, label,
            0x4000a000, 0x080,
            'PC_PINLOCKN', 'GPIO.PC_PINLOCKN', 'read-write',
            "",
            0x0000FFFF, 0x0000FFFF)

        self.PINLOCKN = RM_Field_GPIO_PC_PINLOCKN_PINLOCKN(self)
        self.zz_fdict['PINLOCKN'] = self.PINLOCKN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PC_TOL5VDIS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PC_TOL5VDIS, self).__init__(rmio, label,
            0x4000a000, 0x088,
            'PC_TOL5VDIS', 'GPIO.PC_TOL5VDIS', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TOL5VDIS = RM_Field_GPIO_PC_TOL5VDIS_TOL5VDIS(self)
        self.zz_fdict['TOL5VDIS'] = self.TOL5VDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PD_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PD_CTRL, self).__init__(rmio, label,
            0x4000a000, 0x090,
            'PD_CTRL', 'GPIO.PD_CTRL', 'read-write',
            "",
            0x00600060, 0x10711071)

        self.DRIVESTRENGTH = RM_Field_GPIO_PD_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.SLEWRATE = RM_Field_GPIO_PD_CTRL_SLEWRATE(self)
        self.zz_fdict['SLEWRATE'] = self.SLEWRATE
        self.DINDIS = RM_Field_GPIO_PD_CTRL_DINDIS(self)
        self.zz_fdict['DINDIS'] = self.DINDIS
        self.DRIVESTRENGTHALT = RM_Field_GPIO_PD_CTRL_DRIVESTRENGTHALT(self)
        self.zz_fdict['DRIVESTRENGTHALT'] = self.DRIVESTRENGTHALT
        self.SLEWRATEALT = RM_Field_GPIO_PD_CTRL_SLEWRATEALT(self)
        self.zz_fdict['SLEWRATEALT'] = self.SLEWRATEALT
        self.DINDISALT = RM_Field_GPIO_PD_CTRL_DINDISALT(self)
        self.zz_fdict['DINDISALT'] = self.DINDISALT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PD_MODEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PD_MODEL, self).__init__(rmio, label,
            0x4000a000, 0x094,
            'PD_MODEL', 'GPIO.PD_MODEL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE0 = RM_Field_GPIO_PD_MODEL_MODE0(self)
        self.zz_fdict['MODE0'] = self.MODE0
        self.MODE1 = RM_Field_GPIO_PD_MODEL_MODE1(self)
        self.zz_fdict['MODE1'] = self.MODE1
        self.MODE2 = RM_Field_GPIO_PD_MODEL_MODE2(self)
        self.zz_fdict['MODE2'] = self.MODE2
        self.MODE3 = RM_Field_GPIO_PD_MODEL_MODE3(self)
        self.zz_fdict['MODE3'] = self.MODE3
        self.MODE4 = RM_Field_GPIO_PD_MODEL_MODE4(self)
        self.zz_fdict['MODE4'] = self.MODE4
        self.MODE5 = RM_Field_GPIO_PD_MODEL_MODE5(self)
        self.zz_fdict['MODE5'] = self.MODE5
        self.MODE6 = RM_Field_GPIO_PD_MODEL_MODE6(self)
        self.zz_fdict['MODE6'] = self.MODE6
        self.MODE7 = RM_Field_GPIO_PD_MODEL_MODE7(self)
        self.zz_fdict['MODE7'] = self.MODE7
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PD_MODEH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PD_MODEH, self).__init__(rmio, label,
            0x4000a000, 0x098,
            'PD_MODEH', 'GPIO.PD_MODEH', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE8 = RM_Field_GPIO_PD_MODEH_MODE8(self)
        self.zz_fdict['MODE8'] = self.MODE8
        self.MODE9 = RM_Field_GPIO_PD_MODEH_MODE9(self)
        self.zz_fdict['MODE9'] = self.MODE9
        self.MODE10 = RM_Field_GPIO_PD_MODEH_MODE10(self)
        self.zz_fdict['MODE10'] = self.MODE10
        self.MODE11 = RM_Field_GPIO_PD_MODEH_MODE11(self)
        self.zz_fdict['MODE11'] = self.MODE11
        self.MODE12 = RM_Field_GPIO_PD_MODEH_MODE12(self)
        self.zz_fdict['MODE12'] = self.MODE12
        self.MODE13 = RM_Field_GPIO_PD_MODEH_MODE13(self)
        self.zz_fdict['MODE13'] = self.MODE13
        self.MODE14 = RM_Field_GPIO_PD_MODEH_MODE14(self)
        self.zz_fdict['MODE14'] = self.MODE14
        self.MODE15 = RM_Field_GPIO_PD_MODEH_MODE15(self)
        self.zz_fdict['MODE15'] = self.MODE15
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PD_DOUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PD_DOUT, self).__init__(rmio, label,
            0x4000a000, 0x09C,
            'PD_DOUT', 'GPIO.PD_DOUT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUT = RM_Field_GPIO_PD_DOUT_DOUT(self)
        self.zz_fdict['DOUT'] = self.DOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PD_DOUTTGL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PD_DOUTTGL, self).__init__(rmio, label,
            0x4000a000, 0x0A8,
            'PD_DOUTTGL', 'GPIO.PD_DOUTTGL', 'write-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUTTGL = RM_Field_GPIO_PD_DOUTTGL_DOUTTGL(self)
        self.zz_fdict['DOUTTGL'] = self.DOUTTGL
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PD_DIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PD_DIN, self).__init__(rmio, label,
            0x4000a000, 0x0AC,
            'PD_DIN', 'GPIO.PD_DIN', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DIN = RM_Field_GPIO_PD_DIN_DIN(self)
        self.zz_fdict['DIN'] = self.DIN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PD_PINLOCKN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PD_PINLOCKN, self).__init__(rmio, label,
            0x4000a000, 0x0B0,
            'PD_PINLOCKN', 'GPIO.PD_PINLOCKN', 'read-write',
            "",
            0x0000FFFF, 0x0000FFFF)

        self.PINLOCKN = RM_Field_GPIO_PD_PINLOCKN_PINLOCKN(self)
        self.zz_fdict['PINLOCKN'] = self.PINLOCKN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PD_TOL5VDIS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PD_TOL5VDIS, self).__init__(rmio, label,
            0x4000a000, 0x0B8,
            'PD_TOL5VDIS', 'GPIO.PD_TOL5VDIS', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TOL5VDIS = RM_Field_GPIO_PD_TOL5VDIS_TOL5VDIS(self)
        self.zz_fdict['TOL5VDIS'] = self.TOL5VDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PE_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PE_CTRL, self).__init__(rmio, label,
            0x4000a000, 0x0C0,
            'PE_CTRL', 'GPIO.PE_CTRL', 'read-write',
            "",
            0x00600060, 0x10711071)

        self.DRIVESTRENGTH = RM_Field_GPIO_PE_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.SLEWRATE = RM_Field_GPIO_PE_CTRL_SLEWRATE(self)
        self.zz_fdict['SLEWRATE'] = self.SLEWRATE
        self.DINDIS = RM_Field_GPIO_PE_CTRL_DINDIS(self)
        self.zz_fdict['DINDIS'] = self.DINDIS
        self.DRIVESTRENGTHALT = RM_Field_GPIO_PE_CTRL_DRIVESTRENGTHALT(self)
        self.zz_fdict['DRIVESTRENGTHALT'] = self.DRIVESTRENGTHALT
        self.SLEWRATEALT = RM_Field_GPIO_PE_CTRL_SLEWRATEALT(self)
        self.zz_fdict['SLEWRATEALT'] = self.SLEWRATEALT
        self.DINDISALT = RM_Field_GPIO_PE_CTRL_DINDISALT(self)
        self.zz_fdict['DINDISALT'] = self.DINDISALT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PE_MODEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PE_MODEL, self).__init__(rmio, label,
            0x4000a000, 0x0C4,
            'PE_MODEL', 'GPIO.PE_MODEL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE0 = RM_Field_GPIO_PE_MODEL_MODE0(self)
        self.zz_fdict['MODE0'] = self.MODE0
        self.MODE1 = RM_Field_GPIO_PE_MODEL_MODE1(self)
        self.zz_fdict['MODE1'] = self.MODE1
        self.MODE2 = RM_Field_GPIO_PE_MODEL_MODE2(self)
        self.zz_fdict['MODE2'] = self.MODE2
        self.MODE3 = RM_Field_GPIO_PE_MODEL_MODE3(self)
        self.zz_fdict['MODE3'] = self.MODE3
        self.MODE4 = RM_Field_GPIO_PE_MODEL_MODE4(self)
        self.zz_fdict['MODE4'] = self.MODE4
        self.MODE5 = RM_Field_GPIO_PE_MODEL_MODE5(self)
        self.zz_fdict['MODE5'] = self.MODE5
        self.MODE6 = RM_Field_GPIO_PE_MODEL_MODE6(self)
        self.zz_fdict['MODE6'] = self.MODE6
        self.MODE7 = RM_Field_GPIO_PE_MODEL_MODE7(self)
        self.zz_fdict['MODE7'] = self.MODE7
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PE_MODEH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PE_MODEH, self).__init__(rmio, label,
            0x4000a000, 0x0C8,
            'PE_MODEH', 'GPIO.PE_MODEH', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE8 = RM_Field_GPIO_PE_MODEH_MODE8(self)
        self.zz_fdict['MODE8'] = self.MODE8
        self.MODE9 = RM_Field_GPIO_PE_MODEH_MODE9(self)
        self.zz_fdict['MODE9'] = self.MODE9
        self.MODE10 = RM_Field_GPIO_PE_MODEH_MODE10(self)
        self.zz_fdict['MODE10'] = self.MODE10
        self.MODE11 = RM_Field_GPIO_PE_MODEH_MODE11(self)
        self.zz_fdict['MODE11'] = self.MODE11
        self.MODE12 = RM_Field_GPIO_PE_MODEH_MODE12(self)
        self.zz_fdict['MODE12'] = self.MODE12
        self.MODE13 = RM_Field_GPIO_PE_MODEH_MODE13(self)
        self.zz_fdict['MODE13'] = self.MODE13
        self.MODE14 = RM_Field_GPIO_PE_MODEH_MODE14(self)
        self.zz_fdict['MODE14'] = self.MODE14
        self.MODE15 = RM_Field_GPIO_PE_MODEH_MODE15(self)
        self.zz_fdict['MODE15'] = self.MODE15
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PE_DOUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PE_DOUT, self).__init__(rmio, label,
            0x4000a000, 0x0CC,
            'PE_DOUT', 'GPIO.PE_DOUT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUT = RM_Field_GPIO_PE_DOUT_DOUT(self)
        self.zz_fdict['DOUT'] = self.DOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PE_DOUTTGL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PE_DOUTTGL, self).__init__(rmio, label,
            0x4000a000, 0x0D8,
            'PE_DOUTTGL', 'GPIO.PE_DOUTTGL', 'write-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUTTGL = RM_Field_GPIO_PE_DOUTTGL_DOUTTGL(self)
        self.zz_fdict['DOUTTGL'] = self.DOUTTGL
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PE_DIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PE_DIN, self).__init__(rmio, label,
            0x4000a000, 0x0DC,
            'PE_DIN', 'GPIO.PE_DIN', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DIN = RM_Field_GPIO_PE_DIN_DIN(self)
        self.zz_fdict['DIN'] = self.DIN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PE_PINLOCKN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PE_PINLOCKN, self).__init__(rmio, label,
            0x4000a000, 0x0E0,
            'PE_PINLOCKN', 'GPIO.PE_PINLOCKN', 'read-write',
            "",
            0x0000FFFF, 0x0000FFFF)

        self.PINLOCKN = RM_Field_GPIO_PE_PINLOCKN_PINLOCKN(self)
        self.zz_fdict['PINLOCKN'] = self.PINLOCKN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PE_TOL5VDIS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PE_TOL5VDIS, self).__init__(rmio, label,
            0x4000a000, 0x0E8,
            'PE_TOL5VDIS', 'GPIO.PE_TOL5VDIS', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TOL5VDIS = RM_Field_GPIO_PE_TOL5VDIS_TOL5VDIS(self)
        self.zz_fdict['TOL5VDIS'] = self.TOL5VDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PF_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PF_CTRL, self).__init__(rmio, label,
            0x4000a000, 0x0F0,
            'PF_CTRL', 'GPIO.PF_CTRL', 'read-write',
            "",
            0x00600060, 0x10711071)

        self.DRIVESTRENGTH = RM_Field_GPIO_PF_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.SLEWRATE = RM_Field_GPIO_PF_CTRL_SLEWRATE(self)
        self.zz_fdict['SLEWRATE'] = self.SLEWRATE
        self.DINDIS = RM_Field_GPIO_PF_CTRL_DINDIS(self)
        self.zz_fdict['DINDIS'] = self.DINDIS
        self.DRIVESTRENGTHALT = RM_Field_GPIO_PF_CTRL_DRIVESTRENGTHALT(self)
        self.zz_fdict['DRIVESTRENGTHALT'] = self.DRIVESTRENGTHALT
        self.SLEWRATEALT = RM_Field_GPIO_PF_CTRL_SLEWRATEALT(self)
        self.zz_fdict['SLEWRATEALT'] = self.SLEWRATEALT
        self.DINDISALT = RM_Field_GPIO_PF_CTRL_DINDISALT(self)
        self.zz_fdict['DINDISALT'] = self.DINDISALT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PF_MODEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PF_MODEL, self).__init__(rmio, label,
            0x4000a000, 0x0F4,
            'PF_MODEL', 'GPIO.PF_MODEL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE0 = RM_Field_GPIO_PF_MODEL_MODE0(self)
        self.zz_fdict['MODE0'] = self.MODE0
        self.MODE1 = RM_Field_GPIO_PF_MODEL_MODE1(self)
        self.zz_fdict['MODE1'] = self.MODE1
        self.MODE2 = RM_Field_GPIO_PF_MODEL_MODE2(self)
        self.zz_fdict['MODE2'] = self.MODE2
        self.MODE3 = RM_Field_GPIO_PF_MODEL_MODE3(self)
        self.zz_fdict['MODE3'] = self.MODE3
        self.MODE4 = RM_Field_GPIO_PF_MODEL_MODE4(self)
        self.zz_fdict['MODE4'] = self.MODE4
        self.MODE5 = RM_Field_GPIO_PF_MODEL_MODE5(self)
        self.zz_fdict['MODE5'] = self.MODE5
        self.MODE6 = RM_Field_GPIO_PF_MODEL_MODE6(self)
        self.zz_fdict['MODE6'] = self.MODE6
        self.MODE7 = RM_Field_GPIO_PF_MODEL_MODE7(self)
        self.zz_fdict['MODE7'] = self.MODE7
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PF_MODEH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PF_MODEH, self).__init__(rmio, label,
            0x4000a000, 0x0F8,
            'PF_MODEH', 'GPIO.PF_MODEH', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE8 = RM_Field_GPIO_PF_MODEH_MODE8(self)
        self.zz_fdict['MODE8'] = self.MODE8
        self.MODE9 = RM_Field_GPIO_PF_MODEH_MODE9(self)
        self.zz_fdict['MODE9'] = self.MODE9
        self.MODE10 = RM_Field_GPIO_PF_MODEH_MODE10(self)
        self.zz_fdict['MODE10'] = self.MODE10
        self.MODE11 = RM_Field_GPIO_PF_MODEH_MODE11(self)
        self.zz_fdict['MODE11'] = self.MODE11
        self.MODE12 = RM_Field_GPIO_PF_MODEH_MODE12(self)
        self.zz_fdict['MODE12'] = self.MODE12
        self.MODE13 = RM_Field_GPIO_PF_MODEH_MODE13(self)
        self.zz_fdict['MODE13'] = self.MODE13
        self.MODE14 = RM_Field_GPIO_PF_MODEH_MODE14(self)
        self.zz_fdict['MODE14'] = self.MODE14
        self.MODE15 = RM_Field_GPIO_PF_MODEH_MODE15(self)
        self.zz_fdict['MODE15'] = self.MODE15
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PF_DOUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PF_DOUT, self).__init__(rmio, label,
            0x4000a000, 0x0FC,
            'PF_DOUT', 'GPIO.PF_DOUT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUT = RM_Field_GPIO_PF_DOUT_DOUT(self)
        self.zz_fdict['DOUT'] = self.DOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PF_DOUTTGL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PF_DOUTTGL, self).__init__(rmio, label,
            0x4000a000, 0x108,
            'PF_DOUTTGL', 'GPIO.PF_DOUTTGL', 'write-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUTTGL = RM_Field_GPIO_PF_DOUTTGL_DOUTTGL(self)
        self.zz_fdict['DOUTTGL'] = self.DOUTTGL
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PF_DIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PF_DIN, self).__init__(rmio, label,
            0x4000a000, 0x10C,
            'PF_DIN', 'GPIO.PF_DIN', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DIN = RM_Field_GPIO_PF_DIN_DIN(self)
        self.zz_fdict['DIN'] = self.DIN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PF_PINLOCKN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PF_PINLOCKN, self).__init__(rmio, label,
            0x4000a000, 0x110,
            'PF_PINLOCKN', 'GPIO.PF_PINLOCKN', 'read-write',
            "",
            0x0000FFFF, 0x0000FFFF)

        self.PINLOCKN = RM_Field_GPIO_PF_PINLOCKN_PINLOCKN(self)
        self.zz_fdict['PINLOCKN'] = self.PINLOCKN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PF_TOL5VDIS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PF_TOL5VDIS, self).__init__(rmio, label,
            0x4000a000, 0x118,
            'PF_TOL5VDIS', 'GPIO.PF_TOL5VDIS', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TOL5VDIS = RM_Field_GPIO_PF_TOL5VDIS_TOL5VDIS(self)
        self.zz_fdict['TOL5VDIS'] = self.TOL5VDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PG_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PG_CTRL, self).__init__(rmio, label,
            0x4000a000, 0x120,
            'PG_CTRL', 'GPIO.PG_CTRL', 'read-write',
            "",
            0x00600060, 0x10711071)

        self.DRIVESTRENGTH = RM_Field_GPIO_PG_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.SLEWRATE = RM_Field_GPIO_PG_CTRL_SLEWRATE(self)
        self.zz_fdict['SLEWRATE'] = self.SLEWRATE
        self.DINDIS = RM_Field_GPIO_PG_CTRL_DINDIS(self)
        self.zz_fdict['DINDIS'] = self.DINDIS
        self.DRIVESTRENGTHALT = RM_Field_GPIO_PG_CTRL_DRIVESTRENGTHALT(self)
        self.zz_fdict['DRIVESTRENGTHALT'] = self.DRIVESTRENGTHALT
        self.SLEWRATEALT = RM_Field_GPIO_PG_CTRL_SLEWRATEALT(self)
        self.zz_fdict['SLEWRATEALT'] = self.SLEWRATEALT
        self.DINDISALT = RM_Field_GPIO_PG_CTRL_DINDISALT(self)
        self.zz_fdict['DINDISALT'] = self.DINDISALT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PG_MODEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PG_MODEL, self).__init__(rmio, label,
            0x4000a000, 0x124,
            'PG_MODEL', 'GPIO.PG_MODEL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE0 = RM_Field_GPIO_PG_MODEL_MODE0(self)
        self.zz_fdict['MODE0'] = self.MODE0
        self.MODE1 = RM_Field_GPIO_PG_MODEL_MODE1(self)
        self.zz_fdict['MODE1'] = self.MODE1
        self.MODE2 = RM_Field_GPIO_PG_MODEL_MODE2(self)
        self.zz_fdict['MODE2'] = self.MODE2
        self.MODE3 = RM_Field_GPIO_PG_MODEL_MODE3(self)
        self.zz_fdict['MODE3'] = self.MODE3
        self.MODE4 = RM_Field_GPIO_PG_MODEL_MODE4(self)
        self.zz_fdict['MODE4'] = self.MODE4
        self.MODE5 = RM_Field_GPIO_PG_MODEL_MODE5(self)
        self.zz_fdict['MODE5'] = self.MODE5
        self.MODE6 = RM_Field_GPIO_PG_MODEL_MODE6(self)
        self.zz_fdict['MODE6'] = self.MODE6
        self.MODE7 = RM_Field_GPIO_PG_MODEL_MODE7(self)
        self.zz_fdict['MODE7'] = self.MODE7
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PG_MODEH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PG_MODEH, self).__init__(rmio, label,
            0x4000a000, 0x128,
            'PG_MODEH', 'GPIO.PG_MODEH', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE8 = RM_Field_GPIO_PG_MODEH_MODE8(self)
        self.zz_fdict['MODE8'] = self.MODE8
        self.MODE9 = RM_Field_GPIO_PG_MODEH_MODE9(self)
        self.zz_fdict['MODE9'] = self.MODE9
        self.MODE10 = RM_Field_GPIO_PG_MODEH_MODE10(self)
        self.zz_fdict['MODE10'] = self.MODE10
        self.MODE11 = RM_Field_GPIO_PG_MODEH_MODE11(self)
        self.zz_fdict['MODE11'] = self.MODE11
        self.MODE12 = RM_Field_GPIO_PG_MODEH_MODE12(self)
        self.zz_fdict['MODE12'] = self.MODE12
        self.MODE13 = RM_Field_GPIO_PG_MODEH_MODE13(self)
        self.zz_fdict['MODE13'] = self.MODE13
        self.MODE14 = RM_Field_GPIO_PG_MODEH_MODE14(self)
        self.zz_fdict['MODE14'] = self.MODE14
        self.MODE15 = RM_Field_GPIO_PG_MODEH_MODE15(self)
        self.zz_fdict['MODE15'] = self.MODE15
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PG_DOUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PG_DOUT, self).__init__(rmio, label,
            0x4000a000, 0x12C,
            'PG_DOUT', 'GPIO.PG_DOUT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUT = RM_Field_GPIO_PG_DOUT_DOUT(self)
        self.zz_fdict['DOUT'] = self.DOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PG_DOUTTGL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PG_DOUTTGL, self).__init__(rmio, label,
            0x4000a000, 0x138,
            'PG_DOUTTGL', 'GPIO.PG_DOUTTGL', 'write-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUTTGL = RM_Field_GPIO_PG_DOUTTGL_DOUTTGL(self)
        self.zz_fdict['DOUTTGL'] = self.DOUTTGL
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PG_DIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PG_DIN, self).__init__(rmio, label,
            0x4000a000, 0x13C,
            'PG_DIN', 'GPIO.PG_DIN', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DIN = RM_Field_GPIO_PG_DIN_DIN(self)
        self.zz_fdict['DIN'] = self.DIN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PG_PINLOCKN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PG_PINLOCKN, self).__init__(rmio, label,
            0x4000a000, 0x140,
            'PG_PINLOCKN', 'GPIO.PG_PINLOCKN', 'read-write',
            "",
            0x0000FFFF, 0x0000FFFF)

        self.PINLOCKN = RM_Field_GPIO_PG_PINLOCKN_PINLOCKN(self)
        self.zz_fdict['PINLOCKN'] = self.PINLOCKN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PG_TOL5VDIS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PG_TOL5VDIS, self).__init__(rmio, label,
            0x4000a000, 0x148,
            'PG_TOL5VDIS', 'GPIO.PG_TOL5VDIS', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TOL5VDIS = RM_Field_GPIO_PG_TOL5VDIS_TOL5VDIS(self)
        self.zz_fdict['TOL5VDIS'] = self.TOL5VDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PH_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PH_CTRL, self).__init__(rmio, label,
            0x4000a000, 0x150,
            'PH_CTRL', 'GPIO.PH_CTRL', 'read-write',
            "",
            0x00600060, 0x10711071)

        self.DRIVESTRENGTH = RM_Field_GPIO_PH_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.SLEWRATE = RM_Field_GPIO_PH_CTRL_SLEWRATE(self)
        self.zz_fdict['SLEWRATE'] = self.SLEWRATE
        self.DINDIS = RM_Field_GPIO_PH_CTRL_DINDIS(self)
        self.zz_fdict['DINDIS'] = self.DINDIS
        self.DRIVESTRENGTHALT = RM_Field_GPIO_PH_CTRL_DRIVESTRENGTHALT(self)
        self.zz_fdict['DRIVESTRENGTHALT'] = self.DRIVESTRENGTHALT
        self.SLEWRATEALT = RM_Field_GPIO_PH_CTRL_SLEWRATEALT(self)
        self.zz_fdict['SLEWRATEALT'] = self.SLEWRATEALT
        self.DINDISALT = RM_Field_GPIO_PH_CTRL_DINDISALT(self)
        self.zz_fdict['DINDISALT'] = self.DINDISALT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PH_MODEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PH_MODEL, self).__init__(rmio, label,
            0x4000a000, 0x154,
            'PH_MODEL', 'GPIO.PH_MODEL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE0 = RM_Field_GPIO_PH_MODEL_MODE0(self)
        self.zz_fdict['MODE0'] = self.MODE0
        self.MODE1 = RM_Field_GPIO_PH_MODEL_MODE1(self)
        self.zz_fdict['MODE1'] = self.MODE1
        self.MODE2 = RM_Field_GPIO_PH_MODEL_MODE2(self)
        self.zz_fdict['MODE2'] = self.MODE2
        self.MODE3 = RM_Field_GPIO_PH_MODEL_MODE3(self)
        self.zz_fdict['MODE3'] = self.MODE3
        self.MODE4 = RM_Field_GPIO_PH_MODEL_MODE4(self)
        self.zz_fdict['MODE4'] = self.MODE4
        self.MODE5 = RM_Field_GPIO_PH_MODEL_MODE5(self)
        self.zz_fdict['MODE5'] = self.MODE5
        self.MODE6 = RM_Field_GPIO_PH_MODEL_MODE6(self)
        self.zz_fdict['MODE6'] = self.MODE6
        self.MODE7 = RM_Field_GPIO_PH_MODEL_MODE7(self)
        self.zz_fdict['MODE7'] = self.MODE7
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PH_MODEH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PH_MODEH, self).__init__(rmio, label,
            0x4000a000, 0x158,
            'PH_MODEH', 'GPIO.PH_MODEH', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE8 = RM_Field_GPIO_PH_MODEH_MODE8(self)
        self.zz_fdict['MODE8'] = self.MODE8
        self.MODE9 = RM_Field_GPIO_PH_MODEH_MODE9(self)
        self.zz_fdict['MODE9'] = self.MODE9
        self.MODE10 = RM_Field_GPIO_PH_MODEH_MODE10(self)
        self.zz_fdict['MODE10'] = self.MODE10
        self.MODE11 = RM_Field_GPIO_PH_MODEH_MODE11(self)
        self.zz_fdict['MODE11'] = self.MODE11
        self.MODE12 = RM_Field_GPIO_PH_MODEH_MODE12(self)
        self.zz_fdict['MODE12'] = self.MODE12
        self.MODE13 = RM_Field_GPIO_PH_MODEH_MODE13(self)
        self.zz_fdict['MODE13'] = self.MODE13
        self.MODE14 = RM_Field_GPIO_PH_MODEH_MODE14(self)
        self.zz_fdict['MODE14'] = self.MODE14
        self.MODE15 = RM_Field_GPIO_PH_MODEH_MODE15(self)
        self.zz_fdict['MODE15'] = self.MODE15
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PH_DOUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PH_DOUT, self).__init__(rmio, label,
            0x4000a000, 0x15C,
            'PH_DOUT', 'GPIO.PH_DOUT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUT = RM_Field_GPIO_PH_DOUT_DOUT(self)
        self.zz_fdict['DOUT'] = self.DOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PH_DOUTTGL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PH_DOUTTGL, self).__init__(rmio, label,
            0x4000a000, 0x168,
            'PH_DOUTTGL', 'GPIO.PH_DOUTTGL', 'write-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUTTGL = RM_Field_GPIO_PH_DOUTTGL_DOUTTGL(self)
        self.zz_fdict['DOUTTGL'] = self.DOUTTGL
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PH_DIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PH_DIN, self).__init__(rmio, label,
            0x4000a000, 0x16C,
            'PH_DIN', 'GPIO.PH_DIN', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DIN = RM_Field_GPIO_PH_DIN_DIN(self)
        self.zz_fdict['DIN'] = self.DIN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PH_PINLOCKN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PH_PINLOCKN, self).__init__(rmio, label,
            0x4000a000, 0x170,
            'PH_PINLOCKN', 'GPIO.PH_PINLOCKN', 'read-write',
            "",
            0x0000FFFF, 0x0000FFFF)

        self.PINLOCKN = RM_Field_GPIO_PH_PINLOCKN_PINLOCKN(self)
        self.zz_fdict['PINLOCKN'] = self.PINLOCKN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PH_TOL5VDIS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PH_TOL5VDIS, self).__init__(rmio, label,
            0x4000a000, 0x178,
            'PH_TOL5VDIS', 'GPIO.PH_TOL5VDIS', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TOL5VDIS = RM_Field_GPIO_PH_TOL5VDIS_TOL5VDIS(self)
        self.zz_fdict['TOL5VDIS'] = self.TOL5VDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PI_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PI_CTRL, self).__init__(rmio, label,
            0x4000a000, 0x180,
            'PI_CTRL', 'GPIO.PI_CTRL', 'read-write',
            "",
            0x00600060, 0x10711071)

        self.DRIVESTRENGTH = RM_Field_GPIO_PI_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.SLEWRATE = RM_Field_GPIO_PI_CTRL_SLEWRATE(self)
        self.zz_fdict['SLEWRATE'] = self.SLEWRATE
        self.DINDIS = RM_Field_GPIO_PI_CTRL_DINDIS(self)
        self.zz_fdict['DINDIS'] = self.DINDIS
        self.DRIVESTRENGTHALT = RM_Field_GPIO_PI_CTRL_DRIVESTRENGTHALT(self)
        self.zz_fdict['DRIVESTRENGTHALT'] = self.DRIVESTRENGTHALT
        self.SLEWRATEALT = RM_Field_GPIO_PI_CTRL_SLEWRATEALT(self)
        self.zz_fdict['SLEWRATEALT'] = self.SLEWRATEALT
        self.DINDISALT = RM_Field_GPIO_PI_CTRL_DINDISALT(self)
        self.zz_fdict['DINDISALT'] = self.DINDISALT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PI_MODEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PI_MODEL, self).__init__(rmio, label,
            0x4000a000, 0x184,
            'PI_MODEL', 'GPIO.PI_MODEL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE0 = RM_Field_GPIO_PI_MODEL_MODE0(self)
        self.zz_fdict['MODE0'] = self.MODE0
        self.MODE1 = RM_Field_GPIO_PI_MODEL_MODE1(self)
        self.zz_fdict['MODE1'] = self.MODE1
        self.MODE2 = RM_Field_GPIO_PI_MODEL_MODE2(self)
        self.zz_fdict['MODE2'] = self.MODE2
        self.MODE3 = RM_Field_GPIO_PI_MODEL_MODE3(self)
        self.zz_fdict['MODE3'] = self.MODE3
        self.MODE4 = RM_Field_GPIO_PI_MODEL_MODE4(self)
        self.zz_fdict['MODE4'] = self.MODE4
        self.MODE5 = RM_Field_GPIO_PI_MODEL_MODE5(self)
        self.zz_fdict['MODE5'] = self.MODE5
        self.MODE6 = RM_Field_GPIO_PI_MODEL_MODE6(self)
        self.zz_fdict['MODE6'] = self.MODE6
        self.MODE7 = RM_Field_GPIO_PI_MODEL_MODE7(self)
        self.zz_fdict['MODE7'] = self.MODE7
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PI_MODEH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PI_MODEH, self).__init__(rmio, label,
            0x4000a000, 0x188,
            'PI_MODEH', 'GPIO.PI_MODEH', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE8 = RM_Field_GPIO_PI_MODEH_MODE8(self)
        self.zz_fdict['MODE8'] = self.MODE8
        self.MODE9 = RM_Field_GPIO_PI_MODEH_MODE9(self)
        self.zz_fdict['MODE9'] = self.MODE9
        self.MODE10 = RM_Field_GPIO_PI_MODEH_MODE10(self)
        self.zz_fdict['MODE10'] = self.MODE10
        self.MODE11 = RM_Field_GPIO_PI_MODEH_MODE11(self)
        self.zz_fdict['MODE11'] = self.MODE11
        self.MODE12 = RM_Field_GPIO_PI_MODEH_MODE12(self)
        self.zz_fdict['MODE12'] = self.MODE12
        self.MODE13 = RM_Field_GPIO_PI_MODEH_MODE13(self)
        self.zz_fdict['MODE13'] = self.MODE13
        self.MODE14 = RM_Field_GPIO_PI_MODEH_MODE14(self)
        self.zz_fdict['MODE14'] = self.MODE14
        self.MODE15 = RM_Field_GPIO_PI_MODEH_MODE15(self)
        self.zz_fdict['MODE15'] = self.MODE15
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PI_DOUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PI_DOUT, self).__init__(rmio, label,
            0x4000a000, 0x18C,
            'PI_DOUT', 'GPIO.PI_DOUT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUT = RM_Field_GPIO_PI_DOUT_DOUT(self)
        self.zz_fdict['DOUT'] = self.DOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PI_DOUTTGL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PI_DOUTTGL, self).__init__(rmio, label,
            0x4000a000, 0x198,
            'PI_DOUTTGL', 'GPIO.PI_DOUTTGL', 'write-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUTTGL = RM_Field_GPIO_PI_DOUTTGL_DOUTTGL(self)
        self.zz_fdict['DOUTTGL'] = self.DOUTTGL
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PI_DIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PI_DIN, self).__init__(rmio, label,
            0x4000a000, 0x19C,
            'PI_DIN', 'GPIO.PI_DIN', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DIN = RM_Field_GPIO_PI_DIN_DIN(self)
        self.zz_fdict['DIN'] = self.DIN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PI_PINLOCKN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PI_PINLOCKN, self).__init__(rmio, label,
            0x4000a000, 0x1A0,
            'PI_PINLOCKN', 'GPIO.PI_PINLOCKN', 'read-write',
            "",
            0x0000FFFF, 0x0000FFFF)

        self.PINLOCKN = RM_Field_GPIO_PI_PINLOCKN_PINLOCKN(self)
        self.zz_fdict['PINLOCKN'] = self.PINLOCKN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PI_TOL5VDIS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PI_TOL5VDIS, self).__init__(rmio, label,
            0x4000a000, 0x1A8,
            'PI_TOL5VDIS', 'GPIO.PI_TOL5VDIS', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TOL5VDIS = RM_Field_GPIO_PI_TOL5VDIS_TOL5VDIS(self)
        self.zz_fdict['TOL5VDIS'] = self.TOL5VDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PJ_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PJ_CTRL, self).__init__(rmio, label,
            0x4000a000, 0x1B0,
            'PJ_CTRL', 'GPIO.PJ_CTRL', 'read-write',
            "",
            0x00600060, 0x10711071)

        self.DRIVESTRENGTH = RM_Field_GPIO_PJ_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.SLEWRATE = RM_Field_GPIO_PJ_CTRL_SLEWRATE(self)
        self.zz_fdict['SLEWRATE'] = self.SLEWRATE
        self.DINDIS = RM_Field_GPIO_PJ_CTRL_DINDIS(self)
        self.zz_fdict['DINDIS'] = self.DINDIS
        self.DRIVESTRENGTHALT = RM_Field_GPIO_PJ_CTRL_DRIVESTRENGTHALT(self)
        self.zz_fdict['DRIVESTRENGTHALT'] = self.DRIVESTRENGTHALT
        self.SLEWRATEALT = RM_Field_GPIO_PJ_CTRL_SLEWRATEALT(self)
        self.zz_fdict['SLEWRATEALT'] = self.SLEWRATEALT
        self.DINDISALT = RM_Field_GPIO_PJ_CTRL_DINDISALT(self)
        self.zz_fdict['DINDISALT'] = self.DINDISALT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PJ_MODEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PJ_MODEL, self).__init__(rmio, label,
            0x4000a000, 0x1B4,
            'PJ_MODEL', 'GPIO.PJ_MODEL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE0 = RM_Field_GPIO_PJ_MODEL_MODE0(self)
        self.zz_fdict['MODE0'] = self.MODE0
        self.MODE1 = RM_Field_GPIO_PJ_MODEL_MODE1(self)
        self.zz_fdict['MODE1'] = self.MODE1
        self.MODE2 = RM_Field_GPIO_PJ_MODEL_MODE2(self)
        self.zz_fdict['MODE2'] = self.MODE2
        self.MODE3 = RM_Field_GPIO_PJ_MODEL_MODE3(self)
        self.zz_fdict['MODE3'] = self.MODE3
        self.MODE4 = RM_Field_GPIO_PJ_MODEL_MODE4(self)
        self.zz_fdict['MODE4'] = self.MODE4
        self.MODE5 = RM_Field_GPIO_PJ_MODEL_MODE5(self)
        self.zz_fdict['MODE5'] = self.MODE5
        self.MODE6 = RM_Field_GPIO_PJ_MODEL_MODE6(self)
        self.zz_fdict['MODE6'] = self.MODE6
        self.MODE7 = RM_Field_GPIO_PJ_MODEL_MODE7(self)
        self.zz_fdict['MODE7'] = self.MODE7
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PJ_MODEH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PJ_MODEH, self).__init__(rmio, label,
            0x4000a000, 0x1B8,
            'PJ_MODEH', 'GPIO.PJ_MODEH', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE8 = RM_Field_GPIO_PJ_MODEH_MODE8(self)
        self.zz_fdict['MODE8'] = self.MODE8
        self.MODE9 = RM_Field_GPIO_PJ_MODEH_MODE9(self)
        self.zz_fdict['MODE9'] = self.MODE9
        self.MODE10 = RM_Field_GPIO_PJ_MODEH_MODE10(self)
        self.zz_fdict['MODE10'] = self.MODE10
        self.MODE11 = RM_Field_GPIO_PJ_MODEH_MODE11(self)
        self.zz_fdict['MODE11'] = self.MODE11
        self.MODE12 = RM_Field_GPIO_PJ_MODEH_MODE12(self)
        self.zz_fdict['MODE12'] = self.MODE12
        self.MODE13 = RM_Field_GPIO_PJ_MODEH_MODE13(self)
        self.zz_fdict['MODE13'] = self.MODE13
        self.MODE14 = RM_Field_GPIO_PJ_MODEH_MODE14(self)
        self.zz_fdict['MODE14'] = self.MODE14
        self.MODE15 = RM_Field_GPIO_PJ_MODEH_MODE15(self)
        self.zz_fdict['MODE15'] = self.MODE15
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PJ_DOUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PJ_DOUT, self).__init__(rmio, label,
            0x4000a000, 0x1BC,
            'PJ_DOUT', 'GPIO.PJ_DOUT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUT = RM_Field_GPIO_PJ_DOUT_DOUT(self)
        self.zz_fdict['DOUT'] = self.DOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PJ_DOUTTGL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PJ_DOUTTGL, self).__init__(rmio, label,
            0x4000a000, 0x1C8,
            'PJ_DOUTTGL', 'GPIO.PJ_DOUTTGL', 'write-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUTTGL = RM_Field_GPIO_PJ_DOUTTGL_DOUTTGL(self)
        self.zz_fdict['DOUTTGL'] = self.DOUTTGL
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PJ_DIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PJ_DIN, self).__init__(rmio, label,
            0x4000a000, 0x1CC,
            'PJ_DIN', 'GPIO.PJ_DIN', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DIN = RM_Field_GPIO_PJ_DIN_DIN(self)
        self.zz_fdict['DIN'] = self.DIN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PJ_PINLOCKN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PJ_PINLOCKN, self).__init__(rmio, label,
            0x4000a000, 0x1D0,
            'PJ_PINLOCKN', 'GPIO.PJ_PINLOCKN', 'read-write',
            "",
            0x0000FFFF, 0x0000FFFF)

        self.PINLOCKN = RM_Field_GPIO_PJ_PINLOCKN_PINLOCKN(self)
        self.zz_fdict['PINLOCKN'] = self.PINLOCKN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PJ_TOL5VDIS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PJ_TOL5VDIS, self).__init__(rmio, label,
            0x4000a000, 0x1D8,
            'PJ_TOL5VDIS', 'GPIO.PJ_TOL5VDIS', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TOL5VDIS = RM_Field_GPIO_PJ_TOL5VDIS_TOL5VDIS(self)
        self.zz_fdict['TOL5VDIS'] = self.TOL5VDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PK_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PK_CTRL, self).__init__(rmio, label,
            0x4000a000, 0x1E0,
            'PK_CTRL', 'GPIO.PK_CTRL', 'read-write',
            "",
            0x00600060, 0x10711071)

        self.DRIVESTRENGTH = RM_Field_GPIO_PK_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.SLEWRATE = RM_Field_GPIO_PK_CTRL_SLEWRATE(self)
        self.zz_fdict['SLEWRATE'] = self.SLEWRATE
        self.DINDIS = RM_Field_GPIO_PK_CTRL_DINDIS(self)
        self.zz_fdict['DINDIS'] = self.DINDIS
        self.DRIVESTRENGTHALT = RM_Field_GPIO_PK_CTRL_DRIVESTRENGTHALT(self)
        self.zz_fdict['DRIVESTRENGTHALT'] = self.DRIVESTRENGTHALT
        self.SLEWRATEALT = RM_Field_GPIO_PK_CTRL_SLEWRATEALT(self)
        self.zz_fdict['SLEWRATEALT'] = self.SLEWRATEALT
        self.DINDISALT = RM_Field_GPIO_PK_CTRL_DINDISALT(self)
        self.zz_fdict['DINDISALT'] = self.DINDISALT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PK_MODEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PK_MODEL, self).__init__(rmio, label,
            0x4000a000, 0x1E4,
            'PK_MODEL', 'GPIO.PK_MODEL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE0 = RM_Field_GPIO_PK_MODEL_MODE0(self)
        self.zz_fdict['MODE0'] = self.MODE0
        self.MODE1 = RM_Field_GPIO_PK_MODEL_MODE1(self)
        self.zz_fdict['MODE1'] = self.MODE1
        self.MODE2 = RM_Field_GPIO_PK_MODEL_MODE2(self)
        self.zz_fdict['MODE2'] = self.MODE2
        self.MODE3 = RM_Field_GPIO_PK_MODEL_MODE3(self)
        self.zz_fdict['MODE3'] = self.MODE3
        self.MODE4 = RM_Field_GPIO_PK_MODEL_MODE4(self)
        self.zz_fdict['MODE4'] = self.MODE4
        self.MODE5 = RM_Field_GPIO_PK_MODEL_MODE5(self)
        self.zz_fdict['MODE5'] = self.MODE5
        self.MODE6 = RM_Field_GPIO_PK_MODEL_MODE6(self)
        self.zz_fdict['MODE6'] = self.MODE6
        self.MODE7 = RM_Field_GPIO_PK_MODEL_MODE7(self)
        self.zz_fdict['MODE7'] = self.MODE7
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PK_MODEH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PK_MODEH, self).__init__(rmio, label,
            0x4000a000, 0x1E8,
            'PK_MODEH', 'GPIO.PK_MODEH', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE8 = RM_Field_GPIO_PK_MODEH_MODE8(self)
        self.zz_fdict['MODE8'] = self.MODE8
        self.MODE9 = RM_Field_GPIO_PK_MODEH_MODE9(self)
        self.zz_fdict['MODE9'] = self.MODE9
        self.MODE10 = RM_Field_GPIO_PK_MODEH_MODE10(self)
        self.zz_fdict['MODE10'] = self.MODE10
        self.MODE11 = RM_Field_GPIO_PK_MODEH_MODE11(self)
        self.zz_fdict['MODE11'] = self.MODE11
        self.MODE12 = RM_Field_GPIO_PK_MODEH_MODE12(self)
        self.zz_fdict['MODE12'] = self.MODE12
        self.MODE13 = RM_Field_GPIO_PK_MODEH_MODE13(self)
        self.zz_fdict['MODE13'] = self.MODE13
        self.MODE14 = RM_Field_GPIO_PK_MODEH_MODE14(self)
        self.zz_fdict['MODE14'] = self.MODE14
        self.MODE15 = RM_Field_GPIO_PK_MODEH_MODE15(self)
        self.zz_fdict['MODE15'] = self.MODE15
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PK_DOUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PK_DOUT, self).__init__(rmio, label,
            0x4000a000, 0x1EC,
            'PK_DOUT', 'GPIO.PK_DOUT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUT = RM_Field_GPIO_PK_DOUT_DOUT(self)
        self.zz_fdict['DOUT'] = self.DOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PK_DOUTTGL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PK_DOUTTGL, self).__init__(rmio, label,
            0x4000a000, 0x1F8,
            'PK_DOUTTGL', 'GPIO.PK_DOUTTGL', 'write-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUTTGL = RM_Field_GPIO_PK_DOUTTGL_DOUTTGL(self)
        self.zz_fdict['DOUTTGL'] = self.DOUTTGL
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PK_DIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PK_DIN, self).__init__(rmio, label,
            0x4000a000, 0x1FC,
            'PK_DIN', 'GPIO.PK_DIN', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DIN = RM_Field_GPIO_PK_DIN_DIN(self)
        self.zz_fdict['DIN'] = self.DIN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PK_PINLOCKN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PK_PINLOCKN, self).__init__(rmio, label,
            0x4000a000, 0x200,
            'PK_PINLOCKN', 'GPIO.PK_PINLOCKN', 'read-write',
            "",
            0x0000FFFF, 0x0000FFFF)

        self.PINLOCKN = RM_Field_GPIO_PK_PINLOCKN_PINLOCKN(self)
        self.zz_fdict['PINLOCKN'] = self.PINLOCKN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PK_TOL5VDIS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PK_TOL5VDIS, self).__init__(rmio, label,
            0x4000a000, 0x208,
            'PK_TOL5VDIS', 'GPIO.PK_TOL5VDIS', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TOL5VDIS = RM_Field_GPIO_PK_TOL5VDIS_TOL5VDIS(self)
        self.zz_fdict['TOL5VDIS'] = self.TOL5VDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PL_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PL_CTRL, self).__init__(rmio, label,
            0x4000a000, 0x210,
            'PL_CTRL', 'GPIO.PL_CTRL', 'read-write',
            "",
            0x00600060, 0x10711071)

        self.DRIVESTRENGTH = RM_Field_GPIO_PL_CTRL_DRIVESTRENGTH(self)
        self.zz_fdict['DRIVESTRENGTH'] = self.DRIVESTRENGTH
        self.SLEWRATE = RM_Field_GPIO_PL_CTRL_SLEWRATE(self)
        self.zz_fdict['SLEWRATE'] = self.SLEWRATE
        self.DINDIS = RM_Field_GPIO_PL_CTRL_DINDIS(self)
        self.zz_fdict['DINDIS'] = self.DINDIS
        self.DRIVESTRENGTHALT = RM_Field_GPIO_PL_CTRL_DRIVESTRENGTHALT(self)
        self.zz_fdict['DRIVESTRENGTHALT'] = self.DRIVESTRENGTHALT
        self.SLEWRATEALT = RM_Field_GPIO_PL_CTRL_SLEWRATEALT(self)
        self.zz_fdict['SLEWRATEALT'] = self.SLEWRATEALT
        self.DINDISALT = RM_Field_GPIO_PL_CTRL_DINDISALT(self)
        self.zz_fdict['DINDISALT'] = self.DINDISALT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PL_MODEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PL_MODEL, self).__init__(rmio, label,
            0x4000a000, 0x214,
            'PL_MODEL', 'GPIO.PL_MODEL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE0 = RM_Field_GPIO_PL_MODEL_MODE0(self)
        self.zz_fdict['MODE0'] = self.MODE0
        self.MODE1 = RM_Field_GPIO_PL_MODEL_MODE1(self)
        self.zz_fdict['MODE1'] = self.MODE1
        self.MODE2 = RM_Field_GPIO_PL_MODEL_MODE2(self)
        self.zz_fdict['MODE2'] = self.MODE2
        self.MODE3 = RM_Field_GPIO_PL_MODEL_MODE3(self)
        self.zz_fdict['MODE3'] = self.MODE3
        self.MODE4 = RM_Field_GPIO_PL_MODEL_MODE4(self)
        self.zz_fdict['MODE4'] = self.MODE4
        self.MODE5 = RM_Field_GPIO_PL_MODEL_MODE5(self)
        self.zz_fdict['MODE5'] = self.MODE5
        self.MODE6 = RM_Field_GPIO_PL_MODEL_MODE6(self)
        self.zz_fdict['MODE6'] = self.MODE6
        self.MODE7 = RM_Field_GPIO_PL_MODEL_MODE7(self)
        self.zz_fdict['MODE7'] = self.MODE7
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PL_MODEH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PL_MODEH, self).__init__(rmio, label,
            0x4000a000, 0x218,
            'PL_MODEH', 'GPIO.PL_MODEH', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MODE8 = RM_Field_GPIO_PL_MODEH_MODE8(self)
        self.zz_fdict['MODE8'] = self.MODE8
        self.MODE9 = RM_Field_GPIO_PL_MODEH_MODE9(self)
        self.zz_fdict['MODE9'] = self.MODE9
        self.MODE10 = RM_Field_GPIO_PL_MODEH_MODE10(self)
        self.zz_fdict['MODE10'] = self.MODE10
        self.MODE11 = RM_Field_GPIO_PL_MODEH_MODE11(self)
        self.zz_fdict['MODE11'] = self.MODE11
        self.MODE12 = RM_Field_GPIO_PL_MODEH_MODE12(self)
        self.zz_fdict['MODE12'] = self.MODE12
        self.MODE13 = RM_Field_GPIO_PL_MODEH_MODE13(self)
        self.zz_fdict['MODE13'] = self.MODE13
        self.MODE14 = RM_Field_GPIO_PL_MODEH_MODE14(self)
        self.zz_fdict['MODE14'] = self.MODE14
        self.MODE15 = RM_Field_GPIO_PL_MODEH_MODE15(self)
        self.zz_fdict['MODE15'] = self.MODE15
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PL_DOUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PL_DOUT, self).__init__(rmio, label,
            0x4000a000, 0x21C,
            'PL_DOUT', 'GPIO.PL_DOUT', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUT = RM_Field_GPIO_PL_DOUT_DOUT(self)
        self.zz_fdict['DOUT'] = self.DOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PL_DOUTTGL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PL_DOUTTGL, self).__init__(rmio, label,
            0x4000a000, 0x228,
            'PL_DOUTTGL', 'GPIO.PL_DOUTTGL', 'write-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DOUTTGL = RM_Field_GPIO_PL_DOUTTGL_DOUTTGL(self)
        self.zz_fdict['DOUTTGL'] = self.DOUTTGL
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PL_DIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PL_DIN, self).__init__(rmio, label,
            0x4000a000, 0x22C,
            'PL_DIN', 'GPIO.PL_DIN', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.DIN = RM_Field_GPIO_PL_DIN_DIN(self)
        self.zz_fdict['DIN'] = self.DIN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PL_PINLOCKN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PL_PINLOCKN, self).__init__(rmio, label,
            0x4000a000, 0x230,
            'PL_PINLOCKN', 'GPIO.PL_PINLOCKN', 'read-write',
            "",
            0x0000FFFF, 0x0000FFFF)

        self.PINLOCKN = RM_Field_GPIO_PL_PINLOCKN_PINLOCKN(self)
        self.zz_fdict['PINLOCKN'] = self.PINLOCKN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_PL_TOL5VDIS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_PL_TOL5VDIS, self).__init__(rmio, label,
            0x4000a000, 0x238,
            'PL_TOL5VDIS', 'GPIO.PL_TOL5VDIS', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.TOL5VDIS = RM_Field_GPIO_PL_TOL5VDIS_TOL5VDIS(self)
        self.zz_fdict['TOL5VDIS'] = self.TOL5VDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_EXTIPSELL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_EXTIPSELL, self).__init__(rmio, label,
            0x4000a000, 0x400,
            'EXTIPSELL', 'GPIO.EXTIPSELL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.EXTIPSEL0 = RM_Field_GPIO_EXTIPSELL_EXTIPSEL0(self)
        self.zz_fdict['EXTIPSEL0'] = self.EXTIPSEL0
        self.EXTIPSEL1 = RM_Field_GPIO_EXTIPSELL_EXTIPSEL1(self)
        self.zz_fdict['EXTIPSEL1'] = self.EXTIPSEL1
        self.EXTIPSEL2 = RM_Field_GPIO_EXTIPSELL_EXTIPSEL2(self)
        self.zz_fdict['EXTIPSEL2'] = self.EXTIPSEL2
        self.EXTIPSEL3 = RM_Field_GPIO_EXTIPSELL_EXTIPSEL3(self)
        self.zz_fdict['EXTIPSEL3'] = self.EXTIPSEL3
        self.EXTIPSEL4 = RM_Field_GPIO_EXTIPSELL_EXTIPSEL4(self)
        self.zz_fdict['EXTIPSEL4'] = self.EXTIPSEL4
        self.EXTIPSEL5 = RM_Field_GPIO_EXTIPSELL_EXTIPSEL5(self)
        self.zz_fdict['EXTIPSEL5'] = self.EXTIPSEL5
        self.EXTIPSEL6 = RM_Field_GPIO_EXTIPSELL_EXTIPSEL6(self)
        self.zz_fdict['EXTIPSEL6'] = self.EXTIPSEL6
        self.EXTIPSEL7 = RM_Field_GPIO_EXTIPSELL_EXTIPSEL7(self)
        self.zz_fdict['EXTIPSEL7'] = self.EXTIPSEL7
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_EXTIPSELH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_EXTIPSELH, self).__init__(rmio, label,
            0x4000a000, 0x404,
            'EXTIPSELH', 'GPIO.EXTIPSELH', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.EXTIPSEL8 = RM_Field_GPIO_EXTIPSELH_EXTIPSEL8(self)
        self.zz_fdict['EXTIPSEL8'] = self.EXTIPSEL8
        self.EXTIPSEL9 = RM_Field_GPIO_EXTIPSELH_EXTIPSEL9(self)
        self.zz_fdict['EXTIPSEL9'] = self.EXTIPSEL9
        self.EXTIPSEL10 = RM_Field_GPIO_EXTIPSELH_EXTIPSEL10(self)
        self.zz_fdict['EXTIPSEL10'] = self.EXTIPSEL10
        self.EXTIPSEL11 = RM_Field_GPIO_EXTIPSELH_EXTIPSEL11(self)
        self.zz_fdict['EXTIPSEL11'] = self.EXTIPSEL11
        self.EXTIPSEL12 = RM_Field_GPIO_EXTIPSELH_EXTIPSEL12(self)
        self.zz_fdict['EXTIPSEL12'] = self.EXTIPSEL12
        self.EXTIPSEL13 = RM_Field_GPIO_EXTIPSELH_EXTIPSEL13(self)
        self.zz_fdict['EXTIPSEL13'] = self.EXTIPSEL13
        self.EXTIPSEL14 = RM_Field_GPIO_EXTIPSELH_EXTIPSEL14(self)
        self.zz_fdict['EXTIPSEL14'] = self.EXTIPSEL14
        self.EXTIPSEL15 = RM_Field_GPIO_EXTIPSELH_EXTIPSEL15(self)
        self.zz_fdict['EXTIPSEL15'] = self.EXTIPSEL15
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_EXTIGSELL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_EXTIGSELL, self).__init__(rmio, label,
            0x4000a000, 0x408,
            'EXTIGSELL', 'GPIO.EXTIGSELL', 'read-write',
            "",
            0x32103210, 0x33333333)

        self.EXTIGSEL0 = RM_Field_GPIO_EXTIGSELL_EXTIGSEL0(self)
        self.zz_fdict['EXTIGSEL0'] = self.EXTIGSEL0
        self.EXTIGSEL1 = RM_Field_GPIO_EXTIGSELL_EXTIGSEL1(self)
        self.zz_fdict['EXTIGSEL1'] = self.EXTIGSEL1
        self.EXTIGSEL2 = RM_Field_GPIO_EXTIGSELL_EXTIGSEL2(self)
        self.zz_fdict['EXTIGSEL2'] = self.EXTIGSEL2
        self.EXTIGSEL3 = RM_Field_GPIO_EXTIGSELL_EXTIGSEL3(self)
        self.zz_fdict['EXTIGSEL3'] = self.EXTIGSEL3
        self.EXTIGSEL4 = RM_Field_GPIO_EXTIGSELL_EXTIGSEL4(self)
        self.zz_fdict['EXTIGSEL4'] = self.EXTIGSEL4
        self.EXTIGSEL5 = RM_Field_GPIO_EXTIGSELL_EXTIGSEL5(self)
        self.zz_fdict['EXTIGSEL5'] = self.EXTIGSEL5
        self.EXTIGSEL6 = RM_Field_GPIO_EXTIGSELL_EXTIGSEL6(self)
        self.zz_fdict['EXTIGSEL6'] = self.EXTIGSEL6
        self.EXTIGSEL7 = RM_Field_GPIO_EXTIGSELL_EXTIGSEL7(self)
        self.zz_fdict['EXTIGSEL7'] = self.EXTIGSEL7
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_EXTIGSELH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_EXTIGSELH, self).__init__(rmio, label,
            0x4000a000, 0x40C,
            'EXTIGSELH', 'GPIO.EXTIGSELH', 'read-write',
            "",
            0x32103210, 0x33333333)

        self.EXTIGSEL8 = RM_Field_GPIO_EXTIGSELH_EXTIGSEL8(self)
        self.zz_fdict['EXTIGSEL8'] = self.EXTIGSEL8
        self.EXTIGSEL9 = RM_Field_GPIO_EXTIGSELH_EXTIGSEL9(self)
        self.zz_fdict['EXTIGSEL9'] = self.EXTIGSEL9
        self.EXTIGSEL10 = RM_Field_GPIO_EXTIGSELH_EXTIGSEL10(self)
        self.zz_fdict['EXTIGSEL10'] = self.EXTIGSEL10
        self.EXTIGSEL11 = RM_Field_GPIO_EXTIGSELH_EXTIGSEL11(self)
        self.zz_fdict['EXTIGSEL11'] = self.EXTIGSEL11
        self.EXTIGSEL12 = RM_Field_GPIO_EXTIGSELH_EXTIGSEL12(self)
        self.zz_fdict['EXTIGSEL12'] = self.EXTIGSEL12
        self.EXTIGSEL13 = RM_Field_GPIO_EXTIGSELH_EXTIGSEL13(self)
        self.zz_fdict['EXTIGSEL13'] = self.EXTIGSEL13
        self.EXTIGSEL14 = RM_Field_GPIO_EXTIGSELH_EXTIGSEL14(self)
        self.zz_fdict['EXTIGSEL14'] = self.EXTIGSEL14
        self.EXTIGSEL15 = RM_Field_GPIO_EXTIGSELH_EXTIGSEL15(self)
        self.zz_fdict['EXTIGSEL15'] = self.EXTIGSEL15
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_EXTIRISE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_EXTIRISE, self).__init__(rmio, label,
            0x4000a000, 0x410,
            'EXTIRISE', 'GPIO.EXTIRISE', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.EXTIRISE = RM_Field_GPIO_EXTIRISE_EXTIRISE(self)
        self.zz_fdict['EXTIRISE'] = self.EXTIRISE
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_EXTIFALL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_EXTIFALL, self).__init__(rmio, label,
            0x4000a000, 0x414,
            'EXTIFALL', 'GPIO.EXTIFALL', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.EXTIFALL = RM_Field_GPIO_EXTIFALL_EXTIFALL(self)
        self.zz_fdict['EXTIFALL'] = self.EXTIFALL
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_EXTILEVEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_EXTILEVEL, self).__init__(rmio, label,
            0x4000a000, 0x418,
            'EXTILEVEL', 'GPIO.EXTILEVEL', 'read-write',
            "",
            0x00000000, 0x003F0000)

        self.EM4WULEVEL = RM_Field_GPIO_EXTILEVEL_EM4WULEVEL(self)
        self.zz_fdict['EM4WULEVEL'] = self.EM4WULEVEL
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_IF, self).__init__(rmio, label,
            0x4000a000, 0x41C,
            'IF', 'GPIO.IF', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.EXT = RM_Field_GPIO_IF_EXT(self)
        self.zz_fdict['EXT'] = self.EXT
        self.EM4WU = RM_Field_GPIO_IF_EM4WU(self)
        self.zz_fdict['EM4WU'] = self.EM4WU
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_IFS, self).__init__(rmio, label,
            0x4000a000, 0x420,
            'IFS', 'GPIO.IFS', 'write-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.EXT = RM_Field_GPIO_IFS_EXT(self)
        self.zz_fdict['EXT'] = self.EXT
        self.EM4WU = RM_Field_GPIO_IFS_EM4WU(self)
        self.zz_fdict['EM4WU'] = self.EM4WU
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_IFC, self).__init__(rmio, label,
            0x4000a000, 0x424,
            'IFC', 'GPIO.IFC', 'write-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.EXT = RM_Field_GPIO_IFC_EXT(self)
        self.zz_fdict['EXT'] = self.EXT
        self.EM4WU = RM_Field_GPIO_IFC_EM4WU(self)
        self.zz_fdict['EM4WU'] = self.EM4WU
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_IEN, self).__init__(rmio, label,
            0x4000a000, 0x428,
            'IEN', 'GPIO.IEN', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.EXT = RM_Field_GPIO_IEN_EXT(self)
        self.zz_fdict['EXT'] = self.EXT
        self.EM4WU = RM_Field_GPIO_IEN_EM4WU(self)
        self.zz_fdict['EM4WU'] = self.EM4WU
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_EM4WUEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_EM4WUEN, self).__init__(rmio, label,
            0x4000a000, 0x42C,
            'EM4WUEN', 'GPIO.EM4WUEN', 'read-write',
            "",
            0x00000000, 0xFFFF0000)

        self.EM4WUEN = RM_Field_GPIO_EM4WUEN_EM4WUEN(self)
        self.zz_fdict['EM4WUEN'] = self.EM4WUEN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_ROUTEPEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_ROUTEPEN, self).__init__(rmio, label,
            0x4000a000, 0x440,
            'ROUTEPEN', 'GPIO.ROUTEPEN', 'read-write',
            "",
            0x0000000F, 0x0000001F)

        self.SWCLKTCKPEN = RM_Field_GPIO_ROUTEPEN_SWCLKTCKPEN(self)
        self.zz_fdict['SWCLKTCKPEN'] = self.SWCLKTCKPEN
        self.SWDIOTMSPEN = RM_Field_GPIO_ROUTEPEN_SWDIOTMSPEN(self)
        self.zz_fdict['SWDIOTMSPEN'] = self.SWDIOTMSPEN
        self.TDOPEN = RM_Field_GPIO_ROUTEPEN_TDOPEN(self)
        self.zz_fdict['TDOPEN'] = self.TDOPEN
        self.TDIPEN = RM_Field_GPIO_ROUTEPEN_TDIPEN(self)
        self.zz_fdict['TDIPEN'] = self.TDIPEN
        self.SWVPEN = RM_Field_GPIO_ROUTEPEN_SWVPEN(self)
        self.zz_fdict['SWVPEN'] = self.SWVPEN
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_ROUTELOC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_ROUTELOC0, self).__init__(rmio, label,
            0x4000a000, 0x444,
            'ROUTELOC0', 'GPIO.ROUTELOC0', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.SWVLOC = RM_Field_GPIO_ROUTELOC0_SWVLOC(self)
        self.zz_fdict['SWVLOC'] = self.SWVLOC
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_INSENSE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_INSENSE, self).__init__(rmio, label,
            0x4000a000, 0x450,
            'INSENSE', 'GPIO.INSENSE', 'read-write',
            "",
            0x00000003, 0x00000003)

        self.INT = RM_Field_GPIO_INSENSE_INT(self)
        self.zz_fdict['INT'] = self.INT
        self.EM4WU = RM_Field_GPIO_INSENSE_EM4WU(self)
        self.zz_fdict['EM4WU'] = self.EM4WU
        self.__dict__['zz_frozen'] = True


class RM_Register_GPIO_LOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_GPIO_LOCK, self).__init__(rmio, label,
            0x4000a000, 0x454,
            'LOCK', 'GPIO.LOCK', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.LOCKKEY = RM_Field_GPIO_LOCK_LOCKKEY(self)
        self.zz_fdict['LOCKKEY'] = self.LOCKKEY
        self.__dict__['zz_frozen'] = True


