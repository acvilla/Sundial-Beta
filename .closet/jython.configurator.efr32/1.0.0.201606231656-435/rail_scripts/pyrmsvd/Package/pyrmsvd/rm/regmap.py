
from ..base import Bindings
from collections import OrderedDict
from regmap_io import RegisterMap_IO
import sys

__all__ = [ 'RM_Device' ]


class RM_Enums(object):
    def __init__(self, label, field):
        self.__dict__['zz_frozen'] = False
        self.zz_label = label
        self.zz_field = field
        self.zz_edict = OrderedDict()
        for enum in self.zz_field.enumeratedValues[0].get_enumeratedValue():
            self.zz_edict[enum.name] = int(enum.value, 16)
            self.zz_add_property(enum.name)
        self.__dict__['zz_frozen'] = True
    def __repr__(self):
        out = ""
        for enum in self.zz_field.enumeratedValues[0].get_enumeratedValue():
            out += "        {}  {}: {}\n".format(enum.value, enum.name, enum.description)
        return out
    def __getattr__(self, name):
        if name == 'zz_field':
            return self.__dict__['zz_field']
        elif name == 'zz_edict':
            return self.__dict__['zz_edict']
        else:
            return self.__dict__['zz_edict'][name]
    def __setattr__(self, name, value):
        if self.__dict__['zz_frozen']:
            raise AttributeError("ERROR: Unable to set '{}' to '{}'".format(name, value))
        else:
            self.__dict__[name] = value
    def zz_add_property(self, name):
        # create local fget and fset functions
        fget = lambda self: self.zz_get_property(name)
        fset = lambda self, value: self.zz_set_property(name, value)

        # add property to self
        setattr(self.__class__, name, property(fget, fset))

    def zz_set_property(self, name, value):
        raise AttributeError("ERROR: Unable to set enum '{}'".format(name))

    def zz_get_property(self, name):
        return self.zz_edict[name]

class RM_Field(object):

    def __init__(self, rmio, register, baseAddress, label, field):
        self.__dict__['zz_frozen'] = False
        self.zz_rmio = rmio
        self.zz_reg = register
        self.zz_baseAddr = baseAddress
        self.zz_label = label
        self.zz_field = field
        self.enum = None
        if self.zz_field.enumeratedValues:
            self.enum = RM_Enums(label, self.zz_field)
        self.__dict__['zz_frozen'] = True
    def __repr__(self):
        lsb = int(self.zz_field.bitOffset)
        fsize = int(self.zz_field.bitWidth)
        sliceStr = "{}:{}".format(lsb+fsize-1, lsb) if fsize > 1 else "{}".format(lsb)
        enumStr = ' ENUMERATED' if self.enum is not None else ''
        out = "    {:#010x} {}[{}] contains field {}: {} <{}>{}\n".format((self.zz_baseAddr + int(self.zz_reg.addressOffset, 16)),
                                                                    self.zz_reg.name, sliceStr, self.zz_field.name,
                                                                    self.zz_field.description, self.zz_field.access, enumStr)
        return out
    def __getattr__(self, name):
        if name == 'zz_rmio':
            return self.__dict__['zz_rmio']
        elif name == 'zz_reg':
            return self.__dict__['zz_reg']
        elif name == 'zz_baseAddr':
            return self.__dict__['zz_baseAddr']
        elif name == 'zz_field':
            return self.__dict__['zz_field']
        elif name == 'io':
            return self.zz_rmio.readRegisterField(self.zz_baseAddr, self.zz_reg, self.zz_field)
        elif name == 'enum':
            return self.__dict__['enum']
        else:
            return self
    def __setattr__(self, name, value):
        if self.__dict__['zz_frozen']:
            if name == 'io':
                self.zz_rmio.writeRegisterField(self.zz_baseAddr, self.zz_reg, self.zz_field, value)
            else:
                raise AttributeError("FATAL ERROR: Unable to set '{}' to '{}'".format(name, value))
        else:
            self.__dict__[name] = value
    @property
    def io(self):
        return self.zz_rmio.readRegisterField(self.zz_baseAddr, self.zz_reg, self.zz_field)
    @io.setter
    def io(self, value):
        self.zz_rmio.writeRegisterField(self.zz_baseAddr, self.zz_reg, self.zz_field, value)



