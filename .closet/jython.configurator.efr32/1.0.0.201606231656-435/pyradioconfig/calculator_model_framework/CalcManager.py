"""
Radio Configurator
"""

import os
import traceback
import sys
import types
import warnings
from enum import Enum

from pyradioconfig._version import __version__
from pyradioconfig.calculator_model_framework.Utils.CalcStatus import CalcStatus
from pyradioconfig.calculator_model_framework.Utils.ClassManager import ClassManager
from pyradioconfig.calculator_model_framework.Utils.CustomExceptions import UnknownOPNTypeException
from pyradioconfig.calculator_model_framework.Utils.FileUtilities import FileUtilities
from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pyradioconfig.calculator_model_framework.interfaces.idefault_phy import IDefaultPhy
from pyradioconfig.calculator_model_framework.interfaces.iphy import IPhy
from pyradioconfig.calculator_model_framework.interfaces.iphy_filter import IPhyFilter, PhyFilterGroupTypes
from pyradioconfig.calculator_model_framework.interfaces.iprofile import IProfile
from pyradioconfig.features.features import Features
from pyradioconfig.pycalcmodel import ModelRoot, ModelVariableEmptyValue
from pyradioconfig.pycalcmodel.core.variable import ModelVariableWriteAccess
from pyradioconfig.pycalcmodel.core.variable_access_name import VariableAccess
from pyradioconfig.calculator_model_framework.model_serializers.human_readable import Human_Readable
from pyradioconfig.calculator_model_framework.model_serializers.static_timestamp_xml import Static_TimeStamp_XML

