import sys

class CFGFileDiffManager(object):
    KeyValueDiffs = dict()

    @staticmethod
    def clear_diffs():
        CFGFileDiffManager.KeyValueDiffs = dict()

    @staticmethod
    def process_diff(phy_name, diff):
        counter = 0
        for line in diff:
            counter += 1
            if (counter > 3):
                if line.startswith('+') or line.startswith('-'):
                    if line.startswith('-'):
                        current = True
                    else:
                        current = False
                    line = line[1:]
                    line_split = line.split("=")
                    if len(line_split) > 1:
                        key_name = line_split[0]
                        value = line_split[1]

                        if key_name not in CFGFileDiffManager.KeyValueDiffs:
                            CFGFileDiffManager.KeyValueDiffs[key_name] = KeyValueDiffs()

                        key_value_diff = CFGFileDiffManager.KeyValueDiffs[key_name]
                        if current:
                            key_value_diff.current_value = value.strip()
                        else:
                            key_value_diff.previous_value = value.strip()
                            key_value_diff.phys += phy_name + ", "


    @staticmethod
    def print_diff():
        if len(CFGFileDiffManager.KeyValueDiffs) > 0:
            print bcolors.FAIL + "Found the following .CFG diffs:"
            for key, diff in CFGFileDiffManager.KeyValueDiffs.iteritems():
                print bcolors.FAIL + "key = {0}".format(key) + bcolors.ENDC
                print bcolors.FAIL + "\tprevious value = {0}".format(diff.previous_value) + bcolors.ENDC
                print bcolors.FAIL + "\tcurrent value = {0}".format(diff.current_value) + bcolors.ENDC
                print bcolors.FAIL + "\tphys = {0}".format(diff.phys) + bcolors.ENDC


class KeyValueDiffs(object):
    current_value = None
    previous_value = None
    phys = ''

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'