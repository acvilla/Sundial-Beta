

__all__ = [ 'RegisterMap_IO', 'GetFieldValue', 'SetFieldValue' ]

def GetFieldValue(regValue, lsb, fsize):
    msb = lsb + fsize
    mask = (pow(2, msb) - 1) & ~(pow(2, lsb) - 1)
    return (regValue & mask) >> lsb

def SetFieldValue(regValue, lsb, fsize, fieldValue):
    msb = lsb + fsize
    mask = ~((pow(2, msb) - 1) & ~(pow(2, lsb) - 1))
    return (regValue & mask) | (fieldValue << lsb)


class RegisterMap_IO(object):

    def __init__(self, Reader, Writer):
        # register the reader and writer functions
        self._ReadAddress = Reader
        self._WriteAddress = Writer
    def _read(self, address):
        #print("Reading address {0:#010x}".format(address))
        return self._ReadAddress(address)
    def _write(self, address, value):
        #print("Writing '{:#010x}' to address {:#010x}".format(value, address))
        return self._WriteAddress(address, value)
    def readRegister(self, baseAddr, reg):
        regOffset = int(reg.addressOffset, 16)
        if reg.access is None:
            return self._read(baseAddr + regOffset)
        elif reg.access in ('read-only', 'read-write', 'read-writeOnce'):
            return self._read(baseAddr + regOffset)
        else:
            raise AttributeError("Read Failure: Register '{}' access is '{}'".format(reg.name, reg.access))
    def readRegisterField(self, baseAddr, reg, field):
        regOffset = int(reg.addressOffset, 16)
        bitOffset = int(field.bitOffset)
        bitWidth = int(field.bitWidth)
        if field.access is None:
            return GetFieldValue(self._read(baseAddr + regOffset), bitOffset, bitWidth)
        elif field.access in ('read-only', 'read-write', 'read-writeOnce'):
            return GetFieldValue(self._read(baseAddr + regOffset), bitOffset, bitWidth)
        else:
            raise AttributeError("Read Failure: Register '{}:{}' access is '{}'".format(reg.name, field.name,
                                                                                        field.access))
    def writeRegister(self, baseAddr, reg, regValue):
        regOffset = int(reg.addressOffset, 16)
        if reg.access is None:
            return self._write(baseAddr + regOffset, regValue)
        elif reg.access in ('write-only', 'read-write', 'writeOnce', 'read-writeOnce'):
            return self._write(baseAddr + regOffset, regValue)
        else:
            raise AttributeError("Write Failure: Register '{}' access is '{}'".format(reg.name, reg.access))
    def writeRegisterField(self, baseAddr, reg, field, fieldValue):
        regOffset = int(reg.addressOffset, 16)
        bitOffset = int(field.bitOffset)
        bitWidth = int(field.bitWidth)
        if field.access is None:
            regValue = self._read(baseAddr + regOffset)
            return self._write(baseAddr + regOffset, SetFieldValue(regValue, bitOffset, bitWidth, fieldValue))
        elif field.access in ('read-write', 'read-writeOnce'):
            regValue = self._read(baseAddr + regOffset)
            return self._write(baseAddr + regOffset, SetFieldValue(regValue, bitOffset, bitWidth, fieldValue))
        elif field.access in ('write-only', 'writeOnce'):
            # TODO: Test this case!
            regValue = 0
            return self._write(baseAddr + regOffset, SetFieldValue(regValue, bitOffset, bitWidth, fieldValue))
        else:
            raise AttributeError("Write Failure: Register '{}:{}' access is '{}'".format(reg.name, field.name,
                                                                                        field.access))
