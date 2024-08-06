@echo off

REM Run reference tests
pytest test_my_solution.py > pytest_output.txt

REM Run unit tests for each module and output results to separate files
setlocal enabledelayedexpansion
set modules=roman_chat_gpt4 roman_chat_gpt4o roman_chat_gpt4omini roman_claude_opus roman_claude_sonnet roman_claude_haiku roman_github_copilot roman_gemini

for %%m in (%modules%) do (
    echo Running unit tests for %%m
    pytest %%m.py > %%m_output.txt
)

REM Parse the outputs
python parse_pytest_output.py

echo All tests completed.
pause
