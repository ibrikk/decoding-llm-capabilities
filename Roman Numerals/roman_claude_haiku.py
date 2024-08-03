# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals
"""
__version__ = 1

def valid_numeral(test_case):
    """
    Determines if the given string is a valid Roman numeral.
    
    Args:
        test_case (str): The Roman numeral to be tested.
    
    Returns:
        bool: True if the input is a valid Roman numeral, False otherwise.
    """
    # Rule 1: A valid Roman numeral consists only of alphabetic characters
    if not test_case.isalpha():
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
    #         only if the small-valued symbol is an integer power of 10
    # Rule 6: A valid Roman numeral can have a small-valued symbol precede a large-valued symbol, 
    #         only if the small-valued symbol is an integer power of 10 AND the small-valued symbol 
    #         is one of the two symbols in size order before the large-valued symbol
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = float('inf')
    for char in test_case:
        current_value = values[char]
        if current_value < prev_value and (current_value not in (1, 10, 100) or
                                        values[test_case[test_case.index(char)-1]] not in (1, 10, 100, current_value/10)):
            return False
        prev_value = current_value
    
    # Rule 7: A valid Roman number can have a sequence of 2 or 3 symbols in a row 
    #         if they are integer powers of 10, but not otherwise
    for i in range(len(test_case)-1):
        if test_case[i:i+2] in ('II', 'III', 'XX', 'XXX', 'CC', 'CCC', 'MM', 'MMM'):
            continue
        if test_case[i:i+3] in ('IV', 'IX', 'XL', 'XC', 'CD', 'CM'):
            continue
        return False
    
    return True

def main():
    # Here is where you will call your test cases
    print(valid_numeral('XVIII'))  # True
    print(valid_numeral('MCXIV'))  # True
    print(valid_numeral('CCCC'))   # False
    print(valid_numeral('CIL'))    # False

###############################################################

# Here is where you will write your test case functions
def test1():
    """
    Test that the function rejects non-alphabetic characters.
    """
    assert not valid_numeral('12')
    assert not valid_numeral('I2V')
    assert not valid_numeral('I V')

def test2():
    """
    Test that the function rejects characters outside the valid set.
    """
    assert not valid_numeral('IVXLCDMJ')
    assert not valid_numeral('ivxlcdm')

def test3():
    """
    Test that the function rejects more than 3 consecutive occurrences of the same character.
    """
    assert not valid_numeral('IIII')
    assert not valid_numeral('XXXX')
    assert not valid_numeral('CCCC')
    assert not valid_numeral('MMMM')

def test4():
    """
    Test that the function accepts valid Roman numerals in ascending order.
    """
    assert valid_numeral('I')
    assert valid_numeral('II')
    assert valid_numeral('III')
    assert valid_numeral('IV')
    assert valid_numeral('V')
    assert valid_numeral('VI')
    assert valid_numeral('VII')
    assert valid_numeral('VIII')
    assert valid_numeral('IX')
    assert valid_numeral('X')
    assert valid_numeral('XI')
    assert valid_numeral('XII')
    assert valid_numeral('XIII')
    assert valid_numeral('XIV')
    assert valid_numeral('XV')

def test5():
    """
    Test that the function accepts valid Roman numerals with a smaller-valued symbol preceding a larger-valued symbol.
    """
    assert valid_numeral('IV')
    assert valid_numeral('IX')
    assert valid_numeral('XL')
    assert valid_numeral('XC')
    assert valid_numeral('CD')
    assert valid_numeral('CM')

def test6():
    """
    Test that the function rejects invalid Roman numerals with a smaller-valued symbol preceding a larger-valued symbol.
    """
    assert not valid_numeral('IL')
    assert not valid_numeral('IC')
    assert not valid_numeral('VX')
    assert not valid_numeral('IIX')

def test7():
    """
    Test that the function accepts valid sequences of 2 or 3 symbols that are integer powers of 10.
    """
    assert valid_numeral('II')
    assert valid_numeral('III')
    assert valid_numeral('XX')
    assert valid_numeral('XXX')
    assert valid_numeral('CC')
    assert valid_numeral('CCC')
    assert valid_numeral('MM')
    assert valid_numeral('MMM')

def test8():
    """
    Test that the function rejects invalid sequences of 2 or 3 symbols that are not integer powers of 10.
    """
    assert not valid_numeral('VV')
    assert not valid_numeral('VVV')
    assert not valid_numeral('IIV')
    assert not valid_numeral('IIC')

###############################################################    
    
if __name__ == "__main__":
    main()
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()