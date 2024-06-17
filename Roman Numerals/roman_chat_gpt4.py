# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: YOUR NAME HERE
"""
__version__ = 1

def valid_numeral(test_case):
    # Rule 1: Check for only alphabetic characters
    if not test_case.isalpha():
        return False
    
    # Rule 2: Check for valid Roman numeral characters
    for char in test_case:
        if char not in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
            return False
    
    # Rule 3: No more than three of the same character in a row
    count = 1
    for i in range(1, len(test_case)):
        if test_case[i] == test_case[i - 1]:
            count += 1
            if count > 3:
                return False
        else:
            count = 1
    
    # Rule 4-7: Handling ordering and subtraction exceptions
    # Convert Roman numerals to values for easier processing
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    previous_value = 0
    for char in reversed(test_case):
        value = values[char]
        if value < previous_value:
            # Rule 5 & 6: Check if subtraction is valid
            if previous_value not in [value * 5, value * 10]:
                return False
        previous_value = value
    
    return True


def main():
    # Here is where you will call your test cases
    print(valid_numeral("XVIII"))  # True
    print(valid_numeral("MCXIV"))  # True
    print(valid_numeral("CCCC"))   # False
    print(valid_numeral("CIL"))    # False
    print(valid_numeral("M2C"))    # False
    print(valid_numeral("ASDF"))   # False
    print(valid_numeral("VL"))     # False
    print(valid_numeral("XXX"))    # True
    print(valid_numeral("LLL"))    # False

###############################################################    

# The test functions are demonstrated in the main function rather than as separate functions
# This approach keeps the example concise and focused on the validation logic

if __name__ == "__main__":
    main()    
