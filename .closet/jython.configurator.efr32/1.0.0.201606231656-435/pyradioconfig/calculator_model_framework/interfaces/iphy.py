from abc import ABCMeta, abstractmethod
import inspect
import types
from pyradioconfig.calculator_model_framework.Utils.Object import Object
from pyradioconfig.calculator_model_framework.Utils.Version import Version
from pyradioconfig.pycalcmodel import ModelPhy, ModelInput
import os

"""
Phy interface file
"""
class IPhy(object):

    """
    Returns phy readable and searchable group name
    """
    def getGroupName(self):
        # using class name as the phy group name
        #return str(self.__class__.__name__)
        group_name = os.path.basename(inspect.getfile(self.__class__))
        group_name = str(group_name).replace('.pyc', '')
        group_name = str(group_name).replace('.py', '')
        return group_name

    """
    Returns list of callable phy functions
    """
    @abstractmethod
    def getPhyList(self):
        functionList = list()
        for functionName, functionPointer in inspect.getmembers(self, predicate=inspect.ismethod):
                if str(functionName).lower().startswith('phy_'):  # Check if the function name starts with "phy_"
                    if isinstance(functionPointer, types.MethodType):
                        #functionList.append(self.__class__.__name__ + "." + functionName)
                        functionList.append(functionPointer)
        return functionList

    """
    Builds empty phy model
    """
    @abstractmethod
    def _makePhy(self, modem_model, profile, phy_description=None, phy_group_name=None, readable_name=None, act_logic=''):
        # Build phy from name, version, and class path
        phy_function_name = IPhy.__callersname()  # Phy name is the name of the function that called this maker function
        if phy_description is None:
            if readable_name is None:
                phy_description = phy_function_name
            else:
                phy_description = readable_name
        if phy_group_name is None:
            # Use class name if no group name given
            phy_group_name = self.getGroupName()
        if readable_name is None:
            readable_name = phy_function_name.replace("_", " ")
        phy = ModelPhy(phy_function_name, phy_description, profile, phy_group_name, readable_name=readable_name, act_logic=act_logic)
        modem_model.phys.append(phy)
        return phy

    @staticmethod
    def __callersname():
        import sys
        return str(sys._getframe(2).f_code.co_name)


