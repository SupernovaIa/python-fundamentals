# 08 — Functions
# Exercises

# ============================================================
# Exercise 1 — Basic functions and return
# Write a function bmi(weight_kg, height_m) that:
# - Computes BMI = weight / height^2
# - Returns a tuple (bmi_value, category) where category is:
#   "Underweight" if bmi < 18.5
#   "Normal"      if 18.5 <= bmi < 25
#   "Overweight"  if 25 <= bmi < 30
#   "Obese"       if bmi >= 30
# - Raises ValueError if weight or height are <= 0
# Include a proper docstring.
#
# Test with: (70, 1.75), (50, 1.75), (100, 1.75), (0, 1.75)
# ============================================================

# Your code here


# ============================================================
# Exercise 2 — Default and keyword arguments
# Write a function format_price(amount, currency="EUR",
# decimals=2, show_symbol=True) that returns a formatted
# price string.
#
# Expected outputs:
# format_price(1234.5)                    → "€1,234.50"
# format_price(1234.5, currency="USD")    → "$1,234.50"
# format_price(1234.5, show_symbol=False) → "1,234.50 EUR"
# format_price(1234.5, decimals=0)        → "€1,235"
#
# Currency symbols: EUR → €, USD → $, GBP → £, default → currency code
# ============================================================

# Your code here


# ============================================================
# Exercise 3 — Mutable default value bug
# The function below has the classic mutable default bug.
# - Run it as-is and observe the problem
# - Fix it
# - Add a second parameter allow_duplicates=False that,
#   when False, skips items already in the history
#
# def add_to_history(item, history=[]):
#     history.append(item)
#     return history
# ============================================================


def add_to_history(item, history=[]):
    history.append(item)
    return history


# Your code here


# ============================================================
# Exercise 4 — *args and **kwargs
# Part A: Write a function stats(*numbers) that accepts any
# number of numeric arguments and returns a dict with:
# count, sum, min, max, average
# Handle the case where no arguments are passed.
#
# Part B: Write a function build_profile(name, **attributes)
# that returns a dict with "name" plus all extra attributes.
# Example: build_profile("Javi", age=29, role="AI Engineer")
# → {"name": "Javi", "age": 29, "role": "AI Engineer"}
# ============================================================

# Your code here


# ============================================================
# Exercise 5 — Scope and LEGB
# Predict the output of each block before running it.
# Then run and check. Add your prediction as a comment.
#
# Block A:
x = "global"


def outer():
    x = "enclosing"

    def inner():
        print(x)

    inner()


outer()
print(x)

# Block B:
total = 0


def add(n):
    total = total + n  # What happens here?
    return total


try:
    print(add(5))
except Exception as e:
    print(f"Error: {e}")


# Block C:
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = make_counter()
print(counter())
print(counter())
print(counter())
# ============================================================


# ============================================================
# Exercise 6 — Lambda, map, filter
# Given the list of orders below:
# - Use map to add a 21% VAT to each price
# - Use filter to keep only orders with final price > 100
# - Use sorted with a lambda to sort by final price descending
# - Do all three steps as a pipeline (chain them together)
# - Print the final sorted list
#
# orders = [
#     {"product": "laptop", "price": 999.99},
#     {"product": "mouse", "price": 29.99},
#     {"product": "monitor", "price": 349.50},
#     {"product": "keyboard", "price": 79.99},
#     {"product": "usb hub", "price": 19.99},
#     {"product": "headset", "price": 149.99},
# ]
# ============================================================

orders = [
    {"product": "laptop", "price": 999.99},
    {"product": "mouse", "price": 29.99},
    {"product": "monitor", "price": 349.50},
    {"product": "keyboard", "price": 79.99},
    {"product": "usb hub", "price": 19.99},
    {"product": "headset", "price": 149.99},
]

# Your code here


# ============================================================
# Exercise 7 — Decorators
# Part A: Write a decorator log_call that prints the function
# name, its arguments and its return value every time it
# is called. Use functools.wraps.
#
# Part B: Write a decorator retry(times=3) that retries a
# function up to N times if it raises an exception.
# Print a message on each failed attempt.
# If all attempts fail, re-raise the last exception.
#
# Test retry with a function that randomly fails.
# ============================================================

import functools
import random

# Your code here


# ============================================================
# Exercise 8 — Generators
# Part A: Write a generator fibonacci() that yields Fibonacci
# numbers indefinitely. Use it to print the first 15 terms.
#
# Part B: Write a generator read_in_chunks(data, chunk_size)
# that yields successive chunks of a list.
# Example: read_in_chunks([1..10], 3) →
#   [1, 2, 3], [4, 5, 6], [7, 8, 9], [10]
#
# Part C: Write a generator pipeline that:
# 1. Generates numbers from 1 to 1000
# 2. Filters only those divisible by 3
# 3. Squares each one
# Chain these as generator expressions and print the sum.
# ============================================================

# Your code here
