"""
Created on November 4, 2015

@author: aldangtr
"""

import os
import sys
import json
import argparse

# Add path to the other pieces
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "src")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "lib", "host_py_radio_config", "Package")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "lib")))

from efr32config import Efr32Configurator

class ConfiguratorFrontEnd:
  """
  Class that uses the Efr32Configurator like the GUI would
  Useful for internal build systems
  """

  # ------------------------------------------------------------------------
  def __init__(self):
    self.configurator = Efr32Configurator()
    # The configuration functions are responsible for parsing the file
    # and returning the result of self.configurator.configure()
    self.configFunctions = {
        '.json': self._config_json,
    }

  # -------- External ---------------------------------------------------------
  def generateConfig(self, config_file, output_dir, verbose):
    print ("\n")
    # Validate configuration file
    config_filename = os.path.basename(config_file)
    config_filename, config_fileext = os.path.splitext(config_filename)
    if config_fileext not in self.configFunctions:
      print ("Invalid configuration file {}.".format(config_file))
      print ("Configuration file extension {} is not supported.".format(config_fileext))
      return 1

    print ("Using config file {}".format(config_file))
    config_output = self.configFunctions[config_fileext](config_file)

    if config_output['result_code'] != 0:
      print "Error {0} during configuration: {1}".format(config_output['result_code'], config_output['error_message'])
      return 2

    # Get the colon delimited file names
    output_files = str.split(config_output["file_names"], ":")

    # Output all files with the contents
    for outFile in output_files:
      with open(os.path.join(output_dir, outFile), 'w') as fp:
        print ("Creating output file: {}".format(fp.name))
        fp.write(config_output[outFile])

    if verbose:
      with open(os.path.join(output_dir, "{}_output.txt".format(config_filename)), 'w') as fp:
        print ("Creating output file: {}".format(fp.name))
        config_output_keys = config_output.keys()
        # Remove above keys
        config_output_keys.remove('result_code')
        config_output_keys.remove('file_names')
        for outFile in output_files:
          config_output_keys.remove(outFile)
        config_output_keys = sorted(config_output_keys)
        for key in config_output_keys:
          fp.write("{0} = {1}\n".format(key, config_output[key]))

    return 0

  # -------- Internal ---------------------------------------------------------
  def _config_json(self, jsonfile):
    #Read configuration data from json file
    with open(jsonfile, 'r') as f:
      self.config_data = json.loads(f.read())

    self.configurator.setup(**self.config_data["configurator_settings"])

    if "phy_name" in self.config_data:
      kwargs = {"phy_name":self.config_data["phy_name"]}
      kwargs["optional_inputs"] = self.config_data.get("optional_inputs", dict())
      return self.configurator.configure(**kwargs)
    else:
      self.configInputs = self.config_data["config_inputs"]

      # Load the inputs
      for inputKey in self.configInputs:
        # print ("Key: {}".format(inputKey))
        # print ("Value: {}".format(self.configInputs[inputKey]))
        self.configurator.set_option(inputKey, self.configInputs[inputKey])

      return self.configurator.configure()

def getParserArgs():
  parser = argparse.ArgumentParser(description="Turn configurator inputs into rail outputs")
  parser.add_argument('-c', '--config_file', type=str, default=None, help="Configuration File. Currently support .json.")
  parser.add_argument('-o', '--output_dir', type=str, default=None, help="Specify the output directory.")
  parser.add_argument('-v', '--verbose', action="store_true", help="Specify the output directory.")
  args = parser.parse_args()
  return args
  return

def main():
  args = getParserArgs()

  config_file = os.path.abspath(args.config_file)
  if not os.path.isfile(config_file):
    print ("File {} does not exist".format(config_file))
    return 1

  output_dir = os.path.abspath(args.output_dir)
  try:
    os.makedirs(output_dir)
  except OSError:
    if not os.path.isdir(output_dir):
      raise

  configurator = ConfiguratorFrontEnd()
  return configurator.generateConfig(config_file, output_dir, args.verbose)

if __name__ == '__main__':
  main()
