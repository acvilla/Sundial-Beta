
from static import Base_RM_Register
from PRS_field import *


class RM_Register_PRS_SWPULSE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_SWPULSE, self).__init__(rmio, label,
            0x400e6000, 0x000,
            'SWPULSE', 'PRS.SWPULSE', 'write-only',
            "",
            0x00000000, 0x00000FFF)

        self.CH0PULSE = RM_Field_PRS_SWPULSE_CH0PULSE(self)
        self.zz_fdict['CH0PULSE'] = self.CH0PULSE
        self.CH1PULSE = RM_Field_PRS_SWPULSE_CH1PULSE(self)
        self.zz_fdict['CH1PULSE'] = self.CH1PULSE
        self.CH2PULSE = RM_Field_PRS_SWPULSE_CH2PULSE(self)
        self.zz_fdict['CH2PULSE'] = self.CH2PULSE
        self.CH3PULSE = RM_Field_PRS_SWPULSE_CH3PULSE(self)
        self.zz_fdict['CH3PULSE'] = self.CH3PULSE
        self.CH4PULSE = RM_Field_PRS_SWPULSE_CH4PULSE(self)
        self.zz_fdict['CH4PULSE'] = self.CH4PULSE
        self.CH5PULSE = RM_Field_PRS_SWPULSE_CH5PULSE(self)
        self.zz_fdict['CH5PULSE'] = self.CH5PULSE
        self.CH6PULSE = RM_Field_PRS_SWPULSE_CH6PULSE(self)
        self.zz_fdict['CH6PULSE'] = self.CH6PULSE
        self.CH7PULSE = RM_Field_PRS_SWPULSE_CH7PULSE(self)
        self.zz_fdict['CH7PULSE'] = self.CH7PULSE
        self.CH8PULSE = RM_Field_PRS_SWPULSE_CH8PULSE(self)
        self.zz_fdict['CH8PULSE'] = self.CH8PULSE
        self.CH9PULSE = RM_Field_PRS_SWPULSE_CH9PULSE(self)
        self.zz_fdict['CH9PULSE'] = self.CH9PULSE
        self.CH10PULSE = RM_Field_PRS_SWPULSE_CH10PULSE(self)
        self.zz_fdict['CH10PULSE'] = self.CH10PULSE
        self.CH11PULSE = RM_Field_PRS_SWPULSE_CH11PULSE(self)
        self.zz_fdict['CH11PULSE'] = self.CH11PULSE
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_SWLEVEL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_SWLEVEL, self).__init__(rmio, label,
            0x400e6000, 0x004,
            'SWLEVEL', 'PRS.SWLEVEL', 'read-write',
            "",
            0x00000000, 0x00000FFF)

        self.CH0LEVEL = RM_Field_PRS_SWLEVEL_CH0LEVEL(self)
        self.zz_fdict['CH0LEVEL'] = self.CH0LEVEL
        self.CH1LEVEL = RM_Field_PRS_SWLEVEL_CH1LEVEL(self)
        self.zz_fdict['CH1LEVEL'] = self.CH1LEVEL
        self.CH2LEVEL = RM_Field_PRS_SWLEVEL_CH2LEVEL(self)
        self.zz_fdict['CH2LEVEL'] = self.CH2LEVEL
        self.CH3LEVEL = RM_Field_PRS_SWLEVEL_CH3LEVEL(self)
        self.zz_fdict['CH3LEVEL'] = self.CH3LEVEL
        self.CH4LEVEL = RM_Field_PRS_SWLEVEL_CH4LEVEL(self)
        self.zz_fdict['CH4LEVEL'] = self.CH4LEVEL
        self.CH5LEVEL = RM_Field_PRS_SWLEVEL_CH5LEVEL(self)
        self.zz_fdict['CH5LEVEL'] = self.CH5LEVEL
        self.CH6LEVEL = RM_Field_PRS_SWLEVEL_CH6LEVEL(self)
        self.zz_fdict['CH6LEVEL'] = self.CH6LEVEL
        self.CH7LEVEL = RM_Field_PRS_SWLEVEL_CH7LEVEL(self)
        self.zz_fdict['CH7LEVEL'] = self.CH7LEVEL
        self.CH8LEVEL = RM_Field_PRS_SWLEVEL_CH8LEVEL(self)
        self.zz_fdict['CH8LEVEL'] = self.CH8LEVEL
        self.CH9LEVEL = RM_Field_PRS_SWLEVEL_CH9LEVEL(self)
        self.zz_fdict['CH9LEVEL'] = self.CH9LEVEL
        self.CH10LEVEL = RM_Field_PRS_SWLEVEL_CH10LEVEL(self)
        self.zz_fdict['CH10LEVEL'] = self.CH10LEVEL
        self.CH11LEVEL = RM_Field_PRS_SWLEVEL_CH11LEVEL(self)
        self.zz_fdict['CH11LEVEL'] = self.CH11LEVEL
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_ROUTEPEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_ROUTEPEN, self).__init__(rmio, label,
            0x400e6000, 0x008,
            'ROUTEPEN', 'PRS.ROUTEPEN', 'read-write',
            "",
            0x00000000, 0x00000FFF)

        self.CH0PEN = RM_Field_PRS_ROUTEPEN_CH0PEN(self)
        self.zz_fdict['CH0PEN'] = self.CH0PEN
        self.CH1PEN = RM_Field_PRS_ROUTEPEN_CH1PEN(self)
        self.zz_fdict['CH1PEN'] = self.CH1PEN
        self.CH2PEN = RM_Field_PRS_ROUTEPEN_CH2PEN(self)
        self.zz_fdict['CH2PEN'] = self.CH2PEN
        self.CH3PEN = RM_Field_PRS_ROUTEPEN_CH3PEN(self)
        self.zz_fdict['CH3PEN'] = self.CH3PEN
        self.CH4PEN = RM_Field_PRS_ROUTEPEN_CH4PEN(self)
        self.zz_fdict['CH4PEN'] = self.CH4PEN
        self.CH5PEN = RM_Field_PRS_ROUTEPEN_CH5PEN(self)
        self.zz_fdict['CH5PEN'] = self.CH5PEN
        self.CH6PEN = RM_Field_PRS_ROUTEPEN_CH6PEN(self)
        self.zz_fdict['CH6PEN'] = self.CH6PEN
        self.CH7PEN = RM_Field_PRS_ROUTEPEN_CH7PEN(self)
        self.zz_fdict['CH7PEN'] = self.CH7PEN
        self.CH8PEN = RM_Field_PRS_ROUTEPEN_CH8PEN(self)
        self.zz_fdict['CH8PEN'] = self.CH8PEN
        self.CH9PEN = RM_Field_PRS_ROUTEPEN_CH9PEN(self)
        self.zz_fdict['CH9PEN'] = self.CH9PEN
        self.CH10PEN = RM_Field_PRS_ROUTEPEN_CH10PEN(self)
        self.zz_fdict['CH10PEN'] = self.CH10PEN
        self.CH11PEN = RM_Field_PRS_ROUTEPEN_CH11PEN(self)
        self.zz_fdict['CH11PEN'] = self.CH11PEN
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_ROUTELOC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_ROUTELOC0, self).__init__(rmio, label,
            0x400e6000, 0x010,
            'ROUTELOC0', 'PRS.ROUTELOC0', 'read-write',
            "",
            0x00000000, 0x3F3F3F3F)

        self.CH0LOC = RM_Field_PRS_ROUTELOC0_CH0LOC(self)
        self.zz_fdict['CH0LOC'] = self.CH0LOC
        self.CH1LOC = RM_Field_PRS_ROUTELOC0_CH1LOC(self)
        self.zz_fdict['CH1LOC'] = self.CH1LOC
        self.CH2LOC = RM_Field_PRS_ROUTELOC0_CH2LOC(self)
        self.zz_fdict['CH2LOC'] = self.CH2LOC
        self.CH3LOC = RM_Field_PRS_ROUTELOC0_CH3LOC(self)
        self.zz_fdict['CH3LOC'] = self.CH3LOC
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_ROUTELOC1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_ROUTELOC1, self).__init__(rmio, label,
            0x400e6000, 0x014,
            'ROUTELOC1', 'PRS.ROUTELOC1', 'read-write',
            "",
            0x00000000, 0x3F3F3F3F)

        self.CH4LOC = RM_Field_PRS_ROUTELOC1_CH4LOC(self)
        self.zz_fdict['CH4LOC'] = self.CH4LOC
        self.CH5LOC = RM_Field_PRS_ROUTELOC1_CH5LOC(self)
        self.zz_fdict['CH5LOC'] = self.CH5LOC
        self.CH6LOC = RM_Field_PRS_ROUTELOC1_CH6LOC(self)
        self.zz_fdict['CH6LOC'] = self.CH6LOC
        self.CH7LOC = RM_Field_PRS_ROUTELOC1_CH7LOC(self)
        self.zz_fdict['CH7LOC'] = self.CH7LOC
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_ROUTELOC2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_ROUTELOC2, self).__init__(rmio, label,
            0x400e6000, 0x018,
            'ROUTELOC2', 'PRS.ROUTELOC2', 'read-write',
            "",
            0x00000000, 0x3F3F3F3F)

        self.CH8LOC = RM_Field_PRS_ROUTELOC2_CH8LOC(self)
        self.zz_fdict['CH8LOC'] = self.CH8LOC
        self.CH9LOC = RM_Field_PRS_ROUTELOC2_CH9LOC(self)
        self.zz_fdict['CH9LOC'] = self.CH9LOC
        self.CH10LOC = RM_Field_PRS_ROUTELOC2_CH10LOC(self)
        self.zz_fdict['CH10LOC'] = self.CH10LOC
        self.CH11LOC = RM_Field_PRS_ROUTELOC2_CH11LOC(self)
        self.zz_fdict['CH11LOC'] = self.CH11LOC
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_CTRL, self).__init__(rmio, label,
            0x400e6000, 0x030,
            'CTRL', 'PRS.CTRL', 'read-write',
            "",
            0x00000000, 0x0000001F)

        self.SEVONPRS = RM_Field_PRS_CTRL_SEVONPRS(self)
        self.zz_fdict['SEVONPRS'] = self.SEVONPRS
        self.SEVONPRSSEL = RM_Field_PRS_CTRL_SEVONPRSSEL(self)
        self.zz_fdict['SEVONPRSSEL'] = self.SEVONPRSSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_DMAREQ0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_DMAREQ0, self).__init__(rmio, label,
            0x400e6000, 0x034,
            'DMAREQ0', 'PRS.DMAREQ0', 'read-write',
            "",
            0x00000000, 0x000003C0)

        self.PRSSEL = RM_Field_PRS_DMAREQ0_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_DMAREQ1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_DMAREQ1, self).__init__(rmio, label,
            0x400e6000, 0x038,
            'DMAREQ1', 'PRS.DMAREQ1', 'read-write',
            "",
            0x00000000, 0x000003C0)

        self.PRSSEL = RM_Field_PRS_DMAREQ1_PRSSEL(self)
        self.zz_fdict['PRSSEL'] = self.PRSSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_PEEK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_PEEK, self).__init__(rmio, label,
            0x400e6000, 0x040,
            'PEEK', 'PRS.PEEK', 'read-only',
            "",
            0x00000000, 0x00000FFF)

        self.CH0VAL = RM_Field_PRS_PEEK_CH0VAL(self)
        self.zz_fdict['CH0VAL'] = self.CH0VAL
        self.CH1VAL = RM_Field_PRS_PEEK_CH1VAL(self)
        self.zz_fdict['CH1VAL'] = self.CH1VAL
        self.CH2VAL = RM_Field_PRS_PEEK_CH2VAL(self)
        self.zz_fdict['CH2VAL'] = self.CH2VAL
        self.CH3VAL = RM_Field_PRS_PEEK_CH3VAL(self)
        self.zz_fdict['CH3VAL'] = self.CH3VAL
        self.CH4VAL = RM_Field_PRS_PEEK_CH4VAL(self)
        self.zz_fdict['CH4VAL'] = self.CH4VAL
        self.CH5VAL = RM_Field_PRS_PEEK_CH5VAL(self)
        self.zz_fdict['CH5VAL'] = self.CH5VAL
        self.CH6VAL = RM_Field_PRS_PEEK_CH6VAL(self)
        self.zz_fdict['CH6VAL'] = self.CH6VAL
        self.CH7VAL = RM_Field_PRS_PEEK_CH7VAL(self)
        self.zz_fdict['CH7VAL'] = self.CH7VAL
        self.CH8VAL = RM_Field_PRS_PEEK_CH8VAL(self)
        self.zz_fdict['CH8VAL'] = self.CH8VAL
        self.CH9VAL = RM_Field_PRS_PEEK_CH9VAL(self)
        self.zz_fdict['CH9VAL'] = self.CH9VAL
        self.CH10VAL = RM_Field_PRS_PEEK_CH10VAL(self)
        self.zz_fdict['CH10VAL'] = self.CH10VAL
        self.CH11VAL = RM_Field_PRS_PEEK_CH11VAL(self)
        self.zz_fdict['CH11VAL'] = self.CH11VAL
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_CH0_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_CH0_CTRL, self).__init__(rmio, label,
            0x400e6000, 0x050,
            'CH0_CTRL', 'PRS.CH0_CTRL', 'read-write',
            "",
            0x00000000, 0x5E307F07)

        self.SIGSEL = RM_Field_PRS_CH0_CTRL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_PRS_CH0_CTRL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.EDSEL = RM_Field_PRS_CH0_CTRL_EDSEL(self)
        self.zz_fdict['EDSEL'] = self.EDSEL
        self.STRETCH = RM_Field_PRS_CH0_CTRL_STRETCH(self)
        self.zz_fdict['STRETCH'] = self.STRETCH
        self.INV = RM_Field_PRS_CH0_CTRL_INV(self)
        self.zz_fdict['INV'] = self.INV
        self.ORPREV = RM_Field_PRS_CH0_CTRL_ORPREV(self)
        self.zz_fdict['ORPREV'] = self.ORPREV
        self.ANDNEXT = RM_Field_PRS_CH0_CTRL_ANDNEXT(self)
        self.zz_fdict['ANDNEXT'] = self.ANDNEXT
        self.ASYNC = RM_Field_PRS_CH0_CTRL_ASYNC(self)
        self.zz_fdict['ASYNC'] = self.ASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_CH1_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_CH1_CTRL, self).__init__(rmio, label,
            0x400e6000, 0x054,
            'CH1_CTRL', 'PRS.CH1_CTRL', 'read-write',
            "",
            0x00000000, 0x5E307F07)

        self.SIGSEL = RM_Field_PRS_CH1_CTRL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_PRS_CH1_CTRL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.EDSEL = RM_Field_PRS_CH1_CTRL_EDSEL(self)
        self.zz_fdict['EDSEL'] = self.EDSEL
        self.STRETCH = RM_Field_PRS_CH1_CTRL_STRETCH(self)
        self.zz_fdict['STRETCH'] = self.STRETCH
        self.INV = RM_Field_PRS_CH1_CTRL_INV(self)
        self.zz_fdict['INV'] = self.INV
        self.ORPREV = RM_Field_PRS_CH1_CTRL_ORPREV(self)
        self.zz_fdict['ORPREV'] = self.ORPREV
        self.ANDNEXT = RM_Field_PRS_CH1_CTRL_ANDNEXT(self)
        self.zz_fdict['ANDNEXT'] = self.ANDNEXT
        self.ASYNC = RM_Field_PRS_CH1_CTRL_ASYNC(self)
        self.zz_fdict['ASYNC'] = self.ASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_CH2_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_CH2_CTRL, self).__init__(rmio, label,
            0x400e6000, 0x058,
            'CH2_CTRL', 'PRS.CH2_CTRL', 'read-write',
            "",
            0x00000000, 0x5E307F07)

        self.SIGSEL = RM_Field_PRS_CH2_CTRL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_PRS_CH2_CTRL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.EDSEL = RM_Field_PRS_CH2_CTRL_EDSEL(self)
        self.zz_fdict['EDSEL'] = self.EDSEL
        self.STRETCH = RM_Field_PRS_CH2_CTRL_STRETCH(self)
        self.zz_fdict['STRETCH'] = self.STRETCH
        self.INV = RM_Field_PRS_CH2_CTRL_INV(self)
        self.zz_fdict['INV'] = self.INV
        self.ORPREV = RM_Field_PRS_CH2_CTRL_ORPREV(self)
        self.zz_fdict['ORPREV'] = self.ORPREV
        self.ANDNEXT = RM_Field_PRS_CH2_CTRL_ANDNEXT(self)
        self.zz_fdict['ANDNEXT'] = self.ANDNEXT
        self.ASYNC = RM_Field_PRS_CH2_CTRL_ASYNC(self)
        self.zz_fdict['ASYNC'] = self.ASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_CH3_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_CH3_CTRL, self).__init__(rmio, label,
            0x400e6000, 0x05C,
            'CH3_CTRL', 'PRS.CH3_CTRL', 'read-write',
            "",
            0x00000000, 0x5E307F07)

        self.SIGSEL = RM_Field_PRS_CH3_CTRL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_PRS_CH3_CTRL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.EDSEL = RM_Field_PRS_CH3_CTRL_EDSEL(self)
        self.zz_fdict['EDSEL'] = self.EDSEL
        self.STRETCH = RM_Field_PRS_CH3_CTRL_STRETCH(self)
        self.zz_fdict['STRETCH'] = self.STRETCH
        self.INV = RM_Field_PRS_CH3_CTRL_INV(self)
        self.zz_fdict['INV'] = self.INV
        self.ORPREV = RM_Field_PRS_CH3_CTRL_ORPREV(self)
        self.zz_fdict['ORPREV'] = self.ORPREV
        self.ANDNEXT = RM_Field_PRS_CH3_CTRL_ANDNEXT(self)
        self.zz_fdict['ANDNEXT'] = self.ANDNEXT
        self.ASYNC = RM_Field_PRS_CH3_CTRL_ASYNC(self)
        self.zz_fdict['ASYNC'] = self.ASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_CH4_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_CH4_CTRL, self).__init__(rmio, label,
            0x400e6000, 0x060,
            'CH4_CTRL', 'PRS.CH4_CTRL', 'read-write',
            "",
            0x00000000, 0x5E307F07)

        self.SIGSEL = RM_Field_PRS_CH4_CTRL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_PRS_CH4_CTRL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.EDSEL = RM_Field_PRS_CH4_CTRL_EDSEL(self)
        self.zz_fdict['EDSEL'] = self.EDSEL
        self.STRETCH = RM_Field_PRS_CH4_CTRL_STRETCH(self)
        self.zz_fdict['STRETCH'] = self.STRETCH
        self.INV = RM_Field_PRS_CH4_CTRL_INV(self)
        self.zz_fdict['INV'] = self.INV
        self.ORPREV = RM_Field_PRS_CH4_CTRL_ORPREV(self)
        self.zz_fdict['ORPREV'] = self.ORPREV
        self.ANDNEXT = RM_Field_PRS_CH4_CTRL_ANDNEXT(self)
        self.zz_fdict['ANDNEXT'] = self.ANDNEXT
        self.ASYNC = RM_Field_PRS_CH4_CTRL_ASYNC(self)
        self.zz_fdict['ASYNC'] = self.ASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_CH5_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_CH5_CTRL, self).__init__(rmio, label,
            0x400e6000, 0x064,
            'CH5_CTRL', 'PRS.CH5_CTRL', 'read-write',
            "",
            0x00000000, 0x5E307F07)

        self.SIGSEL = RM_Field_PRS_CH5_CTRL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_PRS_CH5_CTRL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.EDSEL = RM_Field_PRS_CH5_CTRL_EDSEL(self)
        self.zz_fdict['EDSEL'] = self.EDSEL
        self.STRETCH = RM_Field_PRS_CH5_CTRL_STRETCH(self)
        self.zz_fdict['STRETCH'] = self.STRETCH
        self.INV = RM_Field_PRS_CH5_CTRL_INV(self)
        self.zz_fdict['INV'] = self.INV
        self.ORPREV = RM_Field_PRS_CH5_CTRL_ORPREV(self)
        self.zz_fdict['ORPREV'] = self.ORPREV
        self.ANDNEXT = RM_Field_PRS_CH5_CTRL_ANDNEXT(self)
        self.zz_fdict['ANDNEXT'] = self.ANDNEXT
        self.ASYNC = RM_Field_PRS_CH5_CTRL_ASYNC(self)
        self.zz_fdict['ASYNC'] = self.ASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_CH6_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_CH6_CTRL, self).__init__(rmio, label,
            0x400e6000, 0x068,
            'CH6_CTRL', 'PRS.CH6_CTRL', 'read-write',
            "",
            0x00000000, 0x5E307F07)

        self.SIGSEL = RM_Field_PRS_CH6_CTRL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_PRS_CH6_CTRL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.EDSEL = RM_Field_PRS_CH6_CTRL_EDSEL(self)
        self.zz_fdict['EDSEL'] = self.EDSEL
        self.STRETCH = RM_Field_PRS_CH6_CTRL_STRETCH(self)
        self.zz_fdict['STRETCH'] = self.STRETCH
        self.INV = RM_Field_PRS_CH6_CTRL_INV(self)
        self.zz_fdict['INV'] = self.INV
        self.ORPREV = RM_Field_PRS_CH6_CTRL_ORPREV(self)
        self.zz_fdict['ORPREV'] = self.ORPREV
        self.ANDNEXT = RM_Field_PRS_CH6_CTRL_ANDNEXT(self)
        self.zz_fdict['ANDNEXT'] = self.ANDNEXT
        self.ASYNC = RM_Field_PRS_CH6_CTRL_ASYNC(self)
        self.zz_fdict['ASYNC'] = self.ASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_CH7_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_CH7_CTRL, self).__init__(rmio, label,
            0x400e6000, 0x06C,
            'CH7_CTRL', 'PRS.CH7_CTRL', 'read-write',
            "",
            0x00000000, 0x5E307F07)

        self.SIGSEL = RM_Field_PRS_CH7_CTRL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_PRS_CH7_CTRL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.EDSEL = RM_Field_PRS_CH7_CTRL_EDSEL(self)
        self.zz_fdict['EDSEL'] = self.EDSEL
        self.STRETCH = RM_Field_PRS_CH7_CTRL_STRETCH(self)
        self.zz_fdict['STRETCH'] = self.STRETCH
        self.INV = RM_Field_PRS_CH7_CTRL_INV(self)
        self.zz_fdict['INV'] = self.INV
        self.ORPREV = RM_Field_PRS_CH7_CTRL_ORPREV(self)
        self.zz_fdict['ORPREV'] = self.ORPREV
        self.ANDNEXT = RM_Field_PRS_CH7_CTRL_ANDNEXT(self)
        self.zz_fdict['ANDNEXT'] = self.ANDNEXT
        self.ASYNC = RM_Field_PRS_CH7_CTRL_ASYNC(self)
        self.zz_fdict['ASYNC'] = self.ASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_CH8_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_CH8_CTRL, self).__init__(rmio, label,
            0x400e6000, 0x070,
            'CH8_CTRL', 'PRS.CH8_CTRL', 'read-write',
            "",
            0x00000000, 0x5E307F07)

        self.SIGSEL = RM_Field_PRS_CH8_CTRL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_PRS_CH8_CTRL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.EDSEL = RM_Field_PRS_CH8_CTRL_EDSEL(self)
        self.zz_fdict['EDSEL'] = self.EDSEL
        self.STRETCH = RM_Field_PRS_CH8_CTRL_STRETCH(self)
        self.zz_fdict['STRETCH'] = self.STRETCH
        self.INV = RM_Field_PRS_CH8_CTRL_INV(self)
        self.zz_fdict['INV'] = self.INV
        self.ORPREV = RM_Field_PRS_CH8_CTRL_ORPREV(self)
        self.zz_fdict['ORPREV'] = self.ORPREV
        self.ANDNEXT = RM_Field_PRS_CH8_CTRL_ANDNEXT(self)
        self.zz_fdict['ANDNEXT'] = self.ANDNEXT
        self.ASYNC = RM_Field_PRS_CH8_CTRL_ASYNC(self)
        self.zz_fdict['ASYNC'] = self.ASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_CH9_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_CH9_CTRL, self).__init__(rmio, label,
            0x400e6000, 0x074,
            'CH9_CTRL', 'PRS.CH9_CTRL', 'read-write',
            "",
            0x00000000, 0x5E307F07)

        self.SIGSEL = RM_Field_PRS_CH9_CTRL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_PRS_CH9_CTRL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.EDSEL = RM_Field_PRS_CH9_CTRL_EDSEL(self)
        self.zz_fdict['EDSEL'] = self.EDSEL
        self.STRETCH = RM_Field_PRS_CH9_CTRL_STRETCH(self)
        self.zz_fdict['STRETCH'] = self.STRETCH
        self.INV = RM_Field_PRS_CH9_CTRL_INV(self)
        self.zz_fdict['INV'] = self.INV
        self.ORPREV = RM_Field_PRS_CH9_CTRL_ORPREV(self)
        self.zz_fdict['ORPREV'] = self.ORPREV
        self.ANDNEXT = RM_Field_PRS_CH9_CTRL_ANDNEXT(self)
        self.zz_fdict['ANDNEXT'] = self.ANDNEXT
        self.ASYNC = RM_Field_PRS_CH9_CTRL_ASYNC(self)
        self.zz_fdict['ASYNC'] = self.ASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_CH10_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_CH10_CTRL, self).__init__(rmio, label,
            0x400e6000, 0x078,
            'CH10_CTRL', 'PRS.CH10_CTRL', 'read-write',
            "",
            0x00000000, 0x5E307F07)

        self.SIGSEL = RM_Field_PRS_CH10_CTRL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_PRS_CH10_CTRL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.EDSEL = RM_Field_PRS_CH10_CTRL_EDSEL(self)
        self.zz_fdict['EDSEL'] = self.EDSEL
        self.STRETCH = RM_Field_PRS_CH10_CTRL_STRETCH(self)
        self.zz_fdict['STRETCH'] = self.STRETCH
        self.INV = RM_Field_PRS_CH10_CTRL_INV(self)
        self.zz_fdict['INV'] = self.INV
        self.ORPREV = RM_Field_PRS_CH10_CTRL_ORPREV(self)
        self.zz_fdict['ORPREV'] = self.ORPREV
        self.ANDNEXT = RM_Field_PRS_CH10_CTRL_ANDNEXT(self)
        self.zz_fdict['ANDNEXT'] = self.ANDNEXT
        self.ASYNC = RM_Field_PRS_CH10_CTRL_ASYNC(self)
        self.zz_fdict['ASYNC'] = self.ASYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_PRS_CH11_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_PRS_CH11_CTRL, self).__init__(rmio, label,
            0x400e6000, 0x07C,
            'CH11_CTRL', 'PRS.CH11_CTRL', 'read-write',
            "",
            0x00000000, 0x5E307F07)

        self.SIGSEL = RM_Field_PRS_CH11_CTRL_SIGSEL(self)
        self.zz_fdict['SIGSEL'] = self.SIGSEL
        self.SOURCESEL = RM_Field_PRS_CH11_CTRL_SOURCESEL(self)
        self.zz_fdict['SOURCESEL'] = self.SOURCESEL
        self.EDSEL = RM_Field_PRS_CH11_CTRL_EDSEL(self)
        self.zz_fdict['EDSEL'] = self.EDSEL
        self.STRETCH = RM_Field_PRS_CH11_CTRL_STRETCH(self)
        self.zz_fdict['STRETCH'] = self.STRETCH
        self.INV = RM_Field_PRS_CH11_CTRL_INV(self)
        self.zz_fdict['INV'] = self.INV
        self.ORPREV = RM_Field_PRS_CH11_CTRL_ORPREV(self)
        self.zz_fdict['ORPREV'] = self.ORPREV
        self.ANDNEXT = RM_Field_PRS_CH11_CTRL_ANDNEXT(self)
        self.zz_fdict['ANDNEXT'] = self.ANDNEXT
        self.ASYNC = RM_Field_PRS_CH11_CTRL_ASYNC(self)
        self.zz_fdict['ASYNC'] = self.ASYNC
        self.__dict__['zz_frozen'] = True


