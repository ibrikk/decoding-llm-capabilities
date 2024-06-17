"""
Defining a Rational number class

Refer to the instructions on Canvas for more information.
"""
__version__ = 1
import unittest


class Rational:
    '''
    Initialize a new Rational object with value iNum/iDen stored in hidden __numerator and
    __denominator variables.  Calls the reduce() method to put the fraction in lowest terms.
    '''
    def __init__(self, iNum, iDen):
        self.__numerator = iNum
        self.__denominator = iDen
        self.reduce()
        
    
    def getNumerator(self):
        return self.__numerator

    def getDenominator(self):
        return self.__denominator

    def setNumerator(self, n):
        self.__numerator = n
        self.reduce()

    def setDenominator(self, d):
        if d != 0:
            self.__denominator = d
            self.reduce()
    
    
    def isValid(self):
        return self.__denominator != 0
        
    def reciprocal(self):
        self.__numerator, self.__denominator = self.__denominator, self.__numerator
        self.reduce()

    def add(self, num2):
        new_numerator = self.__numerator * num2.getDenominator() + num2.getNumerator() * self.__denominator
        new_denominator = self.__denominator * num2.getDenominator()
        self.__numerator = new_numerator
        self.__denominator = new_denominator
        self.reduce()

    def sub(self, num2):
        new_numerator = self.__numerator * num2.getDenominator() - num2.getNumerator() * self.__denominator
        new_denominator = self.__denominator * num2.getDenominator()
        self.__numerator = new_numerator
        self.__denominator = new_denominator
        self.reduce()

    def mult(self, num2):
        self.__numerator *= num2.getNumerator()
        self.__denominator *= num2.getDenominator()
        self.reduce()

    def div(self, num2):
        self.__numerator *= num2.getDenominator()
        self.__denominator *= num2.getNumerator()
        self.reduce()

    
    
    ################################
    #    HELPER FUNCTIONS BELOW    #
    ################################
    '''
    Reduces the Rational to lowest terms
      - Checks if both the numerator and denominator are negative; if so, makes both positive
      - Calls gcf() to find the greatest common factor between the numerator and denominator, and
        continues to divide by that gcf until the greatest common factor is 1
    '''
    def reduce(self):
        if self.__numerator < 0 and self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator
        common = 0
        while (common != 1):
            common = self.gcf()
            self.__numerator /= common
            self.__denominator /= common
    
    '''
    Determines the greatest common factor between the numerator and denominator
      - Starts checking numbers counting downward from the smaller of the numerator,denominator pair
      - When it finds a number divisble by both, it breaks the loop and returns that number
      - The smallest number that can be returned is 1
    '''
    def gcf(self):
        common_factor = 1
        min_of_parts = min(abs(int(self.__numerator)), abs(int(self.__denominator)))
        for i in range(min_of_parts, 1, -1):
            if self.__numerator % i == 0 and self.__denominator % i == 0:
                 common_factor = i
                 break
        return common_factor
    
    '''
    Returns a string representation of the Rational, e.g. "1/8"
    '''
    def __str__(self):
        return str(int(self.__numerator)) + "/" + str(int(self.__denominator))
    
    '''
    Determines if two Rationals are exactly equal to each other 
    (same numerator and same denominator, 
     no consideration of reducing the numbers)
    '''
    def __eq__(self, r2):
        return self.__numerator == r2.__numerator and self.__denominator == r2.__denominator
    
    ################################
    #     END HELPER FUNCTIONS     #
    ################################    
    
if __name__ == "__main__":
    import unittest
    unittest.main("rationalTest")
    
