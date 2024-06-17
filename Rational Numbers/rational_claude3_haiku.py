class Rational:
    def __init__(self, iNum, iDen):
        self.__numerator = iNum
        self.__denominator = iDen
        self.reduce()

    def reduce(self):
        if self.__denominator == 0:
            return
        
        sign = 1
        if self.__numerator < 0:
            sign *= -1
        if self.__denominator < 0:
            sign *= -1
            self.__denominator *= -1
        
        gcd = self.gcf()
        self.__numerator //= gcd
        self.__denominator //= gcd
        
        if sign == -1:
            self.__numerator *= -1

    def gcf(self):
        a, b = abs(self.__numerator), abs(self.__denominator)
        while b != 0:
            a, b = b, a % b
        return a

    def getNumerator(self):
        return self.__numerator

    def getDenominator(self):
        return self.__denominator

    def setNumerator(self, n):
        self.__numerator = n
        self.reduce()

    def setDenominator(self, d):
        if d == 0:
            return
        self.__denominator = d
        self.reduce()

    def isValid(self):
        return self.__denominator != 0

    def reciprocal(self):
        self.__numerator, self.__denominator = self.__denominator, self.__numerator
        self.reduce()

    def add(self, num2):
        new_num = self.__numerator * num2.getDenominator() + num2.getNumerator() * self.__denominator
        new_den = self.__denominator * num2.getDenominator()
        self.__numerator = new_num
        self.__denominator = new_den
        self.reduce()

    def sub(self, num2):
        new_num = self.__numerator * num2.getDenominator() - num2.getNumerator() * self.__denominator
        new_den = self.__denominator * num2.getDenominator()
        self.__numerator = new_num
        self.__denominator = new_den
        self.reduce()

    def mult(self, num2):
        new_num = self.__numerator * num2.getNumerator()
        new_den = self.__denominator * num2.getDenominator()
        self.__numerator = new_num
        self.__denominator = new_den
        self.reduce()

    def div(self, num2):
        new_num = self.__numerator * num2.getDenominator()
        new_den = self.__denominator * num2.getNumerator()
        self.__numerator = new_num
        self.__denominator = new_den
        self.reduce()

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __eq__(self, r2):
        return self.__numerator == r2.getNumerator() and self.__denominator == r2.getDenominator()