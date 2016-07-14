
class ImportISCFiles(object):

    keys_ignored = ['phy', 'profile']
    phy = None
    profile = None

    def parse_file(self, file_path):

        found_start = False
        found_end = False

        inputs = dict()

        # Loop through file line by line
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if len(line) > 0:
                    if line == '{setupId:efr32RadioConfig':
                        # found start of input section
                        found_start = True
                    elif line == '}' and found_start:
                        # found end of input section
                        found_end = True
                        break
                    elif line.startswith('#') and found_start:
                        # ignore commented out line
                        print "Ingoring line: " + line
                    else:
                        # We found start and are in input section
                        if found_start and not found_end:
                            if '=' in line:
                                pair = line.split("=")
                                key = pair[0].lower()
                                value_pair = pair[1]
                                value_pair = value_pair.replace('serializableObject:', '')
                                if ':' in value_pair:
                                    value_pair = value_pair.split(':')
                                    value_type = value_pair[0]
                                    value = value_pair[-1] # get last value in array

                                    # Check if we need to ignore input
                                    if key not in self.keys_ignored:
                                        # Add to key/value dictionary
                                        inputs[key] = value
                                        print "phy.profile_inputs." + key + ".value = " + value
                                    else:
                                        # Known invalid inputs are caught here
                                        if hasattr(self, key):
                                            # Store to member variable
                                            print "self." + key + " = " + value
                                            setattr(self, key, value)
                                else:
                                    print "Invalid value " + value_pair
                            else:
                                print "Invalid line: " + line
        # Return key/value dictionary
        return inputs


