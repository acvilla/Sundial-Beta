
"""
Access Manager
^^^^^^^^^^^^^^
This package can raise a number of exceptions from the top-level device class.

  .. autoexception:: AccessMgrIoException

  .. autoclass:: Offline_AccessManager
     :members:
     :show-inheritance:
     :inherited-members:

"""

from collections import defaultdict

__all__ = [ 'AccessMgrIoException', 'Offline_AccessManager' ]


class AccessMgrIoException(Exception):
    """
    Indicates an error occurred during access of the offline
    register map.
    """
    pass


class Offline_AccessManager(object):
    """
    This class provides the offline register map dictionary for the
    offline access mode.
    """

    def __init__(self, label):
        """
        Store the label and create the offline register dictionary.

        :type  label: ``str``
        :param label: The DUT label to use in the logger
        """
        assert isinstance(label, basestring)
        self._label = label
        # will default to a value of zero
        self._sim_regs = defaultdict(long)

    def ReadRegister(self, address):
        """
        Read the simulated 32-bit memory mapped value at given address.

        :type  address: ``int`` or ``long``
        :param address: The offline 32-bit memory mapped register address.
        :rtype: ``long``
        :return: The simulated register value
        """
        # TODO: Default to SVD XML reset value if the address has not been written
        return self._sim_regs[address]

    def WriteRegister(self, address, data):
        """
        Write the 32-bit data to the memory mapped 32-bit register at given address.

        :type  address: ``int`` or ``long``
        :param address: The offline memory mapped register address
        :type  data: ``int`` or ``long``
        :param data: The 32-bit data
        :rtype: ``long``
        :return: 0 on success
        :raises: AccessMgrIoException
        """
        self._sim_regs[address] = data
