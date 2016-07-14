
from static import Base_RM_Field
from CSEN_enum import *


class RM_Field_CSEN_CTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_EN, self).__init__(register,
            'EN', 'CSEN.CTRL.EN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_CMPPOL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_CMPPOL, self).__init__(register,
            'CMPPOL', 'CSEN.CTRL.CMPPOL', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_CM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_CM, self).__init__(register,
            'CM', 'CSEN.CTRL.CM', 'read-write',
            "",
            4, 2,
            RM_Enum_CSEN_CTRL_CM(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_SARCR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_SARCR, self).__init__(register,
            'SARCR', 'CSEN.CTRL.SARCR', 'read-write',
            "",
            8, 2,
            RM_Enum_CSEN_CTRL_SARCR(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_ACU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_ACU, self).__init__(register,
            'ACU', 'CSEN.CTRL.ACU', 'read-write',
            "",
            12, 3,
            RM_Enum_CSEN_CTRL_ACU(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_MCEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_MCEN, self).__init__(register,
            'MCEN', 'CSEN.CTRL.MCEN', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_STM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_STM, self).__init__(register,
            'STM', 'CSEN.CTRL.STM', 'read-write',
            "",
            16, 2,
            RM_Enum_CSEN_CTRL_STM(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_CMPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_CMPEN, self).__init__(register,
            'CMPEN', 'CSEN.CTRL.CMPEN', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_DRSF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_DRSF, self).__init__(register,
            'DRSF', 'CSEN.CTRL.DRSF', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_DMAEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_DMAEN, self).__init__(register,
            'DMAEN', 'CSEN.CTRL.DMAEN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_CONVSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_CONVSEL, self).__init__(register,
            'CONVSEL', 'CSEN.CTRL.CONVSEL', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_CHOPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_CHOPEN, self).__init__(register,
            'CHOPEN', 'CSEN.CTRL.CHOPEN', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_AUTOGND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_AUTOGND, self).__init__(register,
            'AUTOGND', 'CSEN.CTRL.AUTOGND', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_MXUC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_MXUC, self).__init__(register,
            'MXUC', 'CSEN.CTRL.MXUC', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_EMACMPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_EMACMPEN, self).__init__(register,
            'EMACMPEN', 'CSEN.CTRL.EMACMPEN', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_WARMUPMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_WARMUPMODE, self).__init__(register,
            'WARMUPMODE', 'CSEN.CTRL.WARMUPMODE', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_LOCALSENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_LOCALSENS, self).__init__(register,
            'LOCALSENS', 'CSEN.CTRL.LOCALSENS', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_CPACCURACY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_CPACCURACY, self).__init__(register,
            'CPACCURACY', 'CSEN.CTRL.CPACCURACY', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CTRL_KEEPIBS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CTRL_KEEPIBS, self).__init__(register,
            'KEEPIBS', 'CSEN.CTRL.KEEPIBS', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TIMCTRL_PCPRESC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TIMCTRL_PCPRESC, self).__init__(register,
            'PCPRESC', 'CSEN.TIMCTRL.PCPRESC', 'read-write',
            "",
            0, 3,
            RM_Enum_CSEN_TIMCTRL_PCPRESC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TIMCTRL_PCTOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TIMCTRL_PCTOP, self).__init__(register,
            'PCTOP', 'CSEN.TIMCTRL.PCTOP', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TIMCTRL_WARMUPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TIMCTRL_WARMUPCNT, self).__init__(register,
            'WARMUPCNT', 'CSEN.TIMCTRL.WARMUPCNT', 'read-write',
            "",
            16, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CMD_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CMD_START, self).__init__(register,
            'START', 'CSEN.CMD.START', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CMD_TAZINIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CMD_TAZINIT, self).__init__(register,
            'TAZINIT', 'CSEN.CMD.TAZINIT', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CMD_IBISTSTART(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CMD_IBISTSTART, self).__init__(register,
            'IBISTSTART', 'CSEN.CMD.IBISTSTART', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_STATUS_CSENBUSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_STATUS_CSENBUSY, self).__init__(register,
            'CSENBUSY', 'CSEN.STATUS.CSENBUSY', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_STATUS_DCXBUSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_STATUS_DCXBUSY, self).__init__(register,
            'DCXBUSY', 'CSEN.STATUS.DCXBUSY', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_STATUS_TCONVBUSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_STATUS_TCONVBUSY, self).__init__(register,
            'TCONVBUSY', 'CSEN.STATUS.TCONVBUSY', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_STATUS_TSTD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_STATUS_TSTD, self).__init__(register,
            'TSTD', 'CSEN.STATUS.TSTD', 'read-only',
            "",
            16, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_PRSSEL_PRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_PRSSEL_PRSSEL, self).__init__(register,
            'PRSSEL', 'CSEN.PRSSEL.PRSSEL', 'read-write',
            "",
            0, 4,
            RM_Enum_CSEN_PRSSEL_PRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_DATA_DATA, self).__init__(register,
            'DATA', 'CSEN.DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_SCANMASK0_SCANINPUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_SCANMASK0_SCANINPUTEN, self).__init__(register,
            'SCANINPUTEN', 'CSEN.SCANMASK0.SCANINPUTEN', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_SCANINPUTSEL0_INPUT0TO7SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_SCANINPUTSEL0_INPUT0TO7SEL, self).__init__(register,
            'INPUT0TO7SEL', 'CSEN.SCANINPUTSEL0.INPUT0TO7SEL', 'read-write',
            "",
            0, 4,
            RM_Enum_CSEN_SCANINPUTSEL0_INPUT0TO7SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_SCANINPUTSEL0_INPUT8TO15SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_SCANINPUTSEL0_INPUT8TO15SEL, self).__init__(register,
            'INPUT8TO15SEL', 'CSEN.SCANINPUTSEL0.INPUT8TO15SEL', 'read-write',
            "",
            8, 4,
            RM_Enum_CSEN_SCANINPUTSEL0_INPUT8TO15SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_SCANINPUTSEL0_INPUT16TO23SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_SCANINPUTSEL0_INPUT16TO23SEL, self).__init__(register,
            'INPUT16TO23SEL', 'CSEN.SCANINPUTSEL0.INPUT16TO23SEL', 'read-write',
            "",
            16, 4,
            RM_Enum_CSEN_SCANINPUTSEL0_INPUT16TO23SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_SCANINPUTSEL0_INPUT24TO31SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_SCANINPUTSEL0_INPUT24TO31SEL, self).__init__(register,
            'INPUT24TO31SEL', 'CSEN.SCANINPUTSEL0.INPUT24TO31SEL', 'read-write',
            "",
            24, 4,
            RM_Enum_CSEN_SCANINPUTSEL0_INPUT24TO31SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_SCANMASK1_SCANINPUTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_SCANMASK1_SCANINPUTEN, self).__init__(register,
            'SCANINPUTEN', 'CSEN.SCANMASK1.SCANINPUTEN', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_SCANINPUTSEL1_INPUT32TO39SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_SCANINPUTSEL1_INPUT32TO39SEL, self).__init__(register,
            'INPUT32TO39SEL', 'CSEN.SCANINPUTSEL1.INPUT32TO39SEL', 'read-write',
            "",
            0, 4,
            RM_Enum_CSEN_SCANINPUTSEL1_INPUT32TO39SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_SCANINPUTSEL1_INPUT40TO47SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_SCANINPUTSEL1_INPUT40TO47SEL, self).__init__(register,
            'INPUT40TO47SEL', 'CSEN.SCANINPUTSEL1.INPUT40TO47SEL', 'read-write',
            "",
            8, 4,
            RM_Enum_CSEN_SCANINPUTSEL1_INPUT40TO47SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_SCANINPUTSEL1_INPUT48TO55SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_SCANINPUTSEL1_INPUT48TO55SEL, self).__init__(register,
            'INPUT48TO55SEL', 'CSEN.SCANINPUTSEL1.INPUT48TO55SEL', 'read-write',
            "",
            16, 4,
            RM_Enum_CSEN_SCANINPUTSEL1_INPUT48TO55SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_SCANINPUTSEL1_INPUT56TO63SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_SCANINPUTSEL1_INPUT56TO63SEL, self).__init__(register,
            'INPUT56TO63SEL', 'CSEN.SCANINPUTSEL1.INPUT56TO63SEL', 'read-write',
            "",
            24, 4,
            RM_Enum_CSEN_SCANINPUTSEL1_INPUT56TO63SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTREQ_APORT1XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTREQ_APORT1XREQ, self).__init__(register,
            'APORT1XREQ', 'CSEN.APORTREQ.APORT1XREQ', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTREQ_APORT1YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTREQ_APORT1YREQ, self).__init__(register,
            'APORT1YREQ', 'CSEN.APORTREQ.APORT1YREQ', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTREQ_APORT2XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTREQ_APORT2XREQ, self).__init__(register,
            'APORT2XREQ', 'CSEN.APORTREQ.APORT2XREQ', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTREQ_APORT2YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTREQ_APORT2YREQ, self).__init__(register,
            'APORT2YREQ', 'CSEN.APORTREQ.APORT2YREQ', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTREQ_APORT3XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTREQ_APORT3XREQ, self).__init__(register,
            'APORT3XREQ', 'CSEN.APORTREQ.APORT3XREQ', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTREQ_APORT3YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTREQ_APORT3YREQ, self).__init__(register,
            'APORT3YREQ', 'CSEN.APORTREQ.APORT3YREQ', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTREQ_APORT4XREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTREQ_APORT4XREQ, self).__init__(register,
            'APORT4XREQ', 'CSEN.APORTREQ.APORT4XREQ', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTREQ_APORT4YREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTREQ_APORT4YREQ, self).__init__(register,
            'APORT4YREQ', 'CSEN.APORTREQ.APORT4YREQ', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTCONFLICT_APORT1XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTCONFLICT_APORT1XCONFLICT, self).__init__(register,
            'APORT1XCONFLICT', 'CSEN.APORTCONFLICT.APORT1XCONFLICT', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTCONFLICT_APORT1YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTCONFLICT_APORT1YCONFLICT, self).__init__(register,
            'APORT1YCONFLICT', 'CSEN.APORTCONFLICT.APORT1YCONFLICT', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTCONFLICT_APORT2XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTCONFLICT_APORT2XCONFLICT, self).__init__(register,
            'APORT2XCONFLICT', 'CSEN.APORTCONFLICT.APORT2XCONFLICT', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTCONFLICT_APORT2YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTCONFLICT_APORT2YCONFLICT, self).__init__(register,
            'APORT2YCONFLICT', 'CSEN.APORTCONFLICT.APORT2YCONFLICT', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTCONFLICT_APORT3XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTCONFLICT_APORT3XCONFLICT, self).__init__(register,
            'APORT3XCONFLICT', 'CSEN.APORTCONFLICT.APORT3XCONFLICT', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTCONFLICT_APORT3YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTCONFLICT_APORT3YCONFLICT, self).__init__(register,
            'APORT3YCONFLICT', 'CSEN.APORTCONFLICT.APORT3YCONFLICT', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTCONFLICT_APORT4XCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTCONFLICT_APORT4XCONFLICT, self).__init__(register,
            'APORT4XCONFLICT', 'CSEN.APORTCONFLICT.APORT4XCONFLICT', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_APORTCONFLICT_APORT4YCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_APORTCONFLICT_APORT4YCONFLICT, self).__init__(register,
            'APORT4YCONFLICT', 'CSEN.APORTCONFLICT.APORT4YCONFLICT', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_CMPTHR_CMPTHR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_CMPTHR_CMPTHR, self).__init__(register,
            'CMPTHR', 'CSEN.CMPTHR.CMPTHR', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_EMA_EMA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_EMA_EMA, self).__init__(register,
            'EMA', 'CSEN.EMA.EMA', 'read-write',
            "",
            0, 22)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_EMACTRL_EMASAMPLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_EMACTRL_EMASAMPLE, self).__init__(register,
            'EMASAMPLE', 'CSEN.EMACTRL.EMASAMPLE', 'read-write',
            "",
            0, 3,
            RM_Enum_CSEN_EMACTRL_EMASAMPLE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_SINGLECTRL_SINGLESEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_SINGLECTRL_SINGLESEL, self).__init__(register,
            'SINGLESEL', 'CSEN.SINGLECTRL.SINGLESEL', 'read-write',
            "",
            4, 7,
            RM_Enum_CSEN_SINGLECTRL_SINGLESEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_DMBASELINE_BASELINEUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_DMBASELINE_BASELINEUP, self).__init__(register,
            'BASELINEUP', 'CSEN.DMBASELINE.BASELINEUP', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_DMBASELINE_BASELINEDN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_DMBASELINE_BASELINEDN, self).__init__(register,
            'BASELINEDN', 'CSEN.DMBASELINE.BASELINEDN', 'read-write',
            "",
            16, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_DMCFG_DMG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_DMCFG_DMG, self).__init__(register,
            'DMG', 'CSEN.DMCFG.DMG', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_DMCFG_DMR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_DMCFG_DMR, self).__init__(register,
            'DMR', 'CSEN.DMCFG.DMR', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_DMCFG_DMCR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_DMCFG_DMCR, self).__init__(register,
            'DMCR', 'CSEN.DMCFG.DMCR', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_DMCFG_CRMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_DMCFG_CRMODE, self).__init__(register,
            'CRMODE', 'CSEN.DMCFG.CRMODE', 'read-write',
            "",
            20, 2,
            RM_Enum_CSEN_DMCFG_CRMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_DMCFG_DMGRDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_DMCFG_DMGRDIS, self).__init__(register,
            'DMGRDIS', 'CSEN.DMCFG.DMGRDIS', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_ANACTRL_CREFHALF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_ANACTRL_CREFHALF, self).__init__(register,
            'CREFHALF', 'CSEN.ANACTRL.CREFHALF', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_ANACTRL_IREFPROG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_ANACTRL_IREFPROG, self).__init__(register,
            'IREFPROG', 'CSEN.ANACTRL.IREFPROG', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_ANACTRL_IDACIREFS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_ANACTRL_IDACIREFS, self).__init__(register,
            'IDACIREFS', 'CSEN.ANACTRL.IDACIREFS', 'read-write',
            "",
            8, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_ANACTRL_DUTYSCALE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_ANACTRL_DUTYSCALE, self).__init__(register,
            'DUTYSCALE', 'CSEN.ANACTRL.DUTYSCALE', 'read-write',
            "",
            16, 2,
            RM_Enum_CSEN_ANACTRL_DUTYSCALE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_ANACTRL_TRSTPROG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_ANACTRL_TRSTPROG, self).__init__(register,
            'TRSTPROG', 'CSEN.ANACTRL.TRSTPROG', 'read-write',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_ANACTRL_BIASPROG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_ANACTRL_BIASPROG, self).__init__(register,
            'BIASPROG', 'CSEN.ANACTRL.BIASPROG', 'read-write',
            "",
            24, 2,
            RM_Enum_CSEN_ANACTRL_BIASPROG(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_ANATRIM_ILTCUATRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_ANATRIM_ILTCUATRIM, self).__init__(register,
            'ILTCUATRIM', 'CSEN.ANATRIM.ILTCUATRIM', 'read-write',
            "",
            0, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TESTCFG_BISTCLKL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TESTCFG_BISTCLKL, self).__init__(register,
            'BISTCLKL', 'CSEN.TESTCFG.BISTCLKL', 'read-write',
            "",
            0, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TESTCFG_BISTCLKH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TESTCFG_BISTCLKH, self).__init__(register,
            'BISTCLKH', 'CSEN.TESTCFG.BISTCLKH', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TESTCFG_IDACTST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TESTCFG_IDACTST, self).__init__(register,
            'IDACTST', 'CSEN.TESTCFG.IDACTST', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TESTCFG_BISTCLKSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TESTCFG_BISTCLKSEL, self).__init__(register,
            'BISTCLKSEL', 'CSEN.TESTCFG.BISTCLKSEL', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TESTCFG_ANATESTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TESTCFG_ANATESTEN, self).__init__(register,
            'ANATESTEN', 'CSEN.TESTCFG.ANATESTEN', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TESTCFG_CHOPPOLTEST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TESTCFG_CHOPPOLTEST, self).__init__(register,
            'CHOPPOLTEST', 'CSEN.TESTCFG.CHOPPOLTEST', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TESTCFG_CLKSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TESTCFG_CLKSEL, self).__init__(register,
            'CLKSEL', 'CSEN.TESTCFG.CLKSEL', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TESTCFG_CRSTCOMB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TESTCFG_CRSTCOMB, self).__init__(register,
            'CRSTCOMB', 'CSEN.TESTCFG.CRSTCOMB', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TESTCFG_ILMTOFF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TESTCFG_ILMTOFF, self).__init__(register,
            'ILMTOFF', 'CSEN.TESTCFG.ILMTOFF', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TESTCFG_VCASHI(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TESTCFG_VCASHI, self).__init__(register,
            'VCASHI', 'CSEN.TESTCFG.VCASHI', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TESTCFG_VRSAMPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TESTCFG_VRSAMPEN, self).__init__(register,
            'VRSAMPEN', 'CSEN.TESTCFG.VRSAMPEN', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TESTCFG_STTLFAST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TESTCFG_STTLFAST, self).__init__(register,
            'STTLFAST', 'CSEN.TESTCFG.STTLFAST', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TESTCFG_SSCALON(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TESTCFG_SSCALON, self).__init__(register,
            'SSCALON', 'CSEN.TESTCFG.SSCALON', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_TESTCFG_VRAMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_TESTCFG_VRAMP, self).__init__(register,
            'VRAMP', 'CSEN.TESTCFG.VRAMP', 'read-write',
            "",
            30, 2,
            RM_Enum_CSEN_TESTCFG_VRAMP(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IF_CMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IF_CMP, self).__init__(register,
            'CMP', 'CSEN.IF.CMP', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IF_CONV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IF_CONV, self).__init__(register,
            'CONV', 'CSEN.IF.CONV', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IF_EOS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IF_EOS, self).__init__(register,
            'EOS', 'CSEN.IF.EOS', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IF_DMAOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IF_DMAOF, self).__init__(register,
            'DMAOF', 'CSEN.IF.DMAOF', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IF_APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IF_APORTCONFLICT, self).__init__(register,
            'APORTCONFLICT', 'CSEN.IF.APORTCONFLICT', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IFS_CMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IFS_CMP, self).__init__(register,
            'CMP', 'CSEN.IFS.CMP', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IFS_CONV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IFS_CONV, self).__init__(register,
            'CONV', 'CSEN.IFS.CONV', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IFS_EOS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IFS_EOS, self).__init__(register,
            'EOS', 'CSEN.IFS.EOS', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IFS_DMAOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IFS_DMAOF, self).__init__(register,
            'DMAOF', 'CSEN.IFS.DMAOF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IFS_APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IFS_APORTCONFLICT, self).__init__(register,
            'APORTCONFLICT', 'CSEN.IFS.APORTCONFLICT', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IFC_CMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IFC_CMP, self).__init__(register,
            'CMP', 'CSEN.IFC.CMP', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IFC_CONV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IFC_CONV, self).__init__(register,
            'CONV', 'CSEN.IFC.CONV', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IFC_EOS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IFC_EOS, self).__init__(register,
            'EOS', 'CSEN.IFC.EOS', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IFC_DMAOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IFC_DMAOF, self).__init__(register,
            'DMAOF', 'CSEN.IFC.DMAOF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IFC_APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IFC_APORTCONFLICT, self).__init__(register,
            'APORTCONFLICT', 'CSEN.IFC.APORTCONFLICT', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IEN_CMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IEN_CMP, self).__init__(register,
            'CMP', 'CSEN.IEN.CMP', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IEN_CONV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IEN_CONV, self).__init__(register,
            'CONV', 'CSEN.IEN.CONV', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IEN_EOS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IEN_EOS, self).__init__(register,
            'EOS', 'CSEN.IEN.EOS', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IEN_DMAOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IEN_DMAOF, self).__init__(register,
            'DMAOF', 'CSEN.IEN.DMAOF', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CSEN_IEN_APORTCONFLICT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CSEN_IEN_APORTCONFLICT, self).__init__(register,
            'APORTCONFLICT', 'CSEN.IEN.APORTCONFLICT', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


