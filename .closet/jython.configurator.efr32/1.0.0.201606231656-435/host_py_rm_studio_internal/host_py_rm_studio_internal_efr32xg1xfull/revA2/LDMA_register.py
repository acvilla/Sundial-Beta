
from static import Base_RM_Register
from LDMA_field import *


class RM_Register_LDMA_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CTRL, self).__init__(rmio, label,
            0x400e2000, 0x000,
            'CTRL', 'LDMA.CTRL', 'read-write',
            "",
            0x07000000, 0x8700FFFF)

        self.SYNCPRSSETEN = RM_Field_LDMA_CTRL_SYNCPRSSETEN(self)
        self.zz_fdict['SYNCPRSSETEN'] = self.SYNCPRSSETEN
        self.SYNCPRSCLREN = RM_Field_LDMA_CTRL_SYNCPRSCLREN(self)
        self.zz_fdict['SYNCPRSCLREN'] = self.SYNCPRSCLREN
        self.NUMFIXED = RM_Field_LDMA_CTRL_NUMFIXED(self)
        self.zz_fdict['NUMFIXED'] = self.NUMFIXED
        self.RESET = RM_Field_LDMA_CTRL_RESET(self)
        self.zz_fdict['RESET'] = self.RESET
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_STATUS, self).__init__(rmio, label,
            0x400e2000, 0x004,
            'STATUS', 'LDMA.STATUS', 'read-only',
            "",
            0x08100000, 0x1F1F073B)

        self.ANYBUSY = RM_Field_LDMA_STATUS_ANYBUSY(self)
        self.zz_fdict['ANYBUSY'] = self.ANYBUSY
        self.ANYREQ = RM_Field_LDMA_STATUS_ANYREQ(self)
        self.zz_fdict['ANYREQ'] = self.ANYREQ
        self.CHGRANT = RM_Field_LDMA_STATUS_CHGRANT(self)
        self.zz_fdict['CHGRANT'] = self.CHGRANT
        self.CHERROR = RM_Field_LDMA_STATUS_CHERROR(self)
        self.zz_fdict['CHERROR'] = self.CHERROR
        self.FIFOLEVEL = RM_Field_LDMA_STATUS_FIFOLEVEL(self)
        self.zz_fdict['FIFOLEVEL'] = self.FIFOLEVEL
        self.CHNUM = RM_Field_LDMA_STATUS_CHNUM(self)
        self.zz_fdict['CHNUM'] = self.CHNUM
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_SYNC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_SYNC, self).__init__(rmio, label,
            0x400e2000, 0x008,
            'SYNC', 'LDMA.SYNC', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.SYNCTRIG = RM_Field_LDMA_SYNC_SYNCTRIG(self)
        self.zz_fdict['SYNCTRIG'] = self.SYNCTRIG
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CHEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CHEN, self).__init__(rmio, label,
            0x400e2000, 0x020,
            'CHEN', 'LDMA.CHEN', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.CHEN = RM_Field_LDMA_CHEN_CHEN(self)
        self.zz_fdict['CHEN'] = self.CHEN
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CHBUSY(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CHBUSY, self).__init__(rmio, label,
            0x400e2000, 0x024,
            'CHBUSY', 'LDMA.CHBUSY', 'read-only',
            "",
            0x00000000, 0x000000FF)

        self.BUSY = RM_Field_LDMA_CHBUSY_BUSY(self)
        self.zz_fdict['BUSY'] = self.BUSY
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CHDONE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CHDONE, self).__init__(rmio, label,
            0x400e2000, 0x028,
            'CHDONE', 'LDMA.CHDONE', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.CHDONE = RM_Field_LDMA_CHDONE_CHDONE(self)
        self.zz_fdict['CHDONE'] = self.CHDONE
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_DBGHALT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_DBGHALT, self).__init__(rmio, label,
            0x400e2000, 0x02C,
            'DBGHALT', 'LDMA.DBGHALT', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.DBGHALT = RM_Field_LDMA_DBGHALT_DBGHALT(self)
        self.zz_fdict['DBGHALT'] = self.DBGHALT
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_SWREQ(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_SWREQ, self).__init__(rmio, label,
            0x400e2000, 0x030,
            'SWREQ', 'LDMA.SWREQ', 'write-only',
            "",
            0x00000000, 0x000000FF)

        self.SWREQ = RM_Field_LDMA_SWREQ_SWREQ(self)
        self.zz_fdict['SWREQ'] = self.SWREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_REQDIS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_REQDIS, self).__init__(rmio, label,
            0x400e2000, 0x034,
            'REQDIS', 'LDMA.REQDIS', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.REQDIS = RM_Field_LDMA_REQDIS_REQDIS(self)
        self.zz_fdict['REQDIS'] = self.REQDIS
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_REQPEND(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_REQPEND, self).__init__(rmio, label,
            0x400e2000, 0x038,
            'REQPEND', 'LDMA.REQPEND', 'read-only',
            "",
            0x00000000, 0x000000FF)

        self.REQPEND = RM_Field_LDMA_REQPEND_REQPEND(self)
        self.zz_fdict['REQPEND'] = self.REQPEND
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_LINKLOAD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_LINKLOAD, self).__init__(rmio, label,
            0x400e2000, 0x03C,
            'LINKLOAD', 'LDMA.LINKLOAD', 'write-only',
            "",
            0x00000000, 0x000000FF)

        self.LINKLOAD = RM_Field_LDMA_LINKLOAD_LINKLOAD(self)
        self.zz_fdict['LINKLOAD'] = self.LINKLOAD
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_REQCLEAR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_REQCLEAR, self).__init__(rmio, label,
            0x400e2000, 0x040,
            'REQCLEAR', 'LDMA.REQCLEAR', 'write-only',
            "",
            0x00000000, 0x000000FF)

        self.REQCLEAR = RM_Field_LDMA_REQCLEAR_REQCLEAR(self)
        self.zz_fdict['REQCLEAR'] = self.REQCLEAR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_IF, self).__init__(rmio, label,
            0x400e2000, 0x060,
            'IF', 'LDMA.IF', 'read-only',
            "",
            0x00000000, 0x800000FF)

        self.DONE = RM_Field_LDMA_IF_DONE(self)
        self.zz_fdict['DONE'] = self.DONE
        self.ERROR = RM_Field_LDMA_IF_ERROR(self)
        self.zz_fdict['ERROR'] = self.ERROR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_IFS, self).__init__(rmio, label,
            0x400e2000, 0x064,
            'IFS', 'LDMA.IFS', 'write-only',
            "",
            0x00000000, 0x800000FF)

        self.DONE = RM_Field_LDMA_IFS_DONE(self)
        self.zz_fdict['DONE'] = self.DONE
        self.ERROR = RM_Field_LDMA_IFS_ERROR(self)
        self.zz_fdict['ERROR'] = self.ERROR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_IFC, self).__init__(rmio, label,
            0x400e2000, 0x068,
            'IFC', 'LDMA.IFC', 'write-only',
            "",
            0x00000000, 0x800000FF)

        self.DONE = RM_Field_LDMA_IFC_DONE(self)
        self.zz_fdict['DONE'] = self.DONE
        self.ERROR = RM_Field_LDMA_IFC_ERROR(self)
        self.zz_fdict['ERROR'] = self.ERROR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_IEN, self).__init__(rmio, label,
            0x400e2000, 0x06C,
            'IEN', 'LDMA.IEN', 'read-write',
            "",
            0x00000000, 0x800000FF)

        self.DONE = RM_Field_LDMA_IEN_DONE(self)
        self.zz_fdict['DONE'] = self.DONE
        self.ERROR = RM_Field_LDMA_IEN_ERROR(self)
        self.zz_fdict['ERROR'] = self.ERROR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH0_REQSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH0_REQSEL, self).__init__(rmio, label,
            0x400e2000, 0x080,
            'CH0_REQSEL', 'LDMA.CH0_REQSEL', 'read-write',
            "",
            0x00000000, 0x003F000F)

        self.SIGSEL = RM_Field_LDMA_CH0_REQSEL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_LDMA_CH0_REQSEL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH0_CFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH0_CFG, self).__init__(rmio, label,
            0x400e2000, 0x084,
            'CH0_CFG', 'LDMA.CH0_CFG', 'read-write',
            "",
            0x00000000, 0x00330000)

        self.ARBSLOTS = RM_Field_LDMA_CH0_CFG_ARBSLOTS(self)
        self.zz_fdict['ARBSLOTS'] = self.ARBSLOTS
        self.SRCINCSIGN = RM_Field_LDMA_CH0_CFG_SRCINCSIGN(self)
        self.zz_fdict['SRCINCSIGN'] = self.SRCINCSIGN
        self.DSTINCSIGN = RM_Field_LDMA_CH0_CFG_DSTINCSIGN(self)
        self.zz_fdict['DSTINCSIGN'] = self.DSTINCSIGN
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH0_LOOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH0_LOOP, self).__init__(rmio, label,
            0x400e2000, 0x088,
            'CH0_LOOP', 'LDMA.CH0_LOOP', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.LOOPCNT = RM_Field_LDMA_CH0_LOOP_LOOPCNT(self)
        self.zz_fdict['LOOPCNT'] = self.LOOPCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH0_CTRL, self).__init__(rmio, label,
            0x400e2000, 0x08C,
            'CH0_CTRL', 'LDMA.CH0_CTRL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFB)

        self.STRUCTTYPE = RM_Field_LDMA_CH0_CTRL_STRUCTTYPE(self)
        self.zz_fdict['STRUCTTYPE'] = self.STRUCTTYPE
        self.STRUCTREQ = RM_Field_LDMA_CH0_CTRL_STRUCTREQ(self)
        self.zz_fdict['STRUCTREQ'] = self.STRUCTREQ
        self.XFERCNT = RM_Field_LDMA_CH0_CTRL_XFERCNT(self)
        self.zz_fdict['XFERCNT'] = self.XFERCNT
        self.BYTESWAP = RM_Field_LDMA_CH0_CTRL_BYTESWAP(self)
        self.zz_fdict['BYTESWAP'] = self.BYTESWAP
        self.BLOCKSIZE = RM_Field_LDMA_CH0_CTRL_BLOCKSIZE(self)
        self.zz_fdict['BLOCKSIZE'] = self.BLOCKSIZE
        self.DONEIFSEN = RM_Field_LDMA_CH0_CTRL_DONEIFSEN(self)
        self.zz_fdict['DONEIFSEN'] = self.DONEIFSEN
        self.REQMODE = RM_Field_LDMA_CH0_CTRL_REQMODE(self)
        self.zz_fdict['REQMODE'] = self.REQMODE
        self.DECLOOPCNT = RM_Field_LDMA_CH0_CTRL_DECLOOPCNT(self)
        self.zz_fdict['DECLOOPCNT'] = self.DECLOOPCNT
        self.IGNORESREQ = RM_Field_LDMA_CH0_CTRL_IGNORESREQ(self)
        self.zz_fdict['IGNORESREQ'] = self.IGNORESREQ
        self.SRCINC = RM_Field_LDMA_CH0_CTRL_SRCINC(self)
        self.zz_fdict['SRCINC'] = self.SRCINC
        self.SIZE = RM_Field_LDMA_CH0_CTRL_SIZE(self)
        self.zz_fdict['SIZE'] = self.SIZE
        self.DSTINC = RM_Field_LDMA_CH0_CTRL_DSTINC(self)
        self.zz_fdict['DSTINC'] = self.DSTINC
        self.SRCMODE = RM_Field_LDMA_CH0_CTRL_SRCMODE(self)
        self.zz_fdict['SRCMODE'] = self.SRCMODE
        self.DSTMODE = RM_Field_LDMA_CH0_CTRL_DSTMODE(self)
        self.zz_fdict['DSTMODE'] = self.DSTMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH0_SRC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH0_SRC, self).__init__(rmio, label,
            0x400e2000, 0x090,
            'CH0_SRC', 'LDMA.CH0_SRC', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.SRCADDR = RM_Field_LDMA_CH0_SRC_SRCADDR(self)
        self.zz_fdict['SRCADDR'] = self.SRCADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH0_DST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH0_DST, self).__init__(rmio, label,
            0x400e2000, 0x094,
            'CH0_DST', 'LDMA.CH0_DST', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DSTADDR = RM_Field_LDMA_CH0_DST_DSTADDR(self)
        self.zz_fdict['DSTADDR'] = self.DSTADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH0_LINK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH0_LINK, self).__init__(rmio, label,
            0x400e2000, 0x098,
            'CH0_LINK', 'LDMA.CH0_LINK', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.LINKMODE = RM_Field_LDMA_CH0_LINK_LINKMODE(self)
        self.zz_fdict['LINKMODE'] = self.LINKMODE
        self.LINK = RM_Field_LDMA_CH0_LINK_LINK(self)
        self.zz_fdict['LINK'] = self.LINK
        self.LINKADDR = RM_Field_LDMA_CH0_LINK_LINKADDR(self)
        self.zz_fdict['LINKADDR'] = self.LINKADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH1_REQSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH1_REQSEL, self).__init__(rmio, label,
            0x400e2000, 0x0B0,
            'CH1_REQSEL', 'LDMA.CH1_REQSEL', 'read-write',
            "",
            0x00000000, 0x003F000F)

        self.SIGSEL = RM_Field_LDMA_CH1_REQSEL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_LDMA_CH1_REQSEL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH1_CFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH1_CFG, self).__init__(rmio, label,
            0x400e2000, 0x0B4,
            'CH1_CFG', 'LDMA.CH1_CFG', 'read-write',
            "",
            0x00000000, 0x00330000)

        self.ARBSLOTS = RM_Field_LDMA_CH1_CFG_ARBSLOTS(self)
        self.zz_fdict['ARBSLOTS'] = self.ARBSLOTS
        self.SRCINCSIGN = RM_Field_LDMA_CH1_CFG_SRCINCSIGN(self)
        self.zz_fdict['SRCINCSIGN'] = self.SRCINCSIGN
        self.DSTINCSIGN = RM_Field_LDMA_CH1_CFG_DSTINCSIGN(self)
        self.zz_fdict['DSTINCSIGN'] = self.DSTINCSIGN
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH1_LOOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH1_LOOP, self).__init__(rmio, label,
            0x400e2000, 0x0B8,
            'CH1_LOOP', 'LDMA.CH1_LOOP', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.LOOPCNT = RM_Field_LDMA_CH1_LOOP_LOOPCNT(self)
        self.zz_fdict['LOOPCNT'] = self.LOOPCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH1_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH1_CTRL, self).__init__(rmio, label,
            0x400e2000, 0x0BC,
            'CH1_CTRL', 'LDMA.CH1_CTRL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFB)

        self.STRUCTTYPE = RM_Field_LDMA_CH1_CTRL_STRUCTTYPE(self)
        self.zz_fdict['STRUCTTYPE'] = self.STRUCTTYPE
        self.STRUCTREQ = RM_Field_LDMA_CH1_CTRL_STRUCTREQ(self)
        self.zz_fdict['STRUCTREQ'] = self.STRUCTREQ
        self.XFERCNT = RM_Field_LDMA_CH1_CTRL_XFERCNT(self)
        self.zz_fdict['XFERCNT'] = self.XFERCNT
        self.BYTESWAP = RM_Field_LDMA_CH1_CTRL_BYTESWAP(self)
        self.zz_fdict['BYTESWAP'] = self.BYTESWAP
        self.BLOCKSIZE = RM_Field_LDMA_CH1_CTRL_BLOCKSIZE(self)
        self.zz_fdict['BLOCKSIZE'] = self.BLOCKSIZE
        self.DONEIFSEN = RM_Field_LDMA_CH1_CTRL_DONEIFSEN(self)
        self.zz_fdict['DONEIFSEN'] = self.DONEIFSEN
        self.REQMODE = RM_Field_LDMA_CH1_CTRL_REQMODE(self)
        self.zz_fdict['REQMODE'] = self.REQMODE
        self.DECLOOPCNT = RM_Field_LDMA_CH1_CTRL_DECLOOPCNT(self)
        self.zz_fdict['DECLOOPCNT'] = self.DECLOOPCNT
        self.IGNORESREQ = RM_Field_LDMA_CH1_CTRL_IGNORESREQ(self)
        self.zz_fdict['IGNORESREQ'] = self.IGNORESREQ
        self.SRCINC = RM_Field_LDMA_CH1_CTRL_SRCINC(self)
        self.zz_fdict['SRCINC'] = self.SRCINC
        self.SIZE = RM_Field_LDMA_CH1_CTRL_SIZE(self)
        self.zz_fdict['SIZE'] = self.SIZE
        self.DSTINC = RM_Field_LDMA_CH1_CTRL_DSTINC(self)
        self.zz_fdict['DSTINC'] = self.DSTINC
        self.SRCMODE = RM_Field_LDMA_CH1_CTRL_SRCMODE(self)
        self.zz_fdict['SRCMODE'] = self.SRCMODE
        self.DSTMODE = RM_Field_LDMA_CH1_CTRL_DSTMODE(self)
        self.zz_fdict['DSTMODE'] = self.DSTMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH1_SRC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH1_SRC, self).__init__(rmio, label,
            0x400e2000, 0x0C0,
            'CH1_SRC', 'LDMA.CH1_SRC', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.SRCADDR = RM_Field_LDMA_CH1_SRC_SRCADDR(self)
        self.zz_fdict['SRCADDR'] = self.SRCADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH1_DST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH1_DST, self).__init__(rmio, label,
            0x400e2000, 0x0C4,
            'CH1_DST', 'LDMA.CH1_DST', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DSTADDR = RM_Field_LDMA_CH1_DST_DSTADDR(self)
        self.zz_fdict['DSTADDR'] = self.DSTADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH1_LINK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH1_LINK, self).__init__(rmio, label,
            0x400e2000, 0x0C8,
            'CH1_LINK', 'LDMA.CH1_LINK', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.LINKMODE = RM_Field_LDMA_CH1_LINK_LINKMODE(self)
        self.zz_fdict['LINKMODE'] = self.LINKMODE
        self.LINK = RM_Field_LDMA_CH1_LINK_LINK(self)
        self.zz_fdict['LINK'] = self.LINK
        self.LINKADDR = RM_Field_LDMA_CH1_LINK_LINKADDR(self)
        self.zz_fdict['LINKADDR'] = self.LINKADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH2_REQSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH2_REQSEL, self).__init__(rmio, label,
            0x400e2000, 0x0E0,
            'CH2_REQSEL', 'LDMA.CH2_REQSEL', 'read-write',
            "",
            0x00000000, 0x003F000F)

        self.SIGSEL = RM_Field_LDMA_CH2_REQSEL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_LDMA_CH2_REQSEL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH2_CFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH2_CFG, self).__init__(rmio, label,
            0x400e2000, 0x0E4,
            'CH2_CFG', 'LDMA.CH2_CFG', 'read-write',
            "",
            0x00000000, 0x00330000)

        self.ARBSLOTS = RM_Field_LDMA_CH2_CFG_ARBSLOTS(self)
        self.zz_fdict['ARBSLOTS'] = self.ARBSLOTS
        self.SRCINCSIGN = RM_Field_LDMA_CH2_CFG_SRCINCSIGN(self)
        self.zz_fdict['SRCINCSIGN'] = self.SRCINCSIGN
        self.DSTINCSIGN = RM_Field_LDMA_CH2_CFG_DSTINCSIGN(self)
        self.zz_fdict['DSTINCSIGN'] = self.DSTINCSIGN
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH2_LOOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH2_LOOP, self).__init__(rmio, label,
            0x400e2000, 0x0E8,
            'CH2_LOOP', 'LDMA.CH2_LOOP', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.LOOPCNT = RM_Field_LDMA_CH2_LOOP_LOOPCNT(self)
        self.zz_fdict['LOOPCNT'] = self.LOOPCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH2_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH2_CTRL, self).__init__(rmio, label,
            0x400e2000, 0x0EC,
            'CH2_CTRL', 'LDMA.CH2_CTRL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFB)

        self.STRUCTTYPE = RM_Field_LDMA_CH2_CTRL_STRUCTTYPE(self)
        self.zz_fdict['STRUCTTYPE'] = self.STRUCTTYPE
        self.STRUCTREQ = RM_Field_LDMA_CH2_CTRL_STRUCTREQ(self)
        self.zz_fdict['STRUCTREQ'] = self.STRUCTREQ
        self.XFERCNT = RM_Field_LDMA_CH2_CTRL_XFERCNT(self)
        self.zz_fdict['XFERCNT'] = self.XFERCNT
        self.BYTESWAP = RM_Field_LDMA_CH2_CTRL_BYTESWAP(self)
        self.zz_fdict['BYTESWAP'] = self.BYTESWAP
        self.BLOCKSIZE = RM_Field_LDMA_CH2_CTRL_BLOCKSIZE(self)
        self.zz_fdict['BLOCKSIZE'] = self.BLOCKSIZE
        self.DONEIFSEN = RM_Field_LDMA_CH2_CTRL_DONEIFSEN(self)
        self.zz_fdict['DONEIFSEN'] = self.DONEIFSEN
        self.REQMODE = RM_Field_LDMA_CH2_CTRL_REQMODE(self)
        self.zz_fdict['REQMODE'] = self.REQMODE
        self.DECLOOPCNT = RM_Field_LDMA_CH2_CTRL_DECLOOPCNT(self)
        self.zz_fdict['DECLOOPCNT'] = self.DECLOOPCNT
        self.IGNORESREQ = RM_Field_LDMA_CH2_CTRL_IGNORESREQ(self)
        self.zz_fdict['IGNORESREQ'] = self.IGNORESREQ
        self.SRCINC = RM_Field_LDMA_CH2_CTRL_SRCINC(self)
        self.zz_fdict['SRCINC'] = self.SRCINC
        self.SIZE = RM_Field_LDMA_CH2_CTRL_SIZE(self)
        self.zz_fdict['SIZE'] = self.SIZE
        self.DSTINC = RM_Field_LDMA_CH2_CTRL_DSTINC(self)
        self.zz_fdict['DSTINC'] = self.DSTINC
        self.SRCMODE = RM_Field_LDMA_CH2_CTRL_SRCMODE(self)
        self.zz_fdict['SRCMODE'] = self.SRCMODE
        self.DSTMODE = RM_Field_LDMA_CH2_CTRL_DSTMODE(self)
        self.zz_fdict['DSTMODE'] = self.DSTMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH2_SRC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH2_SRC, self).__init__(rmio, label,
            0x400e2000, 0x0F0,
            'CH2_SRC', 'LDMA.CH2_SRC', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.SRCADDR = RM_Field_LDMA_CH2_SRC_SRCADDR(self)
        self.zz_fdict['SRCADDR'] = self.SRCADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH2_DST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH2_DST, self).__init__(rmio, label,
            0x400e2000, 0x0F4,
            'CH2_DST', 'LDMA.CH2_DST', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DSTADDR = RM_Field_LDMA_CH2_DST_DSTADDR(self)
        self.zz_fdict['DSTADDR'] = self.DSTADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH2_LINK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH2_LINK, self).__init__(rmio, label,
            0x400e2000, 0x0F8,
            'CH2_LINK', 'LDMA.CH2_LINK', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.LINKMODE = RM_Field_LDMA_CH2_LINK_LINKMODE(self)
        self.zz_fdict['LINKMODE'] = self.LINKMODE
        self.LINK = RM_Field_LDMA_CH2_LINK_LINK(self)
        self.zz_fdict['LINK'] = self.LINK
        self.LINKADDR = RM_Field_LDMA_CH2_LINK_LINKADDR(self)
        self.zz_fdict['LINKADDR'] = self.LINKADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH3_REQSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH3_REQSEL, self).__init__(rmio, label,
            0x400e2000, 0x110,
            'CH3_REQSEL', 'LDMA.CH3_REQSEL', 'read-write',
            "",
            0x00000000, 0x003F000F)

        self.SIGSEL = RM_Field_LDMA_CH3_REQSEL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_LDMA_CH3_REQSEL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH3_CFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH3_CFG, self).__init__(rmio, label,
            0x400e2000, 0x114,
            'CH3_CFG', 'LDMA.CH3_CFG', 'read-write',
            "",
            0x00000000, 0x00330000)

        self.ARBSLOTS = RM_Field_LDMA_CH3_CFG_ARBSLOTS(self)
        self.zz_fdict['ARBSLOTS'] = self.ARBSLOTS
        self.SRCINCSIGN = RM_Field_LDMA_CH3_CFG_SRCINCSIGN(self)
        self.zz_fdict['SRCINCSIGN'] = self.SRCINCSIGN
        self.DSTINCSIGN = RM_Field_LDMA_CH3_CFG_DSTINCSIGN(self)
        self.zz_fdict['DSTINCSIGN'] = self.DSTINCSIGN
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH3_LOOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH3_LOOP, self).__init__(rmio, label,
            0x400e2000, 0x118,
            'CH3_LOOP', 'LDMA.CH3_LOOP', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.LOOPCNT = RM_Field_LDMA_CH3_LOOP_LOOPCNT(self)
        self.zz_fdict['LOOPCNT'] = self.LOOPCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH3_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH3_CTRL, self).__init__(rmio, label,
            0x400e2000, 0x11C,
            'CH3_CTRL', 'LDMA.CH3_CTRL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFB)

        self.STRUCTTYPE = RM_Field_LDMA_CH3_CTRL_STRUCTTYPE(self)
        self.zz_fdict['STRUCTTYPE'] = self.STRUCTTYPE
        self.STRUCTREQ = RM_Field_LDMA_CH3_CTRL_STRUCTREQ(self)
        self.zz_fdict['STRUCTREQ'] = self.STRUCTREQ
        self.XFERCNT = RM_Field_LDMA_CH3_CTRL_XFERCNT(self)
        self.zz_fdict['XFERCNT'] = self.XFERCNT
        self.BYTESWAP = RM_Field_LDMA_CH3_CTRL_BYTESWAP(self)
        self.zz_fdict['BYTESWAP'] = self.BYTESWAP
        self.BLOCKSIZE = RM_Field_LDMA_CH3_CTRL_BLOCKSIZE(self)
        self.zz_fdict['BLOCKSIZE'] = self.BLOCKSIZE
        self.DONEIFSEN = RM_Field_LDMA_CH3_CTRL_DONEIFSEN(self)
        self.zz_fdict['DONEIFSEN'] = self.DONEIFSEN
        self.REQMODE = RM_Field_LDMA_CH3_CTRL_REQMODE(self)
        self.zz_fdict['REQMODE'] = self.REQMODE
        self.DECLOOPCNT = RM_Field_LDMA_CH3_CTRL_DECLOOPCNT(self)
        self.zz_fdict['DECLOOPCNT'] = self.DECLOOPCNT
        self.IGNORESREQ = RM_Field_LDMA_CH3_CTRL_IGNORESREQ(self)
        self.zz_fdict['IGNORESREQ'] = self.IGNORESREQ
        self.SRCINC = RM_Field_LDMA_CH3_CTRL_SRCINC(self)
        self.zz_fdict['SRCINC'] = self.SRCINC
        self.SIZE = RM_Field_LDMA_CH3_CTRL_SIZE(self)
        self.zz_fdict['SIZE'] = self.SIZE
        self.DSTINC = RM_Field_LDMA_CH3_CTRL_DSTINC(self)
        self.zz_fdict['DSTINC'] = self.DSTINC
        self.SRCMODE = RM_Field_LDMA_CH3_CTRL_SRCMODE(self)
        self.zz_fdict['SRCMODE'] = self.SRCMODE
        self.DSTMODE = RM_Field_LDMA_CH3_CTRL_DSTMODE(self)
        self.zz_fdict['DSTMODE'] = self.DSTMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH3_SRC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH3_SRC, self).__init__(rmio, label,
            0x400e2000, 0x120,
            'CH3_SRC', 'LDMA.CH3_SRC', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.SRCADDR = RM_Field_LDMA_CH3_SRC_SRCADDR(self)
        self.zz_fdict['SRCADDR'] = self.SRCADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH3_DST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH3_DST, self).__init__(rmio, label,
            0x400e2000, 0x124,
            'CH3_DST', 'LDMA.CH3_DST', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DSTADDR = RM_Field_LDMA_CH3_DST_DSTADDR(self)
        self.zz_fdict['DSTADDR'] = self.DSTADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH3_LINK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH3_LINK, self).__init__(rmio, label,
            0x400e2000, 0x128,
            'CH3_LINK', 'LDMA.CH3_LINK', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.LINKMODE = RM_Field_LDMA_CH3_LINK_LINKMODE(self)
        self.zz_fdict['LINKMODE'] = self.LINKMODE
        self.LINK = RM_Field_LDMA_CH3_LINK_LINK(self)
        self.zz_fdict['LINK'] = self.LINK
        self.LINKADDR = RM_Field_LDMA_CH3_LINK_LINKADDR(self)
        self.zz_fdict['LINKADDR'] = self.LINKADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH4_REQSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH4_REQSEL, self).__init__(rmio, label,
            0x400e2000, 0x140,
            'CH4_REQSEL', 'LDMA.CH4_REQSEL', 'read-write',
            "",
            0x00000000, 0x003F000F)

        self.SIGSEL = RM_Field_LDMA_CH4_REQSEL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_LDMA_CH4_REQSEL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH4_CFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH4_CFG, self).__init__(rmio, label,
            0x400e2000, 0x144,
            'CH4_CFG', 'LDMA.CH4_CFG', 'read-write',
            "",
            0x00000000, 0x00330000)

        self.ARBSLOTS = RM_Field_LDMA_CH4_CFG_ARBSLOTS(self)
        self.zz_fdict['ARBSLOTS'] = self.ARBSLOTS
        self.SRCINCSIGN = RM_Field_LDMA_CH4_CFG_SRCINCSIGN(self)
        self.zz_fdict['SRCINCSIGN'] = self.SRCINCSIGN
        self.DSTINCSIGN = RM_Field_LDMA_CH4_CFG_DSTINCSIGN(self)
        self.zz_fdict['DSTINCSIGN'] = self.DSTINCSIGN
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH4_LOOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH4_LOOP, self).__init__(rmio, label,
            0x400e2000, 0x148,
            'CH4_LOOP', 'LDMA.CH4_LOOP', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.LOOPCNT = RM_Field_LDMA_CH4_LOOP_LOOPCNT(self)
        self.zz_fdict['LOOPCNT'] = self.LOOPCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH4_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH4_CTRL, self).__init__(rmio, label,
            0x400e2000, 0x14C,
            'CH4_CTRL', 'LDMA.CH4_CTRL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFB)

        self.STRUCTTYPE = RM_Field_LDMA_CH4_CTRL_STRUCTTYPE(self)
        self.zz_fdict['STRUCTTYPE'] = self.STRUCTTYPE
        self.STRUCTREQ = RM_Field_LDMA_CH4_CTRL_STRUCTREQ(self)
        self.zz_fdict['STRUCTREQ'] = self.STRUCTREQ
        self.XFERCNT = RM_Field_LDMA_CH4_CTRL_XFERCNT(self)
        self.zz_fdict['XFERCNT'] = self.XFERCNT
        self.BYTESWAP = RM_Field_LDMA_CH4_CTRL_BYTESWAP(self)
        self.zz_fdict['BYTESWAP'] = self.BYTESWAP
        self.BLOCKSIZE = RM_Field_LDMA_CH4_CTRL_BLOCKSIZE(self)
        self.zz_fdict['BLOCKSIZE'] = self.BLOCKSIZE
        self.DONEIFSEN = RM_Field_LDMA_CH4_CTRL_DONEIFSEN(self)
        self.zz_fdict['DONEIFSEN'] = self.DONEIFSEN
        self.REQMODE = RM_Field_LDMA_CH4_CTRL_REQMODE(self)
        self.zz_fdict['REQMODE'] = self.REQMODE
        self.DECLOOPCNT = RM_Field_LDMA_CH4_CTRL_DECLOOPCNT(self)
        self.zz_fdict['DECLOOPCNT'] = self.DECLOOPCNT
        self.IGNORESREQ = RM_Field_LDMA_CH4_CTRL_IGNORESREQ(self)
        self.zz_fdict['IGNORESREQ'] = self.IGNORESREQ
        self.SRCINC = RM_Field_LDMA_CH4_CTRL_SRCINC(self)
        self.zz_fdict['SRCINC'] = self.SRCINC
        self.SIZE = RM_Field_LDMA_CH4_CTRL_SIZE(self)
        self.zz_fdict['SIZE'] = self.SIZE
        self.DSTINC = RM_Field_LDMA_CH4_CTRL_DSTINC(self)
        self.zz_fdict['DSTINC'] = self.DSTINC
        self.SRCMODE = RM_Field_LDMA_CH4_CTRL_SRCMODE(self)
        self.zz_fdict['SRCMODE'] = self.SRCMODE
        self.DSTMODE = RM_Field_LDMA_CH4_CTRL_DSTMODE(self)
        self.zz_fdict['DSTMODE'] = self.DSTMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH4_SRC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH4_SRC, self).__init__(rmio, label,
            0x400e2000, 0x150,
            'CH4_SRC', 'LDMA.CH4_SRC', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.SRCADDR = RM_Field_LDMA_CH4_SRC_SRCADDR(self)
        self.zz_fdict['SRCADDR'] = self.SRCADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH4_DST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH4_DST, self).__init__(rmio, label,
            0x400e2000, 0x154,
            'CH4_DST', 'LDMA.CH4_DST', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DSTADDR = RM_Field_LDMA_CH4_DST_DSTADDR(self)
        self.zz_fdict['DSTADDR'] = self.DSTADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH4_LINK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH4_LINK, self).__init__(rmio, label,
            0x400e2000, 0x158,
            'CH4_LINK', 'LDMA.CH4_LINK', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.LINKMODE = RM_Field_LDMA_CH4_LINK_LINKMODE(self)
        self.zz_fdict['LINKMODE'] = self.LINKMODE
        self.LINK = RM_Field_LDMA_CH4_LINK_LINK(self)
        self.zz_fdict['LINK'] = self.LINK
        self.LINKADDR = RM_Field_LDMA_CH4_LINK_LINKADDR(self)
        self.zz_fdict['LINKADDR'] = self.LINKADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH5_REQSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH5_REQSEL, self).__init__(rmio, label,
            0x400e2000, 0x170,
            'CH5_REQSEL', 'LDMA.CH5_REQSEL', 'read-write',
            "",
            0x00000000, 0x003F000F)

        self.SIGSEL = RM_Field_LDMA_CH5_REQSEL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_LDMA_CH5_REQSEL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH5_CFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH5_CFG, self).__init__(rmio, label,
            0x400e2000, 0x174,
            'CH5_CFG', 'LDMA.CH5_CFG', 'read-write',
            "",
            0x00000000, 0x00330000)

        self.ARBSLOTS = RM_Field_LDMA_CH5_CFG_ARBSLOTS(self)
        self.zz_fdict['ARBSLOTS'] = self.ARBSLOTS
        self.SRCINCSIGN = RM_Field_LDMA_CH5_CFG_SRCINCSIGN(self)
        self.zz_fdict['SRCINCSIGN'] = self.SRCINCSIGN
        self.DSTINCSIGN = RM_Field_LDMA_CH5_CFG_DSTINCSIGN(self)
        self.zz_fdict['DSTINCSIGN'] = self.DSTINCSIGN
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH5_LOOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH5_LOOP, self).__init__(rmio, label,
            0x400e2000, 0x178,
            'CH5_LOOP', 'LDMA.CH5_LOOP', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.LOOPCNT = RM_Field_LDMA_CH5_LOOP_LOOPCNT(self)
        self.zz_fdict['LOOPCNT'] = self.LOOPCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH5_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH5_CTRL, self).__init__(rmio, label,
            0x400e2000, 0x17C,
            'CH5_CTRL', 'LDMA.CH5_CTRL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFB)

        self.STRUCTTYPE = RM_Field_LDMA_CH5_CTRL_STRUCTTYPE(self)
        self.zz_fdict['STRUCTTYPE'] = self.STRUCTTYPE
        self.STRUCTREQ = RM_Field_LDMA_CH5_CTRL_STRUCTREQ(self)
        self.zz_fdict['STRUCTREQ'] = self.STRUCTREQ
        self.XFERCNT = RM_Field_LDMA_CH5_CTRL_XFERCNT(self)
        self.zz_fdict['XFERCNT'] = self.XFERCNT
        self.BYTESWAP = RM_Field_LDMA_CH5_CTRL_BYTESWAP(self)
        self.zz_fdict['BYTESWAP'] = self.BYTESWAP
        self.BLOCKSIZE = RM_Field_LDMA_CH5_CTRL_BLOCKSIZE(self)
        self.zz_fdict['BLOCKSIZE'] = self.BLOCKSIZE
        self.DONEIFSEN = RM_Field_LDMA_CH5_CTRL_DONEIFSEN(self)
        self.zz_fdict['DONEIFSEN'] = self.DONEIFSEN
        self.REQMODE = RM_Field_LDMA_CH5_CTRL_REQMODE(self)
        self.zz_fdict['REQMODE'] = self.REQMODE
        self.DECLOOPCNT = RM_Field_LDMA_CH5_CTRL_DECLOOPCNT(self)
        self.zz_fdict['DECLOOPCNT'] = self.DECLOOPCNT
        self.IGNORESREQ = RM_Field_LDMA_CH5_CTRL_IGNORESREQ(self)
        self.zz_fdict['IGNORESREQ'] = self.IGNORESREQ
        self.SRCINC = RM_Field_LDMA_CH5_CTRL_SRCINC(self)
        self.zz_fdict['SRCINC'] = self.SRCINC
        self.SIZE = RM_Field_LDMA_CH5_CTRL_SIZE(self)
        self.zz_fdict['SIZE'] = self.SIZE
        self.DSTINC = RM_Field_LDMA_CH5_CTRL_DSTINC(self)
        self.zz_fdict['DSTINC'] = self.DSTINC
        self.SRCMODE = RM_Field_LDMA_CH5_CTRL_SRCMODE(self)
        self.zz_fdict['SRCMODE'] = self.SRCMODE
        self.DSTMODE = RM_Field_LDMA_CH5_CTRL_DSTMODE(self)
        self.zz_fdict['DSTMODE'] = self.DSTMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH5_SRC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH5_SRC, self).__init__(rmio, label,
            0x400e2000, 0x180,
            'CH5_SRC', 'LDMA.CH5_SRC', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.SRCADDR = RM_Field_LDMA_CH5_SRC_SRCADDR(self)
        self.zz_fdict['SRCADDR'] = self.SRCADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH5_DST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH5_DST, self).__init__(rmio, label,
            0x400e2000, 0x184,
            'CH5_DST', 'LDMA.CH5_DST', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DSTADDR = RM_Field_LDMA_CH5_DST_DSTADDR(self)
        self.zz_fdict['DSTADDR'] = self.DSTADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH5_LINK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH5_LINK, self).__init__(rmio, label,
            0x400e2000, 0x188,
            'CH5_LINK', 'LDMA.CH5_LINK', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.LINKMODE = RM_Field_LDMA_CH5_LINK_LINKMODE(self)
        self.zz_fdict['LINKMODE'] = self.LINKMODE
        self.LINK = RM_Field_LDMA_CH5_LINK_LINK(self)
        self.zz_fdict['LINK'] = self.LINK
        self.LINKADDR = RM_Field_LDMA_CH5_LINK_LINKADDR(self)
        self.zz_fdict['LINKADDR'] = self.LINKADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH6_REQSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH6_REQSEL, self).__init__(rmio, label,
            0x400e2000, 0x1A0,
            'CH6_REQSEL', 'LDMA.CH6_REQSEL', 'read-write',
            "",
            0x00000000, 0x003F000F)

        self.SIGSEL = RM_Field_LDMA_CH6_REQSEL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_LDMA_CH6_REQSEL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH6_CFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH6_CFG, self).__init__(rmio, label,
            0x400e2000, 0x1A4,
            'CH6_CFG', 'LDMA.CH6_CFG', 'read-write',
            "",
            0x00000000, 0x00330000)

        self.ARBSLOTS = RM_Field_LDMA_CH6_CFG_ARBSLOTS(self)
        self.zz_fdict['ARBSLOTS'] = self.ARBSLOTS
        self.SRCINCSIGN = RM_Field_LDMA_CH6_CFG_SRCINCSIGN(self)
        self.zz_fdict['SRCINCSIGN'] = self.SRCINCSIGN
        self.DSTINCSIGN = RM_Field_LDMA_CH6_CFG_DSTINCSIGN(self)
        self.zz_fdict['DSTINCSIGN'] = self.DSTINCSIGN
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH6_LOOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH6_LOOP, self).__init__(rmio, label,
            0x400e2000, 0x1A8,
            'CH6_LOOP', 'LDMA.CH6_LOOP', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.LOOPCNT = RM_Field_LDMA_CH6_LOOP_LOOPCNT(self)
        self.zz_fdict['LOOPCNT'] = self.LOOPCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH6_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH6_CTRL, self).__init__(rmio, label,
            0x400e2000, 0x1AC,
            'CH6_CTRL', 'LDMA.CH6_CTRL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFB)

        self.STRUCTTYPE = RM_Field_LDMA_CH6_CTRL_STRUCTTYPE(self)
        self.zz_fdict['STRUCTTYPE'] = self.STRUCTTYPE
        self.STRUCTREQ = RM_Field_LDMA_CH6_CTRL_STRUCTREQ(self)
        self.zz_fdict['STRUCTREQ'] = self.STRUCTREQ
        self.XFERCNT = RM_Field_LDMA_CH6_CTRL_XFERCNT(self)
        self.zz_fdict['XFERCNT'] = self.XFERCNT
        self.BYTESWAP = RM_Field_LDMA_CH6_CTRL_BYTESWAP(self)
        self.zz_fdict['BYTESWAP'] = self.BYTESWAP
        self.BLOCKSIZE = RM_Field_LDMA_CH6_CTRL_BLOCKSIZE(self)
        self.zz_fdict['BLOCKSIZE'] = self.BLOCKSIZE
        self.DONEIFSEN = RM_Field_LDMA_CH6_CTRL_DONEIFSEN(self)
        self.zz_fdict['DONEIFSEN'] = self.DONEIFSEN
        self.REQMODE = RM_Field_LDMA_CH6_CTRL_REQMODE(self)
        self.zz_fdict['REQMODE'] = self.REQMODE
        self.DECLOOPCNT = RM_Field_LDMA_CH6_CTRL_DECLOOPCNT(self)
        self.zz_fdict['DECLOOPCNT'] = self.DECLOOPCNT
        self.IGNORESREQ = RM_Field_LDMA_CH6_CTRL_IGNORESREQ(self)
        self.zz_fdict['IGNORESREQ'] = self.IGNORESREQ
        self.SRCINC = RM_Field_LDMA_CH6_CTRL_SRCINC(self)
        self.zz_fdict['SRCINC'] = self.SRCINC
        self.SIZE = RM_Field_LDMA_CH6_CTRL_SIZE(self)
        self.zz_fdict['SIZE'] = self.SIZE
        self.DSTINC = RM_Field_LDMA_CH6_CTRL_DSTINC(self)
        self.zz_fdict['DSTINC'] = self.DSTINC
        self.SRCMODE = RM_Field_LDMA_CH6_CTRL_SRCMODE(self)
        self.zz_fdict['SRCMODE'] = self.SRCMODE
        self.DSTMODE = RM_Field_LDMA_CH6_CTRL_DSTMODE(self)
        self.zz_fdict['DSTMODE'] = self.DSTMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH6_SRC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH6_SRC, self).__init__(rmio, label,
            0x400e2000, 0x1B0,
            'CH6_SRC', 'LDMA.CH6_SRC', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.SRCADDR = RM_Field_LDMA_CH6_SRC_SRCADDR(self)
        self.zz_fdict['SRCADDR'] = self.SRCADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH6_DST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH6_DST, self).__init__(rmio, label,
            0x400e2000, 0x1B4,
            'CH6_DST', 'LDMA.CH6_DST', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DSTADDR = RM_Field_LDMA_CH6_DST_DSTADDR(self)
        self.zz_fdict['DSTADDR'] = self.DSTADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH6_LINK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH6_LINK, self).__init__(rmio, label,
            0x400e2000, 0x1B8,
            'CH6_LINK', 'LDMA.CH6_LINK', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.LINKMODE = RM_Field_LDMA_CH6_LINK_LINKMODE(self)
        self.zz_fdict['LINKMODE'] = self.LINKMODE
        self.LINK = RM_Field_LDMA_CH6_LINK_LINK(self)
        self.zz_fdict['LINK'] = self.LINK
        self.LINKADDR = RM_Field_LDMA_CH6_LINK_LINKADDR(self)
        self.zz_fdict['LINKADDR'] = self.LINKADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH7_REQSEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH7_REQSEL, self).__init__(rmio, label,
            0x400e2000, 0x1D0,
            'CH7_REQSEL', 'LDMA.CH7_REQSEL', 'read-write',
            "",
            0x00000000, 0x003F000F)

        self.SIGSEL = RM_Field_LDMA_CH7_REQSEL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_LDMA_CH7_REQSEL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH7_CFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH7_CFG, self).__init__(rmio, label,
            0x400e2000, 0x1D4,
            'CH7_CFG', 'LDMA.CH7_CFG', 'read-write',
            "",
            0x00000000, 0x00330000)

        self.ARBSLOTS = RM_Field_LDMA_CH7_CFG_ARBSLOTS(self)
        self.zz_fdict['ARBSLOTS'] = self.ARBSLOTS
        self.SRCINCSIGN = RM_Field_LDMA_CH7_CFG_SRCINCSIGN(self)
        self.zz_fdict['SRCINCSIGN'] = self.SRCINCSIGN
        self.DSTINCSIGN = RM_Field_LDMA_CH7_CFG_DSTINCSIGN(self)
        self.zz_fdict['DSTINCSIGN'] = self.DSTINCSIGN
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH7_LOOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH7_LOOP, self).__init__(rmio, label,
            0x400e2000, 0x1D8,
            'CH7_LOOP', 'LDMA.CH7_LOOP', 'read-write',
            "",
            0x00000000, 0x000000FF)

        self.LOOPCNT = RM_Field_LDMA_CH7_LOOP_LOOPCNT(self)
        self.zz_fdict['LOOPCNT'] = self.LOOPCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH7_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH7_CTRL, self).__init__(rmio, label,
            0x400e2000, 0x1DC,
            'CH7_CTRL', 'LDMA.CH7_CTRL', 'read-write',
            "",
            0x00000000, 0xFFFFFFFB)

        self.STRUCTTYPE = RM_Field_LDMA_CH7_CTRL_STRUCTTYPE(self)
        self.zz_fdict['STRUCTTYPE'] = self.STRUCTTYPE
        self.STRUCTREQ = RM_Field_LDMA_CH7_CTRL_STRUCTREQ(self)
        self.zz_fdict['STRUCTREQ'] = self.STRUCTREQ
        self.XFERCNT = RM_Field_LDMA_CH7_CTRL_XFERCNT(self)
        self.zz_fdict['XFERCNT'] = self.XFERCNT
        self.BYTESWAP = RM_Field_LDMA_CH7_CTRL_BYTESWAP(self)
        self.zz_fdict['BYTESWAP'] = self.BYTESWAP
        self.BLOCKSIZE = RM_Field_LDMA_CH7_CTRL_BLOCKSIZE(self)
        self.zz_fdict['BLOCKSIZE'] = self.BLOCKSIZE
        self.DONEIFSEN = RM_Field_LDMA_CH7_CTRL_DONEIFSEN(self)
        self.zz_fdict['DONEIFSEN'] = self.DONEIFSEN
        self.REQMODE = RM_Field_LDMA_CH7_CTRL_REQMODE(self)
        self.zz_fdict['REQMODE'] = self.REQMODE
        self.DECLOOPCNT = RM_Field_LDMA_CH7_CTRL_DECLOOPCNT(self)
        self.zz_fdict['DECLOOPCNT'] = self.DECLOOPCNT
        self.IGNORESREQ = RM_Field_LDMA_CH7_CTRL_IGNORESREQ(self)
        self.zz_fdict['IGNORESREQ'] = self.IGNORESREQ
        self.SRCINC = RM_Field_LDMA_CH7_CTRL_SRCINC(self)
        self.zz_fdict['SRCINC'] = self.SRCINC
        self.SIZE = RM_Field_LDMA_CH7_CTRL_SIZE(self)
        self.zz_fdict['SIZE'] = self.SIZE
        self.DSTINC = RM_Field_LDMA_CH7_CTRL_DSTINC(self)
        self.zz_fdict['DSTINC'] = self.DSTINC
        self.SRCMODE = RM_Field_LDMA_CH7_CTRL_SRCMODE(self)
        self.zz_fdict['SRCMODE'] = self.SRCMODE
        self.DSTMODE = RM_Field_LDMA_CH7_CTRL_DSTMODE(self)
        self.zz_fdict['DSTMODE'] = self.DSTMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH7_SRC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH7_SRC, self).__init__(rmio, label,
            0x400e2000, 0x1E0,
            'CH7_SRC', 'LDMA.CH7_SRC', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.SRCADDR = RM_Field_LDMA_CH7_SRC_SRCADDR(self)
        self.zz_fdict['SRCADDR'] = self.SRCADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH7_DST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH7_DST, self).__init__(rmio, label,
            0x400e2000, 0x1E4,
            'CH7_DST', 'LDMA.CH7_DST', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.DSTADDR = RM_Field_LDMA_CH7_DST_DSTADDR(self)
        self.zz_fdict['DSTADDR'] = self.DSTADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_LDMA_CH7_LINK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_LDMA_CH7_LINK, self).__init__(rmio, label,
            0x400e2000, 0x1E8,
            'CH7_LINK', 'LDMA.CH7_LINK', 'read-write',
            "",
            0x00000000, 0xFFFFFFFF)

        self.LINKMODE = RM_Field_LDMA_CH7_LINK_LINKMODE(self)
        self.zz_fdict['LINKMODE'] = self.LINKMODE
        self.LINK = RM_Field_LDMA_CH7_LINK_LINK(self)
        self.zz_fdict['LINK'] = self.LINK
        self.LINKADDR = RM_Field_LDMA_CH7_LINK_LINKADDR(self)
        self.zz_fdict['LINKADDR'] = self.LINKADDR
        self.__dict__['zz_frozen'] = True


