# -*- coding: utf-8 -*-
"""Detect valid Roman numerals"""
__version__ = 1

import string

def valid_numeral(test_case):
    """
    Checks if the given string is a valid Roman numeral.
    
    Args:
        test_case (str): The Roman numeral to be validated.
        
    Returns:
        bool: True if the input is a valid Roman numeral, False otherwise.
    """
    # Rule 1: A valid Roman numeral consists only of alphabetic characters
    if not all(char in string.ascii_uppercase for char in test_case):
        return False
    
    # Rule 2: A valid Roman numeral only contains the characters I, V, X, L, C, D, and M
    valid_chars = set('IVXLCDM')
    if not all(char in valid_chars for char in test_case):
        return False
    
    # Rule 3: A valid Roman numeral should not have 4 of the same character in a row
    for char in valid_chars:
        if char * 4 in test_case:
            return False
    
    # Rule 4: A valid Roman numeral should be ordered from large-valued symbol to small-valued symbol
    # Unless...
    
    # Rule 5: A valid Roman numeral can have a small-valued symbol precede a large-valued symbol,
    # only if the small-valued symbol is an integer power of 10
    power_of_ten = {'I': 1, 'X': 10, 'C': 100, 'M': 1000}
    for i in range(len(test_case) - 1):
        if power_of_ten.get(test_case[i], 0) >= power_of_ten.get(test_case[i+1], 0):
            continue
        if test_case[i] not in power_of_ten or test_case[i+1] not in power_of_ten:
            return False
    
    # Rule 6: A valid Roman numeral can have a small-valued symbol precede a large-valued symbol,
    # only if the small-valued symbol is an integer power of 10 AND the small-valued symbol is
    # one of the two symbols in size order before the large-valued symbol
    for i in range(len(test_case) - 2):
        if power_of_ten.get(test_case[i], 0) >= power_of_ten.get(test_case[i+1], 0) >= power_of_ten.get(test_case[i+2], 0):
            continue
        if test_case[i] not in 'IV' or test_case[i+1] not in 'XC' or test_case[i+2] not in 'MD':
            return False
    
    # Rule 7: A valid Roman numeral can have a sequence of 2 or 3 symbols in a row if they are integer powers of 10,
    # but not otherwise
    for i in range(len(test_case) - 1):
        if power_of_ten.get(test_case[i], 0) >= power_of_ten.get(test_case[i+1], 0):
            continue
        if power_of_ten.get(test_case[i], 0) * power_of_ten.get(test_case[i+1], 0) not in [1, 10, 100, 1000]:
            return False
    
    return True

def main():
    # Here is where you will call your test cases
    print(valid_numeral('XVIII'))  # True
    print(valid_numeral('MCXIV'))  # True
    print(valid_numeral('CCCC'))   # False
    print(valid_numeral('CIL'))    # False

if __name__ == "__main__":
    main()