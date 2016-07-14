from pyradioconfig.pycalcmodel import ModelInput, ModelOutput, ModelForce, ModelOutputType, ModelInputType, ModelInputDefaultVisibilityType

def _buildModelOutputStringFromRegisterField(hw_string, category):
    """
    Generic template to build a Model Output based on a hardware register
    """
    return "ModelOutput(model.vars.{0}, '{1}', ModelOutputType.SVD_REG_FIELD, readable_name = '{0}')".format(hw_string, category)

def buildCrcIO(model, profile):
    """
    Builds the inputs and outputs of the CRC block
    """
    # CRC Config Inputs
    profile.inputs.append(ModelInput(model.vars.crc_poly, 'crc', ModelInputType.REQUIRED, default=model.vars.crc_poly.var_enum.NONE, readable_name="CRC Polynomial"))
    profile.inputs.append(ModelInput(model.vars.crc_seed, 'crc', ModelInputType.OPTIONAL, default=0L, readable_name="CRC Seed", value_limit_min=0L, value_limit_max=0xFFFFFFFFL))
    profile.inputs.append(ModelInput(model.vars.crc_byte_endian, 'crc', ModelInputType.OPTIONAL, default=model.vars.crc_byte_endian.var_enum.MSB_FIRST, readable_name="CRC Byte Endian"))
    profile.inputs.append(ModelInput(model.vars.crc_bit_endian, 'crc', ModelInputType.OPTIONAL, default=model.vars.crc_bit_endian.var_enum.MSB_FIRST, readable_name="TX CRC Bit Endian"))
    profile.inputs.append(ModelInput(model.vars.crc_pad_input, 'crc', ModelInputType.OPTIONAL, default=False, readable_name="CRC Input Padding"))
    profile.inputs.append(ModelInput(model.vars.crc_input_order, 'crc', ModelInputType.OPTIONAL, default=model.vars.crc_input_order.var_enum.LSB_FIRST, readable_name="RX CRC Bit Endian"))
    profile.inputs.append(ModelInput(model.vars.crc_invert, 'crc', ModelInputType.OPTIONAL, default=False, readable_name="CRC Invert"))

    #Outputs
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('CRC_CTRL_PADCRCINPUT', 'crc')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('CRC_CTRL_BITSPERWORD', 'crc')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('CRC_CTRL_BITREVERSE', 'crc')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('CRC_CTRL_BYTEREVERSE', 'crc')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('CRC_CTRL_INPUTBITORDER', 'crc')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('CRC_CTRL_CRCWIDTH', 'crc')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('CRC_CTRL_OUTPUTINV', 'crc')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('CRC_INIT_INIT', 'crc')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('CRC_POLY_POLY', 'crc')))

def buildWhiteIO(model, profile):
    """
    Builds the inputs and outputs of the Whitening block
    """
    #Inputs
    profile.inputs.append(ModelInput(model.vars.white_poly, 'whitening', ModelInputType.REQUIRED, default=model.vars.white_poly.var_enum.NONE, readable_name="Whitening Polynomial"))
    profile.inputs.append(ModelInput(model.vars.white_seed, 'whitening', ModelInputType.OPTIONAL, default=0x00000000, readable_name="Whitening Seed", value_limit_min=0, value_limit_max=0xFFFF))
    profile.inputs.append(ModelInput(model.vars.white_output_bit, 'whitening', ModelInputType.OPTIONAL, default=0, readable_name="Whitening Output Bit", value_limit_min=0, value_limit_max=0x0F))

    #Output
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_WHITECTRL_SHROUTPUTSEL', 'whitening')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_WHITECTRL_XORFEEDBACK', 'whitening')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_WHITECTRL_FEEDBACKSEL', 'whitening')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_WHITEPOLY_POLY', 'whitening')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_WHITEINIT_WHITEINIT', 'whitening')))

