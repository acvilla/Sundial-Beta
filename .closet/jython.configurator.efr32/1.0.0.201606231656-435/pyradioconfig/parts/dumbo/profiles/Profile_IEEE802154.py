from pyradioconfig import ModelForce
from pyradioconfig.parts.dumbo.profiles.Profile_Base import Profile_Base


class Profile_IEEE802154(Profile_Base):

    def __init__(self):
        self._profileName = "IEEE802154"
        self._readable_name = "IEEE 802154 Profile"
        self._category = ""
        self._description = "IEEE 802154 Profile"
        self._default = False
        self._activation_logic = ""

    """
    Builds inputs, forced, outputs into modem model
    """
    def buildProfileModel(self, model):

        # Build profile
        profile = super(self.__class__, self).buildProfileModel(model)

        for input in profile.inputs:
            # Ignore base frequency
            if input._var.name != 'base_frequency_hz':
                self._moveVariableFromInputsIntoForces(profile, input._var, input.default)
    
        profile.inputs.base_frequency_hz.default=2405000000L
        profile.inputs.base_frequency_hz.value_limit_min=2400000000L

        # Inputs
        profile.forces.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        profile.forces.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        profile.forces.preamble_pattern.value = 0
        profile.forces.preamble_pattern_len.value = 4
        profile.forces.rx_xtal_error_ppm.value = 0
        profile.forces.syncword_0.value = 0xe5L
        profile.forces.syncword_1.value = 0x0L
        profile.forces.syncword_length.value = 8
        profile.forces.tx_xtal_error_ppm.value = 0
        profile.forces.xtal_frequency_hz.value = 38400000
        profile.forces.symbol_encoding.value = model.vars.symbol_encoding.var_enum.DSSS
        profile.forces.manchester_mapping.value = model.vars.manchester_mapping.var_enum.Default

        # Add 15.4 Packet Configuration
        #Packet Inputs
        profile.forces.frame_bitendian.value = model.vars.frame_bitendian.var_enum.LSB_FIRST
        profile.forces.uart_coding.value = False
        profile.forces.frame_length_type.value = model.vars.frame_length_type.var_enum.VARIABLE_LENGTH
        profile.forces.payload_white_en.value = False
        profile.forces.payload_crc_en.value = True

        #Variable length includes header
        profile.forces.header_en.value = True
        profile.forces.header_size.value = 1
        profile.forces.header_calc_crc.value = False
        profile.forces.header_white_en.value = False

        profile.forces.var_length_numbits.value = 7
        profile.forces.var_length_bitendian.value = model.vars.var_length_bitendian.var_enum.LSB_FIRST
        profile.forces.var_length_shift.value = 0
        profile.forces.var_length_minlength.value = 5
        profile.forces.var_length_maxlength.value = 0x7F
        profile.forces.var_length_includecrc.value = True

        #CRC Inputs
        profile.forces.crc_poly.value = model.vars.crc_poly.var_enum.CCITT_16
        profile.forces.crc_seed.value = 0x00000000L
        profile.forces.crc_input_order.value = model.vars.crc_input_order.var_enum.LSB_FIRST
        profile.forces.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
        profile.forces.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
        profile.forces.crc_pad_input.value = False
        profile.forces.crc_invert.value = False
        
        # Advanced Inputs
        profile.forces.agc_hysteresis.value = 0
        profile.forces.timing_sample_threshold.value = 0
        profile.forces.agc_settling_delay.value = 40
        profile.forces.timing_resync_period.value = 2

        #profile.outputs.AGC_CTRL2_FASTLOOPDEL.override = 4
        profile.forces.append(ModelForce(model.vars.AGC_CTRL2_FASTLOOPDEL, 4))
        #profile.outputs.AGC_GAINSTEPLIM_CFLOOPSTEPMAX.override = 4
        profile.forces.append(ModelForce(model.vars.AGC_GAINSTEPLIM_CFLOOPSTEPMAX, 4))
        #profile.outputs.AGC_LOOPDEL_IFPGADEL.override = 4
        profile.forces.append(ModelForce(model.vars.AGC_LOOPDEL_IFPGADEL, 4))

        profile.forces.baudrate_tol_ppm.value = 4000
        profile.forces.bitrate.value = 250000
        profile.forces.channel_spacing_hz.value = 5000000
        profile.forces.deviation.value = 500000
        profile.forces.dsss_chipping_code.value = 0x744AC39BL
        profile.forces.dsss_len.value = 32
        profile.forces.dsss_spreading_factor.value = 8
        profile.forces.modulation_type.value = model.vars.modulation_type.var_enum.OQPSK
        profile.forces.preamble_length.value = 32
        profile.forces.shaping_filter.value = model.vars.shaping_filter.var_enum.Custom_OQPSK

        # Advanced Inputs
        profile.forces.agc_power_target.value = -6
        profile.forces.rssi_period.value = 8
        profile.forces.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_2520KHz
        profile.forces.timing_detection_threshold.value = 65

