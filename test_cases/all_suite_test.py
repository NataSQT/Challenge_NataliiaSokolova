import unittest

from unittest.loader import makeSuite

from pages.add_match_form import Dashboard
from test_cases.framework import Test
from test_cases.login_to_the_system import TestLoginPage
from test_cases.add_player_test import TestAddPlayerPage


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(Dashboard))
    test_suite.addTest(makeSuite(Test))
    test_suite.addTest(makeSuite(TestAddPlayerPage))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
