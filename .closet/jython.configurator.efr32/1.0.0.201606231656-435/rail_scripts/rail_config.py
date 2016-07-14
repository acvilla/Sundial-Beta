#!/usr/bin/python
#

import os
import re
import argparse

from host_py_rm_studio_internal import RM_Factory
from _version import __version__

from pyradioconfig.calculator_model_framework.CalcManager import CalcManager
from pyradioconfig.pycalcmodel import *

# /* RADIO actions. */
# #define RADIO_ACTION_WRITE             0x00
# #define RADIO_ACTION_AND               0x01
# #define RADIO_ACTION_XOR               0x02
# #define RADIO_ACTION_OR                0x03
# #define RADIO_ACTION_DELAY             0x04
# #define RADIO_ACTION_BITSET            0x05
# #define RADIO_ACTION_BITCLR            0x06
# #define RADIO_ACTION_WAITFORSET        0x07

# #define RADIO_ACTION_DONE              0xFFFFFFFF

_EXTERN_CONFIG_TMPL = """
extern const uint32_t {configName}[];"""

_CONFIG_LIST_TMPL = """
  {configName},"""

_SINGLE_CONFIG_TMPL = """
const uint32_t {configName}[] = {{
{content}
  0xFFFFFFFFUL,
}};
"""

_RADIO_CONFIG_H_TMPL = """
/***************************************************************************//**
 * @file rail_config.h
 * @brief RAIL Configuration
 * @copyright Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com
 ******************************************************************************/
//=============================================================================
//
//  WARNING: Auto-Generated Radio Config Header  -  DO NOT EDIT
//  Radio Configurator Version: {rc_version}
//  RAIL Adapter Version: {version}
//
//=============================================================================

#ifndef __RAIL_CONFIG_H__
#define __RAIL_CONFIG_H__

#include <stdint.h>
#include "rail_types.h"

{externConfigs}

extern const uint32_t *configList[];
extern const char *configNames[];
extern const uint8_t irCalConfig[];

#define NUM_RAIL_CONFIGS {numConfigs}
{channelConfigs}
extern const RAIL_ChannelConfig_t *channelConfigs[];
extern const RAIL_FrameType_t *frameTypeConfigList[];

{infoOutput}

#endif // __RAIL_CONFIG_H__
"""

_RADIO_CONFIG_C_TMPL = """
/***************************************************************************//**
 * @file rail_config.c
 * @brief RAIL Configuration
 * @copyright Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com
 ******************************************************************************/
//=============================================================================
//
//  WARNING: Auto-Generated Radio Config  -  DO NOT EDIT
//  Radio Configurator Version: {rc_version}
//  RAIL Adapter Version: {version}
//
//=============================================================================
#include "rail_config.h"

{frameCoding}

{configArray}

const uint32_t *configList[] = {{
  {configList}
}};

const char *configNames[] = {{
  {configNames}
}};

{channelConfigs}

const RAIL_ChannelConfig_t *channelConfigs[] = {{
  {addresses}
}};

{frameTypeConfigs}

const RAIL_FrameType_t *frameTypeConfigList[] = {{
  {frameTypeConfigNames}
}};

const uint8_t irCalConfig[] = {{
  {irCalConfig}
}};
"""

_CHANNEL_CONFIG_NAME_TMPL_ = "{}_channelConfig"
_CHANNEL_ENTRY_NAME_TMPL_ = "{}_channels"
_CHANNEL_CONFIG_H_TMPL = """
extern RAIL_ChannelConfigEntry_t {entryName}[];
extern const RAIL_ChannelConfig_t {configName};
"""
_CHANNEL_CONFIG_TMPL = """
RAIL_ChannelConfigEntry_t {entryName}[] = {{
{content}
}};

const RAIL_ChannelConfig_t {configName} = {{
  {entryName},
  {numChannelEntries},
}};
"""
_CHANNEL_ENTRY_TMPL = """
  {{{start}, {stop}, {spacing}, {frequency}}},"""
_CHANNEL_CONFIG_ADDRESS_EACH_TMPL = """
  &{configName},"""

FRAME_TYPE_TMPL= """
static const uint16_t {lenListName}[] = {{ {lengthList} }};
static const uint8_t {validListName}[] = {{ {validList} }};
static const RAIL_FrameType_t {frameTypeConfigName} = {{
  {offset}, {mask}, (uint16_t *)&{lenListName}[0], (uint8_t *)&{validListName}[0], false
}};"""

