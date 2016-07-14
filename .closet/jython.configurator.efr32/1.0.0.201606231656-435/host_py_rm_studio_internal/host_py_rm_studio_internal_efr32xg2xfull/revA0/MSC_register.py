
from static import Base_RM_Register
from MSC_field import *


class RM_Register_MSC_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CTRL, self).__init__(rmio, label,
            0x400e0000, 0x000,
            'CTRL', 'MSC.CTRL', 'read-write',
            "",
            0x00000001, 0x0000011F)

        self.ADDRFAULTEN = RM_Field_MSC_CTRL_ADDRFAULTEN(self)
        self.zz_fdict['ADDRFAULTEN'] = self.ADDRFAULTEN
        self.CLKDISFAULTEN = RM_Field_MSC_CTRL_CLKDISFAULTEN(self)
        self.zz_fdict['CLKDISFAULTEN'] = self.CLKDISFAULTEN
        self.PWRUPONDEMAND = RM_Field_MSC_CTRL_PWRUPONDEMAND(self)
        self.zz_fdict['PWRUPONDEMAND'] = self.PWRUPONDEMAND
        self.IFCREADCLEAR = RM_Field_MSC_CTRL_IFCREADCLEAR(self)
        self.zz_fdict['IFCREADCLEAR'] = self.IFCREADCLEAR
        self.TIMEOUTFAULTEN = RM_Field_MSC_CTRL_TIMEOUTFAULTEN(self)
        self.zz_fdict['TIMEOUTFAULTEN'] = self.TIMEOUTFAULTEN
        self.BYPASSAHBCNT = RM_Field_MSC_CTRL_BYPASSAHBCNT(self)
        self.zz_fdict['BYPASSAHBCNT'] = self.BYPASSAHBCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_READCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_READCTRL, self).__init__(rmio, label,
            0x400e0000, 0x004,
            'READCTRL', 'MSC.READCTRL', 'read-write',
            "",
            0x01000100, 0x13000338)

        self.IFCDIS = RM_Field_MSC_READCTRL_IFCDIS(self)
        self.zz_fdict['IFCDIS'] = self.IFCDIS
        self.AIDIS = RM_Field_MSC_READCTRL_AIDIS(self)
        self.zz_fdict['AIDIS'] = self.AIDIS
        self.ICCDIS = RM_Field_MSC_READCTRL_ICCDIS(self)
        self.zz_fdict['ICCDIS'] = self.ICCDIS
        self.PREFETCH = RM_Field_MSC_READCTRL_PREFETCH(self)
        self.zz_fdict['PREFETCH'] = self.PREFETCH
        self.USEHPROT = RM_Field_MSC_READCTRL_USEHPROT(self)
        self.zz_fdict['USEHPROT'] = self.USEHPROT
        self.MODE = RM_Field_MSC_READCTRL_MODE(self)
        self.zz_fdict['MODE'] = self.MODE
        self.SCBTP = RM_Field_MSC_READCTRL_SCBTP(self)
        self.zz_fdict['SCBTP'] = self.SCBTP
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_WRITECTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_WRITECTRL, self).__init__(rmio, label,
            0x400e0000, 0x008,
            'WRITECTRL', 'MSC.WRITECTRL', 'read-write',
            "",
            0x00000000, 0x0000003F)

        self.WREN = RM_Field_MSC_WRITECTRL_WREN(self)
        self.zz_fdict['WREN'] = self.WREN
        self.IRQERASEABORT = RM_Field_MSC_WRITECTRL_IRQERASEABORT(self)
        self.zz_fdict['IRQERASEABORT'] = self.IRQERASEABORT
        self.WDOUBLE = RM_Field_MSC_WRITECTRL_WDOUBLE(self)
        self.zz_fdict['WDOUBLE'] = self.WDOUBLE
        self.LPWRITE = RM_Field_MSC_WRITECTRL_LPWRITE(self)
        self.zz_fdict['LPWRITE'] = self.LPWRITE
        self.LPERASE = RM_Field_MSC_WRITECTRL_LPERASE(self)
        self.zz_fdict['LPERASE'] = self.LPERASE
        self.RWWEN = RM_Field_MSC_WRITECTRL_RWWEN(self)
        self.zz_fdict['RWWEN'] = self.RWWEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_WRITECMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_WRITECMD, self).__init__(rmio, label,
            0x400e0000, 0x00C,
            'WRITECMD', 'MSC.WRITECMD', 'write-only',
            "",
            0x00000000, 0x0000133F)

        self.LADDRIM = RM_Field_MSC_WRITECMD_LADDRIM(self)
        self.zz_fdict['LADDRIM'] = self.LADDRIM
        self.ERASEPAGE = RM_Field_MSC_WRITECMD_ERASEPAGE(self)
        self.zz_fdict['ERASEPAGE'] = self.ERASEPAGE
        self.WRITEEND = RM_Field_MSC_WRITECMD_WRITEEND(self)
        self.zz_fdict['WRITEEND'] = self.WRITEEND
        self.WRITEONCE = RM_Field_MSC_WRITECMD_WRITEONCE(self)
        self.zz_fdict['WRITEONCE'] = self.WRITEONCE
        self.WRITETRIG = RM_Field_MSC_WRITECMD_WRITETRIG(self)
        self.zz_fdict['WRITETRIG'] = self.WRITETRIG
        self.ERASEABORT = RM_Field_MSC_WRITECMD_ERASEABORT(self)
        self.zz_fdict['ERASEABORT'] = self.ERASEABORT
        self.ERASEMAIN0 = RM_Field_MSC_WRITECMD_ERASEMAIN0(self)
        self.zz_fdict['ERASEMAIN0'] = self.ERASEMAIN0
        self.ERASEMAIN1 = RM_Field_MSC_WRITECMD_ERASEMAIN1(self)
        self.zz_fdict['ERASEMAIN1'] = self.ERASEMAIN1
        self.CLEARWDATA = RM_Field_MSC_WRITECMD_CLEARWDATA(self)
        self.zz_fdict['CLEARWDATA'] = self.CLEARWDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_ADDRB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_ADDRB, self).__init__(rmio, label,
            0x400e0000, 0x010,
            'ADDRB', 'MSC.ADDRB', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.ADDRB = RM_Field_MSC_ADDRB_ADDRB(self)
        self.zz_fdict['ADDRB'] = self.ADDRB
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_WDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_WDATA, self).__init__(rmio, label,
            0x400e0000, 0x018,
            'WDATA', 'MSC.WDATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.WDATA = RM_Field_MSC_WDATA_WDATA(self)
        self.zz_fdict['WDATA'] = self.WDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_STATUS, self).__init__(rmio, label,
            0x400e0000, 0x01C,
            'STATUS', 'MSC.STATUS', 'read-only',
            "",
            0x00000008, 0xFF0000FF)

        self.BUSY = RM_Field_MSC_STATUS_BUSY(self)
        self.zz_fdict['BUSY'] = self.BUSY
        self.LOCKED = RM_Field_MSC_STATUS_LOCKED(self)
        self.zz_fdict['LOCKED'] = self.LOCKED
        self.INVADDR = RM_Field_MSC_STATUS_INVADDR(self)
        self.zz_fdict['INVADDR'] = self.INVADDR
        self.WDATAREADY = RM_Field_MSC_STATUS_WDATAREADY(self)
        self.zz_fdict['WDATAREADY'] = self.WDATAREADY
        self.WORDTIMEOUT = RM_Field_MSC_STATUS_WORDTIMEOUT(self)
        self.zz_fdict['WORDTIMEOUT'] = self.WORDTIMEOUT
        self.ERASEABORTED = RM_Field_MSC_STATUS_ERASEABORTED(self)
        self.zz_fdict['ERASEABORTED'] = self.ERASEABORTED
        self.PCRUNNING = RM_Field_MSC_STATUS_PCRUNNING(self)
        self.zz_fdict['PCRUNNING'] = self.PCRUNNING
        self.BANKSWITCHED = RM_Field_MSC_STATUS_BANKSWITCHED(self)
        self.zz_fdict['BANKSWITCHED'] = self.BANKSWITCHED
        self.WDATAVALID = RM_Field_MSC_STATUS_WDATAVALID(self)
        self.zz_fdict['WDATAVALID'] = self.WDATAVALID
        self.PWRUPCKBDFAILCOUNT = RM_Field_MSC_STATUS_PWRUPCKBDFAILCOUNT(self)
        self.zz_fdict['PWRUPCKBDFAILCOUNT'] = self.PWRUPCKBDFAILCOUNT
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_MEMFEATURE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_MEMFEATURE, self).__init__(rmio, label,
            0x400e0000, 0x020,
            'MEMFEATURE', 'MSC.MEMFEATURE', 'write-only',
            "",
            0x0001000B, 0xBD37000F)

        self.FLASHSIZE = RM_Field_MSC_MEMFEATURE_FLASHSIZE(self)
        self.zz_fdict['FLASHSIZE'] = self.FLASHSIZE
        self.MPUPRESENT = RM_Field_MSC_MEMFEATURE_MPUPRESENT(self)
        self.zz_fdict['MPUPRESENT'] = self.MPUPRESENT
        self.CACHERAMIFDIS = RM_Field_MSC_MEMFEATURE_CACHERAMIFDIS(self)
        self.zz_fdict['CACHERAMIFDIS'] = self.CACHERAMIFDIS
        self.INTERLEAVE = RM_Field_MSC_MEMFEATURE_INTERLEAVE(self)
        self.zz_fdict['INTERLEAVE'] = self.INTERLEAVE
        self.FLASHRWWMERGE = RM_Field_MSC_MEMFEATURE_FLASHRWWMERGE(self)
        self.zz_fdict['FLASHRWWMERGE'] = self.FLASHRWWMERGE
        self.USEUPPERHALF = RM_Field_MSC_MEMFEATURE_USEUPPERHALF(self)
        self.zz_fdict['USEUPPERHALF'] = self.USEUPPERHALF
        self.SELECTM3 = RM_Field_MSC_MEMFEATURE_SELECTM3(self)
        self.zz_fdict['SELECTM3'] = self.SELECTM3
        self.FPUDISABLE = RM_Field_MSC_MEMFEATURE_FPUDISABLE(self)
        self.zz_fdict['FPUDISABLE'] = self.FPUDISABLE
        self.BOOTLOADERBYPASS = RM_Field_MSC_MEMFEATURE_BOOTLOADERBYPASS(self)
        self.zz_fdict['BOOTLOADERBYPASS'] = self.BOOTLOADERBYPASS
        self.BANKSWITCHING = RM_Field_MSC_MEMFEATURE_BANKSWITCHING(self)
        self.zz_fdict['BANKSWITCHING'] = self.BANKSWITCHING
        self.INTERLEAVEDISPOL = RM_Field_MSC_MEMFEATURE_INTERLEAVEDISPOL(self)
        self.zz_fdict['INTERLEAVEDISPOL'] = self.INTERLEAVEDISPOL
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CFGFEATURE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CFGFEATURE, self).__init__(rmio, label,
            0x400e0000, 0x024,
            'CFGFEATURE', 'MSC.CFGFEATURE', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.CFGLOCKEN = RM_Field_MSC_CFGFEATURE_CFGLOCKEN(self)
        self.zz_fdict['CFGLOCKEN'] = self.CFGLOCKEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_DEBUGLOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_DEBUGLOCK, self).__init__(rmio, label,
            0x400e0000, 0x028,
            'DEBUGLOCK', 'MSC.DEBUGLOCK', 'write-only',
            "",
            0x00000000, 0x0000000F)

        self.DEBUGEN = RM_Field_MSC_DEBUGLOCK_DEBUGEN(self)
        self.zz_fdict['DEBUGEN'] = self.DEBUGEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_AAPLOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_AAPLOCK, self).__init__(rmio, label,
            0x400e0000, 0x02C,
            'AAPLOCK', 'MSC.AAPLOCK', 'write-only',
            "",
            0x00000000, 0x8000000F)

        self.AAPEN = RM_Field_MSC_AAPLOCK_AAPEN(self)
        self.zz_fdict['AAPEN'] = self.AAPEN
        self.SWUNLOCKAAPEN = RM_Field_MSC_AAPLOCK_SWUNLOCKAAPEN(self)
        self.zz_fdict['SWUNLOCKAAPEN'] = self.SWUNLOCKAAPEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_IF, self).__init__(rmio, label,
            0x400e0000, 0x030,
            'IF', 'MSC.IF', 'read-only',
            "",
            0x00000000, 0x0000017F)

        self.ERASE = RM_Field_MSC_IF_ERASE(self)
        self.zz_fdict['ERASE'] = self.ERASE
        self.WRITE = RM_Field_MSC_IF_WRITE(self)
        self.zz_fdict['WRITE'] = self.WRITE
        self.CHOF = RM_Field_MSC_IF_CHOF(self)
        self.zz_fdict['CHOF'] = self.CHOF
        self.CMOF = RM_Field_MSC_IF_CMOF(self)
        self.zz_fdict['CMOF'] = self.CMOF
        self.PWRUPF = RM_Field_MSC_IF_PWRUPF(self)
        self.zz_fdict['PWRUPF'] = self.PWRUPF
        self.ICACHERR = RM_Field_MSC_IF_ICACHERR(self)
        self.zz_fdict['ICACHERR'] = self.ICACHERR
        self.WDATAOV = RM_Field_MSC_IF_WDATAOV(self)
        self.zz_fdict['WDATAOV'] = self.WDATAOV
        self.LVEWRITE = RM_Field_MSC_IF_LVEWRITE(self)
        self.zz_fdict['LVEWRITE'] = self.LVEWRITE
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_IFS, self).__init__(rmio, label,
            0x400e0000, 0x034,
            'IFS', 'MSC.IFS', 'write-only',
            "",
            0x00000000, 0x0000017F)

        self.ERASE = RM_Field_MSC_IFS_ERASE(self)
        self.zz_fdict['ERASE'] = self.ERASE
        self.WRITE = RM_Field_MSC_IFS_WRITE(self)
        self.zz_fdict['WRITE'] = self.WRITE
        self.CHOF = RM_Field_MSC_IFS_CHOF(self)
        self.zz_fdict['CHOF'] = self.CHOF
        self.CMOF = RM_Field_MSC_IFS_CMOF(self)
        self.zz_fdict['CMOF'] = self.CMOF
        self.PWRUPF = RM_Field_MSC_IFS_PWRUPF(self)
        self.zz_fdict['PWRUPF'] = self.PWRUPF
        self.ICACHERR = RM_Field_MSC_IFS_ICACHERR(self)
        self.zz_fdict['ICACHERR'] = self.ICACHERR
        self.WDATAOV = RM_Field_MSC_IFS_WDATAOV(self)
        self.zz_fdict['WDATAOV'] = self.WDATAOV
        self.LVEWRITE = RM_Field_MSC_IFS_LVEWRITE(self)
        self.zz_fdict['LVEWRITE'] = self.LVEWRITE
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_IFC, self).__init__(rmio, label,
            0x400e0000, 0x038,
            'IFC', 'MSC.IFC', 'write-only',
            "",
            0x00000000, 0x0000017F)

        self.ERASE = RM_Field_MSC_IFC_ERASE(self)
        self.zz_fdict['ERASE'] = self.ERASE
        self.WRITE = RM_Field_MSC_IFC_WRITE(self)
        self.zz_fdict['WRITE'] = self.WRITE
        self.CHOF = RM_Field_MSC_IFC_CHOF(self)
        self.zz_fdict['CHOF'] = self.CHOF
        self.CMOF = RM_Field_MSC_IFC_CMOF(self)
        self.zz_fdict['CMOF'] = self.CMOF
        self.PWRUPF = RM_Field_MSC_IFC_PWRUPF(self)
        self.zz_fdict['PWRUPF'] = self.PWRUPF
        self.ICACHERR = RM_Field_MSC_IFC_ICACHERR(self)
        self.zz_fdict['ICACHERR'] = self.ICACHERR
        self.WDATAOV = RM_Field_MSC_IFC_WDATAOV(self)
        self.zz_fdict['WDATAOV'] = self.WDATAOV
        self.LVEWRITE = RM_Field_MSC_IFC_LVEWRITE(self)
        self.zz_fdict['LVEWRITE'] = self.LVEWRITE
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_IEN, self).__init__(rmio, label,
            0x400e0000, 0x03C,
            'IEN', 'MSC.IEN', 'read-write',
            "",
            0x00000000, 0x0000017F)

        self.ERASE = RM_Field_MSC_IEN_ERASE(self)
        self.zz_fdict['ERASE'] = self.ERASE
        self.WRITE = RM_Field_MSC_IEN_WRITE(self)
        self.zz_fdict['WRITE'] = self.WRITE
        self.CHOF = RM_Field_MSC_IEN_CHOF(self)
        self.zz_fdict['CHOF'] = self.CHOF
        self.CMOF = RM_Field_MSC_IEN_CMOF(self)
        self.zz_fdict['CMOF'] = self.CMOF
        self.PWRUPF = RM_Field_MSC_IEN_PWRUPF(self)
        self.zz_fdict['PWRUPF'] = self.PWRUPF
        self.ICACHERR = RM_Field_MSC_IEN_ICACHERR(self)
        self.zz_fdict['ICACHERR'] = self.ICACHERR
        self.WDATAOV = RM_Field_MSC_IEN_WDATAOV(self)
        self.zz_fdict['WDATAOV'] = self.WDATAOV
        self.LVEWRITE = RM_Field_MSC_IEN_LVEWRITE(self)
        self.zz_fdict['LVEWRITE'] = self.LVEWRITE
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_LOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_LOCK, self).__init__(rmio, label,
            0x400e0000, 0x040,
            'LOCK', 'MSC.LOCK', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.LOCKKEY = RM_Field_MSC_LOCK_LOCKKEY(self)
        self.zz_fdict['LOCKKEY'] = self.LOCKKEY
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHECMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHECMD, self).__init__(rmio, label,
            0x400e0000, 0x044,
            'CACHECMD', 'MSC.CACHECMD', 'write-only',
            "",
            0x00000000, 0x00000007)

        self.INVCACHE = RM_Field_MSC_CACHECMD_INVCACHE(self)
        self.zz_fdict['INVCACHE'] = self.INVCACHE
        self.STARTPC = RM_Field_MSC_CACHECMD_STARTPC(self)
        self.zz_fdict['STARTPC'] = self.STARTPC
        self.STOPPC = RM_Field_MSC_CACHECMD_STOPPC(self)
        self.zz_fdict['STOPPC'] = self.STOPPC
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHEHITS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHEHITS, self).__init__(rmio, label,
            0x400e0000, 0x048,
            'CACHEHITS', 'MSC.CACHEHITS', 'read-only',
            "",
            0x00000000, 0x000FFFFF)

        self.CACHEHITS = RM_Field_MSC_CACHEHITS_CACHEHITS(self)
        self.zz_fdict['CACHEHITS'] = self.CACHEHITS
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHEMISSES(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHEMISSES, self).__init__(rmio, label,
            0x400e0000, 0x04C,
            'CACHEMISSES', 'MSC.CACHEMISSES', 'read-only',
            "",
            0x00000000, 0x000FFFFF)

        self.CACHEMISSES = RM_Field_MSC_CACHEMISSES_CACHEMISSES(self)
        self.zz_fdict['CACHEMISSES'] = self.CACHEMISSES
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_MASSLOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_MASSLOCK, self).__init__(rmio, label,
            0x400e0000, 0x054,
            'MASSLOCK', 'MSC.MASSLOCK', 'read-write',
            "",
            0x00000001, 0x0000FFFF)

        self.LOCKKEY = RM_Field_MSC_MASSLOCK_LOCKKEY(self)
        self.zz_fdict['LOCKKEY'] = self.LOCKKEY
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_STARTUP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_STARTUP, self).__init__(rmio, label,
            0x400e0000, 0x05C,
            'STARTUP', 'MSC.STARTUP', 'read-write',
            "",
            0x1300104D, 0x773FF3FF)

        self.STDLY0 = RM_Field_MSC_STARTUP_STDLY0(self)
        self.zz_fdict['STDLY0'] = self.STDLY0
        self.STDLY1 = RM_Field_MSC_STARTUP_STDLY1(self)
        self.zz_fdict['STDLY1'] = self.STDLY1
        self.ASTWAIT = RM_Field_MSC_STARTUP_ASTWAIT(self)
        self.zz_fdict['ASTWAIT'] = self.ASTWAIT
        self.STWSEN = RM_Field_MSC_STARTUP_STWSEN(self)
        self.zz_fdict['STWSEN'] = self.STWSEN
        self.STWSAEN = RM_Field_MSC_STARTUP_STWSAEN(self)
        self.zz_fdict['STWSAEN'] = self.STWSAEN
        self.STWS = RM_Field_MSC_STARTUP_STWS(self)
        self.zz_fdict['STWS'] = self.STWS
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_UCFGLOCK0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_UCFGLOCK0, self).__init__(rmio, label,
            0x400e0000, 0x068,
            'UCFGLOCK0', 'MSC.UCFGLOCK0', 'write-only',
            "",
            0x00000003, 0x00000007)

        self.INTERLEAVEDIS = RM_Field_MSC_UCFGLOCK0_INTERLEAVEDIS(self)
        self.zz_fdict['INTERLEAVEDIS'] = self.INTERLEAVEDIS
        self.BOOTLOADEREN = RM_Field_MSC_UCFGLOCK0_BOOTLOADEREN(self)
        self.zz_fdict['BOOTLOADEREN'] = self.BOOTLOADEREN
        self.PINRESETSOFT = RM_Field_MSC_UCFGLOCK0_PINRESETSOFT(self)
        self.zz_fdict['PINRESETSOFT'] = self.PINRESETSOFT
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_UCFGLOCK1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_UCFGLOCK1, self).__init__(rmio, label,
            0x400e0000, 0x06C,
            'UCFGLOCK1', 'MSC.UCFGLOCK1', 'write-only',
            "",
            0x00000001, 0x00000001)

        self.BANKSWITCHINGDIS = RM_Field_MSC_UCFGLOCK1_BANKSWITCHINGDIS(self)
        self.zz_fdict['BANKSWITCHINGDIS'] = self.BANKSWITCHINGDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_BANKSWITCHLOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_BANKSWITCHLOCK, self).__init__(rmio, label,
            0x400e0000, 0x070,
            'BANKSWITCHLOCK', 'MSC.BANKSWITCHLOCK', 'read-write',
            "",
            0x00000001, 0x0000FFFF)

        self.BANKSWITCHLOCKKEY = RM_Field_MSC_BANKSWITCHLOCK_BANKSWITCHLOCKKEY(self)
        self.zz_fdict['BANKSWITCHLOCKKEY'] = self.BANKSWITCHLOCKKEY
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CMD, self).__init__(rmio, label,
            0x400e0000, 0x074,
            'CMD', 'MSC.CMD', 'write-only',
            "",
            0x00000000, 0x00000003)

        self.PWRUP = RM_Field_MSC_CMD_PWRUP(self)
        self.zz_fdict['PWRUP'] = self.PWRUP
        self.SWITCHINGBANK = RM_Field_MSC_CMD_SWITCHINGBANK(self)
        self.zz_fdict['SWITCHINGBANK'] = self.SWITCHINGBANK
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_DSRINPORT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_DSRINPORT, self).__init__(rmio, label,
            0x400e0000, 0x078,
            'DSRINPORT', 'MSC.DSRINPORT', 'read-write',
            "",
            0x00000000, 0x000100FF)

        self.DSRINPUT = RM_Field_MSC_DSRINPORT_DSRINPUT(self)
        self.zz_fdict['DSRINPUT'] = self.DSRINPUT
        self.DSRINVALID = RM_Field_MSC_DSRINPORT_DSRINVALID(self)
        self.zz_fdict['DSRINVALID'] = self.DSRINVALID
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_DSROUTPORT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_DSROUTPORT, self).__init__(rmio, label,
            0x400e0000, 0x07C,
            'DSROUTPORT', 'MSC.DSROUTPORT', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.DSROUTPUT = RM_Field_MSC_DSROUTPORT_DSROUTPUT(self)
        self.zz_fdict['DSROUTPUT'] = self.DSROUTPUT
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_DEVINFOLOC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_DEVINFOLOC, self).__init__(rmio, label,
            0x400e0000, 0x080,
            'DEVINFOLOC', 'MSC.DEVINFOLOC', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.BASEADDR = RM_Field_MSC_DEVINFOLOC_BASEADDR(self)
        self.zz_fdict['BASEADDR'] = self.BASEADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CHIPREVHW(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CHIPREVHW, self).__init__(rmio, label,
            0x400e0000, 0x084,
            'CHIPREVHW', 'MSC.CHIPREVHW', 'read-only',
            "",
            0x00240100, 0xFF3F3FFF)

        self.MINOR = RM_Field_MSC_CHIPREVHW_MINOR(self)
        self.zz_fdict['MINOR'] = self.MINOR
        self.MAJOR = RM_Field_MSC_CHIPREVHW_MAJOR(self)
        self.zz_fdict['MAJOR'] = self.MAJOR
        self.FAMILY = RM_Field_MSC_CHIPREVHW_FAMILY(self)
        self.zz_fdict['FAMILY'] = self.FAMILY
        self.VARIENT = RM_Field_MSC_CHIPREVHW_VARIENT(self)
        self.zz_fdict['VARIENT'] = self.VARIENT
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CHIPREV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CHIPREV, self).__init__(rmio, label,
            0x400e0000, 0x08C,
            'CHIPREV', 'MSC.CHIPREV', 'read-write',
            "",
            0x00000000, 0x003F3FFF)

        self.MINOR = RM_Field_MSC_CHIPREV_MINOR(self)
        self.zz_fdict['MINOR'] = self.MINOR
        self.MAJOR = RM_Field_MSC_CHIPREV_MAJOR(self)
        self.zz_fdict['MAJOR'] = self.MAJOR
        self.FAMILY = RM_Field_MSC_CHIPREV_FAMILY(self)
        self.zz_fdict['FAMILY'] = self.FAMILY
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_BOOTLOADERCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_BOOTLOADERCTRL, self).__init__(rmio, label,
            0x400e0000, 0x090,
            'BOOTLOADERCTRL', 'MSC.BOOTLOADERCTRL', 'read-write',
            "",
            0x00000000, 0x00000003)

        self.BLRDIS = RM_Field_MSC_BOOTLOADERCTRL_BLRDIS(self)
        self.zz_fdict['BLRDIS'] = self.BLRDIS
        self.BLWDIS = RM_Field_MSC_BOOTLOADERCTRL_BLWDIS(self)
        self.zz_fdict['BLWDIS'] = self.BLWDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_AAPUNLOCKCMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_AAPUNLOCKCMD, self).__init__(rmio, label,
            0x400e0000, 0x094,
            'AAPUNLOCKCMD', 'MSC.AAPUNLOCKCMD', 'write-only',
            "",
            0x00000000, 0x00000001)

        self.UNLOCKAAP = RM_Field_MSC_AAPUNLOCKCMD_UNLOCKAAP(self)
        self.zz_fdict['UNLOCKAAP'] = self.UNLOCKAAP
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHECONFIG0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHECONFIG0, self).__init__(rmio, label,
            0x400e0000, 0x098,
            'CACHECONFIG0', 'MSC.CACHECONFIG0', 'read-write',
            "",
            0x00000003, 0x00000003)

        self.CACHELPLEVEL = RM_Field_MSC_CACHECONFIG0_CACHELPLEVEL(self)
        self.zz_fdict['CACHELPLEVEL'] = self.CACHELPLEVEL
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHECONFIG1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHECONFIG1, self).__init__(rmio, label,
            0x400e0000, 0x09C,
            'CACHECONFIG1', 'MSC.CACHECONFIG1', 'read-write',
            "",
            0x00000002, 0x00000007)

        self.CACHENESTFACTOR = RM_Field_MSC_CACHECONFIG1_CACHENESTFACTOR(self)
        self.zz_fdict['CACHENESTFACTOR'] = self.CACHENESTFACTOR
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_RAMCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_RAMCTRL, self).__init__(rmio, label,
            0x400e0000, 0x100,
            'RAMCTRL', 'MSC.RAMCTRL', 'read-write',
            "",
            0x00000000, 0x00090101)

        self.RAMCACHEEN = RM_Field_MSC_RAMCTRL_RAMCACHEEN(self)
        self.zz_fdict['RAMCACHEEN'] = self.RAMCACHEEN
        self.RAM1CACHEEN = RM_Field_MSC_RAMCTRL_RAM1CACHEEN(self)
        self.zz_fdict['RAM1CACHEEN'] = self.RAM1CACHEEN
        self.RAM2CACHEEN = RM_Field_MSC_RAMCTRL_RAM2CACHEEN(self)
        self.zz_fdict['RAM2CACHEEN'] = self.RAM2CACHEEN
        self.RAMSEQCACHEEN = RM_Field_MSC_RAMCTRL_RAMSEQCACHEEN(self)
        self.zz_fdict['RAMSEQCACHEEN'] = self.RAMSEQCACHEEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_MBISTCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_MBISTCTRL, self).__init__(rmio, label,
            0x400e0000, 0x114,
            'MBISTCTRL', 'MSC.MBISTCTRL', 'read-write',
            "",
            0x00000000, 0x003FFFF3)

        self.BIST0EN = RM_Field_MSC_MBISTCTRL_BIST0EN(self)
        self.zz_fdict['BIST0EN'] = self.BIST0EN
        self.BIST1EN = RM_Field_MSC_MBISTCTRL_BIST1EN(self)
        self.zz_fdict['BIST1EN'] = self.BIST1EN
        self.BISTCLKEN = RM_Field_MSC_MBISTCTRL_BISTCLKEN(self)
        self.zz_fdict['BISTCLKEN'] = self.BISTCLKEN
        self.BISTRSTN = RM_Field_MSC_MBISTCTRL_BISTRSTN(self)
        self.zz_fdict['BISTRSTN'] = self.BISTRSTN
        self.DIAGEN = RM_Field_MSC_MBISTCTRL_DIAGEN(self)
        self.zz_fdict['DIAGEN'] = self.DIAGEN
        self.DIAGSWEN = RM_Field_MSC_MBISTCTRL_DIAGSWEN(self)
        self.zz_fdict['DIAGSWEN'] = self.DIAGSWEN
        self.HOLDN = RM_Field_MSC_MBISTCTRL_HOLDN(self)
        self.zz_fdict['HOLDN'] = self.HOLDN
        self.STATSEL = RM_Field_MSC_MBISTCTRL_STATSEL(self)
        self.zz_fdict['STATSEL'] = self.STATSEL
        self.ALGSEL = RM_Field_MSC_MBISTCTRL_ALGSEL(self)
        self.zz_fdict['ALGSEL'] = self.ALGSEL
        self.ALGSELDP = RM_Field_MSC_MBISTCTRL_ALGSELDP(self)
        self.zz_fdict['ALGSELDP'] = self.ALGSELDP
        self.DIAGCLKEN = RM_Field_MSC_MBISTCTRL_DIAGCLKEN(self)
        self.zz_fdict['DIAGCLKEN'] = self.DIAGCLKEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_MBISTSTATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_MBISTSTATUS, self).__init__(rmio, label,
            0x400e0000, 0x118,
            'MBISTSTATUS', 'MSC.MBISTSTATUS', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.MBIST_STATUS = RM_Field_MSC_MBISTSTATUS_MBIST_STATUS(self)
        self.zz_fdict['MBIST_STATUS'] = self.MBIST_STATUS
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_MBISTLOCK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_MBISTLOCK, self).__init__(rmio, label,
            0x400e0000, 0x11C,
            'MBISTLOCK', 'MSC.MBISTLOCK', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.LOCKKEY = RM_Field_MSC_MBISTLOCK_LOCKKEY(self)
        self.zz_fdict['LOCKKEY'] = self.LOCKKEY
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_TESTCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_TESTCTRL, self).__init__(rmio, label,
            0x400e0000, 0x120,
            'TESTCTRL', 'MSC.TESTCTRL', 'read-write',
            "",
            0x00000300, 0xD93F33FF)

        self.CTRL = RM_Field_MSC_TESTCTRL_CTRL(self)
        self.zz_fdict['CTRL'] = self.CTRL
        self.TMR = RM_Field_MSC_TESTCTRL_TMR(self)
        self.zz_fdict['TMR'] = self.TMR
        self.TMR1 = RM_Field_MSC_TESTCTRL_TMR1(self)
        self.zz_fdict['TMR1'] = self.TMR1
        self.INST0 = RM_Field_MSC_TESTCTRL_INST0(self)
        self.zz_fdict['INST0'] = self.INST0
        self.INST1 = RM_Field_MSC_TESTCTRL_INST1(self)
        self.zz_fdict['INST1'] = self.INST1
        self.PATMODE = RM_Field_MSC_TESTCTRL_PATMODE(self)
        self.zz_fdict['PATMODE'] = self.PATMODE
        self.PATINFOEN = RM_Field_MSC_TESTCTRL_PATINFOEN(self)
        self.zz_fdict['PATINFOEN'] = self.PATINFOEN
        self.SEMODE = RM_Field_MSC_TESTCTRL_SEMODE(self)
        self.zz_fdict['SEMODE'] = self.SEMODE
        self.PATEN = RM_Field_MSC_TESTCTRL_PATEN(self)
        self.zz_fdict['PATEN'] = self.PATEN
        self.PATRESET = RM_Field_MSC_TESTCTRL_PATRESET(self)
        self.zz_fdict['PATRESET'] = self.PATRESET
        self.LVEMODE = RM_Field_MSC_TESTCTRL_LVEMODE(self)
        self.zz_fdict['LVEMODE'] = self.LVEMODE
        self.CDAEN = RM_Field_MSC_TESTCTRL_CDAEN(self)
        self.zz_fdict['CDAEN'] = self.CDAEN
        self.FLASHTESTEN = RM_Field_MSC_TESTCTRL_FLASHTESTEN(self)
        self.zz_fdict['FLASHTESTEN'] = self.FLASHTESTEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_PATDIAGCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_PATDIAGCTRL, self).__init__(rmio, label,
            0x400e0000, 0x124,
            'PATDIAGCTRL', 'MSC.PATDIAGCTRL', 'read-write',
            "",
            0x80008000, 0x801F801F)

        self.INFODIAGXADR = RM_Field_MSC_PATDIAGCTRL_INFODIAGXADR(self)
        self.zz_fdict['INFODIAGXADR'] = self.INFODIAGXADR
        self.INFODIAGINCR = RM_Field_MSC_PATDIAGCTRL_INFODIAGINCR(self)
        self.zz_fdict['INFODIAGINCR'] = self.INFODIAGINCR
        self.MAINDIAGXADR = RM_Field_MSC_PATDIAGCTRL_MAINDIAGXADR(self)
        self.zz_fdict['MAINDIAGXADR'] = self.MAINDIAGXADR
        self.MAINDIAGINCR = RM_Field_MSC_PATDIAGCTRL_MAINDIAGINCR(self)
        self.zz_fdict['MAINDIAGINCR'] = self.MAINDIAGINCR
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_PATADDR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_PATADDR, self).__init__(rmio, label,
            0x400e0000, 0x128,
            'PATADDR', 'MSC.PATADDR', 'read-only',
            "",
            0x00000000, 0xFFFFFFFF)

        self.PATADDR = RM_Field_MSC_PATADDR_PATADDR(self)
        self.zz_fdict['PATADDR'] = self.PATADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_PATDONEADDR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_PATDONEADDR, self).__init__(rmio, label,
            0x400e0000, 0x12C,
            'PATDONEADDR', 'MSC.PATDONEADDR', 'read-write',
            "",
            0xFFFFFFFF, 0xFFFFFFFF)

        self.PATDONEADDR = RM_Field_MSC_PATDONEADDR_PATDONEADDR(self)
        self.zz_fdict['PATDONEADDR'] = self.PATDONEADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_PATSTATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_PATSTATUS, self).__init__(rmio, label,
            0x400e0000, 0x130,
            'PATSTATUS', 'MSC.PATSTATUS', 'read-only',
            "",
            0x00000030, 0x80000031)

        self.PATDONE = RM_Field_MSC_PATSTATUS_PATDONE(self)
        self.zz_fdict['PATDONE'] = self.PATDONE
        self.INST0PATPASS = RM_Field_MSC_PATSTATUS_INST0PATPASS(self)
        self.zz_fdict['INST0PATPASS'] = self.INST0PATPASS
        self.INST1PATPASS = RM_Field_MSC_PATSTATUS_INST1PATPASS(self)
        self.zz_fdict['INST1PATPASS'] = self.INST1PATPASS
        self.INTERFACERDY = RM_Field_MSC_PATSTATUS_INTERFACERDY(self)
        self.zz_fdict['INTERFACERDY'] = self.INTERFACERDY
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_TESTTC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_TESTTC0, self).__init__(rmio, label,
            0x400e0000, 0x134,
            'TESTTC0', 'MSC.TESTTC0', 'read-only',
            "",
            0x00000000, 0x03FF03FF)

        self.TC0 = RM_Field_MSC_TESTTC0_TC0(self)
        self.zz_fdict['TC0'] = self.TC0
        self.TC1 = RM_Field_MSC_TESTTC0_TC1(self)
        self.zz_fdict['TC1'] = self.TC1
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_TESTREDUNDANCY(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_TESTREDUNDANCY, self).__init__(rmio, label,
            0x400e0000, 0x13C,
            'TESTREDUNDANCY', 'MSC.TESTREDUNDANCY', 'read-write',
            "",
            0x00000000, 0x00010003)

        self.REDEN = RM_Field_MSC_TESTREDUNDANCY_REDEN(self)
        self.zz_fdict['REDEN'] = self.REDEN
        self.IFREN1 = RM_Field_MSC_TESTREDUNDANCY_IFREN1(self)
        self.zz_fdict['IFREN1'] = self.IFREN1
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_INST0_DOUT0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_INST0_DOUT0, self).__init__(rmio, label,
            0x400e0000, 0x140,
            'INST0_DOUT0', 'MSC.INST0_DOUT0', 'read-only',
            "",
            0xFFFFFFFF, 0xFFFFFFFF)

        self.DOUT0 = RM_Field_MSC_INST0_DOUT0_DOUT0(self)
        self.zz_fdict['DOUT0'] = self.DOUT0
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_INST0_DOUT1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_INST0_DOUT1, self).__init__(rmio, label,
            0x400e0000, 0x144,
            'INST0_DOUT1', 'MSC.INST0_DOUT1', 'read-only',
            "",
            0xFFFFFFFF, 0xFFFFFFFF)

        self.DOUT1 = RM_Field_MSC_INST0_DOUT1_DOUT1(self)
        self.zz_fdict['DOUT1'] = self.DOUT1
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_INST1_DOUT0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_INST1_DOUT0, self).__init__(rmio, label,
            0x400e0000, 0x150,
            'INST1_DOUT0', 'MSC.INST1_DOUT0', 'read-only',
            "",
            0xFFFFFFFF, 0xFFFFFFFF)

        self.DOUT0 = RM_Field_MSC_INST1_DOUT0_DOUT0(self)
        self.zz_fdict['DOUT0'] = self.DOUT0
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_INST1_DOUT1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_INST1_DOUT1, self).__init__(rmio, label,
            0x400e0000, 0x154,
            'INST1_DOUT1', 'MSC.INST1_DOUT1', 'read-only',
            "",
            0xFFFFFFFF, 0xFFFFFFFF)

        self.DOUT1 = RM_Field_MSC_INST1_DOUT1_DOUT1(self)
        self.zz_fdict['DOUT1'] = self.DOUT1
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_REPINST0_REPADDR0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_REPINST0_REPADDR0, self).__init__(rmio, label,
            0x400e0000, 0x180,
            'REPINST0_REPADDR0', 'MSC.REPINST0_REPADDR0', 'read-write',
            "",
            0x00000001, 0x0000FFFF)

        self.REPINVALID = RM_Field_MSC_REPINST0_REPADDR0_REPINVALID(self)
        self.zz_fdict['REPINVALID'] = self.REPINVALID
        self.REPADDR = RM_Field_MSC_REPINST0_REPADDR0_REPADDR(self)
        self.zz_fdict['REPADDR'] = self.REPADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_REPINST0_REPADDR1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_REPINST0_REPADDR1, self).__init__(rmio, label,
            0x400e0000, 0x184,
            'REPINST0_REPADDR1', 'MSC.REPINST0_REPADDR1', 'read-write',
            "",
            0x00000001, 0x0000FFFF)

        self.REPINVALID = RM_Field_MSC_REPINST0_REPADDR1_REPINVALID(self)
        self.zz_fdict['REPINVALID'] = self.REPINVALID
        self.REPADDR = RM_Field_MSC_REPINST0_REPADDR1_REPADDR(self)
        self.zz_fdict['REPADDR'] = self.REPADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_REPINST1_REPADDR0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_REPINST1_REPADDR0, self).__init__(rmio, label,
            0x400e0000, 0x1A0,
            'REPINST1_REPADDR0', 'MSC.REPINST1_REPADDR0', 'read-write',
            "",
            0x00000001, 0x0000FFFF)

        self.REPINVALID = RM_Field_MSC_REPINST1_REPADDR0_REPINVALID(self)
        self.zz_fdict['REPINVALID'] = self.REPINVALID
        self.REPADDR = RM_Field_MSC_REPINST1_REPADDR0_REPADDR(self)
        self.zz_fdict['REPADDR'] = self.REPADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_REPINST1_REPADDR1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_REPINST1_REPADDR1, self).__init__(rmio, label,
            0x400e0000, 0x1A4,
            'REPINST1_REPADDR1', 'MSC.REPINST1_REPADDR1', 'read-write',
            "",
            0x00000001, 0x0000FFFF)

        self.REPINVALID = RM_Field_MSC_REPINST1_REPADDR1_REPINVALID(self)
        self.zz_fdict['REPINVALID'] = self.REPINVALID
        self.REPADDR = RM_Field_MSC_REPINST1_REPADDR1_REPADDR(self)
        self.zz_fdict['REPADDR'] = self.REPADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE0_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE0_DATA, self).__init__(rmio, label,
            0x400e0000, 0x200,
            'CACHE0_DATA', 'MSC.CACHE0_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE0_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE1_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE1_DATA, self).__init__(rmio, label,
            0x400e0000, 0x204,
            'CACHE1_DATA', 'MSC.CACHE1_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE1_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE2_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE2_DATA, self).__init__(rmio, label,
            0x400e0000, 0x208,
            'CACHE2_DATA', 'MSC.CACHE2_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE2_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE3_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE3_DATA, self).__init__(rmio, label,
            0x400e0000, 0x20C,
            'CACHE3_DATA', 'MSC.CACHE3_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE3_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE4_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE4_DATA, self).__init__(rmio, label,
            0x400e0000, 0x210,
            'CACHE4_DATA', 'MSC.CACHE4_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE4_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE5_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE5_DATA, self).__init__(rmio, label,
            0x400e0000, 0x214,
            'CACHE5_DATA', 'MSC.CACHE5_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE5_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE6_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE6_DATA, self).__init__(rmio, label,
            0x400e0000, 0x218,
            'CACHE6_DATA', 'MSC.CACHE6_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE6_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE7_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE7_DATA, self).__init__(rmio, label,
            0x400e0000, 0x21C,
            'CACHE7_DATA', 'MSC.CACHE7_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE7_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE8_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE8_DATA, self).__init__(rmio, label,
            0x400e0000, 0x220,
            'CACHE8_DATA', 'MSC.CACHE8_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE8_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE9_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE9_DATA, self).__init__(rmio, label,
            0x400e0000, 0x224,
            'CACHE9_DATA', 'MSC.CACHE9_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE9_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE10_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE10_DATA, self).__init__(rmio, label,
            0x400e0000, 0x228,
            'CACHE10_DATA', 'MSC.CACHE10_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE10_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE11_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE11_DATA, self).__init__(rmio, label,
            0x400e0000, 0x22C,
            'CACHE11_DATA', 'MSC.CACHE11_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE11_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE12_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE12_DATA, self).__init__(rmio, label,
            0x400e0000, 0x230,
            'CACHE12_DATA', 'MSC.CACHE12_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE12_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE13_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE13_DATA, self).__init__(rmio, label,
            0x400e0000, 0x234,
            'CACHE13_DATA', 'MSC.CACHE13_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE13_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE14_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE14_DATA, self).__init__(rmio, label,
            0x400e0000, 0x238,
            'CACHE14_DATA', 'MSC.CACHE14_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE14_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE15_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE15_DATA, self).__init__(rmio, label,
            0x400e0000, 0x23C,
            'CACHE15_DATA', 'MSC.CACHE15_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE15_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE16_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE16_DATA, self).__init__(rmio, label,
            0x400e0000, 0x240,
            'CACHE16_DATA', 'MSC.CACHE16_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE16_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE17_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE17_DATA, self).__init__(rmio, label,
            0x400e0000, 0x244,
            'CACHE17_DATA', 'MSC.CACHE17_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE17_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE18_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE18_DATA, self).__init__(rmio, label,
            0x400e0000, 0x248,
            'CACHE18_DATA', 'MSC.CACHE18_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE18_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE19_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE19_DATA, self).__init__(rmio, label,
            0x400e0000, 0x24C,
            'CACHE19_DATA', 'MSC.CACHE19_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE19_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE20_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE20_DATA, self).__init__(rmio, label,
            0x400e0000, 0x250,
            'CACHE20_DATA', 'MSC.CACHE20_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE20_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE21_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE21_DATA, self).__init__(rmio, label,
            0x400e0000, 0x254,
            'CACHE21_DATA', 'MSC.CACHE21_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE21_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE22_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE22_DATA, self).__init__(rmio, label,
            0x400e0000, 0x258,
            'CACHE22_DATA', 'MSC.CACHE22_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE22_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE23_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE23_DATA, self).__init__(rmio, label,
            0x400e0000, 0x25C,
            'CACHE23_DATA', 'MSC.CACHE23_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE23_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE24_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE24_DATA, self).__init__(rmio, label,
            0x400e0000, 0x260,
            'CACHE24_DATA', 'MSC.CACHE24_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE24_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE25_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE25_DATA, self).__init__(rmio, label,
            0x400e0000, 0x264,
            'CACHE25_DATA', 'MSC.CACHE25_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE25_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE26_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE26_DATA, self).__init__(rmio, label,
            0x400e0000, 0x268,
            'CACHE26_DATA', 'MSC.CACHE26_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE26_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE27_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE27_DATA, self).__init__(rmio, label,
            0x400e0000, 0x26C,
            'CACHE27_DATA', 'MSC.CACHE27_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE27_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE28_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE28_DATA, self).__init__(rmio, label,
            0x400e0000, 0x270,
            'CACHE28_DATA', 'MSC.CACHE28_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE28_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE29_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE29_DATA, self).__init__(rmio, label,
            0x400e0000, 0x274,
            'CACHE29_DATA', 'MSC.CACHE29_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE29_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE30_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE30_DATA, self).__init__(rmio, label,
            0x400e0000, 0x278,
            'CACHE30_DATA', 'MSC.CACHE30_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE30_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE31_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE31_DATA, self).__init__(rmio, label,
            0x400e0000, 0x27C,
            'CACHE31_DATA', 'MSC.CACHE31_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE31_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE32_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE32_DATA, self).__init__(rmio, label,
            0x400e0000, 0x280,
            'CACHE32_DATA', 'MSC.CACHE32_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE32_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE33_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE33_DATA, self).__init__(rmio, label,
            0x400e0000, 0x284,
            'CACHE33_DATA', 'MSC.CACHE33_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE33_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE34_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE34_DATA, self).__init__(rmio, label,
            0x400e0000, 0x288,
            'CACHE34_DATA', 'MSC.CACHE34_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE34_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE35_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE35_DATA, self).__init__(rmio, label,
            0x400e0000, 0x28C,
            'CACHE35_DATA', 'MSC.CACHE35_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE35_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE36_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE36_DATA, self).__init__(rmio, label,
            0x400e0000, 0x290,
            'CACHE36_DATA', 'MSC.CACHE36_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE36_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE37_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE37_DATA, self).__init__(rmio, label,
            0x400e0000, 0x294,
            'CACHE37_DATA', 'MSC.CACHE37_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE37_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE38_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE38_DATA, self).__init__(rmio, label,
            0x400e0000, 0x298,
            'CACHE38_DATA', 'MSC.CACHE38_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE38_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE39_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE39_DATA, self).__init__(rmio, label,
            0x400e0000, 0x29C,
            'CACHE39_DATA', 'MSC.CACHE39_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE39_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE40_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE40_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2A0,
            'CACHE40_DATA', 'MSC.CACHE40_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE40_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE41_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE41_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2A4,
            'CACHE41_DATA', 'MSC.CACHE41_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE41_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE42_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE42_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2A8,
            'CACHE42_DATA', 'MSC.CACHE42_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE42_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE43_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE43_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2AC,
            'CACHE43_DATA', 'MSC.CACHE43_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE43_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE44_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE44_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2B0,
            'CACHE44_DATA', 'MSC.CACHE44_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE44_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE45_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE45_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2B4,
            'CACHE45_DATA', 'MSC.CACHE45_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE45_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE46_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE46_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2B8,
            'CACHE46_DATA', 'MSC.CACHE46_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE46_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE47_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE47_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2BC,
            'CACHE47_DATA', 'MSC.CACHE47_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE47_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE48_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE48_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2C0,
            'CACHE48_DATA', 'MSC.CACHE48_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE48_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE49_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE49_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2C4,
            'CACHE49_DATA', 'MSC.CACHE49_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE49_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE50_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE50_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2C8,
            'CACHE50_DATA', 'MSC.CACHE50_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE50_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE51_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE51_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2CC,
            'CACHE51_DATA', 'MSC.CACHE51_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE51_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE52_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE52_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2D0,
            'CACHE52_DATA', 'MSC.CACHE52_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE52_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE53_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE53_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2D4,
            'CACHE53_DATA', 'MSC.CACHE53_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE53_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE54_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE54_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2D8,
            'CACHE54_DATA', 'MSC.CACHE54_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE54_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE55_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE55_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2DC,
            'CACHE55_DATA', 'MSC.CACHE55_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE55_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE56_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE56_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2E0,
            'CACHE56_DATA', 'MSC.CACHE56_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE56_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE57_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE57_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2E4,
            'CACHE57_DATA', 'MSC.CACHE57_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE57_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE58_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE58_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2E8,
            'CACHE58_DATA', 'MSC.CACHE58_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE58_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE59_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE59_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2EC,
            'CACHE59_DATA', 'MSC.CACHE59_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE59_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE60_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE60_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2F0,
            'CACHE60_DATA', 'MSC.CACHE60_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE60_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE61_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE61_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2F4,
            'CACHE61_DATA', 'MSC.CACHE61_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE61_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE62_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE62_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2F8,
            'CACHE62_DATA', 'MSC.CACHE62_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE62_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE63_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE63_DATA, self).__init__(rmio, label,
            0x400e0000, 0x2FC,
            'CACHE63_DATA', 'MSC.CACHE63_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE63_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE64_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE64_DATA, self).__init__(rmio, label,
            0x400e0000, 0x300,
            'CACHE64_DATA', 'MSC.CACHE64_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE64_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE65_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE65_DATA, self).__init__(rmio, label,
            0x400e0000, 0x304,
            'CACHE65_DATA', 'MSC.CACHE65_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE65_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE66_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE66_DATA, self).__init__(rmio, label,
            0x400e0000, 0x308,
            'CACHE66_DATA', 'MSC.CACHE66_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE66_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE67_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE67_DATA, self).__init__(rmio, label,
            0x400e0000, 0x30C,
            'CACHE67_DATA', 'MSC.CACHE67_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE67_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE68_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE68_DATA, self).__init__(rmio, label,
            0x400e0000, 0x310,
            'CACHE68_DATA', 'MSC.CACHE68_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE68_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE69_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE69_DATA, self).__init__(rmio, label,
            0x400e0000, 0x314,
            'CACHE69_DATA', 'MSC.CACHE69_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE69_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE70_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE70_DATA, self).__init__(rmio, label,
            0x400e0000, 0x318,
            'CACHE70_DATA', 'MSC.CACHE70_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE70_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE71_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE71_DATA, self).__init__(rmio, label,
            0x400e0000, 0x31C,
            'CACHE71_DATA', 'MSC.CACHE71_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE71_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE72_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE72_DATA, self).__init__(rmio, label,
            0x400e0000, 0x320,
            'CACHE72_DATA', 'MSC.CACHE72_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE72_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE73_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE73_DATA, self).__init__(rmio, label,
            0x400e0000, 0x324,
            'CACHE73_DATA', 'MSC.CACHE73_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE73_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE74_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE74_DATA, self).__init__(rmio, label,
            0x400e0000, 0x328,
            'CACHE74_DATA', 'MSC.CACHE74_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE74_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE75_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE75_DATA, self).__init__(rmio, label,
            0x400e0000, 0x32C,
            'CACHE75_DATA', 'MSC.CACHE75_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE75_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE76_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE76_DATA, self).__init__(rmio, label,
            0x400e0000, 0x330,
            'CACHE76_DATA', 'MSC.CACHE76_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE76_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE77_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE77_DATA, self).__init__(rmio, label,
            0x400e0000, 0x334,
            'CACHE77_DATA', 'MSC.CACHE77_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE77_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE78_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE78_DATA, self).__init__(rmio, label,
            0x400e0000, 0x338,
            'CACHE78_DATA', 'MSC.CACHE78_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE78_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE79_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE79_DATA, self).__init__(rmio, label,
            0x400e0000, 0x33C,
            'CACHE79_DATA', 'MSC.CACHE79_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE79_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE80_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE80_DATA, self).__init__(rmio, label,
            0x400e0000, 0x340,
            'CACHE80_DATA', 'MSC.CACHE80_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE80_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE81_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE81_DATA, self).__init__(rmio, label,
            0x400e0000, 0x344,
            'CACHE81_DATA', 'MSC.CACHE81_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE81_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE82_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE82_DATA, self).__init__(rmio, label,
            0x400e0000, 0x348,
            'CACHE82_DATA', 'MSC.CACHE82_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE82_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE83_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE83_DATA, self).__init__(rmio, label,
            0x400e0000, 0x34C,
            'CACHE83_DATA', 'MSC.CACHE83_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE83_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE84_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE84_DATA, self).__init__(rmio, label,
            0x400e0000, 0x350,
            'CACHE84_DATA', 'MSC.CACHE84_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE84_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE85_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE85_DATA, self).__init__(rmio, label,
            0x400e0000, 0x354,
            'CACHE85_DATA', 'MSC.CACHE85_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE85_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE86_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE86_DATA, self).__init__(rmio, label,
            0x400e0000, 0x358,
            'CACHE86_DATA', 'MSC.CACHE86_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE86_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE87_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE87_DATA, self).__init__(rmio, label,
            0x400e0000, 0x35C,
            'CACHE87_DATA', 'MSC.CACHE87_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE87_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE88_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE88_DATA, self).__init__(rmio, label,
            0x400e0000, 0x360,
            'CACHE88_DATA', 'MSC.CACHE88_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE88_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE89_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE89_DATA, self).__init__(rmio, label,
            0x400e0000, 0x364,
            'CACHE89_DATA', 'MSC.CACHE89_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE89_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE90_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE90_DATA, self).__init__(rmio, label,
            0x400e0000, 0x368,
            'CACHE90_DATA', 'MSC.CACHE90_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE90_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE91_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE91_DATA, self).__init__(rmio, label,
            0x400e0000, 0x36C,
            'CACHE91_DATA', 'MSC.CACHE91_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE91_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE92_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE92_DATA, self).__init__(rmio, label,
            0x400e0000, 0x370,
            'CACHE92_DATA', 'MSC.CACHE92_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE92_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE93_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE93_DATA, self).__init__(rmio, label,
            0x400e0000, 0x374,
            'CACHE93_DATA', 'MSC.CACHE93_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE93_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE94_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE94_DATA, self).__init__(rmio, label,
            0x400e0000, 0x378,
            'CACHE94_DATA', 'MSC.CACHE94_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE94_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE95_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE95_DATA, self).__init__(rmio, label,
            0x400e0000, 0x37C,
            'CACHE95_DATA', 'MSC.CACHE95_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE95_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE96_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE96_DATA, self).__init__(rmio, label,
            0x400e0000, 0x380,
            'CACHE96_DATA', 'MSC.CACHE96_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE96_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE97_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE97_DATA, self).__init__(rmio, label,
            0x400e0000, 0x384,
            'CACHE97_DATA', 'MSC.CACHE97_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE97_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE98_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE98_DATA, self).__init__(rmio, label,
            0x400e0000, 0x388,
            'CACHE98_DATA', 'MSC.CACHE98_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE98_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE99_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE99_DATA, self).__init__(rmio, label,
            0x400e0000, 0x38C,
            'CACHE99_DATA', 'MSC.CACHE99_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE99_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE100_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE100_DATA, self).__init__(rmio, label,
            0x400e0000, 0x390,
            'CACHE100_DATA', 'MSC.CACHE100_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE100_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE101_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE101_DATA, self).__init__(rmio, label,
            0x400e0000, 0x394,
            'CACHE101_DATA', 'MSC.CACHE101_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE101_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE102_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE102_DATA, self).__init__(rmio, label,
            0x400e0000, 0x398,
            'CACHE102_DATA', 'MSC.CACHE102_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE102_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE103_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE103_DATA, self).__init__(rmio, label,
            0x400e0000, 0x39C,
            'CACHE103_DATA', 'MSC.CACHE103_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE103_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE104_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE104_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3A0,
            'CACHE104_DATA', 'MSC.CACHE104_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE104_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE105_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE105_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3A4,
            'CACHE105_DATA', 'MSC.CACHE105_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE105_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE106_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE106_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3A8,
            'CACHE106_DATA', 'MSC.CACHE106_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE106_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE107_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE107_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3AC,
            'CACHE107_DATA', 'MSC.CACHE107_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE107_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE108_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE108_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3B0,
            'CACHE108_DATA', 'MSC.CACHE108_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE108_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE109_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE109_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3B4,
            'CACHE109_DATA', 'MSC.CACHE109_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE109_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE110_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE110_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3B8,
            'CACHE110_DATA', 'MSC.CACHE110_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE110_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE111_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE111_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3BC,
            'CACHE111_DATA', 'MSC.CACHE111_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE111_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE112_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE112_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3C0,
            'CACHE112_DATA', 'MSC.CACHE112_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE112_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE113_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE113_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3C4,
            'CACHE113_DATA', 'MSC.CACHE113_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE113_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE114_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE114_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3C8,
            'CACHE114_DATA', 'MSC.CACHE114_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE114_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE115_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE115_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3CC,
            'CACHE115_DATA', 'MSC.CACHE115_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE115_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE116_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE116_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3D0,
            'CACHE116_DATA', 'MSC.CACHE116_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE116_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE117_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE117_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3D4,
            'CACHE117_DATA', 'MSC.CACHE117_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE117_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE118_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE118_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3D8,
            'CACHE118_DATA', 'MSC.CACHE118_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE118_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE119_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE119_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3DC,
            'CACHE119_DATA', 'MSC.CACHE119_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE119_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE120_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE120_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3E0,
            'CACHE120_DATA', 'MSC.CACHE120_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE120_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE121_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE121_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3E4,
            'CACHE121_DATA', 'MSC.CACHE121_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE121_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE122_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE122_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3E8,
            'CACHE122_DATA', 'MSC.CACHE122_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE122_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE123_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE123_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3EC,
            'CACHE123_DATA', 'MSC.CACHE123_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE123_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE124_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE124_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3F0,
            'CACHE124_DATA', 'MSC.CACHE124_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE124_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE125_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE125_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3F4,
            'CACHE125_DATA', 'MSC.CACHE125_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE125_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE126_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE126_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3F8,
            'CACHE126_DATA', 'MSC.CACHE126_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE126_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE127_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE127_DATA, self).__init__(rmio, label,
            0x400e0000, 0x3FC,
            'CACHE127_DATA', 'MSC.CACHE127_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE127_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE128_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE128_DATA, self).__init__(rmio, label,
            0x400e0000, 0x400,
            'CACHE128_DATA', 'MSC.CACHE128_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE128_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE129_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE129_DATA, self).__init__(rmio, label,
            0x400e0000, 0x404,
            'CACHE129_DATA', 'MSC.CACHE129_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE129_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE130_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE130_DATA, self).__init__(rmio, label,
            0x400e0000, 0x408,
            'CACHE130_DATA', 'MSC.CACHE130_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE130_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE131_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE131_DATA, self).__init__(rmio, label,
            0x400e0000, 0x40C,
            'CACHE131_DATA', 'MSC.CACHE131_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE131_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE132_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE132_DATA, self).__init__(rmio, label,
            0x400e0000, 0x410,
            'CACHE132_DATA', 'MSC.CACHE132_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE132_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE133_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE133_DATA, self).__init__(rmio, label,
            0x400e0000, 0x414,
            'CACHE133_DATA', 'MSC.CACHE133_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE133_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE134_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE134_DATA, self).__init__(rmio, label,
            0x400e0000, 0x418,
            'CACHE134_DATA', 'MSC.CACHE134_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE134_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE135_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE135_DATA, self).__init__(rmio, label,
            0x400e0000, 0x41C,
            'CACHE135_DATA', 'MSC.CACHE135_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE135_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE136_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE136_DATA, self).__init__(rmio, label,
            0x400e0000, 0x420,
            'CACHE136_DATA', 'MSC.CACHE136_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE136_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE137_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE137_DATA, self).__init__(rmio, label,
            0x400e0000, 0x424,
            'CACHE137_DATA', 'MSC.CACHE137_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE137_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE138_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE138_DATA, self).__init__(rmio, label,
            0x400e0000, 0x428,
            'CACHE138_DATA', 'MSC.CACHE138_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE138_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE139_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE139_DATA, self).__init__(rmio, label,
            0x400e0000, 0x42C,
            'CACHE139_DATA', 'MSC.CACHE139_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE139_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE140_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE140_DATA, self).__init__(rmio, label,
            0x400e0000, 0x430,
            'CACHE140_DATA', 'MSC.CACHE140_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE140_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE141_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE141_DATA, self).__init__(rmio, label,
            0x400e0000, 0x434,
            'CACHE141_DATA', 'MSC.CACHE141_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE141_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE142_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE142_DATA, self).__init__(rmio, label,
            0x400e0000, 0x438,
            'CACHE142_DATA', 'MSC.CACHE142_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE142_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE143_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE143_DATA, self).__init__(rmio, label,
            0x400e0000, 0x43C,
            'CACHE143_DATA', 'MSC.CACHE143_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE143_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE144_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE144_DATA, self).__init__(rmio, label,
            0x400e0000, 0x440,
            'CACHE144_DATA', 'MSC.CACHE144_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE144_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE145_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE145_DATA, self).__init__(rmio, label,
            0x400e0000, 0x444,
            'CACHE145_DATA', 'MSC.CACHE145_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE145_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE146_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE146_DATA, self).__init__(rmio, label,
            0x400e0000, 0x448,
            'CACHE146_DATA', 'MSC.CACHE146_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE146_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE147_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE147_DATA, self).__init__(rmio, label,
            0x400e0000, 0x44C,
            'CACHE147_DATA', 'MSC.CACHE147_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE147_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE148_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE148_DATA, self).__init__(rmio, label,
            0x400e0000, 0x450,
            'CACHE148_DATA', 'MSC.CACHE148_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE148_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE149_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE149_DATA, self).__init__(rmio, label,
            0x400e0000, 0x454,
            'CACHE149_DATA', 'MSC.CACHE149_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE149_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE150_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE150_DATA, self).__init__(rmio, label,
            0x400e0000, 0x458,
            'CACHE150_DATA', 'MSC.CACHE150_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE150_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE151_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE151_DATA, self).__init__(rmio, label,
            0x400e0000, 0x45C,
            'CACHE151_DATA', 'MSC.CACHE151_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE151_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE152_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE152_DATA, self).__init__(rmio, label,
            0x400e0000, 0x460,
            'CACHE152_DATA', 'MSC.CACHE152_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE152_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE153_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE153_DATA, self).__init__(rmio, label,
            0x400e0000, 0x464,
            'CACHE153_DATA', 'MSC.CACHE153_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE153_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE154_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE154_DATA, self).__init__(rmio, label,
            0x400e0000, 0x468,
            'CACHE154_DATA', 'MSC.CACHE154_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE154_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE155_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE155_DATA, self).__init__(rmio, label,
            0x400e0000, 0x46C,
            'CACHE155_DATA', 'MSC.CACHE155_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE155_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE156_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE156_DATA, self).__init__(rmio, label,
            0x400e0000, 0x470,
            'CACHE156_DATA', 'MSC.CACHE156_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE156_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE157_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE157_DATA, self).__init__(rmio, label,
            0x400e0000, 0x474,
            'CACHE157_DATA', 'MSC.CACHE157_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE157_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE158_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE158_DATA, self).__init__(rmio, label,
            0x400e0000, 0x478,
            'CACHE158_DATA', 'MSC.CACHE158_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE158_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE159_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE159_DATA, self).__init__(rmio, label,
            0x400e0000, 0x47C,
            'CACHE159_DATA', 'MSC.CACHE159_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE159_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE160_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE160_DATA, self).__init__(rmio, label,
            0x400e0000, 0x480,
            'CACHE160_DATA', 'MSC.CACHE160_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE160_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE161_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE161_DATA, self).__init__(rmio, label,
            0x400e0000, 0x484,
            'CACHE161_DATA', 'MSC.CACHE161_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE161_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE162_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE162_DATA, self).__init__(rmio, label,
            0x400e0000, 0x488,
            'CACHE162_DATA', 'MSC.CACHE162_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE162_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE163_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE163_DATA, self).__init__(rmio, label,
            0x400e0000, 0x48C,
            'CACHE163_DATA', 'MSC.CACHE163_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE163_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE164_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE164_DATA, self).__init__(rmio, label,
            0x400e0000, 0x490,
            'CACHE164_DATA', 'MSC.CACHE164_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE164_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE165_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE165_DATA, self).__init__(rmio, label,
            0x400e0000, 0x494,
            'CACHE165_DATA', 'MSC.CACHE165_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE165_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE166_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE166_DATA, self).__init__(rmio, label,
            0x400e0000, 0x498,
            'CACHE166_DATA', 'MSC.CACHE166_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE166_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE167_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE167_DATA, self).__init__(rmio, label,
            0x400e0000, 0x49C,
            'CACHE167_DATA', 'MSC.CACHE167_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE167_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE168_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE168_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4A0,
            'CACHE168_DATA', 'MSC.CACHE168_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE168_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE169_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE169_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4A4,
            'CACHE169_DATA', 'MSC.CACHE169_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE169_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE170_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE170_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4A8,
            'CACHE170_DATA', 'MSC.CACHE170_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE170_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE171_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE171_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4AC,
            'CACHE171_DATA', 'MSC.CACHE171_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE171_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE172_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE172_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4B0,
            'CACHE172_DATA', 'MSC.CACHE172_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE172_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE173_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE173_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4B4,
            'CACHE173_DATA', 'MSC.CACHE173_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE173_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE174_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE174_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4B8,
            'CACHE174_DATA', 'MSC.CACHE174_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE174_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE175_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE175_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4BC,
            'CACHE175_DATA', 'MSC.CACHE175_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE175_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE176_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE176_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4C0,
            'CACHE176_DATA', 'MSC.CACHE176_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE176_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE177_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE177_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4C4,
            'CACHE177_DATA', 'MSC.CACHE177_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE177_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE178_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE178_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4C8,
            'CACHE178_DATA', 'MSC.CACHE178_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE178_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE179_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE179_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4CC,
            'CACHE179_DATA', 'MSC.CACHE179_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE179_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE180_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE180_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4D0,
            'CACHE180_DATA', 'MSC.CACHE180_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE180_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE181_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE181_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4D4,
            'CACHE181_DATA', 'MSC.CACHE181_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE181_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE182_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE182_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4D8,
            'CACHE182_DATA', 'MSC.CACHE182_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE182_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE183_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE183_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4DC,
            'CACHE183_DATA', 'MSC.CACHE183_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE183_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE184_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE184_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4E0,
            'CACHE184_DATA', 'MSC.CACHE184_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE184_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE185_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE185_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4E4,
            'CACHE185_DATA', 'MSC.CACHE185_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE185_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE186_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE186_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4E8,
            'CACHE186_DATA', 'MSC.CACHE186_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE186_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE187_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE187_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4EC,
            'CACHE187_DATA', 'MSC.CACHE187_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE187_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE188_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE188_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4F0,
            'CACHE188_DATA', 'MSC.CACHE188_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE188_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE189_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE189_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4F4,
            'CACHE189_DATA', 'MSC.CACHE189_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE189_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE190_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE190_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4F8,
            'CACHE190_DATA', 'MSC.CACHE190_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE190_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE191_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE191_DATA, self).__init__(rmio, label,
            0x400e0000, 0x4FC,
            'CACHE191_DATA', 'MSC.CACHE191_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE191_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE192_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE192_DATA, self).__init__(rmio, label,
            0x400e0000, 0x500,
            'CACHE192_DATA', 'MSC.CACHE192_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE192_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE193_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE193_DATA, self).__init__(rmio, label,
            0x400e0000, 0x504,
            'CACHE193_DATA', 'MSC.CACHE193_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE193_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE194_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE194_DATA, self).__init__(rmio, label,
            0x400e0000, 0x508,
            'CACHE194_DATA', 'MSC.CACHE194_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE194_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE195_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE195_DATA, self).__init__(rmio, label,
            0x400e0000, 0x50C,
            'CACHE195_DATA', 'MSC.CACHE195_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE195_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE196_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE196_DATA, self).__init__(rmio, label,
            0x400e0000, 0x510,
            'CACHE196_DATA', 'MSC.CACHE196_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE196_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE197_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE197_DATA, self).__init__(rmio, label,
            0x400e0000, 0x514,
            'CACHE197_DATA', 'MSC.CACHE197_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE197_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE198_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE198_DATA, self).__init__(rmio, label,
            0x400e0000, 0x518,
            'CACHE198_DATA', 'MSC.CACHE198_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE198_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE199_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE199_DATA, self).__init__(rmio, label,
            0x400e0000, 0x51C,
            'CACHE199_DATA', 'MSC.CACHE199_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE199_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE200_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE200_DATA, self).__init__(rmio, label,
            0x400e0000, 0x520,
            'CACHE200_DATA', 'MSC.CACHE200_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE200_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE201_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE201_DATA, self).__init__(rmio, label,
            0x400e0000, 0x524,
            'CACHE201_DATA', 'MSC.CACHE201_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE201_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE202_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE202_DATA, self).__init__(rmio, label,
            0x400e0000, 0x528,
            'CACHE202_DATA', 'MSC.CACHE202_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE202_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE203_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE203_DATA, self).__init__(rmio, label,
            0x400e0000, 0x52C,
            'CACHE203_DATA', 'MSC.CACHE203_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE203_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE204_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE204_DATA, self).__init__(rmio, label,
            0x400e0000, 0x530,
            'CACHE204_DATA', 'MSC.CACHE204_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE204_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE205_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE205_DATA, self).__init__(rmio, label,
            0x400e0000, 0x534,
            'CACHE205_DATA', 'MSC.CACHE205_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE205_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE206_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE206_DATA, self).__init__(rmio, label,
            0x400e0000, 0x538,
            'CACHE206_DATA', 'MSC.CACHE206_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE206_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE207_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE207_DATA, self).__init__(rmio, label,
            0x400e0000, 0x53C,
            'CACHE207_DATA', 'MSC.CACHE207_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE207_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE208_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE208_DATA, self).__init__(rmio, label,
            0x400e0000, 0x540,
            'CACHE208_DATA', 'MSC.CACHE208_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE208_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE209_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE209_DATA, self).__init__(rmio, label,
            0x400e0000, 0x544,
            'CACHE209_DATA', 'MSC.CACHE209_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE209_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE210_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE210_DATA, self).__init__(rmio, label,
            0x400e0000, 0x548,
            'CACHE210_DATA', 'MSC.CACHE210_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE210_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE211_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE211_DATA, self).__init__(rmio, label,
            0x400e0000, 0x54C,
            'CACHE211_DATA', 'MSC.CACHE211_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE211_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE212_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE212_DATA, self).__init__(rmio, label,
            0x400e0000, 0x550,
            'CACHE212_DATA', 'MSC.CACHE212_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE212_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE213_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE213_DATA, self).__init__(rmio, label,
            0x400e0000, 0x554,
            'CACHE213_DATA', 'MSC.CACHE213_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE213_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE214_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE214_DATA, self).__init__(rmio, label,
            0x400e0000, 0x558,
            'CACHE214_DATA', 'MSC.CACHE214_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE214_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE215_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE215_DATA, self).__init__(rmio, label,
            0x400e0000, 0x55C,
            'CACHE215_DATA', 'MSC.CACHE215_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE215_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE216_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE216_DATA, self).__init__(rmio, label,
            0x400e0000, 0x560,
            'CACHE216_DATA', 'MSC.CACHE216_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE216_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE217_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE217_DATA, self).__init__(rmio, label,
            0x400e0000, 0x564,
            'CACHE217_DATA', 'MSC.CACHE217_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE217_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE218_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE218_DATA, self).__init__(rmio, label,
            0x400e0000, 0x568,
            'CACHE218_DATA', 'MSC.CACHE218_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE218_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE219_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE219_DATA, self).__init__(rmio, label,
            0x400e0000, 0x56C,
            'CACHE219_DATA', 'MSC.CACHE219_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE219_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE220_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE220_DATA, self).__init__(rmio, label,
            0x400e0000, 0x570,
            'CACHE220_DATA', 'MSC.CACHE220_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE220_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE221_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE221_DATA, self).__init__(rmio, label,
            0x400e0000, 0x574,
            'CACHE221_DATA', 'MSC.CACHE221_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE221_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE222_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE222_DATA, self).__init__(rmio, label,
            0x400e0000, 0x578,
            'CACHE222_DATA', 'MSC.CACHE222_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE222_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE223_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE223_DATA, self).__init__(rmio, label,
            0x400e0000, 0x57C,
            'CACHE223_DATA', 'MSC.CACHE223_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE223_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE224_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE224_DATA, self).__init__(rmio, label,
            0x400e0000, 0x580,
            'CACHE224_DATA', 'MSC.CACHE224_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE224_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE225_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE225_DATA, self).__init__(rmio, label,
            0x400e0000, 0x584,
            'CACHE225_DATA', 'MSC.CACHE225_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE225_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE226_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE226_DATA, self).__init__(rmio, label,
            0x400e0000, 0x588,
            'CACHE226_DATA', 'MSC.CACHE226_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE226_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE227_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE227_DATA, self).__init__(rmio, label,
            0x400e0000, 0x58C,
            'CACHE227_DATA', 'MSC.CACHE227_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE227_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE228_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE228_DATA, self).__init__(rmio, label,
            0x400e0000, 0x590,
            'CACHE228_DATA', 'MSC.CACHE228_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE228_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE229_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE229_DATA, self).__init__(rmio, label,
            0x400e0000, 0x594,
            'CACHE229_DATA', 'MSC.CACHE229_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE229_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE230_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE230_DATA, self).__init__(rmio, label,
            0x400e0000, 0x598,
            'CACHE230_DATA', 'MSC.CACHE230_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE230_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE231_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE231_DATA, self).__init__(rmio, label,
            0x400e0000, 0x59C,
            'CACHE231_DATA', 'MSC.CACHE231_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE231_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE232_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE232_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5A0,
            'CACHE232_DATA', 'MSC.CACHE232_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE232_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE233_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE233_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5A4,
            'CACHE233_DATA', 'MSC.CACHE233_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE233_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE234_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE234_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5A8,
            'CACHE234_DATA', 'MSC.CACHE234_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE234_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE235_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE235_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5AC,
            'CACHE235_DATA', 'MSC.CACHE235_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE235_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE236_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE236_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5B0,
            'CACHE236_DATA', 'MSC.CACHE236_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE236_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE237_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE237_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5B4,
            'CACHE237_DATA', 'MSC.CACHE237_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE237_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE238_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE238_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5B8,
            'CACHE238_DATA', 'MSC.CACHE238_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE238_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE239_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE239_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5BC,
            'CACHE239_DATA', 'MSC.CACHE239_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE239_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE240_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE240_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5C0,
            'CACHE240_DATA', 'MSC.CACHE240_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE240_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE241_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE241_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5C4,
            'CACHE241_DATA', 'MSC.CACHE241_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE241_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE242_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE242_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5C8,
            'CACHE242_DATA', 'MSC.CACHE242_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE242_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE243_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE243_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5CC,
            'CACHE243_DATA', 'MSC.CACHE243_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE243_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE244_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE244_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5D0,
            'CACHE244_DATA', 'MSC.CACHE244_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE244_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE245_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE245_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5D4,
            'CACHE245_DATA', 'MSC.CACHE245_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE245_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE246_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE246_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5D8,
            'CACHE246_DATA', 'MSC.CACHE246_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE246_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE247_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE247_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5DC,
            'CACHE247_DATA', 'MSC.CACHE247_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE247_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE248_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE248_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5E0,
            'CACHE248_DATA', 'MSC.CACHE248_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE248_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE249_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE249_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5E4,
            'CACHE249_DATA', 'MSC.CACHE249_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE249_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE250_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE250_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5E8,
            'CACHE250_DATA', 'MSC.CACHE250_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE250_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE251_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE251_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5EC,
            'CACHE251_DATA', 'MSC.CACHE251_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE251_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE252_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE252_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5F0,
            'CACHE252_DATA', 'MSC.CACHE252_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE252_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE253_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE253_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5F4,
            'CACHE253_DATA', 'MSC.CACHE253_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE253_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE254_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE254_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5F8,
            'CACHE254_DATA', 'MSC.CACHE254_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE254_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


class RM_Register_MSC_CACHE255_DATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MSC_CACHE255_DATA, self).__init__(rmio, label,
            0x400e0000, 0x5FC,
            'CACHE255_DATA', 'MSC.CACHE255_DATA', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DATA = RM_Field_MSC_CACHE255_DATA_DATA(self)
        self.zz_fdict['DATA'] = self.DATA
        self.__dict__['zz_frozen'] = True


