@echo off

REM Run reference tests
pytest test_reference_tests.py > reference_pytest_output.txt

REM Run unit tests
pytest tests\test_unit_tests.py > direct_pytest_output.txt

REM Parse the outputs
python parse_pytest_output.py

REM Run mutation tests
mutmut run --paths-to-mutate roman_chat_gpt4o_new.py --tests-dir tests

REM Generate mutation coverage report
sqlite3 .mutmut-cache "SELECT * FROM mutant" > mutation_test_results.txt

echo All tests and mutation testing completed.
pause
