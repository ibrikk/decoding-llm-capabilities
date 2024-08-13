#!/bin/bash

# Run reference tests
echo "Running reference tests..."
pytest test_my_solution.py > pytest_output.txt
if [ -f "pytest_output.txt" ]; then
    echo "Reference tests output saved to pytest_output.txt"
else
    echo "Failed to create pytest_output.txt"
    exit 1
fi

# Array of module names
modules=("roman_chat_gpt4" "roman_chat_gpt4o" "roman_chat_gpt4omini" "roman_claude_opus" "roman_claude_sonnet" "roman_claude_haiku" "roman_github_copilot" "roman_gemini")

# Run unit tests for each module and output results to separate files
for module in "${modules[@]}"; do
    echo "Running unit tests for $module..."
    pytest "$module.py" > "${module}_output.txt"
    if [ -f "${module}_output.txt" ]; then
        echo "Unit tests output saved to ${module}_output.txt"
    else
        echo "Failed to create ${module}_output.txt"
    fi
done

# Parse the outputs
echo "Parsing test outputs..."
python3 parse_pytest_output.py

echo "All tests completed."
read -n 1 -s -r -p "Press any key to continue..."
