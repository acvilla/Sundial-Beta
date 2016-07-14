import copy
from common import ChipConfiguratorInterface
from .efr32cfginput import Efr32CfgInput

from pyradioconfig.calculator_model_framework.CalcManager import CalcManager
from pyradioconfig.calculator_model_framework.model_serializers.human_readable import Human_Readable
from pyradioconfig.calculator_model_framework.Utils.CalcStatus import CalcStatus
from pyradioconfig.pycalcmodel import ModelVariableEmptyValue
from rail_scripts.rail_config import RAILConfig
from _version import __version__


__all__ = ["Efr32Configurator"]

class Efr32Configurator(ChipConfiguratorInterface):
    '''
    Main interface to efr32-radio-configurator

    Example usages:
        Set option input values and calculate:

        >>> cfg = Efr32Configurator()
        >>> cfg.set_option('modem.base_frequency_hz', 12345L)
        >>> cfg.set_option('crc.crc_poly', CRC_8)
        >>> cfg.set_option('crc.crc_byte_endian', cfg._model_instance.vars.crc_byte_endian._var_enum.LSB_FIRST)
        >>> output = cfg.configure()

        Run PHY only:

        >>> cfg = Efr32Configurator()
        >>> output = cfg.configure(phy_name="PHY_RAIL")

        Run phy with optional inputs:

        >>> optional_inputs=dict()
        >>> optional_inputs['base_frequency_hz'] = 3405000001
        >>> cfg = Efr32Configurator()
        >>> output = cfg.configure(phy_name="PHY_Bluetooth_LE_Narrow_CHBW", optional_inputs=optional_inputs)
        
        Use specific part (defaults to 'dumbo', if not used)
        
        >>> phy_name_config = Efr32Configurator()
        >>> phy_name_config.setup(_profile_name='Base', _part_family="jumbo", _part_rev="A0")

        Loop through outputs

        >>> for key, value in output.iteritems():
        >>>     print ("Config {} Output: {}".format(key, value))

    '''
    
    _part_family = "dumbo"
    _part_rev = "A0"
    _profile_name = "Base"
    
    _model_instance = None
    _radio_configurator = None
    _rail_adapter = None

    def __init__(self):
        self.setup()
        setattr(self, "version", __version__)
        
    def setup(self, _part_family= None, _part_rev=None, _profile_name=None):   
        """
        Sets up the configurator
        
        Args:
            _part_family (str) : Part family name (e.g. 'jumbo').  Defaults to 'dumbo'
            _part_rev (str) : Part family revision name (e.g. 'S2').  Defaults to 'A0'
            _profile_name (str) : Input profile to use (e.g. 'Bluetooth_LE').  Defaults to 'Base'
        """         
        super(Efr32Configurator, self).__init__()
        
        if _part_family is not None:
            self._part_family = _part_family

        if _part_rev is not None:
            self._part_rev = _part_rev
        
        if _profile_name is not None:
            self._profile_name = _profile_name
            
        # Create radio configurator
        self._radio_configurator = CalcManager(self._part_family, self._part_rev)
        self._radio_configurator._CalcManager__developer_mode = False
        
        # Create model instance
        self._model_instance = self._radio_configurator.create_modem_model_instance(profile_name=self._profile_name)

        # Create RAIL Adapter
        self._rail_adapter = RAILConfig(rc_version = self._radio_configurator.version)
    
        self.inputs = Efr32CfgInput(self._model_instance)
                
        self.configuration = {}
        self._sync_categories_and_options()
        
    def configure (self, **kwargs):
        """
        kwargs are all optional.  
        kwargs phy_name is used if you'd like to run a specific phy, instead of a profile
        kwargs optional_inputs is a dictionary of inputs used when running a phy only, as specified above.  
        
        Examples:
        
        >>>   phy_name = 'PHY_BLuetooth'
        >>>   optional_inputs = dict()
        >>>   optional_inputs['base_frequency'] = 3405000001L
        """

        # Optional kwargs
        phy_name = None
        if 'phy_name' in kwargs:
            phy_name = kwargs['phy_name']       
            
            # Optional inputs are only for phy's
            optional_inputs  = dict()
            if 'optional_inputs' in kwargs:
                optional_inputs = kwargs['optional_inputs']       
        
        # Run the calculator
        if phy_name is None:
            # Normally just run a profile with inputs
            # THis is the normal use flow
            _temp_model_instance = copy.deepcopy(self._model_instance)
            result_code, error_message = self._radio_configurator.calculate(_temp_model_instance)
            self._temp_model_instance = _temp_model_instance
        else:
            # Used when you know which phy to run, with additional optional inputs
            _temp_model_instance = self._radio_configurator.calculate_phy(phy_name, optional_inputs)
            result_code = _temp_model_instance.result_code
            error_message = _temp_model_instance.error_message
            self._temp_model_instance = _temp_model_instance
        
        #
        self.configuration["result_code"] = result_code
        self.configuration["error_message"] = error_message
        if (result_code == CalcStatus.Success.value):
            # Run the rail adapter
            # RAILConfig consumes a dictionary of PHYs
            instanceDict = {}
            instanceDict['PHY_generated'] = _temp_model_instance
            self._rail_adapter.setInstanceDict(instanceDict)
            self._rail_adapter.parseConfigs("PHY_generated")
            
            #Colon separated file names for SS to generate
            self.configuration["file_names"] = "rail_config.h:rail_config.c"
            self.configuration["rail_config.h"] = self._rail_adapter.getRadioConfigHeaderC()
            self.configuration["rail_config.c"] = self._rail_adapter.getRadioConfigC()
            
            # Read outputs into a dictionary
            profile = getattr(_temp_model_instance.profiles, self._profile_name)
            for output in profile.outputs:
                try:
                    if output.var_value is not None:
                        self.configuration[output.var_name] = output.var_value
                except ModelVariableEmptyValue, e:
                    pass
            
            # Read profile inputs back, in-case any inputs were deprecated
            for input in profile.inputs:
                key = input.category + "." + input.var_name
                self.set_option(key, input._var.value_forced)

        # Serialize to CFG file
        if 'cfg_filename' in kwargs:
            cfg_filename = kwargs['cfg_filename']       
            Human_Readable.print_modem_model_values_v2(cfg_filename, str(phy_name), _temp_model_instance)

        # Serialize to XML instance file
        if 'xml_filename' in kwargs:
            xml_filename = kwargs['xml_filename']  
            self._radio_configurator.processed_model_to_xml(_temp_model_instance, xml_filename)     

        
        return self.configuration
    
    def set_profile(self, name):
        """
        Sets the profile name
        """
        self._profile_name = name
    
    def get_profile_ids(self):
        """
        Gets the profile name
        """
        return [self._profile_name]
    
