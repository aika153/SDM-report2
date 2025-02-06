#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test_sample4_1 (self):
                self.assertEqual (-1, calc(999, 0.1))

        def test_sample5 (self):
                self.assertEqual (-1, calc(0, 7))

        def test_sample6 (self):
                self.assertEqual (7, calc(1, 7))

        def test_sample7 (self):
                self.assertEqual (-1, calc(7,0))

        def test_sample8 (self):
                self.assertEqual (7, calc(7,1))

        def test_sample9 (self):
                self.assertEqual (999, calc(1,999))

        def test_sample10 (self):
                self.assertEqual (-1, calc(1,1000))

        def test_sample11 (self):
                self.assertEqual (999, calc(999, 1))

        def test_sample12 (self):
                self.assertEqual (-1, calc(1000, 1))

        def test_sample13 (self):
                self.assertEqual (7, calc(7, 1))

        def test_sample14 (self):
                self.assertEqual (49, calc(7, 7))

        def test_sample15 (self):
                self.assertEqual (-1, calc(None ,None))