def buildFecIO(model, profile):
    """
    Builds the inputs and outputs of the FEC block
    """
    #Inputs
    profile.inputs.append(ModelInput(model.vars.fec_en, 'Channel_Coding', ModelInputType.OPTIONAL, default=model.vars.fec_en.var_enum.NONE, readable_name="FEC Algorithm"))

    #Outputs
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FECCTRL_CONVMODE', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FECCTRL_CONVDECODEMODE', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FECCTRL_CONVTRACEBACKDISABLE', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FECCTRL_CONVINV', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FECCTRL_INTERLEAVEMODE', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FECCTRL_INTERLEAVEFIRSTINDEX', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FECCTRL_INTERLEAVEWIDTH', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FECCTRL_CONVBUSLOCK', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FECCTRL_CONVSUBFRAMETERMINATE', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FECCTRL_SINGLEBLOCK', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FECCTRL_FORCE2FSK', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FECCTRL_CONVHARDERROR', 'fec')))

    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_CONVRAMADDR_CONVRAMADDR', 'fec')))

    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_TRAILTXDATACTRL_TRAILTXDATA', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_TRAILTXDATACTRL_TRAILTXDATACNT', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_TRAILTXDATACTRL_TRAILTXDATAFORCE', 'fec')))

    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_CONVGENERATOR_GENERATOR0', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_CONVGENERATOR_GENERATOR1', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_CONVGENERATOR_RECURSIVE', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_CONVGENERATOR_NONSYSTEMATIC', 'fec')))

    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_PUNCTCTRL_PUNCT0', 'fec')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_PUNCTCTRL_PUNCT1', 'fec')))

