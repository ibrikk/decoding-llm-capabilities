"""
@author: Patrick
"""

import unittest
from rational import Rational


class TestRational(unittest.TestCase):
    # Below are the tests for Rational
    def testGetNumerator(self):
        # This test is testing whether or not the proper numerator is retrieved with the getNumerator function
        assert Rational(2, 5).getNumerator() == 2, "2/5 the numerator is 2"
        assert Rational(-1, 7).getNumerator() == -1, "-1/7 the numerator is -1"
        assert Rational(7, -5).getNumerator() == 7, "7/-5 the numerator is 7"
    
    def testGetDenominator(self):
        # This test is testing whether or not the proper denominator is retrieved with the getDenominator function
        assert Rational(3, 5).getDenominator() == 5, "3/5 the denominator is 5"
        assert Rational(-1, 12).getDenominator() == 12,"-1/12 the denominator is 12"
        assert Rational(3, -4).getDenominator() == -4, "3/-4 the denominatoer is -4"
    
    def testSetNumerator(self):
        # This test is testing whether or not the Numerator is replaced and then if possible the Rational value reduced and returned
        assert Rational(1, 2).setNumerator(3) == Rational(3,2), "3/2 was not returned by setNumerator"
        assert Rational(-1, 3).setNumerator(-4) == Rational(-4,3), "-4/3 was not returned by setNumerator"
        assert Rational(1, 2).setNumerator(4) == Rational(2,1), "2/1 was not returned by setNumerator"
    
    def testSetDenominator(self):
        # This test is testing whether or not the Denominator is replaced and then if possible the Rational value reduced and returned
        assert Rational(1, 2).setDenominator(3) == Rational(1,3), "1/3 was not returned by setDenominator"
        assert Rational(1, 2).setDenominator(-4) == Rational(1,-4), "1/-4 was not returned by setDenominator"
        assert Rational(2, 3).setDenominator(4) == Rational(1,2), "1/2 was not returned by setDenominator"
    
    def testIsValid(self):
        # this is testing whether the Rationals denominator is equal to 0 it will return false else it will return true for a valid Rational
        assert Rational(1,7).isValid() == True, "1/7 was not returned as True"
        assert Rational(-1,7).isValid() == True, "-1/7 was not returned as True"
        assert Rational(1,0).isValid() == False, "1/0 was not returned as False"
        
    def testAdd(self):
        # this is testing if the proper sum Rational is returned when two rationals are input
        assert Rational(1, 5).add(Rational(2, 5)) == Rational(3, 5), "3/5 was not returned by add"
        assert Rational(2, 3).add(Rational(3, 4)) == Rational(17, 12), "17/12 was not returned by add"
        assert Rational(1, 2).add(Rational(-1, 4)) == Rational(1, 4), "1/4 was not returned by add"
        
    def testReciprocal(self):
        r = Rational(4, 7)
        r.reciprocal()
        assert r == Rational(7, 4), "reciprocal of 4/7 should be 7/4"
        r.reciprocal()
        assert r == Rational(4, 7), "reciprocal of 7/4 should be 4/7"
        
    def testSub(self):
        # this is testing if the proper difference Rational is returned when two rationals are input
        assert Rational(2, 3).sub(Rational(1, 3)) == Rational(1, 3), "1/3 was not returned by sub"
        assert Rational(4, 5).sub(Rational(-2, 5)) == Rational(6, 5), "6/5 was not returned by sub"
        assert Rational(1, 3).sub(Rational(2, 3)) == Rational(-1, 3), "-1/3 was not returned by sub"
    
    def testMult(self):
        # this is testing if the proper product Rational is returned when two rationals are input
        assert Rational(1,2).mult(Rational(1,4)) == Rational(1, 8), "3/4 was not returned by mult"
        assert Rational(2,5).mult(Rational(-1,4)) == Rational(-1, 10), "-1/10 was not returned by mult"
        assert Rational(3,5).mult(Rational(6,7)) == Rational(18, 35), "18/35 was not returned by mult"
    
    def testDiv(self):
        # this is testing if the proper quotient Rational is returned when two rationals are input
        assert Rational(2,5).div(Rational(3,5)) == Rational(2,3), "2/3 was not returned by div"
        assert Rational(1,5).div(Rational(-1,4)) == Rational(4,-5), "4/-5 was not returned by div"
        assert Rational(-3,2).div(Rational(7,8)) == Rational(-12,7), "-12/7 was not returned by div"

###############################################################

# Here is where you will write your test case functions
    
###############################################################    
    


if __name__ == '__main__':
    unittest.main()
