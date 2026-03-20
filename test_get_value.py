from module import get_value
import sys
from os import system
system("clear")

def run_all_tests():
    tests = [
        (({"a": 1, "b": 2}, "a"), 1),
        (({"x": 10}, "x"), 10),
    ]
    run_tests(tests, get_value)

def run_tests(tests, function):
    failure = False
    for i, (inputs, expected) in enumerate(tests):
        try:
            actual = function(*inputs)
            print(f"{inputs} → Expected: {expected}, Got: {actual}")
            assert actual == expected
            print(f"Test {i}: Pass!\n")
        except AssertionError:
            print(f"Test {i}: Fail\n")
            failure = True
        except Exception as e:
            print(f"Test {i}: Error → {type(e).__name__}: {e}\n")
            failure = True
    print("❌ Failures" if failure else "✅ All passed")

if __name__ == "__main__":
    run_all_tests()
    sys.exit(0)