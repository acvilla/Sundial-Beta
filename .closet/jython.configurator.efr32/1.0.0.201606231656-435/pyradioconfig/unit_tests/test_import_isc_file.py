from unittest import TestCase
from pyradioconfig import CalcManager
from pyradioconfig.calculator_model_framework.model_serializers.human_readable import Human_Readable
from pyradioconfig.calculator_model_framework.model_serializers.import_isc_files import ImportISCFiles
import os

class TestVImportISCFile(TestCase):

    # Hack override used to allow the test to run from python console
    def runTest( self ):
      self.failUnless( True is True )

    def test_import_isc_file(self):
        # Create radio configurator
        radio_configurator = CalcManager("dumbo", "A0")

        # Create file paths needed
        current_path = os.path.dirname(os.path.abspath(__file__))
        test_isc_file_path = os.path.join(current_path, 'unittest_files\\railtest_efr32_RAIL13.isc')
        output_instance_file_path = os.path.join(current_path, 'calculated_output\\converted_iscfile.xml')
        output_cfg_file_path = os.path.join(current_path, 'calculated_output\\converted_iscfile.cfg')

        # Create ISC Parser
        isc = ImportISCFiles()
        inputs = isc.parse_file(test_isc_file_path)

        # Create model and fill with ISC file values
        model_instance = radio_configurator.calc_config_profile(isc.profile, output_instance_file_path, inputs)
        self.assertTrue(os.path.exists(output_instance_file_path))

        # Load DUT with output instance XML
        #if model_instance.result_code == CalcStatus.Success.value:
        #   dut.utils.calc.downloadInstance(output_instance_file_path)

        # Create human readable cfg file (just for fun)
        Human_Readable.print_modem_model_values_v2(output_cfg_file_path, None, model_instance)
        self.assertTrue(os.path.exists(output_cfg_file_path))