def buildFrameIO(model, profile):
    """
    Builds the inputs and outputs of the general frame settings
    """
    MIN_FRAME_LENGTH = 1
    MAX_FRAME_LENGTH = 240
    MIN_HEADER_LENGTH = 0
    MAX_HEADER_LENGTH = 254
    #Inputs
    profile.inputs.append(ModelInput(model.vars.frame_bitendian, 'frame_general', ModelInputType.REQUIRED, default=model.vars.frame_bitendian.var_enum.LSB_FIRST, readable_name="Frame Bit Endian"))
    profile.inputs.append(ModelInput(model.vars.uart_coding, 'frame_general', ModelInputType.REQUIRED, default=False, readable_name="UART Mode", deprecated=True, default_visibility=ModelInputDefaultVisibilityType.HIDDEN))
    profile.inputs.append(ModelInput(model.vars.frame_length_type, 'frame_general', ModelInputType.REQUIRED, default=model.vars.frame_length_type.var_enum.FIXED_LENGTH, readable_name="Frame Length Algorithm"))
    profile.inputs.append(ModelInput(model.vars.header_en, 'frame_general', ModelInputType.REQUIRED, default=False, readable_name="Header Enable"))
    profile.inputs.append(ModelInput(model.vars.frame_coding, 'frame_general', ModelInputType.REQUIRED, default=model.vars.frame_coding.var_enum.NONE, readable_name="Frame Coding Method"))
    # profile.inputs.append(ModelInput(model.vars.accept_crc_errors, 'frame', ModelInputType.REQUIRED, default=False))

    # -- Payload --
    profile.inputs.append(ModelInput(model.vars.payload_white_en, 'frame_payload', ModelInputType.REQUIRED, default=False, readable_name="Payload Whitening Enable"))
    profile.inputs.append(ModelInput(model.vars.payload_crc_en, 'frame_payload', ModelInputType.REQUIRED, default=False, readable_name="Payload CRC Enable"))

    # -- Header --
    profile.inputs.append(ModelInput(model.vars.header_size, 'frame_header', ModelInputType.OPTIONAL, default=0, readable_name="Header Size", value_limit_min=MIN_HEADER_LENGTH, value_limit_max=MAX_HEADER_LENGTH))
    profile.inputs.append(ModelInput(model.vars.header_calc_crc, 'frame_header', ModelInputType.OPTIONAL, default=False, readable_name="CRC Header"))
    # profile.inputs.append(ModelInput(model.vars.header_include_crc, 'frame_header', ModelInputType.OPTIONAL, default=False))
    profile.inputs.append(ModelInput(model.vars.header_white_en, 'frame_header', ModelInputType.OPTIONAL, default=False, readable_name="Whiten Header"))

    # -- Fixed Length --
    # RAIL doesn't support packets longer than 255 (appended info inclusive) so restrict this.
    # I do realize that header+frame_fixed_length can possibly exceed this.
    profile.inputs.append(ModelInput(model.vars.fixed_length_size, 'frame_fixed_length', ModelInputType.OPTIONAL, default=1, readable_name="Fixed Payload Size", value_limit_min=MIN_FRAME_LENGTH, value_limit_max=MAX_FRAME_LENGTH))

    # -- Variable Length --
    profile.inputs.append(ModelInput(model.vars.var_length_numbits, 'frame_var_length', ModelInputType.OPTIONAL, default=0, readable_name="Variable Length Bit Size", value_limit_min=0, value_limit_max=12))
    profile.inputs.append(ModelInput(model.vars.var_length_bitendian, 'frame_var_length', ModelInputType.OPTIONAL, default=model.vars.var_length_bitendian.var_enum.LSB_FIRST, readable_name="Variable Length Bit Endian"))
    profile.inputs.append(ModelInput(model.vars.var_length_byteendian, 'frame_var_length', ModelInputType.OPTIONAL, default=model.vars.var_length_byteendian.var_enum.LSB_FIRST, readable_name="Variable Length Byte Endian"))
    profile.inputs.append(ModelInput(model.vars.var_length_shift, 'frame_var_length', ModelInputType.OPTIONAL, default=0, readable_name="Variable Length Bit Location", value_limit_min=0, value_limit_max=7))
    profile.inputs.append(ModelInput(model.vars.var_length_minlength, 'frame_var_length', ModelInputType.OPTIONAL, default=0, readable_name="Minimum Length", value_limit_min=0, value_limit_max=4095))
    profile.inputs.append(ModelInput(model.vars.var_length_maxlength, 'frame_var_length', ModelInputType.OPTIONAL, default=0, readable_name="Maximum Length", value_limit_min=0, value_limit_max=4095))
    profile.inputs.append(ModelInput(model.vars.var_length_includecrc, 'frame_var_length', ModelInputType.OPTIONAL, default=False, readable_name="Length Includes CRC Bytes"))

    # -- Frame Type --
    profile.inputs.append(ModelInput(model.vars.frame_type_loc, 'frame_type_length', ModelInputType.OPTIONAL, default=0, readable_name="Frame Type Location", value_limit_min=0, value_limit_max=255))
    profile.inputs.append(ModelInput(model.vars.frame_type_bits, 'frame_type_length', ModelInputType.OPTIONAL, default=0, readable_name="Number of Frame Type Bits", value_limit_min=0, value_limit_max=3))
    profile.inputs.append(ModelInput(model.vars.frame_type_lsbit, 'frame_type_length', ModelInputType.OPTIONAL, default=0, readable_name="Frame Type Bit 0 Location", value_limit_min=0, value_limit_max=0x7))
    profile.inputs.append(ModelInput(model.vars.frame_type_0_length, 'frame_type_length', ModelInputType.OPTIONAL, default=0, readable_name="Frame Type 0 Length", value_limit_min=0, value_limit_max=MAX_FRAME_LENGTH))
    profile.inputs.append(ModelInput(model.vars.frame_type_1_length, 'frame_type_length', ModelInputType.OPTIONAL, default=0, readable_name="Frame Type 1 Length", value_limit_min=0, value_limit_max=MAX_FRAME_LENGTH))
    profile.inputs.append(ModelInput(model.vars.frame_type_2_length, 'frame_type_length', ModelInputType.OPTIONAL, default=0, readable_name="Frame Type 2 Length", value_limit_min=0, value_limit_max=MAX_FRAME_LENGTH))
    profile.inputs.append(ModelInput(model.vars.frame_type_3_length, 'frame_type_length', ModelInputType.OPTIONAL, default=0, readable_name="Frame Type 3 Length", value_limit_min=0, value_limit_max=MAX_FRAME_LENGTH))
    profile.inputs.append(ModelInput(model.vars.frame_type_4_length, 'frame_type_length', ModelInputType.OPTIONAL, default=0, readable_name="Frame Type 4 Length", value_limit_min=0, value_limit_max=MAX_FRAME_LENGTH))
    profile.inputs.append(ModelInput(model.vars.frame_type_5_length, 'frame_type_length', ModelInputType.OPTIONAL, default=0, readable_name="Frame Type 5 Length", value_limit_min=0, value_limit_max=MAX_FRAME_LENGTH))
    profile.inputs.append(ModelInput(model.vars.frame_type_6_length, 'frame_type_length', ModelInputType.OPTIONAL, default=0, readable_name="Frame Type 6 Length", value_limit_min=0, value_limit_max=MAX_FRAME_LENGTH))
    profile.inputs.append(ModelInput(model.vars.frame_type_7_length, 'frame_type_length', ModelInputType.OPTIONAL, default=0, readable_name="Frame Type 7 Length", value_limit_min=0, value_limit_max=MAX_FRAME_LENGTH))
    profile.inputs.append(ModelInput(model.vars.frame_type_0_valid, 'frame_type_length', ModelInputType.OPTIONAL, default=False, readable_name="Frame Type 0 Valid"))
    profile.inputs.append(ModelInput(model.vars.frame_type_1_valid, 'frame_type_length', ModelInputType.OPTIONAL, default=False, readable_name="Frame Type 1 Valid"))
    profile.inputs.append(ModelInput(model.vars.frame_type_2_valid, 'frame_type_length', ModelInputType.OPTIONAL, default=False, readable_name="Frame Type 2 Valid"))
    profile.inputs.append(ModelInput(model.vars.frame_type_3_valid, 'frame_type_length', ModelInputType.OPTIONAL, default=False, readable_name="Frame Type 3 Valid"))
    profile.inputs.append(ModelInput(model.vars.frame_type_4_valid, 'frame_type_length', ModelInputType.OPTIONAL, default=False, readable_name="Frame Type 4 Valid"))
    profile.inputs.append(ModelInput(model.vars.frame_type_5_valid, 'frame_type_length', ModelInputType.OPTIONAL, default=False, readable_name="Frame Type 5 Valid"))
    profile.inputs.append(ModelInput(model.vars.frame_type_6_valid, 'frame_type_length', ModelInputType.OPTIONAL, default=False, readable_name="Frame Type 6 Valid"))
    profile.inputs.append(ModelInput(model.vars.frame_type_7_valid, 'frame_type_length', ModelInputType.OPTIONAL, default=False, readable_name="Frame Type 7 Valid"))

    #Outputs
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FECCTRL_BLOCKWHITEMODE', 'frame')))

    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_CTRL_BITSPERWORD', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_CTRL_RXFCDMODE', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_CTRL_TXFCDMODE', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_CTRL_BITORDER', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_CTRL_UARTMODE', 'frame')))

    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_WCNTCMP0_FRAMELENGTH', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_WCNTCMP1_LENGTHFIELDLOC', 'frame')))

    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_DFLCTRL_DFLINCLUDECRC', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_DFLCTRL_MINLENGTH', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_DFLCTRL_DFLBITS', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_DFLCTRL_DFLOFFSET', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_DFLCTRL_DFLSHIFT', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_DFLCTRL_DFLBITORDER', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_DFLCTRL_DFLMODE', 'frame')))

    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_MAXLENGTH_MAXLENGTH', 'frame')))

    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD0_SKIPWHITE', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD0_SKIPCRC', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD0_CALCCRC', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD0_INCLUDECRC', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD0_BUFFER', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD0_WORDS', 'frame')))

    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD1_SKIPWHITE', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD1_SKIPCRC', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD1_CALCCRC', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD1_INCLUDECRC', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD1_BUFFER', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD1_WORDS', 'frame')))

    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD2_SKIPWHITE', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD2_SKIPCRC', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD2_CALCCRC', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD2_INCLUDECRC', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD2_BUFFER', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD2_WORDS', 'frame')))

    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD3_SKIPWHITE', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD3_SKIPCRC', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD3_CALCCRC', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD3_INCLUDECRC', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD3_BUFFER', 'frame')))
    profile.outputs.append(eval(_buildModelOutputStringFromRegisterField('FRC_FCD3_WORDS', 'frame')))


