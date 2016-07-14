
import sys

# For now, limit the pyjlinklib and underlying pyJLinkARM 
# packages to Windows platforms only.
if sys.platform == 'win32':
    try:
        from pyjlinklib.jlink_common import *
        from accessmgr_jlink import *
    except ImportError as err:
        sys.stderr.write("{}: Disabling JLINK support.".format(err))

from accessmgr import *

