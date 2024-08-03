import unittest

def valid_numeral(test_case):
    """Check if the input string is a valid Roman numeral."""
    # Rule 1 & 2: Validate characters
    if not test_case.isalpha() or any(ch not in "IVXLCDM" for ch in test_case):
        return False

    # Rule 3: No more than three consecutive identical symbols
    for symbol in "IVXLCDM":
        if symbol * 4 in test_case:
            return False

    # Rule 4, 5, 6 & 7: Complex validation of order and subtraction rules
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    previous_value = 0
    for i, char in enumerate(reversed(test_case)):
        current_value = roman_values[char]
        if current_value < previous_value:
            # Check for valid subtraction
            if current_value not in [1, 10, 100] or current_value * 10 < previous_value:
                return False
        previous_value = current_value

    return True

class TestRomanNumerals(unittest.TestCase):

    def test_only_characters(self):
        self.assertTrue(valid_numeral("XVIII"))
        self.assertFalse(valid_numeral("123"))
        self.assertFalse(valid_numeral("M2C"))

    def test_valid_characters(self):
        self.assertTrue(valid_numeral("MDCLXVI"))
        self.assertFalse(valid_numeral("ASDF"))
        self.assertFalse(valid_numeral("MCXIVV"))

    def test_repetition(self):
        self.assertTrue(valid_numeral("III"))
        self.assertFalse(valid_numeral("IIII"))
        self.assertFalse(valid_numeral("XXXX"))
        self.assertTrue(valid_numeral("XXX"))

    def test_order_and_subtraction(self):
        self.assertTrue(valid_numeral("IX"))
        self.assertFalse(valid_numeral("IL"))
        self.assertTrue(valid_numeral("MCMXCIX"))
        self.assertFalse(valid_numeral("IIX"))
        self.assertTrue(valid_numeral("XIV"))
        self.assertFalse(valid_numeral("VX"))

if __name__ == "__main__":
    unittest.main()
