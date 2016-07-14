
from static import Base_RM_Register
from EMU_field import *


class RM_Register_EMU_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_CTRL, self).__init__(rmio, label,
            0x400e3000, 0x000,
            'CTRL', 'EMU.CTRL', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.EM23VREG = RM_Field_EMU_CTRL_EM23VREG(self)
        self.zz_fdict['EM23VREG'] = self.EM23VREG
        self.EM2BLOCK = RM_Field_EMU_CTRL_EM2BLOCK(self)
        self.zz_fdict['EM2BLOCK'] = self.EM2BLOCK
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_STATUS, self).__init__(rmio, label,
            0x400e3000, 0x004,
            'STATUS', 'EMU.STATUS', 'read-only',
            "",
            0x00000000, 0x3210019F)

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
        self.VMONPAVDD = RM_Field_EMU_STATUS_VMONPAVDD(self)
        self.zz_fdict['VMONPAVDD'] = self.VMONPAVDD
        self.VMONFVDD = RM_Field_EMU_STATUS_VMONFVDD(self)
        self.zz_fdict['VMONFVDD'] = self.VMONFVDD
        self.EM4IO0RET = RM_Field_EMU_STATUS_EM4IO0RET(self)
        self.zz_fdict['EM4IO0RET'] = self.EM4IO0RET
        self.RACACTIVE = RM_Field_EMU_STATUS_RACACTIVE(self)
        self.zz_fdict['RACACTIVE'] = self.RACACTIVE
        self.CALACTIVE = RM_Field_EMU_STATUS_CALACTIVE(self)
        self.zz_fdict['CALACTIVE'] = self.CALACTIVE
        self.CALCOMPOUT = RM_Field_EMU_STATUS_CALCOMPOUT(self)
        self.zz_fdict['CALCOMPOUT'] = self.CALCOMPOUT
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


