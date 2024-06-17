class Rational:
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
        self.__denominator = d
        self.reduce()

    def isValid(self):
        return self.__denominator != 0

    def reciprocal(self):
        self.__numerator, self.__denominator = self.__denominator, self.__numerator
        self.reduce()

    def add(self, num2):
        if self.__denominator != num2.getDenominator():
            n1 = self.__numerator * num2.getDenominator()
            n2 = self.__denominator * num2.getNumerator()
            d1 = self.__denominator * num2.getDenominator()
            self.__numerator = n1 + n2
            self.__denominator = d1
        else:
            self.__numerator += num2.getNumerator()
        self.reduce()

    def sub(self, num2):
        if self.__denominator != num2.getDenominator():
            n1 = self.__numerator * num2.getDenominator()
            n2 = self.__denominator * num2.getNumerator()
            d1 = self.__denominator * num2.getDenominator()
            self.__numerator = n1 - n2
            self.__denominator = d1
        else:
            self.__numerator -= num2.getNumerator()
        self.reduce()

    def mult(self, num2):
        self.__numerator *= num2.getNumerator()
        self.__denominator *= num2.getDenominator()
        self.reduce()

    def div(self, num2):
        self.__numerator *= num2.getDenominator()
        self.__denominator *= num2.getNumerator()
        self.reduce()

    def reduce(self):
        if self.__numerator < 0 and self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator
        common = 0
        while (common != 1):
            common = self.gcf()
            self.__numerator //= common
            self.__denominator //= common

    def gcf(self):
        common_factor = 1
        min_of_parts = min(abs(int(self.__numerator)), abs(int(self.__denominator)))
        for i in range(min_of_parts, 1, -1):
            if self.__numerator % i == 0 and self.__denominator % i == 0:
                 common_factor = i
                 break
        return common_factor

    def __str__(self):
        return str(int(self.__numerator)) + "/" + str(int(self.__denominator))

    def __eq__(self, r2):
        return self.__numerator == r2.__numerator and self.__denominator == r2.__denominator
