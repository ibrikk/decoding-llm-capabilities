# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals
"""
__version__ = 1

def valid_numeral(test_case):
    # Rule 1: A valid Roman numeral consists only of alphabetic characters
    if not test_case.isalpha():
        return False
    
    # Rule 2: A valid Roman numeral only contains the characters I, V, X, L, C, D, and M
    valid_chars = set("IVXLCDM")
    if not all(char in valid_chars for char in test_case):
        return False
    
    # Rule 3: A valid Roman numeral should not have 4 of the same character in a row
    for char in valid_chars:
        if char * 4 in test_case:
            return False
    
    # Rule 4, 5, 6, 7: Detailed validity check with respect to ordering and repetition
    # Create a mapping of Roman numeral symbols to their integer values
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Convert the Roman numeral to a list of integers
    values = [roman_to_int[char] for char in test_case]
    
    # Check for valid ordering and repetition
    i = 0
    while i < len(values):
        if i < len(values) - 1 and values[i] < values[i + 1]:
            # Check for valid subtractive combinations
            if values[i] in [1, 10, 100]:
                if values[i + 1] > 10 * values[i] or (values[i + 1] != 5 * values[i] and values[i + 1] != 10 * values[i]):
                    return False
            else:
                return False
            i += 2
        else:
            # Check for no more than 3 of the same character in a row
            count = 1
            while i + 1 < len(values) and values[i] == values[i + 1]:
                count += 1
                i += 1
            if count > 3:
                return False
            i += 1
    
    return True


def main():
    # Here is where you will call your test cases
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
    test12()
    print("All tests passed.")


###############################################################

# Here is where you will write your test case functions

def test1():
    # Rule 1: Test for non-alphabetic characters
    assert not valid_numeral('MCXIV2'), "Failed test1: Non-alphabetic character"
    assert not valid_numeral('!MCXIV'), "Failed test1: Non-alphabetic character"
    assert not valid_numeral('MCX IV'), "Failed test1: Space in input"
    assert not valid_numeral(''), "Failed test1: Empty string"
    print("Passed test1")

def test2():
    # Rule 2: Test for valid characters
    assert not valid_numeral('MCXIVQ'), "Failed test2: Invalid character"
    assert not valid_numeral('ASDF'), "Failed test2: Completely invalid characters"
    assert valid_numeral('MCXIV'), "Failed test2: Valid numeral"
    print("Passed test2")

def test3():
    # Rule 3: Test for no more than 3 of the same character in a row
    assert not valid_numeral('IIII'), "Failed test3: Four 'I's in a row"
    assert not valid_numeral('XXXX'), "Failed test3: Four 'X's in a row"
    assert not valid_numeral('CCCC'), "Failed test3: Four 'C's in a row"
    assert valid_numeral('XXX'), "Failed test3: Three 'X's in a row"
    assert valid_numeral('CC'), "Failed test3: Two 'C's in a row"
    print("Passed test3")

def test4():
    # Rule 4: Test for correct ordering
    assert not valid_numeral('IVX'), "Failed test4: Invalid ordering"
    assert not valid_numeral('IIV'), "Failed test4: Invalid ordering"
    assert valid_numeral('VI'), "Failed test4: Valid ordering"
    assert valid_numeral('XI'), "Failed test4: Valid ordering"
    print("Passed test4")

def test5():
    # Rule 5: Test for subtractive combinations
    assert not valid_numeral('VX'), "Failed test5: Invalid subtractive combination"
    assert not valid_numeral('IC'), "Failed test5: Invalid subtractive combination"
    assert valid_numeral('IV'), "Failed test5: Valid subtractive combination"
    assert valid_numeral('IX'), "Failed test5: Valid subtractive combination"
    print("Passed test5")

def test6():
    # Rule 6: Test for small-valued symbols preceding a large-valued symbol
    assert not valid_numeral('IL'), "Failed test6: Invalid small-before-large combination"
    assert not valid_numeral('IC'), "Failed test6: Invalid small-before-large combination"
    assert valid_numeral('XLIX'), "Failed test6: Valid small-before-large combination"
    assert valid_numeral('XC'), "Failed test6: Valid small-before-large combination"
    print("Passed test6")

def test7():
    # Rule 7: Test for valid sequences of symbols
    assert not valid_numeral('VV'), "Failed test7: Invalid sequence of symbols"
    assert not valid_numeral('LLL'), "Failed test7: Invalid sequence of symbols"
    assert valid_numeral('III'), "Failed test7: Valid sequence of symbols"
    assert valid_numeral('XX'), "Failed test7: Valid sequence of symbols"
    print("Passed test7")

def test8():
    # Comprehensive test cases
    assert valid_numeral('XVIII'), "Failed test8: Valid numeral"
    assert valid_numeral('MCXIV'), "Failed test8: Valid numeral"
    assert not valid_numeral('CIL'), "Failed test8: Invalid numeral"
    print("Passed test8")

def test9():
    # Test for maximum valid numeral (3999)
    assert valid_numeral('MMMCMXCIX'), "Failed test9: Maximum valid numeral"
    print("Passed test9")

def test10():
    # Test for numerals just below the maximum
    assert valid_numeral('MMMCMXCVIII'), "Failed test10: Just below maximum"
    print("Passed test10")

def test11():
    # Test for numerals just above the minimum
    assert valid_numeral('I'), "Failed test11: Minimum valid numeral"
    assert valid_numeral('II'), "Failed test11: Just above minimum"
    print("Passed test11")

def test12():
    # Test for invalid numerals just above the maximum
    assert not valid_numeral('MMMM'), "Failed test12: Above maximum numeral"
    print("Passed test12")

###############################################################    

if __name__ == "__main__":
    main()
