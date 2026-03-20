# 07 — Errors and Exceptions
# Exercises

# ============================================================
# Exercise 1 — Basic try-except
# The function below crashes on bad input. Wrap it with
# try-except to handle:
# - ValueError: if the input cannot be converted to float
# - ZeroDivisionError: if the divisor is zero
# In both cases, print a descriptive message and return None.
#
# Test with: ("10", "2"), ("abc", "2"), ("10", "0")
# ============================================================


def safe_divide(a_str, b_str):
    a = float(a_str)
    b = float(b_str)
    return a / b


# Your code here — rewrite safe_divide with error handling


# ============================================================
# Exercise 2 — Multiple exceptions and execution flow
# Predict the output of each block before running it.
# Then run it and check your predictions.
# Add a comment with your prediction above each block.
#
# Block A:
try:
    x = int("42")
    y = x / 0
    print("A: success")
except ValueError:
    print("A: ValueError")
except ZeroDivisionError:
    print("A: ZeroDivisionError")
finally:
    print("A: finally")

# Block B:
try:
    items = [1, 2, 3]
    print(items[1])
except IndexError:
    print("B: IndexError")
else:
    print("B: else")
finally:
    print("B: finally")

# Block C:
try:
    data = {"key": "value"}
    print(data["missing"])
except KeyError as e:
    print(f"C: KeyError — {e}")
except Exception as e:
    print(f"C: Exception — {e}")


# ============================================================
# Exercise 3 — Input validation with raise
# Write a function register_user(name, age, email) that:
# - Raises ValueError if name is empty or only whitespace
# - Raises TypeError if age is not an integer
# - Raises ValueError if age is not between 0 and 120
# - Raises ValueError if email does not contain "@"
# - Returns a dict with the user data if all checks pass
#
# Test it with valid and invalid inputs using try-except.
# ============================================================

# Your code here


# ============================================================
# Exercise 4 — Custom exceptions
# Create a custom exception hierarchy for a simple API client:
# - APIError (base class)
# - RateLimitError (inherits from APIError) — includes retry_after in seconds
# - InvalidResponseError (inherits from APIError) — includes status_code
#
# Write a function simulate_api_call(status_code) that:
# - Returns "OK" if status_code is 200
# - Raises RateLimitError(retry_after=60) if status_code is 429
# - Raises InvalidResponseError(status_code) for any other code
#
# Call it with 200, 429 and 500, handling each case appropriately.
# ============================================================

# Your code here


# ============================================================
# Exercise 5 — Context managers
# Part A: Rewrite the following code using a context manager.
#
# f = open("sample.txt", "w")
# try:
#     f.write("Hello from Python\n")
#     f.write("Second line\n")
# finally:
#     f.close()
#
# Part B: Then read the file back using a context manager
# and print each line with its line number (1-indexed).
# ============================================================

# Your code here


# ============================================================
# Exercise 6 — Robust data processing
# Given the list of raw records below, process each one:
# - Convert "price" to float and "quantity" to int
# - Skip any record where conversion fails (use continue)
# - Skip any record where price <= 0 or quantity <= 0
# - For valid records, compute total = price * quantity
# - Collect valid records in a list and print a summary at the end
#
# raw_records = [
#     {"product": "laptop", "price": "999.99", "quantity": "5"},
#     {"product": "mouse", "price": "abc", "quantity": "10"},
#     {"product": "monitor", "price": "349.50", "quantity": "0"},
#     {"product": "keyboard", "price": "79.99", "quantity": "3"},
#     {"product": "headset", "price": "-1", "quantity": "2"},
#     {"product": "webcam", "price": "89.99", "quantity": "7"},
# ]
# ============================================================

raw_records = [
    {"product": "laptop", "price": "999.99", "quantity": "5"},
    {"product": "mouse", "price": "abc", "quantity": "10"},
    {"product": "monitor", "price": "349.50", "quantity": "0"},
    {"product": "keyboard", "price": "79.99", "quantity": "3"},
    {"product": "headset", "price": "-1", "quantity": "2"},
    {"product": "webcam", "price": "89.99", "quantity": "7"},
]

# Your code here


# ============================================================
# Exercise 7 — assert
# Write a function matrix_multiply(a, b) that multiplies
# two matrices (lists of lists). Before computing, use assert
# to verify:
# - Both inputs are non-empty lists
# - All rows in each matrix have the same length
# - The number of columns in a equals the number of rows in b
#
# Implement the multiplication and test with valid and
# invalid inputs. Catch AssertionError in your test calls.
#
# Example:
# a = [[1, 2], [3, 4]]
# b = [[5, 6], [7, 8]]
# result = [[19, 22], [43, 50]]
# ============================================================

# Your code here
