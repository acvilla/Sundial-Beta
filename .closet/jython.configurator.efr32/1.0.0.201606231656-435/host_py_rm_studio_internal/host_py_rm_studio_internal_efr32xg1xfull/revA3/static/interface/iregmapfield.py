
"""
Field
-----
All rm.<PERIPHERAL>.<REGISTER>.<FIELD> components subclass :class:`~Base_RM_Field`,
which implements this interface.

  .. autoclass:: IRegMapField
     :members:
     :show-inheritance:
     :inherited-members:

"""


__all__ = ['IRegMapField']

from abc import ABCMeta, abstractmethod, abstractproperty

class IRegMapField(object):
    """
    The interface for the dut.rm.<PERIPHERAL>.<REGISTER>.<FIELD> component. This
    component will also contain an enum attribute.
    """
    __metaclass__ = ABCMeta

    def _getio(self):
        """
        This is the io property getter to interact with the part's register
        field, which may be a live instance via J-Link or a simulated dictionary
        for offline use case. Use via the dut.<PERIPHERAL>.<REGISTER>.<FIELD>.io
        property to read the register field value.

        :rtype: ``long``
        :return: The field value.
        """
        pass

    def _setio(self, value):
        """
        This is the io property setter to interact with the part's register
        field, which may be a live instance via J-Link or a simulated dictionary
        for offline use case. Use via the dut.<PERIPHERAL>.<REGISTER>.<FIELD>.io
        property to assign a value.

        :type  value: ``int`` or ``long``
        :param value: The value to assign to the register field.
        """
        pass

    io = abstractproperty(_getio, _setio)

    # I/O Access Methods

    @abstractmethod
    def isReadable(self):
        """
        Check if field is readable.

        :rtype: ``bool``
        :return: ``True`` if readable, else ``False``
        """
        pass

    @abstractmethod
    def isWriteable(self):
        """
        Check if register is writeable.

        :rtype: ``bool``
        :return: ``True`` if writeable, else ``False``
        """
        pass

    # Accessed Flag Methods

    @abstractmethod
    def clearAccessedFlag(self):
        """
        Clear the accessed flag for the field. Note that the accessed flag
        is set whenever the register is written. Any field write will set
        the accessed flag for the parent register as well.
        """
        pass

    @abstractmethod
    def setAccessedFlag(self):
        """
        Set the accessed flag for the field. Note that the accessed flag
        is set whenever the register is written. Any field write will set
        the accessed flag for the parent register as well.
        """
        pass

    @abstractmethod
    def getAccessedFlag(self):
        """
        Return the accessed flag for the field.

        :rtype: ``bool``
        :return: The state of the field's accessed flag
        """
        pass


    @abstractmethod
    def getSliceStr(self):
        """
        Return a string "{msb}:{lsb}" for the field's position within the parent
        register.

        :rtype: ``str``
        :return: The field slice string of format "msb:lsb" within the register
        """
        pass

    # Internal Only

    @abstractmethod
    def dump(self, regValue, fieldCommentList):
        """
        Read register and store in valueDict. The file handle is passed to
        internal functions to do the source dictionary output.

        .. note:: This is an internal function used by the device container.
                  Do not call directly.

        :type  regValue: ``long``
        :param regValue: The register value to process into field review
        :type  fieldCommentList: ``list`` of ``str``
        :param fieldCommentList: A list to collect the comment string \
                                for all fields in the register
        """
        pass


