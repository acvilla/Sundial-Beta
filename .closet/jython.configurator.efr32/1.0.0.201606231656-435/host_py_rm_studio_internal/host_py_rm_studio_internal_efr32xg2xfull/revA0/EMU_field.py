
from static import Base_RM_Field
from EMU_enum import *


class RM_Field_EMU_CTRL_EM23VREG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_CTRL_EM23VREG, self).__init__(register,
            'EM23VREG', 'EMU.CTRL.EM23VREG', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_CTRL_EM2BLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_CTRL_EM2BLOCK, self).__init__(register,
            'EM2BLOCK', 'EMU.CTRL.EM2BLOCK', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_CTRL_EM2BODDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_CTRL_EM2BODDIS, self).__init__(register,
            'EM2BODDIS', 'EMU.CTRL.EM2BODDIS', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_CTRL_EM01LD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_CTRL_EM01LD, self).__init__(register,
            'EM01LD', 'EMU.CTRL.EM01LD', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_CTRL_EM23VSCALEAUTOWSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_CTRL_EM23VSCALEAUTOWSEN, self).__init__(register,
            'EM23VSCALEAUTOWSEN', 'EMU.CTRL.EM23VSCALEAUTOWSEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_CTRL_EM23VSCALE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_CTRL_EM23VSCALE, self).__init__(register,
            'EM23VSCALE', 'EMU.CTRL.EM23VSCALE', 'read-write',
            "",
            8, 2,
            RM_Enum_EMU_CTRL_EM23VSCALE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_CTRL_EM4HVSCALE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_CTRL_EM4HVSCALE, self).__init__(register,
            'EM4HVSCALE', 'EMU.CTRL.EM4HVSCALE', 'read-write',
            "",
            16, 2,
            RM_Enum_EMU_CTRL_EM4HVSCALE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_VMONRDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_VMONRDY, self).__init__(register,
            'VMONRDY', 'EMU.STATUS.VMONRDY', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_VMONAVDD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_VMONAVDD, self).__init__(register,
            'VMONAVDD', 'EMU.STATUS.VMONAVDD', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_VMONALTAVDD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_VMONALTAVDD, self).__init__(register,
            'VMONALTAVDD', 'EMU.STATUS.VMONALTAVDD', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_VMONDVDD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_VMONDVDD, self).__init__(register,
            'VMONDVDD', 'EMU.STATUS.VMONDVDD', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_VMONIO0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_VMONIO0, self).__init__(register,
            'VMONIO0', 'EMU.STATUS.VMONIO0', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_VMONFVDD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_VMONFVDD, self).__init__(register,
            'VMONFVDD', 'EMU.STATUS.VMONFVDD', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_VSCALE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_VSCALE, self).__init__(register,
            'VSCALE', 'EMU.STATUS.VSCALE', 'read-only',
            "",
            16, 2,
            RM_Enum_EMU_STATUS_VSCALE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_VSCALEBUSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_VSCALEBUSY, self).__init__(register,
            'VSCALEBUSY', 'EMU.STATUS.VSCALEBUSY', 'read-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_EM4IORET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_EM4IORET, self).__init__(register,
            'EM4IORET', 'EMU.STATUS.EM4IORET', 'read-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_RACACTIVE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_RACACTIVE, self).__init__(register,
            'RACACTIVE', 'EMU.STATUS.RACACTIVE', 'read-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_TEMPACTIVE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_TEMPACTIVE, self).__init__(register,
            'TEMPACTIVE', 'EMU.STATUS.TEMPACTIVE', 'read-only',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_CALACTIVE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_CALACTIVE, self).__init__(register,
            'CALACTIVE', 'EMU.STATUS.CALACTIVE', 'read-only',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_CALCOMPOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_CALCOMPOUT, self).__init__(register,
            'CALCOMPOUT', 'EMU.STATUS.CALCOMPOUT', 'read-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_BCLFRCOENS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_BCLFRCOENS, self).__init__(register,
            'BCLFRCOENS', 'EMU.STATUS.BCLFRCOENS', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATUS_BCLFRCORDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATUS_BCLFRCORDY, self).__init__(register,
            'BCLFRCORDY', 'EMU.STATUS.BCLFRCORDY', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_LOCK_LOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_LOCK_LOCKKEY, self).__init__(register,
            'LOCKKEY', 'EMU.LOCK.LOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_EMU_LOCK_LOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RAM0CTRL_RAMPOWERDOWN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RAM0CTRL_RAMPOWERDOWN, self).__init__(register,
            'RAMPOWERDOWN', 'EMU.RAM0CTRL.RAMPOWERDOWN', 'read-write',
            "",
            0, 4,
            RM_Enum_EMU_RAM0CTRL_RAMPOWERDOWN(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RAM0CTRL_SEQRAMPOWERDOWN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RAM0CTRL_SEQRAMPOWERDOWN, self).__init__(register,
            'SEQRAMPOWERDOWN', 'EMU.RAM0CTRL.SEQRAMPOWERDOWN', 'read-write',
            "",
            30, 2,
            RM_Enum_EMU_RAM0CTRL_SEQRAMPOWERDOWN(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_CMD_EM4UNLATCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_CMD_EM4UNLATCH, self).__init__(register,
            'EM4UNLATCH', 'EMU.CMD.EM4UNLATCH', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_CMD_LDREFEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_CMD_LDREFEN, self).__init__(register,
            'LDREFEN', 'EMU.CMD.LDREFEN', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_CMD_EM01VSCALE0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_CMD_EM01VSCALE0, self).__init__(register,
            'EM01VSCALE0', 'EMU.CMD.EM01VSCALE0', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_CMD_EM01VSCALE1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_CMD_EM01VSCALE1, self).__init__(register,
            'EM01VSCALE1', 'EMU.CMD.EM01VSCALE1', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_CMD_EM01VSCALE2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_CMD_EM01VSCALE2, self).__init__(register,
            'EM01VSCALE2', 'EMU.CMD.EM01VSCALE2', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PERACTCONF_RACPER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PERACTCONF_RACPER, self).__init__(register,
            'RACPER', 'EMU.PERACTCONF.RACPER', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM4CTRL_EM4STATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM4CTRL_EM4STATE, self).__init__(register,
            'EM4STATE', 'EMU.EM4CTRL.EM4STATE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM4CTRL_RETAINLFRCO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM4CTRL_RETAINLFRCO, self).__init__(register,
            'RETAINLFRCO', 'EMU.EM4CTRL.RETAINLFRCO', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM4CTRL_RETAINLFXO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM4CTRL_RETAINLFXO, self).__init__(register,
            'RETAINLFXO', 'EMU.EM4CTRL.RETAINLFXO', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM4CTRL_RETAINULFRCO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM4CTRL_RETAINULFRCO, self).__init__(register,
            'RETAINULFRCO', 'EMU.EM4CTRL.RETAINULFRCO', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM4CTRL_EM4IORETMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM4CTRL_EM4IORETMODE, self).__init__(register,
            'EM4IORETMODE', 'EMU.EM4CTRL.EM4IORETMODE', 'read-write',
            "",
            4, 2,
            RM_Enum_EMU_EM4CTRL_EM4IORETMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM4CTRL_EM4ENTRY_CMU_HS_TO_DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM4CTRL_EM4ENTRY_CMU_HS_TO_DIS, self).__init__(register,
            'EM4ENTRY_CMU_HS_TO_DIS', 'EMU.EM4CTRL.EM4ENTRY_CMU_HS_TO_DIS', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM4CTRL_EM4ENTRY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM4CTRL_EM4ENTRY, self).__init__(register,
            'EM4ENTRY', 'EMU.EM4CTRL.EM4ENTRY', 'write-only',
            "",
            16, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPLIMITS_TEMPLOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPLIMITS_TEMPLOW, self).__init__(register,
            'TEMPLOW', 'EMU.TEMPLIMITS.TEMPLOW', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPLIMITS_TEMPHIGH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPLIMITS_TEMPHIGH, self).__init__(register,
            'TEMPHIGH', 'EMU.TEMPLIMITS.TEMPHIGH', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPLIMITS_EM4WUEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPLIMITS_EM4WUEN, self).__init__(register,
            'EM4WUEN', 'EMU.TEMPLIMITS.EM4WUEN', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMP_TEMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMP_TEMP, self).__init__(register,
            'TEMP', 'EMU.TEMP.TEMP', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_VMONAVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_VMONAVDDFALL, self).__init__(register,
            'VMONAVDDFALL', 'EMU.IF.VMONAVDDFALL', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_VMONAVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_VMONAVDDRISE, self).__init__(register,
            'VMONAVDDRISE', 'EMU.IF.VMONAVDDRISE', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_VMONALTAVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_VMONALTAVDDFALL, self).__init__(register,
            'VMONALTAVDDFALL', 'EMU.IF.VMONALTAVDDFALL', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_VMONALTAVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_VMONALTAVDDRISE, self).__init__(register,
            'VMONALTAVDDRISE', 'EMU.IF.VMONALTAVDDRISE', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_VMONDVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_VMONDVDDFALL, self).__init__(register,
            'VMONDVDDFALL', 'EMU.IF.VMONDVDDFALL', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_VMONDVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_VMONDVDDRISE, self).__init__(register,
            'VMONDVDDRISE', 'EMU.IF.VMONDVDDRISE', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_VMONIO0FALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_VMONIO0FALL, self).__init__(register,
            'VMONIO0FALL', 'EMU.IF.VMONIO0FALL', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_VMONIO0RISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_VMONIO0RISE, self).__init__(register,
            'VMONIO0RISE', 'EMU.IF.VMONIO0RISE', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_VMONFVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_VMONFVDDFALL, self).__init__(register,
            'VMONFVDDFALL', 'EMU.IF.VMONFVDDFALL', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_VMONFVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_VMONFVDDRISE, self).__init__(register,
            'VMONFVDDRISE', 'EMU.IF.VMONFVDDRISE', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_PFETOVERCURRENTLIMIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_PFETOVERCURRENTLIMIT, self).__init__(register,
            'PFETOVERCURRENTLIMIT', 'EMU.IF.PFETOVERCURRENTLIMIT', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_NFETOVERCURRENTLIMIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_NFETOVERCURRENTLIMIT, self).__init__(register,
            'NFETOVERCURRENTLIMIT', 'EMU.IF.NFETOVERCURRENTLIMIT', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_DCDCLPRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_DCDCLPRUNNING, self).__init__(register,
            'DCDCLPRUNNING', 'EMU.IF.DCDCLPRUNNING', 'read-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_DCDCLNRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_DCDCLNRUNNING, self).__init__(register,
            'DCDCLNRUNNING', 'EMU.IF.DCDCLNRUNNING', 'read-only',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_DCDCINBYPASS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_DCDCINBYPASS, self).__init__(register,
            'DCDCINBYPASS', 'EMU.IF.DCDCINBYPASS', 'read-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_EM23WAKEUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_EM23WAKEUP, self).__init__(register,
            'EM23WAKEUP', 'EMU.IF.EM23WAKEUP', 'read-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_VSCALEDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_VSCALEDONE, self).__init__(register,
            'VSCALEDONE', 'EMU.IF.VSCALEDONE', 'read-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_TEMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_TEMP, self).__init__(register,
            'TEMP', 'EMU.IF.TEMP', 'read-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_TEMPLOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_TEMPLOW, self).__init__(register,
            'TEMPLOW', 'EMU.IF.TEMPLOW', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IF_TEMPHIGH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IF_TEMPHIGH, self).__init__(register,
            'TEMPHIGH', 'EMU.IF.TEMPHIGH', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_VMONAVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_VMONAVDDFALL, self).__init__(register,
            'VMONAVDDFALL', 'EMU.IFS.VMONAVDDFALL', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_VMONAVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_VMONAVDDRISE, self).__init__(register,
            'VMONAVDDRISE', 'EMU.IFS.VMONAVDDRISE', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_VMONALTAVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_VMONALTAVDDFALL, self).__init__(register,
            'VMONALTAVDDFALL', 'EMU.IFS.VMONALTAVDDFALL', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_VMONALTAVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_VMONALTAVDDRISE, self).__init__(register,
            'VMONALTAVDDRISE', 'EMU.IFS.VMONALTAVDDRISE', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_VMONDVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_VMONDVDDFALL, self).__init__(register,
            'VMONDVDDFALL', 'EMU.IFS.VMONDVDDFALL', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_VMONDVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_VMONDVDDRISE, self).__init__(register,
            'VMONDVDDRISE', 'EMU.IFS.VMONDVDDRISE', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_VMONIO0FALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_VMONIO0FALL, self).__init__(register,
            'VMONIO0FALL', 'EMU.IFS.VMONIO0FALL', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_VMONIO0RISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_VMONIO0RISE, self).__init__(register,
            'VMONIO0RISE', 'EMU.IFS.VMONIO0RISE', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_VMONFVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_VMONFVDDFALL, self).__init__(register,
            'VMONFVDDFALL', 'EMU.IFS.VMONFVDDFALL', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_VMONFVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_VMONFVDDRISE, self).__init__(register,
            'VMONFVDDRISE', 'EMU.IFS.VMONFVDDRISE', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_PFETOVERCURRENTLIMIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_PFETOVERCURRENTLIMIT, self).__init__(register,
            'PFETOVERCURRENTLIMIT', 'EMU.IFS.PFETOVERCURRENTLIMIT', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_NFETOVERCURRENTLIMIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_NFETOVERCURRENTLIMIT, self).__init__(register,
            'NFETOVERCURRENTLIMIT', 'EMU.IFS.NFETOVERCURRENTLIMIT', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_DCDCLPRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_DCDCLPRUNNING, self).__init__(register,
            'DCDCLPRUNNING', 'EMU.IFS.DCDCLPRUNNING', 'write-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_DCDCLNRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_DCDCLNRUNNING, self).__init__(register,
            'DCDCLNRUNNING', 'EMU.IFS.DCDCLNRUNNING', 'write-only',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_DCDCINBYPASS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_DCDCINBYPASS, self).__init__(register,
            'DCDCINBYPASS', 'EMU.IFS.DCDCINBYPASS', 'write-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_EM23WAKEUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_EM23WAKEUP, self).__init__(register,
            'EM23WAKEUP', 'EMU.IFS.EM23WAKEUP', 'write-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_VSCALEDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_VSCALEDONE, self).__init__(register,
            'VSCALEDONE', 'EMU.IFS.VSCALEDONE', 'write-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_TEMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_TEMP, self).__init__(register,
            'TEMP', 'EMU.IFS.TEMP', 'write-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_TEMPLOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_TEMPLOW, self).__init__(register,
            'TEMPLOW', 'EMU.IFS.TEMPLOW', 'write-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFS_TEMPHIGH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFS_TEMPHIGH, self).__init__(register,
            'TEMPHIGH', 'EMU.IFS.TEMPHIGH', 'write-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_VMONAVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_VMONAVDDFALL, self).__init__(register,
            'VMONAVDDFALL', 'EMU.IFC.VMONAVDDFALL', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_VMONAVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_VMONAVDDRISE, self).__init__(register,
            'VMONAVDDRISE', 'EMU.IFC.VMONAVDDRISE', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_VMONALTAVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_VMONALTAVDDFALL, self).__init__(register,
            'VMONALTAVDDFALL', 'EMU.IFC.VMONALTAVDDFALL', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_VMONALTAVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_VMONALTAVDDRISE, self).__init__(register,
            'VMONALTAVDDRISE', 'EMU.IFC.VMONALTAVDDRISE', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_VMONDVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_VMONDVDDFALL, self).__init__(register,
            'VMONDVDDFALL', 'EMU.IFC.VMONDVDDFALL', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_VMONDVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_VMONDVDDRISE, self).__init__(register,
            'VMONDVDDRISE', 'EMU.IFC.VMONDVDDRISE', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_VMONIO0FALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_VMONIO0FALL, self).__init__(register,
            'VMONIO0FALL', 'EMU.IFC.VMONIO0FALL', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_VMONIO0RISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_VMONIO0RISE, self).__init__(register,
            'VMONIO0RISE', 'EMU.IFC.VMONIO0RISE', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_VMONFVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_VMONFVDDFALL, self).__init__(register,
            'VMONFVDDFALL', 'EMU.IFC.VMONFVDDFALL', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_VMONFVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_VMONFVDDRISE, self).__init__(register,
            'VMONFVDDRISE', 'EMU.IFC.VMONFVDDRISE', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_PFETOVERCURRENTLIMIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_PFETOVERCURRENTLIMIT, self).__init__(register,
            'PFETOVERCURRENTLIMIT', 'EMU.IFC.PFETOVERCURRENTLIMIT', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_NFETOVERCURRENTLIMIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_NFETOVERCURRENTLIMIT, self).__init__(register,
            'NFETOVERCURRENTLIMIT', 'EMU.IFC.NFETOVERCURRENTLIMIT', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_DCDCLPRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_DCDCLPRUNNING, self).__init__(register,
            'DCDCLPRUNNING', 'EMU.IFC.DCDCLPRUNNING', 'write-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_DCDCLNRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_DCDCLNRUNNING, self).__init__(register,
            'DCDCLNRUNNING', 'EMU.IFC.DCDCLNRUNNING', 'write-only',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_DCDCINBYPASS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_DCDCINBYPASS, self).__init__(register,
            'DCDCINBYPASS', 'EMU.IFC.DCDCINBYPASS', 'write-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_EM23WAKEUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_EM23WAKEUP, self).__init__(register,
            'EM23WAKEUP', 'EMU.IFC.EM23WAKEUP', 'write-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_VSCALEDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_VSCALEDONE, self).__init__(register,
            'VSCALEDONE', 'EMU.IFC.VSCALEDONE', 'write-only',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_TEMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_TEMP, self).__init__(register,
            'TEMP', 'EMU.IFC.TEMP', 'write-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_TEMPLOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_TEMPLOW, self).__init__(register,
            'TEMPLOW', 'EMU.IFC.TEMPLOW', 'write-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IFC_TEMPHIGH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IFC_TEMPHIGH, self).__init__(register,
            'TEMPHIGH', 'EMU.IFC.TEMPHIGH', 'write-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_VMONAVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_VMONAVDDFALL, self).__init__(register,
            'VMONAVDDFALL', 'EMU.IEN.VMONAVDDFALL', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_VMONAVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_VMONAVDDRISE, self).__init__(register,
            'VMONAVDDRISE', 'EMU.IEN.VMONAVDDRISE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_VMONALTAVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_VMONALTAVDDFALL, self).__init__(register,
            'VMONALTAVDDFALL', 'EMU.IEN.VMONALTAVDDFALL', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_VMONALTAVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_VMONALTAVDDRISE, self).__init__(register,
            'VMONALTAVDDRISE', 'EMU.IEN.VMONALTAVDDRISE', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_VMONDVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_VMONDVDDFALL, self).__init__(register,
            'VMONDVDDFALL', 'EMU.IEN.VMONDVDDFALL', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_VMONDVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_VMONDVDDRISE, self).__init__(register,
            'VMONDVDDRISE', 'EMU.IEN.VMONDVDDRISE', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_VMONIO0FALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_VMONIO0FALL, self).__init__(register,
            'VMONIO0FALL', 'EMU.IEN.VMONIO0FALL', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_VMONIO0RISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_VMONIO0RISE, self).__init__(register,
            'VMONIO0RISE', 'EMU.IEN.VMONIO0RISE', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_VMONFVDDFALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_VMONFVDDFALL, self).__init__(register,
            'VMONFVDDFALL', 'EMU.IEN.VMONFVDDFALL', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_VMONFVDDRISE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_VMONFVDDRISE, self).__init__(register,
            'VMONFVDDRISE', 'EMU.IEN.VMONFVDDRISE', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_PFETOVERCURRENTLIMIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_PFETOVERCURRENTLIMIT, self).__init__(register,
            'PFETOVERCURRENTLIMIT', 'EMU.IEN.PFETOVERCURRENTLIMIT', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_NFETOVERCURRENTLIMIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_NFETOVERCURRENTLIMIT, self).__init__(register,
            'NFETOVERCURRENTLIMIT', 'EMU.IEN.NFETOVERCURRENTLIMIT', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_DCDCLPRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_DCDCLPRUNNING, self).__init__(register,
            'DCDCLPRUNNING', 'EMU.IEN.DCDCLPRUNNING', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_DCDCLNRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_DCDCLNRUNNING, self).__init__(register,
            'DCDCLNRUNNING', 'EMU.IEN.DCDCLNRUNNING', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_DCDCINBYPASS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_DCDCINBYPASS, self).__init__(register,
            'DCDCINBYPASS', 'EMU.IEN.DCDCINBYPASS', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_EM23WAKEUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_EM23WAKEUP, self).__init__(register,
            'EM23WAKEUP', 'EMU.IEN.EM23WAKEUP', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_VSCALEDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_VSCALEDONE, self).__init__(register,
            'VSCALEDONE', 'EMU.IEN.VSCALEDONE', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_TEMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_TEMP, self).__init__(register,
            'TEMP', 'EMU.IEN.TEMP', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_TEMPLOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_TEMPLOW, self).__init__(register,
            'TEMPLOW', 'EMU.IEN.TEMPLOW', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_IEN_TEMPHIGH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_IEN_TEMPHIGH, self).__init__(register,
            'TEMPHIGH', 'EMU.IEN.TEMPHIGH', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PWRLOCK_LOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PWRLOCK_LOCKKEY, self).__init__(register,
            'LOCKKEY', 'EMU.PWRLOCK.LOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_EMU_PWRLOCK_LOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PWRCFG_PWRCFG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PWRCFG_PWRCFG, self).__init__(register,
            'PWRCFG', 'EMU.PWRCFG.PWRCFG', 'read-write',
            "",
            0, 4,
            RM_Enum_EMU_PWRCFG_PWRCFG(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PWRCTRL_ANASW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PWRCTRL_ANASW, self).__init__(register,
            'ANASW', 'EMU.PWRCTRL.ANASW', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PWRCTRL_REGDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PWRCTRL_REGDIS, self).__init__(register,
            'REGDIS', 'EMU.PWRCTRL.REGDIS', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PWRCTRL_DCDCPWRSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PWRCTRL_DCDCPWRSEL, self).__init__(register,
            'DCDCPWRSEL', 'EMU.PWRCTRL.DCDCPWRSEL', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PWRCTRL_DCDCVREGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PWRCTRL_DCDCVREGSEL, self).__init__(register,
            'DCDCVREGSEL', 'EMU.PWRCTRL.DCDCVREGSEL', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PWRCTRL_REGPWRSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PWRCTRL_REGPWRSEL, self).__init__(register,
            'REGPWRSEL', 'EMU.PWRCTRL.REGPWRSEL', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PWRCTRL_DVDDBODDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PWRCTRL_DVDDBODDIS, self).__init__(register,
            'DVDDBODDIS', 'EMU.PWRCTRL.DVDDBODDIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCCTRL_DCDCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCCTRL_DCDCMODE, self).__init__(register,
            'DCDCMODE', 'EMU.DCDCCTRL.DCDCMODE', 'read-write',
            "",
            0, 2,
            RM_Enum_EMU_DCDCCTRL_DCDCMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCCTRL_DCDCMODEEM23(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCCTRL_DCDCMODEEM23, self).__init__(register,
            'DCDCMODEEM23', 'EMU.DCDCCTRL.DCDCMODEEM23', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCCTRL_DCDCMODEEM4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCCTRL_DCDCMODEEM4, self).__init__(register,
            'DCDCMODEEM4', 'EMU.DCDCCTRL.DCDCMODEEM4', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCCTRL_LPSTANDBYDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCCTRL_LPSTANDBYDIS, self).__init__(register,
            'LPSTANDBYDIS', 'EMU.DCDCCTRL.LPSTANDBYDIS', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCCTRL_LNSTANDBY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCCTRL_LNSTANDBY, self).__init__(register,
            'LNSTANDBY', 'EMU.DCDCCTRL.LNSTANDBY', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCCTRL_LOWPOWERSKIP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCCTRL_LOWPOWERSKIP, self).__init__(register,
            'LOWPOWERSKIP', 'EMU.DCDCCTRL.LOWPOWERSKIP', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSMCTRL_LPCMPWAITDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSMCTRL_LPCMPWAITDIS, self).__init__(register,
            'LPCMPWAITDIS', 'EMU.DCDCSMCTRL.LPCMPWAITDIS', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSWCTRL_SWDAMPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSWCTRL_SWDAMPEN, self).__init__(register,
            'SWDAMPEN', 'EMU.DCDCSWCTRL.SWDAMPEN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSWCTRL_SWNFETOFF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSWCTRL_SWNFETOFF, self).__init__(register,
            'SWNFETOFF', 'EMU.DCDCSWCTRL.SWNFETOFF', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSWCTRL_PWMDTIME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSWCTRL_PWMDTIME, self).__init__(register,
            'PWMDTIME', 'EMU.DCDCSWCTRL.PWMDTIME', 'read-write',
            "",
            4, 10)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSWCTRL_PWMMIND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSWCTRL_PWMMIND, self).__init__(register,
            'PWMMIND', 'EMU.DCDCSWCTRL.PWMMIND', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSWCTRL_PWMMAXD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSWCTRL_PWMMAXD, self).__init__(register,
            'PWMMAXD', 'EMU.DCDCSWCTRL.PWMMAXD', 'read-write',
            "",
            16, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCMISCCTRL_LNFORCECCM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCMISCCTRL_LNFORCECCM, self).__init__(register,
            'LNFORCECCM', 'EMU.DCDCMISCCTRL.LNFORCECCM', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCMISCCTRL_LPCMPHYSDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCMISCCTRL_LPCMPHYSDIS, self).__init__(register,
            'LPCMPHYSDIS', 'EMU.DCDCMISCCTRL.LPCMPHYSDIS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCMISCCTRL_LPCMPHYSHI(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCMISCCTRL_LPCMPHYSHI, self).__init__(register,
            'LPCMPHYSHI', 'EMU.DCDCMISCCTRL.LPCMPHYSHI', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCMISCCTRL_ZDETINTONLY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCMISCCTRL_ZDETINTONLY, self).__init__(register,
            'ZDETINTONLY', 'EMU.DCDCMISCCTRL.ZDETINTONLY', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCMISCCTRL_CLIMINTONLY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCMISCCTRL_CLIMINTONLY, self).__init__(register,
            'CLIMINTONLY', 'EMU.DCDCMISCCTRL.CLIMINTONLY', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCMISCCTRL_LNFORCECCMIMM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCMISCCTRL_LNFORCECCMIMM, self).__init__(register,
            'LNFORCECCMIMM', 'EMU.DCDCMISCCTRL.LNFORCECCMIMM', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCMISCCTRL_PFETCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCMISCCTRL_PFETCNT, self).__init__(register,
            'PFETCNT', 'EMU.DCDCMISCCTRL.PFETCNT', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCMISCCTRL_NFETCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCMISCCTRL_NFETCNT, self).__init__(register,
            'NFETCNT', 'EMU.DCDCMISCCTRL.NFETCNT', 'read-write',
            "",
            12, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCMISCCTRL_BYPLIMSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCMISCCTRL_BYPLIMSEL, self).__init__(register,
            'BYPLIMSEL', 'EMU.DCDCMISCCTRL.BYPLIMSEL', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCMISCCTRL_LPCLIMILIMSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCMISCCTRL_LPCLIMILIMSEL, self).__init__(register,
            'LPCLIMILIMSEL', 'EMU.DCDCMISCCTRL.LPCLIMILIMSEL', 'read-write',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCMISCCTRL_LNCLIMILIMSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCMISCCTRL_LNCLIMILIMSEL, self).__init__(register,
            'LNCLIMILIMSEL', 'EMU.DCDCMISCCTRL.LNCLIMILIMSEL', 'read-write',
            "",
            24, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCMISCCTRL_LPCMPBIASEM234H(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCMISCCTRL_LPCMPBIASEM234H, self).__init__(register,
            'LPCMPBIASEM234H', 'EMU.DCDCMISCCTRL.LPCMPBIASEM234H', 'read-write',
            "",
            28, 2,
            RM_Enum_EMU_DCDCMISCCTRL_LPCMPBIASEM234H(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCZDETCTRL_ZDETDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCZDETCTRL_ZDETDIS, self).__init__(register,
            'ZDETDIS', 'EMU.DCDCZDETCTRL.ZDETDIS', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCZDETCTRL_ZDETILIMSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCZDETCTRL_ZDETILIMSEL, self).__init__(register,
            'ZDETILIMSEL', 'EMU.DCDCZDETCTRL.ZDETILIMSEL', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCZDETCTRL_ZDETBLANKDLY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCZDETCTRL_ZDETBLANKDLY, self).__init__(register,
            'ZDETBLANKDLY', 'EMU.DCDCZDETCTRL.ZDETBLANKDLY', 'read-write',
            "",
            8, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCCLIMCTRL_CLIMDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCCLIMCTRL_CLIMDIS, self).__init__(register,
            'CLIMDIS', 'EMU.DCDCCLIMCTRL.CLIMDIS', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCCLIMCTRL_CLIMBLANKDLY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCCLIMCTRL_CLIMBLANKDLY, self).__init__(register,
            'CLIMBLANKDLY', 'EMU.DCDCCLIMCTRL.CLIMBLANKDLY', 'read-write',
            "",
            8, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCCLIMCTRL_BYPLIMEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCCLIMCTRL_BYPLIMEN, self).__init__(register,
            'BYPLIMEN', 'EMU.DCDCCLIMCTRL.BYPLIMEN', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLNCOMPCTRL_COMPENR1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLNCOMPCTRL_COMPENR1, self).__init__(register,
            'COMPENR1', 'EMU.DCDCLNCOMPCTRL.COMPENR1', 'read-write',
            "",
            0, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLNCOMPCTRL_COMPENR2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLNCOMPCTRL_COMPENR2, self).__init__(register,
            'COMPENR2', 'EMU.DCDCLNCOMPCTRL.COMPENR2', 'read-write',
            "",
            4, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLNCOMPCTRL_COMPENR3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLNCOMPCTRL_COMPENR3, self).__init__(register,
            'COMPENR3', 'EMU.DCDCLNCOMPCTRL.COMPENR3', 'read-write',
            "",
            12, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLNCOMPCTRL_COMPENC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLNCOMPCTRL_COMPENC1, self).__init__(register,
            'COMPENC1', 'EMU.DCDCLNCOMPCTRL.COMPENC1', 'read-write',
            "",
            20, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLNCOMPCTRL_COMPENC2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLNCOMPCTRL_COMPENC2, self).__init__(register,
            'COMPENC2', 'EMU.DCDCLNCOMPCTRL.COMPENC2', 'read-write',
            "",
            24, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLNCOMPCTRL_COMPENC3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLNCOMPCTRL_COMPENC3, self).__init__(register,
            'COMPENC3', 'EMU.DCDCLNCOMPCTRL.COMPENC3', 'read-write',
            "",
            28, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLNVCTRL_LNATT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLNVCTRL_LNATT, self).__init__(register,
            'LNATT', 'EMU.DCDCLNVCTRL.LNATT', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLNVCTRL_LNVREF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLNVCTRL_LNVREF, self).__init__(register,
            'LNVREF', 'EMU.DCDCLNVCTRL.LNVREF', 'read-write',
            "",
            8, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTIMING_LPINITWAIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTIMING_LPINITWAIT, self).__init__(register,
            'LPINITWAIT', 'EMU.DCDCTIMING.LPINITWAIT', 'read-write',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTIMING_LPCMPBLANKWAIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTIMING_LPCMPBLANKWAIT, self).__init__(register,
            'LPCMPBLANKWAIT', 'EMU.DCDCTIMING.LPCMPBLANKWAIT', 'read-write',
            "",
            9, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTIMING_COMPENPRCHGEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTIMING_COMPENPRCHGEN, self).__init__(register,
            'COMPENPRCHGEN', 'EMU.DCDCTIMING.COMPENPRCHGEN', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTIMING_LNWAIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTIMING_LNWAIT, self).__init__(register,
            'LNWAIT', 'EMU.DCDCTIMING.LNWAIT', 'read-write',
            "",
            12, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTIMING_BYPWAIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTIMING_BYPWAIT, self).__init__(register,
            'BYPWAIT', 'EMU.DCDCTIMING.BYPWAIT', 'read-write',
            "",
            20, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTIMING_PWMRETIME(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTIMING_PWMRETIME, self).__init__(register,
            'PWMRETIME', 'EMU.DCDCTIMING.PWMRETIME', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTIMING_DUTYSCALE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTIMING_DUTYSCALE, self).__init__(register,
            'DUTYSCALE', 'EMU.DCDCTIMING.DUTYSCALE', 'read-write',
            "",
            29, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLPVCTRL_LPATT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLPVCTRL_LPATT, self).__init__(register,
            'LPATT', 'EMU.DCDCLPVCTRL.LPATT', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLPVCTRL_LPVREF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLPVCTRL_LPVREF, self).__init__(register,
            'LPVREF', 'EMU.DCDCLPVCTRL.LPVREF', 'read-write',
            "",
            1, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLPFREQCTRL_LPOSCDIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLPFREQCTRL_LPOSCDIV, self).__init__(register,
            'LPOSCDIV', 'EMU.DCDCLPFREQCTRL.LPOSCDIV', 'read-write',
            "",
            0, 2,
            RM_Enum_EMU_DCDCLPFREQCTRL_LPOSCDIV(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLPCTRL_LPCMPHYSSELEM234H(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLPCTRL_LPCMPHYSSELEM234H, self).__init__(register,
            'LPCMPHYSSELEM234H', 'EMU.DCDCLPCTRL.LPCMPHYSSELEM234H', 'read-write',
            "",
            12, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLPCTRL_LPPUMPDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLPCTRL_LPPUMPDIS, self).__init__(register,
            'LPPUMPDIS', 'EMU.DCDCLPCTRL.LPPUMPDIS', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLPCTRL_LPOSCLSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLPCTRL_LPOSCLSSEL, self).__init__(register,
            'LPOSCLSSEL', 'EMU.DCDCLPCTRL.LPOSCLSSEL', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLPCTRL_LPVREFDUTYEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLPCTRL_LPVREFDUTYEN, self).__init__(register,
            'LPVREFDUTYEN', 'EMU.DCDCLPCTRL.LPVREFDUTYEN', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLPCTRL_LPBLANK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLPCTRL_LPBLANK, self).__init__(register,
            'LPBLANK', 'EMU.DCDCLPCTRL.LPBLANK', 'read-write',
            "",
            25, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLNFREQCTRL_RCOBAND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLNFREQCTRL_RCOBAND, self).__init__(register,
            'RCOBAND', 'EMU.DCDCLNFREQCTRL.RCOBAND', 'read-write',
            "",
            0, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLNFREQCTRL_RCOTRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLNFREQCTRL_RCOTRIM, self).__init__(register,
            'RCOTRIM', 'EMU.DCDCLNFREQCTRL.RCOTRIM', 'read-write',
            "",
            24, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCRCOSC_RCOSYNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCRCOSC_RCOSYNC, self).__init__(register,
            'RCOSYNC', 'EMU.DCDCRCOSC.RCOSYNC', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCRCOSC_RCOHOPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCRCOSC_RCOHOPEN, self).__init__(register,
            'RCOHOPEN', 'EMU.DCDCRCOSC.RCOHOPEN', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCRCOSC_RCOHOPPERIOD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCRCOSC_RCOHOPPERIOD, self).__init__(register,
            'RCOHOPPERIOD', 'EMU.DCDCRCOSC.RCOHOPPERIOD', 'read-write',
            "",
            16, 2,
            RM_Enum_EMU_DCDCRCOSC_RCOHOPPERIOD(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCRCOSC_RCOHOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCRCOSC_RCOHOP, self).__init__(register,
            'RCOHOP', 'EMU.DCDCRCOSC.RCOHOP', 'read-write',
            "",
            20, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCRCOSC_RCOSPREAD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCRCOSC_RCOSPREAD, self).__init__(register,
            'RCOSPREAD', 'EMU.DCDCRCOSC.RCOSPREAD', 'read-write',
            "",
            28, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSYNC_DCDCCTRLBUSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSYNC_DCDCCTRLBUSY, self).__init__(register,
            'DCDCCTRLBUSY', 'EMU.DCDCSYNC.DCDCCTRLBUSY', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSTATUS_RCOCALOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSTATUS_RCOCALOUT, self).__init__(register,
            'RCOCALOUT', 'EMU.DCDCSTATUS.RCOCALOUT', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSTATUS_LPCMPOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSTATUS_LPCMPOUT, self).__init__(register,
            'LPCMPOUT', 'EMU.DCDCSTATUS.LPCMPOUT', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSTATUS_LPTESTCLK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSTATUS_LPTESTCLK, self).__init__(register,
            'LPTESTCLK', 'EMU.DCDCSTATUS.LPTESTCLK', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSTATUS_LPTESTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSTATUS_LPTESTSTATE, self).__init__(register,
            'LPTESTSTATE', 'EMU.DCDCSTATUS.LPTESTSTATE', 'read-only',
            "",
            3, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSTATUS_DCDCSMSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSTATUS_DCDCSMSTATE, self).__init__(register,
            'DCDCSMSTATE', 'EMU.DCDCSTATUS.DCDCSMSTATE', 'read-only',
            "",
            5, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSTATUS_PFETOVERCUR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSTATUS_PFETOVERCUR, self).__init__(register,
            'PFETOVERCUR', 'EMU.DCDCSTATUS.PFETOVERCUR', 'read-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSTATUS_NFETOVERCUR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSTATUS_NFETOVERCUR, self).__init__(register,
            'NFETOVERCUR', 'EMU.DCDCSTATUS.NFETOVERCUR', 'read-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSTATUS_LPTESTCMPRAW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSTATUS_LPTESTCMPRAW, self).__init__(register,
            'LPTESTCMPRAW', 'EMU.DCDCSTATUS.LPTESTCMPRAW', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSTATUS_LPRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSTATUS_LPRUNNING, self).__init__(register,
            'LPRUNNING', 'EMU.DCDCSTATUS.LPRUNNING', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSTATUS_LNRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSTATUS_LNRUNNING, self).__init__(register,
            'LNRUNNING', 'EMU.DCDCSTATUS.LNRUNNING', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCSTATUS_INBYPASS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCSTATUS_INBYPASS, self).__init__(register,
            'INBYPASS', 'EMU.DCDCSTATUS.INBYPASS', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTRIM0_PWMSKIP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTRIM0_PWMSKIP, self).__init__(register,
            'PWMSKIP', 'EMU.DCDCTRIM0.PWMSKIP', 'read-write',
            "",
            0, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTRIM0_RCORAMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTRIM0_RCORAMP, self).__init__(register,
            'RCORAMP', 'EMU.DCDCTRIM0.RCORAMP', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTRIM0_CLIMVOSTRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTRIM0_CLIMVOSTRIM, self).__init__(register,
            'CLIMVOSTRIM', 'EMU.DCDCTRIM0.CLIMVOSTRIM', 'read-write',
            "",
            7, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTRIM0_ZDETVOSTRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTRIM0_ZDETVOSTRIM, self).__init__(register,
            'ZDETVOSTRIM', 'EMU.DCDCTRIM0.ZDETVOSTRIM', 'read-write',
            "",
            10, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTRIM0_LPOSCTRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTRIM0_LPOSCTRIM, self).__init__(register,
            'LPOSCTRIM', 'EMU.DCDCTRIM0.LPOSCTRIM', 'read-write',
            "",
            15, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTRIM0_CLIMBIASTRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTRIM0_CLIMBIASTRIM, self).__init__(register,
            'CLIMBIASTRIM', 'EMU.DCDCTRIM0.CLIMBIASTRIM', 'read-write',
            "",
            19, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTRIM1_ZDETBIASTRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTRIM1_ZDETBIASTRIM, self).__init__(register,
            'ZDETBIASTRIM', 'EMU.DCDCTRIM1.ZDETBIASTRIM', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTRIM1_ZDET0XTRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTRIM1_ZDET0XTRIM, self).__init__(register,
            'ZDET0XTRIM', 'EMU.DCDCTRIM1.ZDET0XTRIM', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTRIM1_LPPFETCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTRIM1_LPPFETCNT, self).__init__(register,
            'LPPFETCNT', 'EMU.DCDCTRIM1.LPPFETCNT', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTRIM1_LPNFETCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTRIM1_LPNFETCNT, self).__init__(register,
            'LPNFETCNT', 'EMU.DCDCTRIM1.LPNFETCNT', 'read-write',
            "",
            20, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTRIM1_LPCLIMILIMSELRAMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTRIM1_LPCLIMILIMSELRAMP, self).__init__(register,
            'LPCLIMILIMSELRAMP', 'EMU.DCDCTRIM1.LPCLIMILIMSELRAMP', 'read-write',
            "",
            24, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTRIM1_BYPPFETEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTRIM1_BYPPFETEN, self).__init__(register,
            'BYPPFETEN', 'EMU.DCDCTRIM1.BYPPFETEN', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTRIM1_SWTRIMEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTRIM1_SWTRIMEN, self).__init__(register,
            'SWTRIMEN', 'EMU.DCDCTRIM1.SWTRIMEN', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_LPINIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_LPINIT, self).__init__(register,
            'LPINIT', 'EMU.DCDCTEST.LPINIT', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_LNPRECHARGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_LNPRECHARGE, self).__init__(register,
            'LNPRECHARGE', 'EMU.DCDCTEST.LNPRECHARGE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_PULSESEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_PULSESEL, self).__init__(register,
            'PULSESEL', 'EMU.DCDCTEST.PULSESEL', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_BYPASSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_BYPASSEN, self).__init__(register,
            'BYPASSEN', 'EMU.DCDCTEST.BYPASSEN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_LPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_LPEN, self).__init__(register,
            'LPEN', 'EMU.DCDCTEST.LPEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_LNEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_LNEN, self).__init__(register,
            'LNEN', 'EMU.DCDCTEST.LNEN', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_LPCMPHYSDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_LPCMPHYSDIS, self).__init__(register,
            'LPCMPHYSDIS', 'EMU.DCDCTEST.LPCMPHYSDIS', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_ZDETILIMEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_ZDETILIMEN, self).__init__(register,
            'ZDETILIMEN', 'EMU.DCDCTEST.ZDETILIMEN', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_LPPUMPDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_LPPUMPDIS, self).__init__(register,
            'LPPUMPDIS', 'EMU.DCDCTEST.LPPUMPDIS', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_SWTESTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_SWTESTEN, self).__init__(register,
            'SWTESTEN', 'EMU.DCDCTEST.SWTESTEN', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_LPTESTCMPBIAS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_LPTESTCMPBIAS, self).__init__(register,
            'LPTESTCMPBIAS', 'EMU.DCDCTEST.LPTESTCMPBIAS', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_SWTESTSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_SWTESTSTATE, self).__init__(register,
            'SWTESTSTATE', 'EMU.DCDCTEST.SWTESTSTATE', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_LPTEST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_LPTEST, self).__init__(register,
            'LPTEST', 'EMU.DCDCTEST.LPTEST', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_LPTESTCMPSENSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_LPTESTCMPSENSE, self).__init__(register,
            'LPTESTCMPSENSE', 'EMU.DCDCTEST.LPTESTCMPSENSE', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_CLIMTESTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_CLIMTESTEN, self).__init__(register,
            'CLIMTESTEN', 'EMU.DCDCTEST.CLIMTESTEN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_LPPUMPHI(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_LPPUMPHI, self).__init__(register,
            'LPPUMPHI', 'EMU.DCDCTEST.LPPUMPHI', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_RCOCALEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_RCOCALEN, self).__init__(register,
            'RCOCALEN', 'EMU.DCDCTEST.RCOCALEN', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCTEST_TESTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCTEST_TESTEN, self).__init__(register,
            'TESTEN', 'EMU.DCDCTEST.TESTEN', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONCTRL_REFRESHRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONCTRL_REFRESHRATE, self).__init__(register,
            'REFRESHRATE', 'EMU.VMONCTRL.REFRESHRATE', 'read-write',
            "",
            0, 2,
            RM_Enum_EMU_VMONCTRL_REFRESHRATE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONAVDDCTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONAVDDCTRL_EN, self).__init__(register,
            'EN', 'EMU.VMONAVDDCTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONAVDDCTRL_EM4ENTRY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONAVDDCTRL_EM4ENTRY, self).__init__(register,
            'EM4ENTRY', 'EMU.VMONAVDDCTRL.EM4ENTRY', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONAVDDCTRL_RISEWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONAVDDCTRL_RISEWU, self).__init__(register,
            'RISEWU', 'EMU.VMONAVDDCTRL.RISEWU', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONAVDDCTRL_FALLWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONAVDDCTRL_FALLWU, self).__init__(register,
            'FALLWU', 'EMU.VMONAVDDCTRL.FALLWU', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONAVDDCTRL_FALLTHRESFINE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONAVDDCTRL_FALLTHRESFINE, self).__init__(register,
            'FALLTHRESFINE', 'EMU.VMONAVDDCTRL.FALLTHRESFINE', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONAVDDCTRL_FALLTHRESCOARSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONAVDDCTRL_FALLTHRESCOARSE, self).__init__(register,
            'FALLTHRESCOARSE', 'EMU.VMONAVDDCTRL.FALLTHRESCOARSE', 'read-write',
            "",
            12, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONAVDDCTRL_RISETHRESFINE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONAVDDCTRL_RISETHRESFINE, self).__init__(register,
            'RISETHRESFINE', 'EMU.VMONAVDDCTRL.RISETHRESFINE', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONAVDDCTRL_RISETHRESCOARSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONAVDDCTRL_RISETHRESCOARSE, self).__init__(register,
            'RISETHRESCOARSE', 'EMU.VMONAVDDCTRL.RISETHRESCOARSE', 'read-write',
            "",
            20, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONALTAVDDCTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONALTAVDDCTRL_EN, self).__init__(register,
            'EN', 'EMU.VMONALTAVDDCTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONALTAVDDCTRL_RISEWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONALTAVDDCTRL_RISEWU, self).__init__(register,
            'RISEWU', 'EMU.VMONALTAVDDCTRL.RISEWU', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONALTAVDDCTRL_FALLWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONALTAVDDCTRL_FALLWU, self).__init__(register,
            'FALLWU', 'EMU.VMONALTAVDDCTRL.FALLWU', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONALTAVDDCTRL_THRESFINE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONALTAVDDCTRL_THRESFINE, self).__init__(register,
            'THRESFINE', 'EMU.VMONALTAVDDCTRL.THRESFINE', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONALTAVDDCTRL_THRESCOARSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONALTAVDDCTRL_THRESCOARSE, self).__init__(register,
            'THRESCOARSE', 'EMU.VMONALTAVDDCTRL.THRESCOARSE', 'read-write',
            "",
            12, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONDVDDCTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONDVDDCTRL_EN, self).__init__(register,
            'EN', 'EMU.VMONDVDDCTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONDVDDCTRL_RISEWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONDVDDCTRL_RISEWU, self).__init__(register,
            'RISEWU', 'EMU.VMONDVDDCTRL.RISEWU', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONDVDDCTRL_FALLWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONDVDDCTRL_FALLWU, self).__init__(register,
            'FALLWU', 'EMU.VMONDVDDCTRL.FALLWU', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONDVDDCTRL_THRESFINE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONDVDDCTRL_THRESFINE, self).__init__(register,
            'THRESFINE', 'EMU.VMONDVDDCTRL.THRESFINE', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONDVDDCTRL_THRESCOARSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONDVDDCTRL_THRESCOARSE, self).__init__(register,
            'THRESCOARSE', 'EMU.VMONDVDDCTRL.THRESCOARSE', 'read-write',
            "",
            12, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONIO0CTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONIO0CTRL_EN, self).__init__(register,
            'EN', 'EMU.VMONIO0CTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONIO0CTRL_RISEWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONIO0CTRL_RISEWU, self).__init__(register,
            'RISEWU', 'EMU.VMONIO0CTRL.RISEWU', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONIO0CTRL_FALLWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONIO0CTRL_FALLWU, self).__init__(register,
            'FALLWU', 'EMU.VMONIO0CTRL.FALLWU', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONIO0CTRL_RETDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONIO0CTRL_RETDIS, self).__init__(register,
            'RETDIS', 'EMU.VMONIO0CTRL.RETDIS', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONIO0CTRL_THRESFINE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONIO0CTRL_THRESFINE, self).__init__(register,
            'THRESFINE', 'EMU.VMONIO0CTRL.THRESFINE', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONIO0CTRL_THRESCOARSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONIO0CTRL_THRESCOARSE, self).__init__(register,
            'THRESCOARSE', 'EMU.VMONIO0CTRL.THRESCOARSE', 'read-write',
            "",
            12, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONFVDDCTRL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONFVDDCTRL_EN, self).__init__(register,
            'EN', 'EMU.VMONFVDDCTRL.EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONFVDDCTRL_RISEWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONFVDDCTRL_RISEWU, self).__init__(register,
            'RISEWU', 'EMU.VMONFVDDCTRL.RISEWU', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONFVDDCTRL_FALLWU(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONFVDDCTRL_FALLWU, self).__init__(register,
            'FALLWU', 'EMU.VMONFVDDCTRL.FALLWU', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONFVDDCTRL_THRESFINE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONFVDDCTRL_THRESFINE, self).__init__(register,
            'THRESFINE', 'EMU.VMONFVDDCTRL.THRESFINE', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONFVDDCTRL_THRESCOARSE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONFVDDCTRL_THRESCOARSE, self).__init__(register,
            'THRESCOARSE', 'EMU.VMONFVDDCTRL.THRESCOARSE', 'read-write',
            "",
            12, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_SGLNAMIXCTRL_SGLNAMIXSTANDBY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_SGLNAMIXCTRL_SGLNAMIXSTANDBY, self).__init__(register,
            'SGLNAMIXSTANDBY', 'EMU.SGLNAMIXCTRL.SGLNAMIXSTANDBY', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RAM1CTRL_RAMPOWERDOWN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RAM1CTRL_RAMPOWERDOWN, self).__init__(register,
            'RAMPOWERDOWN', 'EMU.RAM1CTRL.RAMPOWERDOWN', 'read-write',
            "",
            0, 2,
            RM_Enum_EMU_RAM1CTRL_RAMPOWERDOWN(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RAM2CTRL_RAMPOWERDOWN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RAM2CTRL_RAMPOWERDOWN, self).__init__(register,
            'RAMPOWERDOWN', 'EMU.RAM2CTRL.RAMPOWERDOWN', 'read-write',
            "",
            0, 1,
            RM_Enum_EMU_RAM2CTRL_RAMPOWERDOWN(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATEDLY2_EM23BODDREGWAIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATEDLY2_EM23BODDREGWAIT, self).__init__(register,
            'EM23BODDREGWAIT', 'EMU.STATEDLY2.EM23BODDREGWAIT', 'read-write',
            "",
            0, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATEDLY2_EM234BODWAIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATEDLY2_EM234BODWAIT, self).__init__(register,
            'EM234BODWAIT', 'EMU.STATEDLY2.EM234BODWAIT', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATEDLY2_EM4HWUFLASHVREFWAIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATEDLY2_EM4HWUFLASHVREFWAIT, self).__init__(register,
            'EM4HWUFLASHVREFWAIT', 'EMU.STATEDLY2.EM4HWUFLASHVREFWAIT', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATEDLY2_EM4HLDREGREFWAIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATEDLY2_EM4HLDREGREFWAIT, self).__init__(register,
            'EM4HLDREGREFWAIT', 'EMU.STATEDLY2.EM4HLDREGREFWAIT', 'read-write',
            "",
            24, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLPEM01CFG_LPCMPBIASEM01(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLPEM01CFG_LPCMPBIASEM01, self).__init__(register,
            'LPCMPBIASEM01', 'EMU.DCDCLPEM01CFG.LPCMPBIASEM01', 'read-write',
            "",
            8, 2,
            RM_Enum_EMU_DCDCLPEM01CFG_LPCMPBIASEM01(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCLPEM01CFG_LPCMPHYSSELEM01(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCLPEM01CFG_LPCMPHYSSELEM01, self).__init__(register,
            'LPCMPHYSSELEM01', 'EMU.DCDCLPEM01CFG.LPCMPHYSSELEM01', 'read-write',
            "",
            12, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCPRSSEL_DCDCPRSSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCPRSSEL_DCDCPRSSEL, self).__init__(register,
            'DCDCPRSSEL', 'EMU.DCDCPRSSEL.DCDCPRSSEL', 'read-write',
            "",
            0, 4,
            RM_Enum_EMU_DCDCPRSSEL_DCDCPRSSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DCDCPRSSEL_PRSNOISEDISEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DCDCPRSSEL_PRSNOISEDISEN, self).__init__(register,
            'PRSNOISEDISEN', 'EMU.DCDCPRSSEL.PRSNOISEDISEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_ACMP0UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_ACMP0UNLOCK, self).__init__(register,
            'ACMP0UNLOCK', 'EMU.EM23PERNORETAINCMD.ACMP0UNLOCK', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_ACMP1UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_ACMP1UNLOCK, self).__init__(register,
            'ACMP1UNLOCK', 'EMU.EM23PERNORETAINCMD.ACMP1UNLOCK', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_PCNT0UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_PCNT0UNLOCK, self).__init__(register,
            'PCNT0UNLOCK', 'EMU.EM23PERNORETAINCMD.PCNT0UNLOCK', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_PCNT1UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_PCNT1UNLOCK, self).__init__(register,
            'PCNT1UNLOCK', 'EMU.EM23PERNORETAINCMD.PCNT1UNLOCK', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_PCNT2UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_PCNT2UNLOCK, self).__init__(register,
            'PCNT2UNLOCK', 'EMU.EM23PERNORETAINCMD.PCNT2UNLOCK', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_I2C0UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_I2C0UNLOCK, self).__init__(register,
            'I2C0UNLOCK', 'EMU.EM23PERNORETAINCMD.I2C0UNLOCK', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_I2C1UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_I2C1UNLOCK, self).__init__(register,
            'I2C1UNLOCK', 'EMU.EM23PERNORETAINCMD.I2C1UNLOCK', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_DAC0UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_DAC0UNLOCK, self).__init__(register,
            'DAC0UNLOCK', 'EMU.EM23PERNORETAINCMD.DAC0UNLOCK', 'write-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_IDAC0UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_IDAC0UNLOCK, self).__init__(register,
            'IDAC0UNLOCK', 'EMU.EM23PERNORETAINCMD.IDAC0UNLOCK', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_ADC0UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_ADC0UNLOCK, self).__init__(register,
            'ADC0UNLOCK', 'EMU.EM23PERNORETAINCMD.ADC0UNLOCK', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_LETIMER0UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_LETIMER0UNLOCK, self).__init__(register,
            'LETIMER0UNLOCK', 'EMU.EM23PERNORETAINCMD.LETIMER0UNLOCK', 'write-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_WDOG0UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_WDOG0UNLOCK, self).__init__(register,
            'WDOG0UNLOCK', 'EMU.EM23PERNORETAINCMD.WDOG0UNLOCK', 'write-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_WDOG1UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_WDOG1UNLOCK, self).__init__(register,
            'WDOG1UNLOCK', 'EMU.EM23PERNORETAINCMD.WDOG1UNLOCK', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_LESENSE0UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_LESENSE0UNLOCK, self).__init__(register,
            'LESENSE0UNLOCK', 'EMU.EM23PERNORETAINCMD.LESENSE0UNLOCK', 'write-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_CSENUNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_CSENUNLOCK, self).__init__(register,
            'CSENUNLOCK', 'EMU.EM23PERNORETAINCMD.CSENUNLOCK', 'write-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCMD_LEUART0UNLOCK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCMD_LEUART0UNLOCK, self).__init__(register,
            'LEUART0UNLOCK', 'EMU.EM23PERNORETAINCMD.LEUART0UNLOCK', 'write-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_ACMP0LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_ACMP0LOCKED, self).__init__(register,
            'ACMP0LOCKED', 'EMU.EM23PERNORETAINSTATUS.ACMP0LOCKED', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_ACMP1LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_ACMP1LOCKED, self).__init__(register,
            'ACMP1LOCKED', 'EMU.EM23PERNORETAINSTATUS.ACMP1LOCKED', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_PCNT0LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_PCNT0LOCKED, self).__init__(register,
            'PCNT0LOCKED', 'EMU.EM23PERNORETAINSTATUS.PCNT0LOCKED', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_PCNT1LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_PCNT1LOCKED, self).__init__(register,
            'PCNT1LOCKED', 'EMU.EM23PERNORETAINSTATUS.PCNT1LOCKED', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_PCNT2LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_PCNT2LOCKED, self).__init__(register,
            'PCNT2LOCKED', 'EMU.EM23PERNORETAINSTATUS.PCNT2LOCKED', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_I2C0LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_I2C0LOCKED, self).__init__(register,
            'I2C0LOCKED', 'EMU.EM23PERNORETAINSTATUS.I2C0LOCKED', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_I2C1LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_I2C1LOCKED, self).__init__(register,
            'I2C1LOCKED', 'EMU.EM23PERNORETAINSTATUS.I2C1LOCKED', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_DAC0LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_DAC0LOCKED, self).__init__(register,
            'DAC0LOCKED', 'EMU.EM23PERNORETAINSTATUS.DAC0LOCKED', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_IDAC0LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_IDAC0LOCKED, self).__init__(register,
            'IDAC0LOCKED', 'EMU.EM23PERNORETAINSTATUS.IDAC0LOCKED', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_ADC0LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_ADC0LOCKED, self).__init__(register,
            'ADC0LOCKED', 'EMU.EM23PERNORETAINSTATUS.ADC0LOCKED', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_LETIMER0LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_LETIMER0LOCKED, self).__init__(register,
            'LETIMER0LOCKED', 'EMU.EM23PERNORETAINSTATUS.LETIMER0LOCKED', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_WDOG0LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_WDOG0LOCKED, self).__init__(register,
            'WDOG0LOCKED', 'EMU.EM23PERNORETAINSTATUS.WDOG0LOCKED', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_WDOG1LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_WDOG1LOCKED, self).__init__(register,
            'WDOG1LOCKED', 'EMU.EM23PERNORETAINSTATUS.WDOG1LOCKED', 'read-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_LESENSE0LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_LESENSE0LOCKED, self).__init__(register,
            'LESENSE0LOCKED', 'EMU.EM23PERNORETAINSTATUS.LESENSE0LOCKED', 'read-only',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_CSENLOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_CSENLOCKED, self).__init__(register,
            'CSENLOCKED', 'EMU.EM23PERNORETAINSTATUS.CSENLOCKED', 'read-only',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINSTATUS_LEUART0LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINSTATUS_LEUART0LOCKED, self).__init__(register,
            'LEUART0LOCKED', 'EMU.EM23PERNORETAINSTATUS.LEUART0LOCKED', 'read-only',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_ACMP0DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_ACMP0DIS, self).__init__(register,
            'ACMP0DIS', 'EMU.EM23PERNORETAINCTRL.ACMP0DIS', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_ACMP1DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_ACMP1DIS, self).__init__(register,
            'ACMP1DIS', 'EMU.EM23PERNORETAINCTRL.ACMP1DIS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_PCNT0DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_PCNT0DIS, self).__init__(register,
            'PCNT0DIS', 'EMU.EM23PERNORETAINCTRL.PCNT0DIS', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_PCNT1DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_PCNT1DIS, self).__init__(register,
            'PCNT1DIS', 'EMU.EM23PERNORETAINCTRL.PCNT1DIS', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_PCNT2DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_PCNT2DIS, self).__init__(register,
            'PCNT2DIS', 'EMU.EM23PERNORETAINCTRL.PCNT2DIS', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_I2C0DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_I2C0DIS, self).__init__(register,
            'I2C0DIS', 'EMU.EM23PERNORETAINCTRL.I2C0DIS', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_I2C1DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_I2C1DIS, self).__init__(register,
            'I2C1DIS', 'EMU.EM23PERNORETAINCTRL.I2C1DIS', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_DAC0DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_DAC0DIS, self).__init__(register,
            'DAC0DIS', 'EMU.EM23PERNORETAINCTRL.DAC0DIS', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_IDAC0DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_IDAC0DIS, self).__init__(register,
            'IDAC0DIS', 'EMU.EM23PERNORETAINCTRL.IDAC0DIS', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_ADC0DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_ADC0DIS, self).__init__(register,
            'ADC0DIS', 'EMU.EM23PERNORETAINCTRL.ADC0DIS', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_LETIMER0DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_LETIMER0DIS, self).__init__(register,
            'LETIMER0DIS', 'EMU.EM23PERNORETAINCTRL.LETIMER0DIS', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_WDOG0DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_WDOG0DIS, self).__init__(register,
            'WDOG0DIS', 'EMU.EM23PERNORETAINCTRL.WDOG0DIS', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_WDOG1DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_WDOG1DIS, self).__init__(register,
            'WDOG1DIS', 'EMU.EM23PERNORETAINCTRL.WDOG1DIS', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_LESENSE0DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_LESENSE0DIS, self).__init__(register,
            'LESENSE0DIS', 'EMU.EM23PERNORETAINCTRL.LESENSE0DIS', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_CSENDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_CSENDIS, self).__init__(register,
            'CSENDIS', 'EMU.EM23PERNORETAINCTRL.CSENDIS', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM23PERNORETAINCTRL_LEUART0DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM23PERNORETAINCTRL_LEUART0DIS, self).__init__(register,
            'LEUART0DIS', 'EMU.EM23PERNORETAINCTRL.LEUART0DIS', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_AUXCTRL0_AUX0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_AUXCTRL0_AUX0, self).__init__(register,
            'AUX0', 'EMU.AUXCTRL0.AUX0', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_AUXCTRL1_AUX1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_AUXCTRL1_AUX1, self).__init__(register,
            'AUX1', 'EMU.AUXCTRL1.AUX1', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_AUXCTRL2_AUX2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_AUXCTRL2_AUX2, self).__init__(register,
            'AUX2', 'EMU.AUXCTRL2.AUX2', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_AUXCTRL2_AUX3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_AUXCTRL2_AUX3, self).__init__(register,
            'AUX3', 'EMU.AUXCTRL2.AUX3', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBOD_PORBOD_REFTRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBOD_PORBOD_REFTRIM, self).__init__(register,
            'PORBOD_REFTRIM', 'EMU.PORBOD.PORBOD_REFTRIM', 'read-write',
            "",
            0, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBOD_PORBOD_FORCE_MIRROR_FOR_VREF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBOD_PORBOD_FORCE_MIRROR_FOR_VREF, self).__init__(register,
            'PORBOD_FORCE_MIRROR_FOR_VREF', 'EMU.PORBOD.PORBOD_FORCE_MIRROR_FOR_VREF', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBOD_PORBOD_AVDD_BOD_THR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBOD_PORBOD_AVDD_BOD_THR, self).__init__(register,
            'PORBOD_AVDD_BOD_THR', 'EMU.PORBOD.PORBOD_AVDD_BOD_THR', 'read-write',
            "",
            6, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBOD_PORBOD_DVDD_BOD_THR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBOD_PORBOD_DVDD_BOD_THR, self).__init__(register,
            'PORBOD_DVDD_BOD_THR', 'EMU.PORBOD.PORBOD_DVDD_BOD_THR', 'read-write',
            "",
            11, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBOD_BIAS_TEMP_TRIM_LP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBOD_BIAS_TEMP_TRIM_LP, self).__init__(register,
            'BIAS_TEMP_TRIM_LP', 'EMU.PORBOD.BIAS_TEMP_TRIM_LP', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBOD_BIAS_ABS_TRIM_LP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBOD_BIAS_ABS_TRIM_LP, self).__init__(register,
            'BIAS_ABS_TRIM_LP', 'EMU.PORBOD.BIAS_ABS_TRIM_LP', 'read-write',
            "",
            20, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBOD_BIAS_ILTC_UA_TRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBOD_BIAS_ILTC_UA_TRIM, self).__init__(register,
            'BIAS_ILTC_UA_TRIM', 'EMU.PORBOD.BIAS_ILTC_UA_TRIM', 'read-write',
            "",
            25, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBOD_BIAS_ILTC_NA_TRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBOD_BIAS_ILTC_NA_TRIM, self).__init__(register,
            'BIAS_ILTC_NA_TRIM', 'EMU.PORBOD.BIAS_ILTC_NA_TRIM', 'read-write',
            "",
            28, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBOD_GMC_CALIB_DISABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBOD_GMC_CALIB_DISABLE, self).__init__(register,
            'GMC_CALIB_DISABLE', 'EMU.PORBOD.GMC_CALIB_DISABLE', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBODREFRESH_PORBOD_DUTY_CYCLE_OFF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBODREFRESH_PORBOD_DUTY_CYCLE_OFF, self).__init__(register,
            'PORBOD_DUTY_CYCLE_OFF', 'EMU.PORBODREFRESH.PORBOD_DUTY_CYCLE_OFF', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBODREFRESH_PORBOD_FORCE_REFRESH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBODREFRESH_PORBOD_FORCE_REFRESH, self).__init__(register,
            'PORBOD_FORCE_REFRESH', 'EMU.PORBODREFRESH.PORBOD_FORCE_REFRESH', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBODREFRESH_PORBOD_REFRESHRATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBODREFRESH_PORBOD_REFRESHRATE, self).__init__(register,
            'PORBOD_REFRESHRATE', 'EMU.PORBODREFRESH.PORBOD_REFRESHRATE', 'read-write',
            "",
            2, 2,
            RM_Enum_EMU_PORBODREFRESH_PORBOD_REFRESHRATE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBODOVERRIDE_PORBOD_OVERRIDE_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBODOVERRIDE_PORBOD_OVERRIDE_EN, self).__init__(register,
            'PORBOD_OVERRIDE_EN', 'EMU.PORBODOVERRIDE.PORBOD_OVERRIDE_EN', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_BOD_BOOST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_BOD_BOOST, self).__init__(register,
            'OVR_PORBOD_BOD_BOOST', 'EMU.PORBODOVERRIDE.OVR_PORBOD_BOD_BOOST', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_LEGACY_POR_SAFE_DISABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_LEGACY_POR_SAFE_DISABLE, self).__init__(register,
            'OVR_PORBOD_LEGACY_POR_SAFE_DISABLE', 'EMU.PORBODOVERRIDE.OVR_PORBOD_LEGACY_POR_SAFE_DISABLE', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_AVDD_BOD_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_AVDD_BOD_EN, self).__init__(register,
            'OVR_PORBOD_AVDD_BOD_EN', 'EMU.PORBODOVERRIDE.OVR_PORBOD_AVDD_BOD_EN', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_AVDD_EM4BOD_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_AVDD_EM4BOD_EN, self).__init__(register,
            'OVR_PORBOD_AVDD_EM4BOD_EN', 'EMU.PORBODOVERRIDE.OVR_PORBOD_AVDD_EM4BOD_EN', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_DVDD_BOD_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_DVDD_BOD_EN, self).__init__(register,
            'OVR_PORBOD_DVDD_BOD_EN', 'EMU.PORBODOVERRIDE.OVR_PORBOD_DVDD_BOD_EN', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_FLASH_BOD_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_FLASH_BOD_EN, self).__init__(register,
            'OVR_PORBOD_FLASH_BOD_EN', 'EMU.PORBODOVERRIDE.OVR_PORBOD_FLASH_BOD_EN', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_DEC0_BOD_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_DEC0_BOD_EN, self).__init__(register,
            'OVR_PORBOD_DEC0_BOD_EN', 'EMU.PORBODOVERRIDE.OVR_PORBOD_DEC0_BOD_EN', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_DEC1_BOD_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_DEC1_BOD_EN, self).__init__(register,
            'OVR_PORBOD_DEC1_BOD_EN', 'EMU.PORBODOVERRIDE.OVR_PORBOD_DEC1_BOD_EN', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_BOD_BIAS_ENABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_BOD_BIAS_ENABLE, self).__init__(register,
            'OVR_PORBOD_BOD_BIAS_ENABLE', 'EMU.PORBODOVERRIDE.OVR_PORBOD_BOD_BIAS_ENABLE', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BODCONF_PORBOD_AVDD_EM4BOD_TRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BODCONF_PORBOD_AVDD_EM4BOD_TRIM, self).__init__(register,
            'PORBOD_AVDD_EM4BOD_TRIM', 'EMU.BODCONF.PORBOD_AVDD_EM4BOD_TRIM', 'read-write',
            "",
            2, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BODCONF_PORBOD_AVDD_GL_CURR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BODCONF_PORBOD_AVDD_GL_CURR, self).__init__(register,
            'PORBOD_AVDD_GL_CURR', 'EMU.BODCONF.PORBOD_AVDD_GL_CURR', 'read-write',
            "",
            7, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BODCONF_PORBOD_AVDD_GL_RC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BODCONF_PORBOD_AVDD_GL_RC, self).__init__(register,
            'PORBOD_AVDD_GL_RC', 'EMU.BODCONF.PORBOD_AVDD_GL_RC', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BODCONF_PORBOD_DVDD_GL_CURR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BODCONF_PORBOD_DVDD_GL_CURR, self).__init__(register,
            'PORBOD_DVDD_GL_CURR', 'EMU.BODCONF.PORBOD_DVDD_GL_CURR', 'read-write',
            "",
            17, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BODCONF_PORBOD_DVDD_GL_RC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BODCONF_PORBOD_DVDD_GL_RC, self).__init__(register,
            'PORBOD_DVDD_GL_RC', 'EMU.BODCONF.PORBOD_DVDD_GL_RC', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BODCONF_EMUOSCDIV2EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BODCONF_EMUOSCDIV2EN, self).__init__(register,
            'EMUOSCDIV2EN', 'EMU.BODCONF.EMUOSCDIV2EN', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BODCONF_EMUOSC_TRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BODCONF_EMUOSC_TRIM, self).__init__(register,
            'EMUOSC_TRIM', 'EMU.BODCONF.EMUOSC_TRIM', 'read-write',
            "",
            24, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BODCONF_EMUOSC_RTRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BODCONF_EMUOSC_RTRIM, self).__init__(register,
            'EMUOSC_RTRIM', 'EMU.BODCONF.EMUOSC_RTRIM', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BODCONF_PORBOD_AVDD_EM4BOD_DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BODCONF_PORBOD_AVDD_EM4BOD_DIS, self).__init__(register,
            'PORBOD_AVDD_EM4BOD_DIS', 'EMU.BODCONF.PORBOD_AVDD_EM4BOD_DIS', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BODCONF_EM23BODBOOST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BODCONF_EM23BODBOOST, self).__init__(register,
            'EM23BODBOOST', 'EMU.BODCONF.EM23BODBOOST', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BODCONF_BODBOOSTDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BODCONF_BODBOOSTDIS, self).__init__(register,
            'BODBOOSTDIS', 'EMU.BODCONF.BODBOOSTDIS', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_FLASHBOD_PORBOD_FLASH_BOD_THR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_FLASHBOD_PORBOD_FLASH_BOD_THR, self).__init__(register,
            'PORBOD_FLASH_BOD_THR', 'EMU.FLASHBOD.PORBOD_FLASH_BOD_THR', 'read-write',
            "",
            6, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_FLASHBOD_PORBOD_FLASH_GL_CURR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_FLASHBOD_PORBOD_FLASH_GL_CURR, self).__init__(register,
            'PORBOD_FLASH_GL_CURR', 'EMU.FLASHBOD.PORBOD_FLASH_GL_CURR', 'read-write',
            "",
            16, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_FLASHBOD_PORBOD_FLASH_GL_RC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_FLASHBOD_PORBOD_FLASH_GL_RC, self).__init__(register,
            'PORBOD_FLASH_GL_RC', 'EMU.FLASHBOD.PORBOD_FLASH_GL_RC', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DECBOD_PORBOD_DEC0_BOD_TRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DECBOD_PORBOD_DEC0_BOD_TRIM, self).__init__(register,
            'PORBOD_DEC0_BOD_TRIM', 'EMU.DECBOD.PORBOD_DEC0_BOD_TRIM', 'read-write',
            "",
            0, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DECBOD_PORBOD_DEC0_BOD_THR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DECBOD_PORBOD_DEC0_BOD_THR, self).__init__(register,
            'PORBOD_DEC0_BOD_THR', 'EMU.DECBOD.PORBOD_DEC0_BOD_THR', 'read-write',
            "",
            2, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DECBOD_PORBOD_DEC0_GL_CURR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DECBOD_PORBOD_DEC0_GL_CURR, self).__init__(register,
            'PORBOD_DEC0_GL_CURR', 'EMU.DECBOD.PORBOD_DEC0_GL_CURR', 'read-write',
            "",
            7, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DECBOD_PORBOD_DEC0_GL_RC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DECBOD_PORBOD_DEC0_GL_RC, self).__init__(register,
            'PORBOD_DEC0_GL_RC', 'EMU.DECBOD.PORBOD_DEC0_GL_RC', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DECBOD_PORBOD_DEC1_BOD_TRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DECBOD_PORBOD_DEC1_BOD_TRIM, self).__init__(register,
            'PORBOD_DEC1_BOD_TRIM', 'EMU.DECBOD.PORBOD_DEC1_BOD_TRIM', 'read-write',
            "",
            16, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DECBOD_PORBOD_DEC1_BOD_THR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DECBOD_PORBOD_DEC1_BOD_THR, self).__init__(register,
            'PORBOD_DEC1_BOD_THR', 'EMU.DECBOD.PORBOD_DEC1_BOD_THR', 'read-write',
            "",
            18, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DECBOD_PORBOD_DEC1_GL_CURR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DECBOD_PORBOD_DEC1_GL_CURR, self).__init__(register,
            'PORBOD_DEC1_GL_CURR', 'EMU.DECBOD.PORBOD_DEC1_GL_CURR', 'read-write',
            "",
            23, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DECBOD_PORBOD_DEC1_GL_RC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DECBOD_PORBOD_DEC1_GL_RC, self).__init__(register,
            'PORBOD_DEC1_GL_RC', 'EMU.DECBOD.PORBOD_DEC1_GL_RC', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASCONF_GMCEM01(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASCONF_GMCEM01, self).__init__(register,
            'GMCEM01', 'EMU.BIASCONF.GMCEM01', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASCONF_UADUTYEM01(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASCONF_UADUTYEM01, self).__init__(register,
            'UADUTYEM01', 'EMU.BIASCONF.UADUTYEM01', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASCONF_NADUTYEM01(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASCONF_NADUTYEM01, self).__init__(register,
            'NADUTYEM01', 'EMU.BIASCONF.NADUTYEM01', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASCONF_LPEM01(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASCONF_LPEM01, self).__init__(register,
            'LPEM01', 'EMU.BIASCONF.LPEM01', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASCONF_GMCEM23(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASCONF_GMCEM23, self).__init__(register,
            'GMCEM23', 'EMU.BIASCONF.GMCEM23', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASCONF_UADUTYEM23(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASCONF_UADUTYEM23, self).__init__(register,
            'UADUTYEM23', 'EMU.BIASCONF.UADUTYEM23', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASCONF_NADUTYEM23(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASCONF_NADUTYEM23, self).__init__(register,
            'NADUTYEM23', 'EMU.BIASCONF.NADUTYEM23', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASCONF_LPEM23(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASCONF_LPEM23, self).__init__(register,
            'LPEM23', 'EMU.BIASCONF.LPEM23', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASCONF_EN_GMC_W_BGR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASCONF_EN_GMC_W_BGR, self).__init__(register,
            'EN_GMC_W_BGR', 'EMU.BIASCONF.EN_GMC_W_BGR', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASCONF_LSBIAS_SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASCONF_LSBIAS_SEL, self).__init__(register,
            'LSBIAS_SEL', 'EMU.BIASCONF.LSBIAS_SEL', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASCONF_ILTC_NODUTY_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASCONF_ILTC_NODUTY_EN, self).__init__(register,
            'ILTC_NODUTY_EN', 'EMU.BIASCONF.ILTC_NODUTY_EN', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASCONF_DISRPUPDATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASCONF_DISRPUPDATE, self).__init__(register,
            'DISRPUPDATE', 'EMU.BIASCONF.DISRPUPDATE', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASCONF_BIASCONTTM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASCONF_BIASCONTTM, self).__init__(register,
            'BIASCONTTM', 'EMU.BIASCONF.BIASCONTTM', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASCONF_GMC_CALIB_USESAR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASCONF_GMC_CALIB_USESAR, self).__init__(register,
            'GMC_CALIB_USESAR', 'EMU.BIASCONF.GMC_CALIB_USESAR', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASABSTRIM_BIAS_ABS_TRIM_HP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASABSTRIM_BIAS_ABS_TRIM_HP, self).__init__(register,
            'BIAS_ABS_TRIM_HP', 'EMU.BIASABSTRIM.BIAS_ABS_TRIM_HP', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASABSTRIM_BIAS_ABS_TRIM_HPCAL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASABSTRIM_BIAS_ABS_TRIM_HPCAL, self).__init__(register,
            'BIAS_ABS_TRIM_HPCAL', 'EMU.BIASABSTRIM.BIAS_ABS_TRIM_HPCAL', 'read-write',
            "",
            16, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASABSTRIM_BIAS_ABS_TRIM_LPCAL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASABSTRIM_BIAS_ABS_TRIM_LPCAL, self).__init__(register,
            'BIAS_ABS_TRIM_LPCAL', 'EMU.BIASABSTRIM.BIAS_ABS_TRIM_LPCAL', 'read-write',
            "",
            24, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTEMPTRIM_BIAS_TEMP_TRIM_HP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTEMPTRIM_BIAS_TEMP_TRIM_HP, self).__init__(register,
            'BIAS_TEMP_TRIM_HP', 'EMU.BIASTEMPTRIM.BIAS_TEMP_TRIM_HP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTEMPTRIM_BIAS_TEMP_TRIM_HPCAL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTEMPTRIM_BIAS_TEMP_TRIM_HPCAL, self).__init__(register,
            'BIAS_TEMP_TRIM_HPCAL', 'EMU.BIASTEMPTRIM.BIAS_TEMP_TRIM_HPCAL', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTEMPTRIM_BIAS_TEMP_TRIM_LPCAL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTEMPTRIM_BIAS_TEMP_TRIM_LPCAL, self).__init__(register,
            'BIAS_TEMP_TRIM_LPCAL', 'EMU.BIASTEMPTRIM.BIAS_TEMP_TRIM_LPCAL', 'read-write',
            "",
            12, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTRIM_BIAS_VREF_TRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTRIM_BIAS_VREF_TRIM, self).__init__(register,
            'BIAS_VREF_TRIM', 'EMU.BIASTRIM.BIAS_VREF_TRIM', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTRIM_BIAS_LDO_NABIAS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTRIM_BIAS_LDO_NABIAS, self).__init__(register,
            'BIAS_LDO_NABIAS', 'EMU.BIASTRIM.BIAS_LDO_NABIAS', 'read-write',
            "",
            4, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTRIM_BIAS_LDO_ILOAD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTRIM_BIAS_LDO_ILOAD, self).__init__(register,
            'BIAS_LDO_ILOAD', 'EMU.BIASTRIM.BIAS_LDO_ILOAD', 'read-write',
            "",
            6, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTRIM_BIAS_NA_MULT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTRIM_BIAS_NA_MULT, self).__init__(register,
            'BIAS_NA_MULT', 'EMU.BIASTRIM.BIAS_NA_MULT', 'read-write',
            "",
            8, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTRIM_BIAS_DLY_TRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTRIM_BIAS_DLY_TRIM, self).__init__(register,
            'BIAS_DLY_TRIM', 'EMU.BIASTRIM.BIAS_DLY_TRIM', 'read-write',
            "",
            20, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASPERIOD_BIAS_REFRESH_PERIOD_EM03(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASPERIOD_BIAS_REFRESH_PERIOD_EM03, self).__init__(register,
            'BIAS_REFRESH_PERIOD_EM03', 'EMU.BIASPERIOD.BIAS_REFRESH_PERIOD_EM03', 'read-write',
            "",
            12, 2,
            RM_Enum_EMU_BIASPERIOD_BIAS_REFRESH_PERIOD_EM03(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASPERIOD_BIAS_REFRESH_PERIOD_EM4H(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASPERIOD_BIAS_REFRESH_PERIOD_EM4H, self).__init__(register,
            'BIAS_REFRESH_PERIOD_EM4H', 'EMU.BIASPERIOD.BIAS_REFRESH_PERIOD_EM4H', 'read-write',
            "",
            16, 2,
            RM_Enum_EMU_BIASPERIOD_BIAS_REFRESH_PERIOD_EM4H(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASPERIOD_BIAS_GMC_CALIB_PERIOD_EM03(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASPERIOD_BIAS_GMC_CALIB_PERIOD_EM03, self).__init__(register,
            'BIAS_GMC_CALIB_PERIOD_EM03', 'EMU.BIASPERIOD.BIAS_GMC_CALIB_PERIOD_EM03', 'read-write',
            "",
            20, 3,
            RM_Enum_EMU_BIASPERIOD_BIAS_GMC_CALIB_PERIOD_EM03(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASPERIOD_BIAS_GMC_CALIB_PERIOD_EM4H(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASPERIOD_BIAS_GMC_CALIB_PERIOD_EM4H, self).__init__(register,
            'BIAS_GMC_CALIB_PERIOD_EM4H', 'EMU.BIASPERIOD.BIAS_GMC_CALIB_PERIOD_EM4H', 'read-write',
            "",
            24, 3,
            RM_Enum_EMU_BIASPERIOD_BIAS_GMC_CALIB_PERIOD_EM4H(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DREGCALIB_HDREG_TRIM_VREG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DREGCALIB_HDREG_TRIM_VREG, self).__init__(register,
            'HDREG_TRIM_VREG', 'EMU.DREGCALIB.HDREG_TRIM_VREG', 'read-write',
            "",
            0, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DREGCALIB_HDREG_TRIM_ISRC_CINT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DREGCALIB_HDREG_TRIM_ISRC_CINT, self).__init__(register,
            'HDREG_TRIM_ISRC_CINT', 'EMU.DREGCALIB.HDREG_TRIM_ISRC_CINT', 'read-write',
            "",
            10, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DREGCALIB_LDREG_TRIM_VREG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DREGCALIB_LDREG_TRIM_VREG, self).__init__(register,
            'LDREG_TRIM_VREG', 'EMU.DREGCALIB.LDREG_TRIM_VREG', 'read-write',
            "",
            16, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DREGCALIB_LDREG_DUTYSCALE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DREGCALIB_LDREG_DUTYSCALE, self).__init__(register,
            'LDREG_DUTYSCALE', 'EMU.DREGCALIB.LDREG_DUTYSCALE', 'read-write',
            "",
            21, 2,
            RM_Enum_EMU_DREGCALIB_LDREG_DUTYSCALE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DREGOVERRIDE_LDREG_OVERRIDE_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DREGOVERRIDE_LDREG_OVERRIDE_EN, self).__init__(register,
            'LDREG_OVERRIDE_EN', 'EMU.DREGOVERRIDE.LDREG_OVERRIDE_EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DREGOVERRIDE_OVR_LDREG_EN_PD0SW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DREGOVERRIDE_OVR_LDREG_EN_PD0SW, self).__init__(register,
            'OVR_LDREG_EN_PD0SW', 'EMU.DREGOVERRIDE.OVR_LDREG_EN_PD0SW', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DREGOVERRIDE_OVR_LDREG_EN_LDREG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DREGOVERRIDE_OVR_LDREG_EN_LDREG, self).__init__(register,
            'OVR_LDREG_EN_LDREG', 'EMU.DREGOVERRIDE.OVR_LDREG_EN_LDREG', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DREGOVERRIDE_OVR_LDREG_VREF_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DREGOVERRIDE_OVR_LDREG_VREF_EN, self).__init__(register,
            'OVR_LDREG_VREF_EN', 'EMU.DREGOVERRIDE.OVR_LDREG_VREF_EN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DREGOVERRIDE_HDREG_OVERRIDE_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DREGOVERRIDE_HDREG_OVERRIDE_EN, self).__init__(register,
            'HDREG_OVERRIDE_EN', 'EMU.DREGOVERRIDE.HDREG_OVERRIDE_EN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_HARD_SW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_HARD_SW, self).__init__(register,
            'OVR_HDREG_EN_HARD_SW', 'EMU.DREGOVERRIDE.OVR_HDREG_EN_HARD_SW', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_HDREG_BIAS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_HDREG_BIAS, self).__init__(register,
            'OVR_HDREG_EN_HDREG_BIAS', 'EMU.DREGOVERRIDE.OVR_HDREG_EN_HDREG_BIAS', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_COLD_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_COLD_START, self).__init__(register,
            'OVR_HDREG_EN_COLD_START', 'EMU.DREGOVERRIDE.OVR_HDREG_EN_COLD_START', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_HDREG_FUNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_HDREG_FUNC, self).__init__(register,
            'OVR_HDREG_EN_HDREG_FUNC', 'EMU.DREGOVERRIDE.OVR_HDREG_EN_HDREG_FUNC', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_VREG_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_VREG_MODE, self).__init__(register,
            'OVR_HDREG_EN_VREG_MODE', 'EMU.DREGOVERRIDE.OVR_HDREG_EN_VREG_MODE', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RAM0FEATURE_SEQRAMEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RAM0FEATURE_SEQRAMEN, self).__init__(register,
            'SEQRAMEN', 'EMU.RAM0FEATURE.SEQRAMEN', 'write-only',
            "",
            4, 2,
            RM_Enum_EMU_RAM0FEATURE_SEQRAMEN(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RAM0FEATURE_RAM0DIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RAM0FEATURE_RAM0DIV, self).__init__(register,
            'RAM0DIV', 'EMU.RAM0FEATURE.RAM0DIV', 'write-only',
            "",
            8, 2,
            RM_Enum_EMU_RAM0FEATURE_RAM0DIV(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RAM0FEATURE_RAMSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RAM0FEATURE_RAMSIZE, self).__init__(register,
            'RAMSIZE', 'EMU.RAM0FEATURE.RAMSIZE', 'write-only',
            "",
            16, 5,
            RM_Enum_EMU_RAM0FEATURE_RAMSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATEDLY0_EM23WAITHD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATEDLY0_EM23WAITHD, self).__init__(register,
            'EM23WAITHD', 'EMU.STATEDLY0.EM23WAITHD', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATEDLY0_EM23WAITHDFUNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATEDLY0_EM23WAITHDFUNC, self).__init__(register,
            'EM23WAITHDFUNC', 'EMU.STATEDLY0.EM23WAITHDFUNC', 'read-write',
            "",
            4, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATEDLY0_EM4WAITHD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATEDLY0_EM4WAITHD, self).__init__(register,
            'EM4WAITHD', 'EMU.STATEDLY0.EM4WAITHD', 'read-write',
            "",
            6, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATEDLY0_EM4WAITHDFUNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATEDLY0_EM4WAITHDFUNC, self).__init__(register,
            'EM4WAITHDFUNC', 'EMU.STATEDLY0.EM4WAITHDFUNC', 'read-write',
            "",
            12, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATEDLY0_ISORETDELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATEDLY0_ISORETDELAY, self).__init__(register,
            'ISORETDELAY', 'EMU.STATEDLY0.ISORETDELAY', 'read-write',
            "",
            14, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATEDLY0_RETDEASSERTDELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATEDLY0_RETDEASSERTDELAY, self).__init__(register,
            'RETDEASSERTDELAY', 'EMU.STATEDLY0.RETDEASSERTDELAY', 'read-write',
            "",
            16, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATEDLY1_EM4SPORDELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATEDLY1_EM4SPORDELAY, self).__init__(register,
            'EM4SPORDELAY', 'EMU.STATEDLY1.EM4SPORDELAY', 'read-write',
            "",
            0, 11)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATEDLY1_SETTLINGDELAY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATEDLY1_SETTLINGDELAY, self).__init__(register,
            'SETTLINGDELAY', 'EMU.STATEDLY1.SETTLINGDELAY', 'read-write',
            "",
            16, 11)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_STATEDLY1_EM4HDREGWAIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_STATEDLY1_EM4HDREGWAIT, self).__init__(register,
            'EM4HDREGWAIT', 'EMU.STATEDLY1.EM4HDREGWAIT', 'read-write',
            "",
            27, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONCONF_CALIBEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONCONF_CALIBEN, self).__init__(register,
            'CALIBEN', 'EMU.VMONCONF.CALIBEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONCONF_BUFBIAS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONCONF_BUFBIAS, self).__init__(register,
            'BUFBIAS', 'EMU.VMONCONF.BUFBIAS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONCONF_CURRBOOST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONCONF_CURRBOOST, self).__init__(register,
            'CURRBOOST', 'EMU.VMONCONF.CURRBOOST', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_VMONCONF_VREFCAL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_VMONCONF_VREFCAL, self).__init__(register,
            'VREFCAL', 'EMU.VMONCONF.VREFCAL', 'read-write',
            "",
            3, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTLOCK_LOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTLOCK_LOCKKEY, self).__init__(register,
            'LOCKKEY', 'EMU.TESTLOCK.LOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_EMU_TESTLOCK_LOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_SCANCTRL_SCANTEST_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_SCANCTRL_SCANTEST_EN, self).__init__(register,
            'SCANTEST_EN', 'EMU.SCANCTRL.SCANTEST_EN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_SCANCTRL_SCAN_PIN_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_SCANCTRL_SCAN_PIN_MODE, self).__init__(register,
            'SCAN_PIN_MODE', 'EMU.SCANCTRL.SCAN_PIN_MODE', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_SCANCTRL_SCAN_DRIVE_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_SCANCTRL_SCAN_DRIVE_MODE, self).__init__(register,
            'SCAN_DRIVE_MODE', 'EMU.SCANCTRL.SCAN_DRIVE_MODE', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_SCANCTRL_ISO_OVERRIDE_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_SCANCTRL_ISO_OVERRIDE_EN, self).__init__(register,
            'ISO_OVERRIDE_EN', 'EMU.SCANCTRL.ISO_OVERRIDE_EN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_EXPORT_RESET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_EXPORT_RESET, self).__init__(register,
            'EXPORT_RESET', 'EMU.TESTCTRL.EXPORT_RESET', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_HARD_PIN_RESET_OVERRIDE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_HARD_PIN_RESET_OVERRIDE, self).__init__(register,
            'HARD_PIN_RESET_OVERRIDE', 'EMU.TESTCTRL.HARD_PIN_RESET_OVERRIDE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_MASK_EXPORT_RESET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_MASK_EXPORT_RESET, self).__init__(register,
            'MASK_EXPORT_RESET', 'EMU.TESTCTRL.MASK_EXPORT_RESET', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_RAW_BOD_SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_RAW_BOD_SEL, self).__init__(register,
            'RAW_BOD_SEL', 'EMU.TESTCTRL.RAW_BOD_SEL', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_BOD_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_BOD_MASK, self).__init__(register,
            'BOD_MASK', 'EMU.TESTCTRL.BOD_MASK', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_CMCTRLPRSSEL0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_CMCTRLPRSSEL0, self).__init__(register,
            'CMCTRLPRSSEL0', 'EMU.TESTCTRL.CMCTRLPRSSEL0', 'read-write',
            "",
            8, 6,
            RM_Enum_EMU_TESTCTRL_CMCTRLPRSSEL0(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_CMCTRLPRSSEL1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_CMCTRLPRSSEL1, self).__init__(register,
            'CMCTRLPRSSEL1', 'EMU.TESTCTRL.CMCTRLPRSSEL1', 'read-write',
            "",
            16, 6,
            RM_Enum_EMU_TESTCTRL_CMCTRLPRSSEL1(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_DVDD_DSCHRG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_DVDD_DSCHRG, self).__init__(register,
            'DVDD_DSCHRG', 'EMU.TESTCTRL.DVDD_DSCHRG', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_PD1_DSCHRG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_PD1_DSCHRG, self).__init__(register,
            'PD1_DSCHRG', 'EMU.TESTCTRL.PD1_DSCHRG', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_BIAS_OVERRIDE_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_BIAS_OVERRIDE_EN, self).__init__(register,
            'BIAS_OVERRIDE_EN', 'EMU.TESTCTRL.BIAS_OVERRIDE_EN', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_POWERLOSSDISABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_POWERLOSSDISABLE, self).__init__(register,
            'POWERLOSSDISABLE', 'EMU.TESTCTRL.POWERLOSSDISABLE', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_FLASH_PWR_SW_OVR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_FLASH_PWR_SW_OVR, self).__init__(register,
            'FLASH_PWR_SW_OVR', 'EMU.TESTCTRL.FLASH_PWR_SW_OVR', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_EMUOSCEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_EMUOSCEN, self).__init__(register,
            'EMUOSCEN', 'EMU.TESTCTRL.EMUOSCEN', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_EM234FLASHPWRDOWNDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_EM234FLASHPWRDOWNDIS, self).__init__(register,
            'EM234FLASHPWRDOWNDIS', 'EMU.TESTCTRL.EM234FLASHPWRDOWNDIS', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRL_LDREGDISMASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRL_LDREGDISMASK, self).__init__(register,
            'LDREGDISMASK', 'EMU.TESTCTRL.LDREGDISMASK', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTESTCTRL_GMC_CALIB_START(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTESTCTRL_GMC_CALIB_START, self).__init__(register,
            'GMC_CALIB_START', 'EMU.BIASTESTCTRL.GMC_CALIB_START', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTESTCTRL_FORCE_GMC_CAL_REQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTESTCTRL_FORCE_GMC_CAL_REQ, self).__init__(register,
            'FORCE_GMC_CAL_REQ', 'EMU.BIASTESTCTRL.FORCE_GMC_CAL_REQ', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTESTCTRL_BIAS_RIP_RESET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTESTCTRL_BIAS_RIP_RESET, self).__init__(register,
            'BIAS_RIP_RESET', 'EMU.BIASTESTCTRL.BIAS_RIP_RESET', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTESTCTRL_BIAS_RIP_OVR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTESTCTRL_BIAS_RIP_OVR, self).__init__(register,
            'BIAS_RIP_OVR', 'EMU.BIASTESTCTRL.BIAS_RIP_OVR', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTESTCTRL_BIAS_RIP_OVR_CLK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTESTCTRL_BIAS_RIP_OVR_CLK, self).__init__(register,
            'BIAS_RIP_OVR_CLK', 'EMU.BIASTESTCTRL.BIAS_RIP_OVR_CLK', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTESTCTRL_BIAS_GMC_CALIB_OVR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTESTCTRL_BIAS_GMC_CALIB_OVR, self).__init__(register,
            'BIAS_GMC_CALIB_OVR', 'EMU.BIASTESTCTRL.BIAS_GMC_CALIB_OVR', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTESTCTRL_BIAS_DLY_SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTESTCTRL_BIAS_DLY_SEL, self).__init__(register,
            'BIAS_DLY_SEL', 'EMU.BIASTESTCTRL.BIAS_DLY_SEL', 'read-write',
            "",
            8, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTESTCTRL_GMC_CALIB_OVR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTESTCTRL_GMC_CALIB_OVR, self).__init__(register,
            'GMC_CALIB_OVR', 'EMU.BIASTESTCTRL.GMC_CALIB_OVR', 'read-write',
            "",
            12, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTESTCTRL_TM_BIASRDY_MASK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTESTCTRL_TM_BIASRDY_MASK, self).__init__(register,
            'TM_BIASRDY_MASK', 'EMU.BIASTESTCTRL.TM_BIASRDY_MASK', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTESTCTRL_BLANK_BIAS_RDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTESTCTRL_BLANK_BIAS_RDY, self).__init__(register,
            'BLANK_BIAS_RDY', 'EMU.BIASTESTCTRL.BLANK_BIAS_RDY', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTESTCTRL_OVR_BIAS_RDY_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTESTCTRL_OVR_BIAS_RDY_EN, self).__init__(register,
            'OVR_BIAS_RDY_EN', 'EMU.BIASTESTCTRL.OVR_BIAS_RDY_EN', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BIASTESTCTRL_OVR_BIAS_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BIASTESTCTRL_OVR_BIAS_EN, self).__init__(register,
            'OVR_BIAS_EN', 'EMU.BIASTESTCTRL.OVR_BIAS_EN', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_LFRCO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_LFRCO, self).__init__(register,
            'ISO_LFRCO', 'EMU.TESTCTRLANAISO.ISO_LFRCO', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_LFXO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_LFXO, self).__init__(register,
            'ISO_LFXO', 'EMU.TESTCTRLANAISO.ISO_LFXO', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_ULFRCO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_ULFRCO, self).__init__(register,
            'ISO_ULFRCO', 'EMU.TESTCTRLANAISO.ISO_ULFRCO', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_HFRCO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_HFRCO, self).__init__(register,
            'ISO_HFRCO', 'EMU.TESTCTRLANAISO.ISO_HFRCO', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_AUXHFRCO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_AUXHFRCO, self).__init__(register,
            'ISO_AUXHFRCO', 'EMU.TESTCTRLANAISO.ISO_AUXHFRCO', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_EMUOSC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_EMUOSC, self).__init__(register,
            'ISO_EMUOSC', 'EMU.TESTCTRLANAISO.ISO_EMUOSC', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_BIAS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_BIAS, self).__init__(register,
            'ISO_BIAS', 'EMU.TESTCTRLANAISO.ISO_BIAS', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_PORBOD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_PORBOD, self).__init__(register,
            'ISO_PORBOD', 'EMU.TESTCTRLANAISO.ISO_PORBOD', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_CMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_CMP, self).__init__(register,
            'ISO_CMP', 'EMU.TESTCTRLANAISO.ISO_CMP', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_ADC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_ADC, self).__init__(register,
            'ISO_ADC', 'EMU.TESTCTRLANAISO.ISO_ADC', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_DAC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_DAC, self).__init__(register,
            'ISO_DAC', 'EMU.TESTCTRLANAISO.ISO_DAC', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_AMUXCP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_AMUXCP, self).__init__(register,
            'ISO_AMUXCP', 'EMU.TESTCTRLANAISO.ISO_AMUXCP', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_DCDC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_DCDC, self).__init__(register,
            'ISO_DCDC', 'EMU.TESTCTRLANAISO.ISO_DCDC', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_BCLFRCO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_BCLFRCO, self).__init__(register,
            'ISO_BCLFRCO', 'EMU.TESTCTRLANAISO.ISO_BCLFRCO', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_FLASHVREF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_FLASHVREF, self).__init__(register,
            'ISO_FLASHVREF', 'EMU.TESTCTRLANAISO.ISO_FLASHVREF', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_CSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_CSEN, self).__init__(register,
            'ISO_CSEN', 'EMU.TESTCTRLANAISO.ISO_CSEN', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_WFXO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_WFXO, self).__init__(register,
            'ISO_WFXO', 'EMU.TESTCTRLANAISO.ISO_WFXO', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_RADIO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_RADIO, self).__init__(register,
            'ISO_RADIO', 'EMU.TESTCTRLANAISO.ISO_RADIO', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTCTRLANAISO_ISO_LVDS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTCTRLANAISO_ISO_LVDS, self).__init__(register,
            'ISO_LVDS', 'EMU.TESTCTRLANAISO.ISO_LVDS', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM01COUNTERWAIT_BODSETTLEWAIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM01COUNTERWAIT_BODSETTLEWAIT, self).__init__(register,
            'BODSETTLEWAIT', 'EMU.EM01COUNTERWAIT.BODSETTLEWAIT', 'read-write',
            "",
            0, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM01COUNTERWAIT_HDREGSTEPWAIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM01COUNTERWAIT_HDREGSTEPWAIT, self).__init__(register,
            'HDREGSTEPWAIT', 'EMU.EM01COUNTERWAIT.HDREGSTEPWAIT', 'read-write',
            "",
            5, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM01COUNTERWAIT_VSBODINTWAIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM01COUNTERWAIT_VSBODINTWAIT, self).__init__(register,
            'VSBODINTWAIT', 'EMU.EM01COUNTERWAIT.VSBODINTWAIT', 'read-write',
            "",
            10, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM01COUNTERWAIT_FLASHVREFBYPASSDISWAIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM01COUNTERWAIT_FLASHVREFBYPASSDISWAIT, self).__init__(register,
            'FLASHVREFBYPASSDISWAIT', 'EMU.EM01COUNTERWAIT.FLASHVREFBYPASSDISWAIT', 'read-write',
            "",
            15, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RAM1FEATURE_RAMSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RAM1FEATURE_RAMSIZE, self).__init__(register,
            'RAMSIZE', 'EMU.RAM1FEATURE.RAMSIZE', 'write-only',
            "",
            0, 2,
            RM_Enum_EMU_RAM1FEATURE_RAMSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RAM2FEATURE_RAMSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RAM2FEATURE_RAMSIZE, self).__init__(register,
            'RAMSIZE', 'EMU.RAM2FEATURE.RAMSIZE', 'write-only',
            "",
            0, 1,
            RM_Enum_EMU_RAM2FEATURE_RAMSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RAMBIASCONF_RAMBIASCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RAMBIASCONF_RAMBIASCTRL, self).__init__(register,
            'RAMBIASCTRL', 'EMU.RAMBIASCONF.RAMBIASCTRL', 'read-write',
            "",
            0, 4,
            RM_Enum_EMU_RAMBIASCONF_RAMBIASCTRL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTRAMRM_TGTRAMRM0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTRAMRM_TGTRAMRM0, self).__init__(register,
            'TGTRAMRM0', 'EMU.TGTRAMRM.TGTRAMRM0', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTRAMRM_TGTRAMRM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTRAMRM_TGTRAMRM1, self).__init__(register,
            'TGTRAMRM1', 'EMU.TGTRAMRM.TGTRAMRM1', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTRAMRM_TGTRAMRM2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTRAMRM_TGTRAMRM2, self).__init__(register,
            'TGTRAMRM2', 'EMU.TGTRAMRM.TGTRAMRM2', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTDECBODTHR_TGTDECBODTHR0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTDECBODTHR_TGTDECBODTHR0, self).__init__(register,
            'TGTDECBODTHR0', 'EMU.TGTDECBODTHR.TGTDECBODTHR0', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTDECBODTHR_TGTDECBODTHR1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTDECBODTHR_TGTDECBODTHR1, self).__init__(register,
            'TGTDECBODTHR1', 'EMU.TGTDECBODTHR.TGTDECBODTHR1', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTDECBODTHR_TGTDECBODTHR2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTDECBODTHR_TGTDECBODTHR2, self).__init__(register,
            'TGTDECBODTHR2', 'EMU.TGTDECBODTHR.TGTDECBODTHR2', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTHDREGTRIM_TGTHDREGTRIM0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTHDREGTRIM_TGTHDREGTRIM0, self).__init__(register,
            'TGTHDREGTRIM0', 'EMU.TGTHDREGTRIM.TGTHDREGTRIM0', 'read-write',
            "",
            0, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTHDREGTRIM_TGTHDREGTRIM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTHDREGTRIM_TGTHDREGTRIM1, self).__init__(register,
            'TGTHDREGTRIM1', 'EMU.TGTHDREGTRIM.TGTHDREGTRIM1', 'read-write',
            "",
            8, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTHDREGTRIM_TGTHDREGTRIM2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTHDREGTRIM_TGTHDREGTRIM2, self).__init__(register,
            'TGTHDREGTRIM2', 'EMU.TGTHDREGTRIM.TGTHDREGTRIM2', 'read-write',
            "",
            16, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTDCDCLNVCTRL_TGTDCDCLNVCTRL0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTDCDCLNVCTRL_TGTDCDCLNVCTRL0, self).__init__(register,
            'TGTDCDCLNVCTRL0', 'EMU.TGTDCDCLNVCTRL.TGTDCDCLNVCTRL0', 'read-write',
            "",
            0, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTDCDCLNVCTRL_TGTDCDCLNVCTRL1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTDCDCLNVCTRL_TGTDCDCLNVCTRL1, self).__init__(register,
            'TGTDCDCLNVCTRL1', 'EMU.TGTDCDCLNVCTRL.TGTDCDCLNVCTRL1', 'read-write',
            "",
            8, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTDCDCLNVCTRL_TGTDCDCLNVCTRL2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTDCDCLNVCTRL_TGTDCDCLNVCTRL2, self).__init__(register,
            'TGTDCDCLNVCTRL2', 'EMU.TGTDCDCLNVCTRL.TGTDCDCLNVCTRL2', 'read-write',
            "",
            16, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTLDREGTRIM_TGTLDREGTRIM0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTLDREGTRIM_TGTLDREGTRIM0, self).__init__(register,
            'TGTLDREGTRIM0', 'EMU.TGTLDREGTRIM.TGTLDREGTRIM0', 'read-write',
            "",
            0, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTLDREGTRIM_TGTLDREGTRIM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTLDREGTRIM_TGTLDREGTRIM1, self).__init__(register,
            'TGTLDREGTRIM1', 'EMU.TGTLDREGTRIM.TGTLDREGTRIM1', 'read-write',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTLDREGTRIM_TGTLDREGTRIM2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTLDREGTRIM_TGTLDREGTRIM2, self).__init__(register,
            'TGTLDREGTRIM2', 'EMU.TGTLDREGTRIM.TGTLDREGTRIM2', 'read-write',
            "",
            16, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTDCDCLPVCTRL_TGTDCDCLPVCTRL0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTDCDCLPVCTRL_TGTDCDCLPVCTRL0, self).__init__(register,
            'TGTDCDCLPVCTRL0', 'EMU.TGTDCDCLPVCTRL.TGTDCDCLPVCTRL0', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIML0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIML0, self).__init__(register,
            'TGTRREGTRIML0', 'EMU.TGTRREGTRIM.TGTRREGTRIML0', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIMH0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIMH0, self).__init__(register,
            'TGTRREGTRIMH0', 'EMU.TGTRREGTRIM.TGTRREGTRIMH0', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIML1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIML1, self).__init__(register,
            'TGTRREGTRIML1', 'EMU.TGTRREGTRIM.TGTRREGTRIML1', 'read-write',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIMH1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIMH1, self).__init__(register,
            'TGTRREGTRIMH1', 'EMU.TGTRREGTRIM.TGTRREGTRIMH1', 'read-write',
            "",
            12, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIML2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIML2, self).__init__(register,
            'TGTRREGTRIML2', 'EMU.TGTRREGTRIM.TGTRREGTRIML2', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIMH2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIMH2, self).__init__(register,
            'TGTRREGTRIMH2', 'EMU.TGTRREGTRIM.TGTRREGTRIMH2', 'read-write',
            "",
            20, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTHFRCOCTRL_TUNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTHFRCOCTRL_TUNING, self).__init__(register,
            'TUNING', 'EMU.TGTHFRCOCTRL.TUNING', 'read-write',
            "",
            0, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTHFRCOCTRL_FINETUNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTHFRCOCTRL_FINETUNING, self).__init__(register,
            'FINETUNING', 'EMU.TGTHFRCOCTRL.FINETUNING', 'read-write',
            "",
            8, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTHFRCOCTRL_FREQRANGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTHFRCOCTRL_FREQRANGE, self).__init__(register,
            'FREQRANGE', 'EMU.TGTHFRCOCTRL.FREQRANGE', 'read-write',
            "",
            16, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTHFRCOCTRL_CMPBIAS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTHFRCOCTRL_CMPBIAS, self).__init__(register,
            'CMPBIAS', 'EMU.TGTHFRCOCTRL.CMPBIAS', 'read-write',
            "",
            21, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTHFRCOCTRL_LDOHP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTHFRCOCTRL_LDOHP, self).__init__(register,
            'LDOHP', 'EMU.TGTHFRCOCTRL.LDOHP', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTHFRCOCTRL_CLKDIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTHFRCOCTRL_CLKDIV, self).__init__(register,
            'CLKDIV', 'EMU.TGTHFRCOCTRL.CLKDIV', 'read-write',
            "",
            25, 2,
            RM_Enum_EMU_TGTHFRCOCTRL_CLKDIV(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTHFRCOCTRL_FINETUNINGEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTHFRCOCTRL_FINETUNINGEN, self).__init__(register,
            'FINETUNINGEN', 'EMU.TGTHFRCOCTRL.FINETUNINGEN', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TGTHFRCOCTRL_VREFTC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TGTHFRCOCTRL_VREFTC, self).__init__(register,
            'VREFTC', 'EMU.TGTHFRCOCTRL.VREFTC', 'read-write',
            "",
            28, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGCALIB_RREG_HIGHSIDE_TRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGCALIB_RREG_HIGHSIDE_TRIM, self).__init__(register,
            'RREG_HIGHSIDE_TRIM', 'EMU.RREGCALIB.RREG_HIGHSIDE_TRIM', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGCALIB_RREG_LOWSIDE_TRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGCALIB_RREG_LOWSIDE_TRIM, self).__init__(register,
            'RREG_LOWSIDE_TRIM', 'EMU.RREGCALIB.RREG_LOWSIDE_TRIM', 'read-write',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGCALIB_RREG_IDAC_TRIMH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGCALIB_RREG_IDAC_TRIMH, self).__init__(register,
            'RREG_IDAC_TRIMH', 'EMU.RREGCALIB.RREG_IDAC_TRIMH', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGCALIB_RREG_IDAC_TRIML(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGCALIB_RREG_IDAC_TRIML, self).__init__(register,
            'RREG_IDAC_TRIML', 'EMU.RREGCALIB.RREG_IDAC_TRIML', 'read-write',
            "",
            20, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGTEST_RREG_SW_GATE_DRAIN_DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGTEST_RREG_SW_GATE_DRAIN_DIS, self).__init__(register,
            'RREG_SW_GATE_DRAIN_DIS', 'EMU.RREGTEST.RREG_SW_GATE_DRAIN_DIS', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGTEST_RREG_HIGHSIDE_SW_DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGTEST_RREG_HIGHSIDE_SW_DIS, self).__init__(register,
            'RREG_HIGHSIDE_SW_DIS', 'EMU.RREGTEST.RREG_HIGHSIDE_SW_DIS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGTEST_RREG_LOWSIDE_SW_DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGTEST_RREG_LOWSIDE_SW_DIS, self).__init__(register,
            'RREG_LOWSIDE_SW_DIS', 'EMU.RREGTEST.RREG_LOWSIDE_SW_DIS', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGTEST_RREG_BIAS_5NA_P_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGTEST_RREG_BIAS_5NA_P_EN, self).__init__(register,
            'RREG_BIAS_5NA_P_EN', 'EMU.RREGTEST.RREG_BIAS_5NA_P_EN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGTEST_RREG_CAL_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGTEST_RREG_CAL_EN, self).__init__(register,
            'RREG_CAL_EN', 'EMU.RREGTEST.RREG_CAL_EN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGTEST_RREG_CAL_RST(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGTEST_RREG_CAL_RST, self).__init__(register,
            'RREG_CAL_RST', 'EMU.RREGTEST.RREG_CAL_RST', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGTEST_RREG_STATUS_CMPOUT_HIGH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGTEST_RREG_STATUS_CMPOUT_HIGH, self).__init__(register,
            'RREG_STATUS_CMPOUT_HIGH', 'EMU.RREGTEST.RREG_STATUS_CMPOUT_HIGH', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGTEST_RREG_STATUS_CMPOUT_LOW(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGTEST_RREG_STATUS_CMPOUT_LOW, self).__init__(register,
            'RREG_STATUS_CMPOUT_LOW', 'EMU.RREGTEST.RREG_STATUS_CMPOUT_LOW', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGOVERRIDE_RREG_OVERRIDE_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGOVERRIDE_RREG_OVERRIDE_EN, self).__init__(register,
            'RREG_OVERRIDE_EN', 'EMU.RREGOVERRIDE.RREG_OVERRIDE_EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGOVERRIDE_OVR_RREG_HIGHSIDE_PU_DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGOVERRIDE_OVR_RREG_HIGHSIDE_PU_DIS, self).__init__(register,
            'OVR_RREG_HIGHSIDE_PU_DIS', 'EMU.RREGOVERRIDE.OVR_RREG_HIGHSIDE_PU_DIS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGOVERRIDE_OVR_RREG_HIGHSIDE_PU_WEAK_DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGOVERRIDE_OVR_RREG_HIGHSIDE_PU_WEAK_DIS, self).__init__(register,
            'OVR_RREG_HIGHSIDE_PU_WEAK_DIS', 'EMU.RREGOVERRIDE.OVR_RREG_HIGHSIDE_PU_WEAK_DIS', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGOVERRIDE_OVR_RREG_LOWSIDE_PD_DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGOVERRIDE_OVR_RREG_LOWSIDE_PD_DIS, self).__init__(register,
            'OVR_RREG_LOWSIDE_PD_DIS', 'EMU.RREGOVERRIDE.OVR_RREG_LOWSIDE_PD_DIS', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGOVERRIDE_OVR_RREG_LOWSIDE_PD_WEAK_DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGOVERRIDE_OVR_RREG_LOWSIDE_PD_WEAK_DIS, self).__init__(register,
            'OVR_RREG_LOWSIDE_PD_WEAK_DIS', 'EMU.RREGOVERRIDE.OVR_RREG_LOWSIDE_PD_WEAK_DIS', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_RREGOVERRIDE_OVR_RREG_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_RREGOVERRIDE_OVR_RREG_EN, self).__init__(register,
            'OVR_RREG_EN', 'EMU.RREGOVERRIDE.OVR_RREG_EN', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BCOSCENCMD_BCLFRCOEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BCOSCENCMD_BCLFRCOEN, self).__init__(register,
            'BCLFRCOEN', 'EMU.BCOSCENCMD.BCLFRCOEN', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BCOSCENCMD_BCLFRCODIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BCOSCENCMD_BCLFRCODIS, self).__init__(register,
            'BCLFRCODIS', 'EMU.BCOSCENCMD.BCLFRCODIS', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BCLFRCOCTRL_TUNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BCLFRCOCTRL_TUNING, self).__init__(register,
            'TUNING', 'EMU.BCLFRCOCTRL.TUNING', 'read-write',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BCLFRCOCTRL_ENVREF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BCLFRCOCTRL_ENVREF, self).__init__(register,
            'ENVREF', 'EMU.BCLFRCOCTRL.ENVREF', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BCLFRCOCTRL_ENCHOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BCLFRCOCTRL_ENCHOP, self).__init__(register,
            'ENCHOP', 'EMU.BCLFRCOCTRL.ENCHOP', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BCLFRCOCTRL_ENDEM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BCLFRCOCTRL_ENDEM, self).__init__(register,
            'ENDEM', 'EMU.BCLFRCOCTRL.ENDEM', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BCLFRCOCTRL_TIMEOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BCLFRCOCTRL_TIMEOUT, self).__init__(register,
            'TIMEOUT', 'EMU.BCLFRCOCTRL.TIMEOUT', 'read-write',
            "",
            24, 2,
            RM_Enum_EMU_BCLFRCOCTRL_TIMEOUT(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_BCLFRCOCTRL_GMCCURTUNE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_BCLFRCOCTRL_GMCCURTUNE, self).__init__(register,
            'GMCCURTUNE', 'EMU.BCLFRCOCTRL.GMCCURTUNE', 'read-write',
            "",
            28, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTBCLFRCOCTRL_DISOSC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTBCLFRCOCTRL_DISOSC, self).__init__(register,
            'DISOSC', 'EMU.TESTBCLFRCOCTRL.DISOSC', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTBCLFRCOCTRL_DISSYNC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTBCLFRCOCTRL_DISSYNC, self).__init__(register,
            'DISSYNC', 'EMU.TESTBCLFRCOCTRL.DISSYNC', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTBCLFRCOCTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTBCLFRCOCTRL_MODE, self).__init__(register,
            'MODE', 'EMU.TESTBCLFRCOCTRL.MODE', 'read-write',
            "",
            4, 2,
            RM_Enum_EMU_TESTBCLFRCOCTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTBCLFRCOCTRL_SELCLKDIV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTBCLFRCOCTRL_SELCLKDIV, self).__init__(register,
            'SELCLKDIV', 'EMU.TESTBCLFRCOCTRL.SELCLKDIV', 'read-write',
            "",
            6, 2,
            RM_Enum_EMU_TESTBCLFRCOCTRL_SELCLKDIV(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTBCLFRCOCTRL_VREFUPDATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTBCLFRCOCTRL_VREFUPDATE, self).__init__(register,
            'VREFUPDATE', 'EMU.TESTBCLFRCOCTRL.VREFUPDATE', 'read-write',
            "",
            8, 2,
            RM_Enum_EMU_TESTBCLFRCOCTRL_VREFUPDATE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTBCLFRCOCTRL_VREFPRECH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTBCLFRCOCTRL_VREFPRECH, self).__init__(register,
            'VREFPRECH', 'EMU.TESTBCLFRCOCTRL.VREFPRECH', 'read-write',
            "",
            10, 2,
            RM_Enum_EMU_TESTBCLFRCOCTRL_VREFPRECH(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTBCLFRCOCTRL_FLIPCHOP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTBCLFRCOCTRL_FLIPCHOP, self).__init__(register,
            'FLIPCHOP', 'EMU.TESTBCLFRCOCTRL.FLIPCHOP', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTBCLFRCOCTRL_DEMCLKSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTBCLFRCOCTRL_DEMCLKSEL, self).__init__(register,
            'DEMCLKSEL', 'EMU.TESTBCLFRCOCTRL.DEMCLKSEL', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTBCLFRCOCTRL_WELLBUFDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTBCLFRCOCTRL_WELLBUFDIS, self).__init__(register,
            'WELLBUFDIS', 'EMU.TESTBCLFRCOCTRL.WELLBUFDIS', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTBCLFRCOCTRL_FORCECOMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTBCLFRCOCTRL_FORCECOMP, self).__init__(register,
            'FORCECOMP', 'EMU.TESTBCLFRCOCTRL.FORCECOMP', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTBCLFRCOCTRL_BLOCKIREF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTBCLFRCOCTRL_BLOCKIREF, self).__init__(register,
            'BLOCKIREF', 'EMU.TESTBCLFRCOCTRL.BLOCKIREF', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTBCLFRCOCTRL_RNSHUNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTBCLFRCOCTRL_RNSHUNT, self).__init__(register,
            'RNSHUNT', 'EMU.TESTBCLFRCOCTRL.RNSHUNT', 'read-write',
            "",
            20, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TESTBCLFRCOCTRL_RPSHUNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TESTBCLFRCOCTRL_RPSHUNT, self).__init__(register,
            'RPSHUNT', 'EMU.TESTBCLFRCOCTRL.RPSHUNT', 'read-write',
            "",
            24, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_PORBOD2_PORBOD_REFTRIMEM2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_PORBOD2_PORBOD_REFTRIMEM2, self).__init__(register,
            'PORBOD_REFTRIMEM2', 'EMU.PORBOD2.PORBOD_REFTRIMEM2', 'read-write',
            "",
            0, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_BYPASS_DIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_BYPASS_DIS, self).__init__(register,
            'FLASHVREF_BYPASS_DIS', 'EMU.FLASHVREFCALIB.FLASHVREF_BYPASS_DIS', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_BYPASS_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_BYPASS_EN, self).__init__(register,
            'FLASHVREF_BYPASS_EN', 'EMU.FLASHVREFCALIB.FLASHVREF_BYPASS_EN', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_BYPASS_STATUS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_BYPASS_STATUS, self).__init__(register,
            'FLASHVREF_BYPASS_STATUS', 'EMU.FLASHVREFCALIB.FLASHVREF_BYPASS_STATUS', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_EN, self).__init__(register,
            'FLASHVREF_EN', 'EMU.FLASHVREFCALIB.FLASHVREF_EN', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_SEL, self).__init__(register,
            'FLASHVREF_SEL', 'EMU.FLASHVREFCALIB.FLASHVREF_SEL', 'read-write',
            "",
            4, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_TRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_TRIM, self).__init__(register,
            'FLASHVREF_TRIM', 'EMU.FLASHVREFCALIB.FLASHVREF_TRIM', 'read-write',
            "",
            9, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_VREFDIS_EM23(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_VREFDIS_EM23, self).__init__(register,
            'FLASHVREF_VREFDIS_EM23', 'EMU.FLASHVREFCALIB.FLASHVREF_VREFDIS_EM23', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_PULLDOWNEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_PULLDOWNEN, self).__init__(register,
            'FLASHVREF_PULLDOWNEN', 'EMU.FLASHVREFCALIB.FLASHVREF_PULLDOWNEN', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_DUTYSCALE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_DUTYSCALE, self).__init__(register,
            'FLASHVREF_DUTYSCALE', 'EMU.FLASHVREFCALIB.FLASHVREF_DUTYSCALE', 'read-write',
            "",
            17, 2,
            RM_Enum_EMU_FLASHVREFCALIB_FLASHVREF_DUTYSCALE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPLO_THR0_TEMPLO0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPLO_THR0_TEMPLO0, self).__init__(register,
            'TEMPLO0', 'EMU.TEMPLO_THR0.TEMPLO0', 'write-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPLO_THR0_TEMPLO1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPLO_THR0_TEMPLO1, self).__init__(register,
            'TEMPLO1', 'EMU.TEMPLO_THR0.TEMPLO1', 'write-only',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPLO_THR0_TEMPLO2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPLO_THR0_TEMPLO2, self).__init__(register,
            'TEMPLO2', 'EMU.TEMPLO_THR0.TEMPLO2', 'write-only',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPLO_THR0_TEMPLO3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPLO_THR0_TEMPLO3, self).__init__(register,
            'TEMPLO3', 'EMU.TEMPLO_THR0.TEMPLO3', 'write-only',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPHI_THR0_TEMPHI0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPHI_THR0_TEMPHI0, self).__init__(register,
            'TEMPHI0', 'EMU.TEMPHI_THR0.TEMPHI0', 'write-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPHI_THR0_TEMPHI1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPHI_THR0_TEMPHI1, self).__init__(register,
            'TEMPHI1', 'EMU.TEMPHI_THR0.TEMPHI1', 'write-only',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPHI_THR0_TEMPHI2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPHI_THR0_TEMPHI2, self).__init__(register,
            'TEMPHI2', 'EMU.TEMPHI_THR0.TEMPHI2', 'write-only',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPHI_THR0_TEMPHI3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPHI_THR0_TEMPHI3, self).__init__(register,
            'TEMPHI3', 'EMU.TEMPHI_THR0.TEMPHI3', 'write-only',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPLO_THR1_TEMPLO4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPLO_THR1_TEMPLO4, self).__init__(register,
            'TEMPLO4', 'EMU.TEMPLO_THR1.TEMPLO4', 'write-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPLO_THR1_TEMPLO5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPLO_THR1_TEMPLO5, self).__init__(register,
            'TEMPLO5', 'EMU.TEMPLO_THR1.TEMPLO5', 'write-only',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPLO_THR1_TEMPLO6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPLO_THR1_TEMPLO6, self).__init__(register,
            'TEMPLO6', 'EMU.TEMPLO_THR1.TEMPLO6', 'write-only',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPLO_THR1_TEMPLO7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPLO_THR1_TEMPLO7, self).__init__(register,
            'TEMPLO7', 'EMU.TEMPLO_THR1.TEMPLO7', 'write-only',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPHI_THR1_TEMPHI4(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPHI_THR1_TEMPHI4, self).__init__(register,
            'TEMPHI4', 'EMU.TEMPHI_THR1.TEMPHI4', 'write-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPHI_THR1_TEMPHI5(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPHI_THR1_TEMPHI5, self).__init__(register,
            'TEMPHI5', 'EMU.TEMPHI_THR1.TEMPHI5', 'write-only',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPHI_THR1_TEMPHI6(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPHI_THR1_TEMPHI6, self).__init__(register,
            'TEMPHI6', 'EMU.TEMPHI_THR1.TEMPHI6', 'write-only',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPHI_THR1_TEMPHI7(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPHI_THR1_TEMPHI7, self).__init__(register,
            'TEMPHI7', 'EMU.TEMPHI_THR1.TEMPHI7', 'write-only',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_TEMPLO_THR2_TEMPLO8(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_TEMPLO_THR2_TEMPLO8, self).__init__(register,
            'TEMPLO8', 'EMU.TEMPLO_THR2.TEMPLO8', 'write-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGAEN_DIAGA_GP_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGAEN_DIAGA_GP_EN, self).__init__(register,
            'DIAGA_GP_EN', 'EMU.DIAGAEN.DIAGA_GP_EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGAEN_DIAGA_RF_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGAEN_DIAGA_RF_EN, self).__init__(register,
            'DIAGA_RF_EN', 'EMU.DIAGAEN.DIAGA_RF_EN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGAEN_DIAGPN_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGAEN_DIAGPN_EN, self).__init__(register,
            'DIAGPN_EN', 'EMU.DIAGAEN.DIAGPN_EN', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGAEN_ABUS_DIAGA_GP_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGAEN_ABUS_DIAGA_GP_EN, self).__init__(register,
            'ABUS_DIAGA_GP_EN', 'EMU.DIAGAEN.ABUS_DIAGA_GP_EN', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGAEN_ABUS_DIAGA_RF_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGAEN_ABUS_DIAGA_RF_EN, self).__init__(register,
            'ABUS_DIAGA_RF_EN', 'EMU.DIAGAEN.ABUS_DIAGA_RF_EN', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGAEN_DIAGPN_PADMUXEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGAEN_DIAGPN_PADMUXEN, self).__init__(register,
            'DIAGPN_PADMUXEN', 'EMU.DIAGAEN.DIAGPN_PADMUXEN', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGABLKTPSEL_GPTP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGABLKTPSEL_GPTP, self).__init__(register,
            'GPTP', 'EMU.DIAGABLKTPSEL.GPTP', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGABLKTPSEL_GPBLK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGABLKTPSEL_GPBLK, self).__init__(register,
            'GPBLK', 'EMU.DIAGABLKTPSEL.GPBLK', 'read-write',
            "",
            8, 6,
            RM_Enum_EMU_DIAGABLKTPSEL_GPBLK(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGABLKTPSEL_RFTP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGABLKTPSEL_RFTP, self).__init__(register,
            'RFTP', 'EMU.DIAGABLKTPSEL.RFTP', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGABLKTPSEL_RFBLK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGABLKTPSEL_RFBLK, self).__init__(register,
            'RFBLK', 'EMU.DIAGABLKTPSEL.RFBLK', 'read-write',
            "",
            24, 5,
            RM_Enum_EMU_DIAGABLKTPSEL_RFBLK(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGPNBLKSEL_PNRFBLK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGPNBLKSEL_PNRFBLK, self).__init__(register,
            'PNRFBLK', 'EMU.DIAGPNBLKSEL.PNRFBLK', 'read-write',
            "",
            8, 4,
            RM_Enum_EMU_DIAGPNBLKSEL_PNRFBLK(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGABRIDGESEL_ABUS_DIAGA_GP_SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGABRIDGESEL_ABUS_DIAGA_GP_SEL, self).__init__(register,
            'ABUS_DIAGA_GP_SEL', 'EMU.DIAGABRIDGESEL.ABUS_DIAGA_GP_SEL', 'read-write',
            "",
            0, 2,
            RM_Enum_EMU_DIAGABRIDGESEL_ABUS_DIAGA_GP_SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGABRIDGESEL_DIAGA_GP_BUF_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGABRIDGESEL_DIAGA_GP_BUF_EN, self).__init__(register,
            'DIAGA_GP_BUF_EN', 'EMU.DIAGABRIDGESEL.DIAGA_GP_BUF_EN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGABRIDGESEL_DIAGA_GP_SHORT_N(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGABRIDGESEL_DIAGA_GP_SHORT_N, self).__init__(register,
            'DIAGA_GP_SHORT_N', 'EMU.DIAGABRIDGESEL.DIAGA_GP_SHORT_N', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGABRIDGESEL_ABUS_DIAGA_RF_SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGABRIDGESEL_ABUS_DIAGA_RF_SEL, self).__init__(register,
            'ABUS_DIAGA_RF_SEL', 'EMU.DIAGABRIDGESEL.ABUS_DIAGA_RF_SEL', 'read-write',
            "",
            16, 2,
            RM_Enum_EMU_DIAGABRIDGESEL_ABUS_DIAGA_RF_SEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGABRIDGESEL_DIAGA_RF_BUF_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGABRIDGESEL_DIAGA_RF_BUF_EN, self).__init__(register,
            'DIAGA_RF_BUF_EN', 'EMU.DIAGABRIDGESEL.DIAGA_RF_BUF_EN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGABRIDGESEL_DIAGA_RF_SHORT_N(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGABRIDGESEL_DIAGA_RF_SHORT_N, self).__init__(register,
            'DIAGA_RF_SHORT_N', 'EMU.DIAGABRIDGESEL.DIAGA_RF_SHORT_N', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGABRIDGESEL_DIAGPN_BUF_EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGABRIDGESEL_DIAGPN_BUF_EN, self).__init__(register,
            'DIAGPN_BUF_EN', 'EMU.DIAGABRIDGESEL.DIAGPN_BUF_EN', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_DIAGABRIDGESEL_DIAGA_SEL_VDDX(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_DIAGABRIDGESEL_DIAGA_SEL_VDDX, self).__init__(register,
            'DIAGA_SEL_VDDX', 'EMU.DIAGABRIDGESEL.DIAGA_SEL_VDDX', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_APDPGPIOSEL_APORT_DP_GPIO_SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_APDPGPIOSEL_APORT_DP_GPIO_SEL, self).__init__(register,
            'APORT_DP_GPIO_SEL', 'EMU.APDPGPIOSEL.APORT_DP_GPIO_SEL', 'read-write',
            "",
            0, 17)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_APDNGPIOSEL_APORT_DN_GPIO_SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_APDNGPIOSEL_APORT_DN_GPIO_SEL, self).__init__(register,
            'APORT_DN_GPIO_SEL', 'EMU.APDNGPIOSEL.APORT_DN_GPIO_SEL', 'read-write',
            "",
            0, 17)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_APAPGPIOSEL_APORT_AP_GPIO_SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_APAPGPIOSEL_APORT_AP_GPIO_SEL, self).__init__(register,
            'APORT_AP_GPIO_SEL', 'EMU.APAPGPIOSEL.APORT_AP_GPIO_SEL', 'read-write',
            "",
            0, 17)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_APANGPIOSEL_APORT_AN_GPIO_SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_APANGPIOSEL_APORT_AN_GPIO_SEL, self).__init__(register,
            'APORT_AN_GPIO_SEL', 'EMU.APANGPIOSEL.APORT_AN_GPIO_SEL', 'read-write',
            "",
            0, 17)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_APBPGPIOSEL_APORT_BP_GPIO_SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_APBPGPIOSEL_APORT_BP_GPIO_SEL, self).__init__(register,
            'APORT_BP_GPIO_SEL', 'EMU.APBPGPIOSEL.APORT_BP_GPIO_SEL', 'read-write',
            "",
            0, 17)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_APBNGPIOSEL_APORT_BN_GPIO_SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_APBNGPIOSEL_APORT_BN_GPIO_SEL, self).__init__(register,
            'APORT_BN_GPIO_SEL', 'EMU.APBNGPIOSEL.APORT_BN_GPIO_SEL', 'read-write',
            "",
            0, 17)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_APCPGPIOSEL_APORT_CP_GPIO_SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_APCPGPIOSEL_APORT_CP_GPIO_SEL, self).__init__(register,
            'APORT_CP_GPIO_SEL', 'EMU.APCPGPIOSEL.APORT_CP_GPIO_SEL', 'read-write',
            "",
            0, 17)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_APCNGPIOSEL_APORT_CN_GPIO_SEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_APCNGPIOSEL_APORT_CN_GPIO_SEL, self).__init__(register,
            'APORT_CN_GPIO_SEL', 'EMU.APCNGPIOSEL.APORT_CN_GPIO_SEL', 'read-write',
            "",
            0, 17)
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM2PERCTRL_EM2PERPWDN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM2PERCTRL_EM2PERPWDN, self).__init__(register,
            'EM2PERPWDN', 'EMU.EM2PERCTRL.EM2PERPWDN', 'read-write',
            "",
            0, 2,
            RM_Enum_EMU_EM2PERCTRL_EM2PERPWDN(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_EMU_EM2PERCTRL_EM2PERPWUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_EMU_EM2PERCTRL_EM2PERPWUP, self).__init__(register,
            'EM2PERPWUP', 'EMU.EM2PERCTRL.EM2PERPWUP', 'read-write',
            "",
            2, 2,
            RM_Enum_EMU_EM2PERCTRL_EM2PERPWUP(register.zz_label))
        self.__dict__['zz_frozen'] = True


