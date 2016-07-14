"""
Main entry for executable from console only/n

Executable Args for Version:
        --version : "Returns version", action="store_true"


Executable Args to calcultae an input instance XML:
        --calculate : "Runs calculator, Need to define input and output files"

        --part_family : "Part Family"

        --part_revision : "Part Revision"

       --input_file : "Full path of the input instance XML")

        --output_file : "Full path of the output instance XML")


Executable Args for generating Type File:
        --part_family : "Part Family"

        --part_revision : "Part Revision"

        --output_file : "Full path of the output instance XML")

        --types : "Generates model type XML file", action="store_true")


Executable Args for Phy Name and Optional Inputs:
        --calculate : "Runs calculator, Need to define PHY name"

        --part_family : "Part Family"

        --part_revision : "Part Revision"

        --phy_name : "Phy Name"

        --optional_inputs : "Optional inputs as a Python dictionary string."
            Example:

            >>> --optional_inputs={'base_frequency_hz': 431000000}

        --output_file : "Optional full path of the output instance XML")

Executable Args for ISC file:
        --calculate : "Runs calculator, Need to define PHY name"

        --part_family : "Part Family"

        --part_revision : "Part Revision"

        --isc_file : "Runs calculator, for ISC file path."

        --output_file : "Optional full path of the output instance XML")
"""

import argparse
import os
import sys
import errno
import traceback
from pyradioconfig.calculator_model_framework.CalcManager import CalcManager
from pyradioconfig.calculator_model_framework.Utils.CalcStatus import CalcStatus
from pyradioconfig.calculator_model_framework.model_serializers.import_isc_files import ImportISCFiles
from pyradioconfig.pycalcmodel import ModelRootInstanceXml

