
"""
Register Map I/O
^^^^^^^^^^^^^^^^
The top-level device class can receive a
:class:`pyrmsvd.static.common.regmapio.RegisterMapInterface` instance,
which implements this interface. This ensures a consistent address read/write
API for the low-level access to the part, whether it is a live J-Link connection
or a simulated offline dictionary.

  .. autoclass:: IRegMapIO
     :members:
     :show-inheritance:
     :inherited-members:

"""


__all__ = ['IRegMapIO']

from abc import ABCMeta, abstractmethod

class IRegMapIO(object):
    """
    The interface for low-level part access.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def _read(self, address):
        """
        Low-level raw read function. No access checking performed.

        :type  address: ``int`` or ``long``
        :param address: The read address
        :rtype: ``long``
        :return: The 32-bit value at the address
        """
        pass

    @abstractmethod
    def _write(self, address, value):
        """
        Low-level raw write function. No access checking performed.

        :type  address: ``int`` or ``long``
        :param address: The write address
        :type  value: ``int`` or ``long``
        :param value: The value to write
        """
        pass

    @abstractmethod
    def assignRegisterDefault(self, reg):
        """
        Assign reset value of the register. Raises error if not writeable.

        :type  reg: :class:`~Base_RM_Register`
        :param reg: The register object
        :raises: RegMapAccessError
        """
        pass

    @abstractmethod
    def forceRegister(self, reg, value):
        """
        Force the value of the register, regardless of the access type.
        Only allowed for simulated connections. Raises error for live
        connection.

        :type  reg: :class:`~Base_RM_Register`
        :param reg: The register object
        :type  value: ``int`` or ``long``
        :param value: The register value
        :raises: RegMapAccessError
        """
        pass

    @abstractmethod
    def readRegister(self, reg):
        """
        Read the register. Raises error if not readable.

        :type  reg: :class:`~Base_RM_Register`
        :param reg: The register object
        :rtype: ``long``
        :return: The value of the register
        :raises: RegMapAccessError
        """
        pass

    @abstractmethod
    def readRegisterField(self, reg, field):
        """
        Read the register's field. Raises error if not readable.

        :type  reg: :class:`~Base_RM_Register`
        :param reg: The register object
        :type  field: :class:`~Base_RM_Field`
        :param field: The register's field object
        :rtype: ``long``
        :return: The value of the register's field
        :raises: RegMapAccessError
        """
        pass

    @abstractmethod
    def writeRegister(self, reg, regValue):
        """
        Write value to the register. Raises error if not writeable.

        :type  reg: :class:`~Base_RM_Register`
        :param reg: The register object
        :type  regValue: ``int`` or ``long``
        :param regValue: The register value
        :raises: RegMapAccessError
        """
        pass

    @abstractmethod
    def writeRegisterField(self, reg, field, fieldValue):
        """
        Write value the register's field. Raises error if not writeable.

        :type  reg: :class:`~Base_RM_Register`
        :param reg: The register object
        :type  field: :class:`~Base_RM_Field`
        :param field: The register's field object
        :type  fieldValue: ``int`` or ``long``
        :param fieldValue: The register's field value
        :raises: RegMapAccessError
        """
        pass
