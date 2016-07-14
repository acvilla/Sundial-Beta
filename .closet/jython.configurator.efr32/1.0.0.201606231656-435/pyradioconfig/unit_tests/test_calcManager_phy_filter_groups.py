import inspect
import os
from unittest import TestCase
from pyradioconfig import CalcManager


class TestCalcManagerPhys(TestCase):

    current_path = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_path, 'calculated_output')
    part_family = "unit_test_part"
    #part_family = "dumbo"
    part_revision = "A0"

    # Hack override used to allow the test to run from python console
    def runTest( self ):
        self.failUnless( True is True )

    def get_CalcManager(self):
        return CalcManager(self.part_family, self.part_revision)

    def test_get_customer_phy_groups(self):
        radio_configurator = self.get_CalcManager()
        customer_phy_groups = radio_configurator.get_customer_phy_groups()
        print customer_phy_groups
        self.assertTrue(len(customer_phy_groups) == 1, 'Only 1 cusotmer group phy defined')

    def test_get_sim_test_phy_groups(self):
        radio_configurator = self.get_CalcManager()
        sim_test_phy_groups= radio_configurator.get_sim_tests_phy_groups()
        print sim_test_phy_groups
        self.assertTrue(len(sim_test_phy_groups) == 1, 'Only 1 sim test group phy defined')

    def test_filter_phy_group_names(self):
        radio_configurator = self.get_CalcManager()
        model = radio_configurator.create_modem_model_type()
        customer_phy_groups = radio_configurator.get_customer_phy_groups()

        filtered_phys = radio_configurator.filter_out_phy_group_names(model, customer_phy_groups)
        for phy in filtered_phys:
            print(phy.name)
        self.assertTrue(len(filtered_phys) == 4, 'Only 1 sim test group phy defined')

    def test_filter_phy_group_names_to_xml(self):
        radio_configurator = self.get_CalcManager()
        model = radio_configurator.create_modem_model_type()
        customer_phy_groups = radio_configurator.get_customer_phy_groups()

        filtered_phy_groups = radio_configurator.filter_out_phy_group_names_to_phy_group_name_list(model, customer_phy_groups)
        file_name = self.output_dir + "/" + self.part_family + "_" + self.part_revision + "_filtered_type.xml"
        try:
            os.remove(file_name)
        except:
            pass
        model.to_type_xml(file_name, filtered_phy_groups)
        self.assertTrue(os.path.exists(file_name))

    def test_filter_phy_group_names_to_xml2(self):
        radio_configurator = self.get_CalcManager()
        model = radio_configurator.create_modem_model_type()
        customer_phy_groups = radio_configurator.get_customer_phy_groups()
        sim_test_phy_groups = radio_configurator.get_sim_tests_phy_groups()

        filtered_phy_groups = radio_configurator.filter_out_phy_group_names_to_phy_group_name_list(model, customer_phy_groups + sim_test_phy_groups)
        file_name = self.output_dir + "/" + self.part_family + "_" + self.part_revision + "_filtered_type2.xml"
        try:
            os.remove(file_name)
        except:
            pass
        model.to_type_xml(file_name, filtered_phy_groups)
        self.assertTrue(os.path.exists(file_name))

    def test_filter_phy_group_names_to_xml3(self):
        radio_configurator = self.get_CalcManager()
        model = radio_configurator.create_modem_model_type()
        studio_phy_groups = radio_configurator.get_simplicity_studio_phy_groups()

        filtered_phy_groups = radio_configurator.find_all_phy_group_names_in_phy_group_name_list(model, studio_phy_groups)
        file_name = self.output_dir + "/" + self.part_family + "_" + self.part_revision + "_filtered_type3.xml"
        try:
            os.remove(file_name)
        except:
            pass
        model.to_type_xml(file_name, filtered_phy_groups)
        self.assertTrue(os.path.exists(file_name))

    def test_find_customer(self):
        radio_configurator = self.get_CalcManager()
        model = radio_configurator.create_modem_model_type()
        customer_phy_groups = radio_configurator.get_customer_phy_groups()

        filtered_phys = radio_configurator.find_all_phys_of_group_name(model, customer_phy_groups)
        for phy in filtered_phys:
            print(phy.name)
            print(inspect.getfile(phy.__class__))
        self.assertTrue(len(filtered_phys) == 2, 'Only 2 sim customer phys defined')

    def test_studio_filter(self):
        radio_configurator = self.get_CalcManager()
        model = radio_configurator.create_modem_model_type()
        studio_phy_groups = radio_configurator.get_simplicity_studio_phy_groups()

        filtered_phys = radio_configurator.find_all_phys_of_group_name(model, studio_phy_groups)
        for phy in filtered_phys:
            print(phy.name)
            print(inspect.getfile(phy.__class__))
        #self.assertTrue(len(filtered_phys) == 2, 'Only 2 studio customer phys defined')
