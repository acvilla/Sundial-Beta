"""
Wrapper layer (adapter) for host_py_radio_config to be consumed by Simplicity Studio.
This wrapper allows the "radio configurator" to support the Pro2 style dictionary interface, where the input and output values are defined by key/value pairs.
"""

from .efr32configurator import Efr32Configurator
from .efr32cfginput import Efr32CfgInput
from .efr32category import Efr32Category
