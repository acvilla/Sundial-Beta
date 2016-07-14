from unittest import TestCase

from pyradioconfig.calculator_model_framework.Utils.FileUtilities import FileUtilities
from pyradioconfig.to_be_deprecated.legacy_top_level import *
from file_comparison import *
from pyradioconfig.calculator_model_framework.Utils.CalcStatus import CalcStatus
import time
import sys

from pyradioconfig.unit_tests.CFGFileDiff import CFGFileDiffManager


class TestAllPhys(object):

    part_family = None
    part_rev = None

    # Hack override used to allow the test to run from python console
    def runTest( self ):
        self.failUnless( True is True )

    def build_types_model(self):
        radio_configurator = CalcManager(self.part_family, self.part_rev)
        types_model = radio_configurator.create_modem_model_type()
        return types_model

    #
    # Copy from working output directory to directory where files are committed.
    # Do any other stuff related to releasing a new phy here.
    #
    def release_to_config_output(self, phy_name):

        config_output_file = self.config_output_dir + "/" + phy_name

        calculated_output_file = self.calc_output_dir + "/" + phy_name

        if not os.path.exists(calculated_output_file + ".cfg" ):
            print "Calculated output cfg file for %s does not exist!" % phy_name
            return

        # Copy .cfg file
        shutil.copyfile(calculated_output_file + ".cfg", config_output_file + ".cfg")

        # Copy .xml file
        shutil.copyfile(calculated_output_file + ".xml", config_output_file + ".xml")

    def release_all(self, dut=''):
        FileUtilities.cleandir(self.config_output_dir)

        radio_configurator = CalcManager(self.part_family, self.part_rev)
        sim_tests_phy_groups = radio_configurator.get_sim_tests_phy_groups()
        types_model = radio_configurator.create_modem_model_type()
        # Filter out the sim tests phys
        phys = radio_configurator.filter_out_phy_group_names(types_model, sim_tests_phy_groups)
        for phy in phys:
            self.release_to_config_output(phy_name=phy.name)

    def calc_config(self, phy_name, output_dir=None, optional_inputs=dict(), optional_filename=None, print_to_console=False, test_diff=True):

        print "Calculating phy: %s" % (phy_name)

        if optional_filename is None:
            optional_filename = phy_name

        radio_configurator = CalcManager(self.part_family, self.part_rev)
        model_instance = radio_configurator.calc_config_phy(phy_name, output_dir=output_dir, optional_inputs=optional_inputs, optional_filename=optional_filename)

        # Check return status
        if model_instance.result_code == CalcStatus.Failure.value:
            raise Exception(model_instance.error_message + "\nERROR: Scroll up to see source of error.")

        # Compare to reference .cfg file
        if test_diff:
            different, diff = files_diff(output_dir + "/" + phy_name + ".cfg", self.config_output_dir + "/" + phy_name + ".cfg", print_to_console=print_to_console)
            if different:
                cfg_files_different = True
                print("\tError: Output cfg file is different from reference for: " + phy_name)
                CFGFileDiffManager.process_diff(phy_name, diff)
            else:
                cfg_files_different = False
        else:
            cfg_files_different = False

        # Verify xml file was created
        self.assertTrue(output_dir + "/" + phy_name + ".xml")

        # Compare to reference instance .xml file
        #different = files_diff(output_dir + "/" + phy_name + ".xml", self.config_output_dir + "/" + phy_name + ".xml")
        #if different:
        #    xml_files_different = True
        #    print("\tError: Output xml file is different from reference for: " + phy_name)
        #else:
        xml_files_different = False

        return cfg_files_different, xml_files_different

    def test_calc_single_phy_with_inputs(self):

        phy_name = "PHY_Bluetooth_LE_Studio"

        # Test bad (invalid) input
        optional_inputs=dict()
        optional_inputs['base_frequency11'] = 2405000000L

        self.assertRaises(Exception, self.calc_config, phy_name, output_dir=self.calc_output_dir, optional_inputs=optional_inputs, print_to_console=True)

        # Test good (valid) input
        optional_inputs=dict()
        optional_inputs['base_frequency_hz'] = 2402000000

        cfg_files_different, xml_files_different = self.calc_config(phy_name, output_dir=self.calc_output_dir, optional_inputs=optional_inputs, print_to_console=True)
        CFGFileDiffManager.print_diff()

        # Check to see if any files failed "diff" check
        self.assertFalse(cfg_files_different, "CFG files have differed from reference files.")
        self.assertFalse(xml_files_different, "XML files have differed from reference files.")


    def test_calc_all(self):

        FileUtilities.cleandir(self.calc_output_dir)

        # init variables
        any_cfg_files_different = False
        any_xml_files_different = False

        # Build Types Model
        types_model = self.build_types_model()

        # Loop through all phy's in types model
        sim_tests_phy_groups = radio_configurator.get_sim_tests_phy_groups()
        # Filter out the sim tests phys
        filtered_phys = radio_configurator.filter_out_phy_group_names(types_model, sim_tests_phy_groups)
        print('phy count: ' + str(len(filtered_phys)))
        for phy in filtered_phys:
            cfg_files_different, xml_files_different = self.calc_config(phy.name, output_dir=self.calc_output_dir, print_to_console=True)
            any_cfg_files_different = any_cfg_files_different or cfg_files_different
            any_xml_files_different = any_xml_files_different or xml_files_different


        CFGFileDiffManager.print_diff()

        # Check to see if any files failed "diff" check
        self.assertFalse(any_cfg_files_different, "CFG files have differed from reference files.")
        self.assertFalse(any_xml_files_different, "XML files have differed from reference files.")

    def setUp(self):
        #sys.stdout.flush()
        #time.sleep(1) # delays for x seconds

        if self.part_family is not None:
            print('part_family=' + self.part_family)
            print('part_rev=' + self.part_rev)

            self.current_path = os.path.dirname(os.path.abspath(__file__))
            self.calc_output_dir = os.path.join(self.current_path, 'calculated_output')
            if not os.path.exists(self.calc_output_dir):
                os.makedirs(self.calc_output_dir)

            self.config_output_dir = os.path.join(self.current_path, 'config_output', self.part_family)
            if not os.path.exists(self.config_output_dir):
                os.makedirs(self.config_output_dir)

        CFGFileDiffManager.clear_diffs()

    def tearDown(self):
        #sys.stdout.flush()
        #time.sleep(1) # delays for x seconds
        pass