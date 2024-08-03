# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals
"""
__version__ = 1

def valid_numeral(test_case):
    # Helper function to check if a character is a valid Roman numeral symbol
    def is_valid_symbol(char):
        return char in "IVXLCDM"

    # Helper function to get the value of a Roman numeral symbol
    def symbol_value(char):
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return values.get(char, 0)

    # Rule 1: Check if the string is non-empty and contains only alphabetic characters
    if not test_case or not test_case.isalpha():
        return False

    # Rule 2: Check if the string contains only valid Roman numeral symbols
    if not all(is_valid_symbol(char) for char in test_case):
        return False

    # Rule 3: Check for no more than 3 consecutive identical symbols
    if any(symbol * 4 in test_case for symbol in "IVXLCDM"):
        return False

    # Rules 4-6: Check order and subtraction rules
    prev_value = float('inf')
    for i, char in enumerate(test_case):
        curr_value = symbol_value(char)
        
        if curr_value > prev_value:
            # Check if subtraction is valid
            if prev_value not in [1, 10, 100]:
                return False
            if symbol_value(test_case[i-1]) * 10 < curr_value:
                return False
        
        prev_value = curr_value

    # Rule 7: Check for invalid repetitions of non-power-of-10 symbols
    if any(symbol * 2 in test_case for symbol in "VLD"):
        return False

    return True

def main():
    # Call test cases
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()

# Test cases
def test1():
    assert valid_numeral('XVIII') == True, "Test 1 failed: XVIII should be valid"

def test2():
    assert valid_numeral('MCXIV') == True, "Test 2 failed: MCXIV should be valid"

def test3():
    assert valid_numeral('CCCC') == False, "Test 3 failed: CCCC should be invalid"

def test4():
    assert valid_numeral('CIL') == False, "Test 4 failed: CIL should be invalid"

def test5():
    assert valid_numeral('M2C') == False, "Test 5 failed: M2C should be invalid"

def test6():
    assert valid_numeral('ASDF') == False, "Test 6 failed: ASDF should be invalid"

def test7():
    assert valid_numeral('VL') == False, "Test 7 failed: VL should be invalid"

def test8():
    assert valid_numeral('XXX') == True, "Test 8 failed: XXX should be valid"

def test9():
    assert valid_numeral('LLL') == False, "Test 9 failed: LLL should be invalid"

def test10():
    assert valid_numeral('') == False, "Test 10 failed: Empty string should be invalid"

if __name__ == "__main__":
    main()