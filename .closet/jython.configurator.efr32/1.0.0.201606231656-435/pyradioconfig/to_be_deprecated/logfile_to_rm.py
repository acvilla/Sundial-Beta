from pyradioconfig.calculator_model_framework.Utils.FileUtilities import FileUtilities
from pyradioconfig.calculator_model_framework.CalcManager import CalcManager
from pyradioconfig.calculator_model_framework.model_serializers.human_readable import Human_Readable
from pyradioconfig.pycalcmodel import *

import re

from rm_io import *

from extract import *


# Hack to force part family and revision
part_family = "dumbo"
part_rev = "A0"
radio_configurator = CalcManager(part_family, part_rev)


def logfile_to_rm(rm, filename):

    file = open(filename, 'r')
    lines = file.readlines()
    #print lines
    file.close()

    regex = re.compile("(0x\w+)\t(0x\w+)")
    readonly_list = []
    for line in lines:
        match = regex.match(line)

        if match:
            addr = match.group(1)
            value = match.group(2)

            block, register = EFR32XG1XFULL_REG_ADDR_NAME_MAP[int(addr, 16)].split('_')
            svd_regname = block + '.' + register
            
            print "%s = %s  addr = %s" % (svd_regname, value, addr)
            
            if register == 'IF':
                continue
            
            if 'STATUS' in register:
                continue

            if 'WAITMASK' in register:
                continue
                
            if 'WAITSNSH' in register:
                continue
                
            if 'STIMER' in register:
                continue

            if 'FREQOFFEST' in register:
                continue

            if 'AFCADJ' in register:
                continue

            if 'DCESTI' in register:
                continue

            if 'RSSI' in register:
                continue

            if 'CAPCALCYCLECNT' in register:
                continue

            rm_write_field(rm, svd_regname, value)

            
#
# This parses a logfile from Alex and ends up printing the matching .cfg file for it.
#
def test_logfile():

    rm = build_rm_object()

    logfile_to_rm(rm, "m:/register_contents_2015-10-01_04-19-28.txt")

    model = extract_model_from_rm(rm)
    
    # Output it to a file
    Human_Readable.print_modem_model_values_v2("m:/dump.cfg", "dump", model)
    
    #return rm
    return model
    