class main:

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--version", "--ver", "--v", help="Returns version", action="store_true")
        parser.add_argument("--calculate", "--calc", "--c", help="Runs calculator, Need to define input and output files", action="store_true")
        parser.add_argument("--input_file", "--input", "--i", help="Full path of the input instance XML")
        parser.add_argument("--output_file", "--output", "--o", help="Full path of the output instance XML")
        parser.add_argument("--types", "--t", help="Generates model type XML file", action="store_true")
        # Hidden argument disables customer filter
        parser.add_argument("--disable_filter", "--df", action="store_true", help=argparse.SUPPRESS)
        parser.add_argument("--part_family", "--family", "--f", help="Part Family")
        parser.add_argument("--part_revision", "--rev", "--r", help="Part Revision")
        parser.add_argument("--phy_name", "--phy", "--p", help="Phy Name")
        parser.add_argument("--optional_inputs", "--opt", help="Optional inputs as a Python dictionary string.")
        parser.add_argument("--isc_file", "--isc", help="ISC file path.")
        #args = parser.parse_args()
        args, unknown = parser.parse_known_args()

        #path = os.path.join(os.environ.get("_MEIPASS2",os.path.abspath(".")), __file__)
        #print "printRootStructure, path=" + path
        #FileUtilities.printRootStructure(os.path.dirname(__file__))

        part_family = None
        part_rev = None
        result_code = 0

        if args.version:
            print "Version = " + CalcManager().version
            self.exit(result_code)

        if args.part_family:
            part_family = args.part_family
            print "Setting part family to: " + args.part_family

        if args.part_revision:
            part_rev = args.part_revision
            print "Setting part revision to: " + args.part_revision

        if args.calculate:

            if args.phy_name:
                #
                # User wants to calculate a specific PHY\
                #
                phy_name = args.phy_name

                if not args.optional_inputs:
                    optional_inputs = {}
                else:
                    optional_inputs = eval(args.optional_inputs)

                # Optional output file
                if args.output_file:
                    output_file = args.output_file
                else:
                    current_path = os.path.dirname(os.path.abspath(__file__))
                    output_file = current_path + "/" + phy_name + ".xml"

                if ((part_family is not None) and (part_rev is not None)):
                    try:
                        part_family = part_family.lower()
                        part_rev = part_rev.upper()

                        # Build Modem Model Type
                        radio_configurator = CalcManager(part_family, part_rev)
                        model_instance = radio_configurator.calculate_phy(phy_name, optional_inputs)
                        radio_configurator.processed_model_to_xml(model_instance, output_file)
                    except Exception, e:
                        traceback.print_exc(file=sys.stdout)
                        print "Error: " + str(e.message)
                        self.exit(errno.EFAULT)

                    if (model_instance.result_code is not None):
                        if (model_instance.result_code != CalcStatus.Success.value):
                            print "Error: " + model_instance.error_message
                        else:
                            print "Successfully calculated instance file."
                            print "Output path: " + output_file
                    else:
                        print "Error: Unknown return code received?"

                    self.exit(result_code)
                else:
                    if part_family is None:
                        print "Missing part family"
                    if part_rev is None:
                        print "Missing part revision"
                    self.exit(errno.EFAULT)

            elif args.isc_file:
                #
                # User wants to run an ISC file through the calculator
                #
                isc_file = args.isc_file

                # Optional output file
                if args.output_file:
                    output_file = args.output_file
                else:
                    output_file = isc_file
                    output_file = output_file + ".xml"

                if ((part_family is not None) and (part_rev is not None)):
                    try:
                        part_family = part_family.lower()
                        part_rev = part_rev.upper()

                        # Build Modem Model Type
                        isc = ImportISCFiles()
                        inputs = isc.parse_file(isc_file)

                        # Create model and fill with ISC file values
                        radio_configurator = CalcManager(part_family, part_rev)
                        model_instance = radio_configurator.calc_config_profile(isc.profile, output_file, inputs)

                        # Run model through the Calculator
                        result_code, error_message = radio_configurator.calculate(model_instance)

                        radio_configurator.processed_model_to_xml(model_instance, output_file)
                    except Exception, e:
                        traceback.print_exc(file=sys.stdout)
                        print "Error: " + str(e.message)
                        self.exit(errno.EFAULT)

                    if (model_instance.result_code is not None):
                        if (model_instance.result_code != CalcStatus.Success.value):
                            print "Error: " + model_instance.error_message
                        else:
                            print "Successfully calculated instance file."
                            print "Output path: " + output_file
                    else:
                        print "Error: Unknown return code received?"

                    self.exit(result_code)
                else:
                    if part_family is None:
                        print "Missing part family"
                    if part_rev is None:
                        print "Missing part revision"
                    self.exit(errno.EFAULT)
            else:
                #
                # User wants to calculate an XML file
                #

                # Needs input file
                if not args.input_file:
                    print "No input file specified!"
                    self.exit(errno.EFAULT)
                elif not (os.path.isfile(args.input_file)):
                    print "Error: Input file does not exist: " + args.input_file
                    self.exit(errno.EFAULT)
                else:
                    input_path = args.input_file

                # Needs output file
                if not args.output_file:
                    print "No output file specified!"
                    self.exit(errno.EFAULT)
                else:
                    output_file = args.output_file

                try:
                    # Create manager without part family and revision
                    calMgr = CalcManager()

                    # Get part family and revision from instance file
                    modem_instance_model = ModelRootInstanceXml(input_path)
                    part_family = modem_instance_model.part_family
                    part_revision = modem_instance_model.part_revision
                    print "part_family = " + part_family
                    print "part_revision = " + part_revision

                    # Load back into CalcManager
                    calMgr.part_family = part_family
                    calMgr.part_revision = part_revision
                    result_code, error_message = calMgr.calculateXMLInstance(modem_instance_model, output_file)
                except Exception, e:
                    traceback.print_exc(file=sys.stdout)
                    print "Error: " + str(e.message)
                    self.exit(errno.EFAULT)

                if (result_code is not None):
                    if (result_code != CalcStatus.Success.value):
                        print "Error: " + error_message
                    else:
                        print "Successfully calculated instance file."
                        print "Output path: " + output_file
                else:
                    print "Error: Unknown return code received?"

                self.exit(result_code)

        if args.types:
            if ((part_family is not None) and (part_rev is not None)):
                part_family = part_family.lower()
                part_rev = part_rev.upper()

                # Build Modem Model Type
                radio_configurator = CalcManager(part_family, part_rev)
                model = radio_configurator.create_modem_model_type()

                if args.disable_filter:
                    filtered_phy_groups = list()
                else:
                    # Default to filter out customer phys
                    customer_phy_groups = radio_configurator.get_customer_phy_groups()
                    sim_test_phy_groups = radio_configurator.get_sim_tests_phy_groups()
                    filtered_phy_groups = radio_configurator.filter_out_phy_group_names_to_phy_group_name_list(model, customer_phy_groups + sim_test_phy_groups)

                if args.output_file:
                    file_name = args.output_file
                else:
                    if args.disable_filter:
                        file_name = part_family + "_" + part_rev + "_type." + str(radio_configurator.version) + ".xml"
                    else:
                        file_name = part_family + "_" + part_rev + "_filtered_type." + str(radio_configurator.version) + ".xml"
                print "Making types file: " + file_name
                model.to_type_xml(file_name, filtered_phy_groups)
                self.exit(result_code)
            else:
                if part_family is None:
                    print "Missing part family"
                if part_rev is None:
                    print "Missing part revision"
                self.exit(errno.EFAULT)

        # Should not get here, print help just incase
        parser.print_help()
        self.exit(result_code)

    def exit(self, exit_code):
        print("exit_code:" + str(exit_code))
        sys.exit(exit_code)

if __name__ == "__main__":
    main().main()