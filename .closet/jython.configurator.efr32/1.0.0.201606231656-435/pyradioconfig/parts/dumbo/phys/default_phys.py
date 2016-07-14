"""
This class is where the default phys's are defined
"""
from pyradioconfig.calculator_model_framework.interfaces.idefault_phy import IDefaultPhy
from pyradioconfig.pycalcmodel import ModelDefaultPhy


class DefaultPhys(IDefaultPhy):
    def build(self, model):
        """
        Assigns default PHYs
        """

        # This is just an example default phy for a profile
        # TODO: Add default phys
        model.profiles.Base.default_phys.append(ModelDefaultPhy(model.phys.PHY_Datasheet_868M_2GFSK_500Kbps_125K))
        model.profiles.Bluetooth_LE.default_phys.append(ModelDefaultPhy(model.phys.PHY_Bluetooth_LE_Studio))
        model.profiles.IEEE802154.default_phys.append(ModelDefaultPhy(model.phys.PHY_IEEE802154_2p4GHz_Studio))
