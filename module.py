"""
Dictionary Practice - Functions

Directions:
Complete each function according to its description.

Rules:
- Do NOT change function names or parameters
- Each function must RETURN a value (do not print)
- Follow the requirements listed for each function
"""


# -------------------------------------------------
# get_value
# -------------------------------------------------
# get_value takes a dictionary and a key, and returns
# the value associated with that key.
#
# Examples:
#   get_value({"a": 1, "b": 2}, "a") -> 1
#   get_value({"x": 10}, "x") -> 10
#
# Requirements:
#   - Assume the key exists in the dictionary
#   - Do NOT print anything
#
def get_value(d: dict, key: str):
  return d[key]
# -------------------------------------------------
# key_exists
# -------------------------------------------------
# key_exists takes a dictionary and a key, and returns
# True if the key is in the dictionary, otherwise False.
#
# Examples:
#   key_exists({"a": 1, "b": 2}, "a") -> True
#   key_exists({"a": 1}, "z") -> False
#
# Requirements:
#   - Must return a Boolean value (True or False)
#   - Do NOT print anything
#
def key_exists(d: dict, key: str) -> bool:
    
    if key not in d:
        return False
    else:
        return True




# -------------------------------------------------
# total_values
# -------------------------------------------------
# total_values takes a dictionary with integer values
# and returns the sum of all the values.
#
# Examples:
#   total_values({"a": 1, "b": 2}) -> 3
#   total_values({}) -> 0
#
# Requirements:
#   - Must use a loop
#   - Do NOT use the built-in sum() function
#   - Do NOT print anything
#
def total_values(d: dict) -> int:
    total = 0
    for key in d:
        total += d[key]
    return total


# -------------------------------------------------
# count_value
# -------------------------------------------------
# count_value takes a dictionary and a target value,
# and returns how many times that value appears
# in the dictionary.
#
# Examples:
#   count_value({"a": 1, "b": 2, "c": 1}, 1) -> 2
#   count_value({"x": 5}, 3) -> 0
#
# Requirements:
#   - Must use a loop
#   - Must return an integer
#   - Do NOT print anything
#
def count_value(d: dict, target) -> int:
    count = 0
    for key in d:
        if d[key] == target:
         count += 1
    return count


# -------------------------------------------------
# find_max_key
# -------------------------------------------------
# find_max_key takes a dictionary with integer values
# and returns the key that has the largest value.
#
# Examples:
#   find_max_key({"a": 1, "b": 5, "c": 3}) -> "b"
#   find_max_key({"x": 10}) -> "x"
#
# Requirements:
#   - Must use a loop
#   - Do NOT use the built-in max() function
#   - Assume the dictionary is not empty
#   - Do NOT print anything
#
def find_max_key(d: dict):
  for key in d:
     if d[key] == max(d.values()):
        return key
    
    


# -------------------------------------------------
# invert_dictionary
# -------------------------------------------------
# invert_dictionary takes a dictionary and returns
# a new dictionary where the keys and values are swapped.
#
# Examples:
#   invert_dictionary({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
#   invert_dictionary({"x": 10}) -> {10: "x"}
#
# Requirements:
#   - Must create and return a new dictionary
#   - Assume all values are unique
#   - Do NOT print anything
#
def invert_dictionary(d: dict) -> dict:
    new_dict = {}
    for key in d:
        new_dict[d[key]] = key
    return new_dict     