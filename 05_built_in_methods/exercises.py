# 05 — Built-in Methods
# Exercises

# ============================================================
# Exercise 1 — String cleaning and validation
# Given the raw user inputs below, clean and validate each one:
# - Strip whitespace and convert email to lowercase
# - Strip whitespace and capitalise the name properly
# - Check if the age string is a valid digit before converting
#
# raw_email = "  USER@EXAMPLE.COM  "
# raw_name = "  javi garcía  "
# raw_age = "  29  "
# ============================================================

raw_email = "  USER@EXAMPLE.COM  "
raw_name = "  javi garcía  "
raw_age = "  29  "

# Your code here


# ============================================================
# Exercise 2 — String searching
# Given the text below:
# - Count how many times "python" appears (case-insensitive)
# - Find the index of the first occurrence of "engineer"
# - Check if the text starts with "becoming"
# - Check if the text ends with any of: ".pdf", ".txt", "engineer"
#
# text = "Becoming a Python engineer. Python engineers are in high demand."
# ============================================================

text = "Becoming a Python engineer. Python engineers are in high demand."

# Your code here


# ============================================================
# Exercise 3 — Split and join
# Given the CSV line below:
# - Split it into a list of values
# - Strip any extra whitespace from each value
# - Rebuild it as a clean CSV line with no extra spaces
# - Print the number of fields
#
# csv_line = "name ,  age , city ,  role  , department"
# ============================================================

csv_line = "name ,  age , city ,  role  , department"

# Your code here


# ============================================================
# Exercise 4 — f-string formatting
# Format and print the following data using f-strings:
# - Full name right-aligned in a field of width 20
# - Price with 2 decimal places and thousands separator
# - Conversion rate as a percentage with 1 decimal place
# - A progress bar like: "Progress: [=====     ] 50%"
#   (10 chars wide, filled with = for done, space for remaining)
#
# name = "Ada Lovelace"
# price = 9875432.5
# rate = 0.7348
# progress = 0.5
# ============================================================

name = "Ada Lovelace"
price = 9875432.5
rate = 0.7348
progress = 0.5

# Your code here


# ============================================================
# Exercise 5 — Sorting with key
# Given the list of products below:
# - Sort by price (ascending)
# - Sort by name alphabetically (case-insensitive)
# - Sort by stock (descending)
# - Print each sorted result
#
# products = [
#     {"name": "Laptop", "price": 999.99, "stock": 5},
#     {"name": "monitor", "price": 349.50, "stock": 12},
#     {"name": "Keyboard", "price": 79.99, "stock": 30},
#     {"name": "mouse", "price": 29.99, "stock": 8},
#     {"name": "Headset", "price": 149.99, "stock": 20},
# ]
# ============================================================

products = [
    {"name": "Laptop", "price": 999.99, "stock": 5},
    {"name": "monitor", "price": 349.50, "stock": 12},
    {"name": "Keyboard", "price": 79.99, "stock": 30},
    {"name": "mouse", "price": 29.99, "stock": 8},
    {"name": "Headset", "price": 149.99, "stock": 20},
]

# Your code here


# ============================================================
# Exercise 6 — setdefault
# Given the list of log entries below, group them by level
# using setdefault(). The result should be a dictionary where
# each key is a log level and each value is a list of messages.
#
# logs = [
#     ("INFO", "Server started"),
#     ("ERROR", "Connection failed"),
#     ("INFO", "Request received"),
#     ("WARNING", "High memory usage"),
#     ("ERROR", "Timeout exceeded"),
#     ("INFO", "Request completed"),
# ]
# ============================================================

logs = [
    ("INFO", "Server started"),
    ("ERROR", "Connection failed"),
    ("INFO", "Request received"),
    ("WARNING", "High memory usage"),
    ("ERROR", "Timeout exceeded"),
    ("INFO", "Request completed"),
]

# Your code here


# ============================================================
# Exercise 7 — fromkeys and common mistakes
# Part A: Create a dictionary from the keys below
# with a default value of 0.
#
# metrics = ["clicks", "impressions", "conversions", "revenue"]
#
# Part B: The code below has a bug — all keys share the
# same list. Fix it so each key gets its own independent list.
#
# broken = dict.fromkeys(["a", "b", "c"], [])
# broken["a"].append(1)
# print(broken)  # should be {'a': [1], 'b': [], 'c': []}
# ============================================================

metrics = ["clicks", "impressions", "conversions", "revenue"]

# Your code here


# ============================================================
# Exercise 8 — In-place set operations
# Given the two sets below, use in-place operators to:
# - Add all elements of b into a (union in-place)
# - Print a, then reset both sets to their original values
# - Keep only elements common to both (intersection in-place)
# - Print a, then reset both sets to their original values
# - Remove from a any element that is also in b (difference in-place)
# - Print a
#
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# ============================================================

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Your code here
