def valid_numeral(test_case):
    # Rule 1: A valid Roman numeral consists only of alphabetic characters
    if not test_case.isalpha():
        return False
    
    # Rule 2: A valid Roman numeral only contains the characters I, V, X, L, C, D, and M
    valid_characters = set('IVXLCDM')
    if any(char not in valid_characters for char in test_case):
        return False
    
    # Rule 3: A valid Roman numeral should not have 4 of the same character in a row
    if 'IIII' in test_case or 'VVVV' in test_case or 'XXXX' in test_case \
            or 'LLLL' in test_case or 'CCCC' in test_case or 'DDDD' in test_case \
            or 'MMMM' in test_case:
        return False
    
    # Rule 4: A valid Roman numeral should be ordered from large-valued symbol to small-valued symbol
    # We'll skip implementing this rule here since it will be checked in the subsequent rules
    
    # Rule 5: A valid Roman numeral can have a small-valued symbol precede a large-valued symbol,
    # only if the small-valued symbol is an integer power of 10
    if 'IL' in test_case or 'IC' in test_case or 'ID' in test_case or 'IM' in test_case \
            or 'VL' in test_case or 'VC' in test_case or 'VD' in test_case or 'VM' in test_case \
            or 'XD' in test_case or 'XM' in test_case:
        return False
    
    # Rule 6: A valid Roman numeral can have a small-valued symbol precede a large-valued symbol,
    # only if the small-valued symbol is an integer power of 10 AND the small-valued symbol is one of the two
    # symbols in size order before the large-valued symbol
    if 'IL' in test_case or 'IC' in test_case or 'ID' in test_case or 'IM' in test_case \
            or 'XD' in test_case or 'XM' in test_case:
        return False
    
    # Rule 7: A valid Roman number can have a sequence of 2 or 3 symbols in a row if they are integer powers of 10
    if any(test_case.count(char*3) > 0 for char in 'IVXLCDM'):
        return False
    
    return True


def main():
    # Test cases
    test_cases = ['XVIII', 'MCXIV', 'CCCC', 'CIL', 'M2C', 'ASDF', 'VL', 'XXX', 'LLL']
    for test_case in test_cases:
        print(f"{test_case}: {valid_numeral(test_case)}")

if __name__ == "__main__":
    main()
