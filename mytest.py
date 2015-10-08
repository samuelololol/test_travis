#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Oct 08, 2015 '
__author__= 'samuel'


from mynumber import MyNumber
import unittest

import random
class TestMyNumber(unittest.TestCase):
    def setUp(self):
        self.num = MyNumber()

    def test_add(self):
        x = random.randint(1,10)
        y = random.randint(1,10)
        result = self.num.add(x,y)
        self.assertTrue(result == (x + y))

    def test_sub(self):
        x = random.randint(1,10)
        y = random.randint(1,10)
        result = self.num.sub(x,y)
        self.assertTrue(result == (x - y))

    def test_mul(self):
        x = random.randint(1,10)
        y = random.randint(1,10)
        result = self.num.mul(x,y)
        self.assertTrue(result == (x * y))

    def test_div(self):
        x = random.randint(1,10)
        y = random.randint(1,10)
        result = self.num.div(x,y)
        self.assertTrue(result == (x / y))

    def tearDown(self):
        del self.num

