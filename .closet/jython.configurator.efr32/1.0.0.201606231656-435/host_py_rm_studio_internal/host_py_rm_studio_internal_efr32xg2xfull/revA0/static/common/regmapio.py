
"""
Register Map I/O
^^^^^^^^^^^^^^^^
The register map I/O occurs via the :class:`pyrmsvd.static.common.regmapio.RegisterMapInterface`
instance, which is registered in the top-level device class..

  .. autoclass:: RegisterMapInterface
     :members:
     :show-inheritance:
     :inherited-members:

"""

__all__ = [
    'GetFieldValue',
    'SetFieldValue',
    'RegisterMapInterface'
]


from .. interface import IRegMapIO
from .. common import RegMapAccessError


def GetFieldValue(regValue, lsb, fsize):
    """
    An internal utility function to parse a field value from a register value.

    :type  regValue: ``int`` or ``long``
    :param regValue: The value of the register to parse
    :type  lsb: ``int``
    :param lsb: The least significant bit of the field
    :type  fsize: ``int``
    :param fsize: The size of the field in bits
    :rtype: ``int`` or ``long``
    :return: The field value
    """
    msb = lsb + fsize
    mask = (pow(2, msb) - 1) & ~(pow(2, lsb) - 1)
    return (regValue & mask) >> lsb


def SetFieldValue(regValue, lsb, fsize, fieldValue):
    """
    An internal utility function to assign a field value to a register value.

    :type  regValue: ``int`` or ``long``
    :param regValue: The value of the register to parse
    :type  lsb: ``int``
    :param lsb: The least significant bit of the field
    :type  fsize: ``int``
    :param fsize: The size of the field in bits
    :type  fieldValue: ``int``
    :param fieldValue: The new field value
    :rtype: ``int`` or ``long``
    :return: The new register value
    """
    msb = lsb + fsize
    mask = ~((pow(2, msb) - 1) & ~(pow(2, lsb) - 1))
    return (regValue & mask) | (fieldValue << lsb)


class RegisterMapInterface(IRegMapIO):
    """
    This class defines the register map I/O instance (``rmIO``) that
    is passed to the top-level device class.

    It implements the :class:`pyrmsvd.static.interface.iregmapio.IRegMapIO` interface.
    """

    def __init__(self, Reader, Writer, simulated=False):
        """
        Register the reader and writer functions that the top-level
        device class will use for the peripheral register and register
        field 'io' properties.

        :type Reader: T(<address>)
        :param Reader: The read address function pointer
        :type  Writer: T(<address, value>)
        :param Writer: The write address function pointer
        :type simulated: ``bool``
        :param simulated: Indicates the interface is offline stand-alone \
                          register map
        """
        # register the reader and writer functions
        self._ReadAddress = Reader
        self._WriteAddress = Writer
        self.simulated = simulated

    def _read(self, address):
        #print("Reading address {0:#010x}".format(address))
        return self._ReadAddress(address)

    def _write(self, address, value):
        #print("Writing '{:#010x}' to address {:#010x}".format(value, address))
        return self._WriteAddress(address, value)

    def assignRegisterDefault(self, reg):
        if not self.simulated:
            raise RegMapAccessError("Unable to assign default in live connection")
        return self._write(reg.baseAddress + reg.addressOffset, reg.resetValue)

    def forceRegister(self, reg, value):
        if not self.simulated:
            raise RegMapAccessError("Unable to force value in live connection")
        return self._write(reg.baseAddress + reg.addressOffset, value)

    def readRegister(self, reg):
        if reg.access in [None, 'read-only', 'read-write', 'read-writeOnce']:
            return self._read(reg.baseAddress + reg.addressOffset)
        else:
            raise RegMapAccessError("Read Failure: Register '{}' access is '{}'".format(reg.name, reg.access))

    def readRegisterField(self, reg, field):
        if field.access in [None, 'read-only', 'read-write', 'read-writeOnce']:
            return GetFieldValue(self._read(reg.baseAddress + reg.addressOffset),
                                            field.bitOffset, field.bitWidth)
        else:
            raise RegMapAccessError("Read Failure: Register '{}:{}' access is '{}'".format(reg.name, field.name,
                                                                                        field.access))
    def writeRegister(self, reg, regValue):
        if reg.access in [None, 'write-only', 'read-write', 'writeOnce', 'read-writeOnce']:
            return self._write(reg.baseAddress + reg.addressOffset, regValue)
        else:
            raise RegMapAccessError("Write Failure: Register '{}' access is '{}'".format(reg.name, reg.access))

    def writeRegisterField(self, reg, field, fieldValue):
        if field.access in [None, 'read-write', 'read-writeOnce']:
            regValue = self._read(reg.baseAddress + reg.addressOffset)
            return self._write(reg.baseAddress + reg.addressOffset,
                               SetFieldValue(regValue, field.bitOffset, field.bitWidth, fieldValue))
        elif field.access in ('write-only', 'writeOnce'):
            # TODO: Test this case!
            regValue = 0
            return self._write(reg.baseAddress + reg.addressOffset,
                               SetFieldValue(regValue, field.bitOffset, field.bitWidth, fieldValue))
        else:
            raise RegMapAccessError("Write Failure: Register '{}:{}' access is '{}'".format(reg.name, field.name,
                                                                                        field.access))
