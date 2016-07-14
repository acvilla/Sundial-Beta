from unittest import TestCase
from pyradioconfig import CalcManager, CFGFileDiffManager
from pyradioconfig.unit_tests.test_all_phys import TestAllPhys
import os

class TestAllPhys_Dumbo(TestAllPhys, TestCase):

    def __init__(self, *args, **kwargs):
        # static variables
        self.part_family = "dumbo"
        self.part_rev = "A0"
        super(TestAllPhys_Dumbo, self).__init__(*args, **kwargs)

    def test_calc_single_phy(self):

        phy_name = "PHY_ATnT_911_779"
        cfg_files_different, xml_files_different = self.calc_config(phy_name, output_dir=self.calc_output_dir, print_to_console=True, test_diff=True)
        CFGFileDiffManager.print_diff()

        # Check to see if any files failed "diff" check
        self.assertFalse(cfg_files_different, "CFG files have differed from reference files.")
        self.assertFalse(xml_files_different, "XML files have differed from reference files.")

#
# Run the calculator and generate the calculated outputs
#
def calc_config(phy_name, output_dir=None, optional_inputs=dict(), optional_filename=None, part_family = "dumbo", part_rev = "ANY"):

    if output_dir is None:
        current_path = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(current_path, 'calculated_output')

    radio_configurator = CalcManager(part_family, part_rev)
    model_instance = radio_configurator.calc_config_phy(phy_name, output_dir=output_dir, optional_inputs=optional_inputs, optional_filename=optional_filename)
    return model_instance

#
# Used externally
#
def calc_and_release(dut='', phy_name=''):
    print "calculate and release %s" % phy_name
    calc_config(phy_name)
    test = TestAllPhys_Dumbo()
    test.setUp()
    test.release_to_config_output(phy_name)
    print "Finished calc_and_release(" + phy_name + ")!"


#
# Run the calculator and generate the calculated outputs for all phys
#
def calc_all():
    try:
        test = TestAllPhys_Dumbo()
        test.setUp()
        test.test_calc_all()
        print "Finished calc_all()"
    except AssertionError, e:
        print "\nWARNING: Possible difference from reference files, please review above.\n"

#
# Used externally
#
def release_all(dut=''):
    calc_all()
    test = TestAllPhys_Dumbo()
    test.setUp()
    test.release_all()
    print "Finished release_all()!"

#
# Run the calculator and generate the calculated outputs
#
def calc_config_dumbo(phy_name, output_dir=None, optional_inputs=dict(), optional_filename=None, print_to_console=False, test_diff=True):

    if output_dir is None:
        current_path = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(current_path, 'calculated_output')

    try:
        test = TestAllPhys_Dumbo()
        test.setUp()
        cfg_files_different, xml_files_different = test.calc_config(phy_name, output_dir=output_dir,
                                                                    optional_inputs=optional_inputs,
                                                                    optional_filename=optional_filename,
                                                                    print_to_console=print_to_console,
                                                                    test_diff=test_diff)
        if cfg_files_different:
            print("WARNING: CFG file has differed from reference file.")
        if xml_files_different:
            print("WARNING: XML file has differed from reference file.")
        print "Finished calc_config_dumbo()"
    except AssertionError, e:
        print "\nWARNING: Possible difference from reference files, please review above.\n"

#
# Used externally
#
def calc_and_release_dumbo(dut='', phy_name=''):
    print "calculate and release %s" % phy_name
    calc_config_dumbo(phy_name)
    test = TestAllPhys_Dumbo()
    test.setUp()
    test.release_to_config_output(phy_name)
    print "Finished calc_and_release_dumbo(" + phy_name + ")!"


#
# Run the calculator and generate the calculated outputs for all phys
#
def calc_all_dumbo():
    try:
        test = TestAllPhys_Dumbo()
        test.setUp()
        test.test_calc_all()
        print "Finished calc_all_dumbo()"
    except AssertionError, e:
        print "\nWARNING: Possible difference from reference files, please review above.\n"

#
# Used externally
#
def release_all_dumbo(dut=''):
    calc_all_dumbo()
    test = TestAllPhys_Dumbo()
    test.setUp()
    test.release_all()
    print "Finished release_all_dumbo()!"

