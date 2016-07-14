
__all__ = [ 'Base_RM_Enum' ]

from .. interface import IRegMapEnum


class Base_RM_Enum(IRegMapEnum):

    def __init__(self, label, edict, desc):
        self.__dict__['zz_frozen'] = False
        self.zz_label = label
        self.zz_edict = edict
        self.zz_desc = desc

    def __setattr__(self, name, value):
        if self.__dict__['zz_frozen']:
            raise AttributeError("FATAL ERROR: Unable to set '{}' to '{}'".format(name, value))
        else:
            self.__dict__[name] = value

    def __repr__(self):
        out = ""
        for key in self.zz_edict.keys():
            out += "        {}  {}: {}\n".format(self.zz_edict[key], key, self.zz_desc[key])
        return out

    def getDescByValue(self, value):
        try:
            return self.zz_desc[self.getNameByValue(value)]
        except KeyError:
            return None

    def getNameByValue(self, value):
        for key in self.zz_edict.keys():
            if self.zz_edict[key] == value:
                return key
        return None
