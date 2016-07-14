from unittest import TestCase
from pyradioconfig.calculator_model_framework.Utils.Version import Version


class TestVersion(TestCase):

  # Hack override used to allow the test to run from python console
  def runTest( self ):
      self.failUnless( True is True )

  def test_fromString(self):
    v123 = Version(1,2,3) #Version 1.2.3
    v012 = Version(0,1,2) #Version 0.1.2
    v024 = Version.fromString("0.2.4") #Version 0.2.4
    v201 = Version.fromString("2.0.1") #Version 2.0.1
    sortedVersion = sorted([v123, v012, v024, v201])
    for version in sortedVersion:
        print version

    self.assertEquals(v012, sortedVersion[0])
    self.assertEquals(v024, sortedVersion[1])
    self.assertEquals(v123, sortedVersion[2])
    self.assertEquals(v201, sortedVersion[3])

