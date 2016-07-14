
"""
Enum
----
All rm.<PERIPHERAL>.<REGISTER>.<FIELD>.enum components subclass
:class:`~Base_RM_Enum`, which implements this interface.

  .. autoclass:: IRegMapEnum
     :members:
     :show-inheritance:
     :inherited-members:

"""


__all__ = ['IRegMapEnum']

from abc import ABCMeta, abstractmethod

class IRegMapEnum(object):
    """
    The interface for the dut.rm.<PERIPHERAL>.<REGISTER>.<FIELD>.enum
    component. This component will also contain enum name attributes in
    uppercase. The dut.rm.<PERIPHERAL>.<REGISTER>.<FIELD>.enum will
    contain an both value and description dictionaries. The __repr__()
    method will return name, value, and description details.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def getDescByValue(self, value):
        """
        Get the enum description string based on the passed field value.

        :type  value: ``int`` or ``long``
        :param value: The field value
        :rtype: ``str``
        :return: The enum description
        """
        pass

    @abstractmethod
    def getNameByValue(self, value):
        """
        Get the enum name string based on the passed field value.

        :type  value: ``int`` or ``long``
        :param value: The field value
        :rtype: ``str``
        :return: The enum name
        """
        pass
