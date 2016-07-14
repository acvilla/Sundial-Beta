
from static import Base_RM_Enum
from collections import OrderedDict


class RM_Enum_I2C1_CTRL_CLHR(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.STANDARD = 0x00000000
        zz_edict['STANDARD'] = self.STANDARD
        zz_desc['STANDARD'] = ""
        self.ASYMMETRIC = 0x00000001
        zz_edict['ASYMMETRIC'] = self.ASYMMETRIC
        zz_desc['ASYMMETRIC'] = ""
        self.FAST = 0x00000002
        zz_edict['FAST'] = self.FAST
        zz_desc['FAST'] = ""
        super(RM_Enum_I2C1_CTRL_CLHR, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_I2C1_CTRL_BITO(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.OFF = 0x00000000
        zz_edict['OFF'] = self.OFF
        zz_desc['OFF'] = ""
        #print("WARNING: Aliasing enum '40PCC' to 'E40PCC'")
        self.E40PCC = 0x00000001
        zz_edict['E40PCC'] = self.E40PCC
        zz_desc['E40PCC'] = ""
        #print("WARNING: Aliasing enum '80PCC' to 'E80PCC'")
        self.E80PCC = 0x00000002
        zz_edict['E80PCC'] = self.E80PCC
        zz_desc['E80PCC'] = ""
        #print("WARNING: Aliasing enum '160PCC' to 'E160PCC'")
        self.E160PCC = 0x00000003
        zz_edict['E160PCC'] = self.E160PCC
        zz_desc['E160PCC'] = ""
        super(RM_Enum_I2C1_CTRL_BITO, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_I2C1_CTRL_CLTO(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.OFF = 0x00000000
        zz_edict['OFF'] = self.OFF
        zz_desc['OFF'] = ""
        #print("WARNING: Aliasing enum '40PCC' to 'E40PCC'")
        self.E40PCC = 0x00000001
        zz_edict['E40PCC'] = self.E40PCC
        zz_desc['E40PCC'] = ""
        #print("WARNING: Aliasing enum '80PCC' to 'E80PCC'")
        self.E80PCC = 0x00000002
        zz_edict['E80PCC'] = self.E80PCC
        zz_desc['E80PCC'] = ""
        #print("WARNING: Aliasing enum '160PCC' to 'E160PCC'")
        self.E160PCC = 0x00000003
        zz_edict['E160PCC'] = self.E160PCC
        zz_desc['E160PCC'] = ""
        #print("WARNING: Aliasing enum '320PCC' to 'E320PCC'")
        self.E320PCC = 0x00000004
        zz_edict['E320PCC'] = self.E320PCC
        zz_desc['E320PCC'] = ""
        #print("WARNING: Aliasing enum '1024PCC' to 'E1024PCC'")
        self.E1024PCC = 0x00000005
        zz_edict['E1024PCC'] = self.E1024PCC
        zz_desc['E1024PCC'] = ""
        super(RM_Enum_I2C1_CTRL_CLTO, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_I2C1_STATE_STATE(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.IDLE = 0x00000000
        zz_edict['IDLE'] = self.IDLE
        zz_desc['IDLE'] = ""
        self.WAIT = 0x00000001
        zz_edict['WAIT'] = self.WAIT
        zz_desc['WAIT'] = ""
        self.START = 0x00000002
        zz_edict['START'] = self.START
        zz_desc['START'] = ""
        self.ADDR = 0x00000003
        zz_edict['ADDR'] = self.ADDR
        zz_desc['ADDR'] = ""
        self.ADDRACK = 0x00000004
        zz_edict['ADDRACK'] = self.ADDRACK
        zz_desc['ADDRACK'] = ""
        self.DATA = 0x00000005
        zz_edict['DATA'] = self.DATA
        zz_desc['DATA'] = ""
        self.DATAACK = 0x00000006
        zz_edict['DATAACK'] = self.DATAACK
        zz_desc['DATAACK'] = ""
        super(RM_Enum_I2C1_STATE_STATE, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_I2C1_ROUTELOC0_SDALOC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOC0 = 0x00000000
        zz_edict['LOC0'] = self.LOC0
        zz_desc['LOC0'] = ""
        self.LOC1 = 0x00000001
        zz_edict['LOC1'] = self.LOC1
        zz_desc['LOC1'] = ""
        self.LOC2 = 0x00000002
        zz_edict['LOC2'] = self.LOC2
        zz_desc['LOC2'] = ""
        self.LOC3 = 0x00000003
        zz_edict['LOC3'] = self.LOC3
        zz_desc['LOC3'] = ""
        self.LOC4 = 0x00000004
        zz_edict['LOC4'] = self.LOC4
        zz_desc['LOC4'] = ""
        self.LOC5 = 0x00000005
        zz_edict['LOC5'] = self.LOC5
        zz_desc['LOC5'] = ""
        self.LOC6 = 0x00000006
        zz_edict['LOC6'] = self.LOC6
        zz_desc['LOC6'] = ""
        self.LOC7 = 0x00000007
        zz_edict['LOC7'] = self.LOC7
        zz_desc['LOC7'] = ""
        self.LOC8 = 0x00000008
        zz_edict['LOC8'] = self.LOC8
        zz_desc['LOC8'] = ""
        self.LOC9 = 0x00000009
        zz_edict['LOC9'] = self.LOC9
        zz_desc['LOC9'] = ""
        self.LOC10 = 0x0000000A
        zz_edict['LOC10'] = self.LOC10
        zz_desc['LOC10'] = ""
        self.LOC11 = 0x0000000B
        zz_edict['LOC11'] = self.LOC11
        zz_desc['LOC11'] = ""
        self.LOC12 = 0x0000000C
        zz_edict['LOC12'] = self.LOC12
        zz_desc['LOC12'] = ""
        self.LOC13 = 0x0000000D
        zz_edict['LOC13'] = self.LOC13
        zz_desc['LOC13'] = ""
        self.LOC14 = 0x0000000E
        zz_edict['LOC14'] = self.LOC14
        zz_desc['LOC14'] = ""
        self.LOC15 = 0x0000000F
        zz_edict['LOC15'] = self.LOC15
        zz_desc['LOC15'] = ""
        self.LOC16 = 0x00000010
        zz_edict['LOC16'] = self.LOC16
        zz_desc['LOC16'] = ""
        self.LOC17 = 0x00000011
        zz_edict['LOC17'] = self.LOC17
        zz_desc['LOC17'] = ""
        self.LOC18 = 0x00000012
        zz_edict['LOC18'] = self.LOC18
        zz_desc['LOC18'] = ""
        self.LOC19 = 0x00000013
        zz_edict['LOC19'] = self.LOC19
        zz_desc['LOC19'] = ""
        self.LOC20 = 0x00000014
        zz_edict['LOC20'] = self.LOC20
        zz_desc['LOC20'] = ""
        self.LOC21 = 0x00000015
        zz_edict['LOC21'] = self.LOC21
        zz_desc['LOC21'] = ""
        self.LOC22 = 0x00000016
        zz_edict['LOC22'] = self.LOC22
        zz_desc['LOC22'] = ""
        self.LOC23 = 0x00000017
        zz_edict['LOC23'] = self.LOC23
        zz_desc['LOC23'] = ""
        self.LOC24 = 0x00000018
        zz_edict['LOC24'] = self.LOC24
        zz_desc['LOC24'] = ""
        self.LOC25 = 0x00000019
        zz_edict['LOC25'] = self.LOC25
        zz_desc['LOC25'] = ""
        self.LOC26 = 0x0000001A
        zz_edict['LOC26'] = self.LOC26
        zz_desc['LOC26'] = ""
        self.LOC27 = 0x0000001B
        zz_edict['LOC27'] = self.LOC27
        zz_desc['LOC27'] = ""
        self.LOC28 = 0x0000001C
        zz_edict['LOC28'] = self.LOC28
        zz_desc['LOC28'] = ""
        self.LOC29 = 0x0000001D
        zz_edict['LOC29'] = self.LOC29
        zz_desc['LOC29'] = ""
        self.LOC30 = 0x0000001E
        zz_edict['LOC30'] = self.LOC30
        zz_desc['LOC30'] = ""
        self.LOC31 = 0x0000001F
        zz_edict['LOC31'] = self.LOC31
        zz_desc['LOC31'] = ""
        super(RM_Enum_I2C1_ROUTELOC0_SDALOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


class RM_Enum_I2C1_ROUTELOC0_SCLLOC(Base_RM_Enum):
    def __init__(self, label):
        self.__dict__['zz_frozen'] = False
        zz_edict = OrderedDict()
        zz_desc = {}
        self.LOC0 = 0x00000000
        zz_edict['LOC0'] = self.LOC0
        zz_desc['LOC0'] = ""
        self.LOC1 = 0x00000001
        zz_edict['LOC1'] = self.LOC1
        zz_desc['LOC1'] = ""
        self.LOC2 = 0x00000002
        zz_edict['LOC2'] = self.LOC2
        zz_desc['LOC2'] = ""
        self.LOC3 = 0x00000003
        zz_edict['LOC3'] = self.LOC3
        zz_desc['LOC3'] = ""
        self.LOC4 = 0x00000004
        zz_edict['LOC4'] = self.LOC4
        zz_desc['LOC4'] = ""
        self.LOC5 = 0x00000005
        zz_edict['LOC5'] = self.LOC5
        zz_desc['LOC5'] = ""
        self.LOC6 = 0x00000006
        zz_edict['LOC6'] = self.LOC6
        zz_desc['LOC6'] = ""
        self.LOC7 = 0x00000007
        zz_edict['LOC7'] = self.LOC7
        zz_desc['LOC7'] = ""
        self.LOC8 = 0x00000008
        zz_edict['LOC8'] = self.LOC8
        zz_desc['LOC8'] = ""
        self.LOC9 = 0x00000009
        zz_edict['LOC9'] = self.LOC9
        zz_desc['LOC9'] = ""
        self.LOC10 = 0x0000000A
        zz_edict['LOC10'] = self.LOC10
        zz_desc['LOC10'] = ""
        self.LOC11 = 0x0000000B
        zz_edict['LOC11'] = self.LOC11
        zz_desc['LOC11'] = ""
        self.LOC12 = 0x0000000C
        zz_edict['LOC12'] = self.LOC12
        zz_desc['LOC12'] = ""
        self.LOC13 = 0x0000000D
        zz_edict['LOC13'] = self.LOC13
        zz_desc['LOC13'] = ""
        self.LOC14 = 0x0000000E
        zz_edict['LOC14'] = self.LOC14
        zz_desc['LOC14'] = ""
        self.LOC15 = 0x0000000F
        zz_edict['LOC15'] = self.LOC15
        zz_desc['LOC15'] = ""
        self.LOC16 = 0x00000010
        zz_edict['LOC16'] = self.LOC16
        zz_desc['LOC16'] = ""
        self.LOC17 = 0x00000011
        zz_edict['LOC17'] = self.LOC17
        zz_desc['LOC17'] = ""
        self.LOC18 = 0x00000012
        zz_edict['LOC18'] = self.LOC18
        zz_desc['LOC18'] = ""
        self.LOC19 = 0x00000013
        zz_edict['LOC19'] = self.LOC19
        zz_desc['LOC19'] = ""
        self.LOC20 = 0x00000014
        zz_edict['LOC20'] = self.LOC20
        zz_desc['LOC20'] = ""
        self.LOC21 = 0x00000015
        zz_edict['LOC21'] = self.LOC21
        zz_desc['LOC21'] = ""
        self.LOC22 = 0x00000016
        zz_edict['LOC22'] = self.LOC22
        zz_desc['LOC22'] = ""
        self.LOC23 = 0x00000017
        zz_edict['LOC23'] = self.LOC23
        zz_desc['LOC23'] = ""
        self.LOC24 = 0x00000018
        zz_edict['LOC24'] = self.LOC24
        zz_desc['LOC24'] = ""
        self.LOC25 = 0x00000019
        zz_edict['LOC25'] = self.LOC25
        zz_desc['LOC25'] = ""
        self.LOC26 = 0x0000001A
        zz_edict['LOC26'] = self.LOC26
        zz_desc['LOC26'] = ""
        self.LOC27 = 0x0000001B
        zz_edict['LOC27'] = self.LOC27
        zz_desc['LOC27'] = ""
        self.LOC28 = 0x0000001C
        zz_edict['LOC28'] = self.LOC28
        zz_desc['LOC28'] = ""
        self.LOC29 = 0x0000001D
        zz_edict['LOC29'] = self.LOC29
        zz_desc['LOC29'] = ""
        self.LOC30 = 0x0000001E
        zz_edict['LOC30'] = self.LOC30
        zz_desc['LOC30'] = ""
        self.LOC31 = 0x0000001F
        zz_edict['LOC31'] = self.LOC31
        zz_desc['LOC31'] = ""
        super(RM_Enum_I2C1_ROUTELOC0_SCLLOC, self).__init__(
            label,
            zz_edict,
            zz_desc)
        self.__dict__['zz_frozen'] = True


