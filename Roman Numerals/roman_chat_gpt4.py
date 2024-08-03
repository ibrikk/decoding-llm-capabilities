# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals
"""

__version__ = 1

def valid_numeral(test_case):
    # Rule 1: Roman numeral must contain only valid Roman characters
    if not all(char in 'IVXLCDM' for char in test_case):
        return False
    
    # Rule 3: No four identical characters in a row
    if 'IIII' in test_case or 'VVVV' in test_case or 'XXXX' in test_case or 'LLLL' in test_case or 'CCCC' in test_case or 'DDDD' in test_case or 'MMMM' in test_case:
        return False
    
    # Rules for ordering and subtractive combination
    # Rule 4, 5, 6: Correct order and valid subtractive combinations
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    previous_value = 0
    total = 0
    for char in reversed(test_case):
        value = roman_values[char]
        if value >= previous_value:
            total += value
        else:
            if char in ('I', 'X', 'C') and previous_value in (5*value, 10*value):
                total -= value
            else:
                return False
        previous_value = value
    
    return True

def main():
    # Test cases are run from here
    print("Test Case 1 (XVIII):", valid_numeral('XVIII'))
    print("Test Case 2 (MCXIV):", valid_numeral('MCXIV'))
    print("Test Case 3 (CCCC):", valid_numeral('CCCC'))
    print("Test Case 4 (CIL):", valid_numeral('CIL'))
    print("Test Case 5 (M2C):", valid_numeral('M2C'))
    print("Test Case 6 (ASDF):", valid_numeral('ASDF'))
    print("Test Case 7 (VL):", valid_numeral('VL'))
    print("Test Case 8 (XXX):", valid_numeral('XXX'))
    print("Test Case 9 (LLL):", valid_numeral('LLL'))

if __name__ == "__main__":
    main()
