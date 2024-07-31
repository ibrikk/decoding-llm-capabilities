#!/bin/bash

# Run reference tests
pytest test_reference_tests.py > reference_pytest_output.txt

# Run unit tests
pytest test_unit_tests.py > direct_pytest_output.txt

# Parse the outputs
python parse_pytest_output.py
