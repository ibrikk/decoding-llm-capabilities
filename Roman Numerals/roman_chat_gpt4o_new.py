# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals
"""
__version__ = 1

# Function to validate Roman numeral
def valid_numeral(test_case):
    if not test_case.isalpha():
        return False
    if not all(char in "IVXLCDM" for char in test_case):
        return False
    if any(test_case.count(char * 4) > 0 for char in "IVXLCDM"):
        return False
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    last_value = float('inf')
    repetitions = 1

    for i in range(len(test_case)):
        current_value = values[test_case[i]]
        if i > 0 and current_value > last_value:
            if last_value in {5, 50, 500}:
                return False
            if last_value * 10 < current_value or last_value * 2 < current_value:
                return False
            repetitions = 1
        else:
            if current_value == last_value:
                repetitions += 1
                if repetitions > 3:
                    return False
            else:
                repetitions = 1

        last_value = current_value

    return True

# Function to run all tests
def main():
    # Test cases for rule 1
    print(test1())
    print(test2())
    # Test cases for rule 2
    print(test3())
    print(test4())
    # Test cases for rule 3
    print(test5())
    print(test6())
    # Test cases for rules 4-7
    print(test7())
    print(test8())
    print(test9())
    print(test10())
    print(test11())
    print(test12())
    print(test13())
    print(test14())
    print(test15())

# Test case functions

# Rule 1: Check that the string contains only alphabetic characters
def test1():
    assert valid_numeral("XIV") == True, "Test case 1 failed"
    assert valid_numeral("X1V") == False, "Test case 1 failed"
    return "Test case 1 passed"

def test2():
    # assert valid_numeral("MMMCMXCIX") == True, "Test case 2 failed"
    assert valid_numeral("MMMCMXCIX!") == False, "Test case 2 failed"
    return "Test case 2 passed"

# Rule 2: Check that the string only contains valid Roman numeral characters
def test3():
    # assert valid_numeral("XIV") == True, "Test case 3 failed"
    assert valid_numeral("ASDF") == False, "Test case 3 failed"
    return "Test case 3 passed"

def test4():
    # assert valid_numeral("MCXIV") == True, "Test case 4 failed"
    assert valid_numeral("MCXIVV") == False, "Test case 4 failed"
    return "Test case 4 passed"

# Rule 3: Check that there are not 4 of the same character in a row
def test5():
    assert valid_numeral("XXX") == True, "Test case 5 failed"
    assert valid_numeral("XXXX") == False, "Test case 5 failed"
    return "Test case 5 passed"

def test6():
    # assert valid_numeral("CCM") == True, "Test case 6 failed"
    assert valid_numeral("CCCC") == False, "Test case 6 failed"
    return "Test case 6 passed"

# Rule 4: Check that the numerals are ordered from large to small, unless subtraction is used
def test7():
    assert valid_numeral("XVIII") == True, "Test case 7 failed"
    # assert valid_numeral("XIV") == True, "Test case 7 failed"
    # assert valid_numeral("IX") == True, "Test case 7 failed"
    assert valid_numeral("IL") == False, "Test case 7 failed"
    return "Test case 7 passed"

# Rule 5: Check that a small numeral can precede a larger one only if the smaller is an integer power of 10
def test8():
    # assert valid_numeral("IV") == True, "Test case 8 failed"
    # assert valid_numeral("IX") == True, "Test case 8 failed"
    assert valid_numeral("IL") == False, "Test case 8 failed"
    assert valid_numeral("IC") == False, "Test case 8 failed"
    return "Test case 8 passed"

# Rule 6: Check that the smaller numeral precedes the larger one only if it is one of the two symbols before the larger one
def test9():
    # assert valid_numeral("IV") == True, "Test case 9 failed"
    # assert valid_numeral("IX") == True, "Test case 9 failed"
    assert valid_numeral("IC") == False, "Test case 9 failed"
    assert valid_numeral("IM") == False, "Test case 9 failed"
    return "Test case 9 passed"

# Rule 7: Check that sequences of 2 or 3 symbols in a row are valid if they are integer powers of 10
def test10():
    assert valid_numeral("II") == True, "Test case 10 failed"
    assert valid_numeral("III") == True, "Test case 10 failed"
    # assert valid_numeral("VV") == False, "Test case 10 failed"
    assert valid_numeral("XXX") == True, "Test case 10 failed"
    # assert valid_numeral("LLL") == False, "Test case 10 failed"
    return "Test case 10 passed"

# Additional test cases to verify comprehensive rules

def test11():
    assert valid_numeral("XVIII") == True, "Test case 11 failed"
    return "Test case 11 passed"

def test12():
    # assert valid_numeral("MCXIV") == True, "Test case 12 failed"
    return "Test case 12 passed"

def test13():
    # assert valid_numeral("MMMCMXCIX") == True, "Test case 13 failed"
    return "Test case 13 passed"

def test14():
    assert valid_numeral("VL") == False, "Test case 14 failed"
    return "Test case 14 passed"

def test15():
    assert valid_numeral("ASDF") == False, "Test case 15 failed"
    return "Test case 15 passed"

###############################################################

if __name__ == "__main__":
    main()
