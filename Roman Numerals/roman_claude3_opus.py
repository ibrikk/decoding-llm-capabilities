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
    valid_chars = set('IVXLCDM')
    if not set(test_case).issubset(valid_chars):
        return False

    # Rule 3: A valid Roman numeral should not have 4 of the same character in a row
    if any(char * 4 in test_case for char in valid_chars):
        return False

    # Rule 4: A valid Roman numeral should be ordered from large-valued symbol to small-valued symbol
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = float('inf')
    for char in test_case:
        curr_value = values[char]
        if curr_value > prev_value:
            # Rule 5: A valid Roman numeral can have a small-valued symbol precede a large-valued symbol,
            # only if the small-valued symbol is an integer power of 10
            if curr_value not in [10, 100, 1000] or prev_value not in [1, 10, 100]:
                return False

            # Rule 6: A valid Roman numeral can have a small-valued symbol precede a large-valued symbol,
            # only if the small-valued symbol is an integer power of 10 AND the small-valued symbol
            # is one of the two symbols in size order before the large-valued symbol
            if curr_value // prev_value > 10:
                return False
        prev_value = curr_value

    # Rule 7: A valid Roman number can have a sequence of 2 or 3 symbols in a row if they are integer powers of 10,
    # but not otherwise
    for char in 'VLD':
        if char * 2 in test_case:
            return False

    return True

def test1():
    # Test for Rule 1: A valid Roman numeral consists only of alphabetic characters
    assert valid_numeral('XVIII') == True
    assert valid_numeral('M2C') == False
    assert valid_numeral('X_I') == False
    assert valid_numeral('V (I)') == False

def test2():
    # Test for Rule 2: A valid Roman numeral only contains the characters I, V, X, L, C, D, and M
    assert valid_numeral('MCXIV') == True
    assert valid_numeral('ASDF') == False
    assert valid_numeral('XIix') == False

def test3():
    # Test for Rule 3: A valid Roman numeral should not have 4 of the same character in a row
    assert valid_numeral('MMMCMXCIX') == True
    assert valid_numeral('CCCC') == False
    assert valid_numeral('IIII') == False

def test4():
    # Test for Rule 4: A valid Roman numeral should be ordered from large-valued symbol to small-valued symbol
    assert valid_numeral('XVIII') == True
    assert valid_numeral('VL') == False
    assert valid_numeral('IXC') == False

def test5():
    # Test for Rule 5: A valid Roman numeral can have a small-valued symbol precede a large-valued symbol,
    # only if the small-valued symbol is an integer power of 10
    assert valid_numeral('IV') == True
    assert valid_numeral('IX') == True
    assert valid_numeral('VX') == False

def test6():
    # Test for Rule 6: A valid Roman numeral can have a small-valued symbol precede a large-valued symbol,
    # only if the small-valued symbol is an integer power of 10 AND the small-valued symbol
    # is one of the two symbols in size order before the large-valued symbol
    assert valid_numeral('IV') == True
    assert valid_numeral('IX') == True
    assert valid_numeral('IL') == False
    assert valid_numeral('IC') == False

def test7():
    # Test for Rule 7: A valid Roman number can have a sequence of 2 or 3 symbols in a row if they are integer powers of 10,
    # but not otherwise
    assert valid_numeral('XXX') == True
    assert valid_numeral('III') == True
    assert valid_numeral('VV') == False
    assert valid_numeral('VVV') == False
    assert valid_numeral('LLL') == False

def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    print("All tests passed!")

if __name__ == "__main__":
    main()