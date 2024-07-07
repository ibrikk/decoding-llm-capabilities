""" Defining a Rational number class
Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: YOUR NAME HERE """

class Rational:
    """ The Rational class allows us to implement rational numbers with exact precision, 
    without the approximations/errors used in binary representations """
     
    def __init__(self, iNum, iDen):
        """ Constructs a new Rational object with value iNum/iDen stored in hidden __numerator 
        and __denominator variables.  Calls reduce() to put the fraction in lowest terms. """
        pass # to be implemented ...
    
    def getNumerator(self):
        pass # to be implemented ...
    
    def getDenominator(self):
        pass # to be implemented ...
    
    def setNumerator(self, n):
        pass # to be implemented ...
            
    def setDenominator(self, d):
        pass # to be implemented ...
        
    def isValid(self):
        pass # to be implemented ...
    
    def reciprocal(self):
        pass # to be implemented ...
    
    def add(self, num2):
        pass # to be implemented ...
  	
    def sub(self, num2):
        pass # to be implemented ...
             
    def mult(self, num2):
        pass # to be implemented ...
        
    def div(self, num2):
        pass # to be implemented ...
    
    
    ################################
    #    HELPER FUNCTIONS BELOW    #
    ################################
    def reduce(self):
        """ Reduces the Rational to lowest terms
        - Checks if both the numerator and denominator are negative; if so, makes both positive
        - Calls gcf() to find the greatest common factor between the numerator and denominator, and
            continues to divide by that gcf until the greatest common factor is 1 """
        if self.__numerator < 0 and self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator
        common = 0
        while (common != 1):
            common = self.gcf()
            self.__numerator /= common
            self.__denominator /= common
    
    def gcf(self):
        """ Determines the greatest common factor between the numerator and denominator
        - Starts checking numbers counting downward from the smaller of the numerator,denominator pair
        - When it finds a number divisble by both, it breaks the loop and returns that number
        - The smallest number that can be returned is 1 """
        common_factor = 1
        for i in range(min(abs(int(self.__numerator)), abs(int(self.__denominator))), 1, -1):
            if self.__numerator % i == 0 and self.__denominator % i == 0:
                 common_factor = i
                 break
        return common_factor
    
    def __str__(self):
        """ Returns a string representation of the Rational, e.g. "1/8" """
        return str(int(self.__numerator)) + "/" + str(int(self.__denominator))
    
    def __eq__(self, r2):
        """ Determines if two Rationals are exactly equal to each other 
        (same numerator and same denominator, no consideration of reducing the numbers) """
        return self.__numerator == r2.__numerator and self.__denominator == r2.__denominator
    
    ################################
    #     END HELPER FUNCTIONS     #
    ################################    
    

def main():
    """ This main should only start rationalTest's unit tests.  
    Do NOT implement your tests here.  WebCAT wants them in rationalTest.py """
    import unittest
    unittest.main("rationalTest")
    
if __name__ == "__main__":
    main()
