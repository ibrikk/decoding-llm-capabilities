import os
import re

all_modules = [
    "roman_chat_gpt4",
    "roman_chat_gpt4o",
    "roman_chat_gpt4omini",
    "roman_claude_opus",
    "roman_claude_sonnet",
    "roman_claude_haiku",
    "roman_github_copilot",
    "roman_gemini"
]

def count_failures(output_file, module_name_txt=None):
    failure_counts = {}
    with open(output_file, 'r') as file:
        lines = file.readlines()
    
    if not module_name_txt:
        # Start processing from the "short test summary info" section
        in_summary_section = False
        for line in lines:
            if "short test summary info" in line:
                in_summary_section = True
                continue
            
            if in_summary_section:
                match = re.search(r"(\w+)\[([^\]]+)\]", line)
                if match:
                    test_name, module_name = match.groups()
                    if module_name in all_modules:
                        failure_counts[module_name] = failure_counts.get(module_name, 0) + 1
    else:
        # Count the failures for a specific module
        line_to_parse = ""
        for line in lines:
            if "failed in" in line:
                line_to_parse = line
        if line_to_parse:
            count = re.search(r"(\d+) failed", line_to_parse)
            if count:
                failure_counts[module_name_txt] = int(count.group(1))
    
    return failure_counts

def process_test_output(file_name, test_type, module_name=None):
    if test_type == 'reference':
        file_path = 'C:\\Users\\vmascuser\\Documents\\decoding-llm-capabilities\Roman Numerals\pytest_output.txt'
        print(f"Checking for file: {file_path}")
    else:
        file_path = 'C:\\Users\\vmascuser\\Documents\\decoding-llm-capabilities\\Roman Numerals\\' + file_name
    if os.path.exists(file_path):
            print(f"Processing file: {file_path}")
            failure_counts = count_failures(file_path, module_name)
            if len(failure_counts) == 0:
                print(f"All {test_type} tests passed!")
            else:
                if module_name:
                    print(f"{module_name} unit Test Failure Counts:")
                    if module_name in failure_counts:
                        count = failure_counts[module_name]
                        test_word = "test" if count == 1 else "tests"
                        print(f"{module_name}: {count} failed {test_word}")
                    else:
                        print(f"All {module_name} unit tests passed!")
                else:
                    print(f"{test_type.capitalize()} Test Failure Counts by Module:")
                    for module, count in failure_counts.items():
                        test_word = "test" if count == 1 else "tests"
                        print(f"{module}: {count} failed {test_word}")
                    for my_module in all_modules:
                        if my_module not in failure_counts:
                            print(f"{my_module}: 0 failed tests")
    else:
        print(f"{file_name} not found.")

def main():
    process_test_output('pytest_output.txt', 'reference')

    for module in all_modules:
        output_file_name = f'{module}_output.txt'
        process_test_output(output_file_name, f'{module} unit', module)

if __name__ == "__main__":
    main()
