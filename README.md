
# Decoding the Capabilities of Large Language Models: A Multidimensional Comparison of LLM Tools for Algorithmic Code Generation

## Introduction
This repository contains the code and resources for the Comparison of LLM Tools for Algorithmic Code Generation. 

File naming convention: LLM tools were prompted to fill in the methods. For instance, ```directions.py``` file is the orignal template file and ```directions_chat_gpt4.py``` is the solution provided by Chat GPT 4 and so on.

## Usage
Install Pytest: ```pip install -U pytest```. \
If you are on Linux/MacOS make sure to set the execution permissions using `chmod +x run_tests.sh` to run the scripts. Then, you can run the scripts directly by executing `./run_tests.sh`. \
If you are on Windows, you can run the scripts directly by executing `./run_tests.bat`
## Pytest Command
To run the test for each coding challenge, navigate to its deirectory first e.g ```Directions``` or ```Roman Numerals```, etc. and then use the following commands. \
By applying chmod +x to your script for Linux/MacOS, you're changing its permissions to include execution rights for the user, effectively allowing you to run the script directly.
```bash
chmod +x run_tests.sh
```
Then you can run scripts directly
```bash
./run_tests.sh
```

## Installation Guide for Pytest

### Overview

`pytest` is a robust testing framework for Python that simplifies the creation and execution of tests. This guide will help you install `pytest` on your system.

### Prerequisites

Ensure that Python and pip (Python's package installer) are installed on your system. `pytest` requires Python 3.6 or higher. You can verify your Python and pip installation by running the following commands in your terminal:

```bash
python --version
pip --version
```

If Python is not installed, download and install it from the [official Python website](https://www.python.org/downloads/).

### Installation Steps

#### Step 1: Update pip

Before installing `pytest`, it's a good practice to ensure that pip is up-to-date. You can update pip using the following command:

```bash
python -m pip install --upgrade pip
```

#### Step 2: Install Pytest

Install `pytest` by running the following command:

```bash
pip install pytest
```

#### Step 3: Verify Installation

Confirm that `pytest` was installed correctly by checking its version:

```bash
pytest --version
```

This command should return the version number of `pytest`, confirming that it is correctly installed on your system.

### Writing Your First Test

After installing `pytest`, you can quickly start writing tests. Here is a simple example to test basic arithmetic:

1. Create a new file called `test_arithmetic.py`.
2. Add the following content to the file:

```python
# test_arithmetic.py

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 1
```

3. Run the test by executing:

```bash
pytest test_arithmetic.py
```

`pytest` will automatically find and execute the tests, reporting the results in the terminal.

### Conclusion

You now have `pytest` installed and are ready to start testing your Python applications. For more detailed information and advanced features, visit the [Pytest documentation](https://docs.pytest.org/en/stable/).

## Prompts given to LLMs:

This guide is only for reapplication purposes. If you are an assessor, please disregard this step.

1. Copy Paste the assignment instructions (rational_instructions.txt or roman_instructions.txt) from Canvas. Note that there are no instructions for Directions and Long Toss challenges.
2. Copy Paste the template code associated with the project you are trying to run (directions.py or long_toss.py or rational.py or roman.py) from Canvas.
3. Send the following prompt to the LLM: "Implement the solution to template methods based on given instructions".


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
# llm-comparison
# llm-comparison
