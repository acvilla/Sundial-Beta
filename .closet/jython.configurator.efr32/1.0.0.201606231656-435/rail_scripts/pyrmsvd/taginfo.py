
"""
This module provides an easy way to obtain the version numbers from a 
git tag.
"""

__all__ = [ 'TagInfo' ]

import re
import subprocess
import sys

# ============================================================================
#  CONSTANTS 
# ============================================================================


# ============================================================================
#  CLASSES
# ============================================================================

class TagInfo:
    """
    Process 'rel_x_x', 'rel_x_x_x' or 'rel_x_x_x_x' tag string into 
    group of digits with method to get '.' joined string or custom
    strings.

    Generic:
        major.minor

    Python:
        major.minor.micro(bug fix revision)

    Windows Applciations:
        major.minor[.build[.revision]]
    """
    # ------------------------------------------------------------------------
    def __init__(self, verDigitLen):
        """
        Ensure on detached tag head, which is acheived with a "git checkout
        tags/<tag_name>" operation. Parse out tag string and create digits 
        tuple.
        """
        try:
            self.rawStr = subprocess.check_output(["git", "branch"])
        except subprocess.CalledProcessError:
            sys.stderr.write("ERROR: git operation was not successful, using Development status!\n")
            self.rawStr = 'Development'
        regex = re.compile("^\* \(detached from (.+)\)")
        r = re.search(regex, self.rawStr)
        self.digits = []
        if r and len(r.groups()) == 1:
            self.tagStr = r.group(1)
            # slice up tag string in group(1)
            digitStr = self.tagStr.split('_')[-verDigitLen:]
            if len(digitStr) != verDigitLen:
                self.digits = tuple([0] * verDigitLen)
            else:    
                for digit in digitStr:
                    self.digits.append(int(digit))
                self.digits = tuple(self.digits)
        else:
            self.tagStr = "Development"
            self.digits = tuple([0] * verDigitLen)
    # ------------------------------------------------------------------------
    def getTagStr(self):
        """
        Return raw release_x_x[_x[_x]] string from the tags/ folder.
        """
        return self.tagStr
    # ------------------------------------------------------------------------
    def getDigitsDotStr(self):
        """
        Return raw 'x.x', 'x.x.x', or 'x.x.x.x' string.
        """
        return '.'.join([str(x) for x in self.digits])
    # ------------------------------------------------------------------------
    def getDigitsCommaStr(self):
        """
        Return raw 'x.x', 'x.x.x', or 'x.x.x.x' string.
        """
        return ','.join([str(x) for x in self.digits])
    # ------------------------------------------------------------------------
    def getSetupPyVerStr(self):
        """ 
        Return version string used in setup.py file used for Python EGG.
        """
        return '\nVERSION="{}"\n'.format(self.getDigitsDotStr())
    # ------------------------------------------------------------------------
    def getPkgInfoVerStr(self):
        """
        Return version string used in PKG-INFO file used for Python EGG.
        """
        return '\nVersion: {}\n'.format(self.getDigitsDotStr())
    # ------------------------------------------------------------------------
    def getAssemblyVerStr(self):
        """
        Return a version string used for MS VS C# solution.  Usually output
        to a SolutionVersionInfo.cs file, which would coexist with a reduced
        AssemblyInfo.cs and common SolutionInfo.cs.
        """
        return """\n[assembly: System.Reflection.AssemblyVersion("%s")]\n""" % \
            (self.getDigitsDotStr())
    # ------------------------------------------------------------------------
    def getVsVersionInfoStr(self):
        """
        Return a PRODUCTVERSION string for use in a VS_VERSION_INFO block in 
        MS VS C++ *.RC resource file.
        """
        return """\nPRODUCTVERSION %s)]\n""" % (self.getDigitsCommaStr())


# ============================================================================
def main():
    ti = TagInfo(3)
    # exercise all 'get*' methods
    for method in [ method for method in dir(ti) if method[:3]=='get' and \
                    callable(getattr(ti, method)) ]:
        print("{}():  {}".format(method, getattr(ti, method)()))

# ============================================================================
# MAIN
# ============================================================================
if __name__ == '__main__':
    main()


