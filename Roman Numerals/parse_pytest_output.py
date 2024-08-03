import os

all_modules = [
    "roman_chat_gpt4",
    "roman_chat_gpt4o",
    "roman_chat_gpt4omini",
]

def count_failures(output_file, test_type):
    failure_counts = {}
    with open(output_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if test_type == "direct":
            if "FAILED" in line and "::" in line:
                # Isolate the part containing the test name
                parts = line.split("::")
                if len(parts) > 1:
                    test_detail = parts[1].split(" - ")[0]
                    if "test_" in test_detail:
                        module_name = test_detail.split("test_")[1].split("_test")[0]
                        failure_counts[module_name] = failure_counts.get(module_name, 0) + 1
        else:
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

def parse_mutation_results(result_file):
    killed = 0
    survived = 0

    with open(result_file, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        if "ok_killed" in line:
            killed += 1
        elif "bad_survived" in line:
            survived += 1

    mutation_score = (killed / (killed + survived)) * 100 if (killed + survived) > 0 else 0

    return killed, survived, mutation_score

def main():
    base_dir = "/Users/ibrahimkhalilov/Documents/decoding-llm-capabilities/Roman Numerals"

    # Define the output files
    reference_output_file = os.path.join(base_dir, 'reference_pytest_output.txt')
    direct_output_file = os.path.join(base_dir, 'direct_pytest_output.txt')
    mutation_result_file = os.path.join(base_dir, 'mutation_test_results.txt')
    
    # Count failures
    reference_failure_counts = count_failures(reference_output_file, "reference")
    direct_failure_counts = count_failures(direct_output_file, "direct")

    # Print the results
    print("Failure Counts by Module:")
    for module in all_modules:
        ref_tests = reference_failure_counts.get(module, 0)
        dir_tests = direct_failure_counts.get(module, 0)
        print(f"{module}: {ref_tests} failed reference tests, {dir_tests} failed unit tests")

    # Parse and print mutation results
    killed, survived, mutation_score = parse_mutation_results(mutation_result_file)
    print(f"\nMutation Testing Results:\nKilled: {killed}\nSurvived: {survived}\nMutation Score: {mutation_score:.2f}%")

if __name__ == "__main__":
    main()
