class Rational:
    def __init__(self, iNum, iDen):
        if iDen == 0:
            raise ValueError("Denominator cannot be 0")
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
        if d == 0:
            raise ValueError("Denominator cannot be 0")
        self.__denominator = d
        self.reduce()

    def isValid(self):
        return self.__denominator != 0

    def reciprocal(self):
        if self.__numerator == 0:
            raise ValueError("Cannot take reciprocal of 0")
        self.__numerator, self.__denominator = self.__denominator, self.__numerator
        self.reduce()

    def add(self, num2):
        new_numerator = self.__numerator * num2.getDenominator() + num2.getNumerator() * self.__denominator
        new_denominator = self.__denominator * num2.getDenominator()
        self.__numerator, self.__denominator = new_numerator, new_denominator
        self.reduce()

    def sub(self, num2):
        new_numerator = self.__numerator * num2.getDenominator() - num2.getNumerator() * self.__denominator
        new_denominator = self.__denominator * num2.getDenominator()
        self.__numerator, self.__denominator = new_numerator, new_denominator
        self.reduce()

    def mult(self, num2):
        new_numerator = self.__numerator * num2.getNumerator()
        new_denominator = self.__denominator * num2.getDenominator()
        self.__numerator, self.__denominator = new_numerator, new_denominator
        self.reduce()

    def div(self, num2):
        new_numerator = self.__numerator * num2.getDenominator()
        new_denominator = self.__denominator * num2.getNumerator()
        if new_denominator == 0:
            raise ValueError("Division by zero is undefined")
        self.__numerator, self.__denominator = new_numerator, new_denominator
        self.reduce()

    def reduce(self):
        if self.__numerator == 0:
            self.__denominator = 1
            return
        g = self.gcf(abs(self.__numerator), abs(self.__denominator))
        self.__numerator //= g
        self.__denominator //= g
        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator

    def gcf(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __eq__(self, other):
        return self.__numerator == other.getNumerator() and self.__denominator == other.getDenominator()
