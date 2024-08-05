import os
import unittest

def discover_and_run_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Discover all test files that match the pattern test_*.py
    for file in os.listdir('.'):
        if file.startswith("test_") and file.endswith(".py"):
            module_name = file[:-3]
            try:
                module = __import__(module_name)
                suite.addTests(loader.loadTestsFromModule(module))
            except ImportError as e:
                print(f"Could not import {module_name}: {e}")

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return result

def main():
    result = discover_and_run_tests()

    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print(f"{len(result.failures)} tests failed. Details:")
        for test, reason in result.failures:
            print(f"Test: {test.id()}")
            print(f"Reason: {reason}")

if __name__ == "__main__":
    main()
