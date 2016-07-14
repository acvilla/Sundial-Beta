
"""
This module contains the ModelVariable class to define a working variable in the
calculation flows.
"""

import common
from .. import model_type as model_type
from .. import model_instance as model_inst
from collections import OrderedDict
from enum import Enum, unique, EnumMeta, IntEnum
import sys
import types
import __builtin__
from variable_access_name import *

__all__ = [ 'ModelVariableInvalidValueType',
            'ModelVariableEmptyValue',
            'ModelVariablePropertyDeprecated',
            'ModelVariableCannotForceValue',
            'ModelVariableWriteAccess',
            'ModelVariableFormat',
            'CreateModelVariableEnum',
            'ModelVariable',
            'ModelVariableContainer',
            'ModelVariableTypeXml',
            'ModelVariableInstanceXml' ]

class ModelVariableInvalidValueType(Exception):
    pass

class ModelVariableEmptyValue(Exception):
    pass

class ModelVariablePropertyDeprecated(Exception):
    pass

class ModelVariableCannotForceValue(Exception):
    pass

class ModelVariableWriteAccess(Exception):
    pass

@unique
class ModelVariableFormat(Enum):
    ASCII = 0
    BINARY = 1
    COMPLEX = 2
    DECIMAL = 3
    FLOAT = 4
    HEX = 5
    UTF8 = 6
    UTF16 = 7


def CreateModelVariableEnum(enum_name, enum_desc, member_data):

    def getDesc(self):
        return self._enum_desc

    def getMemberDesc(self, name):
        return self._member_desc[name]

    values = OrderedDict()
    descriptions = OrderedDict()

    for name, value, desc in member_data:
        values[name] = value
        descriptions[name] = desc

    obj = IntEnum(enum_name, values)
    obj._enum_desc = enum_desc
    obj._member_desc = descriptions
    obj.getDesc = types.MethodType(getDesc, obj)
    obj.getMemberDesc = types.MethodType(getMemberDesc, obj)

    return obj


