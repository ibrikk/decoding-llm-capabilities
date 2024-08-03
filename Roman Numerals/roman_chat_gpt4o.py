# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals
"""
__version__ = 1

def valid_numeral(test_case):
    # Helper function to validate the characters in the Roman numeral
    def valid_characters(numeral):
        valid_chars = set("IVXLCDM")
        return all(char in valid_chars for char in numeral)
    
    # Helper function to check for no more than three of the same character in a row
    def no_four_in_a_row(numeral):
        previous_char = ''
        count = 0
        for char in numeral:
            if char == previous_char:
                count += 1
                if count == 4:
                    return False
            else:
                previous_char = char
                count = 1
        return True

    # Helper function to ensure proper ordering and rules for subtraction
    def valid_order(numeral):
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev_value = float('inf')
        for i in range(len(numeral)):
            current_value = values[numeral[i]]
            if current_value > prev_value:
                # Validating if subtraction is correct
                if prev_value in [1, 10, 100] and (prev_value * 10 >= current_value <= prev_value * 10):
                    pass
                else:
                    return False
            prev_value = current_value
        return True

    # Applying the rules
    if not test_case.isalpha():
        return False  # Rule 1
    if not valid_characters(test_case):
        return False  # Rule 2
    if not no_four_in_a_row(test_case):
        return False  # Rule 3
    if not valid_order(test_case):
        return False  # Rules 4-7
    
    return True

def main():
    # Calling the test cases
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
    test11()

###############################################################

# Here are the test case functions

# Below are the tests for Rule 1, validating that the string contains only characters
def test1():
    assert valid_numeral("XVIII") == True
    assert valid_numeral("MCXIV") == True
    assert valid_numeral("M2C") == False
    assert valid_numeral("ASDF") == False
    print("Test 1 passed")

# Below are the tests for Rule 2, ensuring only valid characters are present
def test2():
    assert valid_numeral("XVIII") == True
    assert valid_numeral("MCXIV") == True
    assert valid_numeral("abcd") == False
    assert valid_numeral("XIVM") == True
    print("Test 2 passed")

# Below are the tests for Rule 3, no more than three of the same character in a row
def test3():
    assert valid_numeral("XIIII") == False
    assert valid_numeral("XXXX") == False
    assert valid_numeral("MMMM") == False
    assert valid_numeral("CCC") == True
    print("Test 3 passed")

# Below are the tests for Rule 4, ensuring proper order of numerals
def test4():
    assert valid_numeral("XIX") == True
    assert valid_numeral("XVVX") == False
    assert valid_numeral("LLL") == False
    assert valid_numeral("XL") == True
    print("Test 4 passed")

# Below are the tests for Rule 5, valid small preceding large symbols
def test5():
    assert valid_numeral("IV") == True
    assert valid_numeral("IX") == True
    assert valid_numeral("IL") == False
    assert valid_numeral("IC") == False
    print("Test 5 passed")

# Below are the tests for Rule 6, ensuring valid subtraction rules
def test6():
    assert valid_numeral("IV") == True
    assert valid_numeral("IX") == True
    assert valid_numeral("IL") == False
    assert valid_numeral("IC") == False
    print("Test 6 passed")

# Below are the tests for Rule 7, ensuring sequences of 2 or 3 symbols in a row if they are integer powers of 10
def test7():
    assert valid_numeral("II") == True
    assert valid_numeral("III") == True
    assert valid_numeral("VV") == False
    assert valid_numeral("VVV") == False
    print("Test 7 passed")

# Additional tests for overall validation
def test8():
    assert valid_numeral("XVIII") == True
    assert valid_numeral("MCXIV") == True
    assert valid_numeral("CCCC") == False
    assert valid_numeral("CIL") == False
    print("Test 8 passed")

def test9():
    assert valid_numeral("MCMXCIV") == True  # 1994
    assert valid_numeral("MMMCMXCIX") == True  # 3999
    assert valid_numeral("IIII") == False
    assert valid_numeral("VX") == False
    print("Test 9 passed")

def test10():
    assert valid_numeral("") == False  # empty string
    assert valid_numeral("MCMIV") == True  # 1904
    assert valid_numeral("IC") == False
    assert valid_numeral("XXC") == False
    print("Test 10 passed")

def test11():
    assert valid_numeral("MMMDCCCLXXXVIII") == True  # 3888
    assert valid_numeral("MMMCMXC") == True  # 3990
    assert valid_numeral("IXX") == False
    assert valid_numeral("MMMM") == False
    print("Test 11 passed")

###############################################################    

if __name__ == "__main__":
    main() 
