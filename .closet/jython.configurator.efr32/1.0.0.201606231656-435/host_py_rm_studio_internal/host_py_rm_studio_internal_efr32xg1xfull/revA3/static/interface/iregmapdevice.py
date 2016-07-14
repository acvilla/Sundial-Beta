
"""
Device
------
The top-level device class subclasses :class:`~Base_RM_Device`, which
implements this interface.

  .. autoclass:: IRegMapDevice
     :members:
     :show-inheritance:
     :inherited-members:

"""


__all__ = ['IRegMapDevice']

from abc import ABCMeta, abstractmethod, abstractproperty

class IRegMapDevice(object):
    """
    The interface for the dut.rm device component. This component will also
    contain a list of peripheral name attributes in uppercase.
    """
    __metaclass__ = ABCMeta

    # SVD Info Property

    @abstractproperty
    def svdInfo(self):
        """
        :rtype: :class:`pyrmsvd.static.common.svdinfo.RM_SVD_Info`
        :return: An instance of the RM_SVD_Info with filename, md5sum, and
                 aliased list for registers, fields, and enums.
        """
        pass

    # Name Access Methods

    @abstractmethod
    def addressToName(self, address):
        """
        Returns the register string for the given address.

        :type  address: ``int`` or ``long``
        :param address: The register address
        :rtype: ``str``
        :return: The register name in 'PERIPHERAL.REGISTER' format
        :raises: RegMapAddressError
        """
        pass

    @abstractmethod
    def nameToAddress(self, name):
        """
        Get the address of the register or register field.

        :type  name: ``str``
        :param name: The 'PERIPHERAL.REGISTER' or 'PERIPHERAL.REGISTER.FIELD' name
        :rtype: ``long``
        :return: The address of the register
        :raises: RegMapNameError
        """
        pass

    @abstractmethod
    def writeByName(self, name, value):
        """
        Write the value to register or register field.

        :type  name: ``str``
        :param name: The 'PERIPHERAL.REGISTER' or 'PERIPHERAL.REGISTER.FIELD' name
        :type  value: ``int`` or ``long``
        :param value: The value of the register or register field
        :raises: RegMapNameError
        """
        pass

    @abstractmethod
    def readByName(self, name):
        """
        Return the value for register or register field.

        :type  name: ``str``
        :param name: The 'PERIPHERAL.REGISTER' or 'PERIPHERAL.REGISTER.FIELD' name
        :rtype: ``long``
        :return: The value of the register or register field
        :raises: RegMapNameError
        """
        pass

    @abstractmethod
    def getObjectByName(self, name):
        """
        A helper function used to get register or register field object.

        :type  name: ``str``
        :param name: The 'PERIPHERAL.REGISTER' or 'PERIPHERAL.REGISTER.FIELD' name
        :rtype: :class:`Base_RM_Register` or :class:`Base_RM_Field` instance
        :return: The register or register field object
        :raises: RegMapNameError
        """
        pass

    @abstractmethod
    def getRegisterNameFromFieldName(self, name):
        """
        A helper function use to get the 'PERIPHERAL.REGISTER' name from
        a 'PERIPHERAL.REGISTER.FIELD' name. Will accept a 'PERIPHERAL.REGISTER'
        name without complaint.

        :type  name: ``str``
        :param name: The 'PERIPHERAL.REGISTER' or 'PERIPHERAL.REGISTER.FIELD' name
        :rtype: ``str``
        :return: The 'PERIPHERAL.REGISTER' name
        """
        pass

    @abstractmethod
    def isReadable(self, name):
        """
        A helper function use to determine if 'PERIPHERAL.REGISTER' or
        'PERIPHERAL.REGISTER.FIELD' name is readable.

        :type  name: ``str``
        :param name: The 'PERIPHERAL.REGISTER' or 'PERIPHERAL.REGISTER.FIELD' name
        :rtype: ``bool``
        :return: ``True`` if readable, else ``False``
        :raises: RegMapNameError
        """
        pass

    @abstractmethod
    def isWriteable(self, name):
        """
        A helper function use to determine if 'PERIPHERAL.REGISTER' or
        'PERIPHERAL.REGISTER.FIELD' name is writeable.

        :type  name: ``str``
        :param name: The 'PERIPHERAL.REGISTER' or 'PERIPHERAL.REGISTER.FIELD' name
        :rtype: ``bool``
        :return: ``True`` if writeable, else ``False``
        :raises: RegMapNameError
        """
        pass

    @abstractmethod
    def forceRegister(self, name, value):
        """
        Used to ignore the register access when running in simulation mode,
        where the connection is offline. Allows the user to assign a default
        value to a read-only register.

        :type  name: ``str``
        :param name:  The 'PERIPHERAL.REGISTER' name
        :type  value: ``int`` or ``long``
        :param value: The value to assign to the register
        :raises: RegMapAccessError, RegMapNameError
        """
        pass

    # Accessed Flag Methods

    @abstractmethod
    def clearAccessedFlags(self):
        """
        Clear the accessed flag for all registers in all peripherals, recursively.
        Note that the accessed flag is set whenever the register is written.
        """
        pass

    @abstractmethod
    def setAccessedFlags(self):
        """
        Set the accessed flag for all registers in all peripherals, recursively.
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

    # Data Dictionary Methods

    @abstractmethod
    def writeData(self, dataDict):
        """
        Write register or register field item value from dictionary to part.

        :type  dataDict: ``dict`` of ``str`` : ``int`` or ``long`` item
        :param dataDict: The items of 'PERIPHERAL.REGISTER' or \
                         'PERIPHERAL.REGISTER.FIELD' name key and value
        :raises: RegMapNameError, RegMapValueError
        """
        pass

    @abstractmethod
    def readData(self, dataDict):
        """
        Read register or register field items from part and assign
        values in dictionary.

        :type  dataDict: ``dict`` of ``str`` : ``long`` item
        :param dataDict: The items of 'PERIPHERAL.REGISTER' or \
                         'PERIPHERAL.REGISTER.FIELD' name key and value
        :raises: RegMapNameError
        """
        pass

    @abstractmethod
    def verifyData(self, expectedDict):
        """
        Read register or register field items from part and compare against
        values in dictionary. Create an item in a difference dictionary for a
        mismatch.

        :type  expectedDict: ``dict`` of ``str`` = ``long`` item
        :param expectedDict: The items of 'PERIPHERAL.REGISTER' or \
                            'PERIPHERAL.REGISTER.FIELD' name key and value
        :rtype: ``dict`` of ``str`` : ``long``
        :return: A dictionary with register or register field keys and \
                actual values read. An empty dictionary is returned if no \
                differences are detected.
        :raises: RegMapNameError
        """
        pass

    @abstractmethod
    def readAccessedRegisters(self):
        """
        Read values of all registers with accessed flag set and store in a
        return dictionary.

        :rtype: ``dict`` of ``str`` : ``long``
        :return: A dictionary with 'PERIPHERAL.REGISTER' name key and actual \
                 values read. An empty dictionary is returned if no accessed \
                 flags are set.
        """
        pass

    @abstractmethod
    def readAccessedFields(self):
        """
        Read values of all register fields with accessed flag set and store
        in a return dictionary.

        :rtype: ``dict`` of ``str`` : ``long``
        :return: A dictionary with 'PERIPHERAL.REGISTER.FIELD' name key and \
                 actual values read. An empty dictionary is returned if no \
                 accessed flags are set.
        """
        pass

    # Dump Methods

    @abstractmethod
    def buildRegFilterList(self, filename, listname='regFilterList'):
        """
        Create a python source filename containing a default list of all readable
        register names in 'PERIPHERAL.REGISTER' format. This provides a
        starting point to cull non-essential registers. The resulting list can be
        imported from the python source filename for use in the dump() method.

        .. code-block:: py

            # example filter listing

            regFilterList = [
             'MODEM.AFC',
             'MODEM.AFCADJLIM',
             'MODEM.AFCADJRX',
             'MODEM.AFCADJTX',
             'MODEM.CF',
             'MODEM.CMD',
             'MODEM.CTRL0',
             'MODEM.CTRL1',
             'MODEM.CTRL2',
             'MODEM.CTRL3',
             'MODEM.CTRL4',
             'MODEM.CTRL5',
             'MODEM.DCCOMP',
             'MODEM.DCCOMPFILTINIT',
             'MODEM.DCESTI',
             'MODEM.DSSS0',
             'MODEM.FREQOFFEST',
             'MODEM.IEN',
             'MODEM.IF',
             'MODEM.MIXCTRL',
             'MODEM.MODINDEX',
             'MODEM.PRE',
            ]

        :type  filename: ``str``
        :param filename: Path and filename for a filter list (i.e. 'regfilter.py')
        :type  listname: ``str``
        :param listname: The name to use in the python source file
        :rtype: ``list`` of ``str``
        :return: The list of register names that were written to the python source file
        """

    @abstractmethod
    def dump(self, filename, regFilterList=None):
        """
        Read values of all registers and store in a return dictionary. This
        dictionary is dumped to file name, with 'PERIPHERAL.REGISTER' name
        keys and values read from the part. For each register value, the
        formatted field value is listed in source comments with any
        corresponding enum name and its description text. This dictionary
        is returned for immediate use. The dumped Python source file can
        be used in a diff operation to compare settings. Any previous file
        is overwritten.

        .. warning:: If ``regFilterList`` is ``None``, then **ALL** readable
            registers are dumped. Reading some auto-increment registers can
            cause side effects to a running program.

        .. code-block:: py

            # HOWTO: Dump a dictionary of register values for diffing

            # 1. Build a register filter list
            rm.buildRegFilterList('regfilter.py')
            # 2. Open resulting regfilter.py, cull list, and save file
            # 3. Update code to import regFilterList from new regfilter module
            from regfilter import regFilterList
            # 4. Call the dump() method with the register filter list
            valueDict = rm.dump('my_rm_dump.py', regFilterList)
            # 5. Open my_rm_dump.py source file for detailed field dissection
            #     in source comment blocks
            # 6. The dumped settings can be loaded via rm.writeData() method
            #    so the dump can be shared to reproduce an issue

        :type  filename: ``str``
        :param filename: A python source file to dump the value dictionary
        :type  regFilterList: ``list`` of ``str``
        :param regFilterList: A list of 'PERIPHERAL.REGISTER' names to dump
        :rtype: ``dict`` of ``str`` : ``long``
        :return: A dictionary with 'PERIPHERAL.REGISTER' name key and actual \
                 values read.

        """
        pass

