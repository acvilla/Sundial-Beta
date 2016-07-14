
from static import Base_RM_Register
from EMU_field import *


class RM_Register_EMU_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_CTRL, self).__init__(rmio, label,
            0x400e3000, 0x000,
            'CTRL', 'EMU.CTRL', 'read-write',
            "",
            0x00000000, 0x0003031F)

        self.EM23VREG = RM_Field_EMU_CTRL_EM23VREG(self)
        self.zz_fdict['EM23VREG'] = self.EM23VREG
        self.EM2BLOCK = RM_Field_EMU_CTRL_EM2BLOCK(self)
        self.zz_fdict['EM2BLOCK'] = self.EM2BLOCK
        self.EM2BODDIS = RM_Field_EMU_CTRL_EM2BODDIS(self)
        self.zz_fdict['EM2BODDIS'] = self.EM2BODDIS
        self.EM01LD = RM_Field_EMU_CTRL_EM01LD(self)
        self.zz_fdict['EM01LD'] = self.EM01LD
        self.EM23VSCALEAUTOWSEN = RM_Field_EMU_CTRL_EM23VSCALEAUTOWSEN(self)
        self.zz_fdict['EM23VSCALEAUTOWSEN'] = self.EM23VSCALEAUTOWSEN
        self.EM23VSCALE = RM_Field_EMU_CTRL_EM23VSCALE(self)
        self.zz_fdict['EM23VSCALE'] = self.EM23VSCALE
        self.EM4HVSCALE = RM_Field_EMU_CTRL_EM4HVSCALE(self)
        self.zz_fdict['EM4HVSCALE'] = self.EM4HVSCALE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_STATUS, self).__init__(rmio, label,
            0x400e3000, 0x004,
            'STATUS', 'EMU.STATUS', 'read-only',
            "",
            0x00000000, 0xF617011F)

        self.VMONRDY = RM_Field_EMU_STATUS_VMONRDY(self)
        self.zz_fdict['VMONRDY'] = self.VMONRDY
        self.VMONAVDD = RM_Field_EMU_STATUS_VMONAVDD(self)
        self.zz_fdict['VMONAVDD'] = self.VMONAVDD
        self.VMONALTAVDD = RM_Field_EMU_STATUS_VMONALTAVDD(self)
        self.zz_fdict['VMONALTAVDD'] = self.VMONALTAVDD
        self.VMONDVDD = RM_Field_EMU_STATUS_VMONDVDD(self)
        self.zz_fdict['VMONDVDD'] = self.VMONDVDD
        self.VMONIO0 = RM_Field_EMU_STATUS_VMONIO0(self)
        self.zz_fdict['VMONIO0'] = self.VMONIO0
        self.VMONFVDD = RM_Field_EMU_STATUS_VMONFVDD(self)
        self.zz_fdict['VMONFVDD'] = self.VMONFVDD
        self.VSCALE = RM_Field_EMU_STATUS_VSCALE(self)
        self.zz_fdict['VSCALE'] = self.VSCALE
        self.VSCALEBUSY = RM_Field_EMU_STATUS_VSCALEBUSY(self)
        self.zz_fdict['VSCALEBUSY'] = self.VSCALEBUSY
        self.EM4IORET = RM_Field_EMU_STATUS_EM4IORET(self)
        self.zz_fdict['EM4IORET'] = self.EM4IORET
        self.RACACTIVE = RM_Field_EMU_STATUS_RACACTIVE(self)
        self.zz_fdict['RACACTIVE'] = self.RACACTIVE
        self.TEMPACTIVE = RM_Field_EMU_STATUS_TEMPACTIVE(self)
        self.zz_fdict['TEMPACTIVE'] = self.TEMPACTIVE
        self.CALACTIVE = RM_Field_EMU_STATUS_CALACTIVE(self)
        self.zz_fdict['CALACTIVE'] = self.CALACTIVE
        self.CALCOMPOUT = RM_Field_EMU_STATUS_CALCOMPOUT(self)
        self.zz_fdict['CALCOMPOUT'] = self.CALCOMPOUT
        self.BCLFRCOENS = RM_Field_EMU_STATUS_BCLFRCOENS(self)
        self.zz_fdict['BCLFRCOENS'] = self.BCLFRCOENS
        self.BCLFRCORDY = RM_Field_EMU_STATUS_BCLFRCORDY(self)
        self.zz_fdict['BCLFRCORDY'] = self.BCLFRCORDY
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_LOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_LOCK, self).__init__(rmio, label,
            0x400e3000, 0x008,
            'LOCK', 'EMU.LOCK', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.LOCKKEY = RM_Field_EMU_LOCK_LOCKKEY(self)
        self.zz_fdict['LOCKKEY'] = self.LOCKKEY
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_RAM0CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_RAM0CTRL, self).__init__(rmio, label,
            0x400e3000, 0x00C,
            'RAM0CTRL', 'EMU.RAM0CTRL', 'read-write',
            "",
            0x00000000, 0xC000000F)

        self.RAMPOWERDOWN = RM_Field_EMU_RAM0CTRL_RAMPOWERDOWN(self)
        self.zz_fdict['RAMPOWERDOWN'] = self.RAMPOWERDOWN
        self.SEQRAMPOWERDOWN = RM_Field_EMU_RAM0CTRL_SEQRAMPOWERDOWN(self)
        self.zz_fdict['SEQRAMPOWERDOWN'] = self.SEQRAMPOWERDOWN
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_CMD, self).__init__(rmio, label,
            0x400e3000, 0x010,
            'CMD', 'EMU.CMD', 'write-only',
            "",
            0x00000000, 0x00000073)

        self.EM4UNLATCH = RM_Field_EMU_CMD_EM4UNLATCH(self)
        self.zz_fdict['EM4UNLATCH'] = self.EM4UNLATCH
        self.LDREFEN = RM_Field_EMU_CMD_LDREFEN(self)
        self.zz_fdict['LDREFEN'] = self.LDREFEN
        self.EM01VSCALE0 = RM_Field_EMU_CMD_EM01VSCALE0(self)
        self.zz_fdict['EM01VSCALE0'] = self.EM01VSCALE0
        self.EM01VSCALE1 = RM_Field_EMU_CMD_EM01VSCALE1(self)
        self.zz_fdict['EM01VSCALE1'] = self.EM01VSCALE1
        self.EM01VSCALE2 = RM_Field_EMU_CMD_EM01VSCALE2(self)
        self.zz_fdict['EM01VSCALE2'] = self.EM01VSCALE2
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_PERACTCONF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_PERACTCONF, self).__init__(rmio, label,
            0x400e3000, 0x014,
            'PERACTCONF', 'EMU.PERACTCONF', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.RACPER = RM_Field_EMU_PERACTCONF_RACPER(self)
        self.zz_fdict['RACPER'] = self.RACPER
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_EM4CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_EM4CTRL, self).__init__(rmio, label,
            0x400e3000, 0x018,
            'EM4CTRL', 'EMU.EM4CTRL', 'read-write',
            "",
            0x00000000, 0x0003013F)

        self.EM4STATE = RM_Field_EMU_EM4CTRL_EM4STATE(self)
        self.zz_fdict['EM4STATE'] = self.EM4STATE
        self.RETAINLFRCO = RM_Field_EMU_EM4CTRL_RETAINLFRCO(self)
        self.zz_fdict['RETAINLFRCO'] = self.RETAINLFRCO
        self.RETAINLFXO = RM_Field_EMU_EM4CTRL_RETAINLFXO(self)
        self.zz_fdict['RETAINLFXO'] = self.RETAINLFXO
        self.RETAINULFRCO = RM_Field_EMU_EM4CTRL_RETAINULFRCO(self)
        self.zz_fdict['RETAINULFRCO'] = self.RETAINULFRCO
        self.EM4IORETMODE = RM_Field_EMU_EM4CTRL_EM4IORETMODE(self)
        self.zz_fdict['EM4IORETMODE'] = self.EM4IORETMODE
        self.EM4ENTRY_CMU_HS_TO_DIS = RM_Field_EMU_EM4CTRL_EM4ENTRY_CMU_HS_TO_DIS(self)
        self.zz_fdict['EM4ENTRY_CMU_HS_TO_DIS'] = self.EM4ENTRY_CMU_HS_TO_DIS
        self.EM4ENTRY = RM_Field_EMU_EM4CTRL_EM4ENTRY(self)
        self.zz_fdict['EM4ENTRY'] = self.EM4ENTRY
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TEMPLIMITS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TEMPLIMITS, self).__init__(rmio, label,
            0x400e3000, 0x01C,
            'TEMPLIMITS', 'EMU.TEMPLIMITS', 'read-write',
            "",
            0x0000FF00, 0x0001FFFF)

        self.TEMPLOW = RM_Field_EMU_TEMPLIMITS_TEMPLOW(self)
        self.zz_fdict['TEMPLOW'] = self.TEMPLOW
        self.TEMPHIGH = RM_Field_EMU_TEMPLIMITS_TEMPHIGH(self)
        self.zz_fdict['TEMPHIGH'] = self.TEMPHIGH
        self.EM4WUEN = RM_Field_EMU_TEMPLIMITS_EM4WUEN(self)
        self.zz_fdict['EM4WUEN'] = self.EM4WUEN
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TEMP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TEMP, self).__init__(rmio, label,
            0x400e3000, 0x020,
            'TEMP', 'EMU.TEMP', 'read-only',
            "",
            0x00000000, 0x000000FF)

        self.TEMP = RM_Field_EMU_TEMP_TEMP(self)
        self.zz_fdict['TEMP'] = self.TEMP
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_IF, self).__init__(rmio, label,
            0x400e3000, 0x024,
            'IF', 'EMU.IF', 'read-only',
            "",
            0x00000000, 0xE31FC0FF)

        self.VMONAVDDFALL = RM_Field_EMU_IF_VMONAVDDFALL(self)
        self.zz_fdict['VMONAVDDFALL'] = self.VMONAVDDFALL
        self.VMONAVDDRISE = RM_Field_EMU_IF_VMONAVDDRISE(self)
        self.zz_fdict['VMONAVDDRISE'] = self.VMONAVDDRISE
        self.VMONALTAVDDFALL = RM_Field_EMU_IF_VMONALTAVDDFALL(self)
        self.zz_fdict['VMONALTAVDDFALL'] = self.VMONALTAVDDFALL
        self.VMONALTAVDDRISE = RM_Field_EMU_IF_VMONALTAVDDRISE(self)
        self.zz_fdict['VMONALTAVDDRISE'] = self.VMONALTAVDDRISE
        self.VMONDVDDFALL = RM_Field_EMU_IF_VMONDVDDFALL(self)
        self.zz_fdict['VMONDVDDFALL'] = self.VMONDVDDFALL
        self.VMONDVDDRISE = RM_Field_EMU_IF_VMONDVDDRISE(self)
        self.zz_fdict['VMONDVDDRISE'] = self.VMONDVDDRISE
        self.VMONIO0FALL = RM_Field_EMU_IF_VMONIO0FALL(self)
        self.zz_fdict['VMONIO0FALL'] = self.VMONIO0FALL
        self.VMONIO0RISE = RM_Field_EMU_IF_VMONIO0RISE(self)
        self.zz_fdict['VMONIO0RISE'] = self.VMONIO0RISE
        self.VMONFVDDFALL = RM_Field_EMU_IF_VMONFVDDFALL(self)
        self.zz_fdict['VMONFVDDFALL'] = self.VMONFVDDFALL
        self.VMONFVDDRISE = RM_Field_EMU_IF_VMONFVDDRISE(self)
        self.zz_fdict['VMONFVDDRISE'] = self.VMONFVDDRISE
        self.PFETOVERCURRENTLIMIT = RM_Field_EMU_IF_PFETOVERCURRENTLIMIT(self)
        self.zz_fdict['PFETOVERCURRENTLIMIT'] = self.PFETOVERCURRENTLIMIT
        self.NFETOVERCURRENTLIMIT = RM_Field_EMU_IF_NFETOVERCURRENTLIMIT(self)
        self.zz_fdict['NFETOVERCURRENTLIMIT'] = self.NFETOVERCURRENTLIMIT
        self.DCDCLPRUNNING = RM_Field_EMU_IF_DCDCLPRUNNING(self)
        self.zz_fdict['DCDCLPRUNNING'] = self.DCDCLPRUNNING
        self.DCDCLNRUNNING = RM_Field_EMU_IF_DCDCLNRUNNING(self)
        self.zz_fdict['DCDCLNRUNNING'] = self.DCDCLNRUNNING
        self.DCDCINBYPASS = RM_Field_EMU_IF_DCDCINBYPASS(self)
        self.zz_fdict['DCDCINBYPASS'] = self.DCDCINBYPASS
        self.EM23WAKEUP = RM_Field_EMU_IF_EM23WAKEUP(self)
        self.zz_fdict['EM23WAKEUP'] = self.EM23WAKEUP
        self.VSCALEDONE = RM_Field_EMU_IF_VSCALEDONE(self)
        self.zz_fdict['VSCALEDONE'] = self.VSCALEDONE
        self.TEMP = RM_Field_EMU_IF_TEMP(self)
        self.zz_fdict['TEMP'] = self.TEMP
        self.TEMPLOW = RM_Field_EMU_IF_TEMPLOW(self)
        self.zz_fdict['TEMPLOW'] = self.TEMPLOW
        self.TEMPHIGH = RM_Field_EMU_IF_TEMPHIGH(self)
        self.zz_fdict['TEMPHIGH'] = self.TEMPHIGH
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_IFS, self).__init__(rmio, label,
            0x400e3000, 0x028,
            'IFS', 'EMU.IFS', 'write-only',
            "",
            0x00000000, 0xE31FC0FF)

        self.VMONAVDDFALL = RM_Field_EMU_IFS_VMONAVDDFALL(self)
        self.zz_fdict['VMONAVDDFALL'] = self.VMONAVDDFALL
        self.VMONAVDDRISE = RM_Field_EMU_IFS_VMONAVDDRISE(self)
        self.zz_fdict['VMONAVDDRISE'] = self.VMONAVDDRISE
        self.VMONALTAVDDFALL = RM_Field_EMU_IFS_VMONALTAVDDFALL(self)
        self.zz_fdict['VMONALTAVDDFALL'] = self.VMONALTAVDDFALL
        self.VMONALTAVDDRISE = RM_Field_EMU_IFS_VMONALTAVDDRISE(self)
        self.zz_fdict['VMONALTAVDDRISE'] = self.VMONALTAVDDRISE
        self.VMONDVDDFALL = RM_Field_EMU_IFS_VMONDVDDFALL(self)
        self.zz_fdict['VMONDVDDFALL'] = self.VMONDVDDFALL
        self.VMONDVDDRISE = RM_Field_EMU_IFS_VMONDVDDRISE(self)
        self.zz_fdict['VMONDVDDRISE'] = self.VMONDVDDRISE
        self.VMONIO0FALL = RM_Field_EMU_IFS_VMONIO0FALL(self)
        self.zz_fdict['VMONIO0FALL'] = self.VMONIO0FALL
        self.VMONIO0RISE = RM_Field_EMU_IFS_VMONIO0RISE(self)
        self.zz_fdict['VMONIO0RISE'] = self.VMONIO0RISE
        self.VMONFVDDFALL = RM_Field_EMU_IFS_VMONFVDDFALL(self)
        self.zz_fdict['VMONFVDDFALL'] = self.VMONFVDDFALL
        self.VMONFVDDRISE = RM_Field_EMU_IFS_VMONFVDDRISE(self)
        self.zz_fdict['VMONFVDDRISE'] = self.VMONFVDDRISE
        self.PFETOVERCURRENTLIMIT = RM_Field_EMU_IFS_PFETOVERCURRENTLIMIT(self)
        self.zz_fdict['PFETOVERCURRENTLIMIT'] = self.PFETOVERCURRENTLIMIT
        self.NFETOVERCURRENTLIMIT = RM_Field_EMU_IFS_NFETOVERCURRENTLIMIT(self)
        self.zz_fdict['NFETOVERCURRENTLIMIT'] = self.NFETOVERCURRENTLIMIT
        self.DCDCLPRUNNING = RM_Field_EMU_IFS_DCDCLPRUNNING(self)
        self.zz_fdict['DCDCLPRUNNING'] = self.DCDCLPRUNNING
        self.DCDCLNRUNNING = RM_Field_EMU_IFS_DCDCLNRUNNING(self)
        self.zz_fdict['DCDCLNRUNNING'] = self.DCDCLNRUNNING
        self.DCDCINBYPASS = RM_Field_EMU_IFS_DCDCINBYPASS(self)
        self.zz_fdict['DCDCINBYPASS'] = self.DCDCINBYPASS
        self.EM23WAKEUP = RM_Field_EMU_IFS_EM23WAKEUP(self)
        self.zz_fdict['EM23WAKEUP'] = self.EM23WAKEUP
        self.VSCALEDONE = RM_Field_EMU_IFS_VSCALEDONE(self)
        self.zz_fdict['VSCALEDONE'] = self.VSCALEDONE
        self.TEMP = RM_Field_EMU_IFS_TEMP(self)
        self.zz_fdict['TEMP'] = self.TEMP
        self.TEMPLOW = RM_Field_EMU_IFS_TEMPLOW(self)
        self.zz_fdict['TEMPLOW'] = self.TEMPLOW
        self.TEMPHIGH = RM_Field_EMU_IFS_TEMPHIGH(self)
        self.zz_fdict['TEMPHIGH'] = self.TEMPHIGH
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_IFC, self).__init__(rmio, label,
            0x400e3000, 0x02C,
            'IFC', 'EMU.IFC', 'write-only',
            "",
            0x00000000, 0xE31FC0FF)

        self.VMONAVDDFALL = RM_Field_EMU_IFC_VMONAVDDFALL(self)
        self.zz_fdict['VMONAVDDFALL'] = self.VMONAVDDFALL
        self.VMONAVDDRISE = RM_Field_EMU_IFC_VMONAVDDRISE(self)
        self.zz_fdict['VMONAVDDRISE'] = self.VMONAVDDRISE
        self.VMONALTAVDDFALL = RM_Field_EMU_IFC_VMONALTAVDDFALL(self)
        self.zz_fdict['VMONALTAVDDFALL'] = self.VMONALTAVDDFALL
        self.VMONALTAVDDRISE = RM_Field_EMU_IFC_VMONALTAVDDRISE(self)
        self.zz_fdict['VMONALTAVDDRISE'] = self.VMONALTAVDDRISE
        self.VMONDVDDFALL = RM_Field_EMU_IFC_VMONDVDDFALL(self)
        self.zz_fdict['VMONDVDDFALL'] = self.VMONDVDDFALL
        self.VMONDVDDRISE = RM_Field_EMU_IFC_VMONDVDDRISE(self)
        self.zz_fdict['VMONDVDDRISE'] = self.VMONDVDDRISE
        self.VMONIO0FALL = RM_Field_EMU_IFC_VMONIO0FALL(self)
        self.zz_fdict['VMONIO0FALL'] = self.VMONIO0FALL
        self.VMONIO0RISE = RM_Field_EMU_IFC_VMONIO0RISE(self)
        self.zz_fdict['VMONIO0RISE'] = self.VMONIO0RISE
        self.VMONFVDDFALL = RM_Field_EMU_IFC_VMONFVDDFALL(self)
        self.zz_fdict['VMONFVDDFALL'] = self.VMONFVDDFALL
        self.VMONFVDDRISE = RM_Field_EMU_IFC_VMONFVDDRISE(self)
        self.zz_fdict['VMONFVDDRISE'] = self.VMONFVDDRISE
        self.PFETOVERCURRENTLIMIT = RM_Field_EMU_IFC_PFETOVERCURRENTLIMIT(self)
        self.zz_fdict['PFETOVERCURRENTLIMIT'] = self.PFETOVERCURRENTLIMIT
        self.NFETOVERCURRENTLIMIT = RM_Field_EMU_IFC_NFETOVERCURRENTLIMIT(self)
        self.zz_fdict['NFETOVERCURRENTLIMIT'] = self.NFETOVERCURRENTLIMIT
        self.DCDCLPRUNNING = RM_Field_EMU_IFC_DCDCLPRUNNING(self)
        self.zz_fdict['DCDCLPRUNNING'] = self.DCDCLPRUNNING
        self.DCDCLNRUNNING = RM_Field_EMU_IFC_DCDCLNRUNNING(self)
        self.zz_fdict['DCDCLNRUNNING'] = self.DCDCLNRUNNING
        self.DCDCINBYPASS = RM_Field_EMU_IFC_DCDCINBYPASS(self)
        self.zz_fdict['DCDCINBYPASS'] = self.DCDCINBYPASS
        self.EM23WAKEUP = RM_Field_EMU_IFC_EM23WAKEUP(self)
        self.zz_fdict['EM23WAKEUP'] = self.EM23WAKEUP
        self.VSCALEDONE = RM_Field_EMU_IFC_VSCALEDONE(self)
        self.zz_fdict['VSCALEDONE'] = self.VSCALEDONE
        self.TEMP = RM_Field_EMU_IFC_TEMP(self)
        self.zz_fdict['TEMP'] = self.TEMP
        self.TEMPLOW = RM_Field_EMU_IFC_TEMPLOW(self)
        self.zz_fdict['TEMPLOW'] = self.TEMPLOW
        self.TEMPHIGH = RM_Field_EMU_IFC_TEMPHIGH(self)
        self.zz_fdict['TEMPHIGH'] = self.TEMPHIGH
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_IEN, self).__init__(rmio, label,
            0x400e3000, 0x030,
            'IEN', 'EMU.IEN', 'read-write',
            "",
            0x00000000, 0xE31FC0FF)

        self.VMONAVDDFALL = RM_Field_EMU_IEN_VMONAVDDFALL(self)
        self.zz_fdict['VMONAVDDFALL'] = self.VMONAVDDFALL
        self.VMONAVDDRISE = RM_Field_EMU_IEN_VMONAVDDRISE(self)
        self.zz_fdict['VMONAVDDRISE'] = self.VMONAVDDRISE
        self.VMONALTAVDDFALL = RM_Field_EMU_IEN_VMONALTAVDDFALL(self)
        self.zz_fdict['VMONALTAVDDFALL'] = self.VMONALTAVDDFALL
        self.VMONALTAVDDRISE = RM_Field_EMU_IEN_VMONALTAVDDRISE(self)
        self.zz_fdict['VMONALTAVDDRISE'] = self.VMONALTAVDDRISE
        self.VMONDVDDFALL = RM_Field_EMU_IEN_VMONDVDDFALL(self)
        self.zz_fdict['VMONDVDDFALL'] = self.VMONDVDDFALL
        self.VMONDVDDRISE = RM_Field_EMU_IEN_VMONDVDDRISE(self)
        self.zz_fdict['VMONDVDDRISE'] = self.VMONDVDDRISE
        self.VMONIO0FALL = RM_Field_EMU_IEN_VMONIO0FALL(self)
        self.zz_fdict['VMONIO0FALL'] = self.VMONIO0FALL
        self.VMONIO0RISE = RM_Field_EMU_IEN_VMONIO0RISE(self)
        self.zz_fdict['VMONIO0RISE'] = self.VMONIO0RISE
        self.VMONFVDDFALL = RM_Field_EMU_IEN_VMONFVDDFALL(self)
        self.zz_fdict['VMONFVDDFALL'] = self.VMONFVDDFALL
        self.VMONFVDDRISE = RM_Field_EMU_IEN_VMONFVDDRISE(self)
        self.zz_fdict['VMONFVDDRISE'] = self.VMONFVDDRISE
        self.PFETOVERCURRENTLIMIT = RM_Field_EMU_IEN_PFETOVERCURRENTLIMIT(self)
        self.zz_fdict['PFETOVERCURRENTLIMIT'] = self.PFETOVERCURRENTLIMIT
        self.NFETOVERCURRENTLIMIT = RM_Field_EMU_IEN_NFETOVERCURRENTLIMIT(self)
        self.zz_fdict['NFETOVERCURRENTLIMIT'] = self.NFETOVERCURRENTLIMIT
        self.DCDCLPRUNNING = RM_Field_EMU_IEN_DCDCLPRUNNING(self)
        self.zz_fdict['DCDCLPRUNNING'] = self.DCDCLPRUNNING
        self.DCDCLNRUNNING = RM_Field_EMU_IEN_DCDCLNRUNNING(self)
        self.zz_fdict['DCDCLNRUNNING'] = self.DCDCLNRUNNING
        self.DCDCINBYPASS = RM_Field_EMU_IEN_DCDCINBYPASS(self)
        self.zz_fdict['DCDCINBYPASS'] = self.DCDCINBYPASS
        self.EM23WAKEUP = RM_Field_EMU_IEN_EM23WAKEUP(self)
        self.zz_fdict['EM23WAKEUP'] = self.EM23WAKEUP
        self.VSCALEDONE = RM_Field_EMU_IEN_VSCALEDONE(self)
        self.zz_fdict['VSCALEDONE'] = self.VSCALEDONE
        self.TEMP = RM_Field_EMU_IEN_TEMP(self)
        self.zz_fdict['TEMP'] = self.TEMP
        self.TEMPLOW = RM_Field_EMU_IEN_TEMPLOW(self)
        self.zz_fdict['TEMPLOW'] = self.TEMPLOW
        self.TEMPHIGH = RM_Field_EMU_IEN_TEMPHIGH(self)
        self.zz_fdict['TEMPHIGH'] = self.TEMPHIGH
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_PWRLOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_PWRLOCK, self).__init__(rmio, label,
            0x400e3000, 0x034,
            'PWRLOCK', 'EMU.PWRLOCK', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.LOCKKEY = RM_Field_EMU_PWRLOCK_LOCKKEY(self)
        self.zz_fdict['LOCKKEY'] = self.LOCKKEY
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_PWRCFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_PWRCFG, self).__init__(rmio, label,
            0x400e3000, 0x038,
            'PWRCFG', 'EMU.PWRCFG', 'read-write',
            "",
            0x00000000, 0x0000000F)

        self.PWRCFG = RM_Field_EMU_PWRCFG_PWRCFG(self)
        self.zz_fdict['PWRCFG'] = self.PWRCFG
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_PWRCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_PWRCTRL, self).__init__(rmio, label,
            0x400e3000, 0x03C,
            'PWRCTRL', 'EMU.PWRCTRL', 'read-write',
            "",
            0x00000000, 0x00001760)

        self.ANASW = RM_Field_EMU_PWRCTRL_ANASW(self)
        self.zz_fdict['ANASW'] = self.ANASW
        self.REGDIS = RM_Field_EMU_PWRCTRL_REGDIS(self)
        self.zz_fdict['REGDIS'] = self.REGDIS
        self.DCDCPWRSEL = RM_Field_EMU_PWRCTRL_DCDCPWRSEL(self)
        self.zz_fdict['DCDCPWRSEL'] = self.DCDCPWRSEL
        self.DCDCVREGSEL = RM_Field_EMU_PWRCTRL_DCDCVREGSEL(self)
        self.zz_fdict['DCDCVREGSEL'] = self.DCDCVREGSEL
        self.REGPWRSEL = RM_Field_EMU_PWRCTRL_REGPWRSEL(self)
        self.zz_fdict['REGPWRSEL'] = self.REGPWRSEL
        self.DVDDBODDIS = RM_Field_EMU_PWRCTRL_DVDDBODDIS(self)
        self.zz_fdict['DVDDBODDIS'] = self.DVDDBODDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCCTRL, self).__init__(rmio, label,
            0x400e3000, 0x040,
            'DCDCCTRL', 'EMU.DCDCCTRL', 'read-write',
            "",
            0x00000033, 0x000001F3)

        self.DCDCMODE = RM_Field_EMU_DCDCCTRL_DCDCMODE(self)
        self.zz_fdict['DCDCMODE'] = self.DCDCMODE
        self.DCDCMODEEM23 = RM_Field_EMU_DCDCCTRL_DCDCMODEEM23(self)
        self.zz_fdict['DCDCMODEEM23'] = self.DCDCMODEEM23
        self.DCDCMODEEM4 = RM_Field_EMU_DCDCCTRL_DCDCMODEEM4(self)
        self.zz_fdict['DCDCMODEEM4'] = self.DCDCMODEEM4
        self.LPSTANDBYDIS = RM_Field_EMU_DCDCCTRL_LPSTANDBYDIS(self)
        self.zz_fdict['LPSTANDBYDIS'] = self.LPSTANDBYDIS
        self.LNSTANDBY = RM_Field_EMU_DCDCCTRL_LNSTANDBY(self)
        self.zz_fdict['LNSTANDBY'] = self.LNSTANDBY
        self.LOWPOWERSKIP = RM_Field_EMU_DCDCCTRL_LOWPOWERSKIP(self)
        self.zz_fdict['LOWPOWERSKIP'] = self.LOWPOWERSKIP
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCSMCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCSMCTRL, self).__init__(rmio, label,
            0x400e3000, 0x044,
            'DCDCSMCTRL', 'EMU.DCDCSMCTRL', 'read-write',
            "",
            0x00000001, 0x00000001)

        self.LPCMPWAITDIS = RM_Field_EMU_DCDCSMCTRL_LPCMPWAITDIS(self)
        self.zz_fdict['LPCMPWAITDIS'] = self.LPCMPWAITDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCSWCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCSWCTRL, self).__init__(rmio, label,
            0x400e3000, 0x048,
            'DCDCSWCTRL', 'EMU.DCDCSWCTRL', 'read-write',
            "",
            0x00018A90, 0x0003BFFC)

        self.SWDAMPEN = RM_Field_EMU_DCDCSWCTRL_SWDAMPEN(self)
        self.zz_fdict['SWDAMPEN'] = self.SWDAMPEN
        self.SWNFETOFF = RM_Field_EMU_DCDCSWCTRL_SWNFETOFF(self)
        self.zz_fdict['SWNFETOFF'] = self.SWNFETOFF
        self.PWMDTIME = RM_Field_EMU_DCDCSWCTRL_PWMDTIME(self)
        self.zz_fdict['PWMDTIME'] = self.PWMDTIME
        self.PWMMIND = RM_Field_EMU_DCDCSWCTRL_PWMMIND(self)
        self.zz_fdict['PWMMIND'] = self.PWMMIND
        self.PWMMAXD = RM_Field_EMU_DCDCSWCTRL_PWMMAXD(self)
        self.zz_fdict['PWMMAXD'] = self.PWMMAXD
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCMISCCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCMISCCTRL, self).__init__(rmio, label,
            0x400e3000, 0x04C,
            'DCDCMISCCTRL', 'EMU.DCDCMISCCTRL', 'read-write',
            "",
            0x03107706, 0x377FFF3F)

        self.LNFORCECCM = RM_Field_EMU_DCDCMISCCTRL_LNFORCECCM(self)
        self.zz_fdict['LNFORCECCM'] = self.LNFORCECCM
        self.LPCMPHYSDIS = RM_Field_EMU_DCDCMISCCTRL_LPCMPHYSDIS(self)
        self.zz_fdict['LPCMPHYSDIS'] = self.LPCMPHYSDIS
        self.LPCMPHYSHI = RM_Field_EMU_DCDCMISCCTRL_LPCMPHYSHI(self)
        self.zz_fdict['LPCMPHYSHI'] = self.LPCMPHYSHI
        self.ZDETINTONLY = RM_Field_EMU_DCDCMISCCTRL_ZDETINTONLY(self)
        self.zz_fdict['ZDETINTONLY'] = self.ZDETINTONLY
        self.CLIMINTONLY = RM_Field_EMU_DCDCMISCCTRL_CLIMINTONLY(self)
        self.zz_fdict['CLIMINTONLY'] = self.CLIMINTONLY
        self.LNFORCECCMIMM = RM_Field_EMU_DCDCMISCCTRL_LNFORCECCMIMM(self)
        self.zz_fdict['LNFORCECCMIMM'] = self.LNFORCECCMIMM
        self.PFETCNT = RM_Field_EMU_DCDCMISCCTRL_PFETCNT(self)
        self.zz_fdict['PFETCNT'] = self.PFETCNT
        self.NFETCNT = RM_Field_EMU_DCDCMISCCTRL_NFETCNT(self)
        self.zz_fdict['NFETCNT'] = self.NFETCNT
        self.BYPLIMSEL = RM_Field_EMU_DCDCMISCCTRL_BYPLIMSEL(self)
        self.zz_fdict['BYPLIMSEL'] = self.BYPLIMSEL
        self.LPCLIMILIMSEL = RM_Field_EMU_DCDCMISCCTRL_LPCLIMILIMSEL(self)
        self.zz_fdict['LPCLIMILIMSEL'] = self.LPCLIMILIMSEL
        self.LNCLIMILIMSEL = RM_Field_EMU_DCDCMISCCTRL_LNCLIMILIMSEL(self)
        self.zz_fdict['LNCLIMILIMSEL'] = self.LNCLIMILIMSEL
        self.LPCMPBIASEM234H = RM_Field_EMU_DCDCMISCCTRL_LPCMPBIASEM234H(self)
        self.zz_fdict['LPCMPBIASEM234H'] = self.LPCMPBIASEM234H
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCZDETCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCZDETCTRL, self).__init__(rmio, label,
            0x400e3000, 0x050,
            'DCDCZDETCTRL', 'EMU.DCDCZDETCTRL', 'read-write',
            "",
            0x00000150, 0x00000371)

        self.ZDETDIS = RM_Field_EMU_DCDCZDETCTRL_ZDETDIS(self)
        self.zz_fdict['ZDETDIS'] = self.ZDETDIS
        self.ZDETILIMSEL = RM_Field_EMU_DCDCZDETCTRL_ZDETILIMSEL(self)
        self.zz_fdict['ZDETILIMSEL'] = self.ZDETILIMSEL
        self.ZDETBLANKDLY = RM_Field_EMU_DCDCZDETCTRL_ZDETBLANKDLY(self)
        self.zz_fdict['ZDETBLANKDLY'] = self.ZDETBLANKDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCCLIMCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCCLIMCTRL, self).__init__(rmio, label,
            0x400e3000, 0x054,
            'DCDCCLIMCTRL', 'EMU.DCDCCLIMCTRL', 'read-write',
            "",
            0x00000100, 0x00002301)

        self.CLIMDIS = RM_Field_EMU_DCDCCLIMCTRL_CLIMDIS(self)
        self.zz_fdict['CLIMDIS'] = self.CLIMDIS
        self.CLIMBLANKDLY = RM_Field_EMU_DCDCCLIMCTRL_CLIMBLANKDLY(self)
        self.zz_fdict['CLIMBLANKDLY'] = self.CLIMBLANKDLY
        self.BYPLIMEN = RM_Field_EMU_DCDCCLIMCTRL_BYPLIMEN(self)
        self.zz_fdict['BYPLIMEN'] = self.BYPLIMEN
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCLNCOMPCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCLNCOMPCTRL, self).__init__(rmio, label,
            0x400e3000, 0x058,
            'DCDCLNCOMPCTRL', 'EMU.DCDCLNCOMPCTRL', 'read-write',
            "",
            0x57204077, 0xF730F1F7)

        self.COMPENR1 = RM_Field_EMU_DCDCLNCOMPCTRL_COMPENR1(self)
        self.zz_fdict['COMPENR1'] = self.COMPENR1
        self.COMPENR2 = RM_Field_EMU_DCDCLNCOMPCTRL_COMPENR2(self)
        self.zz_fdict['COMPENR2'] = self.COMPENR2
        self.COMPENR3 = RM_Field_EMU_DCDCLNCOMPCTRL_COMPENR3(self)
        self.zz_fdict['COMPENR3'] = self.COMPENR3
        self.COMPENC1 = RM_Field_EMU_DCDCLNCOMPCTRL_COMPENC1(self)
        self.zz_fdict['COMPENC1'] = self.COMPENC1
        self.COMPENC2 = RM_Field_EMU_DCDCLNCOMPCTRL_COMPENC2(self)
        self.zz_fdict['COMPENC2'] = self.COMPENC2
        self.COMPENC3 = RM_Field_EMU_DCDCLNCOMPCTRL_COMPENC3(self)
        self.zz_fdict['COMPENC3'] = self.COMPENC3
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCLNVCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCLNVCTRL, self).__init__(rmio, label,
            0x400e3000, 0x05C,
            'DCDCLNVCTRL', 'EMU.DCDCLNVCTRL', 'read-write',
            "",
            0x00007100, 0x00007F02)

        self.LNATT = RM_Field_EMU_DCDCLNVCTRL_LNATT(self)
        self.zz_fdict['LNATT'] = self.LNATT
        self.LNVREF = RM_Field_EMU_DCDCLNVCTRL_LNVREF(self)
        self.zz_fdict['LNVREF'] = self.LNVREF
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCTIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCTIMING, self).__init__(rmio, label,
            0x400e3000, 0x060,
            'DCDCTIMING', 'EMU.DCDCTIMING', 'read-write',
            "",
            0x0770B92C, 0x7FF1FFFF)

        self.LPINITWAIT = RM_Field_EMU_DCDCTIMING_LPINITWAIT(self)
        self.zz_fdict['LPINITWAIT'] = self.LPINITWAIT
        self.LPCMPBLANKWAIT = RM_Field_EMU_DCDCTIMING_LPCMPBLANKWAIT(self)
        self.zz_fdict['LPCMPBLANKWAIT'] = self.LPCMPBLANKWAIT
        self.COMPENPRCHGEN = RM_Field_EMU_DCDCTIMING_COMPENPRCHGEN(self)
        self.zz_fdict['COMPENPRCHGEN'] = self.COMPENPRCHGEN
        self.LNWAIT = RM_Field_EMU_DCDCTIMING_LNWAIT(self)
        self.zz_fdict['LNWAIT'] = self.LNWAIT
        self.BYPWAIT = RM_Field_EMU_DCDCTIMING_BYPWAIT(self)
        self.zz_fdict['BYPWAIT'] = self.BYPWAIT
        self.PWMRETIME = RM_Field_EMU_DCDCTIMING_PWMRETIME(self)
        self.zz_fdict['PWMRETIME'] = self.PWMRETIME
        self.DUTYSCALE = RM_Field_EMU_DCDCTIMING_DUTYSCALE(self)
        self.zz_fdict['DUTYSCALE'] = self.DUTYSCALE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCLPVCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCLPVCTRL, self).__init__(rmio, label,
            0x400e3000, 0x064,
            'DCDCLPVCTRL', 'EMU.DCDCLPVCTRL', 'read-write',
            "",
            0x00000168, 0x000001FF)

        self.LPATT = RM_Field_EMU_DCDCLPVCTRL_LPATT(self)
        self.zz_fdict['LPATT'] = self.LPATT
        self.LPVREF = RM_Field_EMU_DCDCLPVCTRL_LPVREF(self)
        self.zz_fdict['LPVREF'] = self.LPVREF
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCLPFREQCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCLPFREQCTRL, self).__init__(rmio, label,
            0x400e3000, 0x068,
            'DCDCLPFREQCTRL', 'EMU.DCDCLPFREQCTRL', 'read-write',
            "",
            0x00000001, 0x00000003)

        self.LPOSCDIV = RM_Field_EMU_DCDCLPFREQCTRL_LPOSCDIV(self)
        self.zz_fdict['LPOSCDIV'] = self.LPOSCDIV
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCLPCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCLPCTRL, self).__init__(rmio, label,
            0x400e3000, 0x06C,
            'DCDCLPCTRL', 'EMU.DCDCLPCTRL', 'read-write',
            "",
            0x03000000, 0x0703F000)

        self.LPCMPHYSSELEM234H = RM_Field_EMU_DCDCLPCTRL_LPCMPHYSSELEM234H(self)
        self.zz_fdict['LPCMPHYSSELEM234H'] = self.LPCMPHYSSELEM234H
        self.LPPUMPDIS = RM_Field_EMU_DCDCLPCTRL_LPPUMPDIS(self)
        self.zz_fdict['LPPUMPDIS'] = self.LPPUMPDIS
        self.LPOSCLSSEL = RM_Field_EMU_DCDCLPCTRL_LPOSCLSSEL(self)
        self.zz_fdict['LPOSCLSSEL'] = self.LPOSCLSSEL
        self.LPVREFDUTYEN = RM_Field_EMU_DCDCLPCTRL_LPVREFDUTYEN(self)
        self.zz_fdict['LPVREFDUTYEN'] = self.LPVREFDUTYEN
        self.LPBLANK = RM_Field_EMU_DCDCLPCTRL_LPBLANK(self)
        self.zz_fdict['LPBLANK'] = self.LPBLANK
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCLNFREQCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCLNFREQCTRL, self).__init__(rmio, label,
            0x400e3000, 0x070,
            'DCDCLNFREQCTRL', 'EMU.DCDCLNFREQCTRL', 'read-write',
            "",
            0x10000000, 0x1F000007)

        self.RCOBAND = RM_Field_EMU_DCDCLNFREQCTRL_RCOBAND(self)
        self.zz_fdict['RCOBAND'] = self.RCOBAND
        self.RCOTRIM = RM_Field_EMU_DCDCLNFREQCTRL_RCOTRIM(self)
        self.zz_fdict['RCOTRIM'] = self.RCOTRIM
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCRCOSC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCRCOSC, self).__init__(rmio, label,
            0x400e3000, 0x074,
            'DCDCRCOSC', 'EMU.DCDCRCOSC', 'read-write',
            "",
            0x24020000, 0x37F30201)

        self.RCOSYNC = RM_Field_EMU_DCDCRCOSC_RCOSYNC(self)
        self.zz_fdict['RCOSYNC'] = self.RCOSYNC
        self.RCOHOPEN = RM_Field_EMU_DCDCRCOSC_RCOHOPEN(self)
        self.zz_fdict['RCOHOPEN'] = self.RCOHOPEN
        self.RCOHOPPERIOD = RM_Field_EMU_DCDCRCOSC_RCOHOPPERIOD(self)
        self.zz_fdict['RCOHOPPERIOD'] = self.RCOHOPPERIOD
        self.RCOHOP = RM_Field_EMU_DCDCRCOSC_RCOHOP(self)
        self.zz_fdict['RCOHOP'] = self.RCOHOP
        self.RCOSPREAD = RM_Field_EMU_DCDCRCOSC_RCOSPREAD(self)
        self.zz_fdict['RCOSPREAD'] = self.RCOSPREAD
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCSYNC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCSYNC, self).__init__(rmio, label,
            0x400e3000, 0x078,
            'DCDCSYNC', 'EMU.DCDCSYNC', 'read-only',
            "",
            0x00000000, 0x00000001)

        self.DCDCCTRLBUSY = RM_Field_EMU_DCDCSYNC_DCDCCTRLBUSY(self)
        self.zz_fdict['DCDCCTRLBUSY'] = self.DCDCCTRLBUSY
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCSTATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCSTATUS, self).__init__(rmio, label,
            0x400e3000, 0x07C,
            'DCDCSTATUS', 'EMU.DCDCSTATUS', 'read-only',
            "",
            0x00000000, 0x0003FFFF)

        self.RCOCALOUT = RM_Field_EMU_DCDCSTATUS_RCOCALOUT(self)
        self.zz_fdict['RCOCALOUT'] = self.RCOCALOUT
        self.LPCMPOUT = RM_Field_EMU_DCDCSTATUS_LPCMPOUT(self)
        self.zz_fdict['LPCMPOUT'] = self.LPCMPOUT
        self.LPTESTCLK = RM_Field_EMU_DCDCSTATUS_LPTESTCLK(self)
        self.zz_fdict['LPTESTCLK'] = self.LPTESTCLK
        self.LPTESTSTATE = RM_Field_EMU_DCDCSTATUS_LPTESTSTATE(self)
        self.zz_fdict['LPTESTSTATE'] = self.LPTESTSTATE
        self.DCDCSMSTATE = RM_Field_EMU_DCDCSTATUS_DCDCSMSTATE(self)
        self.zz_fdict['DCDCSMSTATE'] = self.DCDCSMSTATE
        self.PFETOVERCUR = RM_Field_EMU_DCDCSTATUS_PFETOVERCUR(self)
        self.zz_fdict['PFETOVERCUR'] = self.PFETOVERCUR
        self.NFETOVERCUR = RM_Field_EMU_DCDCSTATUS_NFETOVERCUR(self)
        self.zz_fdict['NFETOVERCUR'] = self.NFETOVERCUR
        self.LPTESTCMPRAW = RM_Field_EMU_DCDCSTATUS_LPTESTCMPRAW(self)
        self.zz_fdict['LPTESTCMPRAW'] = self.LPTESTCMPRAW
        self.LPRUNNING = RM_Field_EMU_DCDCSTATUS_LPRUNNING(self)
        self.zz_fdict['LPRUNNING'] = self.LPRUNNING
        self.LNRUNNING = RM_Field_EMU_DCDCSTATUS_LNRUNNING(self)
        self.zz_fdict['LNRUNNING'] = self.LNRUNNING
        self.INBYPASS = RM_Field_EMU_DCDCSTATUS_INBYPASS(self)
        self.zz_fdict['INBYPASS'] = self.INBYPASS
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCTRIM0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCTRIM0, self).__init__(rmio, label,
            0x400e3000, 0x080,
            'DCDCTRIM0', 'EMU.DCDCTRIM0', 'read-write',
            "",
            0x004A0220, 0x007FFFF3)

        self.PWMSKIP = RM_Field_EMU_DCDCTRIM0_PWMSKIP(self)
        self.zz_fdict['PWMSKIP'] = self.PWMSKIP
        self.RCORAMP = RM_Field_EMU_DCDCTRIM0_RCORAMP(self)
        self.zz_fdict['RCORAMP'] = self.RCORAMP
        self.CLIMVOSTRIM = RM_Field_EMU_DCDCTRIM0_CLIMVOSTRIM(self)
        self.zz_fdict['CLIMVOSTRIM'] = self.CLIMVOSTRIM
        self.ZDETVOSTRIM = RM_Field_EMU_DCDCTRIM0_ZDETVOSTRIM(self)
        self.zz_fdict['ZDETVOSTRIM'] = self.ZDETVOSTRIM
        self.LPOSCTRIM = RM_Field_EMU_DCDCTRIM0_LPOSCTRIM(self)
        self.zz_fdict['LPOSCTRIM'] = self.LPOSCTRIM
        self.CLIMBIASTRIM = RM_Field_EMU_DCDCTRIM0_CLIMBIASTRIM(self)
        self.zz_fdict['CLIMBIASTRIM'] = self.CLIMBIASTRIM
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCTRIM1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCTRIM1, self).__init__(rmio, label,
            0x400e3000, 0x084,
            'DCDCTRIM1', 'EMU.DCDCTRIM1', 'read-write',
            "",
            0x01770909, 0xC7FF1F0F)

        self.ZDETBIASTRIM = RM_Field_EMU_DCDCTRIM1_ZDETBIASTRIM(self)
        self.zz_fdict['ZDETBIASTRIM'] = self.ZDETBIASTRIM
        self.ZDET0XTRIM = RM_Field_EMU_DCDCTRIM1_ZDET0XTRIM(self)
        self.zz_fdict['ZDET0XTRIM'] = self.ZDET0XTRIM
        self.LPPFETCNT = RM_Field_EMU_DCDCTRIM1_LPPFETCNT(self)
        self.zz_fdict['LPPFETCNT'] = self.LPPFETCNT
        self.LPNFETCNT = RM_Field_EMU_DCDCTRIM1_LPNFETCNT(self)
        self.zz_fdict['LPNFETCNT'] = self.LPNFETCNT
        self.LPCLIMILIMSELRAMP = RM_Field_EMU_DCDCTRIM1_LPCLIMILIMSELRAMP(self)
        self.zz_fdict['LPCLIMILIMSELRAMP'] = self.LPCLIMILIMSELRAMP
        self.BYPPFETEN = RM_Field_EMU_DCDCTRIM1_BYPPFETEN(self)
        self.zz_fdict['BYPPFETEN'] = self.BYPPFETEN
        self.SWTRIMEN = RM_Field_EMU_DCDCTRIM1_SWTRIMEN(self)
        self.zz_fdict['SWTRIMEN'] = self.SWTRIMEN
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCTEST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCTEST, self).__init__(rmio, label,
            0x400e3000, 0x088,
            'DCDCTEST', 'EMU.DCDCTEST', 'read-write',
            "",
            0x00000080, 0x8001FFFF)

        self.LPINIT = RM_Field_EMU_DCDCTEST_LPINIT(self)
        self.zz_fdict['LPINIT'] = self.LPINIT
        self.LNPRECHARGE = RM_Field_EMU_DCDCTEST_LNPRECHARGE(self)
        self.zz_fdict['LNPRECHARGE'] = self.LNPRECHARGE
        self.PULSESEL = RM_Field_EMU_DCDCTEST_PULSESEL(self)
        self.zz_fdict['PULSESEL'] = self.PULSESEL
        self.BYPASSEN = RM_Field_EMU_DCDCTEST_BYPASSEN(self)
        self.zz_fdict['BYPASSEN'] = self.BYPASSEN
        self.LPEN = RM_Field_EMU_DCDCTEST_LPEN(self)
        self.zz_fdict['LPEN'] = self.LPEN
        self.LNEN = RM_Field_EMU_DCDCTEST_LNEN(self)
        self.zz_fdict['LNEN'] = self.LNEN
        self.LPCMPHYSDIS = RM_Field_EMU_DCDCTEST_LPCMPHYSDIS(self)
        self.zz_fdict['LPCMPHYSDIS'] = self.LPCMPHYSDIS
        self.ZDETILIMEN = RM_Field_EMU_DCDCTEST_ZDETILIMEN(self)
        self.zz_fdict['ZDETILIMEN'] = self.ZDETILIMEN
        self.LPPUMPDIS = RM_Field_EMU_DCDCTEST_LPPUMPDIS(self)
        self.zz_fdict['LPPUMPDIS'] = self.LPPUMPDIS
        self.SWTESTEN = RM_Field_EMU_DCDCTEST_SWTESTEN(self)
        self.zz_fdict['SWTESTEN'] = self.SWTESTEN
        self.LPTESTCMPBIAS = RM_Field_EMU_DCDCTEST_LPTESTCMPBIAS(self)
        self.zz_fdict['LPTESTCMPBIAS'] = self.LPTESTCMPBIAS
        self.SWTESTSTATE = RM_Field_EMU_DCDCTEST_SWTESTSTATE(self)
        self.zz_fdict['SWTESTSTATE'] = self.SWTESTSTATE
        self.LPTEST = RM_Field_EMU_DCDCTEST_LPTEST(self)
        self.zz_fdict['LPTEST'] = self.LPTEST
        self.LPTESTCMPSENSE = RM_Field_EMU_DCDCTEST_LPTESTCMPSENSE(self)
        self.zz_fdict['LPTESTCMPSENSE'] = self.LPTESTCMPSENSE
        self.CLIMTESTEN = RM_Field_EMU_DCDCTEST_CLIMTESTEN(self)
        self.zz_fdict['CLIMTESTEN'] = self.CLIMTESTEN
        self.LPPUMPHI = RM_Field_EMU_DCDCTEST_LPPUMPHI(self)
        self.zz_fdict['LPPUMPHI'] = self.LPPUMPHI
        self.RCOCALEN = RM_Field_EMU_DCDCTEST_RCOCALEN(self)
        self.zz_fdict['RCOCALEN'] = self.RCOCALEN
        self.TESTEN = RM_Field_EMU_DCDCTEST_TESTEN(self)
        self.zz_fdict['TESTEN'] = self.TESTEN
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_VMONCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_VMONCTRL, self).__init__(rmio, label,
            0x400e3000, 0x08C,
            'VMONCTRL', 'EMU.VMONCTRL', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.REFRESHRATE = RM_Field_EMU_VMONCTRL_REFRESHRATE(self)
        self.zz_fdict['REFRESHRATE'] = self.REFRESHRATE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_VMONAVDDCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_VMONAVDDCTRL, self).__init__(rmio, label,
            0x400e3000, 0x090,
            'VMONAVDDCTRL', 'EMU.VMONAVDDCTRL', 'read-write',
            "",
            0x00000000, 0x00FFFF0F)

        self.EN = RM_Field_EMU_VMONAVDDCTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.EM4ENTRY = RM_Field_EMU_VMONAVDDCTRL_EM4ENTRY(self)
        self.zz_fdict['EM4ENTRY'] = self.EM4ENTRY
        self.RISEWU = RM_Field_EMU_VMONAVDDCTRL_RISEWU(self)
        self.zz_fdict['RISEWU'] = self.RISEWU
        self.FALLWU = RM_Field_EMU_VMONAVDDCTRL_FALLWU(self)
        self.zz_fdict['FALLWU'] = self.FALLWU
        self.FALLTHRESFINE = RM_Field_EMU_VMONAVDDCTRL_FALLTHRESFINE(self)
        self.zz_fdict['FALLTHRESFINE'] = self.FALLTHRESFINE
        self.FALLTHRESCOARSE = RM_Field_EMU_VMONAVDDCTRL_FALLTHRESCOARSE(self)
        self.zz_fdict['FALLTHRESCOARSE'] = self.FALLTHRESCOARSE
        self.RISETHRESFINE = RM_Field_EMU_VMONAVDDCTRL_RISETHRESFINE(self)
        self.zz_fdict['RISETHRESFINE'] = self.RISETHRESFINE
        self.RISETHRESCOARSE = RM_Field_EMU_VMONAVDDCTRL_RISETHRESCOARSE(self)
        self.zz_fdict['RISETHRESCOARSE'] = self.RISETHRESCOARSE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_VMONALTAVDDCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_VMONALTAVDDCTRL, self).__init__(rmio, label,
            0x400e3000, 0x094,
            'VMONALTAVDDCTRL', 'EMU.VMONALTAVDDCTRL', 'read-write',
            "",
            0x00000000, 0x0000FF0D)

        self.EN = RM_Field_EMU_VMONALTAVDDCTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.RISEWU = RM_Field_EMU_VMONALTAVDDCTRL_RISEWU(self)
        self.zz_fdict['RISEWU'] = self.RISEWU
        self.FALLWU = RM_Field_EMU_VMONALTAVDDCTRL_FALLWU(self)
        self.zz_fdict['FALLWU'] = self.FALLWU
        self.THRESFINE = RM_Field_EMU_VMONALTAVDDCTRL_THRESFINE(self)
        self.zz_fdict['THRESFINE'] = self.THRESFINE
        self.THRESCOARSE = RM_Field_EMU_VMONALTAVDDCTRL_THRESCOARSE(self)
        self.zz_fdict['THRESCOARSE'] = self.THRESCOARSE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_VMONDVDDCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_VMONDVDDCTRL, self).__init__(rmio, label,
            0x400e3000, 0x098,
            'VMONDVDDCTRL', 'EMU.VMONDVDDCTRL', 'read-write',
            "",
            0x00000000, 0x0000FF0D)

        self.EN = RM_Field_EMU_VMONDVDDCTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.RISEWU = RM_Field_EMU_VMONDVDDCTRL_RISEWU(self)
        self.zz_fdict['RISEWU'] = self.RISEWU
        self.FALLWU = RM_Field_EMU_VMONDVDDCTRL_FALLWU(self)
        self.zz_fdict['FALLWU'] = self.FALLWU
        self.THRESFINE = RM_Field_EMU_VMONDVDDCTRL_THRESFINE(self)
        self.zz_fdict['THRESFINE'] = self.THRESFINE
        self.THRESCOARSE = RM_Field_EMU_VMONDVDDCTRL_THRESCOARSE(self)
        self.zz_fdict['THRESCOARSE'] = self.THRESCOARSE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_VMONIO0CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_VMONIO0CTRL, self).__init__(rmio, label,
            0x400e3000, 0x09C,
            'VMONIO0CTRL', 'EMU.VMONIO0CTRL', 'read-write',
            "",
            0x00000000, 0x0000FF1D)

        self.EN = RM_Field_EMU_VMONIO0CTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.RISEWU = RM_Field_EMU_VMONIO0CTRL_RISEWU(self)
        self.zz_fdict['RISEWU'] = self.RISEWU
        self.FALLWU = RM_Field_EMU_VMONIO0CTRL_FALLWU(self)
        self.zz_fdict['FALLWU'] = self.FALLWU
        self.RETDIS = RM_Field_EMU_VMONIO0CTRL_RETDIS(self)
        self.zz_fdict['RETDIS'] = self.RETDIS
        self.THRESFINE = RM_Field_EMU_VMONIO0CTRL_THRESFINE(self)
        self.zz_fdict['THRESFINE'] = self.THRESFINE
        self.THRESCOARSE = RM_Field_EMU_VMONIO0CTRL_THRESCOARSE(self)
        self.zz_fdict['THRESCOARSE'] = self.THRESCOARSE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_VMONFVDDCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_VMONFVDDCTRL, self).__init__(rmio, label,
            0x400e3000, 0x0AC,
            'VMONFVDDCTRL', 'EMU.VMONFVDDCTRL', 'read-write',
            "",
            0x00000000, 0x0000FF0D)

        self.EN = RM_Field_EMU_VMONFVDDCTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.RISEWU = RM_Field_EMU_VMONFVDDCTRL_RISEWU(self)
        self.zz_fdict['RISEWU'] = self.RISEWU
        self.FALLWU = RM_Field_EMU_VMONFVDDCTRL_FALLWU(self)
        self.zz_fdict['FALLWU'] = self.FALLWU
        self.THRESFINE = RM_Field_EMU_VMONFVDDCTRL_THRESFINE(self)
        self.zz_fdict['THRESFINE'] = self.THRESFINE
        self.THRESCOARSE = RM_Field_EMU_VMONFVDDCTRL_THRESCOARSE(self)
        self.zz_fdict['THRESCOARSE'] = self.THRESCOARSE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_SGLNAMIXCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_SGLNAMIXCTRL, self).__init__(rmio, label,
            0x400e3000, 0x0B0,
            'SGLNAMIXCTRL', 'EMU.SGLNAMIXCTRL', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.SGLNAMIXSTANDBY = RM_Field_EMU_SGLNAMIXCTRL_SGLNAMIXSTANDBY(self)
        self.zz_fdict['SGLNAMIXSTANDBY'] = self.SGLNAMIXSTANDBY
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_RAM1CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_RAM1CTRL, self).__init__(rmio, label,
            0x400e3000, 0x0B4,
            'RAM1CTRL', 'EMU.RAM1CTRL', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.RAMPOWERDOWN = RM_Field_EMU_RAM1CTRL_RAMPOWERDOWN(self)
        self.zz_fdict['RAMPOWERDOWN'] = self.RAMPOWERDOWN
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_RAM2CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_RAM2CTRL, self).__init__(rmio, label,
            0x400e3000, 0x0B8,
            'RAM2CTRL', 'EMU.RAM2CTRL', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.RAMPOWERDOWN = RM_Field_EMU_RAM2CTRL_RAMPOWERDOWN(self)
        self.zz_fdict['RAMPOWERDOWN'] = self.RAMPOWERDOWN
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_STATEDLY2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_STATEDLY2, self).__init__(rmio, label,
            0x400e3000, 0x0E8,
            'STATEDLY2', 'EMU.STATEDLY2', 'read-write',
            "",
            0x3C80C80A, 0x3FFFFF3F)

        self.EM23BODDREGWAIT = RM_Field_EMU_STATEDLY2_EM23BODDREGWAIT(self)
        self.zz_fdict['EM23BODDREGWAIT'] = self.EM23BODDREGWAIT
        self.EM234BODWAIT = RM_Field_EMU_STATEDLY2_EM234BODWAIT(self)
        self.zz_fdict['EM234BODWAIT'] = self.EM234BODWAIT
        self.EM4HWUFLASHVREFWAIT = RM_Field_EMU_STATEDLY2_EM4HWUFLASHVREFWAIT(self)
        self.zz_fdict['EM4HWUFLASHVREFWAIT'] = self.EM4HWUFLASHVREFWAIT
        self.EM4HLDREGREFWAIT = RM_Field_EMU_STATEDLY2_EM4HLDREGREFWAIT(self)
        self.zz_fdict['EM4HLDREGREFWAIT'] = self.EM4HLDREGREFWAIT
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCLPEM01CFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCLPEM01CFG, self).__init__(rmio, label,
            0x400e3000, 0x0EC,
            'DCDCLPEM01CFG', 'EMU.DCDCLPEM01CFG', 'read-write',
            "",
            0x00000300, 0x0000F300)

        self.LPCMPBIASEM01 = RM_Field_EMU_DCDCLPEM01CFG_LPCMPBIASEM01(self)
        self.zz_fdict['LPCMPBIASEM01'] = self.LPCMPBIASEM01
        self.LPCMPHYSSELEM01 = RM_Field_EMU_DCDCLPEM01CFG_LPCMPHYSSELEM01(self)
        self.zz_fdict['LPCMPHYSSELEM01'] = self.LPCMPHYSSELEM01
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCPRSSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCPRSSEL, self).__init__(rmio, label,
            0x400e3000, 0x0FC,
            'DCDCPRSSEL', 'EMU.DCDCPRSSEL', 'read-write',
            "",
            0x00000000, 0x0000010F)

        self.DCDCPRSSEL = RM_Field_EMU_DCDCPRSSEL_DCDCPRSSEL(self)
        self.zz_fdict['DCDCPRSSEL'] = self.DCDCPRSSEL
        self.PRSNOISEDISEN = RM_Field_EMU_DCDCPRSSEL_PRSNOISEDISEN(self)
        self.zz_fdict['PRSNOISEDISEN'] = self.PRSNOISEDISEN
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_EM23PERNORETAINCMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_EM23PERNORETAINCMD, self).__init__(rmio, label,
            0x400e3000, 0x100,
            'EM23PERNORETAINCMD', 'EMU.EM23PERNORETAINCMD', 'write-only',
            "",
            0x00000000, 0x0000FFFF)

        self.ACMP0UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_ACMP0UNLOCK(self)
        self.zz_fdict['ACMP0UNLOCK'] = self.ACMP0UNLOCK
        self.ACMP1UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_ACMP1UNLOCK(self)
        self.zz_fdict['ACMP1UNLOCK'] = self.ACMP1UNLOCK
        self.PCNT0UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_PCNT0UNLOCK(self)
        self.zz_fdict['PCNT0UNLOCK'] = self.PCNT0UNLOCK
        self.PCNT1UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_PCNT1UNLOCK(self)
        self.zz_fdict['PCNT1UNLOCK'] = self.PCNT1UNLOCK
        self.PCNT2UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_PCNT2UNLOCK(self)
        self.zz_fdict['PCNT2UNLOCK'] = self.PCNT2UNLOCK
        self.I2C0UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_I2C0UNLOCK(self)
        self.zz_fdict['I2C0UNLOCK'] = self.I2C0UNLOCK
        self.I2C1UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_I2C1UNLOCK(self)
        self.zz_fdict['I2C1UNLOCK'] = self.I2C1UNLOCK
        self.DAC0UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_DAC0UNLOCK(self)
        self.zz_fdict['DAC0UNLOCK'] = self.DAC0UNLOCK
        self.IDAC0UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_IDAC0UNLOCK(self)
        self.zz_fdict['IDAC0UNLOCK'] = self.IDAC0UNLOCK
        self.ADC0UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_ADC0UNLOCK(self)
        self.zz_fdict['ADC0UNLOCK'] = self.ADC0UNLOCK
        self.LETIMER0UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_LETIMER0UNLOCK(self)
        self.zz_fdict['LETIMER0UNLOCK'] = self.LETIMER0UNLOCK
        self.WDOG0UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_WDOG0UNLOCK(self)
        self.zz_fdict['WDOG0UNLOCK'] = self.WDOG0UNLOCK
        self.WDOG1UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_WDOG1UNLOCK(self)
        self.zz_fdict['WDOG1UNLOCK'] = self.WDOG1UNLOCK
        self.LESENSE0UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_LESENSE0UNLOCK(self)
        self.zz_fdict['LESENSE0UNLOCK'] = self.LESENSE0UNLOCK
        self.CSENUNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_CSENUNLOCK(self)
        self.zz_fdict['CSENUNLOCK'] = self.CSENUNLOCK
        self.LEUART0UNLOCK = RM_Field_EMU_EM23PERNORETAINCMD_LEUART0UNLOCK(self)
        self.zz_fdict['LEUART0UNLOCK'] = self.LEUART0UNLOCK
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_EM23PERNORETAINSTATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_EM23PERNORETAINSTATUS, self).__init__(rmio, label,
            0x400e3000, 0x104,
            'EM23PERNORETAINSTATUS', 'EMU.EM23PERNORETAINSTATUS', 'read-only',
            "",
            0x00000000, 0x0000FFFF)

        self.ACMP0LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_ACMP0LOCKED(self)
        self.zz_fdict['ACMP0LOCKED'] = self.ACMP0LOCKED
        self.ACMP1LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_ACMP1LOCKED(self)
        self.zz_fdict['ACMP1LOCKED'] = self.ACMP1LOCKED
        self.PCNT0LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_PCNT0LOCKED(self)
        self.zz_fdict['PCNT0LOCKED'] = self.PCNT0LOCKED
        self.PCNT1LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_PCNT1LOCKED(self)
        self.zz_fdict['PCNT1LOCKED'] = self.PCNT1LOCKED
        self.PCNT2LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_PCNT2LOCKED(self)
        self.zz_fdict['PCNT2LOCKED'] = self.PCNT2LOCKED
        self.I2C0LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_I2C0LOCKED(self)
        self.zz_fdict['I2C0LOCKED'] = self.I2C0LOCKED
        self.I2C1LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_I2C1LOCKED(self)
        self.zz_fdict['I2C1LOCKED'] = self.I2C1LOCKED
        self.DAC0LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_DAC0LOCKED(self)
        self.zz_fdict['DAC0LOCKED'] = self.DAC0LOCKED
        self.IDAC0LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_IDAC0LOCKED(self)
        self.zz_fdict['IDAC0LOCKED'] = self.IDAC0LOCKED
        self.ADC0LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_ADC0LOCKED(self)
        self.zz_fdict['ADC0LOCKED'] = self.ADC0LOCKED
        self.LETIMER0LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_LETIMER0LOCKED(self)
        self.zz_fdict['LETIMER0LOCKED'] = self.LETIMER0LOCKED
        self.WDOG0LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_WDOG0LOCKED(self)
        self.zz_fdict['WDOG0LOCKED'] = self.WDOG0LOCKED
        self.WDOG1LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_WDOG1LOCKED(self)
        self.zz_fdict['WDOG1LOCKED'] = self.WDOG1LOCKED
        self.LESENSE0LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_LESENSE0LOCKED(self)
        self.zz_fdict['LESENSE0LOCKED'] = self.LESENSE0LOCKED
        self.CSENLOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_CSENLOCKED(self)
        self.zz_fdict['CSENLOCKED'] = self.CSENLOCKED
        self.LEUART0LOCKED = RM_Field_EMU_EM23PERNORETAINSTATUS_LEUART0LOCKED(self)
        self.zz_fdict['LEUART0LOCKED'] = self.LEUART0LOCKED
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_EM23PERNORETAINCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_EM23PERNORETAINCTRL, self).__init__(rmio, label,
            0x400e3000, 0x108,
            'EM23PERNORETAINCTRL', 'EMU.EM23PERNORETAINCTRL', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.ACMP0DIS = RM_Field_EMU_EM23PERNORETAINCTRL_ACMP0DIS(self)
        self.zz_fdict['ACMP0DIS'] = self.ACMP0DIS
        self.ACMP1DIS = RM_Field_EMU_EM23PERNORETAINCTRL_ACMP1DIS(self)
        self.zz_fdict['ACMP1DIS'] = self.ACMP1DIS
        self.PCNT0DIS = RM_Field_EMU_EM23PERNORETAINCTRL_PCNT0DIS(self)
        self.zz_fdict['PCNT0DIS'] = self.PCNT0DIS
        self.PCNT1DIS = RM_Field_EMU_EM23PERNORETAINCTRL_PCNT1DIS(self)
        self.zz_fdict['PCNT1DIS'] = self.PCNT1DIS
        self.PCNT2DIS = RM_Field_EMU_EM23PERNORETAINCTRL_PCNT2DIS(self)
        self.zz_fdict['PCNT2DIS'] = self.PCNT2DIS
        self.I2C0DIS = RM_Field_EMU_EM23PERNORETAINCTRL_I2C0DIS(self)
        self.zz_fdict['I2C0DIS'] = self.I2C0DIS
        self.I2C1DIS = RM_Field_EMU_EM23PERNORETAINCTRL_I2C1DIS(self)
        self.zz_fdict['I2C1DIS'] = self.I2C1DIS
        self.DAC0DIS = RM_Field_EMU_EM23PERNORETAINCTRL_DAC0DIS(self)
        self.zz_fdict['DAC0DIS'] = self.DAC0DIS
        self.IDAC0DIS = RM_Field_EMU_EM23PERNORETAINCTRL_IDAC0DIS(self)
        self.zz_fdict['IDAC0DIS'] = self.IDAC0DIS
        self.ADC0DIS = RM_Field_EMU_EM23PERNORETAINCTRL_ADC0DIS(self)
        self.zz_fdict['ADC0DIS'] = self.ADC0DIS
        self.LETIMER0DIS = RM_Field_EMU_EM23PERNORETAINCTRL_LETIMER0DIS(self)
        self.zz_fdict['LETIMER0DIS'] = self.LETIMER0DIS
        self.WDOG0DIS = RM_Field_EMU_EM23PERNORETAINCTRL_WDOG0DIS(self)
        self.zz_fdict['WDOG0DIS'] = self.WDOG0DIS
        self.WDOG1DIS = RM_Field_EMU_EM23PERNORETAINCTRL_WDOG1DIS(self)
        self.zz_fdict['WDOG1DIS'] = self.WDOG1DIS
        self.LESENSE0DIS = RM_Field_EMU_EM23PERNORETAINCTRL_LESENSE0DIS(self)
        self.zz_fdict['LESENSE0DIS'] = self.LESENSE0DIS
        self.CSENDIS = RM_Field_EMU_EM23PERNORETAINCTRL_CSENDIS(self)
        self.zz_fdict['CSENDIS'] = self.CSENDIS
        self.LEUART0DIS = RM_Field_EMU_EM23PERNORETAINCTRL_LEUART0DIS(self)
        self.zz_fdict['LEUART0DIS'] = self.LEUART0DIS
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_AUXCTRL0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_AUXCTRL0, self).__init__(rmio, label,
            0x400e3000, 0x140,
            'AUXCTRL0', 'EMU.AUXCTRL0', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.AUX0 = RM_Field_EMU_AUXCTRL0_AUX0(self)
        self.zz_fdict['AUX0'] = self.AUX0
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_AUXCTRL1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_AUXCTRL1, self).__init__(rmio, label,
            0x400e3000, 0x144,
            'AUXCTRL1', 'EMU.AUXCTRL1', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.AUX1 = RM_Field_EMU_AUXCTRL1_AUX1(self)
        self.zz_fdict['AUX1'] = self.AUX1
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_AUXCTRL2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_AUXCTRL2, self).__init__(rmio, label,
            0x400e3000, 0x148,
            'AUXCTRL2', 'EMU.AUXCTRL2', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.AUX2 = RM_Field_EMU_AUXCTRL2_AUX2(self)
        self.zz_fdict['AUX2'] = self.AUX2
        self.AUX3 = RM_Field_EMU_AUXCTRL2_AUX3(self)
        self.zz_fdict['AUX3'] = self.AUX3
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_PORBOD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_PORBOD, self).__init__(rmio, label,
            0x400e3000, 0x14C,
            'PORBOD', 'EMU.PORBOD', 'read-write',
            "",
            0xC90842CC, 0xFFFFFFFF)

        self.PORBOD_REFTRIM = RM_Field_EMU_PORBOD_PORBOD_REFTRIM(self)
        self.zz_fdict['PORBOD_REFTRIM'] = self.PORBOD_REFTRIM
        self.PORBOD_FORCE_MIRROR_FOR_VREF = RM_Field_EMU_PORBOD_PORBOD_FORCE_MIRROR_FOR_VREF(self)
        self.zz_fdict['PORBOD_FORCE_MIRROR_FOR_VREF'] = self.PORBOD_FORCE_MIRROR_FOR_VREF
        self.PORBOD_AVDD_BOD_THR = RM_Field_EMU_PORBOD_PORBOD_AVDD_BOD_THR(self)
        self.zz_fdict['PORBOD_AVDD_BOD_THR'] = self.PORBOD_AVDD_BOD_THR
        self.PORBOD_DVDD_BOD_THR = RM_Field_EMU_PORBOD_PORBOD_DVDD_BOD_THR(self)
        self.zz_fdict['PORBOD_DVDD_BOD_THR'] = self.PORBOD_DVDD_BOD_THR
        self.BIAS_TEMP_TRIM_LP = RM_Field_EMU_PORBOD_BIAS_TEMP_TRIM_LP(self)
        self.zz_fdict['BIAS_TEMP_TRIM_LP'] = self.BIAS_TEMP_TRIM_LP
        self.BIAS_ABS_TRIM_LP = RM_Field_EMU_PORBOD_BIAS_ABS_TRIM_LP(self)
        self.zz_fdict['BIAS_ABS_TRIM_LP'] = self.BIAS_ABS_TRIM_LP
        self.BIAS_ILTC_UA_TRIM = RM_Field_EMU_PORBOD_BIAS_ILTC_UA_TRIM(self)
        self.zz_fdict['BIAS_ILTC_UA_TRIM'] = self.BIAS_ILTC_UA_TRIM
        self.BIAS_ILTC_NA_TRIM = RM_Field_EMU_PORBOD_BIAS_ILTC_NA_TRIM(self)
        self.zz_fdict['BIAS_ILTC_NA_TRIM'] = self.BIAS_ILTC_NA_TRIM
        self.GMC_CALIB_DISABLE = RM_Field_EMU_PORBOD_GMC_CALIB_DISABLE(self)
        self.zz_fdict['GMC_CALIB_DISABLE'] = self.GMC_CALIB_DISABLE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_PORBODREFRESH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_PORBODREFRESH, self).__init__(rmio, label,
            0x400e3000, 0x150,
            'PORBODREFRESH', 'EMU.PORBODREFRESH', 'read-write',
            "",
            0x00000000, 0x0000000F)

        self.PORBOD_DUTY_CYCLE_OFF = RM_Field_EMU_PORBODREFRESH_PORBOD_DUTY_CYCLE_OFF(self)
        self.zz_fdict['PORBOD_DUTY_CYCLE_OFF'] = self.PORBOD_DUTY_CYCLE_OFF
        self.PORBOD_FORCE_REFRESH = RM_Field_EMU_PORBODREFRESH_PORBOD_FORCE_REFRESH(self)
        self.zz_fdict['PORBOD_FORCE_REFRESH'] = self.PORBOD_FORCE_REFRESH
        self.PORBOD_REFRESHRATE = RM_Field_EMU_PORBODREFRESH_PORBOD_REFRESHRATE(self)
        self.zz_fdict['PORBOD_REFRESHRATE'] = self.PORBOD_REFRESHRATE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_PORBODOVERRIDE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_PORBODOVERRIDE, self).__init__(rmio, label,
            0x400e3000, 0x154,
            'PORBODOVERRIDE', 'EMU.PORBODOVERRIDE', 'read-write',
            "",
            0x00000000, 0xFFC00000)

        self.PORBOD_OVERRIDE_EN = RM_Field_EMU_PORBODOVERRIDE_PORBOD_OVERRIDE_EN(self)
        self.zz_fdict['PORBOD_OVERRIDE_EN'] = self.PORBOD_OVERRIDE_EN
        self.OVR_PORBOD_BOD_BOOST = RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_BOD_BOOST(self)
        self.zz_fdict['OVR_PORBOD_BOD_BOOST'] = self.OVR_PORBOD_BOD_BOOST
        self.OVR_PORBOD_LEGACY_POR_SAFE_DISABLE = RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_LEGACY_POR_SAFE_DISABLE(self)
        self.zz_fdict['OVR_PORBOD_LEGACY_POR_SAFE_DISABLE'] = self.OVR_PORBOD_LEGACY_POR_SAFE_DISABLE
        self.OVR_PORBOD_AVDD_BOD_EN = RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_AVDD_BOD_EN(self)
        self.zz_fdict['OVR_PORBOD_AVDD_BOD_EN'] = self.OVR_PORBOD_AVDD_BOD_EN
        self.OVR_PORBOD_AVDD_EM4BOD_EN = RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_AVDD_EM4BOD_EN(self)
        self.zz_fdict['OVR_PORBOD_AVDD_EM4BOD_EN'] = self.OVR_PORBOD_AVDD_EM4BOD_EN
        self.OVR_PORBOD_DVDD_BOD_EN = RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_DVDD_BOD_EN(self)
        self.zz_fdict['OVR_PORBOD_DVDD_BOD_EN'] = self.OVR_PORBOD_DVDD_BOD_EN
        self.OVR_PORBOD_FLASH_BOD_EN = RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_FLASH_BOD_EN(self)
        self.zz_fdict['OVR_PORBOD_FLASH_BOD_EN'] = self.OVR_PORBOD_FLASH_BOD_EN
        self.OVR_PORBOD_DEC0_BOD_EN = RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_DEC0_BOD_EN(self)
        self.zz_fdict['OVR_PORBOD_DEC0_BOD_EN'] = self.OVR_PORBOD_DEC0_BOD_EN
        self.OVR_PORBOD_DEC1_BOD_EN = RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_DEC1_BOD_EN(self)
        self.zz_fdict['OVR_PORBOD_DEC1_BOD_EN'] = self.OVR_PORBOD_DEC1_BOD_EN
        self.OVR_PORBOD_BOD_BIAS_ENABLE = RM_Field_EMU_PORBODOVERRIDE_OVR_PORBOD_BOD_BIAS_ENABLE(self)
        self.zz_fdict['OVR_PORBOD_BOD_BIAS_ENABLE'] = self.OVR_PORBOD_BOD_BIAS_ENABLE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_BODCONF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_BODCONF, self).__init__(rmio, label,
            0x400e3000, 0x158,
            'BODCONF', 'EMU.BODCONF', 'read-write',
            "",
            0x00800000, 0xEF9E07FC)

        self.PORBOD_AVDD_EM4BOD_TRIM = RM_Field_EMU_BODCONF_PORBOD_AVDD_EM4BOD_TRIM(self)
        self.zz_fdict['PORBOD_AVDD_EM4BOD_TRIM'] = self.PORBOD_AVDD_EM4BOD_TRIM
        self.PORBOD_AVDD_GL_CURR = RM_Field_EMU_BODCONF_PORBOD_AVDD_GL_CURR(self)
        self.zz_fdict['PORBOD_AVDD_GL_CURR'] = self.PORBOD_AVDD_GL_CURR
        self.PORBOD_AVDD_GL_RC = RM_Field_EMU_BODCONF_PORBOD_AVDD_GL_RC(self)
        self.zz_fdict['PORBOD_AVDD_GL_RC'] = self.PORBOD_AVDD_GL_RC
        self.PORBOD_DVDD_GL_CURR = RM_Field_EMU_BODCONF_PORBOD_DVDD_GL_CURR(self)
        self.zz_fdict['PORBOD_DVDD_GL_CURR'] = self.PORBOD_DVDD_GL_CURR
        self.PORBOD_DVDD_GL_RC = RM_Field_EMU_BODCONF_PORBOD_DVDD_GL_RC(self)
        self.zz_fdict['PORBOD_DVDD_GL_RC'] = self.PORBOD_DVDD_GL_RC
        self.EMUOSCDIV2EN = RM_Field_EMU_BODCONF_EMUOSCDIV2EN(self)
        self.zz_fdict['EMUOSCDIV2EN'] = self.EMUOSCDIV2EN
        self.EMUOSC_TRIM = RM_Field_EMU_BODCONF_EMUOSC_TRIM(self)
        self.zz_fdict['EMUOSC_TRIM'] = self.EMUOSC_TRIM
        self.EMUOSC_RTRIM = RM_Field_EMU_BODCONF_EMUOSC_RTRIM(self)
        self.zz_fdict['EMUOSC_RTRIM'] = self.EMUOSC_RTRIM
        self.PORBOD_AVDD_EM4BOD_DIS = RM_Field_EMU_BODCONF_PORBOD_AVDD_EM4BOD_DIS(self)
        self.zz_fdict['PORBOD_AVDD_EM4BOD_DIS'] = self.PORBOD_AVDD_EM4BOD_DIS
        self.EM23BODBOOST = RM_Field_EMU_BODCONF_EM23BODBOOST(self)
        self.zz_fdict['EM23BODBOOST'] = self.EM23BODBOOST
        self.BODBOOSTDIS = RM_Field_EMU_BODCONF_BODBOOSTDIS(self)
        self.zz_fdict['BODBOOSTDIS'] = self.BODBOOSTDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_FLASHBOD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_FLASHBOD, self).__init__(rmio, label,
            0x400e3000, 0x15C,
            'FLASHBOD', 'EMU.FLASHBOD', 'read-write',
            "",
            0x00000380, 0x000F07C0)

        self.PORBOD_FLASH_BOD_THR = RM_Field_EMU_FLASHBOD_PORBOD_FLASH_BOD_THR(self)
        self.zz_fdict['PORBOD_FLASH_BOD_THR'] = self.PORBOD_FLASH_BOD_THR
        self.PORBOD_FLASH_GL_CURR = RM_Field_EMU_FLASHBOD_PORBOD_FLASH_GL_CURR(self)
        self.zz_fdict['PORBOD_FLASH_GL_CURR'] = self.PORBOD_FLASH_GL_CURR
        self.PORBOD_FLASH_GL_RC = RM_Field_EMU_FLASHBOD_PORBOD_FLASH_GL_RC(self)
        self.zz_fdict['PORBOD_FLASH_GL_RC'] = self.PORBOD_FLASH_GL_RC
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DECBOD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DECBOD, self).__init__(rmio, label,
            0x400e3000, 0x160,
            'DECBOD', 'EMU.DECBOD', 'read-write',
            "",
            0x00240024, 0x07BF07BF)

        self.PORBOD_DEC0_BOD_TRIM = RM_Field_EMU_DECBOD_PORBOD_DEC0_BOD_TRIM(self)
        self.zz_fdict['PORBOD_DEC0_BOD_TRIM'] = self.PORBOD_DEC0_BOD_TRIM
        self.PORBOD_DEC0_BOD_THR = RM_Field_EMU_DECBOD_PORBOD_DEC0_BOD_THR(self)
        self.zz_fdict['PORBOD_DEC0_BOD_THR'] = self.PORBOD_DEC0_BOD_THR
        self.PORBOD_DEC0_GL_CURR = RM_Field_EMU_DECBOD_PORBOD_DEC0_GL_CURR(self)
        self.zz_fdict['PORBOD_DEC0_GL_CURR'] = self.PORBOD_DEC0_GL_CURR
        self.PORBOD_DEC0_GL_RC = RM_Field_EMU_DECBOD_PORBOD_DEC0_GL_RC(self)
        self.zz_fdict['PORBOD_DEC0_GL_RC'] = self.PORBOD_DEC0_GL_RC
        self.PORBOD_DEC1_BOD_TRIM = RM_Field_EMU_DECBOD_PORBOD_DEC1_BOD_TRIM(self)
        self.zz_fdict['PORBOD_DEC1_BOD_TRIM'] = self.PORBOD_DEC1_BOD_TRIM
        self.PORBOD_DEC1_BOD_THR = RM_Field_EMU_DECBOD_PORBOD_DEC1_BOD_THR(self)
        self.zz_fdict['PORBOD_DEC1_BOD_THR'] = self.PORBOD_DEC1_BOD_THR
        self.PORBOD_DEC1_GL_CURR = RM_Field_EMU_DECBOD_PORBOD_DEC1_GL_CURR(self)
        self.zz_fdict['PORBOD_DEC1_GL_CURR'] = self.PORBOD_DEC1_GL_CURR
        self.PORBOD_DEC1_GL_RC = RM_Field_EMU_DECBOD_PORBOD_DEC1_GL_RC(self)
        self.zz_fdict['PORBOD_DEC1_GL_RC'] = self.PORBOD_DEC1_GL_RC
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_BIASCONF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_BIASCONF, self).__init__(rmio, label,
            0x400e3000, 0x164,
            'BIASCONF', 'EMU.BIASCONF', 'read-write',
            "",
            0x000000F8, 0x0000F3FF)

        self.GMCEM01 = RM_Field_EMU_BIASCONF_GMCEM01(self)
        self.zz_fdict['GMCEM01'] = self.GMCEM01
        self.UADUTYEM01 = RM_Field_EMU_BIASCONF_UADUTYEM01(self)
        self.zz_fdict['UADUTYEM01'] = self.UADUTYEM01
        self.NADUTYEM01 = RM_Field_EMU_BIASCONF_NADUTYEM01(self)
        self.zz_fdict['NADUTYEM01'] = self.NADUTYEM01
        self.LPEM01 = RM_Field_EMU_BIASCONF_LPEM01(self)
        self.zz_fdict['LPEM01'] = self.LPEM01
        self.GMCEM23 = RM_Field_EMU_BIASCONF_GMCEM23(self)
        self.zz_fdict['GMCEM23'] = self.GMCEM23
        self.UADUTYEM23 = RM_Field_EMU_BIASCONF_UADUTYEM23(self)
        self.zz_fdict['UADUTYEM23'] = self.UADUTYEM23
        self.NADUTYEM23 = RM_Field_EMU_BIASCONF_NADUTYEM23(self)
        self.zz_fdict['NADUTYEM23'] = self.NADUTYEM23
        self.LPEM23 = RM_Field_EMU_BIASCONF_LPEM23(self)
        self.zz_fdict['LPEM23'] = self.LPEM23
        self.EN_GMC_W_BGR = RM_Field_EMU_BIASCONF_EN_GMC_W_BGR(self)
        self.zz_fdict['EN_GMC_W_BGR'] = self.EN_GMC_W_BGR
        self.LSBIAS_SEL = RM_Field_EMU_BIASCONF_LSBIAS_SEL(self)
        self.zz_fdict['LSBIAS_SEL'] = self.LSBIAS_SEL
        self.ILTC_NODUTY_EN = RM_Field_EMU_BIASCONF_ILTC_NODUTY_EN(self)
        self.zz_fdict['ILTC_NODUTY_EN'] = self.ILTC_NODUTY_EN
        self.DISRPUPDATE = RM_Field_EMU_BIASCONF_DISRPUPDATE(self)
        self.zz_fdict['DISRPUPDATE'] = self.DISRPUPDATE
        self.BIASCONTTM = RM_Field_EMU_BIASCONF_BIASCONTTM(self)
        self.zz_fdict['BIASCONTTM'] = self.BIASCONTTM
        self.GMC_CALIB_USESAR = RM_Field_EMU_BIASCONF_GMC_CALIB_USESAR(self)
        self.zz_fdict['GMC_CALIB_USESAR'] = self.GMC_CALIB_USESAR
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_BIASABSTRIM(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_BIASABSTRIM, self).__init__(rmio, label,
            0x400e3000, 0x168,
            'BIASABSTRIM', 'EMU.BIASABSTRIM', 'read-write',
            "",
            0x10101000, 0x1F1F1F00)

        self.BIAS_ABS_TRIM_HP = RM_Field_EMU_BIASABSTRIM_BIAS_ABS_TRIM_HP(self)
        self.zz_fdict['BIAS_ABS_TRIM_HP'] = self.BIAS_ABS_TRIM_HP
        self.BIAS_ABS_TRIM_HPCAL = RM_Field_EMU_BIASABSTRIM_BIAS_ABS_TRIM_HPCAL(self)
        self.zz_fdict['BIAS_ABS_TRIM_HPCAL'] = self.BIAS_ABS_TRIM_HPCAL
        self.BIAS_ABS_TRIM_LPCAL = RM_Field_EMU_BIASABSTRIM_BIAS_ABS_TRIM_LPCAL(self)
        self.zz_fdict['BIAS_ABS_TRIM_LPCAL'] = self.BIAS_ABS_TRIM_LPCAL
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_BIASTEMPTRIM(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_BIASTEMPTRIM, self).__init__(rmio, label,
            0x400e3000, 0x16C,
            'BIASTEMPTRIM', 'EMU.BIASTEMPTRIM', 'read-write',
            "",
            0x00008808, 0x0000FF0F)

        self.BIAS_TEMP_TRIM_HP = RM_Field_EMU_BIASTEMPTRIM_BIAS_TEMP_TRIM_HP(self)
        self.zz_fdict['BIAS_TEMP_TRIM_HP'] = self.BIAS_TEMP_TRIM_HP
        self.BIAS_TEMP_TRIM_HPCAL = RM_Field_EMU_BIASTEMPTRIM_BIAS_TEMP_TRIM_HPCAL(self)
        self.zz_fdict['BIAS_TEMP_TRIM_HPCAL'] = self.BIAS_TEMP_TRIM_HPCAL
        self.BIAS_TEMP_TRIM_LPCAL = RM_Field_EMU_BIASTEMPTRIM_BIAS_TEMP_TRIM_LPCAL(self)
        self.zz_fdict['BIAS_TEMP_TRIM_LPCAL'] = self.BIAS_TEMP_TRIM_LPCAL
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_BIASTRIM(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_BIASTRIM, self).__init__(rmio, label,
            0x400e3000, 0x170,
            'BIASTRIM', 'EMU.BIASTRIM', 'read-write',
            "",
            0x00C0000C, 0x01F003FF)

        self.BIAS_VREF_TRIM = RM_Field_EMU_BIASTRIM_BIAS_VREF_TRIM(self)
        self.zz_fdict['BIAS_VREF_TRIM'] = self.BIAS_VREF_TRIM
        self.BIAS_LDO_NABIAS = RM_Field_EMU_BIASTRIM_BIAS_LDO_NABIAS(self)
        self.zz_fdict['BIAS_LDO_NABIAS'] = self.BIAS_LDO_NABIAS
        self.BIAS_LDO_ILOAD = RM_Field_EMU_BIASTRIM_BIAS_LDO_ILOAD(self)
        self.zz_fdict['BIAS_LDO_ILOAD'] = self.BIAS_LDO_ILOAD
        self.BIAS_NA_MULT = RM_Field_EMU_BIASTRIM_BIAS_NA_MULT(self)
        self.zz_fdict['BIAS_NA_MULT'] = self.BIAS_NA_MULT
        self.BIAS_DLY_TRIM = RM_Field_EMU_BIASTRIM_BIAS_DLY_TRIM(self)
        self.zz_fdict['BIAS_DLY_TRIM'] = self.BIAS_DLY_TRIM
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_BIASPERIOD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_BIASPERIOD, self).__init__(rmio, label,
            0x400e3000, 0x174,
            'BIASPERIOD', 'EMU.BIASPERIOD', 'read-write',
            "",
            0x01100000, 0x07733000)

        self.BIAS_REFRESH_PERIOD_EM03 = RM_Field_EMU_BIASPERIOD_BIAS_REFRESH_PERIOD_EM03(self)
        self.zz_fdict['BIAS_REFRESH_PERIOD_EM03'] = self.BIAS_REFRESH_PERIOD_EM03
        self.BIAS_REFRESH_PERIOD_EM4H = RM_Field_EMU_BIASPERIOD_BIAS_REFRESH_PERIOD_EM4H(self)
        self.zz_fdict['BIAS_REFRESH_PERIOD_EM4H'] = self.BIAS_REFRESH_PERIOD_EM4H
        self.BIAS_GMC_CALIB_PERIOD_EM03 = RM_Field_EMU_BIASPERIOD_BIAS_GMC_CALIB_PERIOD_EM03(self)
        self.zz_fdict['BIAS_GMC_CALIB_PERIOD_EM03'] = self.BIAS_GMC_CALIB_PERIOD_EM03
        self.BIAS_GMC_CALIB_PERIOD_EM4H = RM_Field_EMU_BIASPERIOD_BIAS_GMC_CALIB_PERIOD_EM4H(self)
        self.zz_fdict['BIAS_GMC_CALIB_PERIOD_EM4H'] = self.BIAS_GMC_CALIB_PERIOD_EM4H
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DREGCALIB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DREGCALIB, self).__init__(rmio, label,
            0x400e3000, 0x178,
            'DREGCALIB', 'EMU.DREGCALIB', 'read-write',
            "",
            0x00140C19, 0x007F0C3F)

        self.HDREG_TRIM_VREG = RM_Field_EMU_DREGCALIB_HDREG_TRIM_VREG(self)
        self.zz_fdict['HDREG_TRIM_VREG'] = self.HDREG_TRIM_VREG
        self.HDREG_TRIM_ISRC_CINT = RM_Field_EMU_DREGCALIB_HDREG_TRIM_ISRC_CINT(self)
        self.zz_fdict['HDREG_TRIM_ISRC_CINT'] = self.HDREG_TRIM_ISRC_CINT
        self.LDREG_TRIM_VREG = RM_Field_EMU_DREGCALIB_LDREG_TRIM_VREG(self)
        self.zz_fdict['LDREG_TRIM_VREG'] = self.LDREG_TRIM_VREG
        self.LDREG_DUTYSCALE = RM_Field_EMU_DREGCALIB_LDREG_DUTYSCALE(self)
        self.zz_fdict['LDREG_DUTYSCALE'] = self.LDREG_DUTYSCALE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DREGOVERRIDE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DREGOVERRIDE, self).__init__(rmio, label,
            0x400e3000, 0x17C,
            'DREGOVERRIDE', 'EMU.DREGOVERRIDE', 'read-write',
            "",
            0x00000000, 0x00003F1D)

        self.LDREG_OVERRIDE_EN = RM_Field_EMU_DREGOVERRIDE_LDREG_OVERRIDE_EN(self)
        self.zz_fdict['LDREG_OVERRIDE_EN'] = self.LDREG_OVERRIDE_EN
        self.OVR_LDREG_EN_PD0SW = RM_Field_EMU_DREGOVERRIDE_OVR_LDREG_EN_PD0SW(self)
        self.zz_fdict['OVR_LDREG_EN_PD0SW'] = self.OVR_LDREG_EN_PD0SW
        self.OVR_LDREG_EN_LDREG = RM_Field_EMU_DREGOVERRIDE_OVR_LDREG_EN_LDREG(self)
        self.zz_fdict['OVR_LDREG_EN_LDREG'] = self.OVR_LDREG_EN_LDREG
        self.OVR_LDREG_VREF_EN = RM_Field_EMU_DREGOVERRIDE_OVR_LDREG_VREF_EN(self)
        self.zz_fdict['OVR_LDREG_VREF_EN'] = self.OVR_LDREG_VREF_EN
        self.HDREG_OVERRIDE_EN = RM_Field_EMU_DREGOVERRIDE_HDREG_OVERRIDE_EN(self)
        self.zz_fdict['HDREG_OVERRIDE_EN'] = self.HDREG_OVERRIDE_EN
        self.OVR_HDREG_EN_HARD_SW = RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_HARD_SW(self)
        self.zz_fdict['OVR_HDREG_EN_HARD_SW'] = self.OVR_HDREG_EN_HARD_SW
        self.OVR_HDREG_EN_HDREG_BIAS = RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_HDREG_BIAS(self)
        self.zz_fdict['OVR_HDREG_EN_HDREG_BIAS'] = self.OVR_HDREG_EN_HDREG_BIAS
        self.OVR_HDREG_EN_COLD_START = RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_COLD_START(self)
        self.zz_fdict['OVR_HDREG_EN_COLD_START'] = self.OVR_HDREG_EN_COLD_START
        self.OVR_HDREG_EN_HDREG_FUNC = RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_HDREG_FUNC(self)
        self.zz_fdict['OVR_HDREG_EN_HDREG_FUNC'] = self.OVR_HDREG_EN_HDREG_FUNC
        self.OVR_HDREG_EN_VREG_MODE = RM_Field_EMU_DREGOVERRIDE_OVR_HDREG_EN_VREG_MODE(self)
        self.zz_fdict['OVR_HDREG_EN_VREG_MODE'] = self.OVR_HDREG_EN_VREG_MODE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_RAM0FEATURE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_RAM0FEATURE, self).__init__(rmio, label,
            0x400e3000, 0x180,
            'RAM0FEATURE', 'EMU.RAM0FEATURE', 'write-only',
            "",
            0x001F0030, 0x001F0330)

        self.SEQRAMEN = RM_Field_EMU_RAM0FEATURE_SEQRAMEN(self)
        self.zz_fdict['SEQRAMEN'] = self.SEQRAMEN
        self.RAM0DIV = RM_Field_EMU_RAM0FEATURE_RAM0DIV(self)
        self.zz_fdict['RAM0DIV'] = self.RAM0DIV
        self.RAMSIZE = RM_Field_EMU_RAM0FEATURE_RAMSIZE(self)
        self.zz_fdict['RAMSIZE'] = self.RAMSIZE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_STATEDLY0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_STATEDLY0, self).__init__(rmio, label,
            0x400e3000, 0x184,
            'STATEDLY0', 'EMU.STATEDLY0', 'read-write',
            "",
            0x00002547, 0x0003F7FF)

        self.EM23WAITHD = RM_Field_EMU_STATEDLY0_EM23WAITHD(self)
        self.zz_fdict['EM23WAITHD'] = self.EM23WAITHD
        self.EM23WAITHDFUNC = RM_Field_EMU_STATEDLY0_EM23WAITHDFUNC(self)
        self.zz_fdict['EM23WAITHDFUNC'] = self.EM23WAITHDFUNC
        self.EM4WAITHD = RM_Field_EMU_STATEDLY0_EM4WAITHD(self)
        self.zz_fdict['EM4WAITHD'] = self.EM4WAITHD
        self.EM4WAITHDFUNC = RM_Field_EMU_STATEDLY0_EM4WAITHDFUNC(self)
        self.zz_fdict['EM4WAITHDFUNC'] = self.EM4WAITHDFUNC
        self.ISORETDELAY = RM_Field_EMU_STATEDLY0_ISORETDELAY(self)
        self.zz_fdict['ISORETDELAY'] = self.ISORETDELAY
        self.RETDEASSERTDELAY = RM_Field_EMU_STATEDLY0_RETDEASSERTDELAY(self)
        self.zz_fdict['RETDEASSERTDELAY'] = self.RETDEASSERTDELAY
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_STATEDLY1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_STATEDLY1, self).__init__(rmio, label,
            0x400e3000, 0x188,
            'STATEDLY1', 'EMU.STATEDLY1', 'read-write',
            "",
            0x000002FF, 0xFFFF07FF)

        self.EM4SPORDELAY = RM_Field_EMU_STATEDLY1_EM4SPORDELAY(self)
        self.zz_fdict['EM4SPORDELAY'] = self.EM4SPORDELAY
        self.SETTLINGDELAY = RM_Field_EMU_STATEDLY1_SETTLINGDELAY(self)
        self.zz_fdict['SETTLINGDELAY'] = self.SETTLINGDELAY
        self.EM4HDREGWAIT = RM_Field_EMU_STATEDLY1_EM4HDREGWAIT(self)
        self.zz_fdict['EM4HDREGWAIT'] = self.EM4HDREGWAIT
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_VMONCONF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_VMONCONF, self).__init__(rmio, label,
            0x400e3000, 0x18C,
            'VMONCONF', 'EMU.VMONCONF', 'read-write',
            "",
            0x00000020, 0x0000003F)

        self.CALIBEN = RM_Field_EMU_VMONCONF_CALIBEN(self)
        self.zz_fdict['CALIBEN'] = self.CALIBEN
        self.BUFBIAS = RM_Field_EMU_VMONCONF_BUFBIAS(self)
        self.zz_fdict['BUFBIAS'] = self.BUFBIAS
        self.CURRBOOST = RM_Field_EMU_VMONCONF_CURRBOOST(self)
        self.zz_fdict['CURRBOOST'] = self.CURRBOOST
        self.VREFCAL = RM_Field_EMU_VMONCONF_VREFCAL(self)
        self.zz_fdict['VREFCAL'] = self.VREFCAL
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TESTLOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TESTLOCK, self).__init__(rmio, label,
            0x400e3000, 0x190,
            'TESTLOCK', 'EMU.TESTLOCK', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.LOCKKEY = RM_Field_EMU_TESTLOCK_LOCKKEY(self)
        self.zz_fdict['LOCKKEY'] = self.LOCKKEY
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_SCANCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_SCANCTRL, self).__init__(rmio, label,
            0x400e3000, 0x194,
            'SCANCTRL', 'EMU.SCANCTRL', 'read-write',
            "",
            0x00000000, 0x0000001E)

        self.SCANTEST_EN = RM_Field_EMU_SCANCTRL_SCANTEST_EN(self)
        self.zz_fdict['SCANTEST_EN'] = self.SCANTEST_EN
        self.SCAN_PIN_MODE = RM_Field_EMU_SCANCTRL_SCAN_PIN_MODE(self)
        self.zz_fdict['SCAN_PIN_MODE'] = self.SCAN_PIN_MODE
        self.SCAN_DRIVE_MODE = RM_Field_EMU_SCANCTRL_SCAN_DRIVE_MODE(self)
        self.zz_fdict['SCAN_DRIVE_MODE'] = self.SCAN_DRIVE_MODE
        self.ISO_OVERRIDE_EN = RM_Field_EMU_SCANCTRL_ISO_OVERRIDE_EN(self)
        self.zz_fdict['ISO_OVERRIDE_EN'] = self.ISO_OVERRIDE_EN
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TESTCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TESTCTRL, self).__init__(rmio, label,
            0x400e3000, 0x198,
            'TESTCTRL', 'EMU.TESTCTRL', 'read-write',
            "",
            0x00000000, 0xFF3F3FC7)

        self.EXPORT_RESET = RM_Field_EMU_TESTCTRL_EXPORT_RESET(self)
        self.zz_fdict['EXPORT_RESET'] = self.EXPORT_RESET
        self.HARD_PIN_RESET_OVERRIDE = RM_Field_EMU_TESTCTRL_HARD_PIN_RESET_OVERRIDE(self)
        self.zz_fdict['HARD_PIN_RESET_OVERRIDE'] = self.HARD_PIN_RESET_OVERRIDE
        self.MASK_EXPORT_RESET = RM_Field_EMU_TESTCTRL_MASK_EXPORT_RESET(self)
        self.zz_fdict['MASK_EXPORT_RESET'] = self.MASK_EXPORT_RESET
        self.RAW_BOD_SEL = RM_Field_EMU_TESTCTRL_RAW_BOD_SEL(self)
        self.zz_fdict['RAW_BOD_SEL'] = self.RAW_BOD_SEL
        self.BOD_MASK = RM_Field_EMU_TESTCTRL_BOD_MASK(self)
        self.zz_fdict['BOD_MASK'] = self.BOD_MASK
        self.CMCTRLPRSSEL0 = RM_Field_EMU_TESTCTRL_CMCTRLPRSSEL0(self)
        self.zz_fdict['CMCTRLPRSSEL0'] = self.CMCTRLPRSSEL0
        self.CMCTRLPRSSEL1 = RM_Field_EMU_TESTCTRL_CMCTRLPRSSEL1(self)
        self.zz_fdict['CMCTRLPRSSEL1'] = self.CMCTRLPRSSEL1
        self.DVDD_DSCHRG = RM_Field_EMU_TESTCTRL_DVDD_DSCHRG(self)
        self.zz_fdict['DVDD_DSCHRG'] = self.DVDD_DSCHRG
        self.PD1_DSCHRG = RM_Field_EMU_TESTCTRL_PD1_DSCHRG(self)
        self.zz_fdict['PD1_DSCHRG'] = self.PD1_DSCHRG
        self.BIAS_OVERRIDE_EN = RM_Field_EMU_TESTCTRL_BIAS_OVERRIDE_EN(self)
        self.zz_fdict['BIAS_OVERRIDE_EN'] = self.BIAS_OVERRIDE_EN
        self.POWERLOSSDISABLE = RM_Field_EMU_TESTCTRL_POWERLOSSDISABLE(self)
        self.zz_fdict['POWERLOSSDISABLE'] = self.POWERLOSSDISABLE
        self.FLASH_PWR_SW_OVR = RM_Field_EMU_TESTCTRL_FLASH_PWR_SW_OVR(self)
        self.zz_fdict['FLASH_PWR_SW_OVR'] = self.FLASH_PWR_SW_OVR
        self.EMUOSCEN = RM_Field_EMU_TESTCTRL_EMUOSCEN(self)
        self.zz_fdict['EMUOSCEN'] = self.EMUOSCEN
        self.EM234FLASHPWRDOWNDIS = RM_Field_EMU_TESTCTRL_EM234FLASHPWRDOWNDIS(self)
        self.zz_fdict['EM234FLASHPWRDOWNDIS'] = self.EM234FLASHPWRDOWNDIS
        self.LDREGDISMASK = RM_Field_EMU_TESTCTRL_LDREGDISMASK(self)
        self.zz_fdict['LDREGDISMASK'] = self.LDREGDISMASK
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_BIASTESTCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_BIASTESTCTRL, self).__init__(rmio, label,
            0x400e3000, 0x19C,
            'BIASTESTCTRL', 'EMU.BIASTESTCTRL', 'read-write',
            "",
            0x00000000, 0x01BFF37D)

        self.GMC_CALIB_START = RM_Field_EMU_BIASTESTCTRL_GMC_CALIB_START(self)
        self.zz_fdict['GMC_CALIB_START'] = self.GMC_CALIB_START
        self.FORCE_GMC_CAL_REQ = RM_Field_EMU_BIASTESTCTRL_FORCE_GMC_CAL_REQ(self)
        self.zz_fdict['FORCE_GMC_CAL_REQ'] = self.FORCE_GMC_CAL_REQ
        self.BIAS_RIP_RESET = RM_Field_EMU_BIASTESTCTRL_BIAS_RIP_RESET(self)
        self.zz_fdict['BIAS_RIP_RESET'] = self.BIAS_RIP_RESET
        self.BIAS_RIP_OVR = RM_Field_EMU_BIASTESTCTRL_BIAS_RIP_OVR(self)
        self.zz_fdict['BIAS_RIP_OVR'] = self.BIAS_RIP_OVR
        self.BIAS_RIP_OVR_CLK = RM_Field_EMU_BIASTESTCTRL_BIAS_RIP_OVR_CLK(self)
        self.zz_fdict['BIAS_RIP_OVR_CLK'] = self.BIAS_RIP_OVR_CLK
        self.BIAS_GMC_CALIB_OVR = RM_Field_EMU_BIASTESTCTRL_BIAS_GMC_CALIB_OVR(self)
        self.zz_fdict['BIAS_GMC_CALIB_OVR'] = self.BIAS_GMC_CALIB_OVR
        self.BIAS_DLY_SEL = RM_Field_EMU_BIASTESTCTRL_BIAS_DLY_SEL(self)
        self.zz_fdict['BIAS_DLY_SEL'] = self.BIAS_DLY_SEL
        self.GMC_CALIB_OVR = RM_Field_EMU_BIASTESTCTRL_GMC_CALIB_OVR(self)
        self.zz_fdict['GMC_CALIB_OVR'] = self.GMC_CALIB_OVR
        self.TM_BIASRDY_MASK = RM_Field_EMU_BIASTESTCTRL_TM_BIASRDY_MASK(self)
        self.zz_fdict['TM_BIASRDY_MASK'] = self.TM_BIASRDY_MASK
        self.BLANK_BIAS_RDY = RM_Field_EMU_BIASTESTCTRL_BLANK_BIAS_RDY(self)
        self.zz_fdict['BLANK_BIAS_RDY'] = self.BLANK_BIAS_RDY
        self.OVR_BIAS_RDY_EN = RM_Field_EMU_BIASTESTCTRL_OVR_BIAS_RDY_EN(self)
        self.zz_fdict['OVR_BIAS_RDY_EN'] = self.OVR_BIAS_RDY_EN
        self.OVR_BIAS_EN = RM_Field_EMU_BIASTESTCTRL_OVR_BIAS_EN(self)
        self.zz_fdict['OVR_BIAS_EN'] = self.OVR_BIAS_EN
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TESTCTRLANAISO(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TESTCTRLANAISO, self).__init__(rmio, label,
            0x400e3000, 0x1A0,
            'TESTCTRLANAISO', 'EMU.TESTCTRLANAISO', 'read-write',
            "",
            0x00000000, 0xC0787FEE)

        self.ISO_LFRCO = RM_Field_EMU_TESTCTRLANAISO_ISO_LFRCO(self)
        self.zz_fdict['ISO_LFRCO'] = self.ISO_LFRCO
        self.ISO_LFXO = RM_Field_EMU_TESTCTRLANAISO_ISO_LFXO(self)
        self.zz_fdict['ISO_LFXO'] = self.ISO_LFXO
        self.ISO_ULFRCO = RM_Field_EMU_TESTCTRLANAISO_ISO_ULFRCO(self)
        self.zz_fdict['ISO_ULFRCO'] = self.ISO_ULFRCO
        self.ISO_HFRCO = RM_Field_EMU_TESTCTRLANAISO_ISO_HFRCO(self)
        self.zz_fdict['ISO_HFRCO'] = self.ISO_HFRCO
        self.ISO_AUXHFRCO = RM_Field_EMU_TESTCTRLANAISO_ISO_AUXHFRCO(self)
        self.zz_fdict['ISO_AUXHFRCO'] = self.ISO_AUXHFRCO
        self.ISO_EMUOSC = RM_Field_EMU_TESTCTRLANAISO_ISO_EMUOSC(self)
        self.zz_fdict['ISO_EMUOSC'] = self.ISO_EMUOSC
        self.ISO_BIAS = RM_Field_EMU_TESTCTRLANAISO_ISO_BIAS(self)
        self.zz_fdict['ISO_BIAS'] = self.ISO_BIAS
        self.ISO_PORBOD = RM_Field_EMU_TESTCTRLANAISO_ISO_PORBOD(self)
        self.zz_fdict['ISO_PORBOD'] = self.ISO_PORBOD
        self.ISO_CMP = RM_Field_EMU_TESTCTRLANAISO_ISO_CMP(self)
        self.zz_fdict['ISO_CMP'] = self.ISO_CMP
        self.ISO_ADC = RM_Field_EMU_TESTCTRLANAISO_ISO_ADC(self)
        self.zz_fdict['ISO_ADC'] = self.ISO_ADC
        self.ISO_DAC = RM_Field_EMU_TESTCTRLANAISO_ISO_DAC(self)
        self.zz_fdict['ISO_DAC'] = self.ISO_DAC
        self.ISO_AMUXCP = RM_Field_EMU_TESTCTRLANAISO_ISO_AMUXCP(self)
        self.zz_fdict['ISO_AMUXCP'] = self.ISO_AMUXCP
        self.ISO_DCDC = RM_Field_EMU_TESTCTRLANAISO_ISO_DCDC(self)
        self.zz_fdict['ISO_DCDC'] = self.ISO_DCDC
        self.ISO_BCLFRCO = RM_Field_EMU_TESTCTRLANAISO_ISO_BCLFRCO(self)
        self.zz_fdict['ISO_BCLFRCO'] = self.ISO_BCLFRCO
        self.ISO_FLASHVREF = RM_Field_EMU_TESTCTRLANAISO_ISO_FLASHVREF(self)
        self.zz_fdict['ISO_FLASHVREF'] = self.ISO_FLASHVREF
        self.ISO_CSEN = RM_Field_EMU_TESTCTRLANAISO_ISO_CSEN(self)
        self.zz_fdict['ISO_CSEN'] = self.ISO_CSEN
        self.ISO_WFXO = RM_Field_EMU_TESTCTRLANAISO_ISO_WFXO(self)
        self.zz_fdict['ISO_WFXO'] = self.ISO_WFXO
        self.ISO_RADIO = RM_Field_EMU_TESTCTRLANAISO_ISO_RADIO(self)
        self.zz_fdict['ISO_RADIO'] = self.ISO_RADIO
        self.ISO_LVDS = RM_Field_EMU_TESTCTRLANAISO_ISO_LVDS(self)
        self.zz_fdict['ISO_LVDS'] = self.ISO_LVDS
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_EM01COUNTERWAIT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_EM01COUNTERWAIT, self).__init__(rmio, label,
            0x400e3000, 0x1A4,
            'EM01COUNTERWAIT', 'EMU.EM01COUNTERWAIT', 'read-write',
            "",
            0x000292B0, 0x0007FFFF)

        self.BODSETTLEWAIT = RM_Field_EMU_EM01COUNTERWAIT_BODSETTLEWAIT(self)
        self.zz_fdict['BODSETTLEWAIT'] = self.BODSETTLEWAIT
        self.HDREGSTEPWAIT = RM_Field_EMU_EM01COUNTERWAIT_HDREGSTEPWAIT(self)
        self.zz_fdict['HDREGSTEPWAIT'] = self.HDREGSTEPWAIT
        self.VSBODINTWAIT = RM_Field_EMU_EM01COUNTERWAIT_VSBODINTWAIT(self)
        self.zz_fdict['VSBODINTWAIT'] = self.VSBODINTWAIT
        self.FLASHVREFBYPASSDISWAIT = RM_Field_EMU_EM01COUNTERWAIT_FLASHVREFBYPASSDISWAIT(self)
        self.zz_fdict['FLASHVREFBYPASSDISWAIT'] = self.FLASHVREFBYPASSDISWAIT
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_RAM1FEATURE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_RAM1FEATURE, self).__init__(rmio, label,
            0x400e3000, 0x1A8,
            'RAM1FEATURE', 'EMU.RAM1FEATURE', 'write-only',
            "",
            0x00000003, 0x00000003)

        self.RAMSIZE = RM_Field_EMU_RAM1FEATURE_RAMSIZE(self)
        self.zz_fdict['RAMSIZE'] = self.RAMSIZE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_RAM2FEATURE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_RAM2FEATURE, self).__init__(rmio, label,
            0x400e3000, 0x1AC,
            'RAM2FEATURE', 'EMU.RAM2FEATURE', 'write-only',
            "",
            0x00000001, 0x00000001)

        self.RAMSIZE = RM_Field_EMU_RAM2FEATURE_RAMSIZE(self)
        self.zz_fdict['RAMSIZE'] = self.RAMSIZE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_RAMBIASCONF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_RAMBIASCONF, self).__init__(rmio, label,
            0x400e3000, 0x1B0,
            'RAMBIASCONF', 'EMU.RAMBIASCONF', 'read-write',
            "",
            0x00000002, 0x0000000F)

        self.RAMBIASCTRL = RM_Field_EMU_RAMBIASCONF_RAMBIASCTRL(self)
        self.zz_fdict['RAMBIASCTRL'] = self.RAMBIASCTRL
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TGTRAMRM(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TGTRAMRM, self).__init__(rmio, label,
            0x400e3000, 0x1B4,
            'TGTRAMRM', 'EMU.TGTRAMRM', 'read-write',
            "",
            0x00040404, 0x000F0F0F)

        self.TGTRAMRM0 = RM_Field_EMU_TGTRAMRM_TGTRAMRM0(self)
        self.zz_fdict['TGTRAMRM0'] = self.TGTRAMRM0
        self.TGTRAMRM1 = RM_Field_EMU_TGTRAMRM_TGTRAMRM1(self)
        self.zz_fdict['TGTRAMRM1'] = self.TGTRAMRM1
        self.TGTRAMRM2 = RM_Field_EMU_TGTRAMRM_TGTRAMRM2(self)
        self.zz_fdict['TGTRAMRM2'] = self.TGTRAMRM2
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TGTDECBODTHR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TGTDECBODTHR, self).__init__(rmio, label,
            0x400e3000, 0x1B8,
            'TGTDECBODTHR', 'EMU.TGTDECBODTHR', 'read-write',
            "",
            0x000D0A06, 0x000F0F0F)

        self.TGTDECBODTHR0 = RM_Field_EMU_TGTDECBODTHR_TGTDECBODTHR0(self)
        self.zz_fdict['TGTDECBODTHR0'] = self.TGTDECBODTHR0
        self.TGTDECBODTHR1 = RM_Field_EMU_TGTDECBODTHR_TGTDECBODTHR1(self)
        self.zz_fdict['TGTDECBODTHR1'] = self.TGTDECBODTHR1
        self.TGTDECBODTHR2 = RM_Field_EMU_TGTDECBODTHR_TGTDECBODTHR2(self)
        self.zz_fdict['TGTDECBODTHR2'] = self.TGTDECBODTHR2
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TGTHDREGTRIM(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TGTHDREGTRIM, self).__init__(rmio, label,
            0x400e3000, 0x1BC,
            'TGTHDREGTRIM', 'EMU.TGTHDREGTRIM', 'read-write',
            "",
            0x0019140F, 0x003F3F3F)

        self.TGTHDREGTRIM0 = RM_Field_EMU_TGTHDREGTRIM_TGTHDREGTRIM0(self)
        self.zz_fdict['TGTHDREGTRIM0'] = self.TGTHDREGTRIM0
        self.TGTHDREGTRIM1 = RM_Field_EMU_TGTHDREGTRIM_TGTHDREGTRIM1(self)
        self.zz_fdict['TGTHDREGTRIM1'] = self.TGTHDREGTRIM1
        self.TGTHDREGTRIM2 = RM_Field_EMU_TGTHDREGTRIM_TGTHDREGTRIM2(self)
        self.zz_fdict['TGTHDREGTRIM2'] = self.TGTHDREGTRIM2
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TGTDCDCLNVCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TGTDCDCLNVCTRL, self).__init__(rmio, label,
            0x400e3000, 0x1C0,
            'TGTDCDCLNVCTRL', 'EMU.TGTDCDCLNVCTRL', 'read-write',
            "",
            0x00717171, 0x007F7F7F)

        self.TGTDCDCLNVCTRL0 = RM_Field_EMU_TGTDCDCLNVCTRL_TGTDCDCLNVCTRL0(self)
        self.zz_fdict['TGTDCDCLNVCTRL0'] = self.TGTDCDCLNVCTRL0
        self.TGTDCDCLNVCTRL1 = RM_Field_EMU_TGTDCDCLNVCTRL_TGTDCDCLNVCTRL1(self)
        self.zz_fdict['TGTDCDCLNVCTRL1'] = self.TGTDCDCLNVCTRL1
        self.TGTDCDCLNVCTRL2 = RM_Field_EMU_TGTDCDCLNVCTRL_TGTDCDCLNVCTRL2(self)
        self.zz_fdict['TGTDCDCLNVCTRL2'] = self.TGTDCDCLNVCTRL2
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TGTLDREGTRIM(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TGTLDREGTRIM, self).__init__(rmio, label,
            0x400e3000, 0x1C4,
            'TGTLDREGTRIM', 'EMU.TGTLDREGTRIM', 'read-write',
            "",
            0x00140F0A, 0x001F1F1F)

        self.TGTLDREGTRIM0 = RM_Field_EMU_TGTLDREGTRIM_TGTLDREGTRIM0(self)
        self.zz_fdict['TGTLDREGTRIM0'] = self.TGTLDREGTRIM0
        self.TGTLDREGTRIM1 = RM_Field_EMU_TGTLDREGTRIM_TGTLDREGTRIM1(self)
        self.zz_fdict['TGTLDREGTRIM1'] = self.TGTLDREGTRIM1
        self.TGTLDREGTRIM2 = RM_Field_EMU_TGTLDREGTRIM_TGTLDREGTRIM2(self)
        self.zz_fdict['TGTLDREGTRIM2'] = self.TGTLDREGTRIM2
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TGTDCDCLPVCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TGTDCDCLPVCTRL, self).__init__(rmio, label,
            0x400e3000, 0x1C8,
            'TGTDCDCLPVCTRL', 'EMU.TGTDCDCLPVCTRL', 'read-write',
            "",
            0x000000B4, 0x000000FF)

        self.TGTDCDCLPVCTRL0 = RM_Field_EMU_TGTDCDCLPVCTRL_TGTDCDCLPVCTRL0(self)
        self.zz_fdict['TGTDCDCLPVCTRL0'] = self.TGTDCDCLPVCTRL0
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TGTRREGTRIM(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TGTRREGTRIM, self).__init__(rmio, label,
            0x400e3000, 0x1CC,
            'TGTRREGTRIM', 'EMU.TGTRREGTRIM', 'read-write',
            "",
            0x00281411, 0x00FFFFFF)

        self.TGTRREGTRIML0 = RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIML0(self)
        self.zz_fdict['TGTRREGTRIML0'] = self.TGTRREGTRIML0
        self.TGTRREGTRIMH0 = RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIMH0(self)
        self.zz_fdict['TGTRREGTRIMH0'] = self.TGTRREGTRIMH0
        self.TGTRREGTRIML1 = RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIML1(self)
        self.zz_fdict['TGTRREGTRIML1'] = self.TGTRREGTRIML1
        self.TGTRREGTRIMH1 = RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIMH1(self)
        self.zz_fdict['TGTRREGTRIMH1'] = self.TGTRREGTRIMH1
        self.TGTRREGTRIML2 = RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIML2(self)
        self.zz_fdict['TGTRREGTRIML2'] = self.TGTRREGTRIML2
        self.TGTRREGTRIMH2 = RM_Field_EMU_TGTRREGTRIM_TGTRREGTRIMH2(self)
        self.zz_fdict['TGTRREGTRIMH2'] = self.TGTRREGTRIMH2
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TGTHFRCOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TGTHFRCOCTRL, self).__init__(rmio, label,
            0x400e3000, 0x1D0,
            'TGTHFRCOCTRL', 'EMU.TGTHFRCOCTRL', 'read-write',
            "",
            0xB1481F3C, 0xFFFF3F7F)

        self.TUNING = RM_Field_EMU_TGTHFRCOCTRL_TUNING(self)
        self.zz_fdict['TUNING'] = self.TUNING
        self.FINETUNING = RM_Field_EMU_TGTHFRCOCTRL_FINETUNING(self)
        self.zz_fdict['FINETUNING'] = self.FINETUNING
        self.FREQRANGE = RM_Field_EMU_TGTHFRCOCTRL_FREQRANGE(self)
        self.zz_fdict['FREQRANGE'] = self.FREQRANGE
        self.CMPBIAS = RM_Field_EMU_TGTHFRCOCTRL_CMPBIAS(self)
        self.zz_fdict['CMPBIAS'] = self.CMPBIAS
        self.LDOHP = RM_Field_EMU_TGTHFRCOCTRL_LDOHP(self)
        self.zz_fdict['LDOHP'] = self.LDOHP
        self.CLKDIV = RM_Field_EMU_TGTHFRCOCTRL_CLKDIV(self)
        self.zz_fdict['CLKDIV'] = self.CLKDIV
        self.FINETUNINGEN = RM_Field_EMU_TGTHFRCOCTRL_FINETUNINGEN(self)
        self.zz_fdict['FINETUNINGEN'] = self.FINETUNINGEN
        self.VREFTC = RM_Field_EMU_TGTHFRCOCTRL_VREFTC(self)
        self.zz_fdict['VREFTC'] = self.VREFTC
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_RREGCALIB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_RREGCALIB, self).__init__(rmio, label,
            0x400e3000, 0x1D4,
            'RREGCALIB', 'EMU.RREGCALIB', 'read-write',
            "",
            0x00000000, 0x00FF00FF)

        self.RREG_HIGHSIDE_TRIM = RM_Field_EMU_RREGCALIB_RREG_HIGHSIDE_TRIM(self)
        self.zz_fdict['RREG_HIGHSIDE_TRIM'] = self.RREG_HIGHSIDE_TRIM
        self.RREG_LOWSIDE_TRIM = RM_Field_EMU_RREGCALIB_RREG_LOWSIDE_TRIM(self)
        self.zz_fdict['RREG_LOWSIDE_TRIM'] = self.RREG_LOWSIDE_TRIM
        self.RREG_IDAC_TRIMH = RM_Field_EMU_RREGCALIB_RREG_IDAC_TRIMH(self)
        self.zz_fdict['RREG_IDAC_TRIMH'] = self.RREG_IDAC_TRIMH
        self.RREG_IDAC_TRIML = RM_Field_EMU_RREGCALIB_RREG_IDAC_TRIML(self)
        self.zz_fdict['RREG_IDAC_TRIML'] = self.RREG_IDAC_TRIML
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_RREGTEST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_RREGTEST, self).__init__(rmio, label,
            0x400e3000, 0x1D8,
            'RREGTEST', 'EMU.RREGTEST', 'read-write',
            "",
            0x00000008, 0x000000FF)

        self.RREG_SW_GATE_DRAIN_DIS = RM_Field_EMU_RREGTEST_RREG_SW_GATE_DRAIN_DIS(self)
        self.zz_fdict['RREG_SW_GATE_DRAIN_DIS'] = self.RREG_SW_GATE_DRAIN_DIS
        self.RREG_HIGHSIDE_SW_DIS = RM_Field_EMU_RREGTEST_RREG_HIGHSIDE_SW_DIS(self)
        self.zz_fdict['RREG_HIGHSIDE_SW_DIS'] = self.RREG_HIGHSIDE_SW_DIS
        self.RREG_LOWSIDE_SW_DIS = RM_Field_EMU_RREGTEST_RREG_LOWSIDE_SW_DIS(self)
        self.zz_fdict['RREG_LOWSIDE_SW_DIS'] = self.RREG_LOWSIDE_SW_DIS
        self.RREG_BIAS_5NA_P_EN = RM_Field_EMU_RREGTEST_RREG_BIAS_5NA_P_EN(self)
        self.zz_fdict['RREG_BIAS_5NA_P_EN'] = self.RREG_BIAS_5NA_P_EN
        self.RREG_CAL_EN = RM_Field_EMU_RREGTEST_RREG_CAL_EN(self)
        self.zz_fdict['RREG_CAL_EN'] = self.RREG_CAL_EN
        self.RREG_CAL_RST = RM_Field_EMU_RREGTEST_RREG_CAL_RST(self)
        self.zz_fdict['RREG_CAL_RST'] = self.RREG_CAL_RST
        self.RREG_STATUS_CMPOUT_HIGH = RM_Field_EMU_RREGTEST_RREG_STATUS_CMPOUT_HIGH(self)
        self.zz_fdict['RREG_STATUS_CMPOUT_HIGH'] = self.RREG_STATUS_CMPOUT_HIGH
        self.RREG_STATUS_CMPOUT_LOW = RM_Field_EMU_RREGTEST_RREG_STATUS_CMPOUT_LOW(self)
        self.zz_fdict['RREG_STATUS_CMPOUT_LOW'] = self.RREG_STATUS_CMPOUT_LOW
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_RREGOVERRIDE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_RREGOVERRIDE, self).__init__(rmio, label,
            0x400e3000, 0x1DC,
            'RREGOVERRIDE', 'EMU.RREGOVERRIDE', 'read-write',
            "",
            0x00000000, 0x0000003F)

        self.RREG_OVERRIDE_EN = RM_Field_EMU_RREGOVERRIDE_RREG_OVERRIDE_EN(self)
        self.zz_fdict['RREG_OVERRIDE_EN'] = self.RREG_OVERRIDE_EN
        self.OVR_RREG_HIGHSIDE_PU_DIS = RM_Field_EMU_RREGOVERRIDE_OVR_RREG_HIGHSIDE_PU_DIS(self)
        self.zz_fdict['OVR_RREG_HIGHSIDE_PU_DIS'] = self.OVR_RREG_HIGHSIDE_PU_DIS
        self.OVR_RREG_HIGHSIDE_PU_WEAK_DIS = RM_Field_EMU_RREGOVERRIDE_OVR_RREG_HIGHSIDE_PU_WEAK_DIS(self)
        self.zz_fdict['OVR_RREG_HIGHSIDE_PU_WEAK_DIS'] = self.OVR_RREG_HIGHSIDE_PU_WEAK_DIS
        self.OVR_RREG_LOWSIDE_PD_DIS = RM_Field_EMU_RREGOVERRIDE_OVR_RREG_LOWSIDE_PD_DIS(self)
        self.zz_fdict['OVR_RREG_LOWSIDE_PD_DIS'] = self.OVR_RREG_LOWSIDE_PD_DIS
        self.OVR_RREG_LOWSIDE_PD_WEAK_DIS = RM_Field_EMU_RREGOVERRIDE_OVR_RREG_LOWSIDE_PD_WEAK_DIS(self)
        self.zz_fdict['OVR_RREG_LOWSIDE_PD_WEAK_DIS'] = self.OVR_RREG_LOWSIDE_PD_WEAK_DIS
        self.OVR_RREG_EN = RM_Field_EMU_RREGOVERRIDE_OVR_RREG_EN(self)
        self.zz_fdict['OVR_RREG_EN'] = self.OVR_RREG_EN
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_BCOSCENCMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_BCOSCENCMD, self).__init__(rmio, label,
            0x400e3000, 0x1E0,
            'BCOSCENCMD', 'EMU.BCOSCENCMD', 'write-only',
            "",
            0x00000000, 0x00000003)

        self.BCLFRCOEN = RM_Field_EMU_BCOSCENCMD_BCLFRCOEN(self)
        self.zz_fdict['BCLFRCOEN'] = self.BCLFRCOEN
        self.BCLFRCODIS = RM_Field_EMU_BCOSCENCMD_BCLFRCODIS(self)
        self.zz_fdict['BCLFRCODIS'] = self.BCLFRCODIS
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_BCLFRCOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_BCLFRCOCTRL, self).__init__(rmio, label,
            0x400e3000, 0x1E4,
            'BCLFRCOCTRL', 'EMU.BCLFRCOCTRL', 'read-write',
            "",
            0x81060100, 0xF30701FF)

        self.TUNING = RM_Field_EMU_BCLFRCOCTRL_TUNING(self)
        self.zz_fdict['TUNING'] = self.TUNING
        self.ENVREF = RM_Field_EMU_BCLFRCOCTRL_ENVREF(self)
        self.zz_fdict['ENVREF'] = self.ENVREF
        self.ENCHOP = RM_Field_EMU_BCLFRCOCTRL_ENCHOP(self)
        self.zz_fdict['ENCHOP'] = self.ENCHOP
        self.ENDEM = RM_Field_EMU_BCLFRCOCTRL_ENDEM(self)
        self.zz_fdict['ENDEM'] = self.ENDEM
        self.TIMEOUT = RM_Field_EMU_BCLFRCOCTRL_TIMEOUT(self)
        self.zz_fdict['TIMEOUT'] = self.TIMEOUT
        self.GMCCURTUNE = RM_Field_EMU_BCLFRCOCTRL_GMCCURTUNE(self)
        self.zz_fdict['GMCCURTUNE'] = self.GMCCURTUNE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TESTBCLFRCOCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TESTBCLFRCOCTRL, self).__init__(rmio, label,
            0x400e3000, 0x1E8,
            'TESTBCLFRCOCTRL', 'EMU.TESTBCLFRCOCTRL', 'read-write',
            "",
            0x00000000, 0x0FF1FFF3)

        self.DISOSC = RM_Field_EMU_TESTBCLFRCOCTRL_DISOSC(self)
        self.zz_fdict['DISOSC'] = self.DISOSC
        self.DISSYNC = RM_Field_EMU_TESTBCLFRCOCTRL_DISSYNC(self)
        self.zz_fdict['DISSYNC'] = self.DISSYNC
        self.MODE = RM_Field_EMU_TESTBCLFRCOCTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.SELCLKDIV = RM_Field_EMU_TESTBCLFRCOCTRL_SELCLKDIV(self)
        self.zz_fdict['SELCLKDIV'] = self.SELCLKDIV
        self.VREFUPDATE = RM_Field_EMU_TESTBCLFRCOCTRL_VREFUPDATE(self)
        self.zz_fdict['VREFUPDATE'] = self.VREFUPDATE
        self.VREFPRECH = RM_Field_EMU_TESTBCLFRCOCTRL_VREFPRECH(self)
        self.zz_fdict['VREFPRECH'] = self.VREFPRECH
        self.FLIPCHOP = RM_Field_EMU_TESTBCLFRCOCTRL_FLIPCHOP(self)
        self.zz_fdict['FLIPCHOP'] = self.FLIPCHOP
        self.DEMCLKSEL = RM_Field_EMU_TESTBCLFRCOCTRL_DEMCLKSEL(self)
        self.zz_fdict['DEMCLKSEL'] = self.DEMCLKSEL
        self.WELLBUFDIS = RM_Field_EMU_TESTBCLFRCOCTRL_WELLBUFDIS(self)
        self.zz_fdict['WELLBUFDIS'] = self.WELLBUFDIS
        self.FORCECOMP = RM_Field_EMU_TESTBCLFRCOCTRL_FORCECOMP(self)
        self.zz_fdict['FORCECOMP'] = self.FORCECOMP
        self.BLOCKIREF = RM_Field_EMU_TESTBCLFRCOCTRL_BLOCKIREF(self)
        self.zz_fdict['BLOCKIREF'] = self.BLOCKIREF
        self.RNSHUNT = RM_Field_EMU_TESTBCLFRCOCTRL_RNSHUNT(self)
        self.zz_fdict['RNSHUNT'] = self.RNSHUNT
        self.RPSHUNT = RM_Field_EMU_TESTBCLFRCOCTRL_RPSHUNT(self)
        self.zz_fdict['RPSHUNT'] = self.RPSHUNT
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_PORBOD2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_PORBOD2, self).__init__(rmio, label,
            0x400e3000, 0x1EC,
            'PORBOD2', 'EMU.PORBOD2', 'read-write',
            "",
            0x0000000C, 0x0000001F)

        self.PORBOD_REFTRIMEM2 = RM_Field_EMU_PORBOD2_PORBOD_REFTRIMEM2(self)
        self.zz_fdict['PORBOD_REFTRIMEM2'] = self.PORBOD_REFTRIMEM2
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_FLASHVREFCALIB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_FLASHVREFCALIB, self).__init__(rmio, label,
            0x400e3000, 0x1F0,
            'FLASHVREFCALIB', 'EMU.FLASHVREFCALIB', 'read-write',
            "",
            0x0000303C, 0x00067E3F)

        self.FLASHVREF_BYPASS_DIS = RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_BYPASS_DIS(self)
        self.zz_fdict['FLASHVREF_BYPASS_DIS'] = self.FLASHVREF_BYPASS_DIS
        self.FLASHVREF_BYPASS_EN = RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_BYPASS_EN(self)
        self.zz_fdict['FLASHVREF_BYPASS_EN'] = self.FLASHVREF_BYPASS_EN
        self.FLASHVREF_BYPASS_STATUS = RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_BYPASS_STATUS(self)
        self.zz_fdict['FLASHVREF_BYPASS_STATUS'] = self.FLASHVREF_BYPASS_STATUS
        self.FLASHVREF_EN = RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_EN(self)
        self.zz_fdict['FLASHVREF_EN'] = self.FLASHVREF_EN
        self.FLASHVREF_SEL = RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_SEL(self)
        self.zz_fdict['FLASHVREF_SEL'] = self.FLASHVREF_SEL
        self.FLASHVREF_TRIM = RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_TRIM(self)
        self.zz_fdict['FLASHVREF_TRIM'] = self.FLASHVREF_TRIM
        self.FLASHVREF_VREFDIS_EM23 = RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_VREFDIS_EM23(self)
        self.zz_fdict['FLASHVREF_VREFDIS_EM23'] = self.FLASHVREF_VREFDIS_EM23
        self.FLASHVREF_PULLDOWNEN = RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_PULLDOWNEN(self)
        self.zz_fdict['FLASHVREF_PULLDOWNEN'] = self.FLASHVREF_PULLDOWNEN
        self.FLASHVREF_DUTYSCALE = RM_Field_EMU_FLASHVREFCALIB_FLASHVREF_DUTYSCALE(self)
        self.zz_fdict['FLASHVREF_DUTYSCALE'] = self.FLASHVREF_DUTYSCALE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TEMPLO_THR0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TEMPLO_THR0, self).__init__(rmio, label,
            0x400e3000, 0x240,
            'TEMPLO_THR0', 'EMU.TEMPLO_THR0', 'write-only',
            "",
            0xFFFFFFFF, 0xFFFFFFFF)

        self.TEMPLO0 = RM_Field_EMU_TEMPLO_THR0_TEMPLO0(self)
        self.zz_fdict['TEMPLO0'] = self.TEMPLO0
        self.TEMPLO1 = RM_Field_EMU_TEMPLO_THR0_TEMPLO1(self)
        self.zz_fdict['TEMPLO1'] = self.TEMPLO1
        self.TEMPLO2 = RM_Field_EMU_TEMPLO_THR0_TEMPLO2(self)
        self.zz_fdict['TEMPLO2'] = self.TEMPLO2
        self.TEMPLO3 = RM_Field_EMU_TEMPLO_THR0_TEMPLO3(self)
        self.zz_fdict['TEMPLO3'] = self.TEMPLO3
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TEMPHI_THR0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TEMPHI_THR0, self).__init__(rmio, label,
            0x400e3000, 0x244,
            'TEMPHI_THR0', 'EMU.TEMPHI_THR0', 'write-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.TEMPHI0 = RM_Field_EMU_TEMPHI_THR0_TEMPHI0(self)
        self.zz_fdict['TEMPHI0'] = self.TEMPHI0
        self.TEMPHI1 = RM_Field_EMU_TEMPHI_THR0_TEMPHI1(self)
        self.zz_fdict['TEMPHI1'] = self.TEMPHI1
        self.TEMPHI2 = RM_Field_EMU_TEMPHI_THR0_TEMPHI2(self)
        self.zz_fdict['TEMPHI2'] = self.TEMPHI2
        self.TEMPHI3 = RM_Field_EMU_TEMPHI_THR0_TEMPHI3(self)
        self.zz_fdict['TEMPHI3'] = self.TEMPHI3
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TEMPLO_THR1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TEMPLO_THR1, self).__init__(rmio, label,
            0x400e3000, 0x248,
            'TEMPLO_THR1', 'EMU.TEMPLO_THR1', 'write-only',
            "",
            0xFFFFFFFF, 0xFFFFFFFF)

        self.TEMPLO4 = RM_Field_EMU_TEMPLO_THR1_TEMPLO4(self)
        self.zz_fdict['TEMPLO4'] = self.TEMPLO4
        self.TEMPLO5 = RM_Field_EMU_TEMPLO_THR1_TEMPLO5(self)
        self.zz_fdict['TEMPLO5'] = self.TEMPLO5
        self.TEMPLO6 = RM_Field_EMU_TEMPLO_THR1_TEMPLO6(self)
        self.zz_fdict['TEMPLO6'] = self.TEMPLO6
        self.TEMPLO7 = RM_Field_EMU_TEMPLO_THR1_TEMPLO7(self)
        self.zz_fdict['TEMPLO7'] = self.TEMPLO7
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TEMPHI_THR1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TEMPHI_THR1, self).__init__(rmio, label,
            0x400e3000, 0x24C,
            'TEMPHI_THR1', 'EMU.TEMPHI_THR1', 'write-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.TEMPHI4 = RM_Field_EMU_TEMPHI_THR1_TEMPHI4(self)
        self.zz_fdict['TEMPHI4'] = self.TEMPHI4
        self.TEMPHI5 = RM_Field_EMU_TEMPHI_THR1_TEMPHI5(self)
        self.zz_fdict['TEMPHI5'] = self.TEMPHI5
        self.TEMPHI6 = RM_Field_EMU_TEMPHI_THR1_TEMPHI6(self)
        self.zz_fdict['TEMPHI6'] = self.TEMPHI6
        self.TEMPHI7 = RM_Field_EMU_TEMPHI_THR1_TEMPHI7(self)
        self.zz_fdict['TEMPHI7'] = self.TEMPHI7
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_TEMPLO_THR2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_TEMPLO_THR2, self).__init__(rmio, label,
            0x400e3000, 0x250,
            'TEMPLO_THR2', 'EMU.TEMPLO_THR2', 'write-only',
            "",
            0x000000FF, 0x000000FF)

        self.TEMPLO8 = RM_Field_EMU_TEMPLO_THR2_TEMPLO8(self)
        self.zz_fdict['TEMPLO8'] = self.TEMPLO8
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DIAGAEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DIAGAEN, self).__init__(rmio, label,
            0x400e3000, 0x3C0,
            'DIAGAEN', 'EMU.DIAGAEN', 'read-write',
            "",
            0x00000000, 0x80800087)

        self.DIAGA_GP_EN = RM_Field_EMU_DIAGAEN_DIAGA_GP_EN(self)
        self.zz_fdict['DIAGA_GP_EN'] = self.DIAGA_GP_EN
        self.DIAGA_RF_EN = RM_Field_EMU_DIAGAEN_DIAGA_RF_EN(self)
        self.zz_fdict['DIAGA_RF_EN'] = self.DIAGA_RF_EN
        self.DIAGPN_EN = RM_Field_EMU_DIAGAEN_DIAGPN_EN(self)
        self.zz_fdict['DIAGPN_EN'] = self.DIAGPN_EN
        self.ABUS_DIAGA_GP_EN = RM_Field_EMU_DIAGAEN_ABUS_DIAGA_GP_EN(self)
        self.zz_fdict['ABUS_DIAGA_GP_EN'] = self.ABUS_DIAGA_GP_EN
        self.ABUS_DIAGA_RF_EN = RM_Field_EMU_DIAGAEN_ABUS_DIAGA_RF_EN(self)
        self.zz_fdict['ABUS_DIAGA_RF_EN'] = self.ABUS_DIAGA_RF_EN
        self.DIAGPN_PADMUXEN = RM_Field_EMU_DIAGAEN_DIAGPN_PADMUXEN(self)
        self.zz_fdict['DIAGPN_PADMUXEN'] = self.DIAGPN_PADMUXEN
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DIAGABLKTPSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DIAGABLKTPSEL, self).__init__(rmio, label,
            0x400e3000, 0x3C4,
            'DIAGABLKTPSEL', 'EMU.DIAGABLKTPSEL', 'read-write',
            "",
            0x00000000, 0x1F0F3F0F)

        self.GPTP = RM_Field_EMU_DIAGABLKTPSEL_GPTP(self)
        self.zz_fdict['GPTP'] = self.GPTP
        self.GPBLK = RM_Field_EMU_DIAGABLKTPSEL_GPBLK(self)
        self.zz_fdict['GPBLK'] = self.GPBLK
        self.RFTP = RM_Field_EMU_DIAGABLKTPSEL_RFTP(self)
        self.zz_fdict['RFTP'] = self.RFTP
        self.RFBLK = RM_Field_EMU_DIAGABLKTPSEL_RFBLK(self)
        self.zz_fdict['RFBLK'] = self.RFBLK
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DIAGPNBLKSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DIAGPNBLKSEL, self).__init__(rmio, label,
            0x400e3000, 0x3C8,
            'DIAGPNBLKSEL', 'EMU.DIAGPNBLKSEL', 'read-write',
            "",
            0x00000000, 0x00000F00)

        self.PNRFBLK = RM_Field_EMU_DIAGPNBLKSEL_PNRFBLK(self)
        self.zz_fdict['PNRFBLK'] = self.PNRFBLK
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DIAGABRIDGESEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DIAGABRIDGESEL, self).__init__(rmio, label,
            0x400e3000, 0x3CC,
            'DIAGABRIDGESEL', 'EMU.DIAGABRIDGESEL', 'read-write',
            "",
            0x00000000, 0x80730033)

        self.ABUS_DIAGA_GP_SEL = RM_Field_EMU_DIAGABRIDGESEL_ABUS_DIAGA_GP_SEL(self)
        self.zz_fdict['ABUS_DIAGA_GP_SEL'] = self.ABUS_DIAGA_GP_SEL
        self.DIAGA_GP_BUF_EN = RM_Field_EMU_DIAGABRIDGESEL_DIAGA_GP_BUF_EN(self)
        self.zz_fdict['DIAGA_GP_BUF_EN'] = self.DIAGA_GP_BUF_EN
        self.DIAGA_GP_SHORT_N = RM_Field_EMU_DIAGABRIDGESEL_DIAGA_GP_SHORT_N(self)
        self.zz_fdict['DIAGA_GP_SHORT_N'] = self.DIAGA_GP_SHORT_N
        self.ABUS_DIAGA_RF_SEL = RM_Field_EMU_DIAGABRIDGESEL_ABUS_DIAGA_RF_SEL(self)
        self.zz_fdict['ABUS_DIAGA_RF_SEL'] = self.ABUS_DIAGA_RF_SEL
        self.DIAGA_RF_BUF_EN = RM_Field_EMU_DIAGABRIDGESEL_DIAGA_RF_BUF_EN(self)
        self.zz_fdict['DIAGA_RF_BUF_EN'] = self.DIAGA_RF_BUF_EN
        self.DIAGA_RF_SHORT_N = RM_Field_EMU_DIAGABRIDGESEL_DIAGA_RF_SHORT_N(self)
        self.zz_fdict['DIAGA_RF_SHORT_N'] = self.DIAGA_RF_SHORT_N
        self.DIAGPN_BUF_EN = RM_Field_EMU_DIAGABRIDGESEL_DIAGPN_BUF_EN(self)
        self.zz_fdict['DIAGPN_BUF_EN'] = self.DIAGPN_BUF_EN
        self.DIAGA_SEL_VDDX = RM_Field_EMU_DIAGABRIDGESEL_DIAGA_SEL_VDDX(self)
        self.zz_fdict['DIAGA_SEL_VDDX'] = self.DIAGA_SEL_VDDX
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_APDPGPIOSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_APDPGPIOSEL, self).__init__(rmio, label,
            0x400e3000, 0x3D0,
            'APDPGPIOSEL', 'EMU.APDPGPIOSEL', 'read-write',
            "",
            0x00000000, 0x0001FFFF)

        self.APORT_DP_GPIO_SEL = RM_Field_EMU_APDPGPIOSEL_APORT_DP_GPIO_SEL(self)
        self.zz_fdict['APORT_DP_GPIO_SEL'] = self.APORT_DP_GPIO_SEL
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_APDNGPIOSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_APDNGPIOSEL, self).__init__(rmio, label,
            0x400e3000, 0x3D4,
            'APDNGPIOSEL', 'EMU.APDNGPIOSEL', 'read-write',
            "",
            0x00000000, 0x0001FFFF)

        self.APORT_DN_GPIO_SEL = RM_Field_EMU_APDNGPIOSEL_APORT_DN_GPIO_SEL(self)
        self.zz_fdict['APORT_DN_GPIO_SEL'] = self.APORT_DN_GPIO_SEL
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_APAPGPIOSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_APAPGPIOSEL, self).__init__(rmio, label,
            0x400e3000, 0x3D8,
            'APAPGPIOSEL', 'EMU.APAPGPIOSEL', 'read-write',
            "",
            0x00000000, 0x0001FFFF)

        self.APORT_AP_GPIO_SEL = RM_Field_EMU_APAPGPIOSEL_APORT_AP_GPIO_SEL(self)
        self.zz_fdict['APORT_AP_GPIO_SEL'] = self.APORT_AP_GPIO_SEL
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_APANGPIOSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_APANGPIOSEL, self).__init__(rmio, label,
            0x400e3000, 0x3DC,
            'APANGPIOSEL', 'EMU.APANGPIOSEL', 'read-write',
            "",
            0x00000000, 0x0001FFFF)

        self.APORT_AN_GPIO_SEL = RM_Field_EMU_APANGPIOSEL_APORT_AN_GPIO_SEL(self)
        self.zz_fdict['APORT_AN_GPIO_SEL'] = self.APORT_AN_GPIO_SEL
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_APBPGPIOSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_APBPGPIOSEL, self).__init__(rmio, label,
            0x400e3000, 0x3E0,
            'APBPGPIOSEL', 'EMU.APBPGPIOSEL', 'read-write',
            "",
            0x00000000, 0x0001FFFF)

        self.APORT_BP_GPIO_SEL = RM_Field_EMU_APBPGPIOSEL_APORT_BP_GPIO_SEL(self)
        self.zz_fdict['APORT_BP_GPIO_SEL'] = self.APORT_BP_GPIO_SEL
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_APBNGPIOSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_APBNGPIOSEL, self).__init__(rmio, label,
            0x400e3000, 0x3E4,
            'APBNGPIOSEL', 'EMU.APBNGPIOSEL', 'read-write',
            "",
            0x00000000, 0x0001FFFF)

        self.APORT_BN_GPIO_SEL = RM_Field_EMU_APBNGPIOSEL_APORT_BN_GPIO_SEL(self)
        self.zz_fdict['APORT_BN_GPIO_SEL'] = self.APORT_BN_GPIO_SEL
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_APCPGPIOSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_APCPGPIOSEL, self).__init__(rmio, label,
            0x400e3000, 0x3E8,
            'APCPGPIOSEL', 'EMU.APCPGPIOSEL', 'read-write',
            "",
            0x00000000, 0x0001FFFF)

        self.APORT_CP_GPIO_SEL = RM_Field_EMU_APCPGPIOSEL_APORT_CP_GPIO_SEL(self)
        self.zz_fdict['APORT_CP_GPIO_SEL'] = self.APORT_CP_GPIO_SEL
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_APCNGPIOSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_APCNGPIOSEL, self).__init__(rmio, label,
            0x400e3000, 0x3EC,
            'APCNGPIOSEL', 'EMU.APCNGPIOSEL', 'read-write',
            "",
            0x00000000, 0x0001FFFF)

        self.APORT_CN_GPIO_SEL = RM_Field_EMU_APCNGPIOSEL_APORT_CN_GPIO_SEL(self)
        self.zz_fdict['APORT_CN_GPIO_SEL'] = self.APORT_CN_GPIO_SEL
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_EM2PERCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_EM2PERCTRL, self).__init__(rmio, label,
            0x400e3000, 0x3F0,
            'EM2PERCTRL', 'EMU.EM2PERCTRL', 'read-write',
            "",
            0x00000000, 0x0000000F)

        self.EM2PERPWDN = RM_Field_EMU_EM2PERCTRL_EM2PERPWDN(self)
        self.zz_fdict['EM2PERPWDN'] = self.EM2PERPWDN
        self.EM2PERPWUP = RM_Field_EMU_EM2PERCTRL_EM2PERPWUP(self)
        self.zz_fdict['EM2PERPWUP'] = self.EM2PERPWUP
        self.__dict__['zz_frozen'] = True


