# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals
"""
__version__ = 1

def valid_numeral(numeral):
    """
    Checks if the given string is a valid Roman numeral.

    This function implements various rules to determine the validity of the numeral.
    """

    # Check if empty or contains non-alphabetic characters (Rule 1)
    if not numeral.isalpha() or not numeral:
        return False

    # Check if contains only valid characters (Rule 2)
    valid_chars = {"I", "V", "X", "L", "C", "D", "M"}
    if set(numeral) > valid_chars:
        return False

    # Check for no more than three consecutive repeats (Rule 3)
    for i in range(len(numeral) - 3):
        if numeral[i] == numeral[i + 1] == numeral[i + 2] == numeral[i + 3]:
            return False

    # Check for correct order except for valid subtractions (Rule 4)
    previous_value = 0
    for char in numeral:
        current_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}[
            char
        ]
        if current_value <= previous_value and not (
            (char in {"I", "X"}) and (previous_value in {"V", "L"})
        ):
            return False
        previous_value = current_value

    # Check for valid subtractions (Rule 5 and 6)
    for i in range(len(numeral) - 1):
        if (
            numeral[i] in {"I", "X"}
            and numeral[i + 1] in {"V", "L"}
            and numeral.count(numeral[i]) == 1  # Only one I or X allowed before subtraction
        ):
            continue
        elif numeral[i] == numeral[i + 1]:
            return False
    return True

def main():
    # Sample usage and test cases (implement these as separate functions)
    pass


if __name__ == "__main__":
    main()
