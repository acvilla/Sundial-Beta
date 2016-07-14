import os
import sys
from unittest import TestCase
from decorator import contextmanager
from pyradioconfig.calculator_model_framework.CalcManager import CalcManager
from pyradioconfig.calculator_model_framework.Utils.FileUtilities import FileUtilities
from pyradioconfig.main import main


class TestExecutableMain(TestCase):

    # Hack override used to allow the test to run from python console
    def runTest( self ):
        self.failUnless( True is True )

    @contextmanager
    def captured_output(self):
        from StringIO import StringIO
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err


    def test_main_help(self):
        print "test_main_help"
        sys.argv.append('--help')

        # Test to make sure exit code is success
        with self.assertRaises(SystemExit) as cmd:
            with self.captured_output() as (out, err):
                main().main()

        sys.argv.remove('--help')

        output = out.getvalue().strip()
        print output
        test_string = 'usage: '
        self.assertTrue(test_string in output)

        self.assertEqual(cmd.exception.code, 0)


    def test_main_version(self):
        print "test_main_version"
        sys.argv.append('--version')

        # Test to make sure exit code is success
        with self.assertRaises(SystemExit) as cmd:
            with self.captured_output() as (out, err):
                main().main()

        sys.argv.remove('--version')

        output = out.getvalue().strip()
        print output
        test_string = 'Version = ' + CalcManager().version
        self.assertTrue(test_string in output)

        self.assertEqual(cmd.exception.code, 0)



    def test_main_calculate(self):
        print "test_main_calculate"
        sys.argv.append('--calc')
        current_path = os.path.dirname(os.path.abspath(__file__))
        input_path = os.path.join(current_path, "calculated_output\\PHY_WMbus_T_100k.xml")
        output_path =os.path.join(current_path, "calculated_output\\test_output.xml")
        sys.argv.append('--input_file=' + input_path)
        sys.argv.append('--output_file='  + output_path)

        try:
            os.remove(output_path)
        except:
            pass

        # Test to make sure exit code is success
        with self.assertRaises(SystemExit) as cmd:
            with self.captured_output() as (out, err):
                main().main()

        sys.argv.remove('--calc')
        sys.argv.remove('--input_file=' + input_path)
        sys.argv.remove('--output_file='  + output_path)

        output = out.getvalue().strip()
        print output
        test_string = 'Successfully calculated instance file'
        self.assertTrue(test_string in output)

        self.assertTrue(os.path.exists(output_path))

        self.assertEqual(cmd.exception.code, 0)


    def test_main_types(self):
        print "test_main_types"
        sys.argv.append('--types')
        sys.argv.append('--part_family=' + 'dumbo')
        sys.argv.append('--part_revision=' + 'A0')
        current_path = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(current_path, "calculated_output\\dumbo_A0_filtered_type.xml")
        sys.argv.append('--output_file=' + output_path)

        try:
            os.remove(output_path)
        except:
            pass

        # Test to make sure exit code is success
        with self.assertRaises(SystemExit) as cmd:
            with self.captured_output() as (out, err):
                main().main()

        sys.argv.remove('--types')
        sys.argv.remove('--part_family=' + 'dumbo')
        sys.argv.remove('--part_revision=' + 'A0')
        sys.argv.remove('--output_file=' + output_path)

        output = out.getvalue().strip()
        print output
        test_string = 'Making types file'
        self.assertTrue(test_string in output)

        self.assertTrue(os.path.exists(output_path))

        self.assertEqual(cmd.exception.code, 0)

    def test_main_types_unfiltered(self):
        print "test_main_types"
        sys.argv.append('--types')
        sys.argv.append('--disable_filter')
        sys.argv.append('--part_family=' + 'dumbo')
        sys.argv.append('--part_revision=' + 'A0')
        current_path = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(current_path, "calculated_output\\dumbo_A0_type.xml")
        sys.argv.append('--output_file=' + output_path)

        try:
            os.remove(output_path)
        except:
            pass

        # Test to make sure exit code is success
        with self.assertRaises(SystemExit) as cmd:
            with self.captured_output() as (out, err):
                main().main()

        sys.argv.remove('--types')
        sys.argv.remove('--disable_filter')
        sys.argv.remove('--part_family=' + 'dumbo')
        sys.argv.remove('--part_revision=' + 'A0')
        sys.argv.remove('--output_file=' + output_path)

        output = out.getvalue().strip()
        print output
        test_string = 'Making types file'
        self.assertTrue(test_string in output)

        self.assertTrue(os.path.exists(output_path))

        self.assertEqual(cmd.exception.code, 0)


    def test_main_calculate_phy(self):
        print "test_main_calculate"
        sys.argv.append('--calc')
        current_path = os.path.dirname(os.path.abspath(__file__))
        output_path =os.path.join(current_path, "calculated_output\\test_phy_output.xml")
        sys.argv.append('--output_file='  + output_path)
        sys.argv.append('--part_family=' + 'dumbo')
        sys.argv.append('--part_revision=' + 'ANY')
        sys.argv.append('--phy_name='  + "PHY_ATnT_911_779")

        try:
            os.remove(output_path)
        except:
            pass

        # Test to make sure exit code is success
        with self.assertRaises(SystemExit) as cmd:
            with self.captured_output() as (out, err):
                main().main()

        sys.argv.remove('--calc')
        sys.argv.remove('--output_file='  + output_path)
        sys.argv.remove('--phy_name='  + "PHY_ATnT_911_779")
        sys.argv.remove('--part_family=' + 'dumbo')
        sys.argv.remove('--part_revision=' + 'ANY')

        output = out.getvalue().strip()
        print output
        test_string = 'Successfully calculated instance file'
        self.assertTrue(test_string in output)

        self.assertTrue(os.path.exists(output_path))

        self.assertEqual(cmd.exception.code, 0)


    def test_main_calculate_phy_optional_inputs(self):
        print "test_main_calculate"
        sys.argv.append('--calc')
        current_path = os.path.dirname(os.path.abspath(__file__))
        output_path =os.path.join(current_path, "calculated_output\\test_phy_optional_inputs_output.xml")
        sys.argv.append('--output_file='  + output_path)
        sys.argv.append('--part_family=' + 'dumbo')
        sys.argv.append('--part_revision=' + 'ANY')
        sys.argv.append('--phy_name='  + "PHY_ATnT_911_779")
        sys.argv.append('--optional_inputs='  + "{'xtal_frequency_hz': 38400001}")

        try:
            os.remove(output_path)
        except:
            pass

        # Test to make sure exit code is success
        with self.assertRaises(SystemExit) as cmd:
            with self.captured_output() as (out, err):
                main().main()

        sys.argv.remove('--calc')
        sys.argv.remove('--output_file='  + output_path)
        sys.argv.remove('--phy_name='  + "PHY_ATnT_911_779")
        sys.argv.remove('--optional_inputs='  + "{'xtal_frequency_hz': 38400001}")
        sys.argv.remove('--part_family=' + 'dumbo')
        sys.argv.remove('--part_revision=' + 'ANY')

        output = out.getvalue().strip()
        print output
        test_string = 'Successfully calculated instance file'
        self.assertTrue(test_string in output)

        self.assertTrue(os.path.exists(output_path))

        self.assertEqual(cmd.exception.code, 0)

    def test_isc_file(self):
        print "test_main_calculate"
        sys.argv.append('--calc')
        current_path = os.path.dirname(os.path.abspath(__file__))
        sys.argv.append('--part_family=' + 'dumbo')
        sys.argv.append('--part_revision=' + 'ANY')
        isc_path = current_path + "/unittest_files/railtest_efr32_RAIL13.isc"
        sys.argv.append('--isc_file='  + isc_path)
        output_path = isc_path + ".xml"

        try:
            os.remove(output_path)
        except:
            pass

        # Test to make sure exit code is success
        with self.assertRaises(SystemExit) as cmd:
            with self.captured_output() as (out, err):
                main().main()

        sys.argv.remove('--calc')
        sys.argv.remove('--isc_file='  + isc_path)
        sys.argv.remove('--part_family=' + 'dumbo')
        sys.argv.remove('--part_revision=' + 'ANY')

        output = out.getvalue().strip()
        print output
        test_string = 'Successfully calculated instance file'
        self.assertTrue(test_string in output)

        self.assertTrue(os.path.exists(output_path))
        try:
            os.remove(output_path)
        except:
            pass

        self.assertEqual(cmd.exception.code, 0)
