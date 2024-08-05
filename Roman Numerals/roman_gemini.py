# Gemini passes its unit tests
# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals
"""
__version__ = 1


def is_valid_char(char):
  """
  Checks if a character is a valid Roman numeral character (uppercase I, V, X, L, C, D, M).
  """
  return char in "IVXLCDM"


def has_valid_characters(roman_numeral):
  """
  Checks if a string contains only valid Roman numeral characters.
  """
  for char in roman_numeral:
    if not is_valid_char(char):
      return False
  return True


def valid_numeral(roman_numeral):
  """
  Checks if a string is a valid Roman numeral (considering rules 1-4).

  This function currently only considers rules 1-4:
  1. Valid Roman numeral consists only of alphabetic characters.
  2. Valid Roman numeral only contains the characters I, V, X, L, C, D, and M.
  3. Valid Roman numeral should not have 4 of the same character in a row.
  4. Valid Roman numeral should be ordered from large-valued symbol to small-valued symbol.

  This function will be extended to include further validation rules in future iterations.
  """
  if not roman_numeral.isalpha():  # Rule 1: Check for alphabetic characters
    return False
  if not has_valid_characters(roman_numeral):  # Rule 2: Check for valid Roman characters
    return False

  # Rule 3: Check for more than 3 consecutive repetitions
  last_char = None
  count = 0
  for char in roman_numeral:
    if char == last_char:
      count += 1
      if count > 3:
        return False
    else:
      last_char = char
      count = 1

  # Rule 4: Check for large-valued symbol followed by smaller (except for specific cases)
  for i in range(len(roman_numeral) - 1):
    current_value = get_roman_value(roman_numeral[i])
    next_value = get_roman_value(roman_numeral[i + 1])
    if current_value < next_value:
      continue
    if current_value != next_value and not is_valid_subtraction(current_value, next_value):
      return False
  return True


def get_roman_value(char):
  """
  Returns the integer value of a Roman numeral character.
  """
  roman_map = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000,
  }
  return roman_map.get(char)


def is_valid_subtraction(larger_value, smaller_value):
  """
  Checks if a smaller Roman numeral character can be subtracted from a larger one.

  Currently allows subtraction only for (I, V), (X, I)
  """
  return (larger_value, smaller_value) in ((5, 1), (10, 1))


def main():
  """
  Runs the unit tests for the Roman numeral validation function.
  """
  # Test cases for Rule 1 (alphabetic characters)
  assert not valid_numeral("123")
  assert not valid_numeral("!@#$%^")

  # Test cases for Rule 2 (valid Roman characters)
  assert not valid_numeral("IIII")  # More than 3 'I'
  assert not valid_numeral("VVVV")  # More than 3 'V'
  assert not valid_numeral("AB")

  # Test cases for Rule 3 (no more than 3 consecutive repetitions)
  assert not valid_numeral("IIII")
  assert not valid_numeral("VVVVV")

  # Test cases for Rule 4 (larger to smaller order)
  assert not valid_numeral("VL")  # Large followed by smaller (not allowed)
  assert valid_numeral("IV")  # Allowed subtraction (I from V)
  assert valid_numeral("IX")  # Allowed subtraction (I from X)

  print
