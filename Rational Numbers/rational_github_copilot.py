class Rational:
    def __init__(self, iNum, iDen):
        if iDen == 0:
            raise ValueError("Denominator cannot be 0")
        self.__numerator = iNum
        self.__denominator = iDen
        self.reduce()

    def reduce(self):
        factor = self.gcf()
        self.__numerator //= factor
        self.__denominator //= factor

    def gcf(self):
        a, b = self.__numerator, self.__denominator
        while b != 0:
            a, b = b, a % b
        return a

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __eq__(self, r2):
        return self.__numerator == r2.__numerator and self.__denominator == r2.__denominator

    def getNumerator(self):
        return self.__numerator

    def getDenominator(self):
        return self.__denominator

    def setNumerator(self, n):
        self.__numerator = n
        self.reduce()

    def setDenominator(self, d):
        if d == 0:
            raise ValueError("Denominator cannot be 0")
        self.__denominator = d
        self.reduce()

    def isValid(self):
        return self.__denominator != 0

    def reciprocal(self):
        self.__numerator, self.__denominator = self.__denominator, self.__numerator

    def add(self, num2):
        self.__numerator = self.__numerator * num2.__denominator + self.__denominator * num2.__numerator
        self.__denominator *= num2.__denominator
        self.reduce()

    def sub(self, num2):
        self.__numerator = self.__numerator * num2.__denominator - self.__denominator * num2.__numerator
        self.__denominator *= num2.__denominator
        self.reduce()

    def mult(self, num2):
        self.__numerator *= num2.__numerator
        self.__denominator *= num2.__denominator
        self.reduce()

    def div(self, num2):
        self.__numerator *= num2.__denominator
        self.__denominator *= num2.__numerator
        self.reduce()