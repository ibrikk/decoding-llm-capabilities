:: setup.bat
@echo off

:: Create virtual environment
python -m venv myenv

:: Activate virtual environment
call myenv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

echo Virtual environment setup complete. Use 'myenv\Scripts\activate' to activate.
