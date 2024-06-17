# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals 
"""
__version__ = 1

import re

def valid_numeral(numeral):
  # Function to check if a given string is a valid Roman numeral
  
  # Return False if empty string
  if not numeral:
    return False

  # Compile regex to check for valid characters
  valid_chars = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')

  # Check string contains only valid characters
  if not valid_chars.match(numeral): 
    return False
  
  # Add other validation checks here
  
  return True


def main():
  # Test cases
  print(valid_numeral('XVIII')) # True
  print(valid_numeral('MCXIV')) # True 
  print(valid_numeral('CCCC')) # False
  print(valid_numeral('CIL')) # False

  # Add other test cases
  
###############################################################

# Test functions

def test_empty():
  assert not valid_numeral('')

def test_invalid_chars():
  assert not valid_numeral('M2C') 

def test_four_repeats():
  assert not valid_numeral('IIII')

def test_ordered_symbols():
  assert not valid_numeral('VX')

def test_subtraction_rule():
  assert not valid_numeral('IC') 

def test_valid_numerals():
  assert valid_numeral('XVIII')
  assert valid_numeral('MCXIV')

###############################################################
  
if __name__ == "__main__":
  main()

  # Call test functions
  test_empty()
  test_invalid_chars()
  test_four_repeats()
  test_ordered_symbols()
  test_subtraction_rule()
  test_valid_numerals()