class CalcManager(object):
    """
    Main interfaces to pyradioconfig.

    Args:
       part_family (str):  Part family name (e.g. 'dumbo').
       part_rev (str):  Part revision name (e.g. 'A0').

    Example usages:
        Create Radio Configurator Object:

        >>> radio_configurator = CalcManager(part_family='dumbo', part_rev='A0')

        Calculate PHY, generates output instance XML at output_dir and returns handle to model instance:

        >>> radio_configurator.calc_config_phy(phy_name = 'PHY_Datasheet_2450M_2GFSK_1Mbps_500K', output_dir='c:\some_directory')

        Calculate PHY, generates output instance XML at output_dir and returns handle to model instance, with optional inputs:

        >>> optional_inputs=dict()
        >>> optional_inputs['base_frequency_hz'] = 2402000000
        >>> radio_configurator.calc_config_phy(phy_name = 'PHY_Datasheet_2450M_2GFSK_1Mbps_500K', output_dir='c:\some_directory', optional_inputs=optional_inputs)

        Calculate Profile with inputs, generates output model XML instance:

        >>> model = radio_configurator.create_modem_model_instance(profile_name='Base')
        >>> model.inputs.base_frequency_hz.var_value = 915000000L
        >>> radio_configurator.calculateXMLInstance(model, output_path='c:\some_dir\output_instance.xml')

        Alternative calculate Profile with inputs, generates output model instance:

        >>> model = radio_configurator.create_modem_model_instance(profile_name='Base')
        >>> model.inputs.base_frequency_hz.var_value = 915000000L
        >>> radio_configurator.calculate(model_instance_profile)

        How to import .ISC file:

        >>> from pyradioconfig.calculator_model_framework.model_serializers.import_isc_files import ImportISCFiles
        >>> isc = ImportISCFiles()
        >>> inputs = isc.parse_file(test_isc_file_path)
        >>>
        >>> # Create model and fill with ISC file values
        >>> model_instance_input = radio_configurator.calc_config_profile(isc.profile, output_instance_file_path, inputs)
        >>>
        >>> # Calculate the model
        >>> result_code, error_message = radio_configurator.calculate(model_instance_input)

        Convert output instance model to XML file:

        >>> radio_configurator.processed_model_to_xml(model_instance_output, output_file='c:\temp\output.xml')

        For more details example usages, please review unittests.
    """

    # Static variables
    __MODEL_NAME = __name__
    __MODEL_VER = __version__
    __developer_mode = True

    # Private variables
    __part_family = None
    __part_revision = None

    def __init__(self, part_family = None, part_rev = None):
        """CalcManager Constructor.

        Args:
           part_family (str):  Part family name (e.g. 'dumbo').
           part_rev (str):  Part revision name (e.g. 'A0').

        Returns:
           CalcManager.
        """
        self.__part_family = part_family
        self.__part_revision = part_rev

    @property
    def part_family(self):
        """Part family getter

        Returns:
           part_family (str): Part family name (e.g. 'dumbo').

        """
        return self.__part_family

    @part_family.setter
    def part_family(self, part_family):
        """Part family setter

        Args:
           part_family (str): Part family name (e.g. 'dumbo').

        """
        self.__part_family = part_family

    @property
    def part_revision(self):
        """Part revision getter

        Returns:
           part_revision (str): Part revision (e.g. 'A0').

        """
        return self.__part_revision

    @part_revision.setter
    def part_revision(self, part_revision):
        """Part revision setter

        Args:
           part_revision (str): Part revision (e.g. 'A0').

        """
        self.__part_revision = part_revision

    @property
    def version(self):
        """pyradioconfig version getter

        Returns:
           version (str): pyradioconfig version (e.g. '1.0.2').

        """
        return self.__MODEL_VER

    @staticmethod
    def parseOPN(opn):
        """Parses OPN string into part_family, part_revision

        Args:
            opn (str) : Orderable Part Number,  (e.g. "EFR32fg1p133f256gm32-A0")

        Returns:
           part_family (str): Part family name (e.g. 'dumbo').
           part_revision (str): Part revision (e.g. 'A0').

        """
        # Used for unit testing
        if opn.lower().startswith('unit_test_part'):
            tempList = [x.strip() for x in opn.split('-')]
            partFamily = 'unit_test_part'
            partRevision = tempList[1].upper()
            return partFamily, partRevision
        # OPN decoder for EFR32
        elif opn.lower().startswith('efr32'):
            tempList = [x.strip() for x in opn.split('-')]
            partFamily = opn[5]
            if partFamily.lower() == 'f':
                partFamily = 'dumbo'
            partRevision = tempList[1].upper()
            return partFamily, partRevision
        # Unkown OPN type
        else:
            raise UnknownOPNTypeException('Unknown OPN type: ' + str(opn))

    def getProfiles(self):
        """Returns a list of profile objects

        Returns:
           uniqueProfiles (dict): Uniquely named profile objects

        """
        profileList = self.__getProfileList()
        uniqueProfiles = dict()

        for profile in profileList:
            # Check if profile is already in the dictionary
            key  = profile.getName()
            #if not uniqueProfiles.__contains__(key):
            # Add to dictionary
            uniqueProfiles[key] = profile

        return uniqueProfiles

    def __getProfileList(self):
        """Returns a list of all profile names for part family and part revision

        Returns:
           list (list): List of uniquely named profile

        """
        self.__verifyPartFamilyPartRevisionIsSet()
        part_family = self.__part_family
        part_revision = self.__part_revision
        try:
            list = []

            # Find all .py files for this family in common
            path = self.__getPartFamilyPath(part_family) + "/profiles/" + "__init__.py"
            list.extend(self.__getProfileListFromPath(path))

            # Find all .py files for this family and revision in part revision
            #path = self.__getPartFamilyPath(part_family) + "/" + part_revision + "/profiles/" + "__init__.py"
            #list.extend(self.__getProfileListFromPath(path))

            return list
        except ImportError:
            print "Unable to import modules at: %s" % (path,)
        except Exception:
            traceback.print_exc()

    def __getProfileListFromPath(self, path):
        """Returns a list of all profiles for part family and part revision

        Args:
            path (str) : Path to search for profile classes

        Returns:
           list (list): List of uniquely named profile classes
        """
        list = []

        # Import profile modules and classes
        classes = ClassManager.getClasses(path)
        for cls in classes:
            if issubclass(cls, IProfile):  # Make sure it is a Profile class
                # Add everything to list
                list.append(cls())

        return list

    def __getPartFamilyPath(self, part_family):
        """Helper function to build local path from part_family

        Args:
           part_family (str): Part family name (e.g. 'dumbo').

        Returns:
           path (str): Path to part family specific files
        """
        #path = os.path.join(os.path.dirname(__file__),  '..', 'parts', part_family)
        path = os.path.join(FileUtilities.resource_path(os.path.dirname(__file__)),  '..', 'parts', part_family)
        return path

    def __getPartCommonPath(self):
        path = os.path.join(FileUtilities.resource_path(os.path.dirname(__file__)),  '..', 'parts', 'common')
        return path

    def createXMLInstance(self, input_path, phy_name = None, profile_name = None):
        """Create model XML instance file

        Args:
            input_path (str) : Path to which XML instance is written to
            phy_name (str) : PHY name to create insance of (Optional, default = None)
            profile_name (str) : Profile name to create insance of (Optional, default = None)

        Returns:
           status (boolean): Returns True if no exceptions are caught
        """
        status = False
        try:
            # Convert version string to object
            #version = Version.fromString(version_string)

            modem_instance_model = self.create_modem_model_instance(phy_name)
            self.convert_model_instance_to_XML(modem_instance_model, input_path, phy_name = phy_name, profile_name = profile_name)

            status = True
        except:
            raise

        # return success / fail
        return status

    def convert_model_instance_to_XML(self, model, output_path, phy_name = None, profile_name = None):
        """Converts model instance to XML instance file

        Args:
            model (ModelRoot) : Data model instance
            output_path (str) : Path to which XML instance is written to
            phy_name (str) : PHY name to create insance of (Optional, default = None)
            profile_name (str) : Profile name to create insance of (Optional, default = None)
        """
        if phy_name is not None:
            phy = getattr(model.phys, phy_name)
        else:
            phy = None

        # Find profile requested
        #profile = self._findProfile(profile_name, profile_version_string)
        #if (profile == None):
        #    raise Exception("Profile: " +  profile_name + ", Version: " + profile_version_string + " not found.")

        # Build profile model
        #profile.buildProfileModel(modem_model)

        # Send modem model to file
        if profile_name is None:
            profile = getattr(model.profiles, phy.profile_name)
        else:
            profile = getattr(model.profiles, profile_name)

        if hasattr(model, 'processed'):
            processed = model.processed
        else:
            processed = False

        if hasattr(model, 'result_code'):
            result_code = model.result_code
        else:
            result_code = 0

        if hasattr(model, 'error_message'):
            error_message = model.error_message
        else:
            error_message = ''

        model.to_instance_xml(output_path, self.__part_revision, '', processed, result_code, error_message, profile, phy)  # New way

    def _findProfile(self, profile_name):
        """Finds profile for profile_name, version, part_family, part_revision

        Args:
            profile_name (str) : Profile name to create insance of (Optional, default = None)

        Returns:
           profile (Profile): Returns profile model object
        """
        profileFound = False
        profileList = self.__getProfileList()
        for profile in profileList:
            key  = profile.getName()
            if (profile_name == key):
                profileFound = True
                break

        if profileFound:
            return profile
        else:
            return None

    def calculateXMLInstance(self, modem_instance_model, output_path):
        """Create Input XML profile instance file

        Args:
            modem_instance_model (ModelRoot) : Data model instance
            output_path (str) : File path that the output calculated XML instance is written to

        Returns:
           result_code (int): Calculation return status codes
           error_message (str) : Calculation error message, if any (default = '')

        Example Usage:
            Calculate Profile with inputs, generates output model instance:

            >>> model = radio_configurator.create_modem_model_instance(profile_name='Base')
            >>> model.inputs.base_frequency_hz.var_value = 915000000L
            >>> radio_configurator.calculateXMLInstance(model, output_path='c:\some_dir\output_instance.xml')

            Alternative calculate Profile with inputs, generates output model instance:

            >>> model = radio_configurator.create_modem_model_instance(profile_name='Base')
            >>> model.inputs.base_frequency_hz.var_value = 915000000L
            >>> radio_configurator.calculate(model_instance_profile)
        """

        # Should only be one profile?  Should be only one
        result_code = CalcStatus.Success.value
        model_profile = None
        try:
            model_profile = modem_instance_model.profile
        except StopIteration:
            raise Exception("No profile in modem model!  Needs to have atleast one.")

        if model_profile is not None:
            try:
                # Create new model to absorb any new inputs, defaults, etc...
                modem_instance_model_new = self.create_modem_model_instance(profile_name=model_profile.name)
                self.read_profile_inputs_into_model(modem_instance_model_new, model_profile)
            except Exception, e:
                # Let the calculate function catch the error
                result_code = CalcStatus.Failure.value
                error_message = e.message
                pass

        # Run calculators
        if (result_code == CalcStatus.Success.value):
            result_code, error_message = self.execute_calc_fuctions(modem_instance_model_new)

        # Any phy's in here?  Could be one or none
        model_phy = None
        try:
            if result_code == CalcStatus.Success.value:
                model_phy = modem_instance_model.phy
                if model_phy is not None:
                    # add phy to new model
                    phy = self._findPhy(model_phy.name)
                    if not phy is None:
                        phy(modem_instance_model_new)
                        model_phy = modem_instance_model_new.phy
                    else:
                        model_phy = None
        except StopIteration:
            # ignore no phy found
            pass

        model_profile = modem_instance_model_new.profile

        # Send calculated modem model to file
        processed = True
        modem_instance_model_new.to_instance_xml(output_path,
                                                 modem_instance_model_new.part_revision,
                                                 '',
                                                 processed,
                                                 modem_instance_model_new.result_code,
                                                 modem_instance_model_new.error_message,
                                                 model_profile, model_phy)

        return result_code, error_message

    def execute_calc_fuctions(self, model_instance):
        """Executes all calacaultor functions on data model

        Args:
            modem_instance_model (ModelRoot) : Data model instance

        Returns:
           result (int): Calculation return status codes
           error_message (str) : Calculation error message, if any (default = '')
        """

        result = CalcStatus.Success.value
        error_message = ''

        try:
            # Get list of functions to perform calculators
            calcFunctions = self._getCalculatorFunctionList()
            self.calculateOverList(calcFunctions, model_instance)

            self.read_profile_outputs_from_modem_model(model_instance)
        except ModelVariableWriteAccess, e:
            # This is a show stopper (assert) for the calc functions!
            raise
        except Exception, e:
            result = CalcStatus.Failure.value
            error_message = str(e)
            if self.__developer_mode:
                raise
            else:
                print error_message
                print traceback.format_exc()

        model_instance.part_revision = self.part_revision
        model_instance.result_code = result
        model_instance.error_message = error_message
        model_instance.processed = True
        return result, error_message

    def _getCalculatorFunctionList(self):
        """Returns a list of all calculator functions for part family and part revision

        Returns:
           list (list): List of calculation function references
        """
        calculators = self._getCalculatorsList()
        list = []
        for calculator in calculators:
            list.extend(calculator.getCalculationList())

        return list

    def _getCalculatorsList(self):
        """Returns a list of all calculator objects for part family and part revision

        Returns:
           list (list): List of calculation object references
        """
        self.__verifyPartFamilyPartRevisionIsSet()
        part_family = self.__part_family
        part_revision = self.__part_revision

        # Find all part rev specific calculator .py files for this family
        # Loop through common calculators and remove and parent classes from part rev specific instance
        try:
            list = []
            class_type = ICalculator

            # Find all .py files for this part in common
            path = self.__getPartCommonPath() + "/calculators/" + "__init__.py"
            common_part_list = ClassManager.getClassListFromPath(path, class_type)

            # Find all .py files for this family in common
            #path = self.__getPartFamilyPath(part_family) + "/" + part_revision + "/calculators/" + "__init__.py"
            #common_rev_list = ClassManager.getClassListFromPath(path, class_type)

            # Loop through common phys and remove and parent classes from part rev specific instance
            #list = ClassManager.merge_lists_classes(common_rev_list, common_part_list)

            # Find all .py files for this family and revision in part revision
            path = self.__getPartFamilyPath(part_family) + "/calculators/" + "__init__.py"
            rev_list = ClassManager.getClassListFromPath(path, class_type)

            # Loop through common phys and remove and parent classes from part rev specific instance
            list = ClassManager.merge_lists_classes(common_part_list, rev_list)

            return list
        except ImportError:
            print "Unable to import modules at: %s" % (path,)
        except Exception:
            traceback.print_exc()

        return list

    def _getCalculatorsListFromPath(self, path):
        """Returns a list of all calculator objects for part family and part revision

        Args:
            path (str) : Path to search for all Calculator objects

        Returns:
           list (list): List of calcaulator object references
        """
        list = []

        # Import profile modules and classes
        classes = ClassManager.getClasses(path)
        for cls in classes:
            if issubclass(cls, ICalculator):  # Make sure it is a Calculator class
                # Add everything to list
                list.append(cls())

        return list

    def calculateOverList(self, calc_routine_list, modem_model):
        """Loop through all function pointers and execute calculators on model

        Args:
            calc_routine_list (list) : List of calcaultor functions to execute
            modem_model (ModelRoot) : Data model instance

        """
        # Validate model
        if not modem_model.validate():
            raise Exception('Model does not pass validation.  Please review vars and profile var definitions.')

        function  = VariableAccess()
        while True:
            num_calc_routines = calc_routine_list.__len__()
            #print "Number of routines = %d" % num_calc_routines

            for calc_routine in calc_routine_list[:]:       # The [:] thing is a trick to make a copy of the list.
                                                            # Don't iterate over a list while items are being removed from it.
                #print "About to call %s" % calc_routine.func_name
                try:
                    if isinstance(calc_routine, types.MethodType):
                        function.name = calc_routine.im_class.__name__ + "." + calc_routine.__name__ + "()"
                        calc_routine(modem_model)
                        #print "     Success!  %d left" % calc_routine_list.__len__()
                        calc_routine_list.remove(calc_routine)              # Remove the calc routine from the list if it didn't have errors
                        function.name = None
                except ModelVariableEmptyValue, e:
                    # Ignore when variable value has not been set
                    #print "     Undefined inputs found in %s.  Will try again on next pass" % calc_routine.func_name
                    pass
                #except Exception, e:
                #    traceback.print_exc(file=sys.stdout)
                #    print('DEBUG : ' + e.message)
                #    raise e
                finally:
                    function.name = None

            #print "************** Pass complete with %d routines left ******************" % calc_routine_list.__len__()

            if num_calc_routines == calc_routine_list.__len__():
                break

    def getPhys(self):
        """Returns a list of phys

        Returns:
           phyList (list) : List of Phy reference object functions
        """
        phyList = self._getPhyFunctionList()
        return phyList

    def _getPhyFunctionList(self):
        """Returns a list of all phy functions for part family and part revision

        Returns:
           list (list) : List of Phy reference object functions
        """
        phys = self.__getPhyList()
        list = []
        for phy in phys:
            list.extend(phy.getPhyList())

        return list

    def __getPhyList(self):
        """Returns a list of all phys for part family and part revision

        Returns:
           list (list) : List of Phy reference objects
        """
        self.__verifyPartFamilyPartRevisionIsSet()
        part_family = self.__part_family
        part_revision = self.__part_revision

        # Find all .py files for this family in common
        # Find all .py files for this family and revision in part revision
        # Loop through common phys and remove and parent classes from part rev specific instance
        common_path = self.__getPartFamilyPath(part_family) + "/phys/" + "__init__.py"
        #rev_path = self.__getPartFamilyPath(part_family) + "/" + part_revision + "/phys/" + "__init__.py"
        #list = ClassManager.mergeClassListsFromPaths(common_path, rev_path, IPhy)
        list = ClassManager.getClassListFromPath(common_path, IPhy)
        return list

    def read_phy_into_profile(self, phy_name, modem_model):
        """Load PHY values into Profile inputs in data model

        Args:
            phy_name (str) : Key name of the PHY in the model
            modem_model (ModelRoot) : Data model instance

        """
        phy = getattr(modem_model.phys, phy_name)
        profile_name = phy.profile_name
        profile = self._findProfile(profile_name)
        if profile is not None:
            profile.buildProfileModel(modem_model)

        phyFound = self._findPhy(phy_name)
        if not phyFound is None:
            phyFound(modem_model)

        # Assign Phy inputs to Profile Inputs
        profile_reference = getattr(modem_model.profiles, profile_name)
        for profile_input in phy.profile_inputs:
            variable = getattr(profile_reference.inputs, profile_input.var_name)
            value = profile_input.value
            if value is not None:
                variable.var_value = value

        # Assign Phy output overrides to Profile outputs overrides
        profile_reference = getattr(modem_model.profiles, profile_name)
        for profile_output in phy.profile_outputs:
            variable = getattr(profile_reference.outputs, profile_output.var_name)
            value = profile_output.override
            if value is not None:
                variable.override = value


    def read_profile_into_variables(self, modem_model):
        """Load Profile values into variables in data model

        Args:
            modem_model (ModelRoot) : Data model instance
        """
        profile = modem_model.profile

        # Assign defaults from Profile to Variables
        for input in profile.inputs:
            # Do not load deprecated values into model
            if input.default is not None and input.deprecated == False:
                variable = getattr(modem_model.vars, input.var_name)
                variable.value_forced = input.default

        # Assign forces from Profile to Variables
        for force in profile.forces:
            variable = getattr(modem_model.vars, force.var_name)
            if force.value is not None:
                variable.value_forced = force.value

        # Assign user inputs from Profile to Variables
        for input in profile.inputs:
            if input.var_value is not None:
                variable = getattr(modem_model.vars, input.var_name)
                variable.value_forced = input.var_value

        # Assign user inputs from Profile to Variables
        for output in profile.outputs:
            if output.override is not None:
                variable = getattr(modem_model.vars, output.var_name)
                variable.value_forced = output.override


    def create_modem_model_instance(self, phy_name=None, profile_name=None):
        """Creates an empty model instance for a PHY or Profile

        Args:
            phy_name (str) : PHY name to create insance of (Optional, default = None)
            profile_name (str) : Profile name to create insance of (Optional, default = None)
            Note: You must specify either a PHY name or Profile name.

        Returns:
            modem_model (ModelRoot) : Data model instance

        Example Usage:
            Calculate Profile with inputs, generates output model instance:

            >>> model = radio_configurator.create_modem_model_instance(profile_name='Base')
            >>> model.inputs.base_frequency_hz.var_value = 915000000L
            >>> radio_configurator.calculateXMLInstance(model, output_path='c:\some_dir\output_instance.xml')

        """
        self.__verifyPartFamilyPartRevisionIsSet()

        # Create empty modem model
        modem_model_instance = ModelRoot(self.__part_family, self.__MODEL_VER)

        # Build features
        Features.build(modem_model_instance)

        # Build calculator variables
        calculators = self._getCalculatorsList()
        for calculator in calculators:
            calculator.buildVariables(modem_model_instance)

        if profile_name is None:
            # Populate all profiles, since we don't know which one the Phy will need yet
            profiles = self.__getProfileList()
            for profile in profiles:
                profile.buildProfileModel(modem_model_instance)
        else:
            # Only make the profile needed
            profile = self._findProfile(profile_name)
            if profile is not None:
                profile.buildProfileModel(modem_model_instance)

        # Find and build phy
        if phy_name is not None:
            phy = self._findPhy(phy_name)
            if not phy is None:
                phy(modem_model_instance)

            if profile_name is None:
                # Hack to remove profiles we don't need for this phy
                phy_object = getattr(modem_model_instance.phys, phy_name)
                profile_name = phy_object.profile_name
                modem_model_instance.profiles.clear()
                profile = self._findProfile(profile_name)
                if profile is not None:
                    profile.buildProfileModel(modem_model_instance)

        # Add default pnys
        #self._buildDefaultPhys(modem_model_instance)

        return modem_model_instance

    def create_modem_model_type(self):
        """Creates a type model for current part family and revision

        Returns:
            modem_model (ModelRoot) : Data model type (lists all phys, profiles, varaibles, etc...)
        """
        self.__verifyPartFamilyPartRevisionIsSet()

        # Create empty modem model
        modem_type_model = ModelRoot(self.__part_family, self.__MODEL_VER)

        # Build features
        Features.build(modem_type_model)

        # Build calculator variables
        calculators = self._getCalculatorsList()
        for calculator in calculators:
            calculator.buildVariables(modem_type_model)

        # Build model with all profiles
        profiles = self.__getProfileList()
        for profile in profiles:
            profile.buildProfileModel(modem_type_model)

        # Build model with all phys
        phys = self._getPhyFunctionList()
        for phy in phys:
            phy(modem_type_model)

        # Add default pnys
        self._buildDefaultPhys(modem_type_model)

        return modem_type_model

    def _findPhy(self, phy_name):
        """Finds phy for phy_name, version, part_family, part_revision

        Args:
            phy_name (str) : PHY name to find

        Returns:
            phy_function (function) : PHY function reference
        """
        phyFound = False
        phyList = self.__getPhyList()
        for phy in phyList:
            phy_functions = phy.getPhyList()
            for phy_function in phy_functions:
                key  = phy_function.__name__
                if (phy_name == key):
                    phyFound = True
                    break

            if phyFound:
                break

        if phyFound:
            return phy_function
        else:
            return None

    def read_profile_outputs_from_modem_model(self, modem_instance_model):
        """Deprecated: Reads profile outputs from modem model

        Args:
            modem_instance_model (ModelRoot) : Model instance
        """
        warnings.warn("deprecated", DeprecationWarning)
        # Deprecated
        #for profile in modem_instance_model.profiles:
        #    for output in profile.outputs:
        #        variable = getattr(modem_instance_model.vars, output.var_name)
        #        if variable.value is not None:
        #            output.var_value = variable.value
        pass


    def read_profile_inputs_into_model(self, modem_model, model_profile):
        """Reads inputs from profile object into model

        Args:
            modem_model (ModelRoot) : Data model to read into
            model_profile (Profile) : Profile object with input values
        """

        profile_name = model_profile.name
        profile = self._findProfile(profile_name)
        if profile is not None:
            profile.buildProfileModel(modem_model)

        self.read_profile_into_variables(modem_model)

        profile_new = getattr(modem_model.profiles, profile_name)
        # Copy over input values
        for input in model_profile.inputs:
            if input.var_value is not None:
                input_new = getattr(profile_new.inputs, input.var_name)
                input_new.var_value = input.var_value

        # Copy over output overrides
        for output in model_profile.outputs:
            if output.override is not None:
                output_new = getattr(profile_new.outputs, output.var_name)
                output_new.override = output.override

        # Assign user inputs from Model Profile to Variables
        for input in profile_new.inputs:
            if input.var_value is not None:
                variable = getattr(modem_model.vars, input.var_name)
                variable.value_forced = input.var_value

        # Assign user outputs from Model Profile to Variables
        for output in profile_new.outputs:
            if output.override is not None:
                variable = getattr(modem_model.vars, output.var_name)
                variable.value_forced = output.override


    def __verifyPartFamilyPartRevisionIsSet(self):
        """Verifies part family and revision is set

        Returns:
            Succesful (boolean) : Both part family and revision are not None.

        Raises:
            Exception is either part family or revision is None
        """
        if self.__part_family is None:
            raise Exception("Part family must be set!")
        if self.__part_revision is None:
            raise Exception("Part revision must be set!")
        return True

    def getPhyNames(self):
        """Gets a list of PHY names

        Returns:
            phy_names (list) : List of PHY name strings
        """

        phy_names = list()
        for phy in self.getPhys():
            phy_names.append(phy.__name__)

        return phy_names

    def create_modem_model_instance_and_load_phy(self, phy_name=None):
        """Creates a modem model instance and loads PHY

        Args:
            phy_name (str) : PHY name to load

        Returns:
            model_instance (MOdelRoot) : New instance of data model with single PHY
        """
        model_instance = self.create_modem_model_instance(phy_name)
        self.read_phy_into_profile(phy_name, model_instance)
        return model_instance


    def calculate(self, model_instance):
        """Executes all calaualtor functions agains modek variables

        Args:
            model_instance (ModelRoot) : Data model with variables to run through calcaultions

        Returns:
           result_code (int): Calculation return status codes
           error_message (str) : Calculation error message, if any (default = '')
        """
        self.read_profile_into_variables(model_instance)
        result_code, error_message = self.execute_calc_fuctions(model_instance)
        return result_code, error_message

    def calculate_phy(self, phy_name=None, optional_inputs=dict()):
        model_instance = self.create_modem_model_instance_and_load_phy(phy_name)

        model_instance = self.load_input_dictionary_into_model(model_instance, optional_inputs)

        result_code, error_message = self.calculate(model_instance)
        return model_instance

    def load_input_dictionary_into_model(self, model_instance, inputs=dict()):
        """Loads input dictionary into model instance

        Args:
            model_instance (ModelRoot) : Data model to load inputds into
            inputs (dict) : Dictionary of input values.  Key is var_name and Value is var_value

        Returns:
            model_instance (ModelRoot) : Updated data model
        """
        for key, value in inputs.iteritems():
            # process option inputs into profile inputs
            try:
                input = getattr(model_instance.profile.inputs, key)
                if input._var.var_type != Enum:
                    input.var_value = (input._var.var_type)(value)
                else:
                    if isinstance(value, basestring):
                        if value.isdigit():
                            value = int(value)
                            enum_val = input._var.var_enum(value)
                        else:
                            enum_val = getattr(input._var.var_enum, value)
                    input.var_value = enum_val
            except AttributeError, e:
                raise Exception(key + ' is not a valid profile input.')

        return model_instance

    def calc_config_phy(self, phy_name, output_dir=None, optional_inputs=dict(), optional_filename=None):
        """Run the calculator and generate the calculated outputs for a single PHY

        Args:
            phy_name (str) : Name of PHY to run through the calcaultor.
            output_dir (str) : Directory path where output files are generate.
            optional_inputs (dict) : Dictionary of input values.  Key is var_name and Value is var_value [Optional Input].
            optional_filename (string) : Filename to use when generating the output files. [Optional Input: Defaults to phy_name if not specified.].

        Returns:
            model_instance (ModelRoot) : calculated data model instance

        Example usages:
            Calculate PHY, generates output instance XML at output_dir and returns handle to model instance:

            >>> radio_configurator.calc_config_phy(phy_name = 'PHY_Datasheet_2450M_2GFSK_1Mbps_500K', output_dir='c:\some_directory')

            Calculate PHY, generates output instance XML at output_dir and returns handle to model instance, with optional inputs:

            >>> optional_inputs=dict()
            >>> optional_inputs['base_frequency_hz'] = 2402000000
            >>> radio_configurator.calc_config_phy(phy_name = 'PHY_Datasheet_2450M_2GFSK_1Mbps_500K', output_dir='c:\some_directory', optional_inputs=optional_inputs)
        """

        # Force path to end with "/"
        output_dir = os.path.normpath(output_dir) + os.sep

        if optional_filename is None:
            optional_filename = phy_name + ".xml"
        elif not optional_filename.lower().endswith('.xml'):
            optional_filename = optional_filename + ".xml"

        output_path = output_dir + optional_filename
        model_instance = self.calc_config(phy_name, output_path, optional_inputs)

        return model_instance

    def calc_config(self, phy_name, output_path, optional_inputs=dict()):
        """Run the calculator and generate the calculated outputs for a single PHY

        Args:
            phy_name (str) : Name of PHY to run through the calcaultor.
            output_path (str) : Full path to output file
            optional_inputs (dict) : Dictionary of input values.  Key is var_name and Value is var_value [Optional Input].

        Returns:
            model_instance (ModelRoot) : calculated data model instance

        Example usages:
            Calculate PHY, generates output instance XML at output_dir and returns handle to model instance:

            >>> radio_configurator.calc_config(phy_name = 'PHY_Datasheet_2450M_2GFSK_1Mbps_500K', output_path='c:\some_directory\phy_name.xml')

            Calculate PHY, generates output instance XML at output_dir and returns handle to model instance, with optional inputs:

            >>> optional_inputs=dict()
            >>> optional_inputs['base_frequency_hz'] = 2402000000
            >>> radio_configurator.calc_config(phy_name = 'PHY_Datasheet_2450M_2GFSK_1Mbps_500K', output_path='c:\some_directory', optional_inputs=optional_inputs)
        """

        # Load instance model with phy variables
        # call top level calculator function
        model_instance = self.calculate_phy(phy_name, optional_inputs)

        if bool(optional_inputs):
            # Not an empty dictionary of optional input overrides
            #optional_filename = optional_filename + "_with_input_overrides"
            comment = phy_name + " instance with overrides"
        else:
            comment = phy_name + " instance"

        if model_instance.result_code != CalcStatus.Failure.value:
            # print the results to a .cfg file
            output_path_cfg = output_path.replace(".xml", "")
            output_path_cfg = output_path_cfg.replace(".XML", "")
            output_path_cfg = output_path_cfg + ".cfg"
            Human_Readable.print_modem_model_values_v2(output_path_cfg, phy_name, model_instance)

            # Now look for variables that were forced unnecessarily
            output_lines = Human_Readable.compare_forced_to_calculated(model_instance)

            # print to XML file
            Static_TimeStamp_XML.print_modem_model_values_xml(output_path, phy_name, model_instance, comment)
        else:
            # Some error happened, letting that bubble up
            pass

        return model_instance


    def calc_config_profile(self, profile_name, output_file_path, optional_inputs=dict()):
        """Run the calculator and generate the calculated outputs

        Args:
            profile_name (str) : Name of Profile to run through the calculator
            output_file_path (str) : Full file name of output file
            optional_inputs (dict) : Dictionary of input values.  Key is var_name and Value is var_value [Optional Input]

        Returns:
            model_instance (ModelRoot) : calculated data model instance
        """

        model_instance = self.create_modem_model_instance(phy_name=None, profile_name=profile_name)
        model_instance = self.load_input_dictionary_into_model(model_instance, optional_inputs)

        # Run calculations
        result_code, error_message = self.calculate(model_instance)

        if model_instance.result_code != CalcStatus.Failure.value:
            # Create output instance XML
            self.convert_model_instance_to_XML(model_instance, output_file_path, phy_name = None, profile_name = profile_name)
        else:
            # Some error happened, letting that bubble up
            return None

        return model_instance

    def filter_out_phy_group_names(self, model, phy_group_to_exclude):
        """Get list of PHYs from model, filtering out the phy_group_to_exclude

        Args:
            model (ModelRoot) : Data model to filter out phys from
            phy_group_to_exclude (list) : List of PHYs to exclude

        Returns:
            filtered_phys (list) : List of PHY's with filters excluded
        """
        filtered_phys = list()
        for phy in model.phys:
            if phy.group_name not in phy_group_to_exclude:
                filtered_phys.append(phy)
            #else:
            #    print "skipping {0}.{1}".format(phy.group_name, phy.name)

        return filtered_phys

    def find_all_phys_of_group_name(self, model, phy_group_to_include):
        """Get list of PHYs from model, including only phy_group_to_include

        Args:
            model (ModelRoot) : Data model to filter out phys from
            phy_group_to_include (list) : List of PHYs to include

        Returns:
            filtered_phys (list) : List of PHY's with filters included
        """
        filtered_phys = list()
        for phy in model.phys:
            if phy.group_name in phy_group_to_include:
                filtered_phys.append(phy)

        return filtered_phys

    def filter_out_phy_group_names_to_phy_group_name_list(self, model, phy_group_to_exclude):
        """Get list of PHYs from model, excluding phys with groups in phy_group_to_exclude

        Args:
            model (ModelRoot) : Data model to filter out phys from
            phy_group_to_exclude (list) : List of PHY groups to exclude

        Returns:
            filtered_phy_group_names (list) : List of PHY's with group filters excluded
        """
        filtered_phy_group_names = list()
        for phy in model.phys:
            if phy.group_name not in phy_group_to_exclude:
                filtered_phy_group_names.append(phy.group_name)

        return filtered_phy_group_names

    def find_all_phy_group_names_in_phy_group_name_list(self, model, phy_group_to_include):
        """Get list of PHYs from model, including phys with groups in phy_group_to_include

        Args:
            model (ModelRoot) : Data model to filter out phys from
            phy_group_to_include (list) : List of PHY groups to include

        Returns:
            filtered_phy_group_names (list) : List of PHY's with group filters included
        """
        filtered_phy_group_names = list()
        for phy in model.phys:
            if phy.group_name in phy_group_to_include:
                filtered_phy_group_names.append(phy.group_name)

        return filtered_phy_group_names

    def _get_filter_phy_groups(self):
        """Gets list of PHY filter groups for part family and revision

        Returns:
            classlist (list) : List of PHY groups needed to be filtered
        """
        self.__verifyPartFamilyPartRevisionIsSet()
        part_family = self.__part_family
        part_revision = self.__part_revision

        # Find all .py files for this family in common
        # Find all .py files for this family and revision in part revision
        # Loop through common phys and remove and parent classes from part rev specific instance
        common_path = self.__getPartFamilyPath(part_family) + "/filters/" + "__init__.py"
        #rev_path = self.__getPartFamilyPath(part_family) + "/" + part_revision + "/filters/" + "__init__.py"
        #classlist = ClassManager.mergeClassListsFromPaths(common_path, rev_path, IPhyFilter)
        classlist = ClassManager.getClassListFromPath(common_path, IPhyFilter)
        return classlist

    def _get_phy_groups(self, phy_filter_group_types):
        """Gets list of PHY's base on group types

        Args:
            phy_filter_group_types (Enum: PhyFilterGroupTypes) : PHY group type to get

        Returns:
            filterList (list) : List of PHYs in group
        """
        classlist = self._get_filter_phy_groups()

        filterList = []
        for filter in classlist:
            tempList = filter.get_phy_filter_groups(phy_filter_group_types)
            filterList = list(set(filterList + tempList))

        return filterList

    def get_customer_phy_groups(self):
        """Gets list customer PHYs

        Returns:
            filterList (list) : List of PHYs of group type
        """
        return self._get_phy_groups(PhyFilterGroupTypes.customer_phys)

    def get_sim_tests_phy_groups(self):
        """Gets list simulation PHYs

        Returns:
            filterList (list) : List of PHYs of group type
        """
        return self._get_phy_groups(PhyFilterGroupTypes.sim_tests_phys)

    def get_simplicity_studio_phy_groups(self):
        """Gets list Simplicity Studio PHYs

        Returns:
            filterList (list) : List of PHYs of group type
        """
        return self._get_phy_groups(PhyFilterGroupTypes.simplicity_studio_phys)

    def get_non_functional_phy_groups(self):
        """Gets list non-functional PHYs

        Returns:
            filterList (list) : List of PHYs of group type
        """
        return self._get_phy_groups(PhyFilterGroupTypes.non_functional_phys)

    def _buildDefaultPhys(self, modem_type_model):
        """Builds all PHY's into empty data model

        Args:
            modem_type_model (ModelRoot) : Empty data model to fill
        """
        list = self.__getDefaultPhyList()
        for default_phy in list:
            default_phy.build(modem_type_model)

    def __getDefaultPhyList(self):
        """Gets a list of default PHYs

        Returns:
            list (list) : List of PHY objects for part family and revision
        """
        self.__verifyPartFamilyPartRevisionIsSet()
        part_family = self.__part_family
        part_revision = self.__part_revision
        try:
            list = []

            # Find all .py files for this family in common
            path = self.__getPartFamilyPath(part_family) + "/phys/" + "__init__.py"
            list.extend(self.__getDefaultPhyListFromPath(path))

            # Find all .py files for this family and revision in part revision
            #path = self.__getPartFamilyPath(part_family) + "/" + part_revision + "/phys/" + "__init__.py"
            #list.extend(self.__getDefaultPhyListFromPath(path))

            return list
        except ImportError:
            print "Unable to import modules at: %s" % (path,)
        except Exception:
            traceback.print_exc()

    def __getDefaultPhyListFromPath(self, path):
        """Returns a list of all profiles for part family and part revision

        Args:
            path (str) : Path to search for PHY listing

        Returns:
            list (list) : List of PHY objects for part family and revision
        """
        list = []

        # Import profile modules and classes
        classes = ClassManager.getClasses(path)
        for cls in classes:
            if issubclass(cls, IDefaultPhy):  # Make sure it is a Profile class
                # Add everything to list
                list.append(cls())

        return list

    def processed_model_to_xml(self, model_instance, output_file):
        """Converts output instance model to an XML file

        Args:
            model_instance (ModelRoot) : Data model instance
            output_file (str) : Full fiel path name to marshal to XML file

        Returns:
            list (list) : List of PHY objects for part family and revision
        """
        if hasattr(model_instance, 'phy'):
            phy = model_instance.phy
            desc = phy.name
        else:
            desc = os.path.basename(output_file)
            phy = None
        profile = model_instance.profile
        result_code = model_instance.result_code
        error_message = model_instance.error_message
        model_instance.to_instance_xml(output_file, self.__part_revision, desc, True, result_code, error_message, profile, phy)
