import unittest
import argparse
from run import Run


def suite():
    testsuite = unittest.TestSuite()
    testsuite.addTest(Tests('test_args'))
    return testsuite


class Tests(unittest.TestCase):
    def test_args(self):
        argsrun = Run()
        argsrun.setOption("verbosity", True)
        self.assertEqual(argsrun.getOption("verbosity"), True)
        self.assertEqual(argsrun.getOption("trash"), -1)
        self.assertEqual(argsrun.getLogSettings(), "DEBUG")


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
