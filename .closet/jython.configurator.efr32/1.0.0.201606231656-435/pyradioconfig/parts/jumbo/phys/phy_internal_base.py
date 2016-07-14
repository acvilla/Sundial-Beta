from pyradioconfig.parts.dumbo.phys.phy_common import PHY_COMMON_FRAME_INTERNAL

class Phy_Internal_Base(object):
    """
    Common Internal Phy functiosn live here
    """

    @staticmethod
    def GFSK_915M_base(phy, model):
        """GFSK_915M_base

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        phy.profile_inputs.base_frequency_hz.value = 915000000L
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.deviation.value = 50000
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsss_chipping_code.value = 0L
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2
        phy.profile_inputs.preamble_pattern_left.value = 4
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 40
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5
        phy.profile_inputs.syncword_0_left.value = 0xf68dL
        phy.profile_inputs.syncword_1_left.value = 0x0L
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.xtal_frequency_hz.value = 38400000

        PHY_COMMON_FRAME_INTERNAL(phy, model)

        phy.profile_inputs.symbols_in_timing_window.value = 14
        phy.profile_inputs.agc_period.value = 0
        phy.profile_inputs.agc_speed.value = model.vars.agc_speed.var_enum.FAST

    @staticmethod
    def GFSK_2400M_base(phy, model):
        """GFSK_2400M_base

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        phy.profile_inputs.base_frequency_hz.value = 2450000000L
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.deviation.value = 50000
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsss_chipping_code.value = 0L
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2
        phy.profile_inputs.preamble_pattern_left.value = 4
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 40
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5
        phy.profile_inputs.syncword_0_left.value = 0xf68dL
        phy.profile_inputs.syncword_1_left.value = 0x0L
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.xtal_frequency_hz.value = 38400000

        PHY_COMMON_FRAME_INTERNAL(phy, model)

        phy.profile_inputs.agc_power_target.value = -8
        phy.profile_inputs.symbols_in_timing_window.value = 14
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.agc_period.value = 0
        phy.profile_inputs.agc_speed.value = model.vars.agc_speed.var_enum.FAST