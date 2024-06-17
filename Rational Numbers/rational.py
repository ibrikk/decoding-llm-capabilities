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
        # returns the value of the numerator from the input of rational class
        return int(self.__numerator)
    
    def getDenominator(self):
        # returns the value of the denominator from the input of rational class
        return int(self.__denominator)
    
    def setNumerator(self, n):
        # this function resaves the value of the numerator and if possible reduces it when the new numerater value is saved
        self.__numerator = n
        
        self.reduce()
        
        self = Rational(self.__numerator, self.__denominator)
        
        return self
            
        
    def setDenominator(self, d):
        # this function resaves the value of the denominator and if possible reduces it when the new denominator value is saved
        self.__denominator = d
        
        self.reduce()
        
        self = Rational(self.__numerator, self.__denominator)
        
        return self
    
    
    def isValid(self):
        # this function checks to make sure that the rational values inputed create a valid rational number 
        # mainly by making sure that the denominator does not equal 0
        den = int(self.__denominator)
        
        if den == 0:
            return False
        else:
            return True
        
    def reciprocal(self):
        # This function modifies the rational number into its reciprocal.
        self.__numerator, self.__denominator = self.__denominator, self.__numerator
        # self.reduce()
        return self
        # oldNum = self.getNumerator()
        # self.setNumerator(self.getDenominator())
        # self.setDenominator(oldNum)
    
    def add(self, num2):
        # this function takes the input of the already stored rational value and another rational value 
        # then adds the two together then reduces the value to the lowest possible for then stores and returns the value
        denominator2 = num2.getDenominator()

        numerator2 = num2.getNumerator()

        # this is in the case that the denominators are not the same 
        # cross multiplication is applied then addition is possible
        if self.__denominator != denominator2:
	
            n1 = self.__numerator * denominator2

            n2 = self.__denominator * numerator2

            d1 = self.__denominator * denominator2
	
            self.__numerator = int(n1 +n2)
         
            self.__denominator = int(d1)
            
            self.reduce()
         
            self = Rational(self.__numerator, self.__denominator)
         
            return self
         
         # this is in the case that the denominators are the same 
         # that means that they can simply be added together with nothing specaial done to them

        else:	  	
            self.__numerator = self.__numerator + numerator2
            
            self.reduce()
         
            self = Rational(self.__numerator, self.__denominator)

            return self
  	
  	
    def sub(self, num2):
        # this function takes the input of the already stored rational value and another rational value 
        # then subtracts the two together then reduces the value to the lowest possible for then stores and returns the value
 	  	
        denominator2 = num2.getDenominator()

        numerator2 = num2.getNumerator()

        # this is in the case that the denominators are not the same 
        # cross multiplication is applied then subtraction is possible
        if self.__denominator != denominator2:
 	
             n1 = self.__numerator * denominator2

             n2 = self.__denominator * numerator2

             d1 = self.__denominator * denominator2
 	
             self.__numerator = int(n1 - n2)
          
             self.__denominator = int(d1)
             
             self.reduce()
          
             self = Rational(self.__numerator, self.__denominator)
          
             return self
	  	
        # this is in the case that the denominators are the same 
        # that means that they can simply be subtracted with nothing specaial done to them  
        else: 
             self.__numerator = self.__numerator - numerator2
             
             
             self.reduce()
             
             self = Rational(self.__numerator, self.__denominator)
  	
             return self
             
    
    def mult(self, num2):
        # this function multiplies the two numerators and two denominators together 
        # then returns the reduced value of the rational created 
        
        denominator2 = num2.getDenominator()
  	
        numerator2 = num2.getNumerator()
	  	
        self.__numerator = self.__numerator * numerator2
        
        self.__denominator = self.__denominator * denominator2
        
        self.reduce()
        
        self = Rational(self.__numerator, self.__denominator)
        
        return self
        

    
    def div(self, num2):
        # this function multiplies the numerator of one and the denominator of the other
        # then returns the reduced value from the created rational
        
        denominator2 = num2.getDenominator()
  	
        numerator2 = num2.getNumerator()
	  	
        self.__numerator = self.__numerator * denominator2
        
        self.__denominator = self.__denominator * numerator2
        
        self.reduce()
        
        self = Rational(self.__numerator, self.__denominator) 
        
        return self
    
    
    
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
    
