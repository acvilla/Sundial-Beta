
from static import Base_RM_Field
from LDMA_enum import *


class RM_Field_LDMA_CTRL_SYNCPRSSETEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CTRL_SYNCPRSSETEN, self).__init__(register,
            'SYNCPRSSETEN', 'LDMA.CTRL.SYNCPRSSETEN', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CTRL_SYNCPRSCLREN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CTRL_SYNCPRSCLREN, self).__init__(register,
            'SYNCPRSCLREN', 'LDMA.CTRL.SYNCPRSCLREN', 'read-write',
            "",
            8, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CTRL_NUMFIXED(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CTRL_NUMFIXED, self).__init__(register,
            'NUMFIXED', 'LDMA.CTRL.NUMFIXED', 'read-write',
            "",
            24, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CTRL_RESET(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CTRL_RESET, self).__init__(register,
            'RESET', 'LDMA.CTRL.RESET', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_STATUS_ANYBUSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_STATUS_ANYBUSY, self).__init__(register,
            'ANYBUSY', 'LDMA.STATUS.ANYBUSY', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_STATUS_ANYREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_STATUS_ANYREQ, self).__init__(register,
            'ANYREQ', 'LDMA.STATUS.ANYREQ', 'read-only',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_STATUS_CHGRANT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_STATUS_CHGRANT, self).__init__(register,
            'CHGRANT', 'LDMA.STATUS.CHGRANT', 'read-only',
            "",
            3, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_STATUS_CHERROR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_STATUS_CHERROR, self).__init__(register,
            'CHERROR', 'LDMA.STATUS.CHERROR', 'read-only',
            "",
            8, 3)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_STATUS_FIFOLEVEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_STATUS_FIFOLEVEL, self).__init__(register,
            'FIFOLEVEL', 'LDMA.STATUS.FIFOLEVEL', 'read-only',
            "",
            16, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_STATUS_CHNUM(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_STATUS_CHNUM, self).__init__(register,
            'CHNUM', 'LDMA.STATUS.CHNUM', 'read-only',
            "",
            24, 5)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_SYNC_SYNCTRIG(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_SYNC_SYNCTRIG, self).__init__(register,
            'SYNCTRIG', 'LDMA.SYNC.SYNCTRIG', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CHEN_CHEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CHEN_CHEN, self).__init__(register,
            'CHEN', 'LDMA.CHEN.CHEN', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CHBUSY_BUSY(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CHBUSY_BUSY, self).__init__(register,
            'BUSY', 'LDMA.CHBUSY.BUSY', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CHDONE_CHDONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CHDONE_CHDONE, self).__init__(register,
            'CHDONE', 'LDMA.CHDONE.CHDONE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_DBGHALT_DBGHALT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_DBGHALT_DBGHALT, self).__init__(register,
            'DBGHALT', 'LDMA.DBGHALT.DBGHALT', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_SWREQ_SWREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_SWREQ_SWREQ, self).__init__(register,
            'SWREQ', 'LDMA.SWREQ.SWREQ', 'write-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_REQDIS_REQDIS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_REQDIS_REQDIS, self).__init__(register,
            'REQDIS', 'LDMA.REQDIS.REQDIS', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_REQPEND_REQPEND(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_REQPEND_REQPEND, self).__init__(register,
            'REQPEND', 'LDMA.REQPEND.REQPEND', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_LINKLOAD_LINKLOAD(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_LINKLOAD_LINKLOAD, self).__init__(register,
            'LINKLOAD', 'LDMA.LINKLOAD.LINKLOAD', 'write-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_REQCLEAR_REQCLEAR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_REQCLEAR_REQCLEAR, self).__init__(register,
            'REQCLEAR', 'LDMA.REQCLEAR.REQCLEAR', 'write-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_IF_DONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_IF_DONE, self).__init__(register,
            'DONE', 'LDMA.IF.DONE', 'read-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_IF_ERROR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_IF_ERROR, self).__init__(register,
            'ERROR', 'LDMA.IF.ERROR', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_IFS_DONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_IFS_DONE, self).__init__(register,
            'DONE', 'LDMA.IFS.DONE', 'write-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_IFS_ERROR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_IFS_ERROR, self).__init__(register,
            'ERROR', 'LDMA.IFS.ERROR', 'write-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_IFC_DONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_IFC_DONE, self).__init__(register,
            'DONE', 'LDMA.IFC.DONE', 'write-only',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_IFC_ERROR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_IFC_ERROR, self).__init__(register,
            'ERROR', 'LDMA.IFC.ERROR', 'write-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_IEN_DONE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_IEN_DONE, self).__init__(register,
            'DONE', 'LDMA.IEN.DONE', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_IEN_ERROR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_IEN_ERROR, self).__init__(register,
            'ERROR', 'LDMA.IEN.ERROR', 'read-write',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_REQSEL_SIGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_REQSEL_SIGSEL, self).__init__(register,
            'SIGSEL', 'LDMA.CH0_REQSEL.SIGSEL', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_REQSEL_SOURCESEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_REQSEL_SOURCESEL, self).__init__(register,
            'SOURCESEL', 'LDMA.CH0_REQSEL.SOURCESEL', 'read-write',
            "",
            16, 6,
            RM_Enum_LDMA_CH0_REQSEL_SOURCESEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CFG_ARBSLOTS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CFG_ARBSLOTS, self).__init__(register,
            'ARBSLOTS', 'LDMA.CH0_CFG.ARBSLOTS', 'read-write',
            "",
            16, 2,
            RM_Enum_LDMA_CH0_CFG_ARBSLOTS(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CFG_SRCINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CFG_SRCINCSIGN, self).__init__(register,
            'SRCINCSIGN', 'LDMA.CH0_CFG.SRCINCSIGN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CFG_DSTINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CFG_DSTINCSIGN, self).__init__(register,
            'DSTINCSIGN', 'LDMA.CH0_CFG.DSTINCSIGN', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_LOOP_LOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_LOOP_LOOPCNT, self).__init__(register,
            'LOOPCNT', 'LDMA.CH0_LOOP.LOOPCNT', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CTRL_STRUCTTYPE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CTRL_STRUCTTYPE, self).__init__(register,
            'STRUCTTYPE', 'LDMA.CH0_CTRL.STRUCTTYPE', 'read-only',
            "",
            0, 2,
            RM_Enum_LDMA_CH0_CTRL_STRUCTTYPE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CTRL_STRUCTREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CTRL_STRUCTREQ, self).__init__(register,
            'STRUCTREQ', 'LDMA.CH0_CTRL.STRUCTREQ', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CTRL_XFERCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CTRL_XFERCNT, self).__init__(register,
            'XFERCNT', 'LDMA.CH0_CTRL.XFERCNT', 'read-write',
            "",
            4, 11)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CTRL_BYTESWAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CTRL_BYTESWAP, self).__init__(register,
            'BYTESWAP', 'LDMA.CH0_CTRL.BYTESWAP', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CTRL_BLOCKSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CTRL_BLOCKSIZE, self).__init__(register,
            'BLOCKSIZE', 'LDMA.CH0_CTRL.BLOCKSIZE', 'read-write',
            "",
            16, 4,
            RM_Enum_LDMA_CH0_CTRL_BLOCKSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CTRL_DONEIFSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CTRL_DONEIFSEN, self).__init__(register,
            'DONEIFSEN', 'LDMA.CH0_CTRL.DONEIFSEN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CTRL_REQMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CTRL_REQMODE, self).__init__(register,
            'REQMODE', 'LDMA.CH0_CTRL.REQMODE', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CTRL_DECLOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CTRL_DECLOOPCNT, self).__init__(register,
            'DECLOOPCNT', 'LDMA.CH0_CTRL.DECLOOPCNT', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CTRL_IGNORESREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CTRL_IGNORESREQ, self).__init__(register,
            'IGNORESREQ', 'LDMA.CH0_CTRL.IGNORESREQ', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CTRL_SRCINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CTRL_SRCINC, self).__init__(register,
            'SRCINC', 'LDMA.CH0_CTRL.SRCINC', 'read-write',
            "",
            24, 2,
            RM_Enum_LDMA_CH0_CTRL_SRCINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CTRL_SIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CTRL_SIZE, self).__init__(register,
            'SIZE', 'LDMA.CH0_CTRL.SIZE', 'read-write',
            "",
            26, 2,
            RM_Enum_LDMA_CH0_CTRL_SIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CTRL_DSTINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CTRL_DSTINC, self).__init__(register,
            'DSTINC', 'LDMA.CH0_CTRL.DSTINC', 'read-write',
            "",
            28, 2,
            RM_Enum_LDMA_CH0_CTRL_DSTINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CTRL_SRCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CTRL_SRCMODE, self).__init__(register,
            'SRCMODE', 'LDMA.CH0_CTRL.SRCMODE', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_CTRL_DSTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_CTRL_DSTMODE, self).__init__(register,
            'DSTMODE', 'LDMA.CH0_CTRL.DSTMODE', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_SRC_SRCADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_SRC_SRCADDR, self).__init__(register,
            'SRCADDR', 'LDMA.CH0_SRC.SRCADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_DST_DSTADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_DST_DSTADDR, self).__init__(register,
            'DSTADDR', 'LDMA.CH0_DST.DSTADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_LINK_LINKMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_LINK_LINKMODE, self).__init__(register,
            'LINKMODE', 'LDMA.CH0_LINK.LINKMODE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_LINK_LINK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_LINK_LINK, self).__init__(register,
            'LINK', 'LDMA.CH0_LINK.LINK', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH0_LINK_LINKADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH0_LINK_LINKADDR, self).__init__(register,
            'LINKADDR', 'LDMA.CH0_LINK.LINKADDR', 'read-write',
            "",
            2, 30)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_REQSEL_SIGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_REQSEL_SIGSEL, self).__init__(register,
            'SIGSEL', 'LDMA.CH1_REQSEL.SIGSEL', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_REQSEL_SOURCESEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_REQSEL_SOURCESEL, self).__init__(register,
            'SOURCESEL', 'LDMA.CH1_REQSEL.SOURCESEL', 'read-write',
            "",
            16, 6,
            RM_Enum_LDMA_CH1_REQSEL_SOURCESEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CFG_ARBSLOTS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CFG_ARBSLOTS, self).__init__(register,
            'ARBSLOTS', 'LDMA.CH1_CFG.ARBSLOTS', 'read-write',
            "",
            16, 2,
            RM_Enum_LDMA_CH1_CFG_ARBSLOTS(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CFG_SRCINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CFG_SRCINCSIGN, self).__init__(register,
            'SRCINCSIGN', 'LDMA.CH1_CFG.SRCINCSIGN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CFG_DSTINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CFG_DSTINCSIGN, self).__init__(register,
            'DSTINCSIGN', 'LDMA.CH1_CFG.DSTINCSIGN', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_LOOP_LOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_LOOP_LOOPCNT, self).__init__(register,
            'LOOPCNT', 'LDMA.CH1_LOOP.LOOPCNT', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CTRL_STRUCTTYPE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CTRL_STRUCTTYPE, self).__init__(register,
            'STRUCTTYPE', 'LDMA.CH1_CTRL.STRUCTTYPE', 'read-only',
            "",
            0, 2,
            RM_Enum_LDMA_CH1_CTRL_STRUCTTYPE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CTRL_STRUCTREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CTRL_STRUCTREQ, self).__init__(register,
            'STRUCTREQ', 'LDMA.CH1_CTRL.STRUCTREQ', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CTRL_XFERCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CTRL_XFERCNT, self).__init__(register,
            'XFERCNT', 'LDMA.CH1_CTRL.XFERCNT', 'read-write',
            "",
            4, 11)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CTRL_BYTESWAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CTRL_BYTESWAP, self).__init__(register,
            'BYTESWAP', 'LDMA.CH1_CTRL.BYTESWAP', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CTRL_BLOCKSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CTRL_BLOCKSIZE, self).__init__(register,
            'BLOCKSIZE', 'LDMA.CH1_CTRL.BLOCKSIZE', 'read-write',
            "",
            16, 4,
            RM_Enum_LDMA_CH1_CTRL_BLOCKSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CTRL_DONEIFSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CTRL_DONEIFSEN, self).__init__(register,
            'DONEIFSEN', 'LDMA.CH1_CTRL.DONEIFSEN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CTRL_REQMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CTRL_REQMODE, self).__init__(register,
            'REQMODE', 'LDMA.CH1_CTRL.REQMODE', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CTRL_DECLOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CTRL_DECLOOPCNT, self).__init__(register,
            'DECLOOPCNT', 'LDMA.CH1_CTRL.DECLOOPCNT', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CTRL_IGNORESREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CTRL_IGNORESREQ, self).__init__(register,
            'IGNORESREQ', 'LDMA.CH1_CTRL.IGNORESREQ', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CTRL_SRCINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CTRL_SRCINC, self).__init__(register,
            'SRCINC', 'LDMA.CH1_CTRL.SRCINC', 'read-write',
            "",
            24, 2,
            RM_Enum_LDMA_CH1_CTRL_SRCINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CTRL_SIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CTRL_SIZE, self).__init__(register,
            'SIZE', 'LDMA.CH1_CTRL.SIZE', 'read-write',
            "",
            26, 2,
            RM_Enum_LDMA_CH1_CTRL_SIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CTRL_DSTINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CTRL_DSTINC, self).__init__(register,
            'DSTINC', 'LDMA.CH1_CTRL.DSTINC', 'read-write',
            "",
            28, 2,
            RM_Enum_LDMA_CH1_CTRL_DSTINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CTRL_SRCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CTRL_SRCMODE, self).__init__(register,
            'SRCMODE', 'LDMA.CH1_CTRL.SRCMODE', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_CTRL_DSTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_CTRL_DSTMODE, self).__init__(register,
            'DSTMODE', 'LDMA.CH1_CTRL.DSTMODE', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_SRC_SRCADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_SRC_SRCADDR, self).__init__(register,
            'SRCADDR', 'LDMA.CH1_SRC.SRCADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_DST_DSTADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_DST_DSTADDR, self).__init__(register,
            'DSTADDR', 'LDMA.CH1_DST.DSTADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_LINK_LINKMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_LINK_LINKMODE, self).__init__(register,
            'LINKMODE', 'LDMA.CH1_LINK.LINKMODE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_LINK_LINK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_LINK_LINK, self).__init__(register,
            'LINK', 'LDMA.CH1_LINK.LINK', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH1_LINK_LINKADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH1_LINK_LINKADDR, self).__init__(register,
            'LINKADDR', 'LDMA.CH1_LINK.LINKADDR', 'read-write',
            "",
            2, 30)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_REQSEL_SIGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_REQSEL_SIGSEL, self).__init__(register,
            'SIGSEL', 'LDMA.CH2_REQSEL.SIGSEL', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_REQSEL_SOURCESEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_REQSEL_SOURCESEL, self).__init__(register,
            'SOURCESEL', 'LDMA.CH2_REQSEL.SOURCESEL', 'read-write',
            "",
            16, 6,
            RM_Enum_LDMA_CH2_REQSEL_SOURCESEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CFG_ARBSLOTS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CFG_ARBSLOTS, self).__init__(register,
            'ARBSLOTS', 'LDMA.CH2_CFG.ARBSLOTS', 'read-write',
            "",
            16, 2,
            RM_Enum_LDMA_CH2_CFG_ARBSLOTS(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CFG_SRCINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CFG_SRCINCSIGN, self).__init__(register,
            'SRCINCSIGN', 'LDMA.CH2_CFG.SRCINCSIGN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CFG_DSTINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CFG_DSTINCSIGN, self).__init__(register,
            'DSTINCSIGN', 'LDMA.CH2_CFG.DSTINCSIGN', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_LOOP_LOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_LOOP_LOOPCNT, self).__init__(register,
            'LOOPCNT', 'LDMA.CH2_LOOP.LOOPCNT', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CTRL_STRUCTTYPE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CTRL_STRUCTTYPE, self).__init__(register,
            'STRUCTTYPE', 'LDMA.CH2_CTRL.STRUCTTYPE', 'read-only',
            "",
            0, 2,
            RM_Enum_LDMA_CH2_CTRL_STRUCTTYPE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CTRL_STRUCTREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CTRL_STRUCTREQ, self).__init__(register,
            'STRUCTREQ', 'LDMA.CH2_CTRL.STRUCTREQ', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CTRL_XFERCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CTRL_XFERCNT, self).__init__(register,
            'XFERCNT', 'LDMA.CH2_CTRL.XFERCNT', 'read-write',
            "",
            4, 11)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CTRL_BYTESWAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CTRL_BYTESWAP, self).__init__(register,
            'BYTESWAP', 'LDMA.CH2_CTRL.BYTESWAP', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CTRL_BLOCKSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CTRL_BLOCKSIZE, self).__init__(register,
            'BLOCKSIZE', 'LDMA.CH2_CTRL.BLOCKSIZE', 'read-write',
            "",
            16, 4,
            RM_Enum_LDMA_CH2_CTRL_BLOCKSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CTRL_DONEIFSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CTRL_DONEIFSEN, self).__init__(register,
            'DONEIFSEN', 'LDMA.CH2_CTRL.DONEIFSEN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CTRL_REQMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CTRL_REQMODE, self).__init__(register,
            'REQMODE', 'LDMA.CH2_CTRL.REQMODE', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CTRL_DECLOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CTRL_DECLOOPCNT, self).__init__(register,
            'DECLOOPCNT', 'LDMA.CH2_CTRL.DECLOOPCNT', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CTRL_IGNORESREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CTRL_IGNORESREQ, self).__init__(register,
            'IGNORESREQ', 'LDMA.CH2_CTRL.IGNORESREQ', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CTRL_SRCINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CTRL_SRCINC, self).__init__(register,
            'SRCINC', 'LDMA.CH2_CTRL.SRCINC', 'read-write',
            "",
            24, 2,
            RM_Enum_LDMA_CH2_CTRL_SRCINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CTRL_SIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CTRL_SIZE, self).__init__(register,
            'SIZE', 'LDMA.CH2_CTRL.SIZE', 'read-write',
            "",
            26, 2,
            RM_Enum_LDMA_CH2_CTRL_SIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CTRL_DSTINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CTRL_DSTINC, self).__init__(register,
            'DSTINC', 'LDMA.CH2_CTRL.DSTINC', 'read-write',
            "",
            28, 2,
            RM_Enum_LDMA_CH2_CTRL_DSTINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CTRL_SRCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CTRL_SRCMODE, self).__init__(register,
            'SRCMODE', 'LDMA.CH2_CTRL.SRCMODE', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_CTRL_DSTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_CTRL_DSTMODE, self).__init__(register,
            'DSTMODE', 'LDMA.CH2_CTRL.DSTMODE', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_SRC_SRCADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_SRC_SRCADDR, self).__init__(register,
            'SRCADDR', 'LDMA.CH2_SRC.SRCADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_DST_DSTADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_DST_DSTADDR, self).__init__(register,
            'DSTADDR', 'LDMA.CH2_DST.DSTADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_LINK_LINKMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_LINK_LINKMODE, self).__init__(register,
            'LINKMODE', 'LDMA.CH2_LINK.LINKMODE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_LINK_LINK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_LINK_LINK, self).__init__(register,
            'LINK', 'LDMA.CH2_LINK.LINK', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH2_LINK_LINKADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH2_LINK_LINKADDR, self).__init__(register,
            'LINKADDR', 'LDMA.CH2_LINK.LINKADDR', 'read-write',
            "",
            2, 30)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_REQSEL_SIGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_REQSEL_SIGSEL, self).__init__(register,
            'SIGSEL', 'LDMA.CH3_REQSEL.SIGSEL', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_REQSEL_SOURCESEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_REQSEL_SOURCESEL, self).__init__(register,
            'SOURCESEL', 'LDMA.CH3_REQSEL.SOURCESEL', 'read-write',
            "",
            16, 6,
            RM_Enum_LDMA_CH3_REQSEL_SOURCESEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CFG_ARBSLOTS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CFG_ARBSLOTS, self).__init__(register,
            'ARBSLOTS', 'LDMA.CH3_CFG.ARBSLOTS', 'read-write',
            "",
            16, 2,
            RM_Enum_LDMA_CH3_CFG_ARBSLOTS(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CFG_SRCINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CFG_SRCINCSIGN, self).__init__(register,
            'SRCINCSIGN', 'LDMA.CH3_CFG.SRCINCSIGN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CFG_DSTINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CFG_DSTINCSIGN, self).__init__(register,
            'DSTINCSIGN', 'LDMA.CH3_CFG.DSTINCSIGN', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_LOOP_LOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_LOOP_LOOPCNT, self).__init__(register,
            'LOOPCNT', 'LDMA.CH3_LOOP.LOOPCNT', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CTRL_STRUCTTYPE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CTRL_STRUCTTYPE, self).__init__(register,
            'STRUCTTYPE', 'LDMA.CH3_CTRL.STRUCTTYPE', 'read-only',
            "",
            0, 2,
            RM_Enum_LDMA_CH3_CTRL_STRUCTTYPE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CTRL_STRUCTREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CTRL_STRUCTREQ, self).__init__(register,
            'STRUCTREQ', 'LDMA.CH3_CTRL.STRUCTREQ', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CTRL_XFERCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CTRL_XFERCNT, self).__init__(register,
            'XFERCNT', 'LDMA.CH3_CTRL.XFERCNT', 'read-write',
            "",
            4, 11)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CTRL_BYTESWAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CTRL_BYTESWAP, self).__init__(register,
            'BYTESWAP', 'LDMA.CH3_CTRL.BYTESWAP', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CTRL_BLOCKSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CTRL_BLOCKSIZE, self).__init__(register,
            'BLOCKSIZE', 'LDMA.CH3_CTRL.BLOCKSIZE', 'read-write',
            "",
            16, 4,
            RM_Enum_LDMA_CH3_CTRL_BLOCKSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CTRL_DONEIFSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CTRL_DONEIFSEN, self).__init__(register,
            'DONEIFSEN', 'LDMA.CH3_CTRL.DONEIFSEN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CTRL_REQMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CTRL_REQMODE, self).__init__(register,
            'REQMODE', 'LDMA.CH3_CTRL.REQMODE', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CTRL_DECLOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CTRL_DECLOOPCNT, self).__init__(register,
            'DECLOOPCNT', 'LDMA.CH3_CTRL.DECLOOPCNT', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CTRL_IGNORESREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CTRL_IGNORESREQ, self).__init__(register,
            'IGNORESREQ', 'LDMA.CH3_CTRL.IGNORESREQ', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CTRL_SRCINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CTRL_SRCINC, self).__init__(register,
            'SRCINC', 'LDMA.CH3_CTRL.SRCINC', 'read-write',
            "",
            24, 2,
            RM_Enum_LDMA_CH3_CTRL_SRCINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CTRL_SIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CTRL_SIZE, self).__init__(register,
            'SIZE', 'LDMA.CH3_CTRL.SIZE', 'read-write',
            "",
            26, 2,
            RM_Enum_LDMA_CH3_CTRL_SIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CTRL_DSTINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CTRL_DSTINC, self).__init__(register,
            'DSTINC', 'LDMA.CH3_CTRL.DSTINC', 'read-write',
            "",
            28, 2,
            RM_Enum_LDMA_CH3_CTRL_DSTINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CTRL_SRCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CTRL_SRCMODE, self).__init__(register,
            'SRCMODE', 'LDMA.CH3_CTRL.SRCMODE', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_CTRL_DSTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_CTRL_DSTMODE, self).__init__(register,
            'DSTMODE', 'LDMA.CH3_CTRL.DSTMODE', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_SRC_SRCADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_SRC_SRCADDR, self).__init__(register,
            'SRCADDR', 'LDMA.CH3_SRC.SRCADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_DST_DSTADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_DST_DSTADDR, self).__init__(register,
            'DSTADDR', 'LDMA.CH3_DST.DSTADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_LINK_LINKMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_LINK_LINKMODE, self).__init__(register,
            'LINKMODE', 'LDMA.CH3_LINK.LINKMODE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_LINK_LINK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_LINK_LINK, self).__init__(register,
            'LINK', 'LDMA.CH3_LINK.LINK', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH3_LINK_LINKADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH3_LINK_LINKADDR, self).__init__(register,
            'LINKADDR', 'LDMA.CH3_LINK.LINKADDR', 'read-write',
            "",
            2, 30)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_REQSEL_SIGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_REQSEL_SIGSEL, self).__init__(register,
            'SIGSEL', 'LDMA.CH4_REQSEL.SIGSEL', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_REQSEL_SOURCESEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_REQSEL_SOURCESEL, self).__init__(register,
            'SOURCESEL', 'LDMA.CH4_REQSEL.SOURCESEL', 'read-write',
            "",
            16, 6,
            RM_Enum_LDMA_CH4_REQSEL_SOURCESEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CFG_ARBSLOTS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CFG_ARBSLOTS, self).__init__(register,
            'ARBSLOTS', 'LDMA.CH4_CFG.ARBSLOTS', 'read-write',
            "",
            16, 2,
            RM_Enum_LDMA_CH4_CFG_ARBSLOTS(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CFG_SRCINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CFG_SRCINCSIGN, self).__init__(register,
            'SRCINCSIGN', 'LDMA.CH4_CFG.SRCINCSIGN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CFG_DSTINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CFG_DSTINCSIGN, self).__init__(register,
            'DSTINCSIGN', 'LDMA.CH4_CFG.DSTINCSIGN', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_LOOP_LOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_LOOP_LOOPCNT, self).__init__(register,
            'LOOPCNT', 'LDMA.CH4_LOOP.LOOPCNT', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CTRL_STRUCTTYPE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CTRL_STRUCTTYPE, self).__init__(register,
            'STRUCTTYPE', 'LDMA.CH4_CTRL.STRUCTTYPE', 'read-only',
            "",
            0, 2,
            RM_Enum_LDMA_CH4_CTRL_STRUCTTYPE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CTRL_STRUCTREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CTRL_STRUCTREQ, self).__init__(register,
            'STRUCTREQ', 'LDMA.CH4_CTRL.STRUCTREQ', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CTRL_XFERCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CTRL_XFERCNT, self).__init__(register,
            'XFERCNT', 'LDMA.CH4_CTRL.XFERCNT', 'read-write',
            "",
            4, 11)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CTRL_BYTESWAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CTRL_BYTESWAP, self).__init__(register,
            'BYTESWAP', 'LDMA.CH4_CTRL.BYTESWAP', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CTRL_BLOCKSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CTRL_BLOCKSIZE, self).__init__(register,
            'BLOCKSIZE', 'LDMA.CH4_CTRL.BLOCKSIZE', 'read-write',
            "",
            16, 4,
            RM_Enum_LDMA_CH4_CTRL_BLOCKSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CTRL_DONEIFSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CTRL_DONEIFSEN, self).__init__(register,
            'DONEIFSEN', 'LDMA.CH4_CTRL.DONEIFSEN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CTRL_REQMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CTRL_REQMODE, self).__init__(register,
            'REQMODE', 'LDMA.CH4_CTRL.REQMODE', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CTRL_DECLOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CTRL_DECLOOPCNT, self).__init__(register,
            'DECLOOPCNT', 'LDMA.CH4_CTRL.DECLOOPCNT', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CTRL_IGNORESREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CTRL_IGNORESREQ, self).__init__(register,
            'IGNORESREQ', 'LDMA.CH4_CTRL.IGNORESREQ', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CTRL_SRCINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CTRL_SRCINC, self).__init__(register,
            'SRCINC', 'LDMA.CH4_CTRL.SRCINC', 'read-write',
            "",
            24, 2,
            RM_Enum_LDMA_CH4_CTRL_SRCINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CTRL_SIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CTRL_SIZE, self).__init__(register,
            'SIZE', 'LDMA.CH4_CTRL.SIZE', 'read-write',
            "",
            26, 2,
            RM_Enum_LDMA_CH4_CTRL_SIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CTRL_DSTINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CTRL_DSTINC, self).__init__(register,
            'DSTINC', 'LDMA.CH4_CTRL.DSTINC', 'read-write',
            "",
            28, 2,
            RM_Enum_LDMA_CH4_CTRL_DSTINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CTRL_SRCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CTRL_SRCMODE, self).__init__(register,
            'SRCMODE', 'LDMA.CH4_CTRL.SRCMODE', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_CTRL_DSTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_CTRL_DSTMODE, self).__init__(register,
            'DSTMODE', 'LDMA.CH4_CTRL.DSTMODE', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_SRC_SRCADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_SRC_SRCADDR, self).__init__(register,
            'SRCADDR', 'LDMA.CH4_SRC.SRCADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_DST_DSTADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_DST_DSTADDR, self).__init__(register,
            'DSTADDR', 'LDMA.CH4_DST.DSTADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_LINK_LINKMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_LINK_LINKMODE, self).__init__(register,
            'LINKMODE', 'LDMA.CH4_LINK.LINKMODE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_LINK_LINK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_LINK_LINK, self).__init__(register,
            'LINK', 'LDMA.CH4_LINK.LINK', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH4_LINK_LINKADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH4_LINK_LINKADDR, self).__init__(register,
            'LINKADDR', 'LDMA.CH4_LINK.LINKADDR', 'read-write',
            "",
            2, 30)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_REQSEL_SIGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_REQSEL_SIGSEL, self).__init__(register,
            'SIGSEL', 'LDMA.CH5_REQSEL.SIGSEL', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_REQSEL_SOURCESEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_REQSEL_SOURCESEL, self).__init__(register,
            'SOURCESEL', 'LDMA.CH5_REQSEL.SOURCESEL', 'read-write',
            "",
            16, 6,
            RM_Enum_LDMA_CH5_REQSEL_SOURCESEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CFG_ARBSLOTS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CFG_ARBSLOTS, self).__init__(register,
            'ARBSLOTS', 'LDMA.CH5_CFG.ARBSLOTS', 'read-write',
            "",
            16, 2,
            RM_Enum_LDMA_CH5_CFG_ARBSLOTS(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CFG_SRCINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CFG_SRCINCSIGN, self).__init__(register,
            'SRCINCSIGN', 'LDMA.CH5_CFG.SRCINCSIGN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CFG_DSTINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CFG_DSTINCSIGN, self).__init__(register,
            'DSTINCSIGN', 'LDMA.CH5_CFG.DSTINCSIGN', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_LOOP_LOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_LOOP_LOOPCNT, self).__init__(register,
            'LOOPCNT', 'LDMA.CH5_LOOP.LOOPCNT', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CTRL_STRUCTTYPE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CTRL_STRUCTTYPE, self).__init__(register,
            'STRUCTTYPE', 'LDMA.CH5_CTRL.STRUCTTYPE', 'read-only',
            "",
            0, 2,
            RM_Enum_LDMA_CH5_CTRL_STRUCTTYPE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CTRL_STRUCTREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CTRL_STRUCTREQ, self).__init__(register,
            'STRUCTREQ', 'LDMA.CH5_CTRL.STRUCTREQ', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CTRL_XFERCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CTRL_XFERCNT, self).__init__(register,
            'XFERCNT', 'LDMA.CH5_CTRL.XFERCNT', 'read-write',
            "",
            4, 11)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CTRL_BYTESWAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CTRL_BYTESWAP, self).__init__(register,
            'BYTESWAP', 'LDMA.CH5_CTRL.BYTESWAP', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CTRL_BLOCKSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CTRL_BLOCKSIZE, self).__init__(register,
            'BLOCKSIZE', 'LDMA.CH5_CTRL.BLOCKSIZE', 'read-write',
            "",
            16, 4,
            RM_Enum_LDMA_CH5_CTRL_BLOCKSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CTRL_DONEIFSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CTRL_DONEIFSEN, self).__init__(register,
            'DONEIFSEN', 'LDMA.CH5_CTRL.DONEIFSEN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CTRL_REQMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CTRL_REQMODE, self).__init__(register,
            'REQMODE', 'LDMA.CH5_CTRL.REQMODE', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CTRL_DECLOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CTRL_DECLOOPCNT, self).__init__(register,
            'DECLOOPCNT', 'LDMA.CH5_CTRL.DECLOOPCNT', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CTRL_IGNORESREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CTRL_IGNORESREQ, self).__init__(register,
            'IGNORESREQ', 'LDMA.CH5_CTRL.IGNORESREQ', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CTRL_SRCINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CTRL_SRCINC, self).__init__(register,
            'SRCINC', 'LDMA.CH5_CTRL.SRCINC', 'read-write',
            "",
            24, 2,
            RM_Enum_LDMA_CH5_CTRL_SRCINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CTRL_SIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CTRL_SIZE, self).__init__(register,
            'SIZE', 'LDMA.CH5_CTRL.SIZE', 'read-write',
            "",
            26, 2,
            RM_Enum_LDMA_CH5_CTRL_SIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CTRL_DSTINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CTRL_DSTINC, self).__init__(register,
            'DSTINC', 'LDMA.CH5_CTRL.DSTINC', 'read-write',
            "",
            28, 2,
            RM_Enum_LDMA_CH5_CTRL_DSTINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CTRL_SRCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CTRL_SRCMODE, self).__init__(register,
            'SRCMODE', 'LDMA.CH5_CTRL.SRCMODE', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_CTRL_DSTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_CTRL_DSTMODE, self).__init__(register,
            'DSTMODE', 'LDMA.CH5_CTRL.DSTMODE', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_SRC_SRCADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_SRC_SRCADDR, self).__init__(register,
            'SRCADDR', 'LDMA.CH5_SRC.SRCADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_DST_DSTADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_DST_DSTADDR, self).__init__(register,
            'DSTADDR', 'LDMA.CH5_DST.DSTADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_LINK_LINKMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_LINK_LINKMODE, self).__init__(register,
            'LINKMODE', 'LDMA.CH5_LINK.LINKMODE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_LINK_LINK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_LINK_LINK, self).__init__(register,
            'LINK', 'LDMA.CH5_LINK.LINK', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH5_LINK_LINKADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH5_LINK_LINKADDR, self).__init__(register,
            'LINKADDR', 'LDMA.CH5_LINK.LINKADDR', 'read-write',
            "",
            2, 30)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_REQSEL_SIGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_REQSEL_SIGSEL, self).__init__(register,
            'SIGSEL', 'LDMA.CH6_REQSEL.SIGSEL', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_REQSEL_SOURCESEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_REQSEL_SOURCESEL, self).__init__(register,
            'SOURCESEL', 'LDMA.CH6_REQSEL.SOURCESEL', 'read-write',
            "",
            16, 6,
            RM_Enum_LDMA_CH6_REQSEL_SOURCESEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CFG_ARBSLOTS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CFG_ARBSLOTS, self).__init__(register,
            'ARBSLOTS', 'LDMA.CH6_CFG.ARBSLOTS', 'read-write',
            "",
            16, 2,
            RM_Enum_LDMA_CH6_CFG_ARBSLOTS(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CFG_SRCINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CFG_SRCINCSIGN, self).__init__(register,
            'SRCINCSIGN', 'LDMA.CH6_CFG.SRCINCSIGN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CFG_DSTINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CFG_DSTINCSIGN, self).__init__(register,
            'DSTINCSIGN', 'LDMA.CH6_CFG.DSTINCSIGN', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_LOOP_LOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_LOOP_LOOPCNT, self).__init__(register,
            'LOOPCNT', 'LDMA.CH6_LOOP.LOOPCNT', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CTRL_STRUCTTYPE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CTRL_STRUCTTYPE, self).__init__(register,
            'STRUCTTYPE', 'LDMA.CH6_CTRL.STRUCTTYPE', 'read-only',
            "",
            0, 2,
            RM_Enum_LDMA_CH6_CTRL_STRUCTTYPE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CTRL_STRUCTREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CTRL_STRUCTREQ, self).__init__(register,
            'STRUCTREQ', 'LDMA.CH6_CTRL.STRUCTREQ', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CTRL_XFERCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CTRL_XFERCNT, self).__init__(register,
            'XFERCNT', 'LDMA.CH6_CTRL.XFERCNT', 'read-write',
            "",
            4, 11)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CTRL_BYTESWAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CTRL_BYTESWAP, self).__init__(register,
            'BYTESWAP', 'LDMA.CH6_CTRL.BYTESWAP', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CTRL_BLOCKSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CTRL_BLOCKSIZE, self).__init__(register,
            'BLOCKSIZE', 'LDMA.CH6_CTRL.BLOCKSIZE', 'read-write',
            "",
            16, 4,
            RM_Enum_LDMA_CH6_CTRL_BLOCKSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CTRL_DONEIFSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CTRL_DONEIFSEN, self).__init__(register,
            'DONEIFSEN', 'LDMA.CH6_CTRL.DONEIFSEN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CTRL_REQMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CTRL_REQMODE, self).__init__(register,
            'REQMODE', 'LDMA.CH6_CTRL.REQMODE', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CTRL_DECLOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CTRL_DECLOOPCNT, self).__init__(register,
            'DECLOOPCNT', 'LDMA.CH6_CTRL.DECLOOPCNT', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CTRL_IGNORESREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CTRL_IGNORESREQ, self).__init__(register,
            'IGNORESREQ', 'LDMA.CH6_CTRL.IGNORESREQ', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CTRL_SRCINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CTRL_SRCINC, self).__init__(register,
            'SRCINC', 'LDMA.CH6_CTRL.SRCINC', 'read-write',
            "",
            24, 2,
            RM_Enum_LDMA_CH6_CTRL_SRCINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CTRL_SIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CTRL_SIZE, self).__init__(register,
            'SIZE', 'LDMA.CH6_CTRL.SIZE', 'read-write',
            "",
            26, 2,
            RM_Enum_LDMA_CH6_CTRL_SIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CTRL_DSTINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CTRL_DSTINC, self).__init__(register,
            'DSTINC', 'LDMA.CH6_CTRL.DSTINC', 'read-write',
            "",
            28, 2,
            RM_Enum_LDMA_CH6_CTRL_DSTINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CTRL_SRCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CTRL_SRCMODE, self).__init__(register,
            'SRCMODE', 'LDMA.CH6_CTRL.SRCMODE', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_CTRL_DSTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_CTRL_DSTMODE, self).__init__(register,
            'DSTMODE', 'LDMA.CH6_CTRL.DSTMODE', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_SRC_SRCADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_SRC_SRCADDR, self).__init__(register,
            'SRCADDR', 'LDMA.CH6_SRC.SRCADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_DST_DSTADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_DST_DSTADDR, self).__init__(register,
            'DSTADDR', 'LDMA.CH6_DST.DSTADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_LINK_LINKMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_LINK_LINKMODE, self).__init__(register,
            'LINKMODE', 'LDMA.CH6_LINK.LINKMODE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_LINK_LINK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_LINK_LINK, self).__init__(register,
            'LINK', 'LDMA.CH6_LINK.LINK', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH6_LINK_LINKADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH6_LINK_LINKADDR, self).__init__(register,
            'LINKADDR', 'LDMA.CH6_LINK.LINKADDR', 'read-write',
            "",
            2, 30)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_REQSEL_SIGSEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_REQSEL_SIGSEL, self).__init__(register,
            'SIGSEL', 'LDMA.CH7_REQSEL.SIGSEL', 'read-write',
            "",
            0, 4)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_REQSEL_SOURCESEL(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_REQSEL_SOURCESEL, self).__init__(register,
            'SOURCESEL', 'LDMA.CH7_REQSEL.SOURCESEL', 'read-write',
            "",
            16, 6,
            RM_Enum_LDMA_CH7_REQSEL_SOURCESEL(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CFG_ARBSLOTS(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CFG_ARBSLOTS, self).__init__(register,
            'ARBSLOTS', 'LDMA.CH7_CFG.ARBSLOTS', 'read-write',
            "",
            16, 2,
            RM_Enum_LDMA_CH7_CFG_ARBSLOTS(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CFG_SRCINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CFG_SRCINCSIGN, self).__init__(register,
            'SRCINCSIGN', 'LDMA.CH7_CFG.SRCINCSIGN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CFG_DSTINCSIGN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CFG_DSTINCSIGN, self).__init__(register,
            'DSTINCSIGN', 'LDMA.CH7_CFG.DSTINCSIGN', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_LOOP_LOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_LOOP_LOOPCNT, self).__init__(register,
            'LOOPCNT', 'LDMA.CH7_LOOP.LOOPCNT', 'read-write',
            "",
            0, 8)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CTRL_STRUCTTYPE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CTRL_STRUCTTYPE, self).__init__(register,
            'STRUCTTYPE', 'LDMA.CH7_CTRL.STRUCTTYPE', 'read-only',
            "",
            0, 2,
            RM_Enum_LDMA_CH7_CTRL_STRUCTTYPE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CTRL_STRUCTREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CTRL_STRUCTREQ, self).__init__(register,
            'STRUCTREQ', 'LDMA.CH7_CTRL.STRUCTREQ', 'write-only',
            "",
            3, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CTRL_XFERCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CTRL_XFERCNT, self).__init__(register,
            'XFERCNT', 'LDMA.CH7_CTRL.XFERCNT', 'read-write',
            "",
            4, 11)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CTRL_BYTESWAP(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CTRL_BYTESWAP, self).__init__(register,
            'BYTESWAP', 'LDMA.CH7_CTRL.BYTESWAP', 'read-write',
            "",
            15, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CTRL_BLOCKSIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CTRL_BLOCKSIZE, self).__init__(register,
            'BLOCKSIZE', 'LDMA.CH7_CTRL.BLOCKSIZE', 'read-write',
            "",
            16, 4,
            RM_Enum_LDMA_CH7_CTRL_BLOCKSIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CTRL_DONEIFSEN(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CTRL_DONEIFSEN, self).__init__(register,
            'DONEIFSEN', 'LDMA.CH7_CTRL.DONEIFSEN', 'read-write',
            "",
            20, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CTRL_REQMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CTRL_REQMODE, self).__init__(register,
            'REQMODE', 'LDMA.CH7_CTRL.REQMODE', 'read-write',
            "",
            21, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CTRL_DECLOOPCNT(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CTRL_DECLOOPCNT, self).__init__(register,
            'DECLOOPCNT', 'LDMA.CH7_CTRL.DECLOOPCNT', 'read-write',
            "",
            22, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CTRL_IGNORESREQ(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CTRL_IGNORESREQ, self).__init__(register,
            'IGNORESREQ', 'LDMA.CH7_CTRL.IGNORESREQ', 'read-write',
            "",
            23, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CTRL_SRCINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CTRL_SRCINC, self).__init__(register,
            'SRCINC', 'LDMA.CH7_CTRL.SRCINC', 'read-write',
            "",
            24, 2,
            RM_Enum_LDMA_CH7_CTRL_SRCINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CTRL_SIZE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CTRL_SIZE, self).__init__(register,
            'SIZE', 'LDMA.CH7_CTRL.SIZE', 'read-write',
            "",
            26, 2,
            RM_Enum_LDMA_CH7_CTRL_SIZE(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CTRL_DSTINC(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CTRL_DSTINC, self).__init__(register,
            'DSTINC', 'LDMA.CH7_CTRL.DSTINC', 'read-write',
            "",
            28, 2,
            RM_Enum_LDMA_CH7_CTRL_DSTINC(register.zz_label))
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CTRL_SRCMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CTRL_SRCMODE, self).__init__(register,
            'SRCMODE', 'LDMA.CH7_CTRL.SRCMODE', 'read-only',
            "",
            30, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_CTRL_DSTMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_CTRL_DSTMODE, self).__init__(register,
            'DSTMODE', 'LDMA.CH7_CTRL.DSTMODE', 'read-only',
            "",
            31, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_SRC_SRCADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_SRC_SRCADDR, self).__init__(register,
            'SRCADDR', 'LDMA.CH7_SRC.SRCADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_DST_DSTADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_DST_DSTADDR, self).__init__(register,
            'DSTADDR', 'LDMA.CH7_DST.DSTADDR', 'read-write',
            "",
            0, 32)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_LINK_LINKMODE(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_LINK_LINKMODE, self).__init__(register,
            'LINKMODE', 'LDMA.CH7_LINK.LINKMODE', 'read-only',
            "",
            0, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_LINK_LINK(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_LINK_LINK, self).__init__(register,
            'LINK', 'LDMA.CH7_LINK.LINK', 'read-write',
            "",
            1, 1)
        self.__dict__['zz_frozen'] = True


class RM_Field_LDMA_CH7_LINK_LINKADDR(Base_RM_Field):
    def __init__(self, register):
        self.__dict__['zz_frozen'] = False
        super(RM_Field_LDMA_CH7_LINK_LINKADDR, self).__init__(register,
            'LINKADDR', 'LDMA.CH7_LINK.LINKADDR', 'read-write',
            "",
            2, 30)
        self.__dict__['zz_frozen'] = True


