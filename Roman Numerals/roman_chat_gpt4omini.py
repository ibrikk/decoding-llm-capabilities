import os

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

def count_failures(output_file):
    failure_counts = {}
    with open(output_file, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        for module in all_modules:
            if module in line:
                if "FAILED" in line and "::" in line:
                    parts = line.split("::")
                    if len(parts) > 1:
                        test_detail = parts[1].split(" - ")[0]
                    if "[" in test_detail:
                        module_name = test_detail.split("[")[1].split("]")[0]
                    else:
                        module_name = test_detail
                    module_name = module_name.split("-")[0]
                    failure_counts[module_name] = failure_counts.get(module_name, 0) + 1
    
    return failure_counts

def process_test_output(file_name, test_type, module_name=None):
    if os.path.exists(file_name):
        print(f"Processing file: {file_name}")
        failure_counts = count_failures(file_name)
        if len(failure_counts) == 0:
            print(f"All {test_type} tests passed!")
        else:
            if module_name:
                print(f"{module_name} unit Test Failure Counts:")
            else:
                print(f"{test_type.capitalize()} Test Failure Counts by Module:")
            for module, count in failure_counts.items():
                test_word = "test" if count == 1 else "tests"
                if module_name:
                    print(f"{module}: {count} failed {test_word}")
                else:
                    print(f"{module}: {count} failed {test_word}")
            if not module_name:
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