class RM_Register_EMU_MEMCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_MEMCTRL, self).__init__(rmio, label,
            0x400e3000, 0x00C,
            'MEMCTRL', 'EMU.MEMCTRL', 'read-write',
            "",
            0x00000000, 0x0000110F)

        self.RAMPOWERDOWN = RM_Field_EMU_MEMCTRL_RAMPOWERDOWN(self)
        self.zz_fdict['RAMPOWERDOWN'] = self.RAMPOWERDOWN
        self.RAMHPOWERDOWN = RM_Field_EMU_MEMCTRL_RAMHPOWERDOWN(self)
        self.zz_fdict['RAMHPOWERDOWN'] = self.RAMHPOWERDOWN
        self.SEQRAMPOWERDOWN = RM_Field_EMU_MEMCTRL_SEQRAMPOWERDOWN(self)
        self.zz_fdict['SEQRAMPOWERDOWN'] = self.SEQRAMPOWERDOWN
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_CMD, self).__init__(rmio, label,
            0x400e3000, 0x010,
            'CMD', 'EMU.CMD', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.EM4UNLATCH = RM_Field_EMU_CMD_EM4UNLATCH(self)
        self.zz_fdict['EM4UNLATCH'] = self.EM4UNLATCH
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
        self.EM4IO0RETMODE = RM_Field_EMU_EM4CTRL_EM4IO0RETMODE(self)
        self.zz_fdict['EM4IO0RETMODE'] = self.EM4IO0RETMODE
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
            0x00000000, 0xE11FF0FF)

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
        self.VMONPAVDDFALL = RM_Field_EMU_IF_VMONPAVDDFALL(self)
        self.zz_fdict['VMONPAVDDFALL'] = self.VMONPAVDDFALL
        self.VMONPAVDDRISE = RM_Field_EMU_IF_VMONPAVDDRISE(self)
        self.zz_fdict['VMONPAVDDRISE'] = self.VMONPAVDDRISE
        self.VMONFVDDFALL = RM_Field_EMU_IF_VMONFVDDFALL(self)
        self.zz_fdict['VMONFVDDFALL'] = self.VMONFVDDFALL
        self.VMONFVDDRISE = RM_Field_EMU_IF_VMONFVDDRISE(self)
        self.zz_fdict['VMONFVDDRISE'] = self.VMONFVDDRISE
        self.DCDCPFETUPDREQ = RM_Field_EMU_IF_DCDCPFETUPDREQ(self)
        self.zz_fdict['DCDCPFETUPDREQ'] = self.DCDCPFETUPDREQ
        self.DCDCNFETUPDREQ = RM_Field_EMU_IF_DCDCNFETUPDREQ(self)
        self.zz_fdict['DCDCNFETUPDREQ'] = self.DCDCNFETUPDREQ
        self.DCDCLPRUNNING = RM_Field_EMU_IF_DCDCLPRUNNING(self)
        self.zz_fdict['DCDCLPRUNNING'] = self.DCDCLPRUNNING
        self.DCDCLNRUNNING = RM_Field_EMU_IF_DCDCLNRUNNING(self)
        self.zz_fdict['DCDCLNRUNNING'] = self.DCDCLNRUNNING
        self.DCDCINBYPASS = RM_Field_EMU_IF_DCDCINBYPASS(self)
        self.zz_fdict['DCDCINBYPASS'] = self.DCDCINBYPASS
        self.EM23WAKEUP = RM_Field_EMU_IF_EM23WAKEUP(self)
        self.zz_fdict['EM23WAKEUP'] = self.EM23WAKEUP
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
            0x00000000, 0xE11FF0FF)

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
        self.VMONPAVDDFALL = RM_Field_EMU_IFS_VMONPAVDDFALL(self)
        self.zz_fdict['VMONPAVDDFALL'] = self.VMONPAVDDFALL
        self.VMONPAVDDRISE = RM_Field_EMU_IFS_VMONPAVDDRISE(self)
        self.zz_fdict['VMONPAVDDRISE'] = self.VMONPAVDDRISE
        self.VMONFVDDFALL = RM_Field_EMU_IFS_VMONFVDDFALL(self)
        self.zz_fdict['VMONFVDDFALL'] = self.VMONFVDDFALL
        self.VMONFVDDRISE = RM_Field_EMU_IFS_VMONFVDDRISE(self)
        self.zz_fdict['VMONFVDDRISE'] = self.VMONFVDDRISE
        self.DCDCPFETUPDREQ = RM_Field_EMU_IFS_DCDCPFETUPDREQ(self)
        self.zz_fdict['DCDCPFETUPDREQ'] = self.DCDCPFETUPDREQ
        self.DCDCNFETUPDREQ = RM_Field_EMU_IFS_DCDCNFETUPDREQ(self)
        self.zz_fdict['DCDCNFETUPDREQ'] = self.DCDCNFETUPDREQ
        self.DCDCLPRUNNING = RM_Field_EMU_IFS_DCDCLPRUNNING(self)
        self.zz_fdict['DCDCLPRUNNING'] = self.DCDCLPRUNNING
        self.DCDCLNRUNNING = RM_Field_EMU_IFS_DCDCLNRUNNING(self)
        self.zz_fdict['DCDCLNRUNNING'] = self.DCDCLNRUNNING
        self.DCDCINBYPASS = RM_Field_EMU_IFS_DCDCINBYPASS(self)
        self.zz_fdict['DCDCINBYPASS'] = self.DCDCINBYPASS
        self.EM23WAKEUP = RM_Field_EMU_IFS_EM23WAKEUP(self)
        self.zz_fdict['EM23WAKEUP'] = self.EM23WAKEUP
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
            0x00000000, 0xE11FF0FF)

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
        self.VMONPAVDDFALL = RM_Field_EMU_IFC_VMONPAVDDFALL(self)
        self.zz_fdict['VMONPAVDDFALL'] = self.VMONPAVDDFALL
        self.VMONPAVDDRISE = RM_Field_EMU_IFC_VMONPAVDDRISE(self)
        self.zz_fdict['VMONPAVDDRISE'] = self.VMONPAVDDRISE
        self.VMONFVDDFALL = RM_Field_EMU_IFC_VMONFVDDFALL(self)
        self.zz_fdict['VMONFVDDFALL'] = self.VMONFVDDFALL
        self.VMONFVDDRISE = RM_Field_EMU_IFC_VMONFVDDRISE(self)
        self.zz_fdict['VMONFVDDRISE'] = self.VMONFVDDRISE
        self.DCDCPFETUPDREQ = RM_Field_EMU_IFC_DCDCPFETUPDREQ(self)
        self.zz_fdict['DCDCPFETUPDREQ'] = self.DCDCPFETUPDREQ
        self.DCDCNFETUPDREQ = RM_Field_EMU_IFC_DCDCNFETUPDREQ(self)
        self.zz_fdict['DCDCNFETUPDREQ'] = self.DCDCNFETUPDREQ
        self.DCDCLPRUNNING = RM_Field_EMU_IFC_DCDCLPRUNNING(self)
        self.zz_fdict['DCDCLPRUNNING'] = self.DCDCLPRUNNING
        self.DCDCLNRUNNING = RM_Field_EMU_IFC_DCDCLNRUNNING(self)
        self.zz_fdict['DCDCLNRUNNING'] = self.DCDCLNRUNNING
        self.DCDCINBYPASS = RM_Field_EMU_IFC_DCDCINBYPASS(self)
        self.zz_fdict['DCDCINBYPASS'] = self.DCDCINBYPASS
        self.EM23WAKEUP = RM_Field_EMU_IFC_EM23WAKEUP(self)
        self.zz_fdict['EM23WAKEUP'] = self.EM23WAKEUP
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
            0x00000000, 0xE11FF0FF)

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
        self.VMONPAVDDFALL = RM_Field_EMU_IEN_VMONPAVDDFALL(self)
        self.zz_fdict['VMONPAVDDFALL'] = self.VMONPAVDDFALL
        self.VMONPAVDDRISE = RM_Field_EMU_IEN_VMONPAVDDRISE(self)
        self.zz_fdict['VMONPAVDDRISE'] = self.VMONPAVDDRISE
        self.VMONFVDDFALL = RM_Field_EMU_IEN_VMONFVDDFALL(self)
        self.zz_fdict['VMONFVDDFALL'] = self.VMONFVDDFALL
        self.VMONFVDDRISE = RM_Field_EMU_IEN_VMONFVDDRISE(self)
        self.zz_fdict['VMONFVDDRISE'] = self.VMONFVDDRISE
        self.DCDCPFETUPDREQ = RM_Field_EMU_IEN_DCDCPFETUPDREQ(self)
        self.zz_fdict['DCDCPFETUPDREQ'] = self.DCDCPFETUPDREQ
        self.DCDCNFETUPDREQ = RM_Field_EMU_IEN_DCDCNFETUPDREQ(self)
        self.zz_fdict['DCDCNFETUPDREQ'] = self.DCDCNFETUPDREQ
        self.DCDCLPRUNNING = RM_Field_EMU_IEN_DCDCLPRUNNING(self)
        self.zz_fdict['DCDCLPRUNNING'] = self.DCDCLPRUNNING
        self.DCDCLNRUNNING = RM_Field_EMU_IEN_DCDCLNRUNNING(self)
        self.zz_fdict['DCDCLNRUNNING'] = self.DCDCLNRUNNING
        self.DCDCINBYPASS = RM_Field_EMU_IEN_DCDCINBYPASS(self)
        self.zz_fdict['DCDCINBYPASS'] = self.DCDCINBYPASS
        self.EM23WAKEUP = RM_Field_EMU_IEN_EM23WAKEUP(self)
        self.zz_fdict['EM23WAKEUP'] = self.EM23WAKEUP
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
            0x00000000, 0x00038360)

        self.ANASW = RM_Field_EMU_PWRCTRL_ANASW(self)
        self.zz_fdict['ANASW'] = self.ANASW
        self.REGDIS = RM_Field_EMU_PWRCTRL_REGDIS(self)
        self.zz_fdict['REGDIS'] = self.REGDIS
        self.DCDCPWRSEL = RM_Field_EMU_PWRCTRL_DCDCPWRSEL(self)
        self.zz_fdict['DCDCPWRSEL'] = self.DCDCPWRSEL
        self.DCDCVREGSEL = RM_Field_EMU_PWRCTRL_DCDCVREGSEL(self)
        self.zz_fdict['DCDCVREGSEL'] = self.DCDCVREGSEL
        self.PROBE = RM_Field_EMU_PWRCTRL_PROBE(self)
        self.zz_fdict['PROBE'] = self.PROBE
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCCTRL, self).__init__(rmio, label,
            0x400e3000, 0x040,
            'DCDCCTRL', 'EMU.DCDCCTRL', 'read-write',
            "",
            0x00000030, 0x000001F3)

        self.DCDCMODE = RM_Field_EMU_DCDCCTRL_DCDCMODE(self)
        self.zz_fdict['DCDCMODE'] = self.DCDCMODE
        self.DCDCMODEEM23 = RM_Field_EMU_DCDCCTRL_DCDCMODEEM23(self)
        self.zz_fdict['DCDCMODEEM23'] = self.DCDCMODEEM23
        self.DCDCMODEEM4 = RM_Field_EMU_DCDCCTRL_DCDCMODEEM4(self)
        self.zz_fdict['DCDCMODEEM4'] = self.DCDCMODEEM4
        self.LPSTANDBY = RM_Field_EMU_DCDCCTRL_LPSTANDBY(self)
        self.zz_fdict['LPSTANDBY'] = self.LPSTANDBY
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
            0x00000000, 0x00000001)

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
            0x33307700, 0x377FFF1F)

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
        self.PSLICESEL = RM_Field_EMU_DCDCMISCCTRL_PSLICESEL(self)
        self.zz_fdict['PSLICESEL'] = self.PSLICESEL
        self.NSLICESEL = RM_Field_EMU_DCDCMISCCTRL_NSLICESEL(self)
        self.zz_fdict['NSLICESEL'] = self.NSLICESEL
        self.BYPLIMSEL = RM_Field_EMU_DCDCMISCCTRL_BYPLIMSEL(self)
        self.zz_fdict['BYPLIMSEL'] = self.BYPLIMSEL
        self.LPCLIMILIMSEL = RM_Field_EMU_DCDCMISCCTRL_LPCLIMILIMSEL(self)
        self.zz_fdict['LPCLIMILIMSEL'] = self.LPCLIMILIMSEL
        self.LNCLIMILIMSEL = RM_Field_EMU_DCDCMISCCTRL_LNCLIMILIMSEL(self)
        self.zz_fdict['LNCLIMILIMSEL'] = self.LNCLIMILIMSEL
        self.LPCMPBIAS = RM_Field_EMU_DCDCMISCCTRL_LPCMPBIAS(self)
        self.zz_fdict['LPCMPBIAS'] = self.LPCMPBIAS
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DCDCZDETCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DCDCZDETCTRL, self).__init__(rmio, label,
            0x400e3000, 0x050,
            'DCDCZDETCTRL', 'EMU.DCDCZDETCTRL', 'read-write',
            "",
            0x00000130, 0x00000371)

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
            0x00002100, 0x00002301)

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
            0x0FF1F8FF, 0x7FF1F8FF)

        self.LPINITWAIT = RM_Field_EMU_DCDCTIMING_LPINITWAIT(self)
        self.zz_fdict['LPINITWAIT'] = self.LPINITWAIT
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
            0x00007000, 0x0703F000)

        self.LPCMPHYSSEL = RM_Field_EMU_DCDCLPCTRL_LPCMPHYSSEL(self)
        self.zz_fdict['LPCMPHYSSEL'] = self.LPCMPHYSSEL
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
            0x00000909, 0xC0001F0F)

        self.ZDETBIASTRIM = RM_Field_EMU_DCDCTRIM1_ZDETBIASTRIM(self)
        self.zz_fdict['ZDETBIASTRIM'] = self.ZDETBIASTRIM
        self.ZDET0XTRIM = RM_Field_EMU_DCDCTRIM1_ZDET0XTRIM(self)
        self.zz_fdict['ZDET0XTRIM'] = self.ZDET0XTRIM
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


