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
        # This function resaves the value of the numerator and reduces it
        self.__numerator = n
        self.reduce()
        return self

    def setDenominator(self, d):
        # This function resaves the value of the denominator and reduces it
        if d != 0:  # Check for invalid denominator (0)
            self.__denominator = d
            self.reduce()
            return self
        else:
            raise ValueError("Denominator cannot be zero")

    def isValid(self):
        # This function checks if the rational values inputed create a valid rational number
        # mainly by making sure that the denominator does not equal 0
        return self.__denominator != 0

    def reciprocal(self):
        # This function modifies the rational number into its reciprocal.
        self.__numerator, self.__denominator = self.__denominator, self.__numerator

    def add(self, num2):
        # This function adds two rational numbers
        denominator2 = num2.getDenominator()
        numerator2 = num2.getNumerator()

        if self.__denominator != denominator2:
            # Cross multiplication
            n1 = self.__numerator * denominator2
            n2 = self.__denominator * numerator2
            d1 = self.__denominator * denominator2
            self.__numerator = n1 + n2
            self.__denominator = d1
        else:
            # Same denominator, simple addition
            self.__numerator += numerator2

        self.reduce()
        return self

    def sub(self, num2):
        # This function subtracts two rational numbers
        denominator2 = num2.getDenominator()
        numerator2 = num2.getNumerator()

        if self.__denominator != denominator2:
            # Cross multiplication
            n1 = self.__numerator * denominator2
            n2 = self.__denominator * numerator2
            d1 = self.__denominator * denominator2
            self.__numerator = n1 - n2
            self.__denominator = d1
        else:
            # Same denominator, simple subtraction
            self.__numerator -= numerator2

        self.reduce()
        return self

    def mult(self, num2):
        # This function multiplies two rational numbers
        self.__numerator *= num2.getNumerator()
        self.__denominator *= num2.getDenominator()
        self.reduce()
        return self

    def div(self, num2):
        # This function divides two rational numbers (equivalent to multiplying by the reciprocal)
        if num2.isValid():  # Check for division by zero
            self.__numerator *= num2.getDenominator()
            self.__denominator *= num2.getNumerator()
            self.reduce()
            return self
        else:
            raise ValueError("Cannot divide by zero")

    def reduce(self):
        # Reduces the rational number to lowest terms
        if self.__numerator < 0 and self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator
        common = 0
        while (common != 1):
            common = self.gcf()
            self.__numerator //= common
            self.__denominator //= common

    def gcf(self):
        # Determines the greatest common factor
        common_factor = 1
        min_of_parts = min(abs(int(self.__numerator)), abs(int(self.__denominator)))
        for i in range(min_of_parts, 1, -1):
            if self.__numerator % i == 0 and self.__denominator % i == 0:
                common_factor = i
                break
        return common_factor

    