class ModelVariable(object):
    """
    Represent a variable in the calculation model. Allow for tracking calculated, user-forced,
    and actual reverse-decoded versions of the value. Requires a var_type. Provides
    description string. Also supports min/max limits.
    """

    function = VariableAccess()

    def __init__(self, name, var_type, is_array, desc='',
                 format=ModelVariableFormat.HEX, forceable=True):
        #: The variable name
        self.name = name
        if not issubclass(var_type, Enum):
            assert var_type in (basestring, bool, complex, float, int, long, str), \
                "FATAL ERROR: Unsupported class for var_type: {}".format(var_type)
        #: The class type of the variable
        self._var_type = var_type
        if self.var_type == Enum:
            assert not is_array, "FATAL ERROR: array of Enum not supported"
        #: The value is an array
        self._is_array = is_array
        #: Defines the display format of the variable
        self.format = format
        #: A string description of the variable
        self.desc = desc
        assert isinstance(forceable, bool)
        self._forceable = forceable
        #: The peripheral.register.field notation string
        self._svd_mapping = None
        #: The units string for the variable
        self._units = None
        #: A forced value to use in place of the calculated value
        self._value_forced = None
        #: The calculated value of the variable from an internal stage. \
        #: Can be overridden with the value_force.
        self._value_calc = None

        self._var_enum = None

        # List of functions that were used to read or writea variable
        self._access_read = list()
        self._access_write = list()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert isinstance(value, basestring)
        self._name = value

    @property
    def var_type(self):
        return self._var_type

    @property
    def is_array(self):
        return self._is_array

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        assert isinstance(value, basestring)
        self._desc = value

    @property
    def format(self):
        return self._var_format

    @format.setter
    def format(self, value):
        assert isinstance(value, ModelVariableFormat)
        self._var_format = value

    @property
    def forceable(self):
        return self._forceable

    @property
    def svd_mapping(self):
        return self._svd_mapping

    @svd_mapping.setter
    def svd_mapping(self, value):
        assert isinstance(value, basestring)
        assert len(value.split('.')) == 3, \
            "FATAL ERROR: {} must be PERIPHERAL.REGISTER.FIELD format".format(value)
        self._svd_mapping = value

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, value):
        assert isinstance(value, basestring)
        self._units = value

    @property
    def value(self):
        if self.function.name is not None:
            self._access_read.append(self.function.name)

        if self._value_forced is not None:
            return self._value_forced
        elif self._value_calc is not None:
            return self._value_calc
        else:
            if self.function.name is not None:
                # Only raise the exception if we are inside the calc functions
                raise ModelVariableEmptyValue("Value is empty for variable '{}'".format(self.name))
            else:
                return None

    @value.setter
    def value(self, value):
        if self.function.name is not None:
            if len(self._access_write) == 0:
                self._access_write.append(self.function.name)
            elif self._access_write[0] != self.function.name:
                # Can only have one function write to a variable at a time
                raise ModelVariableWriteAccess("Function: " + self.function.name + " tried to access variable: " + self.name + ". This variable was already written to by: " + str(self._access_write[0]))

        self.validate_type(value)
        self._value_calc = value

    @property
    def value_forced(self):
        return self._value_forced

    @value_forced.setter
    def value_forced(self, value):
        if not self.forceable:
            raise ModelVariableCannotForceValue("Cannot force variable '{}'".format(self.name))
        self.validate_type(value)
        self._value_forced = value

    @property
    def value_calc(self):
        return self._value_calc

    @value_calc.setter
    def value_calc(self, value):
        self.validate_type(value)
        self._value_calc = value

    @property
    def var_enum(self):
        return self._var_enum

    @var_enum.setter
    def var_enum(self, value):
        assert isinstance(value, EnumMeta)
        self._var_enum = value

    def validate(self):
        """
        Validate the type plus optional min/max limits for any forced,
        or calculated values.

        :rtype: ``bool``
        :return: True for valid, False for invalid.
        """
        return self._validate_variable(self._value_forced) and \
            self._validate_variable(self._value_calc)

    def _validate_variable(self, variable):
        """
        Validate one of the value types (forced, or calculated)

        :type variable: See the var_type.
        :param variable: The variable to validate type, and any limits.
        :rtype: ``bool``
        :return: True if variable is none or defined an successfully eval
        """
        if variable is not None:
            # test type
            if not self.validate_type(variable):
                return False

        return True

    def validate_type(self, value):
        if value is None:
            return True
        elif self.is_array:
            for item in value:
                if not isinstance(item, self._var_type):
                    raise ModelVariableInvalidValueType("List item '{}' is not type {}".format(item,
                                                                                           self._var_type))
        else:
            if not isinstance(value, self._var_type):
                raise ModelVariableInvalidValueType("Value '{}' is not type {}".format(value,
                                                                                   self._var_type))

        return True

    def _get_type_str(self):
        if self._var_type in (bool, complex, float, int, long):
            return self._var_type.__name__
        elif self._var_type is basestring:
            return "string"
        elif self._var_type is str:
            return "string"
        elif issubclass(self._var_type, Enum):
            return "enum"
        else:
            return "None"

    def _get_enum_type_xml(self):
        if self.var_enum:
            enum_obj = model_type.enumType(name=self.var_enum.__name__,
                                           desc=self.var_enum.getDesc(),
                                           members=model_type.membersType())
            for member in self.var_enum.__members__:
                member_obj = model_type.memberType(name=member,
                                                   value=self.var_enum.__members__[member].value,
                                                   desc=self.var_enum.getMemberDesc(member))
                enum_obj.members.add_member(member_obj)
        else:
            enum_obj = None
        return enum_obj


    def to_type_xml(self):
        return model_type.variableType(name=self.name,
                                       type_=self._get_type_str(),
                                       is_array=self.is_array,
                                       format=self.format.name.lower(),
                                       desc=self.desc,
                                       forceable=self.forceable,
                                       svd_mapping=self.svd_mapping,
                                       units=self.units,
                                       enum=self._get_enum_type_xml())

    def _get_enum_instance_xml(self):
        if self.var_enum:
            enum_obj = model_inst.enumType(name=self.var_enum.__name__,
                                           desc=self.var_enum.getDesc(),
                                           members=model_inst.membersType())
            for member in self.var_enum.__members__:
                member_obj = model_inst.memberType(name=member,
                                                   value=self.var_enum.__members__[member].value,
                                                   desc=self.var_enum.getMemberDesc(member))
                enum_obj.members.add_member(member_obj)
        else:
            enum_obj = None
        return enum_obj

    def to_instance_xml(self):
        values_obj = model_inst.valuesType(calculated=model_inst.calculatedType(common.get_xml_str_values(self.is_array,
                                                                                                          self._value_calc)),
                                           forced=model_inst.forcedType(common.get_xml_str_values(self.is_array,
                                                                                                  self._value_forced)))
        return model_inst.variableType(name=self.name,
                                       type_=self._get_type_str(),
                                       is_array=self.is_array,
                                       format=self.format.name.lower(),
                                       desc=self.desc,
                                       forceable=self.forceable,
                                       svd_mapping=self.svd_mapping,
                                       units=self.units,
                                       enum=self._get_enum_instance_xml(),
                                       values=values_obj,
                                       access_read = self._get_access_read_instance_xml(),
                                       access_write = self._get_access_write_instance_xml())

    def __str__(self):
        out = '\n  Variable - {}\n'.format(self.name)
        out += '    Type:             {}\n'.format(self.var_type)
        out += '    Arrayed:          {}\n'.format(self.is_array)
        out += '    Format:           {}\n'.format(self.format)
        out += '    Desc:             {}\n'.format(self.desc)
        out += '    Forceable:        {}\n'.format(self.forceable)
        if self.svd_mapping is not None:
            out += '    SVD Mapping:      {}\n'.format(self.svd_mapping)
        if self.units is not None:
            out += '    Units:      {}\n'.format(self.units)
        #TODO: Apply the format to view the value attributes
        if self.value_calc is not None:
            out += '    Value Calculated: {}\n'.format(self.value_calc)
        if self.value_forced is not None:
            out += '    Value Forced:     {}\n'.format(self.value_forced)
        if self.var_enum:
            out += '\n  Enum - {}:\n'.format(self.var_enum.__name__)
            out += '\n  Enum Desc: {}\n'.format(self.var_enum.getDesc())
            for member in self.var_enum.__members__:
                out += '    {} = {}   # {}\n'.format(member,
                                                     self.var_enum.__members__[member].value,
                                                     self.var_enum.getMemberDesc(member))
        if self.access_read is not None:
            out += '    Access read:      {}\n'.format(str(self.access_read))
        if self.access_write is not None:
            out += '    Access write:     {}\n'.format(str(self.access_write))

        return out

    @property
    def access_read(self):
        return list(self._access_read)

    @property
    def access_write(self):
        return list(self._access_write)

    def _get_access_read_instance_xml(self):
        access_read = self.access_read
        if access_read is None:
            access_read = list()
        access_read_obj = model_inst.access_readType(name=access_read)
        return access_read_obj

    def _get_access_write_instance_xml(self):
        access_write = self.access_write
        if (access_write is None) or (len(access_write) == 0):
            access_write = list()
            access_write.append(None)
        access_write_obj = model_inst.access_writeType(name=access_write[0])
        return access_write_obj