class RM_Register_EMU_VMONPAVDDCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_VMONPAVDDCTRL, self).__init__(rmio, label,
            0x400e3000, 0x0A8,
            'VMONPAVDDCTRL', 'EMU.VMONPAVDDCTRL', 'read-write',
            "",
            0x00000000, 0x0000FF0D)

        self.EN = RM_Field_EMU_VMONPAVDDCTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.RISEWU = RM_Field_EMU_VMONPAVDDCTRL_RISEWU(self)
        self.zz_fdict['RISEWU'] = self.RISEWU
        self.FALLWU = RM_Field_EMU_VMONPAVDDCTRL_FALLWU(self)
        self.zz_fdict['FALLWU'] = self.FALLWU
        self.THRESFINE = RM_Field_EMU_VMONPAVDDCTRL_THRESFINE(self)
        self.zz_fdict['THRESFINE'] = self.THRESFINE
        self.THRESCOARSE = RM_Field_EMU_VMONPAVDDCTRL_THRESCOARSE(self)
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
            0xC9082C43, 0xFFFF3CFF)

        self.PORBOD_REFTRIM = RM_Field_EMU_PORBOD_PORBOD_REFTRIM(self)
        self.zz_fdict['PORBOD_REFTRIM'] = self.PORBOD_REFTRIM
        self.PORBOD_SEL_IVBGR_FOR_VREF = RM_Field_EMU_PORBOD_PORBOD_SEL_IVBGR_FOR_VREF(self)
        self.zz_fdict['PORBOD_SEL_IVBGR_FOR_VREF'] = self.PORBOD_SEL_IVBGR_FOR_VREF
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
            0x00800000, 0xEFFEDFFF)

        self.PORBOD_AVDD_BOD_TRIM = RM_Field_EMU_BODCONF_PORBOD_AVDD_BOD_TRIM(self)
        self.zz_fdict['PORBOD_AVDD_BOD_TRIM'] = self.PORBOD_AVDD_BOD_TRIM
        self.PORBOD_AVDD_EM4BOD_TRIM = RM_Field_EMU_BODCONF_PORBOD_AVDD_EM4BOD_TRIM(self)
        self.zz_fdict['PORBOD_AVDD_EM4BOD_TRIM'] = self.PORBOD_AVDD_EM4BOD_TRIM
        self.PORBOD_AVDD_GL_CURR = RM_Field_EMU_BODCONF_PORBOD_AVDD_GL_CURR(self)
        self.zz_fdict['PORBOD_AVDD_GL_CURR'] = self.PORBOD_AVDD_GL_CURR
        self.PORBOD_AVDD_GL_RC = RM_Field_EMU_BODCONF_PORBOD_AVDD_GL_RC(self)
        self.zz_fdict['PORBOD_AVDD_GL_RC'] = self.PORBOD_AVDD_GL_RC
        self.PORBOD_AVDD_GL_THR = RM_Field_EMU_BODCONF_PORBOD_AVDD_GL_THR(self)
        self.zz_fdict['PORBOD_AVDD_GL_THR'] = self.PORBOD_AVDD_GL_THR
        self.PORBOD_DVDD_BOD_TRIM = RM_Field_EMU_BODCONF_PORBOD_DVDD_BOD_TRIM(self)
        self.zz_fdict['PORBOD_DVDD_BOD_TRIM'] = self.PORBOD_DVDD_BOD_TRIM
        self.PORBOD_DVDD_GL_CURR = RM_Field_EMU_BODCONF_PORBOD_DVDD_GL_CURR(self)
        self.zz_fdict['PORBOD_DVDD_GL_CURR'] = self.PORBOD_DVDD_GL_CURR
        self.PORBOD_DVDD_GL_RC = RM_Field_EMU_BODCONF_PORBOD_DVDD_GL_RC(self)
        self.zz_fdict['PORBOD_DVDD_GL_RC'] = self.PORBOD_DVDD_GL_RC
        self.PORBOD_DVDD_GL_THR = RM_Field_EMU_BODCONF_PORBOD_DVDD_GL_THR(self)
        self.zz_fdict['PORBOD_DVDD_GL_THR'] = self.PORBOD_DVDD_GL_THR
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
            0x00000100, 0x018F03F0)

        self.PORBOD_FLASH_BOD_TRIM = RM_Field_EMU_FLASHBOD_PORBOD_FLASH_BOD_TRIM(self)
        self.zz_fdict['PORBOD_FLASH_BOD_TRIM'] = self.PORBOD_FLASH_BOD_TRIM
        self.PORBOD_FLASH_BOD_THR = RM_Field_EMU_FLASHBOD_PORBOD_FLASH_BOD_THR(self)
        self.zz_fdict['PORBOD_FLASH_BOD_THR'] = self.PORBOD_FLASH_BOD_THR
        self.PORBOD_FLASH_GL_CURR = RM_Field_EMU_FLASHBOD_PORBOD_FLASH_GL_CURR(self)
        self.zz_fdict['PORBOD_FLASH_GL_CURR'] = self.PORBOD_FLASH_GL_CURR
        self.PORBOD_FLASH_GL_RC = RM_Field_EMU_FLASHBOD_PORBOD_FLASH_GL_RC(self)
        self.zz_fdict['PORBOD_FLASH_GL_RC'] = self.PORBOD_FLASH_GL_RC
        self.PORBOD_FLASH_GL_THR = RM_Field_EMU_FLASHBOD_PORBOD_FLASH_GL_THR(self)
        self.zz_fdict['PORBOD_FLASH_GL_THR'] = self.PORBOD_FLASH_GL_THR
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DECBOD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DECBOD, self).__init__(rmio, label,
            0x400e3000, 0x160,
            'DECBOD', 'EMU.DECBOD', 'read-write',
            "",
            0x00240024, 0x1FBF1FBF)

        self.PORBOD_DEC0_BOD_TRIM = RM_Field_EMU_DECBOD_PORBOD_DEC0_BOD_TRIM(self)
        self.zz_fdict['PORBOD_DEC0_BOD_TRIM'] = self.PORBOD_DEC0_BOD_TRIM
        self.PORBOD_DEC0_BOD_THR = RM_Field_EMU_DECBOD_PORBOD_DEC0_BOD_THR(self)
        self.zz_fdict['PORBOD_DEC0_BOD_THR'] = self.PORBOD_DEC0_BOD_THR
        self.PORBOD_DEC0_GL_CURR = RM_Field_EMU_DECBOD_PORBOD_DEC0_GL_CURR(self)
        self.zz_fdict['PORBOD_DEC0_GL_CURR'] = self.PORBOD_DEC0_GL_CURR
        self.PORBOD_DEC0_GL_RC = RM_Field_EMU_DECBOD_PORBOD_DEC0_GL_RC(self)
        self.zz_fdict['PORBOD_DEC0_GL_RC'] = self.PORBOD_DEC0_GL_RC
        self.PORBOD_DEC0_GL_THR = RM_Field_EMU_DECBOD_PORBOD_DEC0_GL_THR(self)
        self.zz_fdict['PORBOD_DEC0_GL_THR'] = self.PORBOD_DEC0_GL_THR
        self.PORBOD_DEC1_BOD_TRIM = RM_Field_EMU_DECBOD_PORBOD_DEC1_BOD_TRIM(self)
        self.zz_fdict['PORBOD_DEC1_BOD_TRIM'] = self.PORBOD_DEC1_BOD_TRIM
        self.PORBOD_DEC1_BOD_THR = RM_Field_EMU_DECBOD_PORBOD_DEC1_BOD_THR(self)
        self.zz_fdict['PORBOD_DEC1_BOD_THR'] = self.PORBOD_DEC1_BOD_THR
        self.PORBOD_DEC1_GL_CURR = RM_Field_EMU_DECBOD_PORBOD_DEC1_GL_CURR(self)
        self.zz_fdict['PORBOD_DEC1_GL_CURR'] = self.PORBOD_DEC1_GL_CURR
        self.PORBOD_DEC1_GL_RC = RM_Field_EMU_DECBOD_PORBOD_DEC1_GL_RC(self)
        self.zz_fdict['PORBOD_DEC1_GL_RC'] = self.PORBOD_DEC1_GL_RC
        self.PORBOD_DEC1_GL_THR = RM_Field_EMU_DECBOD_PORBOD_DEC1_GL_THR(self)
        self.zz_fdict['PORBOD_DEC1_GL_THR'] = self.PORBOD_DEC1_GL_THR
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_BIASCONF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_BIASCONF, self).__init__(rmio, label,
            0x400e3000, 0x164,
            'BIASCONF', 'EMU.BIASCONF', 'read-write',
            "",
            0x000000F8, 0x000003FF)

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
            0x00C00008, 0x01F003FF)

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
            0x00000419, 0x00000C3F)

        self.HDREG_TRIM_VREG = RM_Field_EMU_DREGCALIB_HDREG_TRIM_VREG(self)
        self.zz_fdict['HDREG_TRIM_VREG'] = self.HDREG_TRIM_VREG
        self.HDREG_TRIM_ISRC_CINT = RM_Field_EMU_DREGCALIB_HDREG_TRIM_ISRC_CINT(self)
        self.zz_fdict['HDREG_TRIM_ISRC_CINT'] = self.HDREG_TRIM_ISRC_CINT
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_DREGOVERRIDE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_DREGOVERRIDE, self).__init__(rmio, label,
            0x400e3000, 0x17C,
            'DREGOVERRIDE', 'EMU.DREGOVERRIDE', 'read-write',
            "",
            0x00000000, 0x000003FF)

        self.LDREG_OVERRIDE_EN = RM_Field_EMU_DREGOVERRIDE_LDREG_OVERRIDE_EN(self)
        self.zz_fdict['LDREG_OVERRIDE_EN'] = self.LDREG_OVERRIDE_EN
        self.OVR_LDREG_SEL_VDDX_DREG = RM_Field_EMU_DREGOVERRIDE_OVR_LDREG_SEL_VDDX_DREG(self)
        self.zz_fdict['OVR_LDREG_SEL_VDDX_DREG'] = self.OVR_LDREG_SEL_VDDX_DREG
        self.OVR_LDREG_EN_PD0SW = RM_Field_EMU_DREGOVERRIDE_OVR_LDREG_EN_PD0SW(self)
        self.zz_fdict['OVR_LDREG_EN_PD0SW'] = self.OVR_LDREG_EN_PD0SW
        self.OVR_LDREG_EN_LDREG = RM_Field_EMU_DREGOVERRIDE_OVR_LDREG_EN_LDREG(self)
        self.zz_fdict['OVR_LDREG_EN_LDREG'] = self.OVR_LDREG_EN_LDREG
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


