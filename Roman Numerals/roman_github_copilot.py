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
    valid_chars = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    if not all(char in valid_chars for char in test_case):
        return False
    
    # Rule 3: Check if the string has 4 of the same character in a row
    if any(test_case[i] == test_case[i+1] == test_case[i+2] == test_case[i+3] for i in range(len(test_case) - 3)):
        return False
    
    # Rule 4-6: Check the order and subtraction rules
    value_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = float('inf')
    for i, char in enumerate(test_case):
        current_value = value_map[char]
        if current_value > prev_value:
            # Rule 5: Check if the small-valued symbol is an integer power of 10
            if prev_value not in {1, 10, 100}:
                return False
            # Rule 6: Check if the small-valued symbol is one of the two symbols in size order before the large-valued symbol
            if not (prev_value == current_value / 10 or prev_value == current_value / 5):
                return False
        prev_value = current_value
    
    # Rule 7: Check if there are sequences of 2 or 3 symbols in a row if they are integer powers of 10
    for i in range(len(test_case) - 1):
        if test_case[i] == test_case[i+1]:
            if test_case[i] not in {'I', 'X', 'C', 'M'}:
                return False
            if i + 2 < len(test_case) and test_case[i] == test_case[i+2]:
                if i + 3 < len(test_case) and test_case[i] == test_case[i+3]:
                    return False
    
    return True

def main():
    # Call each test function and print the results
    print("Test 1:", test1())
    print("Test 2:", test2())
    print("Test N:", testN())

###############################################################

# Here is where you will write your test case functions

# Below are the tests for Rule 1, validating that the string contains only characters
def test1():
    # Test cases for Rule 1
    assert valid_numeral('XVIII') == True
    assert valid_numeral('MCXIV') == True
    assert valid_numeral('1234') == False
    assert valid_numeral('') == False
    return "Rule 1 tests passed"

def test2():
    # Test cases for Rule 2
    assert valid_numeral('XVIII') == True
    assert valid_numeral('MCXIV') == True
    assert valid_numeral('ASDF') == False
    assert valid_numeral('IIII') == False
    return "Rule 2 tests passed"

# Below are the tests for Rule N, .....
def testN():
    # Test cases for Rule 3-7
    assert valid_numeral('IIII') == False
    assert valid_numeral('VVVV') == False
    assert valid_numeral('IL') == False
    assert valid_numeral('IC') == False
    assert valid_numeral('XLIX') == True
    assert valid_numeral('XXX') == True
    assert valid_numeral('LLL') == False
    return "Rule 3-7 tests passed"

###############################################################    

if __name__ == "__main__":
    main()