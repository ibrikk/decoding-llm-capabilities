# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals
"""
__version__ = 1

def valid_numeral(test_case):
    # Rule 1: Check if the string contains only alphabetic characters
    if not test_case.isalpha():
        return False
    
    # Rule 2: Check if the string contains only valid Roman numeral characters
    roman_numerals = set("IVXLCDM")
    if any(char not in roman_numerals for char in test_case):
        return False
    
    # Rule 3: Check for four of the same character in a row
    for char in "IVXLCDM":
        if char * 4 in test_case:
            return False
    
    # Rule 4: Check ordering of symbols
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = float('inf')
    for char in test_case:
        current_value = value[char]
        if current_value > prev_value:
            # Rule 5 and 6: Check subtraction rules
            if prev_value in {1, 10, 100} and (prev_value * 10 != current_value) and (prev_value * 5 != current_value):
                return False
        prev_value = current_value

    # Rule 7: Check sequences of 2 or 3 symbols in a row
    count = 1
    for i in range(1, len(test_case)):
        if test_case[i] == test_case[i - 1]:
            count += 1
            if count > 3:
                return False
        else:
            count = 1

    return True

def main():
    # Run the test cases
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    print("All tests passed!")

###############################################################

# Here is where you will write your test case functions

def test1():
    # Test for invalid characters
    assert not valid_numeral("M2C"), "Test case 1 failed"
    assert not valid_numeral("ASDF"), "Test case 2 failed"

def test2():
    # Test for valid Roman numeral characters
    assert valid_numeral("XVIII"), "Test case 1 failed"
    assert not valid_numeral("Mxxiv"), "Test case 2 failed"

def test3():
    # Test for invalid numerals with more than 3 of the same character
    assert not valid_numeral("CCCC"), "Test case 1 failed"
    assert not valid_numeral("VV"), "Test case 2 failed"

def test4():
    # Test for valid ordering of symbols
    assert valid_numeral("XIV"), "Test case 1 failed"
    assert not valid_numeral("VL"), "Test case 2 failed"

def test5():
    # Test for valid numeral with subtraction rules
    assert valid_numeral("IX"), "Test case 1 failed"
    assert not valid_numeral("VX"), "Test case 2 failed"

def test6():
    # Test for valid sequences of 2 or 3 symbols in a row
    assert valid_numeral("III"), "Test case 1 failed"
    assert not valid_numeral("VVV"), "Test case 2 failed"

def test7():
    # Test valid and invalid cases together
    assert valid_numeral("MCXIV"), "Test case 1 failed"
    assert not valid_numeral("IL"), "Test case 2 failed"

###############################################################    

if __name__ == "__main__":
    main()
