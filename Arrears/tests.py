import unittest

from functions.engine import *

class EngineValues(unittest.TestCase):
    def test_decimal(self):
        amnt=4567.37
        mmt=m_round(amnt,trac=0.05)
        self.assertEquals(mmt,4567.35)

    def test_daysCalculator(self):
        nodays=1
        toPay=1000
        daysInMonth=31
        arrear=daysCalculator(nodays,toPay,daysInMonth)
        self.assertEquals(arrear,32.25)

