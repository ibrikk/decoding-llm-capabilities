# -*- coding: utf-8 -*- 
""" Detect valid Roman numerals """
__version__ = 1

# Helper function to check if a character is a valid Roman numeral symbol
def is_valid_symbol(char):
    valid_symbols = set(['I', 'V', 'X', 'L', 'C', 'D', 'M'])
    return char in valid_symbols

# Helper function to get the value of a Roman numeral symbol
def get_value(char):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return values.get(char, 0)

def valid_numeral(test_case):
    # Rule 1: A valid Roman numeral consists only of alphabetic characters (as a corollary, the empty string is invalid)
    if not test_case.isalpha():
        return False

    # Rule 2: A valid Roman numeral only contains the characters I, V, X, L, C, D, and M (the lower-case versions of these characters are not valid)
    for char in test_case:
        if not is_valid_symbol(char):
            return False

    # Rule 3: A valid Roman numeral should not have 4 of the same character in a row
    for i in range(len(test_case) - 3):
        if test_case[i] == test_case[i+1] == test_case[i+2] == test_case[i+3]:
            return False

    # Rule 4: A valid Roman numeral should be ordered from large-valued symbol to small-valued symbol. Unless...
    value = 0
    prev_value = get_value(test_case[0])
    for i in range(1, len(test_case)):
        curr_value = get_value(test_case[i])
        if curr_value <= prev_value:
            value += prev_value
        else:
            # Rule 5: A valid Roman numeral can have a small-valued symbol precede a large-valued symbol, only if the small-valued symbol is an integer power of 10
            # Rule 6: A valid Roman numeral can have a small-valued symbol precede a large-valued symbol, only if the small-valued symbol is an integer power of 10 AND the small-valued symbol is one of the two symbols in size order before the large-valued symbol
            if prev_value not in [1, 10, 100]:
                return False
            if curr_value not in [5 * prev_value, 10 * prev_value]:
                return False
            value -= prev_value
        prev_value = curr_value
    value += prev_value

    # Rule 7: A valid Roman number can have a sequence of 2 or 3 symbols in a row if they are integer powers of 10, but not otherwise
    for i in range(len(test_case) - 2):
        if get_value(test_case[i]) == get_value(test_case[i+1]) == get_value(test_case[i+2]):
            if get_value(test_case[i]) not in [1, 10, 100]:
                return False

    return True

def main():
    # Test cases
    print(valid_numeral('XVIII'))  # True
    print(valid_numeral('MCXIV'))  # True
    print(valid_numeral('CCCC'))   # False
    print(valid_numeral('CIL'))    # False
    print(valid_numeral('M2C'))    # False
    print(valid_numeral('ASDF'))   # False
    print(valid_numeral('VL'))     # False
    print(valid_numeral('XXX'))    # True
    print(valid_numeral('LLL'))    # False

if __name__ == "__main__":
    main()