"""
Peripheral
----------
All rm.<PERIPHERAL> components subclass :class:`~Base_RM_Peripheral`, which
implements this interface.

  .. autoclass:: IRegMapPeripheral
     :members:
     :show-inheritance:
     :inherited-members:

"""


__all__ = ['IRegMapPeripheral']

from abc import ABCMeta, abstractmethod

class IRegMapPeripheral(object):
    """
    The interface for the dut.rm.<PERIPHERAL> component. This component
    will also contain a list of register name attributes in uppercase.
    """
    __metaclass__ = ABCMeta

    # Accessed Flag Methods

    @abstractmethod
    def clearAccessedFlags(self):
        """
        Clear the accessed flag for all registers in this peripheral.
        Note that the accessed flag is set whenever the register is written.
        """
        pass

    @abstractmethod
    def setAccessedFlags(self):
        """
        Set the accessed flag for all registers in this peripheral.
        Note that the accessed flag is set whenever the register is written.
        """
        pass

    @abstractmethod
    def getAccessedRegisterNames(self):
        """
        Return a list of 'PERIPHERAL.REGISTER' names with accessed flag set.

        :rtype: ``list`` of ``str``
        :return: A list of register names
        """
        pass

    @abstractmethod
    def getAccessedFieldNames(self):
        """
        Return a list of 'PERIPHERAL.REGISTER.FIELD' names with accessed flag set.

        :rtype: ``list`` of ``str``
        :return: A list of register field names
        """
        pass

    @abstractmethod
    def assignRegDefault(self):
        """
        Assign all registers in this peripheral to default values from the
        CMSIS SVD XML.
        """
        pass

    # Internal Only

    @abstractmethod
    def getAddressNameMap(self, addrNameDict):
        """
        Update passed dictionary with address key and register name value
        for all registers in this peripheral.

        .. note:: This is an internal function used by the device container.
                  Do not call directly.

        :type  addrNameDict: ``dict`` of ``long`` : ``str`` item
        :param addrNameDict: The items of address key and 'PERIPHERAL.REGISTER'
                             value
        """
        pass

    @abstractmethod
    def buildRegFilterList(self, outFH, filterList):
        """
        Query peripheral for all readable registers, then store 'PERIPHERAL.REGISTER'
        names in both the output file and append to filterList.

        .. note:: This is an internal function used by the device container.
                  Do not call directly.

        :type  outFH: File Handle
        :param outFH: A file handle to dump the register names with formatting
        :type  filterList: ``list`` of ``str``
        :param filterList: The list to append 'PERIPHERAL.REGISTER' names
        """
        pass

    @abstractmethod
    def dump(self, outFH, valueDict):
        """
        Read values of all registers and store in valueDict. The file
        handle is passed to internal functions to do the source dictionary
        output.

        .. note:: This is an internal function used by the device container.
                  Do not call directly.

        :type  outFH: File Handle
        :param outFH: A file handle to dump the value dictionary with formatting
        :type  valueDict: ``dict`` of ``str`` : ``long`` item
        :param valueDict: A dictionary to collect 'PERIPHERAL.REGISTER' name
                          with value
        """
        pass
