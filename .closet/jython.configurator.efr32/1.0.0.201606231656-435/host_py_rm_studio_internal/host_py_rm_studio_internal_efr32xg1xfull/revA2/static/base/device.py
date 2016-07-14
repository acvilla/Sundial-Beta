
__all__ = [ 'Base_RM_Device' ]

from collections import OrderedDict

from .. interface import IRegMapDevice
from .. common import Offline_AccessManager, \
    RegisterMapInterface, \
    RegMapAccessError, \
    RegMapNameError, \
    RegMapAddressError, \
    RegMapValueError
from register import Base_RM_Register

class Base_RM_Device(IRegMapDevice):

    def __init__(self, rmio, label, name, svd_info):
        self.__dict__['zz_frozen'] = False
        self.zz_name = name
        self.zz_label = label
        self.zz_svd_info = svd_info
        if rmio is None:
            self.offline = True
            accessMgr = Offline_AccessManager(self.zz_label)
            self.zz_rmio = RegisterMapInterface(accessMgr.ReadRegister,
                                                accessMgr.WriteRegister,
                                                simulated=True)
        else:
            self.offline = False
            self.zz_rmio = rmio
        self.zz_pdict = OrderedDict()
        self.zz_reg_addr_to_name = {}

    def __setattr__(self, name, value):
        if self.__dict__['zz_frozen']:
            if name not in self.zz_pdict:
                raise AttributeError("ERROR: Invalid peripheral '{}'\n".format(name))
            else:
                raise AttributeError("ERROR: Unable to set '{}' to '{}'\n".format(name, value))
        else:
            self.__dict__[name] = value

    def __repr__(self):
        out = "{} ({} peripherals)\n".format(self.zz_name, len(self.zz_pdict))
        for key in sorted(self.zz_pdict.iterkeys()):
            out += "  {}\n".format(key)
        return out

    @property
    def svdInfo(self):
        return self.zz_svd_info

    def addressToName(self, address):
        if not isinstance(address, (int, long)):
            raise RegMapAddressError("Invalid address '{}'".format(address))
        try:
            return self.zz_reg_addr_to_name[address]
        except KeyError:
            raise RegMapAddressError("No register found for address {:#010x}".format(address))

    def nameToAddress(self, name):
        reg_or_field = self.getObjectByName(name)
        return reg_or_field.baseAddress + reg_or_field.addressOffset

    def writeByName(self, name, value):
        if value is None:
            raise RegMapValueError("None value for '{}'".format(name))
        self.getObjectByName(name).io = value

    def readByName(self, name):
        return self.getObjectByName(name).io

    def getObjectByName(self, name):
        if len(name.split('.')) == 2:
            per_name, reg_name = name.split('.')
            try:
                return self.zz_pdict[per_name].zz_rdict[reg_name]
            except KeyError:
                raise RegMapNameError("Invalid register name '{}'".format(name))
        elif len(name.split('.')) == 3:
            per_name, reg_name, field_name = name.split('.')
            try:
                return self.zz_pdict[per_name].zz_rdict[reg_name].zz_fdict[field_name]
            except KeyError:
                raise RegMapNameError("Invalid register field name '{}'".format(name))
        else:
            raise RegMapNameError("Invalid name '{}', must be PER.REG or PER.REG.FIELD".format(name))

    def isReadable(self, name):
        obj = self.getObjectByName(name)
        return obj.isReadable()

    def isWriteable(self, name):
        obj = self.getObjectByName(name)
        return obj.isWriteable()

    def getRegisterNameFromFieldName(self, name):
        periods = len(name.split('.'))
        if periods == 2 or periods == 3:
            return '.'.join(name.split('.')[:2])
        else:
            raise RegMapNameError("Invalid name '{}', must be PER.REG or PER.REG.FIELD".format(name))

    def forceRegister(self, name, value):
        if not self.offline:
            raise RegMapAccessError("Cannot directly assign within a live connection")
        reg = self.getObjectByName(name)
        if not isinstance(reg, Base_RM_Register):
            raise RegMapNameError("Name must be register name")
        self.zz_rmio.forceRegister(reg, value)

    def clearAccessedFlags(self):
        for key in sorted(self.zz_pdict.iterkeys()):
            self.zz_pdict[key].clearAccessedFlags()

    def setAccessedFlags(self):
        for key in sorted(self.zz_pdict.iterkeys()):
            self.zz_pdict[key].setAccessedFlags()

    def getAccessedRegisterNames(self):
        nameList = []
        for key in sorted(self.zz_pdict.iterkeys()):
            nameList.extend(self.zz_pdict[key].getAccessedRegisterNames())
        return nameList

    def getAccessedFieldNames(self):
        nameList = []
        for key in sorted(self.zz_pdict.iterkeys()):
            nameList.extend(self.zz_pdict[key].getAccessedFieldNames())
        return nameList

    def writeData(self, dataDict):
        for key in dataDict:
            self.writeByName(key, dataDict[key])

    def readData(self, dataDict):
        for key in dataDict:
            dataDict[key] = self.readByName(key)

    def verifyData(self, expectedDict):
        diffDict = {}
        for key in expectedDict:
            actualValue= self.readByName(key)
            if actualValue != expectedDict[key]:
                diffDict[key] = actualValue
        return diffDict

    def readAccessedRegisters(self):
        valueDict = {}
        for key in self.getAccessedRegisterNames():
            valueDict[key] = self.readByName(key)
        return valueDict

    def readAccessedFields(self):
        valueDict = {}
        for key in self.getAccessedFieldNames():
            valueDict[key] = self.readByName(key)
        return valueDict

    def buildRegFilterList(self, filename, listname='regFilterList'):
        filterList = []
        with open(filename, 'w') as outFH:
            outFH.write("\n# Register Map Register Name Filter List\n")
            outFH.write("\n{} = [\n".format(listname))
            for key in sorted(self.zz_pdict.iterkeys()):
                self.zz_pdict[key].buildRegFilterList(outFH, filterList)
            outFH.write("]\n\n")
        return filterList

    def dump(self, filename, regFilterList=None):
        valueDict = {}
        with open(filename, 'w') as outFH:
            outFH.write("\nREGISTER_DUMP = {\n")
            if regFilterList:
                for name in sorted(regFilterList):
                    obj = self.getObjectByName(name)
                    if isinstance(obj, Base_RM_Register):
                        obj.dump(outFH, valueDict)
                    else:
                        outFH.write("    # Skipping invalid reg name '{}'\n".format(name))
            else:
                for key in sorted(self.zz_pdict.iterkeys()):
                    self.zz_pdict[key].dump(outFH, valueDict)
            outFH.write("}\n\n")
        return valueDict
