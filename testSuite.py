import unittest

from unittestpackage.test_assert import TestClass1
from unittestpackage.test_assert1 import youDontWantSmoke


# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(youDontWantSmoke)

# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1,tc2])


unittest.TextTestRunner(verbosity=2).run(smokeTest)