from pyradioconfig.calculator_model_framework.Utils.FileUtilities import FileUtilities
from pyradioconfig.calculator_model_framework.CalcManager import CalcManager
from pyradioconfig.pycalcmodel import *

import os.path
from pyrmsvd import *

from rm_io import *

# Hack to force part family and revision
part_family = "dumbo"
part_rev = "A0"
radio_configurator = CalcManager(part_family, part_rev)



# Populate the profile overrides for registers with values 
# read from an rm object
#                                
def read_rm_into_profile(rm, model):

    for output in model.profile.get_outputs([ModelOutputType.SVD_REG_FIELD, ModelOutputType.SEQ_REG_FIELD]):
        #print "Reading %s" % output.var.svd_mapping
        register_read_value = rm_read_field(rm, output.var.svd_mapping)
        output.override = output.var.var_type(register_read_value)


#
# This reads all fields listed in the profile output, forces them as output overrides,
# then runs the calculator to see what the _actual values are.  It can also be used
# to generate an output file that can be compared against something generated by 
# the calculator. 
#
def extract_model_from_rm(rm, xtal_frequency=None):

    if xtal_frequency==None:
        xtal_frequency = 38400000
        print "No crystal frequency supplied, assuming 38.4MHz"

    # Create a model object and populate all variables
    # in it that are registers
    model = radio_configurator.create_modem_model_instance(profile_name="Base")
    read_rm_into_profile(rm, model)

    # For now, just force the crystal frequency to 38.4MHz
    model.profile.inputs.xtal_frequency_hz.var_value = xtal_frequency
    
    # Run the calculator to calculate the "actual" values
    radio_configurator.calculate(model)

    # Running the calculator calculates some outputs that are fixed
    # constants that don't depend on any inputs.  This means that even
    # though we started with minimal inputs, we now have some outputs 
    # that are set.  These outputs most likely match the values that were
    # forced.  So, if any calculated output matches the forced output
    # value, remove the forced value.  No need to pointlessly override
    # an output.
    for output in model.profile.get_outputs([ModelOutputType.SVD_REG_FIELD, ModelOutputType.SEQ_REG_FIELD]):
        if output.override == output.var._value_calc:
            output.override = None
    
    return model

