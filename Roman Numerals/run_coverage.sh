#!/bin/bash

# Array of Python files to check coverage
files=(
    "roman_chat_gpt4.py"
    "roman_chat_gpt4o.py"
    "roman_chat_gpt4omini.py"
    "roman_claude_opus.py"
    "roman_claude_sonnet.py"
    "roman_claude_haiku.py"
    "roman_github_copilot.py"
    "roman_gemini.py"
)

# Clear any existing coverage data
coverage erase

# Loop through each file and run coverage
for file in "${files[@]}"; do
    echo "Running coverage for $file"
    coverage run --append "$file"
done

# Generate the combined coverage report
echo "Generating coverage report..."
coverage report
coverage html
echo "Coverage report generated in the 'htmlcov' directory."
