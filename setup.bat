@echo off

REM Install Python 3 from the official website (https://www.python.org/downloads/)
REM Follow the installation instructions and make sure to select the option to add Python to the system PATH

REM Create virtual environment
python -m venv myenv

REM Activate virtual environment
call myenv\Scripts\activate.bat

REM Install pytest
pip install pytest

echo Virtual environment setup complete with Python 3 and pytest installed. Use 'myenv\Scripts\activate.bat' to activate.
pause