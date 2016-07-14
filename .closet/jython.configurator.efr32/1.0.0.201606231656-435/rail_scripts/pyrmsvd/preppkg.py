
"""
This file contains the code to create the setup.py and PKG-INFO used to 
create an egg.  Parse out the tag and create a version string, which is 
prepended to template files to create the final files for dist-utils.

This file also contains the code to create the version.py file used in 
the package for the binding version and library versions.
"""

import os
import re
import sys
from taginfo import *


# ============================================================================
#  CONSTANTS
# ============================================================================


VERSION_PY_TEMPLATE = """

# WARNING: This file is auto-generated, do not edit
__version__ = '%s'


"""

# ============================================================================
#  CLASSES 
# ============================================================================


# ============================================================================
# FUNCTIONS
# ============================================================================


# ----------------------------------------------------------------------------
def CreateVersionPyFile(pkgPath, verStrComma):
    """
    Create _version.py with PKG_VER string.
    """
    outPath = pkgPath + os.sep + '_version.py'
    outFH = open(outPath, 'w')
    outFH.write(VERSION_PY_TEMPLATE % (verStrComma))
    outFH.close()

# ----------------------------------------------------------------------------
def GenerateWorkingFile(pkgPath, templateFn, verStr):
    """
    Verify template exists in the given path and prepend version string
    to generate working file.
    """
    templatePath = pkgPath + os.sep + templateFn 
    if templateFn[-3:] != '.in':
        sys.stderr.write("\nERROR: Missing '.in' suffix '%s'\n" % templatePath)
        sys.exit(2)
    if not os.path.exists(templatePath):
        sys.stderr.write("\nERROR: Invalid file '%s'\n" % templatePath)
        sys.exit(2)
    inFH = open(templatePath, 'r')
    # strip off the '.in' suffix for output file
    outFH = open(templatePath[:-3], 'w')
    outFH.write(verStr)
    outFH.write(inFH.read())
    outFH.close()
    inFH.close()


# ----------------------------------------------------------------------------
def ShowUsage():
    """
    Display usage help.
    """
    sys.stderr.write(
        "\nUsage:\n    %s <package path> <module path>\n" % (
        os.path.basename(sys.argv[0])))

# ----------------------------------------------------------------------------
def Main():
    if len(sys.argv) < 3:
        ShowUsage()
        sys.exit(1)

    pkgPath = sys.argv[1]
    modPath = sys.argv[2]
    tag = TagInfo(3)
    GenerateWorkingFile(pkgPath, 'setup.py.in', tag.getSetupPyVerStr()) 
    GenerateWorkingFile(pkgPath, 'PKG-INFO.in', tag.getPkgInfoVerStr()) 
    CreateVersionPyFile(modPath, tag.getDigitsDotStr())


# ============================================================================
# MAIN
# ============================================================================
if __name__ == '__main__':
    Main()

