import os
from unittest import TestCase
import unittest
from enum import Enum
from pyradioconfig.calculator_model_framework.CalcManager import CalcManager
from pyradioconfig.calculator_model_framework.Utils.CustomExceptions import UnknownOPNTypeException
from pyradioconfig.features.features import Features
from pyradioconfig.pycalcmodel import ModelRootInstanceXml
from pyradioconfig._version import __version__ as calculator_version
from pyradioconfig.pycalcmodel import ModelRoot


class TestCalcManager(TestCase):

    current_path = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_path, 'calculated_output')
    part_family = "dumbo"
    part_rev = "A0"

    # Hack override used to allow the test to run from python console
    def runTest( self ):
     self.failUnless( True is True )

    def test_getProfilesFromOPN(self):
        opn = "EFR32fg1p133f256gm32-A0"
        part_family, part_revision = CalcManager.parseOPN(opn)
        calMgr = CalcManager(part_family, part_revision)
        profiles = calMgr.getProfiles()
        print "profiles = " + str(profiles)
        self.assertTrue(len(profiles) > 0)
        key, value = profiles.popitem()
        # Confirm we got more than one instance back
        self.assertTrue(len(key) > 0)

    def test_create_then_import_instance_profile_only(self):
        self.createXMLInstanceWithProfile()
        self.calculateXMLInstance()

    def test_create_then_import_instance_from_phy(self):
        self.createXMLInstanceWithPhy()
        self.calculateXMLInstance()

    def createXMLInstanceWithProfile(self):
        part_family = "dumbo"
        part_revision = "A0"
        calMgr = CalcManager(part_family, part_revision)
        current_path = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(current_path, 'calculated_output')
        test_fn = 'test_full.xml'
        try:
            os.remove(output_dir + "\\" + test_fn)
        except:
            pass
        calMgr.createXMLInstance(output_dir + "\\" + test_fn, profile_name="Base")
        self.assertTrue(os.path.exists(output_dir + "\\" + test_fn))

    def createXMLInstanceWithPhy(self):
        part_family = "dumbo"
        part_revision = "A0"
        calMgr = CalcManager(part_family, part_revision)
        current_path = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(current_path, 'calculated_output')
        test_fn = 'test_full.xml'
        try:
            os.remove(output_dir + "\\" + test_fn)
        except:
            pass
        calMgr.createXMLInstance(output_dir + "\\" + test_fn, phy_name="PHY_Essence_868M_38p4kbps")
        self.assertTrue(os.path.exists(output_dir + "\\" + test_fn))

    def calculateXMLInstance(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(current_path, 'calculated_output')
        test_file_input = 'test_full.xml'
        test_file_output = 'test_output.xml'
        try:
              os.remove(output_dir + "\\" + test_file_output)
        except:
            pass

        # Create manager without part family and revision
        calMgr = CalcManager()

        # Get part family and revision from instance file
        modem_instance_model = ModelRootInstanceXml(output_dir + "\\" + test_file_input)
        part_family = modem_instance_model.part_family
        part_revision = modem_instance_model.part_revision
        print "part_family = " + part_family
        print "part_revision = " + part_revision
        self.assertEquals("dumbo", part_family)
        self.assertEquals("A0", part_revision)

        # Load back into CalcManager
        calMgr.part_family = part_family
        calMgr.part_revision = part_revision
        calMgr.calculateXMLInstance(modem_instance_model, output_dir + "\\" + test_file_output)
        self.assertTrue(os.path.exists(output_dir + "\\" + test_file_output))

    def test_createXMLInstanceException(self):
        part_family = "unit_test_part"
        part_revision = "A0"
        calMgr = CalcManager(part_family, part_revision)
        self.assertRaises(Exception, calMgr.createXMLInstance, "PHY_Fake", "9.9.9")

    # Test valid parser
    def test_parseOPN(self):
      part_family, part_revision = CalcManager.parseOPN("EFR32FG1P133F256GM32-A0")
      self.assertEquals("dumbo", part_family)
      self.assertEquals("A0", part_revision)

    # Test whether exception is caught
    def test_parseOPNException(self):
      self.assertRaises(UnknownOPNTypeException, CalcManager.parseOPN, "ERROR_FG1P133F256GM32-A0")

    # Test whether exception is caught
    def test_CalcManager_NoPartSet_Exception(self):

      self.createXMLInstanceWithProfile()

      current_path = os.path.dirname(os.path.abspath(__file__))
      output_dir = os.path.join(current_path, 'calculated_output')
      test_file_input = 'test_full.xml'
      test_file_output = 'test_output.xml'
      calMgr = CalcManager()
      modem_instance_model = ModelRootInstanceXml(output_dir + "\\" + test_file_input)
      # Since part family and revision is not set, should throw an exception
      #self.assertRaises(Exception, calMgr.calculateXMLInstance, modem_instance_model, output_dir + "\\" + test_file_output)


    def test_CalcManager_version(self):
      calMgr = CalcManager()
      version = calMgr.version
      print version

    def test_create_type_XML(self):
      # Build Modem Model Type and write to type file
      radio_configurator = CalcManager(self.part_family, self.part_rev)
      type_model = radio_configurator.create_modem_model_type()
      file_name = self.output_dir + "/" + self.part_family + "_" + self.part_rev + "_type.xml"
      type_model.to_type_xml(file_name)
      self.assertTrue(file_name)

    def test_EfrListCalculatorFunctions(self):
        part_family = "dumbo"
        part_revision = "A0"
        calMgr = CalcManager(part_family, part_revision)
        calcFunctions = calMgr._getCalculatorFunctionList()

        # Got some functions back?
        self.assertTrue(len(calcFunctions) > 0)

        for calc in calcFunctions:
            print calc.__name__

    def test_EfrBuildVariables(self):
        part_family = "dumbo"
        part_revision = "A0"
        calMgr = CalcManager(part_family, part_revision)
       # Create empty modem model
        version = calculator_version
        modem_model = ModelRoot(part_family, version)

        # Build features
        Features.build(modem_model)

        # Build calculator variables
        calculators = calMgr._getCalculatorsList()
        for calculator in calculators:
            calculator.buildVariables(modem_model)

        # Got some vars back?
        self.assertTrue(len(modem_model.vars.ZZ_VARIABLE_KEYS) > 0)

        for var in modem_model.vars:
            print var.name

    def test_create_modem_model_instance_empyt(self):
        calcManager = CalcManager(self.part_family, self.part_rev)
        modem_instance_model = calcManager.create_modem_model_instance()

        # Got some vars back?
        self.assertTrue(len(modem_instance_model.vars.ZZ_VARIABLE_KEYS) > 0)

        for var in modem_instance_model.vars:
            print var.name

    def test_create_modem_model_instance_profile(self):
        calcManager = CalcManager(self.part_family, self.part_rev)
        modem_instance_model = calcManager.create_modem_model_instance(profile_name='Base')

        # Got some vars back?
        self.assertTrue(len(modem_instance_model.profiles.ZZ_PROFILE_KEYS) > 0)
        self.assertTrue('Base' in modem_instance_model.profiles.ZZ_PROFILE_KEYS)

    def test_create_modem_model_instance_phy(self):
        calcManager = CalcManager(self.part_family, self.part_rev)
        modem_instance_model = calcManager.create_modem_model_instance(phy_name="PHY_Bluetooth_LE_Narrow_CHBW")

        # Got some vars back?
        self.assertTrue(len(modem_instance_model.phys.ZZ_PHY_KEYS) > 0)
        self.assertTrue('PHY_Bluetooth_LE_Narrow_CHBW' in modem_instance_model.phys.ZZ_PHY_KEYS)

    def test_profile_min_max_values(self):
        radio_configurator = CalcManager(self.part_family, self.part_rev)
        type_model = radio_configurator.create_modem_model_type()

        for profile in type_model.profiles:
            # Loop through all inputs and check that min and max alues exist
            for input in profile.inputs:
                if input._var.var_type != bool and input._var.var_type != Enum:
                    if input.value_limit_max is None:
                        message = profile.name + " profile input " + input.var_name + " max value missing.  Var type is " + str(input._var.var_type)
                        print(message)
                        self.assertTrue(False, message)
                    if input.value_limit_min is None:
                        message = profile.name + " profile input " + input.var_name + " min value missing.  Var type is " + str(input._var.var_type)
                        print(message)
                        self.assertTrue(False, message)

    def test_phy_values(self):
        radio_configurator = CalcManager(self.part_family, self.part_rev)
        type_model = radio_configurator.create_modem_model_type()

        for phy in type_model.phys:
            for profile_input in phy.profile_inputs:
                # Test casting type
                self.assertTrue(profile_input._var.validate_type(profile_input.value), profile_input.var_name + ' is of the wrong type. Should be ' + str(profile_input._var.var_type))

                # Checking against min and max
                if profile_input._var.var_type != bool and profile_input._var.var_type != Enum:
                    input = getattr(phy._profile.inputs, profile_input.var_name)
                    if profile_input.value is not None:
                        if not input._var.is_array:
                            if profile_input.value < input.value_limit_min:
                                message = phy.name + " " + profile_input.var_name + " input value is below minimum.  " + str(profile_input.value) + " < " + str(input.value_limit_min)
                                print(message)
                                self.assertTrue(profile_input.value < input.value_limit_min, message)

                            if profile_input.value > input.value_limit_max:
                                message = phy.name + " " + profile_input.var_name + " input value is above maximum.  " + str(profile_input.value) + " > " + str(input.value_limit_max)
                                print(message)
                                self.assertTrue(profile_input.value > input.value_limit_max, message)
                        else:
                            counter = 0
                            for value in profile_input.value:
                                if value < input.value_limit_min:
                                    message = phy.name + " " + profile_input.var_name + " input[" + str(counter) + "] value is below minimum.  " + str(value) + " < " + str(input.value_limit_min)
                                    print(message)
                                    self.assertTrue(profile_input.value < input.value_limit_min, message)

                                if value > input.value_limit_max:
                                    message = phy.name + " " + profile_input.var_name + " input[" + str(counter) + "] value is above maximum.  " + str(value) + " > " + str(input.value_limit_max)
                                    print(message)
                                    self.assertTrue(profile_input.value > input.value_limit_max, message)

                                counter += 1

            #for profile_output in phy.profile_outputs:
            #    # Test casting type
            #    self.assertTrue(profile_output._var.validate_type(profile_output.override), profile_output.var_name + ' is of the wrong type. Should be ' + str(profile_output._var.var_type))
            #
            #    if profile_output._var.var_type != bool and profile_output._var.var_type != Enum:
            #        output = getattr(phy._profile.outputs, profile_output.var_name)
            #        if profile_output.override is not None:
            #            if not output._var.is_array:
            #                if profile_output.override < output.value_limit_min:
            #                    message = phy.name + " " + profile_output.var_name + " output override is below minimum.  " + str(profile_output.override) + " < " + str(output.override_limit_min)
            #                    print(message)
            #                    #self.assertTrue(profile_output.override < output.override_limit_min, message)
            #
            #                if profile_output.override > output.value_limit_max:
            #                    message = phy.name + " " + profile_output.var_name + " output override is above maximum.  " + str(profile_output.override) + " > " + str(output.value_limit_max)
            #                    print(message)
            #                    #self.assertTrue(profile_output.override > output.value_limit_max, message)
            #            else:
            #                counter = 0
            #                for value in profile_output.override:
            #                    if value < output.value_limit_min:
            #                        message = phy.name + " " + profile_output.var_name + " output]" + str(counter) + "] override is below minimum.  " + str(value) + " < " + str(output.value_limit_min)
            #                        print(message)
            #                        #self.assertTrue(profile_output.override < output.value_limit_min, message)
            #
            #                    if value > output.value_limit_max:
            #                        message = phy.name + " " + profile_output.var_name + " output[" + str(counter) + "] override is above maximum.  " + str(value) + " > " + str(output.value_limit_max)
            #                        print(message)
            #                        #self.assertTrue(profile_output.override > output.value_limit_max, message)
            #
            #                    counter += 1

    def test_profile_fractional_digits(self):
        radio_configurator = CalcManager(self.part_family, self.part_rev)
        type_model = radio_configurator.create_modem_model_type()

        for profile in type_model.profiles:
            # Loop through all inputs and check that min and max alues exist
            for input in profile.inputs:
                if input._var.var_type == float:
                    if input.fractional_digits is None:
                        message = profile.name + " profile input " + input.var_name + " is float, but has no fractional_digits set."
                        print(message)
                        self.assertTrue(False, message)

    def test_ExistanceOfProfiles(self):
        default_profile_found = False
        radio_configurator = CalcManager(self.part_family, self.part_rev)
        type_model = radio_configurator.create_modem_model_type()

        for profile in type_model.profiles:
            if profile.default == True:
                default_profile_found = True
                break

        self.assertTrue(default_profile_found, 'Need at least on default profile')

    def test_ExistanceOfProfiles(self):
        radio_configurator = CalcManager(self.part_family, self.part_rev)
        type_model = radio_configurator.create_modem_model_type()

        for profile in type_model.profiles:
            for input in profile.inputs:
                # each input should have it's properties set
                self.assertIsNotNone(input.input_type)
                self.assertIsNotNone(input._var.var_type)
                self.assertIsNotNone(input._var.format)
                self.assertTrue(input.var_name is not None, str(input) + ' var_name should not be None')
                self.assertFalse(input.var_name.strip() == '', str(input) + ' var_name should not be Empty')
                self.assertIsNotNone(input.category)
                self.assertFalse(input.category.strip() == '')

    def test_PhysInputType(self):
        radio_configurator = CalcManager(self.part_family, self.part_rev)
        type_model = radio_configurator.create_modem_model_type()

        for phy in type_model.phys:
            for profile_input in phy.profile_inputs:
                if profile_input.value is not None:
                    try:
                        if profile_input._var.var_type == Enum:
                            self.assertTrue(issubclass(type(profile_input.value), Enum))
                            val = profile_input._var.var_enum(profile_input.value.value)
                        else:
                            val = (profile_input._var.var_type)(profile_input.value)
                    except Exception, e:
                        message = profile_input.var_name + ' has an invalid value (' + str(profile_input.value) + '). ' + str(e.message)
                        print(message)
                        raise Exception(message)

    @unittest.skip("Disabled.  Not all defaults set.")
    def test_ProfileInputDefaultValueExistance(self):
        radio_configurator = CalcManager(self.part_family, self.part_rev)
        type_model = radio_configurator.create_modem_model_type()

        for profile in type_model.profiles:
            for input in profile.inputs:
                self.assertIsNotNone(input.default, 'Profile ' + str(profile.name) + ' input default ' + input.var_name + ' is None.')
