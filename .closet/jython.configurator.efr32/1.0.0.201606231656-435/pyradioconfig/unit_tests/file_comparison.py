import difflib
import os
import sys
import shutil
import itertools

def files_diff( calc_file_path, ref_file_path, print_to_console=False):
    # Verify calc file exists
    calc_file_exists = os.path.exists(calc_file_path)
    if not calc_file_exists:
        print(calc_file_path + " does not exist.")
        return True

    # Verify ref file exists
    ref_file_exitst = os.path.exists(ref_file_path)
    if not ref_file_exitst:
        #warnings.warn("Reference file does not exist.  Copying over calculated file.")
        # Helper logic to Copy into reference directory, if missing
        #shutil.copyfile(calc_file_path, ref_file_path)
        return True

    calc_file = open(calc_file_path)
    ref_file = open(ref_file_path)
    diff = difflib.unified_diff(ref_file.readlines(), calc_file.readlines(), fromfile=ref_file_path, tofile=calc_file_path)

    different = False
    # Loop through differences found
    if print_to_console:
        diff_print, diff = itertools.tee(diff) # hack since you can only loop once through a generator object
        for line in diff_print:
            different = True
            sys.stdout.write(line)

    return different, diff