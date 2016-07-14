# This is a python adapter that adapts to the IModemCalculator java interface
#
# Still need to figure out the datails of how this ties in.

# These are required to tie in java
from com.ember.workbench.util import TextUtility
from com.ember.workbench.chip_config import IChipConfigurator
from com.ember.workbench.chip_config import ChipConfiguratorData
from com.ember.workbench.option import OptionList, OptionType
from types import *
try:
    from version_info import version_info
except ImportError:
    # sead 2016-Jan-11
    # ugly hack to work around an ImportError issue with EFR32 chip config
    pass
# import jarray

# If I don't do these two things, then jython is whining about some NoneType when
# using sys.prefix. This is quite a hack. I have no clue what I'm doing or what sys.prefix is.
import sys
sys.prefix = "/"

# Class implementation
class ChipConfiguratorJavaInterface(IChipConfigurator):

    group_order = 0
    item_order = 0
    
    def __init__ (self):
        print("Not allowed to create this class")
        raise

    def _getOptionType(self, var):
        if ((isinstance(var, int) or
            isinstance(var, long)) and
            not (isinstance(var, bool))):
            return OptionType.INTEGER
        if isinstance(var, float):
            return OptionType.FLOAT
        if (isinstance(var, str) or  
            isinstance(var, unicode) or
            isinstance(var, list) or
            isinstance(var, NoneType) or
            isinstance(var, complex)) :
            return OptionType.STRING
        if isinstance(var, bool):
            return OptionType.BOOLEAN
        if isinstance(var, enum):
            return OptionType.ENUM
        raise RuntimeError("Value {} Unrecognized input type {} in calculate()".format(var, type(var),))
        
    def calculate(self, chipId, configInput):
        configurator = self.configurator.instance(chipId)
#         print("DEBUG: setting input:\n{}".format(configInput.toString()))
#         profileId = TextUtility.print(configInput.get(ChipConfiguratorData.RADIO_PROFILE))
#         if not(profileId is None):
#             self.configurator.instance(chipId).set_profile(profileId)
        profileId = configInput.get(ChipConfiguratorData.RADIO_PROFILE)
        needToSetOptions = True
        if profileId is None:
            # not providing a profile means setting the profile to empty string
            configurator.set_profile("")
        elif profileId in self.profileIds(chipId):
            # If the specified profile is known to the chip configurator, go ahead and set the profile
            configurator.set_profile(TextUtility.print(profileId))
        else:
            # The profile is not none and it's not known to chip configurator
            profileData = {}
            for item in configInput.keys():
                if item != ChipConfiguratorData.RADIO_PROFILE:
                    profileData[item] = TextUtility.print(configInput.get(item))
            configurator.add_profile(TextUtility.print(profileId), profileData)
            # Signal that there is not need to set the options because add_profile() would have
            # done so.
            needToSetOptions = False
        # then set all other inputs if needed
        if needToSetOptions:
            for item in configInput.keys():
                if item != ChipConfiguratorData.RADIO_PROFILE:
                    configurator.set_option(item, self._get_literal(configInput.get(item)))
#         print("DEBUG: calling configure...")
        config_data = configurator.configure(split_set_property = True)
        if config_data is None:
            raise RuntimeError("Fatal runtime error")
        return self._dict_as_chip_configurator_data(config_data)
    
    def _get_literal(self, value):
        return TextUtility.print(value)

    def _dict_as_chip_configurator_data(self, data):
#         print(data)
        outputs = ChipConfiguratorData()
        for k, v in data.items():
            if isinstance(v, int):
                outputs.setInt(k, v)
            elif isinstance(v, long):
                outputs.setLong(k, v)
            elif isinstance(v, float):
                outputs.setDouble(k, v)
            elif isinstance(v, str):
                outputs.setString(k, v)
            elif isinstance(v, bytearray):
                outputs.setBytes(k, bytes(v))
            elif isinstance(v, list):
                outputs.setString(k, v.__repr__())
            else:
                raise RuntimeError("Key {}, value {} Unrecognized input type {} in calculate()".format(k, v, type(v),))
        return outputs
        
    def inputOptions(self, chipId, category):
#         self.group_order += 1
#         self.item_order = 0
#         print("group.{0}.label={0}".format(category))
#         print("group.{}.order={}".format(category, self.group_order))
#         print("")
        option_list = OptionList.empty()
        for k, v in self.configurator.instance(chipId).get_options(category).items():
#             self.item_order += 1
#             print("{0}.label={0}".format(k))
#             print("{}.tooltip=".format(k))
#             print("{}.group={}".format(k,category))
#             print("{}.order={}".format(k, self.item_order))
#             print("")
#             print("{} {} {}".format(k, type(v), v))
            option_list.add(k, k, "", self._getOptionType(v), "{}".format(v))
        return option_list

    def categories(self, chipId):
        return self.configurator.instance(chipId).get_categories()
    
    def profileIds(self, chipId):
        return self.configurator.instance(chipId).get_profile_ids()
    
    def profileData(self, chipId, profileId):
        pData = self.configurator.instance(chipId).get_profile_data(profileId)
        return self._dict_as_chip_configurator_data(pData)
    
    def isOptionIdValid(self, chipId, optionId):
        return optionId in self.configurator.instance(chipId).get_options().keys()
    
    def version(self, chipId):
        return version_info.get_version_string()
