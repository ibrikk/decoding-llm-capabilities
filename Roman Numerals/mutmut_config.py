from mutmut import Configuration

config = Configuration(
    tests_dir='tests',
    paths_to_mutate=['roman_chat_gpt4o.py'],
    test_command='pytest tests/test_unit_tests.py'
)
