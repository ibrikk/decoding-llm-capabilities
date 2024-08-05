#!/bin/bash

# Define the modules to test
modules=("roman_chat_gpt4" "roman_chat_gpt4o" "roman_chat_gpt4omini" "roman_claude_opus" "roman_claude_sonnet" "roman_claude_haiku" "roman_github_copilot" "roman_gemini")

# Run reference tests
pytest test_my_solution.py > pytest_output.txt

# Run unit tests for each module and output results to separate files
for module in "${modules[@]}"
do
    echo "Running unit tests for $module"
    pytest ${module}.py > ${module}_output.txt
done

# Parse the outputs
python3 parse_pytest_output.py

echo "All tests completed."
