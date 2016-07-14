"""
This defines generic frame/packet configurations and calculation
This file also houses calculations for fields that are affected by multiiple blocks:
  calc_blockwhitemode(): calc_white, calc_fec

"""
"""
Calculator functions are pulled by using their names.
Calculator functions must start with "calc_", if they are to be consumed by the framework.
    Or they should be returned by overriding the function:
        def getCalculationList(self):
"""

import inspect
from enum import Enum
from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pyradioconfig.pycalcmodel import ModelVariableFormat, CreateModelVariableEnum
from pyradioconfig.pycalcmodel import ModelVariableEmptyValue, ModelVariableInvalidValueType

class CALC_Frame(ICalculator):

    """
    Init internal variables
    """
    def __init__(self):
        self._major = 1
        self._minor = 0
        self._patch = 0

    def buildVariables(self, model):
        """Populates a list of needed variables for this calculator

        Args:
            model (ModelRoot) : Builds the variables specific to this calculator
        """

        """
        #Inputs
        """
        #-------- General Frame Configurations --------
        # BIT_ORDER
        var = self._addModelVariable(model, 'frame_bitendian', Enum, ModelVariableFormat.DECIMAL, 'Define how the payload bits are transmitted over the air')
        member_data = [
            ['LSB_FIRST' , 0, 'Least significant bit is transmitted first over the air'],
            ['MSB_FIRST',  1, 'Most significant bit is transmitted first over the air'],
        ]
        var.var_enum = CreateModelVariableEnum(
            'bitEndian',
            'Define how the payload bits are transmitted over the air',
            member_data)

        #UART_MODE
        self._addModelVariable(model, 'uart_coding', bool, ModelVariableFormat.ASCII, 'Set to true to enable uart coding of the frame.')

        #FRAME_LENGTH
        var = self._addModelVariable(model, 'frame_length_type', Enum, ModelVariableFormat.DECIMAL, 'Possible Length Configurations')
        member_data = [
            ['FIXED_LENGTH' , 0, 'The frame length is fixed and never changes'],
            ['VARIABLE_LENGTH',  1, 'The frame length is determined by an explicit length field within the packet. Requires header to be enabled.'],
            ['FRAME_TYPE',  2, 'The packet length is determined from an encoded set of bit that implicitly determines the length'],
        ]
        var.var_enum = CreateModelVariableEnum(
            'FrameLengthEnum',
            'List of supported frame length configurations',
            member_data)

        #payload_white_en
        self._addModelVariable(model, 'payload_white_en', bool, ModelVariableFormat.ASCII, 'Set to true to whiten the payload')
        #payload_crc_en
        self._addModelVariable(model, 'payload_crc_en', bool, ModelVariableFormat.ASCII, 'Set to true to crc the payload')
        #ACCEPT_CRC_ERRORS
        self._addModelVariable(model, 'accept_crc_errors', bool, ModelVariableFormat.ASCII, 'Set to true if you want to accept invalid crcs')

        #-------- Header Configurations --------
        #HEADER_ENABLE
        self._addModelVariable(model, 'header_en', bool, ModelVariableFormat.ASCII, 'Set to true to enable a distinct header from the payload.')
        #HEADER_SIZE
        self._addModelVariable(model, 'header_size', int, ModelVariableFormat.DECIMAL, units='bytes', desc='Define the number of bytes that make up the header. Include the variable length byte(s).')
        #HEADER_CALC_CRC
        self._addModelVariable(model, 'header_calc_crc', bool, ModelVariableFormat.ASCII, 'Set to true to include the header bytes in the CRC.')
        #HEADER_CALC_CRC
        self._addModelVariable(model, 'header_include_crc', bool, ModelVariableFormat.ASCII, 'Set to true to check/transmit crc specifically for the header')
        #HEADER_WHITE_EN
        self._addModelVariable(model, 'header_white_en', bool, ModelVariableFormat.ASCII, 'Set to true to enable whitening over the header')

        #-------- Fixed Length Configurations --------
        #FIXED_LENGTH_SIZE
        self._addModelVariable(model, 'fixed_length_size', int, ModelVariableFormat.DECIMAL, units='bytes', desc='Define the number of bytes in the payload. This does not include the length of the header if used. Header + Payload must be less than 4096 bytes.')

        #-------- Variable Length Configurations --------
        #VARIABLE_LENGTH_LOCATION
        self._addModelVariable(model, 'var_length_loc', int, ModelVariableFormat.DECIMAL, 'Define the zero-based start location in the header that holds the variable length field.')
        #VARIABLE_LENGTH_NUMBYTES
        self._addModelVariable(model, 'var_length_numbytes', int, ModelVariableFormat.DECIMAL, units='bytes', desc='Define the size of the variable length field in bytes.')
        #VARIABLE_LENGTH_NUMBITS
        self._addModelVariable(model, 'var_length_numbits', int, ModelVariableFormat.DECIMAL, units='bits', desc='Define the size of the variable length field in bits.')
        #VARIABLE_LENGTH_BYTEENDIAN
        var = self._addModelVariable(model, 'var_length_byteendian', Enum, ModelVariableFormat.DECIMAL, 'Define the byte endianness of the variable length field')
        member_data = [
            ['LSB_FIRST' , 0, 'The least significant byte of the variable length field is transmitted over the air first.'],
            ['MSB_FIRST' , 1, 'The most significant byte of the variable length field is transmitted over the air first.'],
        ]
        var.var_enum = CreateModelVariableEnum(
            'VarLengthByteEndian',
            'Define how the variable length byte(s) are transmitted over the air',
            member_data)
        #VARIABLE_LENGTH_BITENDIAN
        var = self._addModelVariable(model, 'var_length_bitendian', Enum, ModelVariableFormat.DECIMAL, 'Define the bit endianness of the variable length field')
        member_data = [
            ['LSB_FIRST' , 0, 'The variable length field is transmitted least signficant bit first.'],
            ['MSB_FIRST' , 1, 'The variable length field is transmitted most significant bit first.'],
        ]
        var.var_enum = CreateModelVariableEnum(
            'VarLengthBitEndian',
            'Define how the variable length bits are transmitted over the air',
            member_data)
        #VARIABLE_LENGTH_SHIFT
        self._addModelVariable(model, 'var_length_shift', int, ModelVariableFormat.DECIMAL, 'Define the location of the least significant bit of the variable length field.')
        #VARIABLE_LENGTH_MINLENGTH
        self._addModelVariable(model, 'var_length_minlength', int, ModelVariableFormat.DECIMAL, units='bytes', desc='Define the minimum value of the variable length field.')
        #VARIABLE_LENGTH_MAXLENGTH
        self._addModelVariable(model, 'var_length_maxlength', int, ModelVariableFormat.DECIMAL, units='bytes', desc='Define the maximum value of the variable length field. Cannot exceed the variable length size.')
        #VARIABLE_LENGTH_INCLUDECRC
        self._addModelVariable(model, 'var_length_includecrc', bool, ModelVariableFormat.ASCII, 'Set to true if the crc bytes are included in the variable length')

        #-------- Frame Type Configurations --------
        #FRAME_TYPE
        self._addModelVariable(model, 'frame_type_loc', int, ModelVariableFormat.DECIMAL, 'Define the zero-based start location in the frame that holds the frame type encoding.')
        self._addModelVariable(model, 'frame_type_mask', int, ModelVariableFormat.HEX, 'Define the bitmask to extract the frame type in the byte.')
        self._addModelVariable(model, 'frame_type_bits', int, ModelVariableFormat.DECIMAL, desc='Define the number of bits of the frame type field.', units='bits')
        self._addModelVariable(model, 'frame_type_lsbit', int, ModelVariableFormat.DECIMAL, "Define the bit location of the frame type's least significant bit.")
        self._addModelVariable(model, 'frame_type_lengths', int, ModelVariableFormat.DECIMAL, desc='Define the frame length of each frame type.', is_array=True, units='bytes')
        self._addModelVariable(model, 'frame_type_valid', bool, ModelVariableFormat.ASCII, desc='Define the valid frame types.', is_array=True)

        #@bug https://jira.silabs.com/browse/MCUW_RADIO_CFG-37
        # This is a temporary measure to not use is_array
        self._addModelVariable(model, 'frame_type_0_length', int, ModelVariableFormat.DECIMAL, desc='Define the frame length of each frame type.', units='bytes')
        self._addModelVariable(model, 'frame_type_1_length', int, ModelVariableFormat.DECIMAL, desc='Define the frame length of each frame type.', units='bytes')
        self._addModelVariable(model, 'frame_type_2_length', int, ModelVariableFormat.DECIMAL, desc='Define the frame length of each frame type.', units='bytes')
        self._addModelVariable(model, 'frame_type_3_length', int, ModelVariableFormat.DECIMAL, desc='Define the frame length of each frame type.', units='bytes')
        self._addModelVariable(model, 'frame_type_4_length', int, ModelVariableFormat.DECIMAL, desc='Define the frame length of each frame type.', units='bytes')
        self._addModelVariable(model, 'frame_type_5_length', int, ModelVariableFormat.DECIMAL, desc='Define the frame length of each frame type.', units='bytes')
        self._addModelVariable(model, 'frame_type_6_length', int, ModelVariableFormat.DECIMAL, desc='Define the frame length of each frame type.', units='bytes')
        self._addModelVariable(model, 'frame_type_7_length', int, ModelVariableFormat.DECIMAL, desc='Define the frame length of each frame type.', units='bytes')

        self._addModelVariable(model, 'frame_type_0_valid', bool, ModelVariableFormat.ASCII, desc='Define the valid frame types.')
        self._addModelVariable(model, 'frame_type_1_valid', bool, ModelVariableFormat.ASCII, desc='Define the valid frame types.')
        self._addModelVariable(model, 'frame_type_2_valid', bool, ModelVariableFormat.ASCII, desc='Define the valid frame types.')
        self._addModelVariable(model, 'frame_type_3_valid', bool, ModelVariableFormat.ASCII, desc='Define the valid frame types.')
        self._addModelVariable(model, 'frame_type_4_valid', bool, ModelVariableFormat.ASCII, desc='Define the valid frame types.')
        self._addModelVariable(model, 'frame_type_5_valid', bool, ModelVariableFormat.ASCII, desc='Define the valid frame types.')
        self._addModelVariable(model, 'frame_type_6_valid', bool, ModelVariableFormat.ASCII, desc='Define the valid frame types.')
        self._addModelVariable(model, 'frame_type_7_valid', bool, ModelVariableFormat.ASCII, desc='Define the valid frame types.')

        #-------- Frame Coding--------
        var = self._addModelVariable(model, 'frame_coding', Enum, ModelVariableFormat.DECIMAL, 'List of supported frame coding methods')
        member_data = [
            ['NONE' , 0, 'No Frame Coding'],
            ['UART_NO_VAL', 1, 'UART Frame Coding without start/stop bit validation'],
            ['UART_VAL', 2, 'UART Frame Coding with start/stop bit validation'],
        ]
        var.var_enum = CreateModelVariableEnum(
            'FrameCodingEnum',
            'List of supported Frame Coding Methods',
            member_data)

        """
        #Outputs
        """
        var = self._addModelVariable(model, 'frame_coding_array', int, ModelVariableFormat.DECIMAL, is_array=True)
        self._addModelRegister(model, 'FRC.FECCTRL.BLOCKWHITEMODE', int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'FRC.CTRL.BITSPERWORD', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.CTRL.RXFCDMODE', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.CTRL.TXFCDMODE', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.CTRL.BITORDER', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.CTRL.UARTMODE', int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'FRC.WCNTCMP0.FRAMELENGTH', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.WCNTCMP1.LENGTHFIELDLOC', int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'FRC.DFLCTRL.DFLINCLUDECRC', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.DFLCTRL.MINLENGTH', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.DFLCTRL.DFLBITS', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.DFLCTRL.DFLOFFSET', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.DFLCTRL.DFLSHIFT', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.DFLCTRL.DFLBITORDER', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.DFLCTRL.DFLMODE', int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'FRC.MAXLENGTH.MAXLENGTH', int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'FRC.FCD0.SKIPWHITE', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD0.SKIPCRC', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD0.CALCCRC', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD0.INCLUDECRC', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD0.BUFFER', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD0.WORDS', int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'FRC.FCD1.SKIPWHITE', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD1.SKIPCRC', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD1.CALCCRC', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD1.INCLUDECRC', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD1.BUFFER', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD1.WORDS', int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'FRC.FCD2.SKIPWHITE', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD2.SKIPCRC', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD2.CALCCRC', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD2.INCLUDECRC', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD2.BUFFER', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD2.WORDS', int, ModelVariableFormat.HEX )

        self._addModelRegister(model, 'FRC.FCD3.SKIPWHITE', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD3.SKIPCRC', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD3.CALCCRC', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD3.INCLUDECRC', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD3.BUFFER', int, ModelVariableFormat.HEX )
        self._addModelRegister(model, 'FRC.FCD3.WORDS', int, ModelVariableFormat.HEX )


    def _calc_frame_length_defaults(self, model):
        """_calc_frame_length_defaults

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        self._reg_write(model.vars.FRC_WCNTCMP0_FRAMELENGTH, 0)
        self._reg_write(model.vars.FRC_WCNTCMP1_LENGTHFIELDLOC, 0)

        self._reg_write(model.vars.FRC_DFLCTRL_DFLINCLUDECRC, 0)
        self._reg_write(model.vars.FRC_DFLCTRL_MINLENGTH, 0)
        self._reg_write(model.vars.FRC_DFLCTRL_DFLBITS, 0)
        self._reg_write(model.vars.FRC_DFLCTRL_DFLOFFSET, 0)
        self._reg_write(model.vars.FRC_DFLCTRL_DFLSHIFT, 0)
        self._reg_write(model.vars.FRC_DFLCTRL_DFLBITORDER, 0)
        self._reg_write(model.vars.FRC_DFLCTRL_DFLMODE, 0)

        self._reg_write(model.vars.FRC_MAXLENGTH_MAXLENGTH, 0)

        self._reg_write(model.vars.FRC_FCD0_SKIPWHITE, 0)
        self._reg_write(model.vars.FRC_FCD0_SKIPCRC, 0)
        self._reg_write(model.vars.FRC_FCD0_CALCCRC, 0)
        self._reg_write(model.vars.FRC_FCD0_INCLUDECRC, 0)
        self._reg_write(model.vars.FRC_FCD0_BUFFER, 0)
        self._reg_write(model.vars.FRC_FCD0_WORDS, 0)

        self._reg_write(model.vars.FRC_FCD1_SKIPWHITE, 0)
        self._reg_write(model.vars.FRC_FCD1_SKIPCRC, 0)
        self._reg_write(model.vars.FRC_FCD1_CALCCRC, 0)
        self._reg_write(model.vars.FRC_FCD1_INCLUDECRC, 0)
        self._reg_write(model.vars.FRC_FCD1_BUFFER, 0)
        self._reg_write(model.vars.FRC_FCD1_WORDS, 0)

        self._reg_write(model.vars.FRC_FCD2_SKIPWHITE, 0)
        self._reg_write(model.vars.FRC_FCD2_SKIPCRC, 0)
        self._reg_write(model.vars.FRC_FCD2_CALCCRC, 0)
        self._reg_write(model.vars.FRC_FCD2_INCLUDECRC, 0)
        self._reg_write(model.vars.FRC_FCD2_BUFFER, 0)
        self._reg_write(model.vars.FRC_FCD2_WORDS, 0)

        self._reg_write(model.vars.FRC_FCD3_SKIPWHITE, 0)
        self._reg_write(model.vars.FRC_FCD3_SKIPCRC, 0)
        self._reg_write(model.vars.FRC_FCD3_CALCCRC, 0)
        self._reg_write(model.vars.FRC_FCD3_INCLUDECRC, 0)
        self._reg_write(model.vars.FRC_FCD3_BUFFER, 0)
        self._reg_write(model.vars.FRC_FCD3_WORDS, 0)
        return

    def _configure_fcd(self, model, fcdindex, skipwhite, skipcrc, calccrc, includecrc, buf, words):
        """_configure_fcd

        Args:
            model (ModelRoot) : Data model to read and write variables from
            fcdindex (unknown) : unknown
            skipwhite (unknown) : unknown
            skipcrc (unknown) : unknown
            calccrc (unknown) : unknown
            includecrc (unknown) : unknown
            buf (unknown) : unknown
            words (unknown) : unknown
        """

        if model.vars.ber_force_whitening.value == True:
            self._reg_write(eval("model.vars.FRC_FCD{}_SKIPWHITE".format(fcdindex)), 0)
        else:
            self._reg_write(eval("model.vars.FRC_FCD{}_SKIPWHITE".format(fcdindex)), skipwhite)
        
        self._reg_write(eval("model.vars.FRC_FCD{}_SKIPCRC".format(fcdindex)), skipcrc)
        self._reg_write(eval("model.vars.FRC_FCD{}_CALCCRC".format(fcdindex)), calccrc)
        self._reg_write(eval("model.vars.FRC_FCD{}_INCLUDECRC".format(fcdindex)), includecrc)
        self._reg_write(eval("model.vars.FRC_FCD{}_BUFFER".format(fcdindex)), buf)
        self._reg_write(eval("model.vars.FRC_FCD{}_WORDS".format(fcdindex)), words)
        return

    def _configure_header(self, model):
        """_configure_header

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        #Header Configuration
        fcdDict = {
            "skipwhite": int(model.vars.header_white_en.value == False),
            "skipcrc": 0,
            "calccrc": int(model.vars.header_calc_crc.value == True),
            "includecrc": int(model.vars.header_include_crc.value == True),
            "words": model.vars.header_size.value - 1,
        }
        #Configure TX FCD
        self._configure_fcd(model, fcdindex="0", buf=0, **fcdDict)
        #Configure RX FCD
        self._configure_fcd(model, fcdindex="2", buf=1, **fcdDict)
        return

    def _configure_payload_with_header(self, model):
        """_configure_payload_with_header

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        #Payload Configuration
        fcdDict = {
            "skipwhite": int(model.vars.payload_white_en.value == False),
            "skipcrc": 0,
            "calccrc": int(model.vars.payload_crc_en.value == True),
            "includecrc": int(model.vars.payload_crc_en.value == True),
            "words": 0xFF,
        }
        #Configure TX FCD
        self._configure_fcd(model, fcdindex="1", buf=0, **fcdDict)
        #Configure RX FCD
        self._configure_fcd(model, fcdindex="3", buf=1, **fcdDict)
        return

    def _fixed_length_with_header(self, model):
        """_fixed_length_with_header

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        self._reg_write(model.vars.FRC_WCNTCMP0_FRAMELENGTH, model.vars.fixed_length_size.value + model.vars.header_size.value - 1)

        #Header Configuration
        self._configure_header(model)

        #Payload Configuration
        self._configure_payload_with_header(model)

        #Use FCD0/2 for first subframe then FCD1/3 is used for all following subframes
        self._reg_write(model.vars.FRC_CTRL_TXFCDMODE, 2)
        self._reg_write(model.vars.FRC_CTRL_RXFCDMODE, 2)
        return

    def _fixed_length_no_header(self, model):
        """_fixed_length_no_header

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        self._reg_write(model.vars.FRC_WCNTCMP0_FRAMELENGTH, model.vars.fixed_length_size.value - 1)
        fcdDict = {
            "skipwhite": int(model.vars.payload_white_en.value == False),
            "skipcrc": 0,
            "calccrc": int(model.vars.payload_crc_en.value == True),
            "includecrc": int(model.vars.payload_crc_en.value == True),
            "words": 0xFF,
        }
        #Configure TX FCD
        self._configure_fcd(model, fcdindex="0", buf=0, **fcdDict)
        self._reg_write(model.vars.FRC_CTRL_TXFCDMODE, 0)
        #Configure RX FCD
        self._configure_fcd(model, fcdindex="2", buf=1, **fcdDict)
        self._reg_write(model.vars.FRC_CTRL_RXFCDMODE, 0)
        return

    def _configure_variable_length(self, model):
        """_configure_variable_length

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        self._reg_write(model.vars.FRC_WCNTCMP1_LENGTHFIELDLOC, model.vars.var_length_loc.value)
        self._reg_write(model.vars.FRC_MAXLENGTH_MAXLENGTH, model.vars.var_length_maxlength.value)

        self._reg_write(model.vars.FRC_DFLCTRL_DFLINCLUDECRC, int(model.vars.var_length_includecrc.value == True))
        self._reg_write(model.vars.FRC_DFLCTRL_MINLENGTH, model.vars.var_length_minlength.value)
        self._reg_write(model.vars.FRC_DFLCTRL_DFLBITS, model.vars.var_length_numbits.value)
        self._reg_write(model.vars.FRC_DFLCTRL_DFLOFFSET, model.vars.var_length_loc.value)
        self._reg_write(model.vars.FRC_DFLCTRL_DFLSHIFT, model.vars.var_length_shift.value)
        if (model.vars.var_length_bitendian.value.value != model.vars.frame_bitendian.value.value):
            self._reg_write(model.vars.FRC_DFLCTRL_DFLBITORDER, 1)
        else:
            self._reg_write(model.vars.FRC_DFLCTRL_DFLBITORDER, 0)

        #DFLMODE
        if (model.vars.ber_force_infinite_length is True):
            # Infinite length
            self._reg_write(model.vars.FRC_DFLCTRL_DFLMODE, 1)
        elif (model.vars.var_length_numbytes.value == 1):
            #SINGLEBYTE
            self._reg_write(model.vars.FRC_DFLCTRL_DFLMODE, 1)
        else: #Two bytes
            if (model.vars.var_length_byteendian.value == model.vars.var_length_byteendian.var_enum.LSB_FIRST):
                #DUALBYTELSBFIRST
                self._reg_write(model.vars.FRC_DFLCTRL_DFLMODE, 3)
            else:
                #DUALBYTEMSBFIRST
                self._reg_write(model.vars.FRC_DFLCTRL_DFLMODE, 4)
        return

    def _configure_frame_type(self, model):
        """_configure_frame_type

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        BIT_MASK = {0: 0x00, 1: 0x01, 2: 0x03, 3: 0x07}
        # Handle Code Generation in RAIL Adapter to create C structures

        #Move from discrete inputs to a list
        num_entries = (2**model.vars.frame_type_bits.value)
        model.vars.frame_type_lengths.value = []
        model.vars.frame_type_valid.value = []
        for i in range(num_entries):
          model.vars.frame_type_lengths.value.append(eval("model.vars.frame_type_{}_length.value".format(i)))
          model.vars.frame_type_valid.value.append(eval("model.vars.frame_type_{}_valid.value".format(i)))

        #Set FRC_WCNTCMP0 to the size of the header
        # The seqeuncer will write this register after it decodes the frame type
        # We just want to provide enough room in advance so that we don't complete the frame too early
        # Init to the smallest valid length
        min_size = 0xFF
        for i in range(len(model.vars.frame_type_lengths.value)):
          if (model.vars.frame_type_valid.value[i] == True):
            if (model.vars.frame_type_lengths.value[i] < min_size):
              min_size = model.vars.frame_type_lengths.value[i]

        self._reg_write(model.vars.FRC_WCNTCMP0_FRAMELENGTH, min_size - 1)

        model.vars.frame_type_mask.value = BIT_MASK[model.vars.frame_type_bits.value] << model.vars.frame_type_lsbit.value

        # Only use one frame descriptor
        fcdDict = {
            "skipwhite": int(model.vars.payload_white_en.value == False),
            "skipcrc": 0,
            "calccrc": int(model.vars.payload_crc_en.value == True),
            "includecrc": int(model.vars.payload_crc_en.value == True),
            "words": 0xFF,
        }
        #Configure TX FCD
        self._configure_fcd(model, fcdindex="0", buf=0, **fcdDict)
        self._reg_write(model.vars.FRC_CTRL_TXFCDMODE, 0)
        #Configure RX FCD
        self._configure_fcd(model, fcdindex="2", buf=1, **fcdDict)
        self._reg_write(model.vars.FRC_CTRL_RXFCDMODE, 0)
        return

    def calc_possible_future_inputs(self, model):
        """
        # This routine initializes variables that could be possible future inputs

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        model.vars.header_include_crc.value = False
        return

    def calc_frame(self, model):
        """
        Configure general frame configurations

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        #Account for +1 in register
        self._reg_write(model.vars.FRC_CTRL_BITSPERWORD, (8 - 1))
        
        if model.vars.ber_force_bitorder.value is True:
            self._reg_write(model.vars.FRC_CTRL_BITORDER, 1)
        else:
            self._reg_write(model.vars.FRC_CTRL_BITORDER, int(model.vars.frame_bitendian.value == model.vars.frame_bitendian.var_enum.MSB_FIRST))
        return

    def calc_frame_length(self, model):
        """calc_frame_length

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        self._calc_frame_length_defaults(model);
        if (model.vars.frame_length_type.value == model.vars.frame_length_type.var_enum.FIXED_LENGTH):
            if (model.vars.header_en.value == True):
                self._fixed_length_with_header(model)
            else:
                self._fixed_length_no_header(model)

        elif (model.vars.frame_length_type.value == model.vars.frame_length_type.var_enum.VARIABLE_LENGTH):
            #Variable Length requires headers
            self._configure_header(model)

            #Variable Length
            self._configure_variable_length(model)

            #Configure rest of payload options
            self._configure_payload_with_header(model)

            #Use FCD0/2 for first subframe then FCD1/3 is used for all following subframes
            self._reg_write(model.vars.FRC_CTRL_TXFCDMODE, 2)
            self._reg_write(model.vars.FRC_CTRL_RXFCDMODE, 2)
        elif (model.vars.frame_length_type.value == model.vars.frame_length_type.var_enum.FRAME_TYPE):
            #Frame Type
            self._configure_frame_type(model)
            pass
        return

    def _frame_coding_UART(self):
        """_frame_coding_UART
        Function creates block coding array for UART frame coding

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        content = []
        for received in range(1024):
          if (received & 0x200) and (not (received & 0x001)):
            content.append((received >> 1) & 0xFF)
          else:
            content.append(0x8000 + ((received >> 1) & 0xFF))

        # Transmit table
        for i in range(256):
          content.append(0x200 + (i << 1))
        return content

    def calc_frame_coding(self, model):
        """calc_frame_coding
        For coding schemes that use the block coding hardware,\n
        this is a dictionary lookup of each of the supported frame coding methods\n
        Each dictionary entry is a tuple which maps to the following entries:\n
          (starting bit size, coded bit size, coding array)\n

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        FRAME_CODING_LOOKUP = {
              model.vars.frame_coding.var_enum.UART_VAL.value: (8, 10, self._frame_coding_UART),
        }

        self._reg_write(model.vars.FRC_CTRL_UARTMODE, 0)

        if model.vars.frame_coding.value == model.vars.frame_coding.var_enum.NONE.value:
            return
        elif model.vars.frame_coding.value == model.vars.frame_coding.var_enum.UART_NO_VAL.value:
            # Actual hardware bit that supports this coding scheme
            self._reg_write(model.vars.FRC_CTRL_UARTMODE, 1)
            model.vars.frame_coding_array.value = None
        else:
            # Need to use block coding in efr
            frameCodingParams = FRAME_CODING_LOOKUP[model.vars.frame_coding.value]
            self._reg_write(model.vars.FRC_WHITECTRL_SHROUTPUTSEL, frameCodingParams[0] - 1)
            self._reg_write(model.vars.FRC_WHITEPOLY_POLY, 1 << (frameCodingParams[1] - 1))
            model.vars.frame_coding_array.value = frameCodingParams[2]()
        return

    #TODO: Support block coding
    #TODO: Support 15.4g (which I believe uses INTERLEAVEDWHITE1)
    def calc_blockwhitemode(self, model):
        """calc_blockwhitemode

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        # Arbitrate the proper setting for FRC_FECCTRL_BLOCKWHITEMODE
        if (model.vars.ber_force_whitening.value == True):
            self._reg_write(model.vars.FRC_FECCTRL_BLOCKWHITEMODE, 1)
        elif ((model.vars.white_poly.value != model.vars.white_poly.var_enum.NONE) and (model.vars.fec_en.value != model.vars.fec_en.var_enum.NONE)):
            self._reg_write(model.vars.FRC_FECCTRL_BLOCKWHITEMODE, 3)
        elif (model.vars.white_poly.value != model.vars.white_poly.var_enum.NONE) and (model.vars.fec_en.value == model.vars.fec_en.var_enum.NONE):
            if (model.vars.white_poly.value == model.vars.white_poly.var_enum.PN9_BYTE):
                #BYTEWHITE
                self._reg_write(model.vars.FRC_FECCTRL_BLOCKWHITEMODE, 2)
            else:
                self._reg_write(model.vars.FRC_FECCTRL_BLOCKWHITEMODE, 1)
        elif ((model.vars.frame_coding.value != model.vars.frame_coding.var_enum.NONE.value) and
             (model.vars.frame_coding.value != model.vars.frame_coding.var_enum.UART_NO_VAL.value)):
            self._reg_write(model.vars.FRC_FECCTRL_BLOCKWHITEMODE, 7) # Use a lookup table
        else:
            self._reg_write(model.vars.FRC_FECCTRL_BLOCKWHITEMODE, 0)
        return

    def calc_var_length_numbytes(self, model):
        """calc_var_length_numbytes

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        # If the number of variable length bit plus the amount needed to shift exceeds 8
        # then the number of bytes needed to contain the variable length field is two.
        quotient, remainder = divmod((model.vars.var_length_numbits.value + model.vars.var_length_shift.value), 8)
        if (remainder > 0):
            model.vars.var_length_numbytes.value = quotient + 1
        else:
            model.vars.var_length_numbytes.value = quotient

    def calc_var_length_loc(self, model):
        """
        The variable length location must be the last 1 or 2 bytes of the header

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        model.vars.var_length_loc.value = model.vars.header_size.value - model.vars.var_length_numbytes.value
