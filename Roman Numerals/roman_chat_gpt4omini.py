# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals
"""
__version__ = 1

def valid_numeral(test_case):
    if not is_alpha(test_case):
        return False
    if not only_valid_chars(test_case):
        return False
    if has_four_consecutive_same_chars(test_case):
        return False
    if not ordered_large_to_small(test_case):
        if not valid_subtractives(test_case):
            return False
    if has_invalid_repeats(test_case):
        return False
    return True

def is_alpha(s):
    """Check if the string contains only alphabetic characters"""
    return s.isalpha()

def only_valid_chars(s):
    """Check if the string contains only valid Roman numeral characters"""
    valid_chars = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    return all(char in valid_chars for char in s)

def has_four_consecutive_same_chars(s):
    """Check if there are four consecutive identical characters"""
    for i in range(len(s) - 3):
        if s[i] == s[i+1] == s[i+2] == s[i+3]:
            return True
    return False

def ordered_large_to_small(s):
    """Check if the string is ordered from large-valued symbol to small-valued symbol"""
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = float('inf')
    for char in s:
        current_value = values[char]
        if current_value > prev_value:
            return False
        prev_value = current_value
    return True

def valid_subtractives(s):
    """Check if the subtractive notation is valid"""
    subtractive_pairs = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
    i = 0
    while i < len(s) - 1:
        if s[i:i+2] in subtractive_pairs:
            if not is_valid_subtractive(s[i:i+2]):
                return False
            i += 2
        else:
            i += 1
    return True

def is_valid_subtractive(pair):
    """Check if the subtractive pair is valid"""
    valid_pairs = {'IV': '5-1', 'IX': '10-1', 'XL': '50-10', 'XC': '100-10', 'CD': '500-100', 'CM': '1000-100'}
    return pair in valid_pairs

def has_invalid_repeats(s):
    """Check for invalid sequences of 2 or 3 symbols in a row"""
    invalid_sequences = {'VV', 'LL', 'DD', 'VVV', 'LLL', 'DDD'}
    for seq in invalid_sequences:
        if seq in s:
            return True
    return False

def main():
    # Here is where you will call your test cases
    test1()
    test2()
    # Add calls to other test functions here

###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for Rule 1, validating that the string contains only characters
def test1():
    assert valid_numeral('XVIII') == True, "Test case test1 failed"
    assert valid_numeral('1234') == False, "Test case test1 failed"
    assert valid_numeral('MCM') == True, "Test case test1 failed"
    assert valid_numeral('MCM!') == False, "Test case test1 failed"

def test2():
    # Below are the tests for Rule 2, only valid Roman numeral characters
    assert valid_numeral('XVII') == True, "Test case test2 failed"
    assert valid_numeral('XIIIi') == False, "Test case test2 failed"
    assert valid_numeral('IXV') == True, "Test case test2 failed"
    assert valid_numeral('Xo') == False, "Test case test2 failed"

# Add tests for remaining rules here
# def test3():
#     # Below are the tests for Rule 3, no four consecutive identical characters
#     assert valid_numeral('IIII') == False, "Test case test3 failed"
#     assert valid_numeral('XXI') == True, "Test case test3 failed"
#     assert valid_numeral('XXX') == True, "Test case test3 failed"
#     assert valid_numeral('XXXX') == False, "Test case test3 failed"

# def test4():
#     # Below are the tests for Rule 4, correct ordering of symbols
#     assert valid_numeral('XV') == True, "Test case test4 failed"
#     assert valid_numeral('VIX') == False, "Test case test4 failed"
#     assert valid_numeral('MCM') == True, "Test case test4 failed"
#     assert valid_numeral('IC') == False, "Test case test4 failed"

# def test5():
#     # Below are the tests for Rule 5, correct use of subtractive notation
#     assert valid_numeral('IX') == True, "Test case test5 failed"
#     assert valid_numeral('VX') == False, "Test case test5 failed"
#     assert valid_numeral('IV') == True, "Test case test5 failed"
#     assert valid_numeral('IL') == False, "Test case test5 failed"

# def test6():
#     # Below are the tests for Rule 6, small-valued symbol precedes larger ones
#     assert valid_numeral('XL') == True, "Test case test6 failed"
#     assert valid_numeral('IC') == False, "Test case test6 failed"
#     assert valid_numeral('XC') == True, "Test case test6 failed"
#     assert valid_numeral('IL') == False, "Test case test6 failed"

# def test7():
#     # Below are the tests for Rule 7, invalid sequences of 2 or 3 symbols in a row
#     assert valid_numeral('XXX') == True, "Test case test7 failed"
#     assert valid_numeral('LLL') == False, "Test case test7 failed"
#     assert valid_numeral('VV') == False, "Test case test7 failed"
#     assert valid_numeral('MMM') == True, "Test case test7 failed"
    
###############################################################    

if __name__ == "__main__":
    main()