EXCLUDE_BLOCK_LIST = [
]

WRITE_ONLY_REGISTERS = [
]

class RAILConfig:
  """
  Class takes an input file and parses it into header file content
  """
  # ------------------------------------------------------------------------
  def __init__(self, rc_version = "0.0.0"):
    self.rc_version = rc_version
    setattr(self, "version", __version__)
    self.instanceDict = None

  # -------- Intrinsic --------------------------------------------------------
  def __repr__(self):
    regs = sorted(self.regs)
    out = ''
    for reg in regs:
      out += "0x%.8x: 0x%.8x\n" % (reg[0], reg[1])
    return out

  # -------- Internal ---------------------------------------------------------
  def _regOutput(self, block, register, value):
    # Use the RM_Device object to get register address value pairs
    baseAddrString = "self.rm.{0}.{1}.baseAddress".format(block, register)
    regOffsetString = "self.rm.{0}.{1}.addressOffset".format(block, register)
    regAddr = eval(baseAddrString) + eval(regOffsetString)

    return (regAddr, value)

  def getConfigOutputC(self, model, regs, config):
    _REG_BASES = {
      0x40080000: 0,
      0x21000000: 1,
    }
    _RADIO_ACTION_WRITE_TMPL = """  0x{0:08X}UL, 0x{1:08X}UL,\n"""

    # Create the properly formatted output array from the register pairs
    content = ""
    for reg in regs:
      reg_base = _REG_BASES[int(reg[0]) & 0xFFFF0000]
      reg_offset = int(reg[0]) & 0x0000FFFF
      write_length = 0x00010000
      radio_action = 0 #RADIO_ACTION_WRITE
      content += _RADIO_ACTION_WRITE_TMPL.format(((radio_action << 28) | (reg_base << 24) | write_length | reg_offset), int(reg[1]))

    if model.vars.frame_coding_array.value != None:
      # Write the address of the block decoding table to BLOCKRAMADDR
      # when BLOCKWHITEMODE == BLOCKLOOKUP
      content += "  0x00010038UL, (uint32_t) &frameCodingTable[0],\n"

    args = {'content': content, 'configName': config}
    return _SINGLE_CONFIG_TMPL.format(**args)

  def _getRegNameFromFieldName(self, fieldname):
      (block, reg, field) = fieldname.split('.')
      return block + '.' + reg

  # Takes a model instance and writes it to a rm object
  # register_dict keeps track of written registers
  def _writeModelToRmDevice(self, radio_model, rm, register_dict):
    # write the registers to the rm         fixme:  This should use the profile instead
    for output in radio_model.profile.get_outputs([ModelOutputType.SVD_REG_FIELD, ModelOutputType.SEQ_REG_FIELD]):
        fieldname = output.var.svd_mapping
        registerName = self._getRegNameFromFieldName(fieldname)
        if registerName in WRITE_ONLY_REGISTERS:
          register_dict[registerName] = str(output.var.value)
        else:
          register_dict[registerName] = ''        # Add this register to the register dictionary
        if (output.var.value != None):
          register_write_exec_string = "rm.{0}.io={1}".format(fieldname, str(output.var.value))
          #print register_write_exec_string
          exec(register_write_exec_string)
        else:
          print ("Field {} does not have a valid value".format(fieldname))

    # @TODO: fixme!
    # Delete this one from the output.  We weren't outputting it before.
    # Shouldn't be a big deal that we missed it.  Just the channel number.
    register_dict.pop('SYNTH.CHCTRL')

  # For a particular PHY get the frame config
  def _generateFrameTypeStructures(self, configName, model):
    if ((model.vars.frame_type_lengths.value != None) and
        (len(model.vars.frame_type_lengths.value) > 0)):
      lengthListStr = ""
      validListStr = ""
      for length in (model.vars.frame_type_lengths.value):
        lengthListStr += "{}, ".format(str(length))
      for valid in (model.vars.frame_type_valid.value):
        validListStr += "{}, ".format("1" if (valid == True) else "0")

      frameTypeDict = {
        'frameTypeConfigName': "{}FrameTypeConfig".format(configName),
        'lenListName': "{}LenList".format(configName),
        'validListName': "{}ValidList".format(configName),
        'lengthList': lengthListStr,
        'validList': validListStr,
        'offset': model.vars.frame_type_loc.value,
        'mask': model.vars.frame_type_mask.value,
      }

      self.frameTypeLengthConfigs += "&{},\n".format(frameTypeDict['frameTypeConfigName'])
      self.frameTypeC += FRAME_TYPE_TMPL.format(**frameTypeDict)
    else:
      self.frameTypeLengthConfigs += "NULL,\n"

    return

  def _generateFrameCoding(self, codingArray, model):
    if codingArray != None:
      frameCodingStr = "uint16_t frameCodingTable[] = {\n"

      # Split list into 16 value chunks
      codingSplitList = [codingArray[i:i+16] for i in range (0, len(codingArray), 16)]
      for codingSubList in codingSplitList:
        frameCodingStr += ", ".join(map(str, codingSubList))
        frameCodingStr += ",\n"

      frameCodingStr += "};"
    else:
      frameCodingStr = ""
    return frameCodingStr

  def _generateIrCalStructure(self, model):
    codeStr = "16" # the number of bytes being passed in this structure (excluding this byte)
    codeStr += ", " + str(model.vars.ircal_auxndiv.value)
    codeStr += ", " + str(model.vars.ircal_auxlodiv.value)
    codeStr += ", " + str(model.vars.ircal_rampval.value)
    codeStr += ", " + str(model.vars.ircal_rxamppll.value)
    codeStr += ", " + str(model.vars.ircal_rxamppa.value)
    codeStr += ", " + str(int(model.vars.ircal_manufconfigvalid.value))
    codeStr += ", " + str(int(model.vars.ircal_pllconfigvalid.value))
    codeStr += ", " + str(int(model.vars.ircal_paconfigvalid.value))
    codeStr += ", " + str(int(model.vars.ircal_bestconfig.value)) # enum to int
    codeStr += ", " + str(int(model.vars.ircal_useswrssiaveraging.value))
    codeStr += ", " + str(model.vars.ircal_numrssitoavg.value)
    codeStr += ", " + str(model.vars.ircal_throwawaybeforerssi.value)
    codeStr += ", " + str(int(model.vars.ircal_delayusbeforerssi.value % 256)) # lower byte of uint16_t
    codeStr += ", " + str(int(model.vars.ircal_delayusbeforerssi.value / 256)) # upper byte of uint16_t
    codeStr += ", " + str(int(model.vars.ircal_delayusbetweenswrssi.value % 256)) # lower byte of uint16_t
    codeStr += ", " + str(int(model.vars.ircal_delayusbetweenswrssi.value / 256)) # upper byte of uint16_t
    return codeStr
    
  def _generateChannelStructures(self, configName, model):
    #Get the channel scheme for each PHY
    channelConfigInfo = [(0, 20, model.vars.channel_spacing.value, model.vars.base_frequency.value)]

    # Build up the Channel Entries Content
    channelEntryContent= ""
    numChannelEntries = 0
    for channelEntry in channelConfigInfo:
      channelInfoArgs = {'start':channelEntry[0], 'stop':channelEntry[1],
                         'spacing':channelEntry[2], 'frequency':channelEntry[3]}
      channelEntryContent += _CHANNEL_ENTRY_TMPL.format(**channelInfoArgs)
      numChannelEntries += 1

    #Generate the externs
    args = {
      'entryName': _CHANNEL_ENTRY_NAME_TMPL_.format(configName),
      'configName': _CHANNEL_CONFIG_NAME_TMPL_.format(configName),
    }
    self.channelConfigsH += _CHANNEL_CONFIG_H_TMPL.format(**args)

    #Generate the C structures
    args = {
      'configName': _CHANNEL_CONFIG_NAME_TMPL_.format(configName),
      'entryName': _CHANNEL_ENTRY_NAME_TMPL_.format(configName),
      'content': channelEntryContent,
      'numChannelEntries': numChannelEntries,
    }
    self.channelConfigs += _CHANNEL_CONFIG_TMPL.format(**args)

    #Add the pointer to the ChannelConfig to the overall list
    args = {
      'configName': _CHANNEL_CONFIG_NAME_TMPL_.format(configName),
    }
    self.channelConfigAddresses += _CHANNEL_CONFIG_ADDRESS_EACH_TMPL.format(**args)

  def _convertRmToRegisters(self, rm, register_dict):
    regs = []
    for registerName in register_dict.keys():
      (block, register) = registerName.split(".")
      if block not in EXCLUDE_BLOCK_LIST:
        if register_dict[registerName] != "":
          # This is a workaround for write only registers
          regs.append(self._regOutput(block, register, register_dict[registerName]))
        else:
          value = eval(".".join(["rm", block, register, "io"]))
          regs.append(self._regOutput(block, register, value))
    return regs

  def _getInfoOutput(self, model):
    # Take number and suffix and create string
    def floatToStringWithinMax(floatVal, suffixStr):
      charMax = 8
      floatCharMax = charMax - len(suffixStr)

      floatValStr = (str(floatVal))[0:floatCharMax]
      if (floatValStr[-1:] == "."):
        floatValStr = floatValStr[:-1]

      return "{}{}".format(floatValStr, suffixStr)

    infoOutputStr = ""

    # https://jira.silabs.com/browse/RAIL-185
    # Output base frequency as a #define
    if (model.vars.base_frequency.value is not None):
      infoOutputStr += "#define RADIO_CONFIG_BASE_FREQUENCY {}UL\n".format(model.vars.base_frequency.value)

    ###
    # https://jira.silabs.com/browse/RAIL-192
    ###
    # XTAL Frequency
    if (model.vars.xtal_frequency.value is not None):
      infoOutputStr += "#define RADIO_CONFIG_XTAL_FREQUENCY {}UL\n".format(model.vars.xtal_frequency.value)

    #Bitrate
    if (model.vars.bitrate.value is not None):
      bitrate = float(model.vars.bitrate.value)
      if (bitrate >= 1000000):
        bitrateStr = floatToStringWithinMax(bitrate/1000000, "Mbps")
      elif (bitrate >= 1000):
        bitrateStr = floatToStringWithinMax(bitrate/1000, "kbps")
      else:
        bitrateStr = "{}bps".format(bitrate)
      infoOutputStr += "#define RADIO_CONFIG_BITRATE \"{}\"\n".format(bitrateStr)

    #Modulation Type
    if (model.vars.modulation_type.value is not None):
      modType = model.vars.modulation_type.value.name
      # Strip ModModeEnum. from modulation type
      modType = re.sub("ModModeEnum\.", '', modType)
      infoOutputStr += "#define RADIO_CONFIG_MODULATION_TYPE \"{}\"\n".format(modType)

    #deviation
    if (model.vars.deviation.value is not None):
      deviation = float(model.vars.deviation.value)
      if (deviation >= 1000000):
        deviationStr = floatToStringWithinMax(deviation/1000000, "MHz")
      elif (deviation >= 1000):
        deviationStr = floatToStringWithinMax(deviation/1000, "kHz")
      else:
        deviationStr = "{}Hz".format(deviation)
      infoOutputStr += "#define RADIO_CONFIG_DEVIATION \"{}\"\n".format(deviationStr)

    return infoOutputStr

  # -------- External ---------------------------------------------------------
  def setInstanceDict(self, instanceDict):
    self.instanceDict = instanceDict

  def parseConfigs(self, customer):
    # Empty output strings
    self.frameCoding = ""
    self.irCalSettings = ""
    self.configArray= ""
    self.configList = ""
    self.configNames = ""
    self.numConfigs = 0
    self.externConfigs = ""
    self.channelConfigs = ""
    self.channelConfigsH = ""
    self.channelConfigAddresses = ""
    self.frameTypeLengthConfigs = ""
    self.frameTypeC = ""
    self.infoOutput = ""

    #Check if we have an instanceDict
    if self.instanceDict == None:
      print "No instanceDict configured. Please call the setInstanceDict method."

    # Parsing all config files for a customer
    for phy in sorted(self.instanceDict.keys()):
      PART_FAMILY_RM_FACTORY = {
          'dumbo': RM_Factory("DUMBO"),
          'jumbo': RM_Factory("JUMBO"),
      }
      # Remove "PHY_"
      configName = phy[4:]
      model = self.instanceDict[phy]
      part_family = model._part_family

      # Add instance name to configList
      self.numConfigs += 1
      self.configList += _CONFIG_LIST_TMPL.format(configName=configName)
      self.configNames += _CONFIG_LIST_TMPL.format(configName='"%s"' %configName)
      self.externConfigs += _EXTERN_CONFIG_TMPL.format(configName = configName)

      # Create a proper rm object depending on part_family
      self.rm = PART_FAMILY_RM_FACTORY[part_family]()
      #Create a register dictionary
      registerDict = {}

      # Write model instance to RM device
      # rm and registerDict are both modified here
      self._writeModelToRmDevice(model, self.rm, registerDict)

      #Handle Frame Type Configurations
      self._generateFrameTypeStructures(configName, model)

      self.frameCoding = self._generateFrameCoding(model.vars.frame_coding_array.value, model)

      #Handle IR Cal Settings
      self.irCalSettings = self._generateIrCalStructure(model)

      #Handle Channel Lists
      self._generateChannelStructures(configName, model)

      regs = self._convertRmToRegisters(self.rm, registerDict)

      self.infoOutput = self._getInfoOutput(model)

      # Check for duplicates since we won't know what to do with them
      regs = sorted(regs)
      prevAddr = None
      prevValue = None
      for reg in regs:
        if prevAddr != None and reg[0] == prevAddr:
          if prevValue != reg[1]:
            # raise Exception("Duplicate non-identical set of register 0x%.8x!" % reg[0])
            print "Error: Conflicting definition for register 0x%.8x (%s)" % (reg[0], filePath)
          else:
            print "Warning: Duplicate definition of register 0x%.8x (%s)" % (reg[0], filePath)
        prevAddr = reg[0]
        prevValue = reg[1]

      self.configArray+= self.getConfigOutputC(model, regs, configName)

  def getRadioConfigC(self):
    #populate rail_config.c template
    #must have called parseConfigs first
    args = {
      'frameCoding': self.frameCoding,
      'irCalConfig': self.irCalSettings,
      'configArray': self.configArray,
      'configList': self.configList,
      'configNames': self.configNames,
      'channelConfigs': self.channelConfigs,
      'addresses': self.channelConfigAddresses,
      'frameTypeConfigs': self.frameTypeC,
      'frameTypeConfigNames': self.frameTypeLengthConfigs,
      'rc_version': self.rc_version,
      'version': self.version,
    }
    return _RADIO_CONFIG_C_TMPL.format(**args)

  def getRadioConfigHeaderC(self):
    #populate rail_config.h template
    #must have called parseConfigs first
    args = {
      'externConfigs': self.externConfigs,
      'numConfigs': self.numConfigs,
      'channelConfigs': self.channelConfigsH,
      'infoOutput': self.infoOutput,
      'rc_version': self.rc_version,
      'version': self.version,
    }
    return _RADIO_CONFIG_H_TMPL.format(**args)