class ModelVariableContainer(object):
    def __init__(self):
        self.ZZ_VARIABLE_KEYS = OrderedDict()

    def __iter__(self):
        for key in self.ZZ_VARIABLE_KEYS:
            yield self.ZZ_VARIABLE_KEYS[key]

    def __contains__(self, name):
        return name in self.ZZ_VARIABLE_KEYS

    def get_var(self, var_name):
        return self.ZZ_VARIABLE_KEYS[var_name]

    def append(self, var):
        assert isinstance(var, ModelVariable), "FATAL ERROR: var must be ModelVariable"
        if var.name in self.ZZ_VARIABLE_KEYS:
            raise ValueError("Variable '{}' already exists, please use another name".format(var.name))
        self.ZZ_VARIABLE_KEYS[var.name] = var
        setattr(self, var.name, var)

    def extend(self, var_list):
        for var in var_list:
            self.append(var)

    def validate(self):
        for var in self:
            if not var.validate():
                sys.stderr.write("ERROR: Invalid variable '{}'".format(var.name))
                return False
        return True

    def to_type_xml(self):
        variables = model_type.variablesType()
        for var in self:
            variables.add_variable(var.to_type_xml())
        return variables

    def to_instance_xml(self):
        variables = model_inst.variablesType()
        for var in self:
            variables.add_variable(var.to_instance_xml())
        return variables

class ModelVariableXml(ModelVariable):

    def __init__(self, name, type_, is_array):
        super(ModelVariableXml, self).__init__(name, type_, is_array)

    def _get_var_type(self, var_root):
        if var_root.type_ in ('bool', 'complex', 'float', 'int', 'long'):
            return getattr(__builtin__, var_root.type_)
        if var_root.type_ =='string':
            return str
        elif var_root.type_ == 'enum':
            return Enum
        else:
            return None

    def _build_var_enum_from_xml(self, enum_root):
        member_data = []
        for member in enum_root.get_members().get_member():
            member_data.append([member.name, member.value, member.desc])
        self.var_enum = CreateModelVariableEnum(enum_root.name, enum_root.desc, member_data)


class ModelVariableTypeXml(ModelVariableXml):

    def __init__(self, var_root):
        assert isinstance(var_root, model_type.variableType)
        super(ModelVariableTypeXml, self).__init__(var_root.name,
                                                   self._get_var_type(var_root),
                                                   var_root.is_array)
        if self.var_type == Enum:
            self._build_var_enum_from_xml(var_root.enum)
        self.format = getattr(ModelVariableFormat, var_root.format.upper())
        self.desc = var_root.desc
        if var_root.svd_mapping is not None:
            self.svd_mapping = var_root.svd_mapping
        if var_root.units is not None:
            self.units = var_root.units


class ModelVariableInstanceXml(ModelVariableXml):

    def __init__(self, var_root):
        assert isinstance(var_root, model_inst.variableType)
        super(ModelVariableInstanceXml, self).__init__(var_root.name,
                                                       self._get_var_type(var_root),
                                                       var_root.is_array)
        if self.var_type == Enum:
            self._build_var_enum_from_xml(var_root.enum)
        self.format = getattr(ModelVariableFormat, var_root.format.upper())
        self.desc = var_root.desc
        if var_root.svd_mapping is not None:
            self.svd_mapping = var_root.svd_mapping
        if var_root.units is not None:
            self.units = var_root.units

        # assign values with the instance
        self.value_calc = common.cast_value_from_xml(self, var_root.values.calculated.value)
        self.value_forced = common.cast_value_from_xml(self, var_root.values.forced.value)
