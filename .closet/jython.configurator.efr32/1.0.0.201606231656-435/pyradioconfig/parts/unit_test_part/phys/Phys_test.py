from pyradioconfig.calculator_model_framework.interfaces.iphy import IPhy


class PHYS_test(IPhy):
    """
    Init internal variables
    """
    def __init__(self):
        self._phy_name = "Test Phys"
        self._major = 1
        self._minor = 0
        self._patch = 0


    def PHY_Test_868M_38p4kbps(self, model):

        phy = self._makePhy(model, model.profiles.Base, 'PHY Test 868M 38p4kbps')

        phy.profile_inputs.shaping_filter.values = model.vars.shaping_filter.var_enum.None

        phy.profile_inputs.base_frequency_hz.values = 868300000L


    def PHY_Test_868M_38p4kbps_long_preamble(self, modem_model):

        phy = self._makePhy(modem_model, modem_model.profiles.Base, 'PHY Test 868M 38p4kbps long preamble')

        phy.profile_inputs.shaping_filter.values = 1

        phy.profile_inputs.base_frequency_hz.values = 868000003L

        phy.profile_inputs.preamble_pattern_left.values = 16384


