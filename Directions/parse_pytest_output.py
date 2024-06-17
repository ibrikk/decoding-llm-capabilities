import os

all_modules = [
    "directions_chat_gpt4",
    "directions_chat_gpt3",
    "directions_claude3_opus",
    "directions_claude3_sonnet",
    "directions_claude3_haiku",
    "directions_claude_free",
    "directions_github_copilot",
    "directions_gemini"
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
                        test_detail = parts[1].split(" - ")[0]  # Initial split by " - " to get the part with potential module name
                    if "[" in test_detail:
                        module_name = test_detail.split("[")[1].split("]")[0]  # Extracts module name from between brackets
                    else:
                        module_name = test_detail
                    # If the extracted module name contains detailed identifiers (e.g., '-1-4-True-1/4'), remove them
                    module_name = module_name.split("-")[0]  # Keeps only the base module name before any '-' character
                    failure_counts[module_name] = failure_counts.get(module_name, 0) + 1
    
    
    return failure_counts

def main():
    # Use a relative path for simplicity and flexibility
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file_name = 'pytest_output.txt'
    output_file_path = os.path.join(script_dir, output_file_name)
    
    # Create the file if it does not exist
    if not os.path.exists(output_file_path):
        print(f"{output_file_name} does not exist, creating...")
        open(output_file_path, 'a').close()  # 'a' mode will create the file if it doesn't exist
    
    print(f"Processing file: {output_file_path}")
    failure_counts = count_failures(output_file_path)

    if len(failure_counts) == 0:
        print("All tests passed!")
    else:
        print("Failure Counts by Module:")
        for module, count in failure_counts.items():
            # Using the singular or plural form of "test" appropriately
            test_word = "test" if count == 1 else "tests"
            print(f"{module}: {count} failed {test_word}")
        for my_module in all_modules:
            if my_module not in failure_counts:
                print(f"{my_module}: 0 failed tests")
        

if __name__ == "__main__":
    main()
