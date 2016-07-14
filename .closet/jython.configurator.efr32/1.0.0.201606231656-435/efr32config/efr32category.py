
from common import CategoryInterface
from enum import Enum
from pyradioconfig.pycalcmodel import ModelVariableInvalidValueType

__all__ = ["Efr32Category"]

class Efr32Category(CategoryInterface):
    """
    Imports and lists all the input categories defined for this library.
    This class manages the actual key/value pairs
    """
    
    NO_CATEGORY_STRING = "NO_CATEGORY"
    #OUTPUT_CATEGORY_STRING = "OUTPUT_OVERRIDE"

    _profile = None

    def __init__(self, name, profile):
        self.reset()
        self._name = name
        self._profile = profile
        
        # Add profile inputs and outputs as options
        for input in profile.inputs:
            if name == self.NO_CATEGORY_STRING:
                if (input.category is None) or (input.category == ""):
                    if input.deprecated:
                        self._options[input.var_name] = None
                    else:
                        self._options[input.var_name] = input.default
            elif name == input.category:
                if input.deprecated:
                    self._options[input.var_name] = None
                else:
                    self._options[input.var_name] = input.default

        # Profile outputs that can be overridden are now defined as linked inputs
        #for output in profile.outputs:
        #    if name == self.OUTPUT_CATEGORY_STRING:
        #        if (output.category is None) or (output.category == ""):
        #            self._options[output.var_name] = None
        #    elif name == output.category:
        #        self._options[output.var_name] = None
                
    def get_options(self):
        return self._options

    def set_option(self, option, value):
        if self._input_is_array(option):
            newValue = self._set_option_list(option, value)    
        else:
            newValue = self._set_option_scalar(option, value)
        self._options[option] = newValue
        self._updateProfile(option, newValue)
        
        return newValue
    
    def _set_option_scalar(self, option, value):
        opt_type = self._get_option_type(option)
        value_type = type(value)
        if opt_type is value_type:
            newValue = value
        elif value is None:
            newValue = value
        elif (opt_type == Enum):
            if (value_type == int):
                # Converts integer to Enum
                try:
                    opt_type_enum = self._get_option_enum_class(option)
                    newValue = opt_type_enum(value)
                    value = newValue
                except Exception, e:
                    raise ModelVariableInvalidValueType(e.message)
            elif (issubclass(value_type, Enum)):
                newValue = value
            elif (value is None):
                newValue = value
            else:
                raise ModelVariableInvalidValueType("Unknown Enum type conversion for {} of type {}.".format(value, value_type))
        elif opt_type == float:
            newValue = float(value)
        elif opt_type == long:
            newValue = long(value)         
        elif opt_type == bool:
            newValue = bool(value)
        else:
            raise ModelVariableInvalidValueType("Value '{}' is not type {}".format(value, opt_type))
        return newValue
    
    def _set_option_list(self, option, value):
        newValue = []
        opt_type = self._get_option_type(option)
        if type(value) == list:
            if type(list[0]) == opt_type:
                newValue = value
        return newValue
    
    def _input_is_array(self, option):
        if hasattr(self._profile.inputs, option):
            profile_input = getattr(self._profile.inputs, option)
            return profile_input.is_array
        else:
            return False
    
    def _updateProfile(self, option, value):
        if hasattr(self._profile.inputs, option):
            profile_input = getattr(self._profile.inputs, option)
            profile_input.var_value = value
        
        # No longer can override outputs
        #if hasattr(self._profile.outputs, option):
        #    output = getattr(self._profile.outputs, option)
        #    output.override = value
        
    def _get_option_type(self, option):
        if hasattr(self._profile.inputs, option):
            input = getattr(self._profile.inputs, option)
            return input._var.var_type
        else:
            return None

    def _get_option_enum_class(self, option):
        if hasattr(self._profile.inputs, option):
            input = getattr(self._profile.inputs, option)
            return input._var._var_enum
        else:
            return None
        
    def reset(self):
        self._name = ''
        self._profile = None
        self._options = dict()
    