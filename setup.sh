#!/bin/bash

# Detect the operating system and install Python 3 if not installed
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)
        if command -v apt-get >/dev/null 2>&1; then
            sudo apt-get update
            sudo apt-get install -y python3 python3-venv python3-pip
        elif command -v dnf >/dev/null 2>&1; then
            sudo dnf install -y python3 python3-venv python3-pip
        elif command -v pacman >/dev/null 2>&1; then
            sudo pacman -Sy python3 python-virtualenv python-pip
        else
            echo "Unsupported Linux distribution. Please install Python 3 manually."
            exit 1
        fi
        ;;
    Darwin*)
        if command -v brew >/dev/null 2>&1; then
            brew install python3
        else
            echo "Homebrew not found. Please install Python 3 manually."
            exit 1
        fi
        ;;
    *)
        echo "Unsupported operating system. Please install Python 3 manually."
        exit 1
        ;;
esac

# Create virtual environment
python3 -m venv myenv

# Activate virtual environment
source myenv/bin/activate

# Install necessary Python packages
pip install pytest mutmut

echo "Virtual environment setup complete with Python 3 and necessary packages installed. Use 'source myenv/bin/activate' to activate."

# Run the tests and mutation tests
pytest "Roman Numerals/test_reference_tests.py" > "Roman Numerals/reference_pytest_output.txt"
pytest "Roman Numerals/tests/test_unit_tests.py" > "Roman Numerals/direct_pytest_output.txt"
python "Roman Numerals/parse_pytest_output.py"
mutmut run --paths-to-mutate "Roman Numerals/roman_chat_gpt4o_new.py" --tests-dir "Roman Numerals/tests"
mutmut results > "Roman Numerals/mutation_test_results.txt"

echo "All tests and mutation testing completed."
