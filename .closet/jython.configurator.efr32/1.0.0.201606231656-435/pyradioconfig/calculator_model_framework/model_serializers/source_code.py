class Source_Code(object):

    #
    # Create Python source code from a modem_model object.  Running the Python code
    # will initialize the model to the same state it was in memory.  This is used
    # to create templates for phy configuration source code.
    #
    @staticmethod
    def print_modem_model_forced_as_source(outputfilename, phy_name, modem_model):

        output_lines = list()

        line = 'def %s(modem_model): ' % phy_name
        #print line
        output_lines.append(line)

        for var in modem_model.vars:
            if var.svd_mapping:
                if var._value_forced is not None:       # gdc:  What's the right way to check this?
                    line = "    modem_model.vars.%s.value_forced = %r" % (var.name, var.value_forced)
                    #print line
                    output_lines.append(line)
            else:
                if var._value_forced is not None:
                    line = "    modem_model.vars.%s.value_forced = %r" % (var.name, var.value_forced)
                    #print line
                    output_lines.append(line)


        # write the lines to a file
        outputfile = open(outputfilename, 'w')
        for line in output_lines:
            outputfile.write('%s\n' % line)
        outputfile.write('\n')
        outputfile.close()