
from static import Base_RM_Register
from ETM_field import *


class RM_Register_ETM_ETMCR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMCR, self).__init__(rmio, label,
            0xe0041000, 0x000,
            'ETMCR', 'ETM.ETMCR', 'read-write',
            "",
            0x00000411, 0x10632FF1)

        self.POWERDWN = RM_Field_ETM_ETMCR_POWERDWN(self)
        self.zz_fdict['POWERDWN'] = self.POWERDWN
        self.PORTSIZE = RM_Field_ETM_ETMCR_PORTSIZE(self)
        self.zz_fdict['PORTSIZE'] = self.PORTSIZE
        self.STALL = RM_Field_ETM_ETMCR_STALL(self)
        self.zz_fdict['STALL'] = self.STALL
        self.BRANCHOUTPUT = RM_Field_ETM_ETMCR_BRANCHOUTPUT(self)
        self.zz_fdict['BRANCHOUTPUT'] = self.BRANCHOUTPUT
        self.DBGREQCTRL = RM_Field_ETM_ETMCR_DBGREQCTRL(self)
        self.zz_fdict['DBGREQCTRL'] = self.DBGREQCTRL
        self.ETMPROG = RM_Field_ETM_ETMCR_ETMPROG(self)
        self.zz_fdict['ETMPROG'] = self.ETMPROG
        self.ETMPORTSEL = RM_Field_ETM_ETMCR_ETMPORTSEL(self)
        self.zz_fdict['ETMPORTSEL'] = self.ETMPORTSEL
        self.PORTMODE2 = RM_Field_ETM_ETMCR_PORTMODE2(self)
        self.zz_fdict['PORTMODE2'] = self.PORTMODE2
        self.PORTMODE = RM_Field_ETM_ETMCR_PORTMODE(self)
        self.zz_fdict['PORTMODE'] = self.PORTMODE
        self.EPORTSIZE = RM_Field_ETM_ETMCR_EPORTSIZE(self)
        self.zz_fdict['EPORTSIZE'] = self.EPORTSIZE
        self.TSTAMPEN = RM_Field_ETM_ETMCR_TSTAMPEN(self)
        self.zz_fdict['TSTAMPEN'] = self.TSTAMPEN
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMCCR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMCCR, self).__init__(rmio, label,
            0xe0041000, 0x004,
            'ETMCCR', 'ETM.ETMCCR', 'read-only',
            "",
            0x8C802000, 0x8FFFFFFF)

        self.ADRCMPPAIR = RM_Field_ETM_ETMCCR_ADRCMPPAIR(self)
        self.zz_fdict['ADRCMPPAIR'] = self.ADRCMPPAIR
        self.DATACMPNUM = RM_Field_ETM_ETMCCR_DATACMPNUM(self)
        self.zz_fdict['DATACMPNUM'] = self.DATACMPNUM
        self.MMDECCNT = RM_Field_ETM_ETMCCR_MMDECCNT(self)
        self.zz_fdict['MMDECCNT'] = self.MMDECCNT
        self.COUNTNUM = RM_Field_ETM_ETMCCR_COUNTNUM(self)
        self.zz_fdict['COUNTNUM'] = self.COUNTNUM
        self.SEQPRES = RM_Field_ETM_ETMCCR_SEQPRES(self)
        self.zz_fdict['SEQPRES'] = self.SEQPRES
        self.EXTINPNUM = RM_Field_ETM_ETMCCR_EXTINPNUM(self)
        self.zz_fdict['EXTINPNUM'] = self.EXTINPNUM
        self.EXTOUTNUM = RM_Field_ETM_ETMCCR_EXTOUTNUM(self)
        self.zz_fdict['EXTOUTNUM'] = self.EXTOUTNUM
        self.FIFOFULLPRES = RM_Field_ETM_ETMCCR_FIFOFULLPRES(self)
        self.zz_fdict['FIFOFULLPRES'] = self.FIFOFULLPRES
        self.IDCOMPNUM = RM_Field_ETM_ETMCCR_IDCOMPNUM(self)
        self.zz_fdict['IDCOMPNUM'] = self.IDCOMPNUM
        self.TRACESS = RM_Field_ETM_ETMCCR_TRACESS(self)
        self.zz_fdict['TRACESS'] = self.TRACESS
        self.MMACCESS = RM_Field_ETM_ETMCCR_MMACCESS(self)
        self.zz_fdict['MMACCESS'] = self.MMACCESS
        self.ETMID = RM_Field_ETM_ETMCCR_ETMID(self)
        self.zz_fdict['ETMID'] = self.ETMID
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMTRIGGER(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMTRIGGER, self).__init__(rmio, label,
            0xe0041000, 0x008,
            'ETMTRIGGER', 'ETM.ETMTRIGGER', 'read-write',
            "",
            0x00000000, 0x0001FFFF)

        self.RESA = RM_Field_ETM_ETMTRIGGER_RESA(self)
        self.zz_fdict['RESA'] = self.RESA
        self.RESB = RM_Field_ETM_ETMTRIGGER_RESB(self)
        self.zz_fdict['RESB'] = self.RESB
        self.ETMFCN = RM_Field_ETM_ETMTRIGGER_ETMFCN(self)
        self.zz_fdict['ETMFCN'] = self.ETMFCN
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMSR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMSR, self).__init__(rmio, label,
            0xe0041000, 0x010,
            'ETMSR', 'ETM.ETMSR', 'read-write',
            "",
            0x00000002, 0x0000000F)

        self.ETHOF = RM_Field_ETM_ETMSR_ETHOF(self)
        self.zz_fdict['ETHOF'] = self.ETHOF
        self.ETMPROGBIT = RM_Field_ETM_ETMSR_ETMPROGBIT(self)
        self.zz_fdict['ETMPROGBIT'] = self.ETMPROGBIT
        self.TRACESTAT = RM_Field_ETM_ETMSR_TRACESTAT(self)
        self.zz_fdict['TRACESTAT'] = self.TRACESTAT
        self.TRIGBIT = RM_Field_ETM_ETMSR_TRIGBIT(self)
        self.zz_fdict['TRIGBIT'] = self.TRIGBIT
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMSCR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMSCR, self).__init__(rmio, label,
            0xe0041000, 0x014,
            'ETMSCR', 'ETM.ETMSCR', 'read-only',
            "",
            0x00020D09, 0x00027F0F)

        self.MAXPORTSIZE = RM_Field_ETM_ETMSCR_MAXPORTSIZE(self)
        self.zz_fdict['MAXPORTSIZE'] = self.MAXPORTSIZE
        self.Reserved = RM_Field_ETM_ETMSCR_Reserved(self)
        self.zz_fdict['Reserved'] = self.Reserved
        self.FIFOFULL = RM_Field_ETM_ETMSCR_FIFOFULL(self)
        self.zz_fdict['FIFOFULL'] = self.FIFOFULL
        self.MAXPORTSIZE3 = RM_Field_ETM_ETMSCR_MAXPORTSIZE3(self)
        self.zz_fdict['MAXPORTSIZE3'] = self.MAXPORTSIZE3
        self.PORTSIZE = RM_Field_ETM_ETMSCR_PORTSIZE(self)
        self.zz_fdict['PORTSIZE'] = self.PORTSIZE
        self.PORTMODE = RM_Field_ETM_ETMSCR_PORTMODE(self)
        self.zz_fdict['PORTMODE'] = self.PORTMODE
        self.PROCNUM = RM_Field_ETM_ETMSCR_PROCNUM(self)
        self.zz_fdict['PROCNUM'] = self.PROCNUM
        self.NOFETCHCOMP = RM_Field_ETM_ETMSCR_NOFETCHCOMP(self)
        self.zz_fdict['NOFETCHCOMP'] = self.NOFETCHCOMP
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMTEEVR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMTEEVR, self).__init__(rmio, label,
            0xe0041000, 0x020,
            'ETMTEEVR', 'ETM.ETMTEEVR', 'read-write',
            "",
            0x00000000, 0x0001FFFF)

        self.RESA = RM_Field_ETM_ETMTEEVR_RESA(self)
        self.zz_fdict['RESA'] = self.RESA
        self.RESB = RM_Field_ETM_ETMTEEVR_RESB(self)
        self.zz_fdict['RESB'] = self.RESB
        self.ETMFCNEN = RM_Field_ETM_ETMTEEVR_ETMFCNEN(self)
        self.zz_fdict['ETMFCNEN'] = self.ETMFCNEN
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMTECR1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMTECR1, self).__init__(rmio, label,
            0xe0041000, 0x024,
            'ETMTECR1', 'ETM.ETMTECR1', 'read-write',
            "",
            0x00000000, 0x03FFFFFF)

        self.ADRCMP = RM_Field_ETM_ETMTECR1_ADRCMP(self)
        self.zz_fdict['ADRCMP'] = self.ADRCMP
        self.MEMMAP = RM_Field_ETM_ETMTECR1_MEMMAP(self)
        self.zz_fdict['MEMMAP'] = self.MEMMAP
        self.INCEXCTL = RM_Field_ETM_ETMTECR1_INCEXCTL(self)
        self.zz_fdict['INCEXCTL'] = self.INCEXCTL
        self.TCE = RM_Field_ETM_ETMTECR1_TCE(self)
        self.zz_fdict['TCE'] = self.TCE
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMFFLR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMFFLR, self).__init__(rmio, label,
            0xe0041000, 0x02C,
            'ETMFFLR', 'ETM.ETMFFLR', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.BYTENUM = RM_Field_ETM_ETMFFLR_BYTENUM(self)
        self.zz_fdict['BYTENUM'] = self.BYTENUM
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMCNTRLDVR1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMCNTRLDVR1, self).__init__(rmio, label,
            0xe0041000, 0x140,
            'ETMCNTRLDVR1', 'ETM.ETMCNTRLDVR1', 'read-write',
            "",
            0x00000000, 0x0000FFFF)

        self.COUNT = RM_Field_ETM_ETMCNTRLDVR1_COUNT(self)
        self.zz_fdict['COUNT'] = self.COUNT
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMSYNCFR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMSYNCFR, self).__init__(rmio, label,
            0xe0041000, 0x1E0,
            'ETMSYNCFR', 'ETM.ETMSYNCFR', 'read-write',
            "",
            0x00000400, 0x00000FFF)

        self.FREQ = RM_Field_ETM_ETMSYNCFR_FREQ(self)
        self.zz_fdict['FREQ'] = self.FREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMIDR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMIDR, self).__init__(rmio, label,
            0xe0041000, 0x1E4,
            'ETMIDR', 'ETM.ETMIDR', 'read-only',
            "",
            0x4114F253, 0xFF1DFFFF)

        self.IMPVER = RM_Field_ETM_ETMIDR_IMPVER(self)
        self.zz_fdict['IMPVER'] = self.IMPVER
        self.ETMMINVER = RM_Field_ETM_ETMIDR_ETMMINVER(self)
        self.zz_fdict['ETMMINVER'] = self.ETMMINVER
        self.ETMMAJVER = RM_Field_ETM_ETMIDR_ETMMAJVER(self)
        self.zz_fdict['ETMMAJVER'] = self.ETMMAJVER
        self.PROCFAM = RM_Field_ETM_ETMIDR_PROCFAM(self)
        self.zz_fdict['PROCFAM'] = self.PROCFAM
        self.LPCF = RM_Field_ETM_ETMIDR_LPCF(self)
        self.zz_fdict['LPCF'] = self.LPCF
        self.THUMBT = RM_Field_ETM_ETMIDR_THUMBT(self)
        self.zz_fdict['THUMBT'] = self.THUMBT
        self.SECEXT = RM_Field_ETM_ETMIDR_SECEXT(self)
        self.zz_fdict['SECEXT'] = self.SECEXT
        self.BPE = RM_Field_ETM_ETMIDR_BPE(self)
        self.zz_fdict['BPE'] = self.BPE
        self.IMPCODE = RM_Field_ETM_ETMIDR_IMPCODE(self)
        self.zz_fdict['IMPCODE'] = self.IMPCODE
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMCCER(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMCCER, self).__init__(rmio, label,
            0xe0041000, 0x1E8,
            'ETMCCER', 'ETM.ETMCCER', 'read-only',
            "",
            0x18541800, 0x387FFFFB)

        self.EXTINPSEL = RM_Field_ETM_ETMCCER_EXTINPSEL(self)
        self.zz_fdict['EXTINPSEL'] = self.EXTINPSEL
        self.EXTINPBUS = RM_Field_ETM_ETMCCER_EXTINPBUS(self)
        self.zz_fdict['EXTINPBUS'] = self.EXTINPBUS
        self.READREGS = RM_Field_ETM_ETMCCER_READREGS(self)
        self.zz_fdict['READREGS'] = self.READREGS
        self.DADDRCMP = RM_Field_ETM_ETMCCER_DADDRCMP(self)
        self.zz_fdict['DADDRCMP'] = self.DADDRCMP
        self.INSTRES = RM_Field_ETM_ETMCCER_INSTRES(self)
        self.zz_fdict['INSTRES'] = self.INSTRES
        self.EICEWPNT = RM_Field_ETM_ETMCCER_EICEWPNT(self)
        self.zz_fdict['EICEWPNT'] = self.EICEWPNT
        self.TEICEWPNT = RM_Field_ETM_ETMCCER_TEICEWPNT(self)
        self.zz_fdict['TEICEWPNT'] = self.TEICEWPNT
        self.EICEIMP = RM_Field_ETM_ETMCCER_EICEIMP(self)
        self.zz_fdict['EICEIMP'] = self.EICEIMP
        self.TIMP = RM_Field_ETM_ETMCCER_TIMP(self)
        self.zz_fdict['TIMP'] = self.TIMP
        self.RFCNT = RM_Field_ETM_ETMCCER_RFCNT(self)
        self.zz_fdict['RFCNT'] = self.RFCNT
        self.TENC = RM_Field_ETM_ETMCCER_TENC(self)
        self.zz_fdict['TENC'] = self.TENC
        self.TSIZE = RM_Field_ETM_ETMCCER_TSIZE(self)
        self.zz_fdict['TSIZE'] = self.TSIZE
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMTESSEICR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMTESSEICR, self).__init__(rmio, label,
            0xe0041000, 0x1F0,
            'ETMTESSEICR', 'ETM.ETMTESSEICR', 'read-write',
            "",
            0x00000000, 0x000F000F)

        self.STARTRSEL = RM_Field_ETM_ETMTESSEICR_STARTRSEL(self)
        self.zz_fdict['STARTRSEL'] = self.STARTRSEL
        self.STOPRSEL = RM_Field_ETM_ETMTESSEICR_STOPRSEL(self)
        self.zz_fdict['STOPRSEL'] = self.STOPRSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMTSEVR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMTSEVR, self).__init__(rmio, label,
            0xe0041000, 0x1F8,
            'ETMTSEVR', 'ETM.ETMTSEVR', 'read-write',
            "",
            0x00000000, 0x0001FFFF)

        self.RESAEVT = RM_Field_ETM_ETMTSEVR_RESAEVT(self)
        self.zz_fdict['RESAEVT'] = self.RESAEVT
        self.RESBEVT = RM_Field_ETM_ETMTSEVR_RESBEVT(self)
        self.zz_fdict['RESBEVT'] = self.RESBEVT
        self.ETMFCNEVT = RM_Field_ETM_ETMTSEVR_ETMFCNEVT(self)
        self.zz_fdict['ETMFCNEVT'] = self.ETMFCNEVT
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMTRACEIDR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMTRACEIDR, self).__init__(rmio, label,
            0xe0041000, 0x200,
            'ETMTRACEIDR', 'ETM.ETMTRACEIDR', 'read-write',
            "",
            0x00000000, 0x0000007F)

        self.TRACEID = RM_Field_ETM_ETMTRACEIDR_TRACEID(self)
        self.zz_fdict['TRACEID'] = self.TRACEID
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMIDR2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMIDR2, self).__init__(rmio, label,
            0xe0041000, 0x208,
            'ETMIDR2', 'ETM.ETMIDR2', 'read-only',
            "",
            0x00000000, 0x00000003)

        self.RFE = RM_Field_ETM_ETMIDR2_RFE(self)
        self.zz_fdict['RFE'] = self.RFE
        self.SWP = RM_Field_ETM_ETMIDR2_SWP(self)
        self.zz_fdict['SWP'] = self.SWP
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMPDSR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMPDSR, self).__init__(rmio, label,
            0xe0041000, 0x314,
            'ETMPDSR', 'ETM.ETMPDSR', 'read-only',
            "",
            0x00000001, 0x00000001)

        self.ETMUP = RM_Field_ETM_ETMPDSR_ETMUP(self)
        self.zz_fdict['ETMUP'] = self.ETMUP
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMISCIN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMISCIN, self).__init__(rmio, label,
            0xe0041000, 0xEE0,
            'ETMISCIN', 'ETM.ETMISCIN', 'read-write',
            "",
            0x00000000, 0x00000013)

        self.EXTIN = RM_Field_ETM_ETMISCIN_EXTIN(self)
        self.zz_fdict['EXTIN'] = self.EXTIN
        self.COREHALT = RM_Field_ETM_ETMISCIN_COREHALT(self)
        self.zz_fdict['COREHALT'] = self.COREHALT
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ITTRIGOUT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ITTRIGOUT, self).__init__(rmio, label,
            0xe0041000, 0xEE8,
            'ITTRIGOUT', 'ETM.ITTRIGOUT', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.TRIGGEROUT = RM_Field_ETM_ITTRIGOUT_TRIGGEROUT(self)
        self.zz_fdict['TRIGGEROUT'] = self.TRIGGEROUT
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMITATBCTR2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMITATBCTR2, self).__init__(rmio, label,
            0xe0041000, 0xEF0,
            'ETMITATBCTR2', 'ETM.ETMITATBCTR2', 'read-only',
            "",
            0x00000001, 0x00000001)

        self.ATREADY = RM_Field_ETM_ETMITATBCTR2_ATREADY(self)
        self.zz_fdict['ATREADY'] = self.ATREADY
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMITATBCTR0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMITATBCTR0, self).__init__(rmio, label,
            0xe0041000, 0xEF8,
            'ETMITATBCTR0', 'ETM.ETMITATBCTR0', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.ATVALID = RM_Field_ETM_ETMITATBCTR0_ATVALID(self)
        self.zz_fdict['ATVALID'] = self.ATVALID
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMITCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMITCTRL, self).__init__(rmio, label,
            0xe0041000, 0xF00,
            'ETMITCTRL', 'ETM.ETMITCTRL', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.ITEN = RM_Field_ETM_ETMITCTRL_ITEN(self)
        self.zz_fdict['ITEN'] = self.ITEN
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMCLAIMSET(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMCLAIMSET, self).__init__(rmio, label,
            0xe0041000, 0xFA0,
            'ETMCLAIMSET', 'ETM.ETMCLAIMSET', 'read-write',
            "",
            0x0000000F, 0x000000FF)

        self.SETTAG = RM_Field_ETM_ETMCLAIMSET_SETTAG(self)
        self.zz_fdict['SETTAG'] = self.SETTAG
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMCLAIMCLR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMCLAIMCLR, self).__init__(rmio, label,
            0xe0041000, 0xFA4,
            'ETMCLAIMCLR', 'ETM.ETMCLAIMCLR', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.CLRTAG = RM_Field_ETM_ETMCLAIMCLR_CLRTAG(self)
        self.zz_fdict['CLRTAG'] = self.CLRTAG
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMLAR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMLAR, self).__init__(rmio, label,
            0xe0041000, 0xFB0,
            'ETMLAR', 'ETM.ETMLAR', 'read-write',
            "",
            0x00000000, 0x00000001)

        self.KEY = RM_Field_ETM_ETMLAR_KEY(self)
        self.zz_fdict['KEY'] = self.KEY
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMLSR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMLSR, self).__init__(rmio, label,
            0xe0041000, 0xFB4,
            'ETMLSR', 'ETM.ETMLSR', 'read-only',
            "",
            0x00000003, 0x00000003)

        self.LOCKIMP = RM_Field_ETM_ETMLSR_LOCKIMP(self)
        self.zz_fdict['LOCKIMP'] = self.LOCKIMP
        self.LOCKED = RM_Field_ETM_ETMLSR_LOCKED(self)
        self.zz_fdict['LOCKED'] = self.LOCKED
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMAUTHSTATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMAUTHSTATUS, self).__init__(rmio, label,
            0xe0041000, 0xFB8,
            'ETMAUTHSTATUS', 'ETM.ETMAUTHSTATUS', 'read-only',
            "",
            0x000000C0, 0x000000FF)

        self.NONSECINVDBG = RM_Field_ETM_ETMAUTHSTATUS_NONSECINVDBG(self)
        self.zz_fdict['NONSECINVDBG'] = self.NONSECINVDBG
        self.NONSECNONINVDBG = RM_Field_ETM_ETMAUTHSTATUS_NONSECNONINVDBG(self)
        self.zz_fdict['NONSECNONINVDBG'] = self.NONSECNONINVDBG
        self.SECINVDBG = RM_Field_ETM_ETMAUTHSTATUS_SECINVDBG(self)
        self.zz_fdict['SECINVDBG'] = self.SECINVDBG
        self.SECNONINVDBG = RM_Field_ETM_ETMAUTHSTATUS_SECNONINVDBG(self)
        self.zz_fdict['SECNONINVDBG'] = self.SECNONINVDBG
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMDEVTYPE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMDEVTYPE, self).__init__(rmio, label,
            0xe0041000, 0xFCC,
            'ETMDEVTYPE', 'ETM.ETMDEVTYPE', 'read-only',
            "",
            0x00000013, 0x000000FF)

        self.TRACESRC = RM_Field_ETM_ETMDEVTYPE_TRACESRC(self)
        self.zz_fdict['TRACESRC'] = self.TRACESRC
        self.PROCTRACE = RM_Field_ETM_ETMDEVTYPE_PROCTRACE(self)
        self.zz_fdict['PROCTRACE'] = self.PROCTRACE
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMPIDR4(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMPIDR4, self).__init__(rmio, label,
            0xe0041000, 0xFD0,
            'ETMPIDR4', 'ETM.ETMPIDR4', 'read-only',
            "",
            0x00000004, 0x000000FF)

        self.CONTCODE = RM_Field_ETM_ETMPIDR4_CONTCODE(self)
        self.zz_fdict['CONTCODE'] = self.CONTCODE
        self.COUNT = RM_Field_ETM_ETMPIDR4_COUNT(self)
        self.zz_fdict['COUNT'] = self.COUNT
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMPIDR0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMPIDR0, self).__init__(rmio, label,
            0xe0041000, 0xFE0,
            'ETMPIDR0', 'ETM.ETMPIDR0', 'read-only',
            "",
            0x00000025, 0x000000FF)

        self.PARTNUM = RM_Field_ETM_ETMPIDR0_PARTNUM(self)
        self.zz_fdict['PARTNUM'] = self.PARTNUM
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMPIDR1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMPIDR1, self).__init__(rmio, label,
            0xe0041000, 0xFE4,
            'ETMPIDR1', 'ETM.ETMPIDR1', 'read-only',
            "",
            0x000000B9, 0x000000FF)

        self.PARTNUM = RM_Field_ETM_ETMPIDR1_PARTNUM(self)
        self.zz_fdict['PARTNUM'] = self.PARTNUM
        self.IDCODE = RM_Field_ETM_ETMPIDR1_IDCODE(self)
        self.zz_fdict['IDCODE'] = self.IDCODE
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMPIDR2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMPIDR2, self).__init__(rmio, label,
            0xe0041000, 0xFE8,
            'ETMPIDR2', 'ETM.ETMPIDR2', 'read-only',
            "",
            0x0000000B, 0x000000FF)

        self.IDCODE = RM_Field_ETM_ETMPIDR2_IDCODE(self)
        self.zz_fdict['IDCODE'] = self.IDCODE
        self.ALWAYS1 = RM_Field_ETM_ETMPIDR2_ALWAYS1(self)
        self.zz_fdict['ALWAYS1'] = self.ALWAYS1
        self.REV = RM_Field_ETM_ETMPIDR2_REV(self)
        self.zz_fdict['REV'] = self.REV
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMPIDR3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMPIDR3, self).__init__(rmio, label,
            0xe0041000, 0xFEC,
            'ETMPIDR3', 'ETM.ETMPIDR3', 'read-only',
            "",
            0x00000000, 0x000000FF)

        self.CUSTMOD = RM_Field_ETM_ETMPIDR3_CUSTMOD(self)
        self.zz_fdict['CUSTMOD'] = self.CUSTMOD
        self.REVAND = RM_Field_ETM_ETMPIDR3_REVAND(self)
        self.zz_fdict['REVAND'] = self.REVAND
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMCIDR0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMCIDR0, self).__init__(rmio, label,
            0xe0041000, 0xFF0,
            'ETMCIDR0', 'ETM.ETMCIDR0', 'read-only',
            "",
            0x0000000D, 0x000000FF)

        self.PREAMB = RM_Field_ETM_ETMCIDR0_PREAMB(self)
        self.zz_fdict['PREAMB'] = self.PREAMB
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMCIDR1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMCIDR1, self).__init__(rmio, label,
            0xe0041000, 0xFF4,
            'ETMCIDR1', 'ETM.ETMCIDR1', 'read-only',
            "",
            0x00000090, 0x000000FF)

        self.PREAMB = RM_Field_ETM_ETMCIDR1_PREAMB(self)
        self.zz_fdict['PREAMB'] = self.PREAMB
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMCIDR2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMCIDR2, self).__init__(rmio, label,
            0xe0041000, 0xFF8,
            'ETMCIDR2', 'ETM.ETMCIDR2', 'read-only',
            "",
            0x00000005, 0x000000FF)

        self.PREAMB = RM_Field_ETM_ETMCIDR2_PREAMB(self)
        self.zz_fdict['PREAMB'] = self.PREAMB
        self.__dict__['zz_frozen'] = True


class RM_Register_ETM_ETMCIDR3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_ETM_ETMCIDR3, self).__init__(rmio, label,
            0xe0041000, 0xFFC,
            'ETMCIDR3', 'ETM.ETMCIDR3', 'read-only',
            "",
            0x000000B1, 0x000000FF)

        self.PREAMB = RM_Field_ETM_ETMCIDR3_PREAMB(self)
        self.zz_fdict['PREAMB'] = self.PREAMB
        self.__dict__['zz_frozen'] = True


