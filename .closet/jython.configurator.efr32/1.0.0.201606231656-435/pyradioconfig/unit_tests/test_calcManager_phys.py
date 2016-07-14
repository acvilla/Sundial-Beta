from unittest import TestCase
from enum import Enum

from pyradioconfig.calculator_model_framework.CalcManager import CalcManager
from pyradioconfig.features.features import Features
from pyradioconfig.parts.unit_test_part.phys.Phys_Essence import PHYS_Essence
from pyradioconfig.parts.unit_test_part.profiles.Profile_Base import Profile_Base
from pyradioconfig._version import __version__ as calculator_version
from pyradioconfig.pycalcmodel import ModelRoot, ModelVariable, ModelVariableFormat, CreateModelVariableEnum


class TestCalcManagerPhys(TestCase):

  # Hack override used to allow the test to run from python console
  def runTest( self ):
    self.failUnless( True is True )

  def test_getPhysFromOPN(self):
        part_family = "dumbo"
        part_revision = "A0"
        calMgr = CalcManager(part_family, part_revision)
        phys = calMgr.getPhyNames()
        for phy in phys:
            print phy
        self.assertTrue(len(phys) > 0)

