# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals
"""
__version__ = 1

def valid_numeral(test_case):
    # Roman numeral value map
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Rule 1: A valid Roman numeral must be a non-empty string consisting only of the Roman characters
    if not test_case or not all(char in roman_values for char in test_case):
        return False
    
    # Rule 2: All characters should be uppercase Roman numeral letters
    if any(char not in roman_values for char in test_case):
        return False
    
    # Convert the Roman numeral to a list of values
    values = [roman_values[char] for char in test_case]
    
    # Rule 3: No more than three of the same character in a row
    for i in range(len(values) - 3):
        if values[i] == values[i+1] == values[i+2] == values[i+3]:
            return False

    # Rule 4, 5, 6, 7: Ordering and valid subtractive combinations
    for i in range(len(values) - 1):
        if values[i] < values[i + 1]:
            # Rule 6: Only powers of 10 can precede larger symbols
            if test_case[i] not in {'I', 'X', 'C'}:
                return False
            # Rule 5 & 6: Valid preceding rules
            if values[i] * 10 < values[i + 1]:
                return False

    return True

def main():
    # This is where we will call test cases
    test_cases()

def test_cases():
    # Test cases for the rules
    assert valid_numeral('XVIII') == True, "Test failed for XVIII"
    assert valid_numeral('MCXIV') == True, "Test failed for MCXIV"
    assert valid_numeral('CCCC') == False, "Test failed for CCCC"
    assert valid_numeral('CIL') == False, "Test failed for CIL"
    assert valid_numeral('M2C') == False, "Test failed for M2C"
    assert valid_numeral('ASDF') == False, "Test failed for ASDF"
    assert valid_numeral('VL') == False, "Test failed for VL"
    assert valid_numeral('XXX') == True, "Test failed for XXX"
    assert valid_numeral('LLL') == False, "Test failed for LLL"

    print("All tests passed!")

if __name__ == "__main__":
    main()
