
import sys
import os
TEST_CASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test-cases')
sys.path.append(TEST_CASE_DIR)

import unittest

import functions_test as ft

if __name__ == '__main__':
    """
    execute test suite
    """
    pass


suite = unittest.TestSuite()
tests = unittest.defaultTestLoader.loadTestsFromTestCase(ft.FunctionsBlackBox)
suite.addTests(tests)
unittest.TextTestRunner().run(suite)