class RM_Register_EMU_MEMFEATURE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_MEMFEATURE, self).__init__(rmio, label,
            0x400e3000, 0x180,
            'MEMFEATURE', 'EMU.MEMFEATURE', 'write-only',
            "",
            0x111F0000, 0x111F4300)

        self.RAM0DIV = RM_Field_EMU_MEMFEATURE_RAM0DIV(self)
        self.zz_fdict['RAM0DIV'] = self.RAM0DIV
        self.RAMPOWDOWNLOCK = RM_Field_EMU_MEMFEATURE_RAMPOWDOWNLOCK(self)
        self.zz_fdict['RAMPOWDOWNLOCK'] = self.RAMPOWDOWNLOCK
        self.RAMSIZE = RM_Field_EMU_MEMFEATURE_RAMSIZE(self)
        self.zz_fdict['RAMSIZE'] = self.RAMSIZE
        self.FRCRAMEN = RM_Field_EMU_MEMFEATURE_FRCRAMEN(self)
        self.zz_fdict['FRCRAMEN'] = self.FRCRAMEN
        self.SEQRAMEN = RM_Field_EMU_MEMFEATURE_SEQRAMEN(self)
        self.zz_fdict['SEQRAMEN'] = self.SEQRAMEN
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
            0x000002FF, 0x07FF07FF)

        self.EM4SPORDELAY = RM_Field_EMU_STATEDLY1_EM4SPORDELAY(self)
        self.zz_fdict['EM4SPORDELAY'] = self.EM4SPORDELAY
        self.SETTLINGDELAY = RM_Field_EMU_STATEDLY1_SETTLINGDELAY(self)
        self.zz_fdict['SETTLINGDELAY'] = self.SETTLINGDELAY
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
            0x00000000, 0xFF1F1F81)

        self.EXPORT_RESET = RM_Field_EMU_TESTCTRL_EXPORT_RESET(self)
        self.zz_fdict['EXPORT_RESET'] = self.EXPORT_RESET
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
            0x00000000, 0xC0007FEE)

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
        self.ISO_RADIO = RM_Field_EMU_TESTCTRLANAISO_ISO_RADIO(self)
        self.zz_fdict['ISO_RADIO'] = self.ISO_RADIO
        self.ISO_LVDS = RM_Field_EMU_TESTCTRLANAISO_ISO_LVDS(self)
        self.zz_fdict['ISO_LVDS'] = self.ISO_LVDS
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_MBISTCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_MBISTCTRL, self).__init__(rmio, label,
            0x400e3000, 0x3AC,
            'MBISTCTRL', 'EMU.MBISTCTRL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MBIST_CONFIG = RM_Field_EMU_MBISTCTRL_MBIST_CONFIG(self)
        self.zz_fdict['MBIST_CONFIG'] = self.MBIST_CONFIG
        self.__dict__['zz_frozen'] = True


class RM_Register_EMU_MBISTSTATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_EMU_MBISTSTATUS, self).__init__(rmio, label,
            0x400e3000, 0x3B0,
            'MBISTSTATUS', 'EMU.MBISTSTATUS', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MBIST_STATUS = RM_Field_EMU_MBISTSTATUS_MBIST_STATUS(self)
        self.zz_fdict['MBIST_STATUS'] = self.MBIST_STATUS
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
            0x00000000, 0x1F0F1F0F)

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


