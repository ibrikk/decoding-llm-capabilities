"""
@author: John; Patrick Sullivan
"""
import rational
import unittest
import rationalTest

class TestRational(unittest.TestCase):

    # Helper functions
    def createRational(self, n, d):
        ''' Returns a new Rational n/d '''
        return rational.Rational(n,d)
    
    # getNumerator
    def test_RationalTest(self):
        print("Students' tests in rationalTest:")
        results = unittest.main("rationalTest", exit=False, verbosity=0)
        numFails = len(results.result.failures)
        numErrors = len(results.result.errors)
        self.assertEqual(numFails, 0, "A test in your TestRational class failed")
        self.assertEqual(numErrors, 0, "A test in your TestRational class produced an error")

    def test_getNumerator_one(self):
        r = self.createRational(1,4)
        self.assertEqual(r.getNumerator(), 1, "getNumerator() tested on 1/4 should return 1")
    
    def test_getNumerator_two(self):
        r = self.createRational(2,16)
        self.assertEqual(r.getNumerator(), 1, "getNumerator() tested on 2/16 should return 1")
    
    def test_getNumerator_three(self):
        r = self.createRational(-2,16)
        self.assertEqual(r.getNumerator(), -1, "getNumerator() tested on -2/16 should return -1")
        
    def test_getNumerator_four(self):
        r = self.createRational(2,-16)
        self.assertEqual(r.getNumerator(), 1, "getNumerator() tested on 2/-16 should return 1")        
    
    
    # getDenominator
    def test_getDenominator_one(self):
        r = self.createRational(1,4)
        self.assertEqual(r.getDenominator(), 4, "getDenominator() tested on 1/4 should return 4")
    
    def test_getDenominator_two(self):
        r = self.createRational(2,16)
        self.assertEqual(r.getDenominator(), 8, "getDenominator() tested on 2/16 should return 8")
    
    def test_getDenominator_three(self):
        r = self.createRational(-2,16)
        self.assertEqual(r.getDenominator(), 8, "getDenominator() tested on -2/16 should return 8")
        
    def test_getDenominator_four(self):
        r = self.createRational(2,-16)
        self.assertEqual(r.getDenominator(), -8, "getDenominator() tested on 2/-16 should return -8")        


    # setNumerator
    def test_setNumerator_one(self):
        r = self.createRational(1,4)
        r.setNumerator(3)
        self.assertEqual(r.getNumerator(), 3, "setNumerator(3) tested on 1/4 should return 3")

    def test_setNumerator_two(self):
        r = self.createRational(1,4)
        r.setNumerator(2)
        self.assertEqual(r.getNumerator(), 1, "setNumerator(2) tested on 1/4 should return 1")

    def test_setNumerator_three(self):
        r = self.createRational(1,4)
        r.setNumerator(-2)
        self.assertEqual(r.getNumerator(), -1, "setNumerator(-2) tested on 1/4 should return -1")


    # setDenominator
    def test_setDenominator_one(self):
        r = self.createRational(1,4)
        r.setDenominator(3)
        self.assertEqual(r.getDenominator(), 3, "setDenominator(3) tested on 1/4 should return 3")

    def test_setDenominator_two(self):
        r = self.createRational(2,7)
        r.setDenominator(4)
        self.assertEqual(r.getDenominator(), 2, "setDenominator(4) tested on 2/7 should return 2")

    def test_setDenominator_three(self):
        r = self.createRational(2,7)
        r.setDenominator(-4)
        self.assertEqual(r.getDenominator(), -2, "setDenominator(-4) tested on 2/7 should return -2")


    # isValid
    def test_isValid_one(self):
        r = self.createRational(1,4)
        self.assertEqual(r.isValid(), True, "1/4 should be a valid Rational")

    def test_isValid_two(self):
        r = self.createRational(1,-4)
        self.assertEqual(r.isValid(), True, "1/-4 should be a valid Rational")
        
    def test_isValid_three(self):
        r = self.createRational(1,0)
        self.assertEqual(r.isValid(), False, "1/0 should NOT be a valid Rational")

    def test_isValid_four(self):
        r = self.createRational(1,-0)
        self.assertEqual(r.isValid(), False, "1/-0 should NOT be a valid Rational")

    def test_reciprocal_4_7(self):
        r1 = self.createRational(4, 7)
        r2 = self.createRational(7, 4)
        r1.reciprocal()
        self.assertEqual(r1, r2, "Reciprocal of 4/7 should be 7/4")

    def test_reciprocal_7_4(self):
        r1 = self.createRational(4, 7)
        r2 = self.createRational(7, 4)
        r2.reciprocal()
        self.assertEqual(r1, r2, "Reciprocal of 7/4 should be 4/7")
    
    # add
    def test_add_one(self):
        r1 = self.createRational(1,4)
        r2 = self.createRational(1,4)
        r_sol = self.createRational(1,2)
        r1.add(r2)
        self.assertEqual(r1, r_sol, "1/4 + 1/4 = 1/2")
        
    def test_add_two(self):
        r1 = self.createRational(1,4)
        r2 = self.createRational(-1,8)
        r_sol = self.createRational(1,8)
        r1.add(r2)
        self.assertEqual(r1, r_sol, "1/4 + -1/8 = 1/8")

    def test_add_three(self):
        r1 = self.createRational(1,4)
        r2 = self.createRational(1,8)
        r_sol = self.createRational(3,8)
        r1.add(r2)
        self.assertEqual(r1, r_sol, "1/4 + 1/8 = 3/8")
        
    def test_add_four(self):
        r1 = self.createRational(1,10)
        r2 = self.createRational(2,10)
        r_sol = self.createRational(3,10)
        r1.add(r2)
        self.assertEqual(r1, r_sol, "1/10 + 2/10 = 3/10")        
        
    def test_add_five(self):
        r1 = self.createRational(1,4)
        r2 = self.createRational(1,-8)
        r_sol = self.createRational(1,8)
        r1.add(r2)
        self.assertEqual(r1, r_sol, "1/4 + 1/-8 = 1/8")           
        
    def test_add_six(self):
        r1 = self.createRational(1,2)
        r2 = self.createRational(1,-8)
        r_sol = self.createRational(3,8)
        r1.add(r2)
        self.assertEqual(r1, r_sol, "1/2 + 1/-8 = 3/8")  
        
        
    # sub
    def test_sub_one(self):
        r1 = self.createRational(3,2)
        r2 = self.createRational(1,4)
        r_sol = self.createRational(5,4)
        r1.sub(r2)
        self.assertEqual(r1, r_sol, "3/2 - 1/4 = 5/4")
        
    def test_sub_two(self):
        r1 = self.createRational(1,4)
        r2 = self.createRational(-1,8)
        r_sol = self.createRational(3,8)
        r1.sub(r2)
        self.assertEqual(r1, r_sol, "1/4 - -1/8 = 3/8")

    def test_sub_three(self):
        r1 = self.createRational(1,4)
        r2 = self.createRational(1,8)
        r_sol = self.createRational(1,8)
        r1.sub(r2)
        self.assertEqual(r1, r_sol, "1/4 - 1/8 = 1/8")
        
    def test_sub_four(self):
        r1 = self.createRational(1,10)
        r2 = self.createRational(2,10)
        r_sol = self.createRational(-1,10)
        r1.sub(r2)
        self.assertEqual(r1, r_sol, "1/10 - 2/10 = -1/10")        
        
    def test_sub_five(self):
        r1 = self.createRational(1,4)
        r2 = self.createRational(1,-8)
        r_sol = self.createRational(3,8)
        r1.sub(r2)
        self.assertEqual(r1, r_sol, "1/4 - 1/-8 = 3/8")           
        
    def test_sub_six(self):
        r1 = self.createRational(1,2)
        r2 = self.createRational(1,-8)
        r_sol = self.createRational(5,8)
        r1.sub(r2)
        self.assertEqual(r1, r_sol, "1/2 - 1/-8 = 5/8")          
        
        
    # mult
    def test_mult_one(self):
        r1 = self.createRational(3,2)
        r2 = self.createRational(1,4)
        r_sol = self.createRational(3,8)
        r1.mult(r2)
        self.assertEqual(r1, r_sol, "3/2 * 1/4 = 3/8")
        
    def test_mult_two(self):
        r1 = self.createRational(1,4)
        r2 = self.createRational(-1,8)
        r_sol = self.createRational(-1,32)
        r1.mult(r2)
        self.assertEqual(r1, r_sol, "1/4 * -1/8 = -1/32")

    def test_mult_three(self):
        r1 = self.createRational(1,4)
        r2 = self.createRational(1,8)
        r_sol = self.createRational(1,32)
        r1.mult(r2)
        self.assertEqual(r1, r_sol, "1/4 * 1/8 = 1/32")
        
    def test_mult_four(self):
        r1 = self.createRational(1,10)
        r2 = self.createRational(2,10)
        r_sol = self.createRational(1,50)
        r1.mult(r2)
        self.assertEqual(r1, r_sol, "1/10 * 2/10 = 1/50")        
        
    def test_mult_five(self):
        r1 = self.createRational(1,4)
        r2 = self.createRational(1,-8)
        r_sol = self.createRational(1,-32)
        r1.mult(r2)
        self.assertEqual(r1, r_sol, "1/4 * 1/-8 = 1/-32")           
        
    def test_mult_six(self):
        r1 = self.createRational(1,2)
        r2 = self.createRational(1,-8)
        r_sol = self.createRational(1,-16)
        r1.mult(r2)
        self.assertEqual(r1, r_sol, "1/2 * 1/-8 = 1/-16")            
        
        
    # mult
    def test_div_one(self):
        r1 = self.createRational(3,2)
        r2 = self.createRational(1,4)
        r_sol = self.createRational(6,1)
        r1.div(r2)
        self.assertEqual(r1, r_sol, "3/2 / 1/4 = 6/1")
        
    def test_div_two(self):
        r1 = self.createRational(1,4)
        r2 = self.createRational(1,8)
        r_sol = self.createRational(2,1)
        r1.div(r2)
        self.assertEqual(r1, r_sol, "1/4 / 1/8 = 2/1")

    def test_div_three(self):
        r1 = self.createRational(3,7)
        r2 = self.createRational(1,3)
        r_sol = self.createRational(9,7)
        r1.div(r2)
        self.assertEqual(r1, r_sol, "3/7 / 1/3 = 9/7")
        
    def test_div_four(self):
        r1 = self.createRational(7,3)
        r2 = self.createRational(1,3)
        r_sol = self.createRational(7,1)
        r1.div(r2)
        self.assertEqual(r1, r_sol, "7/3 / 1/3 = 7/1")        
        
    def test_div_five(self):
        r1 = self.createRational(7,3)
        r2 = self.createRational(1,5)
        r_sol = self.createRational(35,3)
        r1.div(r2)
        self.assertEqual(r1, r_sol, "7/3 / 1/5 = 35/3")           
        
    def test_div_six(self):
        r1 = self.createRational(7,5)
        r2 = self.createRational(1,3)
        r_sol = self.createRational(21,5)
        r1.div(r2)
        self.assertEqual(r1, r_sol, "7/5 / 1/3 = 21/5")          
        
if __name__=='__main__':
    unittest.main(verbosity=0)