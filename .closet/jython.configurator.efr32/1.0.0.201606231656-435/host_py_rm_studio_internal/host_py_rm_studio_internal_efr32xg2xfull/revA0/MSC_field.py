
from static import Base_RM_Field
from MSC_enum import *


class RM_Field_MSC_CTRL_ADDRFAULTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CTRL_ADDRFAULTEN, self).__init__(register,
            'ADDRFAULTEN', 'MSC.CTRL.ADDRFAULTEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CTRL_CLKDISFAULTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CTRL_CLKDISFAULTEN, self).__init__(register,
            'CLKDISFAULTEN', 'MSC.CTRL.CLKDISFAULTEN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CTRL_PWRUPONDEMAND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CTRL_PWRUPONDEMAND, self).__init__(register,
            'PWRUPONDEMAND', 'MSC.CTRL.PWRUPONDEMAND', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CTRL_IFCREADCLEAR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CTRL_IFCREADCLEAR, self).__init__(register,
            'IFCREADCLEAR', 'MSC.CTRL.IFCREADCLEAR', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CTRL_TIMEOUTFAULTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CTRL_TIMEOUTFAULTEN, self).__init__(register,
            'TIMEOUTFAULTEN', 'MSC.CTRL.TIMEOUTFAULTEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CTRL_BYPASSAHBCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CTRL_BYPASSAHBCNT, self).__init__(register,
            'BYPASSAHBCNT', 'MSC.CTRL.BYPASSAHBCNT', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_READCTRL_IFCDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_READCTRL_IFCDIS, self).__init__(register,
            'IFCDIS', 'MSC.READCTRL.IFCDIS', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_READCTRL_AIDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_READCTRL_AIDIS, self).__init__(register,
            'AIDIS', 'MSC.READCTRL.AIDIS', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_READCTRL_ICCDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_READCTRL_ICCDIS, self).__init__(register,
            'ICCDIS', 'MSC.READCTRL.ICCDIS', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_READCTRL_PREFETCH(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_READCTRL_PREFETCH, self).__init__(register,
            'PREFETCH', 'MSC.READCTRL.PREFETCH', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_READCTRL_USEHPROT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_READCTRL_USEHPROT, self).__init__(register,
            'USEHPROT', 'MSC.READCTRL.USEHPROT', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_READCTRL_MODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_READCTRL_MODE, self).__init__(register,
            'MODE', 'MSC.READCTRL.MODE', 'read-write',
            "",
            24, 2,
            RM_Enum_MSC_READCTRL_MODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_READCTRL_SCBTP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_READCTRL_SCBTP, self).__init__(register,
            'SCBTP', 'MSC.READCTRL.SCBTP', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECTRL_WREN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECTRL_WREN, self).__init__(register,
            'WREN', 'MSC.WRITECTRL.WREN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECTRL_IRQERASEABORT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECTRL_IRQERASEABORT, self).__init__(register,
            'IRQERASEABORT', 'MSC.WRITECTRL.IRQERASEABORT', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECTRL_WDOUBLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECTRL_WDOUBLE, self).__init__(register,
            'WDOUBLE', 'MSC.WRITECTRL.WDOUBLE', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECTRL_LPWRITE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECTRL_LPWRITE, self).__init__(register,
            'LPWRITE', 'MSC.WRITECTRL.LPWRITE', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECTRL_LPERASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECTRL_LPERASE, self).__init__(register,
            'LPERASE', 'MSC.WRITECTRL.LPERASE', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECTRL_RWWEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECTRL_RWWEN, self).__init__(register,
            'RWWEN', 'MSC.WRITECTRL.RWWEN', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECMD_LADDRIM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECMD_LADDRIM, self).__init__(register,
            'LADDRIM', 'MSC.WRITECMD.LADDRIM', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECMD_ERASEPAGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECMD_ERASEPAGE, self).__init__(register,
            'ERASEPAGE', 'MSC.WRITECMD.ERASEPAGE', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECMD_WRITEEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECMD_WRITEEND, self).__init__(register,
            'WRITEEND', 'MSC.WRITECMD.WRITEEND', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECMD_WRITEONCE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECMD_WRITEONCE, self).__init__(register,
            'WRITEONCE', 'MSC.WRITECMD.WRITEONCE', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECMD_WRITETRIG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECMD_WRITETRIG, self).__init__(register,
            'WRITETRIG', 'MSC.WRITECMD.WRITETRIG', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECMD_ERASEABORT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECMD_ERASEABORT, self).__init__(register,
            'ERASEABORT', 'MSC.WRITECMD.ERASEABORT', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECMD_ERASEMAIN0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECMD_ERASEMAIN0, self).__init__(register,
            'ERASEMAIN0', 'MSC.WRITECMD.ERASEMAIN0', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECMD_ERASEMAIN1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECMD_ERASEMAIN1, self).__init__(register,
            'ERASEMAIN1', 'MSC.WRITECMD.ERASEMAIN1', 'write-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WRITECMD_CLEARWDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WRITECMD_CLEARWDATA, self).__init__(register,
            'CLEARWDATA', 'MSC.WRITECMD.CLEARWDATA', 'write-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_ADDRB_ADDRB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_ADDRB_ADDRB, self).__init__(register,
            'ADDRB', 'MSC.ADDRB.ADDRB', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_WDATA_WDATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_WDATA_WDATA, self).__init__(register,
            'WDATA', 'MSC.WDATA.WDATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STATUS_BUSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STATUS_BUSY, self).__init__(register,
            'BUSY', 'MSC.STATUS.BUSY', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STATUS_LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STATUS_LOCKED, self).__init__(register,
            'LOCKED', 'MSC.STATUS.LOCKED', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STATUS_INVADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STATUS_INVADDR, self).__init__(register,
            'INVADDR', 'MSC.STATUS.INVADDR', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STATUS_WDATAREADY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STATUS_WDATAREADY, self).__init__(register,
            'WDATAREADY', 'MSC.STATUS.WDATAREADY', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STATUS_WORDTIMEOUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STATUS_WORDTIMEOUT, self).__init__(register,
            'WORDTIMEOUT', 'MSC.STATUS.WORDTIMEOUT', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STATUS_ERASEABORTED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STATUS_ERASEABORTED, self).__init__(register,
            'ERASEABORTED', 'MSC.STATUS.ERASEABORTED', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STATUS_PCRUNNING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STATUS_PCRUNNING, self).__init__(register,
            'PCRUNNING', 'MSC.STATUS.PCRUNNING', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STATUS_BANKSWITCHED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STATUS_BANKSWITCHED, self).__init__(register,
            'BANKSWITCHED', 'MSC.STATUS.BANKSWITCHED', 'read-only',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STATUS_WDATAVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STATUS_WDATAVALID, self).__init__(register,
            'WDATAVALID', 'MSC.STATUS.WDATAVALID', 'read-only',
            "",
            24, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STATUS_PWRUPCKBDFAILCOUNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STATUS_PWRUPCKBDFAILCOUNT, self).__init__(register,
            'PWRUPCKBDFAILCOUNT', 'MSC.STATUS.PWRUPCKBDFAILCOUNT', 'read-only',
            "",
            28, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MEMFEATURE_FLASHSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MEMFEATURE_FLASHSIZE, self).__init__(register,
            'FLASHSIZE', 'MSC.MEMFEATURE.FLASHSIZE', 'write-only',
            "",
            0, 4,
            RM_Enum_MSC_MEMFEATURE_FLASHSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MEMFEATURE_MPUPRESENT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MEMFEATURE_MPUPRESENT, self).__init__(register,
            'MPUPRESENT', 'MSC.MEMFEATURE.MPUPRESENT', 'write-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MEMFEATURE_CACHERAMIFDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MEMFEATURE_CACHERAMIFDIS, self).__init__(register,
            'CACHERAMIFDIS', 'MSC.MEMFEATURE.CACHERAMIFDIS', 'write-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MEMFEATURE_INTERLEAVE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MEMFEATURE_INTERLEAVE, self).__init__(register,
            'INTERLEAVE', 'MSC.MEMFEATURE.INTERLEAVE', 'write-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MEMFEATURE_FLASHRWWMERGE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MEMFEATURE_FLASHRWWMERGE, self).__init__(register,
            'FLASHRWWMERGE', 'MSC.MEMFEATURE.FLASHRWWMERGE', 'write-only',
            "",
            20, 2,
            RM_Enum_MSC_MEMFEATURE_FLASHRWWMERGE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MEMFEATURE_USEUPPERHALF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MEMFEATURE_USEUPPERHALF, self).__init__(register,
            'USEUPPERHALF', 'MSC.MEMFEATURE.USEUPPERHALF', 'write-only',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MEMFEATURE_SELECTM3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MEMFEATURE_SELECTM3, self).__init__(register,
            'SELECTM3', 'MSC.MEMFEATURE.SELECTM3', 'write-only',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MEMFEATURE_FPUDISABLE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MEMFEATURE_FPUDISABLE, self).__init__(register,
            'FPUDISABLE', 'MSC.MEMFEATURE.FPUDISABLE', 'write-only',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MEMFEATURE_BOOTLOADERBYPASS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MEMFEATURE_BOOTLOADERBYPASS, self).__init__(register,
            'BOOTLOADERBYPASS', 'MSC.MEMFEATURE.BOOTLOADERBYPASS', 'write-only',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MEMFEATURE_BANKSWITCHING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MEMFEATURE_BANKSWITCHING, self).__init__(register,
            'BANKSWITCHING', 'MSC.MEMFEATURE.BANKSWITCHING', 'write-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MEMFEATURE_INTERLEAVEDISPOL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MEMFEATURE_INTERLEAVEDISPOL, self).__init__(register,
            'INTERLEAVEDISPOL', 'MSC.MEMFEATURE.INTERLEAVEDISPOL', 'write-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CFGFEATURE_CFGLOCKEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CFGFEATURE_CFGLOCKEN, self).__init__(register,
            'CFGLOCKEN', 'MSC.CFGFEATURE.CFGLOCKEN', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_DEBUGLOCK_DEBUGEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_DEBUGLOCK_DEBUGEN, self).__init__(register,
            'DEBUGEN', 'MSC.DEBUGLOCK.DEBUGEN', 'write-only',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_AAPLOCK_AAPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_AAPLOCK_AAPEN, self).__init__(register,
            'AAPEN', 'MSC.AAPLOCK.AAPEN', 'write-only',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_AAPLOCK_SWUNLOCKAAPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_AAPLOCK_SWUNLOCKAAPEN, self).__init__(register,
            'SWUNLOCKAAPEN', 'MSC.AAPLOCK.SWUNLOCKAAPEN', 'write-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IF_ERASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IF_ERASE, self).__init__(register,
            'ERASE', 'MSC.IF.ERASE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IF_WRITE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IF_WRITE, self).__init__(register,
            'WRITE', 'MSC.IF.WRITE', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IF_CHOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IF_CHOF, self).__init__(register,
            'CHOF', 'MSC.IF.CHOF', 'read-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IF_CMOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IF_CMOF, self).__init__(register,
            'CMOF', 'MSC.IF.CMOF', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IF_PWRUPF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IF_PWRUPF, self).__init__(register,
            'PWRUPF', 'MSC.IF.PWRUPF', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IF_ICACHERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IF_ICACHERR, self).__init__(register,
            'ICACHERR', 'MSC.IF.ICACHERR', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IF_WDATAOV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IF_WDATAOV, self).__init__(register,
            'WDATAOV', 'MSC.IF.WDATAOV', 'read-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IF_LVEWRITE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IF_LVEWRITE, self).__init__(register,
            'LVEWRITE', 'MSC.IF.LVEWRITE', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFS_ERASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFS_ERASE, self).__init__(register,
            'ERASE', 'MSC.IFS.ERASE', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFS_WRITE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFS_WRITE, self).__init__(register,
            'WRITE', 'MSC.IFS.WRITE', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFS_CHOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFS_CHOF, self).__init__(register,
            'CHOF', 'MSC.IFS.CHOF', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFS_CMOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFS_CMOF, self).__init__(register,
            'CMOF', 'MSC.IFS.CMOF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFS_PWRUPF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFS_PWRUPF, self).__init__(register,
            'PWRUPF', 'MSC.IFS.PWRUPF', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFS_ICACHERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFS_ICACHERR, self).__init__(register,
            'ICACHERR', 'MSC.IFS.ICACHERR', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFS_WDATAOV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFS_WDATAOV, self).__init__(register,
            'WDATAOV', 'MSC.IFS.WDATAOV', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFS_LVEWRITE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFS_LVEWRITE, self).__init__(register,
            'LVEWRITE', 'MSC.IFS.LVEWRITE', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFC_ERASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFC_ERASE, self).__init__(register,
            'ERASE', 'MSC.IFC.ERASE', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFC_WRITE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFC_WRITE, self).__init__(register,
            'WRITE', 'MSC.IFC.WRITE', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFC_CHOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFC_CHOF, self).__init__(register,
            'CHOF', 'MSC.IFC.CHOF', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFC_CMOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFC_CMOF, self).__init__(register,
            'CMOF', 'MSC.IFC.CMOF', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFC_PWRUPF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFC_PWRUPF, self).__init__(register,
            'PWRUPF', 'MSC.IFC.PWRUPF', 'write-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFC_ICACHERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFC_ICACHERR, self).__init__(register,
            'ICACHERR', 'MSC.IFC.ICACHERR', 'write-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFC_WDATAOV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFC_WDATAOV, self).__init__(register,
            'WDATAOV', 'MSC.IFC.WDATAOV', 'write-only',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IFC_LVEWRITE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IFC_LVEWRITE, self).__init__(register,
            'LVEWRITE', 'MSC.IFC.LVEWRITE', 'write-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IEN_ERASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IEN_ERASE, self).__init__(register,
            'ERASE', 'MSC.IEN.ERASE', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IEN_WRITE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IEN_WRITE, self).__init__(register,
            'WRITE', 'MSC.IEN.WRITE', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IEN_CHOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IEN_CHOF, self).__init__(register,
            'CHOF', 'MSC.IEN.CHOF', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IEN_CMOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IEN_CMOF, self).__init__(register,
            'CMOF', 'MSC.IEN.CMOF', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IEN_PWRUPF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IEN_PWRUPF, self).__init__(register,
            'PWRUPF', 'MSC.IEN.PWRUPF', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IEN_ICACHERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IEN_ICACHERR, self).__init__(register,
            'ICACHERR', 'MSC.IEN.ICACHERR', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IEN_WDATAOV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IEN_WDATAOV, self).__init__(register,
            'WDATAOV', 'MSC.IEN.WDATAOV', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_IEN_LVEWRITE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_IEN_LVEWRITE, self).__init__(register,
            'LVEWRITE', 'MSC.IEN.LVEWRITE', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_LOCK_LOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_LOCK_LOCKKEY, self).__init__(register,
            'LOCKKEY', 'MSC.LOCK.LOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_MSC_LOCK_LOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHECMD_INVCACHE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHECMD_INVCACHE, self).__init__(register,
            'INVCACHE', 'MSC.CACHECMD.INVCACHE', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHECMD_STARTPC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHECMD_STARTPC, self).__init__(register,
            'STARTPC', 'MSC.CACHECMD.STARTPC', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHECMD_STOPPC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHECMD_STOPPC, self).__init__(register,
            'STOPPC', 'MSC.CACHECMD.STOPPC', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHEHITS_CACHEHITS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHEHITS_CACHEHITS, self).__init__(register,
            'CACHEHITS', 'MSC.CACHEHITS.CACHEHITS', 'read-only',
            "",
            0, 20)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHEMISSES_CACHEMISSES(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHEMISSES_CACHEMISSES, self).__init__(register,
            'CACHEMISSES', 'MSC.CACHEMISSES.CACHEMISSES', 'read-only',
            "",
            0, 20)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MASSLOCK_LOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MASSLOCK_LOCKKEY, self).__init__(register,
            'LOCKKEY', 'MSC.MASSLOCK.LOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_MSC_MASSLOCK_LOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STARTUP_STDLY0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STARTUP_STDLY0, self).__init__(register,
            'STDLY0', 'MSC.STARTUP.STDLY0', 'read-write',
            "",
            0, 10)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STARTUP_STDLY1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STARTUP_STDLY1, self).__init__(register,
            'STDLY1', 'MSC.STARTUP.STDLY1', 'read-write',
            "",
            12, 10)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STARTUP_ASTWAIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STARTUP_ASTWAIT, self).__init__(register,
            'ASTWAIT', 'MSC.STARTUP.ASTWAIT', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STARTUP_STWSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STARTUP_STWSEN, self).__init__(register,
            'STWSEN', 'MSC.STARTUP.STWSEN', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STARTUP_STWSAEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STARTUP_STWSAEN, self).__init__(register,
            'STWSAEN', 'MSC.STARTUP.STWSAEN', 'read-write',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_STARTUP_STWS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_STARTUP_STWS, self).__init__(register,
            'STWS', 'MSC.STARTUP.STWS', 'read-write',
            "",
            28, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_UCFGLOCK0_INTERLEAVEDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_UCFGLOCK0_INTERLEAVEDIS, self).__init__(register,
            'INTERLEAVEDIS', 'MSC.UCFGLOCK0.INTERLEAVEDIS', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_UCFGLOCK0_BOOTLOADEREN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_UCFGLOCK0_BOOTLOADEREN, self).__init__(register,
            'BOOTLOADEREN', 'MSC.UCFGLOCK0.BOOTLOADEREN', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_UCFGLOCK0_PINRESETSOFT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_UCFGLOCK0_PINRESETSOFT, self).__init__(register,
            'PINRESETSOFT', 'MSC.UCFGLOCK0.PINRESETSOFT', 'write-only',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_UCFGLOCK1_BANKSWITCHINGDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_UCFGLOCK1_BANKSWITCHINGDIS, self).__init__(register,
            'BANKSWITCHINGDIS', 'MSC.UCFGLOCK1.BANKSWITCHINGDIS', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_BANKSWITCHLOCK_BANKSWITCHLOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_BANKSWITCHLOCK_BANKSWITCHLOCKKEY, self).__init__(register,
            'BANKSWITCHLOCKKEY', 'MSC.BANKSWITCHLOCK.BANKSWITCHLOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_MSC_BANKSWITCHLOCK_BANKSWITCHLOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CMD_PWRUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CMD_PWRUP, self).__init__(register,
            'PWRUP', 'MSC.CMD.PWRUP', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CMD_SWITCHINGBANK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CMD_SWITCHINGBANK, self).__init__(register,
            'SWITCHINGBANK', 'MSC.CMD.SWITCHINGBANK', 'write-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_DSRINPORT_DSRINPUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_DSRINPORT_DSRINPUT, self).__init__(register,
            'DSRINPUT', 'MSC.DSRINPORT.DSRINPUT', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_DSRINPORT_DSRINVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_DSRINPORT_DSRINVALID, self).__init__(register,
            'DSRINVALID', 'MSC.DSRINPORT.DSRINVALID', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_DSROUTPORT_DSROUTPUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_DSROUTPORT_DSROUTPUT, self).__init__(register,
            'DSROUTPUT', 'MSC.DSROUTPORT.DSROUTPUT', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_DEVINFOLOC_BASEADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_DEVINFOLOC_BASEADDR, self).__init__(register,
            'BASEADDR', 'MSC.DEVINFOLOC.BASEADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CHIPREVHW_MINOR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CHIPREVHW_MINOR, self).__init__(register,
            'MINOR', 'MSC.CHIPREVHW.MINOR', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CHIPREVHW_MAJOR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CHIPREVHW_MAJOR, self).__init__(register,
            'MAJOR', 'MSC.CHIPREVHW.MAJOR', 'read-only',
            "",
            8, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CHIPREVHW_FAMILY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CHIPREVHW_FAMILY, self).__init__(register,
            'FAMILY', 'MSC.CHIPREVHW.FAMILY', 'read-only',
            "",
            16, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CHIPREVHW_VARIENT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CHIPREVHW_VARIENT, self).__init__(register,
            'VARIENT', 'MSC.CHIPREVHW.VARIENT', 'read-only',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CHIPREV_MINOR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CHIPREV_MINOR, self).__init__(register,
            'MINOR', 'MSC.CHIPREV.MINOR', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CHIPREV_MAJOR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CHIPREV_MAJOR, self).__init__(register,
            'MAJOR', 'MSC.CHIPREV.MAJOR', 'read-write',
            "",
            8, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CHIPREV_FAMILY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CHIPREV_FAMILY, self).__init__(register,
            'FAMILY', 'MSC.CHIPREV.FAMILY', 'read-write',
            "",
            16, 6)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_BOOTLOADERCTRL_BLRDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_BOOTLOADERCTRL_BLRDIS, self).__init__(register,
            'BLRDIS', 'MSC.BOOTLOADERCTRL.BLRDIS', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_BOOTLOADERCTRL_BLWDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_BOOTLOADERCTRL_BLWDIS, self).__init__(register,
            'BLWDIS', 'MSC.BOOTLOADERCTRL.BLWDIS', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_AAPUNLOCKCMD_UNLOCKAAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_AAPUNLOCKCMD_UNLOCKAAP, self).__init__(register,
            'UNLOCKAAP', 'MSC.AAPUNLOCKCMD.UNLOCKAAP', 'write-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHECONFIG0_CACHELPLEVEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHECONFIG0_CACHELPLEVEL, self).__init__(register,
            'CACHELPLEVEL', 'MSC.CACHECONFIG0.CACHELPLEVEL', 'read-write',
            "",
            0, 2,
            RM_Enum_MSC_CACHECONFIG0_CACHELPLEVEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHECONFIG1_CACHENESTFACTOR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHECONFIG1_CACHENESTFACTOR, self).__init__(register,
            'CACHENESTFACTOR', 'MSC.CACHECONFIG1.CACHENESTFACTOR', 'read-write',
            "",
            0, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_RAMCTRL_RAMCACHEEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_RAMCTRL_RAMCACHEEN, self).__init__(register,
            'RAMCACHEEN', 'MSC.RAMCTRL.RAMCACHEEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_RAMCTRL_RAM1CACHEEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_RAMCTRL_RAM1CACHEEN, self).__init__(register,
            'RAM1CACHEEN', 'MSC.RAMCTRL.RAM1CACHEEN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_RAMCTRL_RAM2CACHEEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_RAMCTRL_RAM2CACHEEN, self).__init__(register,
            'RAM2CACHEEN', 'MSC.RAMCTRL.RAM2CACHEEN', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_RAMCTRL_RAMSEQCACHEEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_RAMCTRL_RAMSEQCACHEEN, self).__init__(register,
            'RAMSEQCACHEEN', 'MSC.RAMCTRL.RAMSEQCACHEEN', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MBISTCTRL_BIST0EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MBISTCTRL_BIST0EN, self).__init__(register,
            'BIST0EN', 'MSC.MBISTCTRL.BIST0EN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MBISTCTRL_BIST1EN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MBISTCTRL_BIST1EN, self).__init__(register,
            'BIST1EN', 'MSC.MBISTCTRL.BIST1EN', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MBISTCTRL_BISTCLKEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MBISTCTRL_BISTCLKEN, self).__init__(register,
            'BISTCLKEN', 'MSC.MBISTCTRL.BISTCLKEN', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MBISTCTRL_BISTRSTN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MBISTCTRL_BISTRSTN, self).__init__(register,
            'BISTRSTN', 'MSC.MBISTCTRL.BISTRSTN', 'read-write',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MBISTCTRL_DIAGEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MBISTCTRL_DIAGEN, self).__init__(register,
            'DIAGEN', 'MSC.MBISTCTRL.DIAGEN', 'read-write',
            "",
            6, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MBISTCTRL_DIAGSWEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MBISTCTRL_DIAGSWEN, self).__init__(register,
            'DIAGSWEN', 'MSC.MBISTCTRL.DIAGSWEN', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MBISTCTRL_HOLDN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MBISTCTRL_HOLDN, self).__init__(register,
            'HOLDN', 'MSC.MBISTCTRL.HOLDN', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MBISTCTRL_STATSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MBISTCTRL_STATSEL, self).__init__(register,
            'STATSEL', 'MSC.MBISTCTRL.STATSEL', 'read-write',
            "",
            9, 3,
            RM_Enum_MSC_MBISTCTRL_STATSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MBISTCTRL_ALGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MBISTCTRL_ALGSEL, self).__init__(register,
            'ALGSEL', 'MSC.MBISTCTRL.ALGSEL', 'read-write',
            "",
            12, 7,
            RM_Enum_MSC_MBISTCTRL_ALGSEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MBISTCTRL_ALGSELDP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MBISTCTRL_ALGSELDP, self).__init__(register,
            'ALGSELDP', 'MSC.MBISTCTRL.ALGSELDP', 'read-write',
            "",
            19, 2,
            RM_Enum_MSC_MBISTCTRL_ALGSELDP(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MBISTCTRL_DIAGCLKEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MBISTCTRL_DIAGCLKEN, self).__init__(register,
            'DIAGCLKEN', 'MSC.MBISTCTRL.DIAGCLKEN', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MBISTSTATUS_MBIST_STATUS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MBISTSTATUS_MBIST_STATUS, self).__init__(register,
            'MBIST_STATUS', 'MSC.MBISTSTATUS.MBIST_STATUS', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_MBISTLOCK_LOCKKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_MBISTLOCK_LOCKKEY, self).__init__(register,
            'LOCKKEY', 'MSC.MBISTLOCK.LOCKKEY', 'read-write',
            "",
            0, 16,
            RM_Enum_MSC_MBISTLOCK_LOCKKEY(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTCTRL_CTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTCTRL_CTRL, self).__init__(register,
            'CTRL', 'MSC.TESTCTRL.CTRL', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTCTRL_TMR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTCTRL_TMR, self).__init__(register,
            'TMR', 'MSC.TESTCTRL.TMR', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTCTRL_TMR1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTCTRL_TMR1, self).__init__(register,
            'TMR1', 'MSC.TESTCTRL.TMR1', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTCTRL_INST0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTCTRL_INST0, self).__init__(register,
            'INST0', 'MSC.TESTCTRL.INST0', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTCTRL_INST1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTCTRL_INST1, self).__init__(register,
            'INST1', 'MSC.TESTCTRL.INST1', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTCTRL_PATMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTCTRL_PATMODE, self).__init__(register,
            'PATMODE', 'MSC.TESTCTRL.PATMODE', 'read-write',
            "",
            16, 3,
            RM_Enum_MSC_TESTCTRL_PATMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTCTRL_PATINFOEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTCTRL_PATINFOEN, self).__init__(register,
            'PATINFOEN', 'MSC.TESTCTRL.PATINFOEN', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTCTRL_SEMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTCTRL_SEMODE, self).__init__(register,
            'SEMODE', 'MSC.TESTCTRL.SEMODE', 'read-write',
            "",
            20, 2,
            RM_Enum_MSC_TESTCTRL_SEMODE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTCTRL_PATEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTCTRL_PATEN, self).__init__(register,
            'PATEN', 'MSC.TESTCTRL.PATEN', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTCTRL_PATRESET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTCTRL_PATRESET, self).__init__(register,
            'PATRESET', 'MSC.TESTCTRL.PATRESET', 'read-write',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTCTRL_LVEMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTCTRL_LVEMODE, self).__init__(register,
            'LVEMODE', 'MSC.TESTCTRL.LVEMODE', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTCTRL_CDAEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTCTRL_CDAEN, self).__init__(register,
            'CDAEN', 'MSC.TESTCTRL.CDAEN', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTCTRL_FLASHTESTEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTCTRL_FLASHTESTEN, self).__init__(register,
            'FLASHTESTEN', 'MSC.TESTCTRL.FLASHTESTEN', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_PATDIAGCTRL_INFODIAGXADR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_PATDIAGCTRL_INFODIAGXADR, self).__init__(register,
            'INFODIAGXADR', 'MSC.PATDIAGCTRL.INFODIAGXADR', 'read-write',
            "",
            0, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_PATDIAGCTRL_INFODIAGINCR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_PATDIAGCTRL_INFODIAGINCR, self).__init__(register,
            'INFODIAGINCR', 'MSC.PATDIAGCTRL.INFODIAGINCR', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_PATDIAGCTRL_MAINDIAGXADR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_PATDIAGCTRL_MAINDIAGXADR, self).__init__(register,
            'MAINDIAGXADR', 'MSC.PATDIAGCTRL.MAINDIAGXADR', 'read-write',
            "",
            16, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_PATDIAGCTRL_MAINDIAGINCR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_PATDIAGCTRL_MAINDIAGINCR, self).__init__(register,
            'MAINDIAGINCR', 'MSC.PATDIAGCTRL.MAINDIAGINCR', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_PATADDR_PATADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_PATADDR_PATADDR, self).__init__(register,
            'PATADDR', 'MSC.PATADDR.PATADDR', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_PATDONEADDR_PATDONEADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_PATDONEADDR_PATDONEADDR, self).__init__(register,
            'PATDONEADDR', 'MSC.PATDONEADDR.PATDONEADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_PATSTATUS_PATDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_PATSTATUS_PATDONE, self).__init__(register,
            'PATDONE', 'MSC.PATSTATUS.PATDONE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_PATSTATUS_INST0PATPASS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_PATSTATUS_INST0PATPASS, self).__init__(register,
            'INST0PATPASS', 'MSC.PATSTATUS.INST0PATPASS', 'read-only',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_PATSTATUS_INST1PATPASS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_PATSTATUS_INST1PATPASS, self).__init__(register,
            'INST1PATPASS', 'MSC.PATSTATUS.INST1PATPASS', 'read-only',
            "",
            5, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_PATSTATUS_INTERFACERDY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_PATSTATUS_INTERFACERDY, self).__init__(register,
            'INTERFACERDY', 'MSC.PATSTATUS.INTERFACERDY', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTTC0_TC0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTTC0_TC0, self).__init__(register,
            'TC0', 'MSC.TESTTC0.TC0', 'read-only',
            "",
            0, 10)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTTC0_TC1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTTC0_TC1, self).__init__(register,
            'TC1', 'MSC.TESTTC0.TC1', 'read-only',
            "",
            16, 10)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTREDUNDANCY_REDEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTREDUNDANCY_REDEN, self).__init__(register,
            'REDEN', 'MSC.TESTREDUNDANCY.REDEN', 'read-write',
            "",
            0, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_TESTREDUNDANCY_IFREN1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_TESTREDUNDANCY_IFREN1, self).__init__(register,
            'IFREN1', 'MSC.TESTREDUNDANCY.IFREN1', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_INST0_DOUT0_DOUT0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_INST0_DOUT0_DOUT0, self).__init__(register,
            'DOUT0', 'MSC.INST0_DOUT0.DOUT0', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_INST0_DOUT1_DOUT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_INST0_DOUT1_DOUT1, self).__init__(register,
            'DOUT1', 'MSC.INST0_DOUT1.DOUT1', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_INST1_DOUT0_DOUT0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_INST1_DOUT0_DOUT0, self).__init__(register,
            'DOUT0', 'MSC.INST1_DOUT0.DOUT0', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_INST1_DOUT1_DOUT1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_INST1_DOUT1_DOUT1, self).__init__(register,
            'DOUT1', 'MSC.INST1_DOUT1.DOUT1', 'read-only',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_REPINST0_REPADDR0_REPINVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_REPINST0_REPADDR0_REPINVALID, self).__init__(register,
            'REPINVALID', 'MSC.REPINST0_REPADDR0.REPINVALID', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_REPINST0_REPADDR0_REPADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_REPINST0_REPADDR0_REPADDR, self).__init__(register,
            'REPADDR', 'MSC.REPINST0_REPADDR0.REPADDR', 'read-write',
            "",
            1, 15)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_REPINST0_REPADDR1_REPINVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_REPINST0_REPADDR1_REPINVALID, self).__init__(register,
            'REPINVALID', 'MSC.REPINST0_REPADDR1.REPINVALID', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_REPINST0_REPADDR1_REPADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_REPINST0_REPADDR1_REPADDR, self).__init__(register,
            'REPADDR', 'MSC.REPINST0_REPADDR1.REPADDR', 'read-write',
            "",
            1, 15)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_REPINST1_REPADDR0_REPINVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_REPINST1_REPADDR0_REPINVALID, self).__init__(register,
            'REPINVALID', 'MSC.REPINST1_REPADDR0.REPINVALID', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_REPINST1_REPADDR0_REPADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_REPINST1_REPADDR0_REPADDR, self).__init__(register,
            'REPADDR', 'MSC.REPINST1_REPADDR0.REPADDR', 'read-write',
            "",
            1, 15)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_REPINST1_REPADDR1_REPINVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_REPINST1_REPADDR1_REPINVALID, self).__init__(register,
            'REPINVALID', 'MSC.REPINST1_REPADDR1.REPINVALID', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_REPINST1_REPADDR1_REPADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_REPINST1_REPADDR1_REPADDR, self).__init__(register,
            'REPADDR', 'MSC.REPINST1_REPADDR1.REPADDR', 'read-write',
            "",
            1, 15)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE0_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE0_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE0_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE1_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE1_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE1_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE2_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE2_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE2_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE3_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE3_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE3_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE4_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE4_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE4_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE5_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE5_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE5_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE6_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE6_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE6_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE7_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE7_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE7_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE8_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE8_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE8_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE9_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE9_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE9_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE10_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE10_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE10_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE11_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE11_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE11_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE12_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE12_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE12_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE13_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE13_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE13_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE14_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE14_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE14_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE15_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE15_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE15_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE16_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE16_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE16_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE17_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE17_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE17_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE18_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE18_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE18_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE19_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE19_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE19_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE20_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE20_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE20_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE21_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE21_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE21_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE22_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE22_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE22_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE23_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE23_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE23_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE24_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE24_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE24_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE25_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE25_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE25_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE26_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE26_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE26_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE27_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE27_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE27_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE28_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE28_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE28_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE29_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE29_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE29_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE30_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE30_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE30_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE31_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE31_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE31_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE32_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE32_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE32_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE33_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE33_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE33_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE34_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE34_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE34_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE35_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE35_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE35_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE36_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE36_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE36_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE37_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE37_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE37_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE38_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE38_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE38_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE39_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE39_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE39_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE40_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE40_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE40_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE41_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE41_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE41_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE42_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE42_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE42_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE43_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE43_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE43_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE44_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE44_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE44_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE45_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE45_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE45_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE46_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE46_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE46_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE47_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE47_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE47_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE48_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE48_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE48_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE49_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE49_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE49_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE50_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE50_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE50_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE51_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE51_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE51_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE52_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE52_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE52_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE53_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE53_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE53_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE54_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE54_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE54_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE55_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE55_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE55_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE56_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE56_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE56_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE57_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE57_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE57_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE58_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE58_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE58_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE59_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE59_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE59_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE60_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE60_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE60_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE61_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE61_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE61_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE62_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE62_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE62_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE63_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE63_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE63_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE64_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE64_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE64_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE65_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE65_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE65_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE66_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE66_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE66_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE67_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE67_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE67_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE68_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE68_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE68_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE69_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE69_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE69_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE70_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE70_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE70_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE71_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE71_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE71_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE72_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE72_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE72_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE73_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE73_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE73_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE74_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE74_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE74_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE75_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE75_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE75_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE76_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE76_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE76_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE77_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE77_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE77_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE78_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE78_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE78_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE79_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE79_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE79_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE80_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE80_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE80_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE81_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE81_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE81_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE82_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE82_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE82_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE83_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE83_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE83_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE84_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE84_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE84_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE85_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE85_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE85_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE86_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE86_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE86_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE87_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE87_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE87_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE88_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE88_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE88_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE89_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE89_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE89_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE90_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE90_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE90_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE91_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE91_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE91_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE92_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE92_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE92_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE93_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE93_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE93_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE94_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE94_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE94_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE95_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE95_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE95_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE96_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE96_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE96_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE97_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE97_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE97_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE98_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE98_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE98_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE99_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE99_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE99_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE100_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE100_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE100_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE101_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE101_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE101_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE102_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE102_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE102_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE103_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE103_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE103_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE104_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE104_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE104_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE105_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE105_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE105_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE106_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE106_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE106_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE107_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE107_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE107_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE108_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE108_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE108_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE109_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE109_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE109_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE110_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE110_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE110_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE111_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE111_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE111_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE112_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE112_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE112_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE113_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE113_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE113_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE114_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE114_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE114_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE115_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE115_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE115_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE116_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE116_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE116_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE117_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE117_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE117_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE118_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE118_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE118_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE119_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE119_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE119_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE120_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE120_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE120_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE121_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE121_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE121_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE122_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE122_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE122_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE123_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE123_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE123_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE124_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE124_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE124_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE125_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE125_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE125_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE126_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE126_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE126_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE127_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE127_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE127_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE128_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE128_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE128_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE129_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE129_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE129_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE130_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE130_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE130_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE131_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE131_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE131_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE132_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE132_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE132_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE133_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE133_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE133_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE134_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE134_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE134_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE135_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE135_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE135_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE136_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE136_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE136_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE137_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE137_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE137_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE138_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE138_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE138_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE139_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE139_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE139_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE140_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE140_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE140_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE141_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE141_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE141_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE142_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE142_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE142_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE143_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE143_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE143_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE144_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE144_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE144_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE145_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE145_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE145_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE146_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE146_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE146_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE147_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE147_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE147_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE148_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE148_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE148_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE149_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE149_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE149_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE150_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE150_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE150_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE151_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE151_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE151_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE152_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE152_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE152_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE153_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE153_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE153_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE154_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE154_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE154_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE155_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE155_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE155_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE156_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE156_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE156_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE157_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE157_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE157_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE158_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE158_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE158_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE159_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE159_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE159_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE160_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE160_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE160_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE161_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE161_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE161_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE162_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE162_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE162_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE163_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE163_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE163_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE164_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE164_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE164_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE165_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE165_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE165_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE166_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE166_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE166_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE167_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE167_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE167_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE168_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE168_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE168_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE169_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE169_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE169_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE170_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE170_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE170_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE171_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE171_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE171_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE172_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE172_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE172_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE173_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE173_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE173_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE174_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE174_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE174_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE175_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE175_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE175_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE176_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE176_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE176_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE177_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE177_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE177_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE178_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE178_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE178_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE179_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE179_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE179_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE180_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE180_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE180_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE181_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE181_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE181_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE182_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE182_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE182_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE183_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE183_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE183_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE184_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE184_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE184_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE185_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE185_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE185_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE186_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE186_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE186_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE187_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE187_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE187_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE188_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE188_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE188_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE189_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE189_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE189_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE190_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE190_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE190_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE191_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE191_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE191_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE192_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE192_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE192_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE193_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE193_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE193_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE194_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE194_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE194_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE195_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE195_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE195_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE196_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE196_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE196_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE197_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE197_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE197_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE198_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE198_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE198_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE199_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE199_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE199_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE200_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE200_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE200_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE201_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE201_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE201_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE202_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE202_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE202_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE203_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE203_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE203_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE204_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE204_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE204_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE205_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE205_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE205_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE206_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE206_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE206_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE207_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE207_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE207_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE208_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE208_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE208_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE209_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE209_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE209_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE210_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE210_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE210_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE211_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE211_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE211_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE212_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE212_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE212_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE213_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE213_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE213_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE214_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE214_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE214_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE215_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE215_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE215_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE216_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE216_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE216_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE217_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE217_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE217_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE218_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE218_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE218_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE219_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE219_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE219_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE220_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE220_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE220_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE221_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE221_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE221_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE222_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE222_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE222_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE223_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE223_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE223_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE224_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE224_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE224_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE225_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE225_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE225_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE226_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE226_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE226_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE227_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE227_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE227_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE228_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE228_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE228_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE229_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE229_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE229_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE230_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE230_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE230_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE231_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE231_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE231_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE232_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE232_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE232_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE233_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE233_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE233_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE234_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE234_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE234_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE235_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE235_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE235_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE236_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE236_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE236_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE237_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE237_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE237_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE238_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE238_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE238_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE239_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE239_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE239_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE240_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE240_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE240_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE241_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE241_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE241_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE242_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE242_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE242_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE243_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE243_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE243_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE244_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE244_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE244_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE245_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE245_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE245_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE246_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE246_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE246_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE247_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE247_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE247_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE248_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE248_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE248_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE249_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE249_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE249_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE250_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE250_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE250_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE251_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE251_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE251_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE252_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE252_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE252_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE253_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE253_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE253_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE254_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE254_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE254_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_MSC_CACHE255_DATA_DATA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_MSC_CACHE255_DATA_DATA, self).__init__(register,
            'DATA', 'MSC.CACHE255_DATA.DATA', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


