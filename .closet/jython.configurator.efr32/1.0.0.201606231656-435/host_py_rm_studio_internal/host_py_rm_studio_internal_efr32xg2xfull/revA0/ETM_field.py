
from static import Base_RM_Field
from ETM_enum import *


class RM_Field_ETM_ETMCR_POWERDWN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCR_POWERDWN, self).__init__(register,
            'POWERDWN', 'ETM.ETMCR.POWERDWN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCR_PORTSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCR_PORTSIZE, self).__init__(register,
            'PORTSIZE', 'ETM.ETMCR.PORTSIZE', 'read-write',
            "",
            4, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCR_STALL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCR_STALL, self).__init__(register,
            'STALL', 'ETM.ETMCR.STALL', 'read-write',
            "",
            7, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCR_BRANCHOUTPUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCR_BRANCHOUTPUT, self).__init__(register,
            'BRANCHOUTPUT', 'ETM.ETMCR.BRANCHOUTPUT', 'read-write',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCR_DBGREQCTRL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCR_DBGREQCTRL, self).__init__(register,
            'DBGREQCTRL', 'ETM.ETMCR.DBGREQCTRL', 'read-write',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCR_ETMPROG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCR_ETMPROG, self).__init__(register,
            'ETMPROG', 'ETM.ETMCR.ETMPROG', 'read-write',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCR_ETMPORTSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCR_ETMPORTSEL, self).__init__(register,
            'ETMPORTSEL', 'ETM.ETMCR.ETMPORTSEL', 'read-write',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCR_PORTMODE2(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCR_PORTMODE2, self).__init__(register,
            'PORTMODE2', 'ETM.ETMCR.PORTMODE2', 'read-write',
            "",
            13, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCR_PORTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCR_PORTMODE, self).__init__(register,
            'PORTMODE', 'ETM.ETMCR.PORTMODE', 'read-write',
            "",
            16, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCR_EPORTSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCR_EPORTSIZE, self).__init__(register,
            'EPORTSIZE', 'ETM.ETMCR.EPORTSIZE', 'read-write',
            "",
            21, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCR_TSTAMPEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCR_TSTAMPEN, self).__init__(register,
            'TSTAMPEN', 'ETM.ETMCR.TSTAMPEN', 'read-write',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCR_ADRCMPPAIR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCR_ADRCMPPAIR, self).__init__(register,
            'ADRCMPPAIR', 'ETM.ETMCCR.ADRCMPPAIR', 'read-only',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCR_DATACMPNUM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCR_DATACMPNUM, self).__init__(register,
            'DATACMPNUM', 'ETM.ETMCCR.DATACMPNUM', 'read-only',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCR_MMDECCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCR_MMDECCNT, self).__init__(register,
            'MMDECCNT', 'ETM.ETMCCR.MMDECCNT', 'read-only',
            "",
            8, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCR_COUNTNUM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCR_COUNTNUM, self).__init__(register,
            'COUNTNUM', 'ETM.ETMCCR.COUNTNUM', 'read-only',
            "",
            13, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCR_SEQPRES(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCR_SEQPRES, self).__init__(register,
            'SEQPRES', 'ETM.ETMCCR.SEQPRES', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCR_EXTINPNUM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCR_EXTINPNUM, self).__init__(register,
            'EXTINPNUM', 'ETM.ETMCCR.EXTINPNUM', 'read-only',
            "",
            17, 3,
            RM_Enum_ETM_ETMCCR_EXTINPNUM(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCR_EXTOUTNUM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCR_EXTOUTNUM, self).__init__(register,
            'EXTOUTNUM', 'ETM.ETMCCR.EXTOUTNUM', 'read-only',
            "",
            20, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCR_FIFOFULLPRES(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCR_FIFOFULLPRES, self).__init__(register,
            'FIFOFULLPRES', 'ETM.ETMCCR.FIFOFULLPRES', 'read-only',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCR_IDCOMPNUM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCR_IDCOMPNUM, self).__init__(register,
            'IDCOMPNUM', 'ETM.ETMCCR.IDCOMPNUM', 'read-only',
            "",
            24, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCR_TRACESS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCR_TRACESS, self).__init__(register,
            'TRACESS', 'ETM.ETMCCR.TRACESS', 'read-only',
            "",
            26, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCR_MMACCESS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCR_MMACCESS, self).__init__(register,
            'MMACCESS', 'ETM.ETMCCR.MMACCESS', 'read-only',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCR_ETMID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCR_ETMID, self).__init__(register,
            'ETMID', 'ETM.ETMCCR.ETMID', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTRIGGER_RESA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTRIGGER_RESA, self).__init__(register,
            'RESA', 'ETM.ETMTRIGGER.RESA', 'read-write',
            "",
            0, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTRIGGER_RESB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTRIGGER_RESB, self).__init__(register,
            'RESB', 'ETM.ETMTRIGGER.RESB', 'read-write',
            "",
            7, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTRIGGER_ETMFCN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTRIGGER_ETMFCN, self).__init__(register,
            'ETMFCN', 'ETM.ETMTRIGGER.ETMFCN', 'read-write',
            "",
            14, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMSR_ETHOF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMSR_ETHOF, self).__init__(register,
            'ETHOF', 'ETM.ETMSR.ETHOF', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMSR_ETMPROGBIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMSR_ETMPROGBIT, self).__init__(register,
            'ETMPROGBIT', 'ETM.ETMSR.ETMPROGBIT', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMSR_TRACESTAT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMSR_TRACESTAT, self).__init__(register,
            'TRACESTAT', 'ETM.ETMSR.TRACESTAT', 'read-write',
            "",
            2, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMSR_TRIGBIT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMSR_TRIGBIT, self).__init__(register,
            'TRIGBIT', 'ETM.ETMSR.TRIGBIT', 'read-write',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMSCR_MAXPORTSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMSCR_MAXPORTSIZE, self).__init__(register,
            'MAXPORTSIZE', 'ETM.ETMSCR.MAXPORTSIZE', 'read-only',
            "",
            0, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMSCR_Reserved(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMSCR_Reserved, self).__init__(register,
            'Reserved', 'ETM.ETMSCR.Reserved', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMSCR_FIFOFULL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMSCR_FIFOFULL, self).__init__(register,
            'FIFOFULL', 'ETM.ETMSCR.FIFOFULL', 'read-only',
            "",
            8, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMSCR_MAXPORTSIZE3(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMSCR_MAXPORTSIZE3, self).__init__(register,
            'MAXPORTSIZE3', 'ETM.ETMSCR.MAXPORTSIZE3', 'read-only',
            "",
            9, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMSCR_PORTSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMSCR_PORTSIZE, self).__init__(register,
            'PORTSIZE', 'ETM.ETMSCR.PORTSIZE', 'read-only',
            "",
            10, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMSCR_PORTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMSCR_PORTMODE, self).__init__(register,
            'PORTMODE', 'ETM.ETMSCR.PORTMODE', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMSCR_PROCNUM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMSCR_PROCNUM, self).__init__(register,
            'PROCNUM', 'ETM.ETMSCR.PROCNUM', 'read-only',
            "",
            12, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMSCR_NOFETCHCOMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMSCR_NOFETCHCOMP, self).__init__(register,
            'NOFETCHCOMP', 'ETM.ETMSCR.NOFETCHCOMP', 'read-only',
            "",
            17, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTEEVR_RESA(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTEEVR_RESA, self).__init__(register,
            'RESA', 'ETM.ETMTEEVR.RESA', 'read-write',
            "",
            0, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTEEVR_RESB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTEEVR_RESB, self).__init__(register,
            'RESB', 'ETM.ETMTEEVR.RESB', 'read-write',
            "",
            7, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTEEVR_ETMFCNEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTEEVR_ETMFCNEN, self).__init__(register,
            'ETMFCNEN', 'ETM.ETMTEEVR.ETMFCNEN', 'read-write',
            "",
            14, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTECR1_ADRCMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTECR1_ADRCMP, self).__init__(register,
            'ADRCMP', 'ETM.ETMTECR1.ADRCMP', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTECR1_MEMMAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTECR1_MEMMAP, self).__init__(register,
            'MEMMAP', 'ETM.ETMTECR1.MEMMAP', 'read-write',
            "",
            8, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTECR1_INCEXCTL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTECR1_INCEXCTL, self).__init__(register,
            'INCEXCTL', 'ETM.ETMTECR1.INCEXCTL', 'read-write',
            "",
            24, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTECR1_TCE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTECR1_TCE, self).__init__(register,
            'TCE', 'ETM.ETMTECR1.TCE', 'read-write',
            "",
            25, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMFFLR_BYTENUM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMFFLR_BYTENUM, self).__init__(register,
            'BYTENUM', 'ETM.ETMFFLR.BYTENUM', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCNTRLDVR1_COUNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCNTRLDVR1_COUNT, self).__init__(register,
            'COUNT', 'ETM.ETMCNTRLDVR1.COUNT', 'read-write',
            "",
            0, 16)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMSYNCFR_FREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMSYNCFR_FREQ, self).__init__(register,
            'FREQ', 'ETM.ETMSYNCFR.FREQ', 'read-write',
            "",
            0, 12)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMIDR_IMPVER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMIDR_IMPVER, self).__init__(register,
            'IMPVER', 'ETM.ETMIDR.IMPVER', 'read-only',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMIDR_ETMMINVER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMIDR_ETMMINVER, self).__init__(register,
            'ETMMINVER', 'ETM.ETMIDR.ETMMINVER', 'read-only',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMIDR_ETMMAJVER(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMIDR_ETMMAJVER, self).__init__(register,
            'ETMMAJVER', 'ETM.ETMIDR.ETMMAJVER', 'read-only',
            "",
            8, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMIDR_PROCFAM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMIDR_PROCFAM, self).__init__(register,
            'PROCFAM', 'ETM.ETMIDR.PROCFAM', 'read-only',
            "",
            12, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMIDR_LPCF(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMIDR_LPCF, self).__init__(register,
            'LPCF', 'ETM.ETMIDR.LPCF', 'read-only',
            "",
            16, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMIDR_THUMBT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMIDR_THUMBT, self).__init__(register,
            'THUMBT', 'ETM.ETMIDR.THUMBT', 'read-only',
            "",
            18, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMIDR_SECEXT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMIDR_SECEXT, self).__init__(register,
            'SECEXT', 'ETM.ETMIDR.SECEXT', 'read-only',
            "",
            19, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMIDR_BPE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMIDR_BPE, self).__init__(register,
            'BPE', 'ETM.ETMIDR.BPE', 'read-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMIDR_IMPCODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMIDR_IMPCODE, self).__init__(register,
            'IMPCODE', 'ETM.ETMIDR.IMPCODE', 'read-only',
            "",
            24, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCER_EXTINPSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCER_EXTINPSEL, self).__init__(register,
            'EXTINPSEL', 'ETM.ETMCCER.EXTINPSEL', 'read-only',
            "",
            0, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCER_EXTINPBUS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCER_EXTINPBUS, self).__init__(register,
            'EXTINPBUS', 'ETM.ETMCCER.EXTINPBUS', 'read-only',
            "",
            3, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCER_READREGS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCER_READREGS, self).__init__(register,
            'READREGS', 'ETM.ETMCCER.READREGS', 'read-only',
            "",
            11, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCER_DADDRCMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCER_DADDRCMP, self).__init__(register,
            'DADDRCMP', 'ETM.ETMCCER.DADDRCMP', 'read-only',
            "",
            12, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCER_INSTRES(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCER_INSTRES, self).__init__(register,
            'INSTRES', 'ETM.ETMCCER.INSTRES', 'read-only',
            "",
            13, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCER_EICEWPNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCER_EICEWPNT, self).__init__(register,
            'EICEWPNT', 'ETM.ETMCCER.EICEWPNT', 'read-only',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCER_TEICEWPNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCER_TEICEWPNT, self).__init__(register,
            'TEICEWPNT', 'ETM.ETMCCER.TEICEWPNT', 'read-only',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCER_EICEIMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCER_EICEIMP, self).__init__(register,
            'EICEIMP', 'ETM.ETMCCER.EICEIMP', 'read-only',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCER_TIMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCER_TIMP, self).__init__(register,
            'TIMP', 'ETM.ETMCCER.TIMP', 'read-only',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCER_RFCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCER_RFCNT, self).__init__(register,
            'RFCNT', 'ETM.ETMCCER.RFCNT', 'read-only',
            "",
            27, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCER_TENC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCER_TENC, self).__init__(register,
            'TENC', 'ETM.ETMCCER.TENC', 'read-only',
            "",
            28, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCCER_TSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCCER_TSIZE, self).__init__(register,
            'TSIZE', 'ETM.ETMCCER.TSIZE', 'read-only',
            "",
            29, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTESSEICR_STARTRSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTESSEICR_STARTRSEL, self).__init__(register,
            'STARTRSEL', 'ETM.ETMTESSEICR.STARTRSEL', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTESSEICR_STOPRSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTESSEICR_STOPRSEL, self).__init__(register,
            'STOPRSEL', 'ETM.ETMTESSEICR.STOPRSEL', 'read-write',
            "",
            16, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTSEVR_RESAEVT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTSEVR_RESAEVT, self).__init__(register,
            'RESAEVT', 'ETM.ETMTSEVR.RESAEVT', 'read-write',
            "",
            0, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTSEVR_RESBEVT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTSEVR_RESBEVT, self).__init__(register,
            'RESBEVT', 'ETM.ETMTSEVR.RESBEVT', 'read-write',
            "",
            7, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTSEVR_ETMFCNEVT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTSEVR_ETMFCNEVT, self).__init__(register,
            'ETMFCNEVT', 'ETM.ETMTSEVR.ETMFCNEVT', 'read-write',
            "",
            14, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMTRACEIDR_TRACEID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMTRACEIDR_TRACEID, self).__init__(register,
            'TRACEID', 'ETM.ETMTRACEIDR.TRACEID', 'read-write',
            "",
            0, 7)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMIDR2_RFE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMIDR2_RFE, self).__init__(register,
            'RFE', 'ETM.ETMIDR2.RFE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMIDR2_SWP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMIDR2_SWP, self).__init__(register,
            'SWP', 'ETM.ETMIDR2.SWP', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMPDSR_ETMUP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMPDSR_ETMUP, self).__init__(register,
            'ETMUP', 'ETM.ETMPDSR.ETMUP', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMISCIN_EXTIN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMISCIN_EXTIN, self).__init__(register,
            'EXTIN', 'ETM.ETMISCIN.EXTIN', 'read-write',
            "",
            0, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMISCIN_COREHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMISCIN_COREHALT, self).__init__(register,
            'COREHALT', 'ETM.ETMISCIN.COREHALT', 'read-write',
            "",
            4, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ITTRIGOUT_TRIGGEROUT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ITTRIGOUT_TRIGGEROUT, self).__init__(register,
            'TRIGGEROUT', 'ETM.ITTRIGOUT.TRIGGEROUT', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMITATBCTR2_ATREADY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMITATBCTR2_ATREADY, self).__init__(register,
            'ATREADY', 'ETM.ETMITATBCTR2.ATREADY', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMITATBCTR0_ATVALID(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMITATBCTR0_ATVALID, self).__init__(register,
            'ATVALID', 'ETM.ETMITATBCTR0.ATVALID', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMITCTRL_ITEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMITCTRL_ITEN, self).__init__(register,
            'ITEN', 'ETM.ETMITCTRL.ITEN', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCLAIMSET_SETTAG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCLAIMSET_SETTAG, self).__init__(register,
            'SETTAG', 'ETM.ETMCLAIMSET.SETTAG', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCLAIMCLR_CLRTAG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCLAIMCLR_CLRTAG, self).__init__(register,
            'CLRTAG', 'ETM.ETMCLAIMCLR.CLRTAG', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMLAR_KEY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMLAR_KEY, self).__init__(register,
            'KEY', 'ETM.ETMLAR.KEY', 'read-write',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMLSR_LOCKIMP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMLSR_LOCKIMP, self).__init__(register,
            'LOCKIMP', 'ETM.ETMLSR.LOCKIMP', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMLSR_LOCKED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMLSR_LOCKED, self).__init__(register,
            'LOCKED', 'ETM.ETMLSR.LOCKED', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMAUTHSTATUS_NONSECINVDBG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMAUTHSTATUS_NONSECINVDBG, self).__init__(register,
            'NONSECINVDBG', 'ETM.ETMAUTHSTATUS.NONSECINVDBG', 'read-only',
            "",
            0, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMAUTHSTATUS_NONSECNONINVDBG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMAUTHSTATUS_NONSECNONINVDBG, self).__init__(register,
            'NONSECNONINVDBG', 'ETM.ETMAUTHSTATUS.NONSECNONINVDBG', 'read-only',
            "",
            2, 2,
            RM_Enum_ETM_ETMAUTHSTATUS_NONSECNONINVDBG(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMAUTHSTATUS_SECINVDBG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMAUTHSTATUS_SECINVDBG, self).__init__(register,
            'SECINVDBG', 'ETM.ETMAUTHSTATUS.SECINVDBG', 'read-only',
            "",
            4, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMAUTHSTATUS_SECNONINVDBG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMAUTHSTATUS_SECNONINVDBG, self).__init__(register,
            'SECNONINVDBG', 'ETM.ETMAUTHSTATUS.SECNONINVDBG', 'read-only',
            "",
            6, 2)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMDEVTYPE_TRACESRC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMDEVTYPE_TRACESRC, self).__init__(register,
            'TRACESRC', 'ETM.ETMDEVTYPE.TRACESRC', 'read-only',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMDEVTYPE_PROCTRACE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMDEVTYPE_PROCTRACE, self).__init__(register,
            'PROCTRACE', 'ETM.ETMDEVTYPE.PROCTRACE', 'read-only',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMPIDR4_CONTCODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMPIDR4_CONTCODE, self).__init__(register,
            'CONTCODE', 'ETM.ETMPIDR4.CONTCODE', 'read-only',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMPIDR4_COUNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMPIDR4_COUNT, self).__init__(register,
            'COUNT', 'ETM.ETMPIDR4.COUNT', 'read-only',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMPIDR0_PARTNUM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMPIDR0_PARTNUM, self).__init__(register,
            'PARTNUM', 'ETM.ETMPIDR0.PARTNUM', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMPIDR1_PARTNUM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMPIDR1_PARTNUM, self).__init__(register,
            'PARTNUM', 'ETM.ETMPIDR1.PARTNUM', 'read-only',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMPIDR1_IDCODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMPIDR1_IDCODE, self).__init__(register,
            'IDCODE', 'ETM.ETMPIDR1.IDCODE', 'read-only',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMPIDR2_IDCODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMPIDR2_IDCODE, self).__init__(register,
            'IDCODE', 'ETM.ETMPIDR2.IDCODE', 'read-only',
            "",
            0, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMPIDR2_ALWAYS1(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMPIDR2_ALWAYS1, self).__init__(register,
            'ALWAYS1', 'ETM.ETMPIDR2.ALWAYS1', 'read-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMPIDR2_REV(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMPIDR2_REV, self).__init__(register,
            'REV', 'ETM.ETMPIDR2.REV', 'read-only',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMPIDR3_CUSTMOD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMPIDR3_CUSTMOD, self).__init__(register,
            'CUSTMOD', 'ETM.ETMPIDR3.CUSTMOD', 'read-only',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMPIDR3_REVAND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMPIDR3_REVAND, self).__init__(register,
            'REVAND', 'ETM.ETMPIDR3.REVAND', 'read-only',
            "",
            4, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCIDR0_PREAMB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCIDR0_PREAMB, self).__init__(register,
            'PREAMB', 'ETM.ETMCIDR0.PREAMB', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCIDR1_PREAMB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCIDR1_PREAMB, self).__init__(register,
            'PREAMB', 'ETM.ETMCIDR1.PREAMB', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCIDR2_PREAMB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCIDR2_PREAMB, self).__init__(register,
            'PREAMB', 'ETM.ETMCIDR2.PREAMB', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_ETM_ETMCIDR3_PREAMB(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_ETM_ETMCIDR3_PREAMB, self).__init__(register,
            'PREAMB', 'ETM.ETMCIDR3.PREAMB', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


