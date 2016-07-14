
from static import Base_RM_Field
from CM3_enum import *


class RM_Field_CM3_NVICAUXCTRL_DISMCYCINT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICAUXCTRL_DISMCYCINT, self).__init__(register,
            'DISMCYCINT', 'CM3.NVICAUXCTRL.DISMCYCINT', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICAUXCTRL_DISDEFWBUF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICAUXCTRL_DISDEFWBUF, self).__init__(register,
            'DISDEFWBUF', 'CM3.NVICAUXCTRL.DISDEFWBUF', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICAUXCTRL_DISFOLD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICAUXCTRL_DISFOLD, self).__init__(register,
            'DISFOLD', 'CM3.NVICAUXCTRL.DISFOLD', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICVECTSETIEN_IEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICVECTSETIEN_IEN, self).__init__(register,
            'IEN', 'CM3.NVICVECTSETIEN.IEN', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICVECTSETIEN1_IEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICVECTSETIEN1_IEN, self).__init__(register,
            'IEN', 'CM3.NVICVECTSETIEN1.IEN', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICVECTSETIDIS_IDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICVECTSETIDIS_IDIS, self).__init__(register,
            'IDIS', 'CM3.NVICVECTSETIDIS.IDIS', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICVECTSETIDIS1_IDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICVECTSETIDIS1_IDIS, self).__init__(register,
            'IDIS', 'CM3.NVICVECTSETIDIS1.IDIS', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICVECTSETPEND_SETPEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICVECTSETPEND_SETPEND, self).__init__(register,
            'SETPEND', 'CM3.NVICVECTSETPEND.SETPEND', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICVECTSETPEND1_SETPEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICVECTSETPEND1_SETPEND, self).__init__(register,
            'SETPEND', 'CM3.NVICVECTSETPEND1.SETPEND', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICVECTCLEARPEND_CLEARPEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICVECTCLEARPEND_CLEARPEND, self).__init__(register,
            'CLEARPEND', 'CM3.NVICVECTCLEARPEND.CLEARPEND', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICVECTCLEARPEND1_CLEARPEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICVECTCLEARPEND1_CLEARPEND, self).__init__(register,
            'CLEARPEND', 'CM3.NVICVECTCLEARPEND1.CLEARPEND', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICPRI0_PRI0(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICPRI0_PRI0, self).__init__(register,
            'PRI0', 'CM3.NVICPRI0.PRI0', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICPRI0_PRI1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICPRI0_PRI1, self).__init__(register,
            'PRI1', 'CM3.NVICPRI0.PRI1', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICPRI0_PRI2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICPRI0_PRI2, self).__init__(register,
            'PRI2', 'CM3.NVICPRI0.PRI2', 'read-write',
            "",
            16, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICPRI0_PRI3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICPRI0_PRI3, self).__init__(register,
            'PRI3', 'CM3.NVICPRI0.PRI3', 'read-write',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICISCR_VECTACTIVE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICISCR_VECTACTIVE, self).__init__(register,
            'VECTACTIVE', 'CM3.NVICISCR.VECTACTIVE', 'read-write',
            "",
            0, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICISCR_RETTOBASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICISCR_RETTOBASE, self).__init__(register,
            'RETTOBASE', 'CM3.NVICISCR.RETTOBASE', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICISCR_VECTPENDING(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICISCR_VECTPENDING, self).__init__(register,
            'VECTPENDING', 'CM3.NVICISCR.VECTPENDING', 'read-write',
            "",
            12, 9)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICVECTTABOFF_OFFSET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICVECTTABOFF_OFFSET, self).__init__(register,
            'OFFSET', 'CM3.NVICVECTTABOFF.OFFSET', 'read-write',
            "",
            7, 22)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICVECTTABOFF_BASE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICVECTTABOFF_BASE, self).__init__(register,
            'BASE', 'CM3.NVICVECTTABOFF.BASE', 'read-write',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSCTRL_SLEEPONEXIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSCTRL_SLEEPONEXIT, self).__init__(register,
            'SLEEPONEXIT', 'CM3.NVICSYSCTRL.SLEEPONEXIT', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSCTRL_GOSUBEM1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSCTRL_GOSUBEM1, self).__init__(register,
            'GOSUBEM1', 'CM3.NVICSYSCTRL.GOSUBEM1', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSCTRL_SEVONPEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSCTRL_SEVONPEND, self).__init__(register,
            'SEVONPEND', 'CM3.NVICSYSCTRL.SEVONPEND', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSHANDLER_MEMFAULTACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSHANDLER_MEMFAULTACT, self).__init__(register,
            'MEMFAULTACT', 'CM3.NVICSYSHANDLER.MEMFAULTACT', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSHANDLER_BUSFAULTACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSHANDLER_BUSFAULTACT, self).__init__(register,
            'BUSFAULTACT', 'CM3.NVICSYSHANDLER.BUSFAULTACT', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSHANDLER_USGFAULTACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSHANDLER_USGFAULTACT, self).__init__(register,
            'USGFAULTACT', 'CM3.NVICSYSHANDLER.USGFAULTACT', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSHANDLER_SVCALLACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSHANDLER_SVCALLACT, self).__init__(register,
            'SVCALLACT', 'CM3.NVICSYSHANDLER.SVCALLACT', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSHANDLER_MONITORACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSHANDLER_MONITORACT, self).__init__(register,
            'MONITORACT', 'CM3.NVICSYSHANDLER.MONITORACT', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSHANDLER_PENDSVACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSHANDLER_PENDSVACT, self).__init__(register,
            'PENDSVACT', 'CM3.NVICSYSHANDLER.PENDSVACT', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSHANDLER_SYSTICKACT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSHANDLER_SYSTICKACT, self).__init__(register,
            'SYSTICKACT', 'CM3.NVICSYSHANDLER.SYSTICKACT', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSHANDLER_USGFAULTPENDED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSHANDLER_USGFAULTPENDED, self).__init__(register,
            'USGFAULTPENDED', 'CM3.NVICSYSHANDLER.USGFAULTPENDED', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSHANDLER_MEMFAULTPENDED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSHANDLER_MEMFAULTPENDED, self).__init__(register,
            'MEMFAULTPENDED', 'CM3.NVICSYSHANDLER.MEMFAULTPENDED', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSHANDLER_BUSFAULTPENDED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSHANDLER_BUSFAULTPENDED, self).__init__(register,
            'BUSFAULTPENDED', 'CM3.NVICSYSHANDLER.BUSFAULTPENDED', 'read-write',
            "",
            14, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSHANDLER_SVCALLPENDED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSHANDLER_SVCALLPENDED, self).__init__(register,
            'SVCALLPENDED', 'CM3.NVICSYSHANDLER.SVCALLPENDED', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSHANDLER_MEMFAULTENA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSHANDLER_MEMFAULTENA, self).__init__(register,
            'MEMFAULTENA', 'CM3.NVICSYSHANDLER.MEMFAULTENA', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSHANDLER_BUSFAULTENA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSHANDLER_BUSFAULTENA, self).__init__(register,
            'BUSFAULTENA', 'CM3.NVICSYSHANDLER.BUSFAULTENA', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICSYSHANDLER_USGFAULTENA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICSYSHANDLER_USGFAULTENA, self).__init__(register,
            'USGFAULTENA', 'CM3.NVICSYSHANDLER.USGFAULTENA', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICCFSR_IBUSERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICCFSR_IBUSERR, self).__init__(register,
            'IBUSERR', 'CM3.NVICCFSR.IBUSERR', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICCFSR_PRECISERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICCFSR_PRECISERR, self).__init__(register,
            'PRECISERR', 'CM3.NVICCFSR.PRECISERR', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICCFSR_IMPRECISERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICCFSR_IMPRECISERR, self).__init__(register,
            'IMPRECISERR', 'CM3.NVICCFSR.IMPRECISERR', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICCFSR_UNSTKERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICCFSR_UNSTKERR, self).__init__(register,
            'UNSTKERR', 'CM3.NVICCFSR.UNSTKERR', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICCFSR_STKERR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICCFSR_STKERR, self).__init__(register,
            'STKERR', 'CM3.NVICCFSR.STKERR', 'read-write',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICCFSR_BFARVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICCFSR_BFARVALID, self).__init__(register,
            'BFARVALID', 'CM3.NVICCFSR.BFARVALID', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICCFSR_UNDEFINSTR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICCFSR_UNDEFINSTR, self).__init__(register,
            'UNDEFINSTR', 'CM3.NVICCFSR.UNDEFINSTR', 'read-write',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICCFSR_INVSTATE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICCFSR_INVSTATE, self).__init__(register,
            'INVSTATE', 'CM3.NVICCFSR.INVSTATE', 'read-write',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICCFSR_INVPC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICCFSR_INVPC, self).__init__(register,
            'INVPC', 'CM3.NVICCFSR.INVPC', 'read-write',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICCFSR_NOCP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICCFSR_NOCP, self).__init__(register,
            'NOCP', 'CM3.NVICCFSR.NOCP', 'read-write',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICCFSR_UNALIGNED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICCFSR_UNALIGNED, self).__init__(register,
            'UNALIGNED', 'CM3.NVICCFSR.UNALIGNED', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICCFSR_DIVBYZERO(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICCFSR_DIVBYZERO, self).__init__(register,
            'DIVBYZERO', 'CM3.NVICCFSR.DIVBYZERO', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICHFSR_VECTTBL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICHFSR_VECTTBL, self).__init__(register,
            'VECTTBL', 'CM3.NVICHFSR.VECTTBL', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICHFSR_FORCED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICHFSR_FORCED, self).__init__(register,
            'FORCED', 'CM3.NVICHFSR.FORCED', 'read-write',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICHFSR_DEBUGEVT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICHFSR_DEBUGEVT, self).__init__(register,
            'DEBUGEVT', 'CM3.NVICHFSR.DEBUGEVT', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICAIRC_VECTRESET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICAIRC_VECTRESET, self).__init__(register,
            'VECTRESET', 'CM3.NVICAIRC.VECTRESET', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICAIRC_SYSRESETREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICAIRC_SYSRESETREQ, self).__init__(register,
            'SYSRESETREQ', 'CM3.NVICAIRC.SYSRESETREQ', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICAIRC_PRIGROUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICAIRC_PRIGROUP, self).__init__(register,
            'PRIGROUP', 'CM3.NVICAIRC.PRIGROUP', 'read-write',
            "",
            8, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_NVICAIRC_VECTKEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_NVICAIRC_VECTKEY, self).__init__(register,
            'VECTKEY', 'CM3.NVICAIRC.VECTKEY', 'read-write',
            "",
            16, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_CHIPREVMAJORLSB_MAJORREVLSB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_CHIPREVMAJORLSB_MAJORREVLSB, self).__init__(register,
            'MAJORREVLSB', 'CM3.CHIPREVMAJORLSB.MAJORREVLSB', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_CHIPREVMAJORMSB_MAJORREVMSB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_CHIPREVMAJORMSB_MAJORREVMSB, self).__init__(register,
            'MAJORREVMSB', 'CM3.CHIPREVMAJORMSB.MAJORREVMSB', 'read-only',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_CHIPREVMAJORMSB_JEP106LSB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_CHIPREVMAJORMSB_JEP106LSB, self).__init__(register,
            'JEP106LSB', 'CM3.CHIPREVMAJORMSB.JEP106LSB', 'read-only',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_CHIPREVMINORMSB_JEP106MSB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_CHIPREVMINORMSB_JEP106MSB, self).__init__(register,
            'JEP106MSB', 'CM3.CHIPREVMINORMSB.JEP106MSB', 'read-only',
            "",
            0, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_CHIPREVMINORMSB_JEP106USED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_CHIPREVMINORMSB_JEP106USED, self).__init__(register,
            'JEP106USED', 'CM3.CHIPREVMINORMSB.JEP106USED', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_CHIPREVMINORMSB_MINORREVMSB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_CHIPREVMINORMSB_MINORREVMSB, self).__init__(register,
            'MINORREVMSB', 'CM3.CHIPREVMINORMSB.MINORREVMSB', 'read-only',
            "",
            4, 4,
            RM_Enum_CM3_CHIPREVMINORMSB_MINORREVMSB(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_CM3_CHIPREVMINORLSB_MINORREVLSB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_CM3_CHIPREVMINORLSB_MINORREVLSB, self).__init__(register,
            'MINORREVLSB', 'CM3.CHIPREVMINORLSB.MINORREVLSB', 'read-only',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