class RM_Register(object):

    def __init__(self, rmio, register, baseAddress, label):
        self.__dict__['zz_frozen'] = False
        self.zz_rmio = rmio
        self.zz_reg = register
        self.zz_baseAddr = baseAddress
        self.zz_label = label
        self.zz_fdict = OrderedDict()
        for field in self.zz_reg.fields.get_field():
            self.zz_fdict[field.name] = RM_Field(rmio, register, baseAddress, label, field)
            self.zz_add_property(field.name)
        self.__dict__['zz_frozen'] = True
    def __repr__(self):
        out = "    {:#010x}  {}: {} <{}>\n".format((self.zz_baseAddr + int(self.zz_reg.addressOffset, 16)),
                                                   self.zz_reg.name, self.zz_reg.description, self.zz_reg.access)
        for key in sorted(self.zz_fdict.iterkeys()):
            f = self.zz_fdict[key].zz_field
            lsb = int(f.bitOffset)
            fsize = int(f.bitWidth)
            sliceStr = "{}:{}".format(lsb+fsize-1, lsb) if fsize > 1 else "{}".format(lsb)
            out += "        {} ({}): {} <{}>\n".format(f.name, sliceStr, f.description, f.access)
        return out
    def __getattr__(self, name):
        if name == 'zz_rmio':
            return self.__dict__['zz_rmio']
        elif name == 'zz_reg':
            return self.__dict__['zz_reg']
        elif name == 'zz_fdict':
            return self.__dict__['zz_fdict']
        elif name == 'zz_baseAddr':
            return self.__dict__['zz_baseAddr']
        elif name == 'io':
            return self.zz_rmio.readRegister(self.zz_baseAddr, self.zz_reg)
        else:
            return self.__dict__[name]
    def __setattr__(self, name, value):
        if name == 'io':
            self.zz_rmio.writeRegister(self.zz_baseAddr, self.zz_reg, value)
        elif self.__dict__['zz_frozen']:
            raise AttributeError("ERROR: Unable to set '{}' to '{}'".format(name, value))
        else:
            self.__dict__[name] = value
    def zz_add_property(self, name):
        # create local fget and fset functions
        fget = lambda self: self.zz_get_property(name)
        fset = lambda self, value: self.zz_set_property(name, value)

        # add property to self
        setattr(self.__class__, name, property(fget, fset))

    def zz_set_property(self, name, value):
        raise AttributeError("ERROR: Unable to set field '{}' to '{}'".format(name, value))

    def zz_get_property(self, name):
        return self.zz_fdict[name]

    @property
    def io(self):
        return self.zz_rmio.readRegister(self.zz_baseAddr, self.zz_reg)
    @io.setter
    def io(self, value):
        self.zz_rmio.writeRegister(self.zz_baseAddr, self.zz_reg, value)

class RM_Peripheral(object):

    def __init__(self, rmio, peripheral, label):
        self.__dict__['zz_frozen'] = False
        self.zz_rmio = rmio
        self.zz_per = peripheral
        self.zz_label = label
        self.zz_rdict = OrderedDict()
        for reg in self.zz_per.registers.get_register():
            if reg and reg.fields:
                self.zz_rdict[reg.name] = RM_Register(self.zz_rmio, reg,
                                                      int(self.zz_per.baseAddress, 16),
                                                      label)
                self.zz_add_property(reg.name)
        self.__dict__['zz_frozen'] = True
    def __repr__(self):
        out = "{}  {}: {}\n".format(self.zz_per.baseAddress, self.zz_per.name,
                                    self.zz_per.description)
        for key in sorted(self.zz_rdict.iterkeys()):
            out += "    {}\n".format(key)
        return out
    def __getattr__(self, name):
        if name == 'zz_rmio':
            return self.__dict__['zz_rmio']
        elif name == 'zz_per':
            return self.__dict__['zz_per']
        elif name == 'zz_rdict':
            return self.__dict__['zz_rdict']
        else:
            return self.__dict__[name]
    def __setattr__(self, name, value):
        if self.__dict__['zz_frozen']:
            if name not in self.zz_rdict:
                sys.stderr.write("ERROR: Invalid register '{}'\n".format(name))
            else:
                sys.stderr.write("ERROR: Unable to set '{}' to '{}'\n".format(name, value))
        else:
            self.__dict__[name] = value

    def zz_add_property(self, name):
        # create local fget and fset functions
        fget = lambda self: self.zz_get_property(name)
        fset = lambda self, value: self.zz_set_property(name, value)

        # add property to self
        setattr(self.__class__, name, property(fget, fset))

    def zz_set_property(self, name, value):
        raise AttributeError("ERROR: Unable to set register '{}' to '{}'".format(name, value))

    def zz_get_property(self, name):
        return self.zz_rdict[name]

class RM_Device(object):

    def __init__(self, svdFN, rmIO, label):
        self.__dict__['zz_frozen'] = False
        self.zz_svd = Bindings.parse(svdFN)
        assert isinstance(rmIO, RegisterMap_IO)
        self.zz_rmio = rmIO
        self.zz_pdict = OrderedDict()
        self.zz_label = label
        for per in self.zz_svd.peripherals.get_peripheral():
            if per.registers:
                self.zz_pdict[per.name] = RM_Peripheral(self.zz_rmio, per, label)
                self.zz_add_property(per.name)
        self.__dict__['zz_frozen'] = True
    def __repr__(self):
        out = "{}\n".format(self.zz_svd.name)
        for key in sorted(self.zz_pdict.iterkeys()):
            out += "  {}\n".format(key)
        return out
    def __getattr__(self, name):
        if name == 'zz_svd':
            return self.__dict__['zz_svd']
        elif name == 'zz_rmio':
            return self.__dict__['zz_rmio']
        elif name == 'zz_pdict':
            return self.__dict__['zz_pdict']
        else:
            return self.__dict__[name]
    def __setattr__(self, name, value):
        if self.__dict__['zz_frozen']:
            if name not in self.zz_pdict:
                sys.stderr.write("ERROR: Invalid peripheral '{}'\n".format(name))
            else:
                sys.stderr.write("ERROR: Unable to set '{}' to '{}'\n".format(name, value))
        else:
            self.__dict__[name] = value

    def zz_add_property(self, name):
        # create local fget and fset functions
        fget = lambda self: self.zz_get_property(name)
        fset = lambda self, value: self.zz_set_property(name, value)

        # add property to self
        setattr(self.__class__, name, property(fget, fset))

    def zz_set_property(self, name, value):
        raise AttributeError("ERROR: Unable to set peripheral '{}' to '{}'".format(name, value))

    def zz_get_property(self, name):
        return self.zz_pdict[name]
