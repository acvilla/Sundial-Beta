
from static import Base_RM_Register
from CM4_field import *


class RM_Register_CM4_NVICAUXCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICAUXCTRL, self).__init__(rmio, label,
            0xe0000000, 0xE008,
            'NVICAUXCTRL', 'CM4.NVICAUXCTRL', 'read-write',
            "",
            0x00000000, 0x00000007)

        self.DISMCYCINT = RM_Field_CM4_NVICAUXCTRL_DISMCYCINT(self)
        self.zz_fdict['DISMCYCINT'] = self.DISMCYCINT
        self.DISDEFWBUF = RM_Field_CM4_NVICAUXCTRL_DISDEFWBUF(self)
        self.zz_fdict['DISDEFWBUF'] = self.DISDEFWBUF
        self.DISFOLD = RM_Field_CM4_NVICAUXCTRL_DISFOLD(self)
        self.zz_fdict['DISFOLD'] = self.DISFOLD
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICVECTSETIEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICVECTSETIEN, self).__init__(rmio, label,
            0xe0000000, 0xE100,
            'NVICVECTSETIEN', 'CM4.NVICVECTSETIEN', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.IEN = RM_Field_CM4_NVICVECTSETIEN_IEN(self)
        self.zz_fdict['IEN'] = self.IEN
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICVECTSETIEN1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICVECTSETIEN1, self).__init__(rmio, label,
            0xe0000000, 0xE104,
            'NVICVECTSETIEN1', 'CM4.NVICVECTSETIEN1', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.IEN = RM_Field_CM4_NVICVECTSETIEN1_IEN(self)
        self.zz_fdict['IEN'] = self.IEN
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICVECTSETIDIS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICVECTSETIDIS, self).__init__(rmio, label,
            0xe0000000, 0xE180,
            'NVICVECTSETIDIS', 'CM4.NVICVECTSETIDIS', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.IDIS = RM_Field_CM4_NVICVECTSETIDIS_IDIS(self)
        self.zz_fdict['IDIS'] = self.IDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICVECTSETIDIS1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICVECTSETIDIS1, self).__init__(rmio, label,
            0xe0000000, 0xE184,
            'NVICVECTSETIDIS1', 'CM4.NVICVECTSETIDIS1', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.IDIS = RM_Field_CM4_NVICVECTSETIDIS1_IDIS(self)
        self.zz_fdict['IDIS'] = self.IDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICVECTSETPEND(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICVECTSETPEND, self).__init__(rmio, label,
            0xe0000000, 0xE200,
            'NVICVECTSETPEND', 'CM4.NVICVECTSETPEND', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.SETPEND = RM_Field_CM4_NVICVECTSETPEND_SETPEND(self)
        self.zz_fdict['SETPEND'] = self.SETPEND
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICVECTSETPEND1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICVECTSETPEND1, self).__init__(rmio, label,
            0xe0000000, 0xE204,
            'NVICVECTSETPEND1', 'CM4.NVICVECTSETPEND1', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.SETPEND = RM_Field_CM4_NVICVECTSETPEND1_SETPEND(self)
        self.zz_fdict['SETPEND'] = self.SETPEND
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICVECTCLEARPEND(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICVECTCLEARPEND, self).__init__(rmio, label,
            0xe0000000, 0xE280,
            'NVICVECTCLEARPEND', 'CM4.NVICVECTCLEARPEND', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.CLEARPEND = RM_Field_CM4_NVICVECTCLEARPEND_CLEARPEND(self)
        self.zz_fdict['CLEARPEND'] = self.CLEARPEND
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICVECTCLEARPEND1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICVECTCLEARPEND1, self).__init__(rmio, label,
            0xe0000000, 0xE284,
            'NVICVECTCLEARPEND1', 'CM4.NVICVECTCLEARPEND1', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.CLEARPEND = RM_Field_CM4_NVICVECTCLEARPEND1_CLEARPEND(self)
        self.zz_fdict['CLEARPEND'] = self.CLEARPEND
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICPRI0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICPRI0, self).__init__(rmio, label,
            0xe0000000, 0xE400,
            'NVICPRI0', 'CM4.NVICPRI0', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.PRI0 = RM_Field_CM4_NVICPRI0_PRI0(self)
        self.zz_fdict['PRI0'] = self.PRI0
        self.PRI1 = RM_Field_CM4_NVICPRI0_PRI1(self)
        self.zz_fdict['PRI1'] = self.PRI1
        self.PRI2 = RM_Field_CM4_NVICPRI0_PRI2(self)
        self.zz_fdict['PRI2'] = self.PRI2
        self.PRI3 = RM_Field_CM4_NVICPRI0_PRI3(self)
        self.zz_fdict['PRI3'] = self.PRI3
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICISCR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICISCR, self).__init__(rmio, label,
            0xe0000000, 0xED04,
            'NVICISCR', 'CM4.NVICISCR', 'read-write',
            "",
            0x00000000, 0x001FF9FF)

        self.VECTACTIVE = RM_Field_CM4_NVICISCR_VECTACTIVE(self)
        self.zz_fdict['VECTACTIVE'] = self.VECTACTIVE
        self.RETTOBASE = RM_Field_CM4_NVICISCR_RETTOBASE(self)
        self.zz_fdict['RETTOBASE'] = self.RETTOBASE
        self.VECTPENDING = RM_Field_CM4_NVICISCR_VECTPENDING(self)
        self.zz_fdict['VECTPENDING'] = self.VECTPENDING
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICVECTTABOFF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICVECTTABOFF, self).__init__(rmio, label,
            0xe0000000, 0xED08,
            'NVICVECTTABOFF', 'CM4.NVICVECTTABOFF', 'read-write',
            "",
            0x00000000, 0x3FFFFF80)

        self.OFFSET = RM_Field_CM4_NVICVECTTABOFF_OFFSET(self)
        self.zz_fdict['OFFSET'] = self.OFFSET
        self.BASE = RM_Field_CM4_NVICVECTTABOFF_BASE(self)
        self.zz_fdict['BASE'] = self.BASE
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICSYSCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICSYSCTRL, self).__init__(rmio, label,
            0xe0000000, 0xED10,
            'NVICSYSCTRL', 'CM4.NVICSYSCTRL', 'read-write',
            "",
            0x00000000, 0x00000016)

        self.SLEEPONEXIT = RM_Field_CM4_NVICSYSCTRL_SLEEPONEXIT(self)
        self.zz_fdict['SLEEPONEXIT'] = self.SLEEPONEXIT
        self.GOSUBEM1 = RM_Field_CM4_NVICSYSCTRL_GOSUBEM1(self)
        self.zz_fdict['GOSUBEM1'] = self.GOSUBEM1
        self.SEVONPEND = RM_Field_CM4_NVICSYSCTRL_SEVONPEND(self)
        self.zz_fdict['SEVONPEND'] = self.SEVONPEND
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICSYSHANDLER(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICSYSHANDLER, self).__init__(rmio, label,
            0xe0000000, 0xED24,
            'NVICSYSHANDLER', 'CM4.NVICSYSHANDLER', 'read-write',
            "",
            0x00000000, 0x0007FD8B)

        self.MEMFAULTACT = RM_Field_CM4_NVICSYSHANDLER_MEMFAULTACT(self)
        self.zz_fdict['MEMFAULTACT'] = self.MEMFAULTACT
        self.BUSFAULTACT = RM_Field_CM4_NVICSYSHANDLER_BUSFAULTACT(self)
        self.zz_fdict['BUSFAULTACT'] = self.BUSFAULTACT
        self.USGFAULTACT = RM_Field_CM4_NVICSYSHANDLER_USGFAULTACT(self)
        self.zz_fdict['USGFAULTACT'] = self.USGFAULTACT
        self.SVCALLACT = RM_Field_CM4_NVICSYSHANDLER_SVCALLACT(self)
        self.zz_fdict['SVCALLACT'] = self.SVCALLACT
        self.MONITORACT = RM_Field_CM4_NVICSYSHANDLER_MONITORACT(self)
        self.zz_fdict['MONITORACT'] = self.MONITORACT
        self.PENDSVACT = RM_Field_CM4_NVICSYSHANDLER_PENDSVACT(self)
        self.zz_fdict['PENDSVACT'] = self.PENDSVACT
        self.SYSTICKACT = RM_Field_CM4_NVICSYSHANDLER_SYSTICKACT(self)
        self.zz_fdict['SYSTICKACT'] = self.SYSTICKACT
        self.USGFAULTPENDED = RM_Field_CM4_NVICSYSHANDLER_USGFAULTPENDED(self)
        self.zz_fdict['USGFAULTPENDED'] = self.USGFAULTPENDED
        self.MEMFAULTPENDED = RM_Field_CM4_NVICSYSHANDLER_MEMFAULTPENDED(self)
        self.zz_fdict['MEMFAULTPENDED'] = self.MEMFAULTPENDED
        self.BUSFAULTPENDED = RM_Field_CM4_NVICSYSHANDLER_BUSFAULTPENDED(self)
        self.zz_fdict['BUSFAULTPENDED'] = self.BUSFAULTPENDED
        self.SVCALLPENDED = RM_Field_CM4_NVICSYSHANDLER_SVCALLPENDED(self)
        self.zz_fdict['SVCALLPENDED'] = self.SVCALLPENDED
        self.MEMFAULTENA = RM_Field_CM4_NVICSYSHANDLER_MEMFAULTENA(self)
        self.zz_fdict['MEMFAULTENA'] = self.MEMFAULTENA
        self.BUSFAULTENA = RM_Field_CM4_NVICSYSHANDLER_BUSFAULTENA(self)
        self.zz_fdict['BUSFAULTENA'] = self.BUSFAULTENA
        self.USGFAULTENA = RM_Field_CM4_NVICSYSHANDLER_USGFAULTENA(self)
        self.zz_fdict['USGFAULTENA'] = self.USGFAULTENA
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICCFSR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICCFSR, self).__init__(rmio, label,
            0xe0000000, 0xED28,
            'NVICCFSR', 'CM4.NVICCFSR', 'read-write',
            "",
            0x00000000, 0x030F9F00)

        self.IBUSERR = RM_Field_CM4_NVICCFSR_IBUSERR(self)
        self.zz_fdict['IBUSERR'] = self.IBUSERR
        self.PRECISERR = RM_Field_CM4_NVICCFSR_PRECISERR(self)
        self.zz_fdict['PRECISERR'] = self.PRECISERR
        self.IMPRECISERR = RM_Field_CM4_NVICCFSR_IMPRECISERR(self)
        self.zz_fdict['IMPRECISERR'] = self.IMPRECISERR
        self.UNSTKERR = RM_Field_CM4_NVICCFSR_UNSTKERR(self)
        self.zz_fdict['UNSTKERR'] = self.UNSTKERR
        self.STKERR = RM_Field_CM4_NVICCFSR_STKERR(self)
        self.zz_fdict['STKERR'] = self.STKERR
        self.BFARVALID = RM_Field_CM4_NVICCFSR_BFARVALID(self)
        self.zz_fdict['BFARVALID'] = self.BFARVALID
        self.UNDEFINSTR = RM_Field_CM4_NVICCFSR_UNDEFINSTR(self)
        self.zz_fdict['UNDEFINSTR'] = self.UNDEFINSTR
        self.INVSTATE = RM_Field_CM4_NVICCFSR_INVSTATE(self)
        self.zz_fdict['INVSTATE'] = self.INVSTATE
        self.INVPC = RM_Field_CM4_NVICCFSR_INVPC(self)
        self.zz_fdict['INVPC'] = self.INVPC
        self.NOCP = RM_Field_CM4_NVICCFSR_NOCP(self)
        self.zz_fdict['NOCP'] = self.NOCP
        self.UNALIGNED = RM_Field_CM4_NVICCFSR_UNALIGNED(self)
        self.zz_fdict['UNALIGNED'] = self.UNALIGNED
        self.DIVBYZERO = RM_Field_CM4_NVICCFSR_DIVBYZERO(self)
        self.zz_fdict['DIVBYZERO'] = self.DIVBYZERO
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICHFSR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICHFSR, self).__init__(rmio, label,
            0xe0000000, 0xED2C,
            'NVICHFSR', 'CM4.NVICHFSR', 'read-write',
            "",
            0x00000000, 0xC0000002)

        self.VECTTBL = RM_Field_CM4_NVICHFSR_VECTTBL(self)
        self.zz_fdict['VECTTBL'] = self.VECTTBL
        self.FORCED = RM_Field_CM4_NVICHFSR_FORCED(self)
        self.zz_fdict['FORCED'] = self.FORCED
        self.DEBUGEVT = RM_Field_CM4_NVICHFSR_DEBUGEVT(self)
        self.zz_fdict['DEBUGEVT'] = self.DEBUGEVT
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_NVICAIRC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_NVICAIRC, self).__init__(rmio, label,
            0xe0000000, 0x1CD0C,
            'NVICAIRC', 'CM4.NVICAIRC', 'read-write',
            "",
            0x00000000, 0xFFFF0705)

        self.VECTRESET = RM_Field_CM4_NVICAIRC_VECTRESET(self)
        self.zz_fdict['VECTRESET'] = self.VECTRESET
        self.SYSRESETREQ = RM_Field_CM4_NVICAIRC_SYSRESETREQ(self)
        self.zz_fdict['SYSRESETREQ'] = self.SYSRESETREQ
        self.PRIGROUP = RM_Field_CM4_NVICAIRC_PRIGROUP(self)
        self.zz_fdict['PRIGROUP'] = self.PRIGROUP
        self.VECTKEY = RM_Field_CM4_NVICAIRC_VECTKEY(self)
        self.zz_fdict['VECTKEY'] = self.VECTKEY
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_CHIPREVMAJORLSB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_CHIPREVMAJORLSB, self).__init__(rmio, label,
            0xe0000000, 0xFFFE0,
            'CHIPREVMAJORLSB', 'CM4.CHIPREVMAJORLSB', 'read-only',
            "",
            0x00000001, 0x000000FF)

        self.MAJORREVLSB = RM_Field_CM4_CHIPREVMAJORLSB_MAJORREVLSB(self)
        self.zz_fdict['MAJORREVLSB'] = self.MAJORREVLSB
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_CHIPREVMAJORMSB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_CHIPREVMAJORMSB, self).__init__(rmio, label,
            0xe0000000, 0xFFFE4,
            'CHIPREVMAJORMSB', 'CM4.CHIPREVMAJORMSB', 'read-only',
            "",
            0x00000030, 0x000000FF)

        self.MAJORREVMSB = RM_Field_CM4_CHIPREVMAJORMSB_MAJORREVMSB(self)
        self.zz_fdict['MAJORREVMSB'] = self.MAJORREVMSB
        self.JEP106LSB = RM_Field_CM4_CHIPREVMAJORMSB_JEP106LSB(self)
        self.zz_fdict['JEP106LSB'] = self.JEP106LSB
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_CHIPREVMINORMSB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_CHIPREVMINORMSB, self).__init__(rmio, label,
            0xe0000000, 0xFFFE8,
            'CHIPREVMINORMSB', 'CM4.CHIPREVMINORMSB', 'read-only',
            "",
            0x0000000F, 0x000000FF)

        self.JEP106MSB = RM_Field_CM4_CHIPREVMINORMSB_JEP106MSB(self)
        self.zz_fdict['JEP106MSB'] = self.JEP106MSB
        self.JEP106USED = RM_Field_CM4_CHIPREVMINORMSB_JEP106USED(self)
        self.zz_fdict['JEP106USED'] = self.JEP106USED
        self.MINORREVMSB = RM_Field_CM4_CHIPREVMINORMSB_MINORREVMSB(self)
        self.zz_fdict['MINORREVMSB'] = self.MINORREVMSB
        self.__dict__['zz_frozen'] = True


class RM_Register_CM4_CHIPREVMINORLSB(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_CM4_CHIPREVMINORLSB, self).__init__(rmio, label,
            0xe0000000, 0xFFFEC,
            'CHIPREVMINORLSB', 'CM4.CHIPREVMINORLSB', 'read-only',
            "",
            0x00000000, 0x000000F0)

        self.MINORREVLSB = RM_Field_CM4_CHIPREVMINORLSB_MINORREVLSB(self)
        self.zz_fdict['MINORREVLSB'] = self.MINORREVLSB
        self.__dict__['zz_frozen'] = True


