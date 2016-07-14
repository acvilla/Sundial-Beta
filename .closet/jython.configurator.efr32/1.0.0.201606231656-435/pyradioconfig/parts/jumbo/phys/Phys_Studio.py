from pyradioconfig.calculator_model_framework.interfaces.iphy import IPhy


class PHYS_Studio(IPhy):

    def PHY_Bluetooth_LE_Studio(self, model):
        phy = self._makePhy(model, model.profiles.Bluetooth_LE, 'Bluetooth LE')
        phy.profile_inputs.base_frequency_hz.value = 2402000000L

    def PHY_IEEE802154_2p4GHz_Studio(self, model):
        phy = self._makePhy(model, model.profiles.IEEE802154, 'IEEE 802154 2p4GHz')
        phy.profile_inputs.base_frequency_hz.value = 2405000000L
