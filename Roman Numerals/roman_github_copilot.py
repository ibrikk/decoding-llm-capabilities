import re

def valid_numeral(test_case):
    if not test_case.isalpha():  # Rule 1
        return False
    if not set(test_case).issubset(set('IVXLCDM')):  # Rule 2
        return False
    if re.search(r'(.)\1{3,}', test_case):  # Rule 3
        return False
    if re.search(r'I[^VX]|V[^I]|X[^IVLC]|L[^X]|C[^IVXLD]|D[^C]|M[^IVXLC]', test_case):  # Rule 4
        return False
    if re.search(r'IV|IX|XL|XC|CD|CM', test_case) and re.search(r'I[^VX]|X[^IVLC]|C[^IVXLD]', test_case):  # Rule 5 and 6
        return False
    if re.search(r'V{2,}|L{2,}|D{2,}', test_case):  # Rule 7
        return False
    return True

def test1():
    assert valid_numeral('XVIII') == True
    assert valid_numeral('MCXIV') == True
    assert valid_numeral('CCCC') == False
    assert valid_numeral('CIL') == False

def test2():
    assert valid_numeral('M2C') == False
    assert valid_numeral('ASDF') == False
    assert valid_numeral('VL') == False
    assert valid_numeral('XXX') == True
    assert valid_numeral('LLL') == False

def main():
    test1()
    test2()

if __name__ == "__main__":
    main()