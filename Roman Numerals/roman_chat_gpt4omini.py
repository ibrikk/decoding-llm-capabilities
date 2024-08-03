# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals
"""
__version__ = 1

# Define the valid Roman numeral symbols and their values
ROMAN_VALUES = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# Define valid Roman numeral rules
def valid_numeral(test_case):
    # Rule 1: Only alphabetic characters (no empty strings)
    if not test_case.isalpha() or not test_case:
        return False

    # Rule 2: Only contains valid Roman numeral characters
    if any(char not in ROMAN_VALUES for char in test_case):
        return False

    # Rule 3: No more than three of the same character in a row
    for char in ROMAN_VALUES.keys():
        if char * 4 in test_case:
            return False

    # Rule 4: Valid ordering from large to small
    # Rule 5 & 6: Valid subtraction rules
    i = 0
    while i < len(test_case):
        if i + 1 < len(test_case):
            current_value = ROMAN_VALUES[test_case[i]]
            next_value = ROMAN_VALUES[test_case[i + 1]]
            if current_value < next_value:
                # Rule 6: Valid subtraction rule
                if not (current_value in [1, 10] and next_value in [5, 50]) and \
                   not (current_value in [10, 100] and next_value in [50, 500]) and \
                   not (current_value in [100, 1000] and next_value in [500, 1000]):
                    return False
            elif current_value == next_value:
                # Rule 7: Valid sequence of 2 or 3 symbols
                if i + 2 < len(test_case) and test_case[i + 2] == test_case[i]:
                    if not (current_value in [1, 10, 100]):
                        return False
        i += 1

    return True

def main():
    # Test cases for Rule 1: Only alphabetic characters
    print("Rule 1 Tests:")
    assert valid_numeral('XVIII') == True, "Test 1 Failed"
    assert valid_numeral('MCXIV') == True, "Test 2 Failed"
    assert valid_numeral('M2C') == False, "Test 3 Failed"
    assert valid_numeral('ASDF') == False, "Test 4 Failed"
    print("Rule 1 Tests Passed")

    # Test cases for Rule 2: Valid Roman numeral characters
    print("Rule 2 Tests:")
    assert valid_numeral('XVIII') == True, "Test 5 Failed"
    assert valid_numeral('VV') == False, "Test 6 Failed"
    print("Rule 2 Tests Passed")

    # Test cases for Rule 3: No more than three of the same character in a row
    print("Rule 3 Tests:")
    assert valid_numeral('III') == True, "Test 7 Failed"
    assert valid_numeral('IIII') == False, "Test 8 Failed"
    print("Rule 3 Tests Passed")

    # Test cases for Rule 4 & 5 & 6: Valid ordering and subtraction rules
    print("Rules 4, 5, 6 Tests:")
    assert valid_numeral('IX') == True, "Test 9 Failed"
    assert valid_numeral('XL') == True, "Test 10 Failed"
    assert valid_numeral('IL') == False, "Test 11 Failed"
    assert valid_numeral('VV') == False, "Test 12 Failed"
    print("Rules 4, 5, 6 Tests Passed")

    # Test cases for Rule 7: Valid sequences of 2 or 3 symbols
    print("Rule 7 Tests:")
    assert valid_numeral('XXX') == True, "Test 13 Failed"
    assert valid_numeral('LLL') == False, "Test 14 Failed"
    print("Rule 7 Tests Passed")

if __name__ == "__main__":
    main()
