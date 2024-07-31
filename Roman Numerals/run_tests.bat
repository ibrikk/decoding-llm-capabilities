@echo off

REM Run reference tests
pytest test_reference_tests.py > reference_pytest_output.txt

REM Run unit tests
pytest tests\test_unit_tests.py > direct_pytest_output.txt

REM Parse the outputs
python parse_pytest_output.py
pause
