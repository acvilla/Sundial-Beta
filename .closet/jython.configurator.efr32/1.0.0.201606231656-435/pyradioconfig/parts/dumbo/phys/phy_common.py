"""
 This file contains common input settings that might be shared across PHYs
"""

def PHY_COMMON_FRAME_154(phy, model):
    """
    Common Frame Inputs for IEEE 802.15.4
    """

    #Packet Inputs
    phy.profile_inputs.frame_bitendian.value = model.vars.frame_bitendian.var_enum.LSB_FIRST
    phy.profile_inputs.frame_length_type.value = model.vars.frame_length_type.var_enum.VARIABLE_LENGTH
    phy.profile_inputs.payload_white_en.value = False
    phy.profile_inputs.payload_crc_en.value = True

    #Variable length includes header
    phy.profile_inputs.header_en.value = True
    phy.profile_inputs.header_size.value = 1
    phy.profile_inputs.header_calc_crc.value = False
    phy.profile_inputs.header_white_en.value = False

    phy.profile_inputs.var_length_numbits.value = 7
    phy.profile_inputs.var_length_bitendian.value = model.vars.var_length_bitendian.var_enum.LSB_FIRST
    phy.profile_inputs.var_length_shift.value = 0
    phy.profile_inputs.var_length_minlength.value = 5
    phy.profile_inputs.var_length_maxlength.value = 0x7F
    phy.profile_inputs.var_length_includecrc.value = True

    #CRC Inputs
    phy.profile_inputs.crc_poly.value = model.vars.crc_poly.var_enum.CCITT_16
    phy.profile_inputs.crc_seed.value = 0x00000000L
    phy.profile_inputs.crc_input_order.value = model.vars.crc_input_order.var_enum.LSB_FIRST
    phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
    phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
    phy.profile_inputs.crc_pad_input.value = False
    phy.profile_inputs.crc_invert.value = False

def PHY_COMMON_FRAME_BLE(phy, model):
    """
    Common Frame Configuration for Bluetooth Low Energy
    """
    #Packet Inputs
    phy.profile_inputs.frame_bitendian.value = model.vars.frame_bitendian.var_enum.LSB_FIRST
    phy.profile_inputs.frame_length_type.value = model.vars.frame_length_type.var_enum.VARIABLE_LENGTH
    phy.profile_inputs.payload_white_en.value = False
    phy.profile_inputs.payload_crc_en.value = True

    #Variable length includes header
    phy.profile_inputs.header_en.value = True
    phy.profile_inputs.header_size.value = 2
    phy.profile_inputs.header_calc_crc.value = True
    phy.profile_inputs.header_white_en.value = False

    phy.profile_inputs.var_length_numbits.value = 6
    phy.profile_inputs.var_length_bitendian.value = model.vars.var_length_bitendian.var_enum.LSB_FIRST
    phy.profile_inputs.var_length_shift.value = 0
    phy.profile_inputs.var_length_minlength.value = 0
    phy.profile_inputs.var_length_maxlength.value = 47
    phy.profile_inputs.var_length_includecrc.value = False

    #CRC Inputs
    phy.profile_inputs.crc_poly.value = model.vars.crc_poly.var_enum.BLE_24
    phy.profile_inputs.crc_seed.value = 0x00FFFFFFL
    phy.profile_inputs.crc_input_order.value = model.vars.crc_input_order.var_enum.LSB_FIRST
    phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
    phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
    phy.profile_inputs.crc_pad_input.value = False
    phy.profile_inputs.crc_invert.value = False

def PHY_COMMON_FRAME_IOHOME (phy, model):
    """
    """
    #Packet Inputs
    phy.profile_inputs.frame_bitendian.value = model.vars.frame_bitendian.var_enum.LSB_FIRST
    phy.profile_inputs.frame_coding.value = model.vars.frame_coding.var_enum.UART_NO_VAL
    phy.profile_inputs.frame_length_type.value = model.vars.frame_length_type.var_enum.VARIABLE_LENGTH
    phy.profile_inputs.payload_white_en.value = False
    phy.profile_inputs.payload_crc_en.value = True

    #Variable length includes header
    phy.profile_inputs.header_en.value = True
    phy.profile_inputs.header_size.value = 1
    phy.profile_inputs.header_calc_crc.value = True
    phy.profile_inputs.header_white_en.value = False

    phy.profile_inputs.var_length_numbits.value = 5
    phy.profile_inputs.var_length_bitendian.value = model.vars.var_length_bitendian.var_enum.LSB_FIRST
    phy.profile_inputs.var_length_shift.value = 0
    phy.profile_inputs.var_length_minlength.value = 0
    phy.profile_inputs.var_length_maxlength.value = 29
    phy.profile_inputs.var_length_includecrc.value = False

    #CRC Inputs
    phy.profile_inputs.crc_poly.value = model.vars.crc_poly.var_enum.CRC_16
    phy.profile_inputs.crc_seed.value = 0x00000000L
    phy.profile_inputs.crc_input_order.value = model.vars.crc_input_order.var_enum.MSB_FIRST
    phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.LSB_FIRST
    phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
    phy.profile_inputs.crc_pad_input.value = False
    phy.profile_inputs.crc_invert.value = False

def PHY_COMMON_FRAME_INTERNAL(phy, model):
    """
    """
    # Frame Configuration
    #Frame Inputs
    phy.profile_inputs.fixed_length_size.value = 16
    phy.profile_inputs.frame_length_type.value = model.vars.frame_length_type.var_enum.FIXED_LENGTH
    phy.profile_inputs.header_en.value = False
    phy.profile_inputs.frame_bitendian.value = model.vars.frame_bitendian.var_enum.LSB_FIRST
    phy.profile_inputs.payload_crc_en.value = True
    phy.profile_inputs.payload_white_en.value = False

    #CRC Inputs
    phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
    phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.LSB_FIRST
    phy.profile_inputs.crc_seed.value = 0x00000000L
    phy.profile_inputs.crc_input_order.value = model.vars.crc_input_order.var_enum.LSB_FIRST
    phy.profile_inputs.crc_invert.value = False
    phy.profile_inputs.crc_pad_input.value = False
    phy.profile_inputs.crc_poly.value = model.vars.crc_poly.var_enum.CRC_16
