@echo off

REM Detect the operating system
set osversion=
for /f "tokens=4-7 delims=[.] " %%i in ('ver') do (
    if %%i==Version (
        set osversion=%%j.%%k
    )
)

REM Check if Python 3 is installed
python --version >nul 2>&1
if errorlevel 1 goto install_python

REM Check if virtual environment module is installed
python -m venv --help >nul 2>&1
if errorlevel 1 goto install_venv

REM Create virtual environment
python -m venv myenv

REM Activate virtual environment
call myenv\Scripts\activate.bat

REM Install pytest
pip install pytest

echo Virtual environment setup complete with Python 3 and pytest installed. Use 'myenv\Scripts\activate.bat' to activate.
goto end

:install_python
echo Python 3 not found. Downloading and installing...
if "%osversion%" == "10.0" (
    bitsadmin /transfer downloadjob /download /priority foreground https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe %temp%\python-3.9.13-amd64.exe
    start /wait %temp%\python-3.9.13-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
) else (
    echo Unsupported Windows version. Please install Python 3 manually.
    exit /b 1
)
goto install_venv

:install_venv
echo Virtual environment module not found. Installing...
python -m pip install --user --upgrade pip
python -m pip install --user virtualenv
goto start

:end
pause