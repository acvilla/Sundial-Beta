from unittest import TestCase

from enum import Enum

from pyradioconfig.calculator_model_framework.CalcManager import CalcManager
from pyradioconfig.features.features import Features
from pyradioconfig.parts.unit_test_part.calculators.common import Common
from pyradioconfig._version import __version__ as calculator_version
from pyradioconfig.pycalcmodel import ModelRoot


class SomeEnum(Enum):
  first = 1
  second = 2
  third = 3
  fourth = 4
  def __mul__(self, other):
        return SomeEnum(self.value * other)
  def __rmul__(self, other):
        return SomeEnum(self.value * other)

"""
This is a simple test that exercises the root calculation logic without the part info (family, revision) overhead
"""
class TestCalc(TestCase):

  # Hack override used to allow the test to run from python console
  def runTest( self ):
      self.failUnless( True is True )

  def test_calculate(self):
    # Create the model for the modem...
    part_family = 'unit_test_part'
    modem_model = ModelRoot(part_family, calculator_version)

    # Build features
    Features.build(modem_model)

    # Examples from unit_test_part
    calc = Common()
    calc.buildVariables(modem_model)
    #print modem_model

    # Confirm we got more than one var back
    self.assertTrue(len(modem_model.vars.ZZ_VARIABLE_KEYS) > 0, "No variabels returned")

    # Set some values and expect them to double
    modem_model.vars.dummy_modem_sync_bits.value = 100
    modem_model.vars.dummy_modindex.value = 1.0
    modem_model.vars.dummy_complex.value = complex(2,3)
    modem_model.vars.dummy_long.value = long(65535)
    modem_model.vars.dummy_bool.value = False
    modem_model.vars.dummy_str.value = "i"
    modem_model.vars.dummy_modem_cf_oversampling.value = SomeEnum.first

    calc_functions = list()
    calc_functions.extend(calc.getCalculationList())
    calcManager = CalcManager("", "")
    calcManager.calculateOverList(calc_functions, modem_model)
    #print modem_model

    self.assertEqual(200, modem_model.vars.dummy_modem_sync_bits.value)
    self.assertEqual(2.0, modem_model.vars.dummy_modindex.value)
    self.assertEqual(complex(4,6), modem_model.vars.dummy_complex.value)
    self.assertEqual(long(131070), modem_model.vars.dummy_long.value)
    self.assertEqual(False, modem_model.vars.dummy_bool.value)
    self.assertEqual("ii", modem_model.vars.dummy_str.value)
    self.assertEqual(SomeEnum.second, modem_model.vars.dummy_modem_cf_oversampling.value)
