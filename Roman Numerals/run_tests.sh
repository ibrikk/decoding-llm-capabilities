#!/bin/bash

# Run reference tests
pytest Roman\ Numerals/test_reference_tests.py > Roman\ Numerals/reference_pytest_output.txt

# Run unit tests
pytest Roman\ Numerals/tests/test_unit_tests.py > Roman\ Numerals/direct_pytest_output.txt

# Parse the outputs
python Roman\ Numerals/parse_pytest_output.py

# Run mutation tests
mutmut run --paths-to-mutate Roman\ Numerals/roman_chat_gpt4o_new.py --tests-dir Roman\ Numerals/tests

# Generate mutation coverage report
sqlite3 .mutmut-cache "SELECT * FROM mutant" > Roman\ Numerals/mutation_test_results.txt

echo "All tests and mutation testing completed."
