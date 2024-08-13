import os
import re
import subprocess

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
        line_to_parse = ""
        for line in lines:
            if "no tests ran" in line:
                print("NO TESTS RAN!!!!!")
                return None
            if "failed in" in line or "failed," in line:
                line_to_parse = line
                break
        if line_to_parse:
            count = re.search(r"(\d+) failed", line_to_parse)
            if count:
                failure_counts[module_name_txt] = int(count.group(1))
    
    return failure_counts

def process_test_output(file_name, test_type, module_name=None):
    if test_type == 'reference':
        file_path = '/Users/ibrahimkhalilov/Documents/decoding-llm-capabilities/Roman Numerals/pytest_output.txt'
        print(f"Checking for file: {file_path}")
    else:
        # file_path = 'C:\\Users\\vmascuser\\Documents\\decoding-llm-capabilities\\Roman Numerals\\' + file_name
        file_path = '/Users/ibrahimkhalilov/Documents/decoding-llm-capabilities/Roman Numerals/' + file_name
    if os.path.exists(file_path):
        print(f"Processing file: {file_path}")
        failure_counts = count_failures(file_path, module_name)
        if len(failure_counts) == 0:
            print(f"All {test_type} tests passed!")
            # TODO: Uncomment this but might not work properly
            # if test_type.endswith('unit'):
            #     run_mutation_tests(module_name)
        elif failure_counts is None:
            print(f"{file_path} DID NOT RUN!!!!!")
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

def get_test_functions(test_file):
    path = 'C:\\Users\\vmascuser\\Documents\\decoding-llm-capabilities\\Roman Numerals\\' + test_file
    if os.path.exists(path):
        print(f"Reading test functions from {test_file}")
        with open(path, 'r') as file:
            content = file.read()
        test_functions = re.findall(r'def (test_\w+)\(', content)
        return test_functions
    else:
        print(f"{test_file} not found.")
        return []

def count_emojis_in_output(output):
    emojis = ['🎉', '⏰', '🤔', '🙁', '🔇']
    emoji_count = {emoji: output.count(emoji) for emoji in emojis}
    return emoji_count

def run_mutation_tests(module_name):
    test_file = 'test_my_solution.py'
    test_functions = get_test_functions(test_file)
    if not test_functions:
        print(f"No test functions found in {test_file}.")
        return
    
    total_tests = len(test_functions)
    passed_tests = 0
    
    for test_function in test_functions:
        mutmut_command = f'mutmut run --paths-to-mutate {module_name}.py --tests-dir . --runner "pytest {test_file}::{test_function}[{module_name}]"'
        print(f"Running mutation tests for {module_name} with command: {mutmut_command}")
        result = subprocess.run(
            mutmut_command,
            shell=True,
            capture_output=True,
            text=True,
            cwd='C:\\Users\\vmascuser\\Documents\\decoding-llm-capabilities\\Roman Numerals',
            encoding='utf-8'
        )
        emoji_count = count_emojis_in_output(result.stdout)
        if result.returncode == 0 or all(count > 0 for count in emoji_count.values()):
            print(f"Mutation testing for {module_name}::{test_function} completed successfully.")
            passed_tests += 1
        else:
            print(f"Mutation testing for {module_name}::{test_function} failed.")
            print("Return code:", result.returncode)
            print("Stdout:", result.stdout)
            print("Stderr:", result.stderr)
    
    print(f"Mutation testing summary for {module_name}:")
    print(f"Total tests: {total_tests}")
    print(f"Passed tests: {passed_tests}")
    if total_tests > 0:
        coverage_percentage = (passed_tests / total_tests) * 100
        print(f"Mutation testing coverage: {coverage_percentage:.2f}%")

def main():
    process_test_output('pytest_output.txt', 'reference')

    for module in all_modules:
        output_file_name = f'{module}_output.txt'
        process_test_output(output_file_name, f'{module} unit', module)

if __name__ == "__main__":
    main()
