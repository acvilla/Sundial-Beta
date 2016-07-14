from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pyradioconfig.pycalcmodel.core.output import ModelVariableEmptyValue
from pyradioconfig.pycalcmodel.core.output import ModelOutputType
import warnings

class Human_Readable(object):

    #
    # Print a modem_model object to a humanly readable file.
    #
    @staticmethod
    def print_modem_model_values(outputfilename, phy_name, modem_model):

        warnings.warn("deprecated", DeprecationWarning)
        output_lines = list()

        line = 'info.config_name = ' + phy_name
        #print line
        output_lines.append(line)

        for var in modem_model.vars:
            if var.svd_mapping:
                # For registers,
                #       output the value as        "rm.<svd_mapping> = <value>"
                #       output the forced value as "forced.<svd_mapping> = <value_forced>"
                register_name = var.svd_mapping
                #print "var.name = %s" % var.name

                if var._value_forced is not None:       # gdc:  What's the right way to check this?
                    line = "forced.%s = %s" % (register_name, var.value_forced)                 # gdc:  Should print "forced"
                    output_lines.append(line)
                    #print line
                    line = "rm.%s = %s" % (register_name, var.value_forced)
                    output_lines.append(line)
                    #print line
                elif var._value_calc is not None:       # gdc:  What's the right way to check this?
                    line = "rm.%s = %s" % (register_name, var.value)
                    output_lines.append(line)
                    #print line
            else:
                # for things that aren't registers,
                #       output the actual value as    "actual.<name> = <value>"
                #       output the value as           "calculated.<name> = <value>"
                #       output the forced value as    "config.<name> = <value_forced>
                if var._value_calc is not None:
                    if '_actual' in var.name:
                        line = "actual.%s = %s" % (var.name, var.value)
                        #print line
                        output_lines.append(line)
                    else:
                        line = "calculated.%s = %s" % (var.name, var.value)
                        #print line
                        output_lines.append(line)

                if var._value_forced is not None:
                    line = "config.%s = %s" % (var.name, var.value_forced)
                    #print line
                    output_lines.append(line)

        # Sort the lines and write them to a file
        outputfile = open(outputfilename, 'wb')
        for line in sorted(output_lines):
            outputfile.write('%s\n' % line)
        #outputfile.write('\n')
        outputfile.close()


    #
    # Print a modem_model object to a humanly readable file.
    #
    @staticmethod
    def print_modem_model_values_v2(outputfilename, phy_name, modem_model):

        output_lines = list()

        line = 'info.config_name = ' + str(phy_name)
        #print line
        output_lines.append(line)

        profile = modem_model.profile # should only be one profile!

        for input in profile.inputs:
            if input.var_value is not None:
                line = "config.%s = %s" % (input.var_name, input.var_value)
                output_lines.append(line)

        for force in profile.forces:
            if force.value is not None:
                line = "forced.%s = %s" % (force.var_name, force.value)
                output_lines.append(line)

        for output in profile.outputs:
            if output.override is not None:
                if (output.output_type is ModelOutputType.SVD_REG_FIELD) or (output.output_type is ModelOutputType.SEQ_REG_FIELD):
                    var = getattr(modem_model.vars, output.var_name)
                    line = "forced.%s = %s" % (var.svd_mapping, output.override)
                else:
                    line = "forced.%s = %s" % (output.var_name, output.override)
                output_lines.append(line)

            if output.var_value is not None:
                if (output.output_type is ModelOutputType.SVD_REG_FIELD) or (output.output_type is ModelOutputType.SEQ_REG_FIELD):
                    var = getattr(modem_model.vars, output.var_name)
                    line = "rm.%s = %s" % (var.svd_mapping, output.var_value)
                else:
                    line = "rm.%s = %s" % (output.var_name, output.var_value)
                output_lines.append(line)

        for var in modem_model.vars:
            if var.svd_mapping is None:
                try:
                    if var.value is not None:
                        if not (hasattr(profile.inputs, var.name) or \
                           hasattr(profile.forces, var.name) or \
                           hasattr(profile.outputs, var.name)):
                            if var.name.endswith(ICalculator.actual_suffix):
                                line = "actual.%s = %s" % (var.name, var.value)
                            else:
                                line = "calculated.%s = %s" % (var.name, var.value)
                            output_lines.append(line)
                except ModelVariableEmptyValue:
                    pass

        # Sort the lines and write them to a file
        outputfile = open(outputfilename, 'wb')
        for line in sorted(output_lines):
            outputfile.write('%s\n' % line)
        outputfile.close()

    #
    # Print a modem_model object to a humanly readable file.
    #
    @staticmethod
    def compare_forced_to_calculated(modem_model):
        output_lines = list()
        for var in modem_model.vars:
            if var._value_forced is not None:       # gdc:  What's the right way to check this?
                if var._value_calc is not None:
                    if var._value_calc == var._value_forced:
                        line = "        %s = %d:  Calculated value matches forced value." % (var.name, var.value_forced)
                        print line
                        output_lines.append(line)

        return output_lines