def getParserArgs():
  """
  Build argparse parser and return arguments from sys.argv.
  """
  parser = argparse.ArgumentParser(description="Parse radio configurator output into header file.")
  parser.add_argument('-o', '--output_dir', type=str, default=None, help="The output dir.")
  parser.add_argument('-p', '--phy_name', type=str, default="PHY_RAIL", help="Build configuration for a specific PHY")
  args = parser.parse_args()
  return args

def main():
  args = getParserArgs()
  basePath = os.path.abspath(os.getcwd())

  # Check output information
  outDir = os.path.abspath(args.output_dir)

  radio_configurator = CalcManager("dumbo", "A0")

  phy_name = args.phy_name
  if phy_name not in radio_configurator.getPhyNames():
    print ("Phy Name {} is not a valid phy. Using PHY_RAIL.".format(phy_name))
    phy_name = "PHY_RAIL"

  instanceDict = {}
  instanceDict["PHY_generated"] = radio_configurator.calculate_phy(phy_name)
  railConfig = RAILConfig(instanceDict)
  railConfig.parseConfigs("PHY_generated")

  outPathH = os.path.join(outDir, 'rail_config.h')
  outPathC = os.path.join(outDir, 'rail_config.c')
  outputDir = os.path.dirname(outPathH)

  try:
    os.makedirs(outputDir)
  except OSError:
    if not os.path.isdir(outputDir):
      raise

  with open(outPathC, 'w') as fc:
    print ("Creating '{}'...".format(outPathC))
    fc.write(railConfig.getRadioConfigC())
    fc.close()
  with open(outPathH, 'w') as f:
    print("Creating '{}'...".format(outPathH))
    f.write(railConfig.getRadioConfigHeaderC())
    f.close()

  # Script Finished
  return 0

# Call main if necessary
if __name__ == '__main__':
  main()
