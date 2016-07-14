# This is a python adapter that adapts to the IModemCalculator java interface
from ChipConfiguratorJavaInterface import ChipConfiguratorJavaInterface
# These are required to tie into the actual modem calculator
from si4010_modem_calc import Si4010ApiCalc

__all__ = ["si4010ConfiguratorJavaInterface"]

# Class implementation
class si4010ConfiguratorJavaInterface(ChipConfiguratorJavaInterface):

    def __init__ (self):
        self.configurator = Si4010ApiCalc()
