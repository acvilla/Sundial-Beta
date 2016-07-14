
__all__ = [ 'Base_RM_Field' ]

from .. interface import IRegMapField
from .. common import GetFieldValue


class Base_RM_Field(IRegMapField):
    def __init__(self, register, name, fullname, access, description, bitOffset, bitWidth, enum=None):
        self.__dict__['zz_frozen'] = False
        self.zz_accessed_flag = False
        self.zz_reg = register
        self.baseAddress = self.zz_reg.baseAddress
        self.addressOffset = self.zz_reg.addressOffset
        self.name = name
        self.fullname = fullname
        self.access = access
        self.description = description
        self.bitOffset = bitOffset
        self.bitWidth = bitWidth
        self.enum = enum

    def __setattr__(self, name, value):
        if self.__dict__['zz_frozen']:
            if name == '_setio':
                self.setAccessedFlag()
                self.zz_reg.setAccessedFlag()
                self.zz_reg.zz_rmio.writeRegisterField(self.zz_reg, self, value)
            elif name == 'io':
                self.setAccessedFlag()
                self.zz_reg.setAccessedFlag()
                self.zz_reg.zz_rmio.writeRegisterField(self.zz_reg, self, value)
            else:
                raise AttributeError("FATAL ERROR: Unable to set '{}' to '{}'".format(name, value))
        else:
            self.__dict__[name] = value

    def __repr__(self):
        flagStr = "**" if self.getAccessedFlag() else ""
        enumStr = ' ENUMERATED' if self.enum is not None else ''
        out = "    {:#010x} {}[{}] contains field {}{}: {} <{}>{}\n".format(self.baseAddress + self.addressOffset,
                                                                          self.zz_reg.name, self.getSliceStr(),
                                                                          self.name, flagStr,
                                                                          self.description, self.access, enumStr)
        return out

    def _getio(self):
        return self.zz_reg.zz_rmio.readRegisterField(self.zz_reg, self)

    def _setio(self, value):
        self.setAccessedFlag()
        self.zz_reg.setAccessedFlag()
        self.zz_reg.zz_rmio.writeRegisterField(self.zz_reg, self, value)

    io = property(_getio, _setio)

    def isReadable(self):
        return self.access in [None, 'read-only', 'read-write', 'read-writeOnce']

    def isWriteable(self):
        return self.access in [None, 'write-only', 'read-write', 'writeOnce', 'read-writeOnce']

    def clearAccessedFlag(self):
        self.__dict__['zz_accessed_flag'] = False

    def setAccessedFlag(self):
        self.__dict__['zz_accessed_flag'] = True

    def getAccessedFlag(self):
        return self.__dict__['zz_accessed_flag']

    def getSliceStr(self):
        lsb = self.bitOffset
        fsize = self.bitWidth
        return "{}:{}".format(lsb+fsize-1, lsb) if fsize > 1 else "{}".format(lsb)

    def dump(self, regValue, fieldCommentList):
        sliceStr = self.getSliceStr()
        fieldValue = GetFieldValue(regValue, self.bitOffset, self.bitWidth)
        if self.enum:
            fieldValueStr = "{:#x} (enum {}: {})".format(fieldValue,
                                                         self.enum.getNameByValue(fieldValue),
                                                         self.enum.getDescByValue(fieldValue))
        else:
            fieldValueStr = "{:#x}".format(fieldValue)
        line  = "        # [{}] {}: {}\n".format(sliceStr, self.name, fieldValueStr)
        fieldCommentList.append([int(sliceStr.split(':')[0]), self.fullname, line])
