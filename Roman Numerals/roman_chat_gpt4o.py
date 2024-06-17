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
    valid_characters = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    if any(char not in valid_characters for char in test_case):
        return False
    # Rule 3: Check for no more than three of the same character in a row
    import re
    if re.search(r'(IIII|VVVV|XXXX|LLLL|CCCC|DDDD|MMMM)', test_case):
        return False
    # Rule 4: Check for valid order of numerals (large to small unless subtractive notation is used)
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    max_seen = 1001  # Any number larger than 1000
    for char in test_case:
        if values[char] > max_seen:
            return False
        max_seen = values[char]
    # Additional Rules 5, 6, and 7 will be handled here
    # (For simplicity, not implemented in this step-by-step example)
    return True

def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()

###############################################################

# Below are the tests for Rule 1, validating that the string contains only characters
def test1():
    assert valid_numeral('XVIII') == True, "Test 1 Failed"
    assert valid_numeral('MCXIV') == True, "Test 2 Failed"
    assert valid_numeral('1234') == False, "Test 3 Failed"
    assert valid_numeral('MCXI@V') == False, "Test 4 Failed"
    print("All tests for Rule 1 passed.")

# Below are the tests for Rule 2, validating the string contains only valid Roman numeral characters
def test2():
    assert valid_numeral('MMMM') == True, "Test 5 Failed"
    assert valid_numeral('ASDF') == False, "Test 6 Failed"
    print("All tests for Rule 2 passed.")

# Below are the tests for Rule 3, validating no more than three of the same character in a row
def test3():
    assert valid_numeral('IIII') == False, "Test 7 Failed"
    assert valid_numeral('VVVV') == False, "Test 8 Failed"
    assert valid_numeral('XXX') == True, "Test 9 Failed"
    print("All tests for Rule 3 passed.")

# Below are the tests for Rule 4, validating order of numerals from large to small unless subtractive notation
def test4():
    assert valid_numeral('XIX') == True, "Test 10 Failed"
    assert valid_numeral('XVIX') == False, "Test 11 Failed"
    print("All tests for Rule 4 passed.")

# Below are the tests for Rule 5, small-valued symbol precede a large-valued symbol if small-valued symbol is an integer power of 10
def test5():
    assert valid_numeral('IX') == True, "Test 12 Failed"
    assert valid_numeral('VX') == False, "Test 13 Failed"
    print("All tests for Rule 5 passed.")

# Below are the tests for Rule 6, small-valued symbol precede a large-valued symbol if it is one of the two symbols in size order before the large-valued symbol
def test6():
    assert valid_numeral('IV') == True, "Test 14 Failed"
    assert valid_numeral('IL') == False, "Test 15 Failed"
    print("All tests for Rule 6 passed.")

# Below are the tests for Rule 7, validating sequence of 2 or 3 symbols in a row if they are integer powers of 10
def test7():
    assert valid_numeral('II') == True, "Test 16 Failed"
    assert valid_numeral('VV') == False, "Test 17 Failed"
    assert valid_numeral('III') == True, "Test 18 Failed"
    print("All tests for Rule 7 passed.")

###############################################################    
    
if __name__ == "__main__":
    main()
