from module import key_exists
import sys
from os import system
system("clear")

def run_all_tests():
    tests = [
        (({"a": 1, "b": 2}, "a"), True),
        (({"a": 1}, "z"), False),
    ]
    run_tests(tests, key_exists)

def run_tests(tests, function):
    failure = False
    for i, (inputs, expected) in enumerate(tests):
        try:
            actual = function(*inputs)
            print(f"{inputs} → {actual}")
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