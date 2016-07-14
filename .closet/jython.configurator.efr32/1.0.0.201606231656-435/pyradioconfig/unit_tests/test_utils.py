import os
import inspect
from unittest import TestCase
from pyradioconfig.calculator_model_framework.Utils.ClassManager import ClassManager

class TestUtils(TestCase):

  # Hack override used to allow the test to run from python console
  def runTest( self ):
      self.failUnless( True is True )

  # Test loading a module with path
  def test_load_module(self):
      path = os.path.dirname(__file__) + r"\..\calculator_model_framework\Utils\Version.py"
      module = ClassManager.load_module(path)
      #module.Version(1,2,3).hello("Test")

      for cls in dir(module):          #<-- Loop over all objects in the module's namespace
        cls=getattr(module,cls)
        if (inspect.isclass(cls)                # Make sure it is a class
            and inspect.getmodule(cls)==module ):  # Make sure it was defined in module, not just imported
            #and issubclass(cls,Version)):          # Make sure it is a subclass of base
            # print('found in {f}: {c}'.format(f=module.__name__,c=cls))
            self.assertEquals("1.2.3", str(cls(1,2,3)))

