class Rational:
    def __init__(self, iNum, iDen):
        self.__numerator = iNum
        self.__denominator = iDen
        self.reduce()

    def __str__(self):
        return str(self.__numerator) + "/" + str(self.__denominator)

    def __eq__(self, r2):
        return self.__numerator == r2.__numerator and self.__denominator == r2.__denominator

    def reduce(self):
        gcd_val = self.gcf(self.__numerator, self.__denominator) 
        sign = 1
        if self.__numerator < 0:
            sign = -1
            self.__numerator = -self.__numerator
        if self.__denominator < 0:
            sign = -sign
            self.__denominator = -self.__denominator
        self.__numerator //= gcd_val
        self.__denominator //= gcd_val
        self.__numerator = sign*self.__numerator

    def gcf(self, num1, num2):
        factor = 1
        for i in range(1, min(abs(num1), abs(num2)) + 1):
            if num1 % i == 0 and num2 % i == 0:
                factor = i
        return factor

    def getNumerator(self):
        return self.__numerator
    
    def getDenominator(self):
        return self.__denominator
    
    def setNumerator(self, n):
        self.__numerator = n
        self.reduce()
    
    def setDenominator(self, d):
        self.__denominator = d
        self.reduce()
    
    def isValid(self):
        return self.__denominator != 0

    def reciprocal(self):
        temp = self.__numerator
        self.__numerator = self.__denominator
        self.__denominator = temp
        self.reduce()

    def add(self, num2):
        num = self.__numerator * num2.__denominator + num2.__numerator * self.__denominator
        den = self.__denominator * num2.__denominator
        self.__numerator = num
        self.__denominator = den
        self.reduce()

    def sub(self, num2):
        num = self.__numerator * num2.__denominator - num2.__numerator * self.__denominator
        den = self.__denominator * num2.__denominator
        self.__numerator = num
        self.__denominator = den
        self.reduce()

    def mult(self, num2):
        self.__numerator *= num2.__numerator
        self.__denominator *= num2.__denominator
        self.reduce()

    def div(self, num2):
        self.__numerator *= num2.__denominator
        self.__denominator *= num2.__numerator
        self.reduce()