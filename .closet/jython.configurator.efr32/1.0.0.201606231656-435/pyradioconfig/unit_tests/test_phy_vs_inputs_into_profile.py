import os
import inspect
from unittest import TestCase
import datetime
from pyradioconfig import CalcManager
from pyradioconfig.calculator_model_framework.Utils.ClassManager import ClassManager
from pyradioconfig.calculator_model_framework.model_serializers.human_readable import Human_Readable
from pyradioconfig.calculator_model_framework.model_serializers.static_timestamp_xml import Static_TimeStamp_XML


class TestPhyVsInputsIntoProfile(TestCase):

    # Hack override used to allow the test to run from python console
    def runTest( self ):
        self.failUnless( True is True )

    def setUp(self):
        self.part_family = "dumbo"
        self.part_revision = "A0"
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.calc_output_dir = os.path.join(self.current_path, 'calculated_output')
        self.radio_configurator = CalcManager(self.part_family, self.part_revision)

    def tearDown(self):
        self.radio_configurator = None

    def test_load_phy_vs_inputs(self):
        type_model = self.radio_configurator.create_modem_model_type()

        for phy in type_model.phys:
            # phy_name = 'PHY_Datasheet_2450M_2GFSK_1Mbps_500K'
            # phy_name = "PHY_Datasheet_169M_2GFSK_38p4Kbps_20K"
            self.load_phy_vs_inputs(phy.name)

    def load_phy_vs_inputs(self, phy_name):
        print("Testing PHY vs Profile inputs for: " + phy_name)
        model_instance_phy = self.radio_configurator.calc_config_phy(phy_name, output_dir=self.calc_output_dir)

        model_instance_profile = self.radio_configurator.create_modem_model_instance(profile_name=model_instance_phy.phy.profile_name)
        profile = model_instance_profile.profile
        for input in model_instance_phy.phy.profile_inputs:
            #print(input.var_name + " = " + str(input.value))
            profile_input = getattr(profile.inputs, input.var_name)
            profile_input.var_value = input.value
            #print(profile_input.var_name + " = " + str(profile_input.var_value))

        for output in model_instance_phy.phy.profile_outputs:
            profile_output = getattr(profile.outputs, output.var_name)
            profile_output.override = output.override

        self.radio_configurator.calculate(model_instance_profile)
        profile = model_instance_profile.profile

        # Compare outputs of both instance models
        for phy_output in model_instance_phy.profile.outputs:
            #print(phy_output.var_name + " = " + str(phy_output.var_value))
            profile_output = getattr(profile.outputs, phy_output.var_name)
            #print(profile_output.var_name + " = " + str(profile_output.var_value))
            self.assertEqual(phy_output.var_value, profile_output.var_value, "PHY vs Profile Inputs only, output " + phy_output.var_name + " don't match for " + phy_name + ": " + str(phy_output.var_value) + " != " + str(profile_output.var_value))

        # # print the results to a .cfg file
        # Human_Readable.print_modem_model_values_v2(calc_output_dir + "/" + phy_name + "_profile.cfg", phy_name, model_instance_profile)
        #
        # # print to XML file
        # phy = None # getattr(model_instance.phys, phy_name)
        # profile = model_instance_profile.profile
        # static_timestamp = datetime.datetime(1984, 1, 2, 12, 34, 56)
        # part_rev = model_instance_profile.part_revision
        # result_code = model_instance_profile.result_code
        # error_message = model_instance_profile.error_message
        # model_instance_profile.to_instance_xml(calc_output_dir + "/" + phy_name + "_profile.xml", part_rev, phy_name + " instance", True, result_code, error_message, profile, phy, static_timestamp)

    def test_load_single_phy_vs_inputs_with_optional_overrides(self):
        type_model = self.radio_configurator.create_modem_model_type()

        phy_name = 'PHY_Datasheet_169M_2GFSK_38p4Kbps_20K'
        print("Testing PHY vs Profile inputs with overrides for: " + phy_name)

        optional_inputs = dict()
        optional_inputs['freq_offset_hz'] = 400
        optional_inputs['timing_detection_threshold'] = 12
        optional_inputs['timing_sample_threshold'] = 8
        optional_inputs['agc_settling_delay'] = 34

        model_instance_phy = self.radio_configurator.calc_config_phy(phy_name, output_dir=self.calc_output_dir, optional_inputs=optional_inputs)

        model_instance_profile = self.radio_configurator.create_modem_model_instance(profile_name=model_instance_phy.phy.profile_name)
        profile = model_instance_profile.profile
        for input in model_instance_phy.phy.profile_inputs:
            #print(input.var_name + " = " + str(input.value))
            profile_input = getattr(profile.inputs, input.var_name)
            profile_input.var_value = input.value
            #print(profile_input.var_name + " = " + str(profile_input.var_value))

        profile.inputs.freq_offset_hz.var_value = 400
        profile.inputs.timing_detection_threshold.var_value = 12
        profile.inputs.timing_sample_threshold.var_value = 8
        profile.inputs.agc_settling_delay.var_value = 34

        for output in model_instance_phy.phy.profile_outputs:
            profile_output = getattr(profile.outputs, output.var_name)
            profile_output.override = output.override

        self.radio_configurator.calculate(model_instance_profile)
        profile = model_instance_profile.profile

        # Compare outputs of both instance models
        for phy_output in model_instance_phy.profile.outputs:
            #print(phy_output.var_name + " = " + str(phy_output.var_value))
            profile_output = getattr(profile.outputs, phy_output.var_name)
            #print(profile_output.var_name + " = " + str(profile_output.var_value))
            self.assertEqual(phy_output.var_value, profile_output.var_value, "PHY vs Profile Inputs only, output " + phy_output.var_name + " don't match for " + phy_name + ": " + str(phy_output.var_value) + " != " + str(profile_output.var_value))

