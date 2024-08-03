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
    for char in valid_chars:
        if char * 4 in test_case:
            return False

    # Rule 4: A valid Roman numeral should be ordered from large-valued symbol to small-valued symbol
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(test_case) - 1):
        if values[test_case[i]] < values[test_case[i + 1]]:
            # Rule 5: A valid Roman numeral can have a small-valued symbol precede a large-valued symbol,
            # only if the small-valued symbol is an integer power of 10
            if values[test_case[i]] not in [1, 10, 100]:
                return False
            # Rule 6: A valid Roman numeral can have a small-valued symbol precede a large-valued symbol,
            # only if the small-valued symbol is an integer power of 10 AND the small-valued symbol is
            # one of the two symbols in size order before the large-valued symbol
            if values[test_case[i]] * 10 < values[test_case[i + 1]]:
                return False

    # Rule 7: A valid Roman number can have a sequence of 2 or 3 symbols in a row if they are integer powers of 10,
    # but not otherwise
    for char in 'VLD':
        if char * 2 in test_case:
            return False
    for char in 'IXCM':
        if char * 4 in test_case:
            return False

    return True


def main():
    # Call test cases
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()


# Test case functions

# Rule 1 tests
def test1():
    assert valid_numeral('XVIII') == True
    assert valid_numeral('M2C') == False
    assert valid_numeral('XIIa') == False
    assert valid_numeral('XI_X') == False

# Rule 2 tests
def test2():
    assert valid_numeral('ASDF') == False
    assert valid_numeral('MCXIV') == True
    assert valid_numeral('XiX') == False

# Rule 3 tests
def test3():
    assert valid_numeral('CCCC') == False
    assert valid_numeral('XXXIX') == True
    assert valid_numeral('IIII') == False

# Rule 4 tests
def test4():
    assert valid_numeral('XVIII') == True
    assert valid_numeral('MCXIV') == True
    assert valid_numeral('VL') == False

# Rule 5 tests
def test5():
    assert valid_numeral('IV') == True
    assert valid_numeral('IX') == True
    assert valid_numeral('VX') == False

# Rule 6 tests
def test6():
    assert valid_numeral('IV') == True
    assert valid_numeral('IX') == True
    assert valid_numeral('IL') == False
    assert valid_numeral('IC') == False

# Rule 7 tests
def test7():
    assert valid_numeral('II') == True
    assert valid_numeral('III') == True
    assert valid_numeral('VV') == False
    assert valid_numeral('VVV') == False
    assert valid_numeral('LLL') == False


if __name__ == "__main__":
    main()